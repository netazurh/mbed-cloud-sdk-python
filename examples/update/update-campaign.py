"""Example: Listing and creating update campaigns."""
# -*- coding: utf-8 -*-
from mbed_cloud.devices import DeviceAPI
from mbed_cloud.update import UpdateAPI
import os
import random
import string
import sys


def _read_file(f):
    fh = open(f)
    d = fh.read()
    fh.close()
    return d


def _rand_id(N=6):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))


def _print_manifests(mresp):
    num_manifests = mresp.count()
    if num_manifests == 0:
        print("No manifests found.")
        return

    header = "Manifests (%d)" % (num_manifests)
    print("%s\n%s" % (header, "-" * len(header)))
    for m, idx in mresp.iteritems():
        print("%s | %s | %s" % (m.name, m.datafile, m.created_at.strftime("%Y-%m-%d %H:%M:%S")))


def _print_manifest_details(m):
    detail_props = ['description', 'deviceId', 'classId']
    details = map(lambda p: "\t- %s: %s" % (p, m.manifest_contents.get(p, "-")), detail_props)
    print("\n".join(details))
    print("")


def _main():
    update_api = UpdateAPI()

    # Read manifest from first argument on command line
    if len(sys.argv) < 2:
        raise ValueError("No manifest filename found on command line")
    filename = os.path.abspath(sys.argv[1])

    # Upload manifest
    mobj = update_api.upload_manifest(
        name="Auto manifest %s" % _rand_id(),
        datafile=filename,
        description="Manifest uploaded using mbed cloud SDK")
    print("Successfully uploaded manifest %r\n\tURL: %s\nProperties:" % (mobj.name, mobj.datafile))
    _print_manifest_details(mobj)

    # List all manifests currently uploaded
    mresp = update_api.list_manifests(limit=10)
    _print_manifests(mresp)

    # List all filters
    device_api = DeviceAPI()
    fresp = device_api.list_filters()
    header = "Current filters:"
    print("\n%s\n%s" % (header, "-" * len(header)))
    if fresp.count() == 0:
        print("No filters created. Please create one to apply the update on.")
        sys.exit(1)
    filters = [f for f, idx in fresp.iteritems()]
    print("\n".join(["\t- %s" % (f.name) for f in filters]))
    selected_filter = random.choice(filters)
    print("Randomly chose %r for applying update" % (selected_filter.name))

    # Create update campaign. For this step we need three pieces of information:
    # 1. The name of the update campaign (we auto-generate this)
    # 2. What manifest to use for running the update
    # 3. What devices we should apply the updat on (i.e. the filter to use)
    campaign_name = _rand_id()
    update_api.create_update_campaign()


if __name__ == '__main__':
    _main()
