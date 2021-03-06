import logging
import os
import shlex
import subprocess
import sys
import time

from threading import Timer

import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from tests.common import BaseCase

from xml.etree import ElementTree

LOG = logging.getLogger(__name__)


def timeout_check_output(timeout=5, process=None, _or_fail=True, *args, **kwargs):
    """This is a Py2/3 replacement for timeout

    Uses a thread to kill the subprocess if it's not finished after the timeout
    """
    process = process or subprocess.Popen(
        *args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        **kwargs
    )

    stdout = '<no output collected>'
    now = time.time()

    def killer():
        # called by timer thread to terminate process
        process.timed_out = time.time() - now
        process.kill()

    timer = Timer(timeout, killer)
    timer.start()
    try:
        stdout, stderr = process.communicate()
    finally:
        timer.cancel()
    status_code = process.poll()
    if _or_fail and status_code != 0:
        timed_out = getattr(process, 'timed_out', '')
        raise subprocess.CalledProcessError(
            status_code,
            (timed_out and '<TIMED OUT (%.2fs)>\'' % timed_out) + str(kwargs.get('args', args)),
            output=stdout
        )
    return stdout


def new_server_process(coverage=True):
    exe = sys.executable
    target = os.path.join(os.path.dirname(__file__), 'server.py')
    cmd = [exe, '-u']
    if coverage:
        cmd.extend(['-m', 'coverage', 'run'])
    cmd.append(target)
    LOG.info('starting new test server: `%s`', cmd)
    process = subprocess.Popen(args=cmd, universal_newlines=True)
    try:
        # ping the server to make sure it's up
        test_server_local_address = 'http://127.0.0.1:5000'
        url = '%s/ping' % test_server_local_address
        s = requests.Session()
        s.mount(url, adapter=HTTPAdapter(max_retries=Retry(total=20, connect=5, read=15, backoff_factor=0.5)))
        response = s.get(url, timeout=(15, 15))
        response.raise_for_status()
    except Exception as e:
        LOG.error('could not reach test server locally: %s\n%s' % (cmd, e))
        LOG.info('server status', process.poll(), process.pid)
        LOG.info(timeout_check_output(args=shlex.split('ps -aux')))
        LOG.info(timeout_check_output(args=shlex.split('netstat -aon')))
        raise
    else:
        LOG.info('SDK test server is running locally on %s' % (test_server_local_address,))
    return process


class TestWithRPC(BaseCase):

    process = None

    def setUp(self):
        self.process = new_server_process()
        logging.basicConfig(level=logging.INFO)

    def test_run(self):
        timeout_check_output(process=self.process, timeout=9*60)
        self.process.wait()
        LOG.info('Test server was shut down')

        # now go to the rpc test result directory and load outcome
        for i in range(10):
            if os.path.exists('results/results.xml'):
                break
            time.sleep(0.2)
        else:
            raise IOError('could not find integration results')

        self.outcome = ElementTree.parse('results/results.xml').getroot().attrib

        for outcome in {'errors', 'failures'}:
            remote_value = int(self.outcome.get(outcome, 0))
            if remote_value:
                self.fail('Remote test had %s %s' % (remote_value, outcome))
