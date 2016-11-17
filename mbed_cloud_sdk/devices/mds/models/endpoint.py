# coding: utf-8

"""
    mbed Cloud Connect REST API

    mbed Cloud Connect REST API allows web applications to communicate with devices.

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Endpoint(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, status=None, q=None, type=None, name=None):
        """
        Endpoint - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'status': 'str',
            'q': 'bool',
            'type': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'status': 'status',
            'q': 'q',
            'type': 'type',
            'name': 'name'
        }

        self._status = status
        self._q = q
        self._type = type
        self._name = name

    @property
    def status(self):
        """
        Gets the status of this Endpoint.
        Possible values ACTIVE, STALE.

        :return: The status of this Endpoint.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Endpoint.
        Possible values ACTIVE, STALE.

        :param status: The status of this Endpoint.
        :type: str
        """

        self._status = status

    @property
    def q(self):
        """
        Gets the q of this Endpoint.
        Determines whether the device is in queue mode.  <br/><br/><b>Queue mode</b><br/> When an endpoint is in queue mode, messages sent to the endpoint do not wake up the physical device.  The messages are queued and delivered when the device wakes up and connects to mbed Cloud Connect  itself. You can also use the Queue mode when the device is behind a NAT and cannot be reached directly by  mbed Cloud Connect. 

        :return: The q of this Endpoint.
        :rtype: bool
        """
        return self._q

    @q.setter
    def q(self, q):
        """
        Sets the q of this Endpoint.
        Determines whether the device is in queue mode.  <br/><br/><b>Queue mode</b><br/> When an endpoint is in queue mode, messages sent to the endpoint do not wake up the physical device.  The messages are queued and delivered when the device wakes up and connects to mbed Cloud Connect  itself. You can also use the Queue mode when the device is behind a NAT and cannot be reached directly by  mbed Cloud Connect. 

        :param q: The q of this Endpoint.
        :type: bool
        """

        self._q = q

    @property
    def type(self):
        """
        Gets the type of this Endpoint.
        Type of endpoint. (Free text)

        :return: The type of this Endpoint.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Endpoint.
        Type of endpoint. (Free text)

        :param type: The type of this Endpoint.
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """
        Gets the name of this Endpoint.
        Unique identifier representing the endpoint.

        :return: The name of this Endpoint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Endpoint.
        Unique identifier representing the endpoint.

        :param name: The name of this Endpoint.
        :type: str
        """

        self._name = name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
