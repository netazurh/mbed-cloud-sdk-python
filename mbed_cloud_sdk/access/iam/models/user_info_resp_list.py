# coding: utf-8

"""
    IAM Identities REST API

    REST API to manage accounts, groups, users and api-keys

    OpenAPI spec version: v3
    
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


class UserInfoRespList(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, after=None, object=None, total_count=None, limit=None, data=None, order=None):
        """
        UserInfoRespList - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'after': 'str',
            'object': 'str',
            'total_count': 'int',
            'limit': 'int',
            'data': 'list[UserInfoResp]',
            'order': 'str'
        }

        self.attribute_map = {
            'after': 'after',
            'object': 'object',
            'total_count': 'totalCount',
            'limit': 'limit',
            'data': 'data',
            'order': 'order'
        }

        self._after = after
        self._object = object
        self._total_count = total_count
        self._limit = limit
        self._data = data
        self._order = order

    @property
    def after(self):
        """
        Gets the after of this UserInfoRespList.
        The entity id to fetch after it.

        :return: The after of this UserInfoRespList.
        :rtype: str
        """
        return self._after

    @after.setter
    def after(self, after):
        """
        Sets the after of this UserInfoRespList.
        The entity id to fetch after it.

        :param after: The after of this UserInfoRespList.
        :type: str
        """

        self._after = after

    @property
    def object(self):
        """
        Gets the object of this UserInfoRespList.
        entity name: always 'list'

        :return: The object of this UserInfoRespList.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this UserInfoRespList.
        entity name: always 'list'

        :param object: The object of this UserInfoRespList.
        :type: str
        """
        allowed_values = ["user", "apikey", "group", "account", "list", "error"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def total_count(self):
        """
        Gets the total_count of this UserInfoRespList.
        The total number or records, if requested 

        :return: The total_count of this UserInfoRespList.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """
        Sets the total_count of this UserInfoRespList.
        The total number or records, if requested 

        :param total_count: The total_count of this UserInfoRespList.
        :type: int
        """

        self._total_count = total_count

    @property
    def limit(self):
        """
        Gets the limit of this UserInfoRespList.
        The number of results to return, (range: 2-1000), or equals to total_count

        :return: The limit of this UserInfoRespList.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this UserInfoRespList.
        The number of results to return, (range: 2-1000), or equals to total_count

        :param limit: The limit of this UserInfoRespList.
        :type: int
        """

        self._limit = limit

    @property
    def data(self):
        """
        Gets the data of this UserInfoRespList.
        List of entities.

        :return: The data of this UserInfoRespList.
        :rtype: list[UserInfoResp]
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this UserInfoRespList.
        List of entities.

        :param data: The data of this UserInfoRespList.
        :type: list[UserInfoResp]
        """

        self._data = data

    @property
    def order(self):
        """
        Gets the order of this UserInfoRespList.
        The order of the records to return. Available values: ASC, DESC. Default value is ASC

        :return: The order of this UserInfoRespList.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this UserInfoRespList.
        The order of the records to return. Available values: ASC, DESC. Default value is ASC

        :param order: The order of this UserInfoRespList.
        :type: str
        """
        allowed_values = ["ASC", "DESC"]
        if order not in allowed_values:
            raise ValueError(
                "Invalid value for `order` ({0}), must be one of {1}"
                .format(order, allowed_values)
            )

        self._order = order

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
