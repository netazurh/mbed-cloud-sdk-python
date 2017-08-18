# coding: utf-8

"""
    Device Directory API

    This is the API Documentation for the mbed device directory update service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DeviceDataPatchRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, description=None, endpoint_name=None, auto_update=None, host_gateway=None, object=None, custom_attributes=None, device_key=None, endpoint_type=None, ca_id=None, name=None):
        """
        DeviceDataPatchRequest - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'endpoint_name': 'str',
            'auto_update': 'bool',
            'host_gateway': 'str',
            'object': 'str',
            'custom_attributes': 'object',
            'device_key': 'str',
            'endpoint_type': 'str',
            'ca_id': 'str',
            'name': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'endpoint_name': 'endpoint_name',
            'auto_update': 'auto_update',
            'host_gateway': 'host_gateway',
            'object': 'object',
            'custom_attributes': 'custom_attributes',
            'device_key': 'device_key',
            'endpoint_type': 'endpoint_type',
            'ca_id': 'ca_id',
            'name': 'name'
        }

        self._description = description
        self._endpoint_name = endpoint_name
        self._auto_update = auto_update
        self._host_gateway = host_gateway
        self._object = object
        self._custom_attributes = custom_attributes
        self._device_key = device_key
        self._endpoint_type = endpoint_type
        self._ca_id = ca_id
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this DeviceDataPatchRequest.
        The description of the device.

        :return: The description of this DeviceDataPatchRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DeviceDataPatchRequest.
        The description of the device.

        :param description: The description of this DeviceDataPatchRequest.
        :type: str
        """

        self._description = description

    @property
    def endpoint_name(self):
        """
        Gets the endpoint_name of this DeviceDataPatchRequest.
        The endpoint name given to the device.

        :return: The endpoint_name of this DeviceDataPatchRequest.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """
        Sets the endpoint_name of this DeviceDataPatchRequest.
        The endpoint name given to the device.

        :param endpoint_name: The endpoint_name of this DeviceDataPatchRequest.
        :type: str
        """
        if endpoint_name is not None and len(endpoint_name) > 64:
            raise ValueError("Invalid value for `endpoint_name`, length must be less than or equal to `64`")

        self._endpoint_name = endpoint_name

    @property
    def auto_update(self):
        """
        Gets the auto_update of this DeviceDataPatchRequest.
        DEPRECATED Mark this device for auto firmware update.

        :return: The auto_update of this DeviceDataPatchRequest.
        :rtype: bool
        """
        return self._auto_update

    @auto_update.setter
    def auto_update(self, auto_update):
        """
        Sets the auto_update of this DeviceDataPatchRequest.
        DEPRECATED Mark this device for auto firmware update.

        :param auto_update: The auto_update of this DeviceDataPatchRequest.
        :type: bool
        """

        self._auto_update = auto_update

    @property
    def host_gateway(self):
        """
        Gets the host_gateway of this DeviceDataPatchRequest.
        The endpoint_name of the host gateway, if appropriate.

        :return: The host_gateway of this DeviceDataPatchRequest.
        :rtype: str
        """
        return self._host_gateway

    @host_gateway.setter
    def host_gateway(self, host_gateway):
        """
        Sets the host_gateway of this DeviceDataPatchRequest.
        The endpoint_name of the host gateway, if appropriate.

        :param host_gateway: The host_gateway of this DeviceDataPatchRequest.
        :type: str
        """

        self._host_gateway = host_gateway

    @property
    def object(self):
        """
        Gets the object of this DeviceDataPatchRequest.
        The API resource entity.

        :return: The object of this DeviceDataPatchRequest.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this DeviceDataPatchRequest.
        The API resource entity.

        :param object: The object of this DeviceDataPatchRequest.
        :type: str
        """

        self._object = object

    @property
    def custom_attributes(self):
        """
        Gets the custom_attributes of this DeviceDataPatchRequest.
        Up to 5 custom JSON attributes

        :return: The custom_attributes of this DeviceDataPatchRequest.
        :rtype: object
        """
        return self._custom_attributes

    @custom_attributes.setter
    def custom_attributes(self, custom_attributes):
        """
        Sets the custom_attributes of this DeviceDataPatchRequest.
        Up to 5 custom JSON attributes

        :param custom_attributes: The custom_attributes of this DeviceDataPatchRequest.
        :type: object
        """

        self._custom_attributes = custom_attributes

    @property
    def device_key(self):
        """
        Gets the device_key of this DeviceDataPatchRequest.
        Fingerprint of the device certificate.

        :return: The device_key of this DeviceDataPatchRequest.
        :rtype: str
        """
        return self._device_key

    @device_key.setter
    def device_key(self, device_key):
        """
        Sets the device_key of this DeviceDataPatchRequest.
        Fingerprint of the device certificate.

        :param device_key: The device_key of this DeviceDataPatchRequest.
        :type: str
        """
        if device_key is not None and len(device_key) > 512:
            raise ValueError("Invalid value for `device_key`, length must be less than or equal to `512`")

        self._device_key = device_key

    @property
    def endpoint_type(self):
        """
        Gets the endpoint_type of this DeviceDataPatchRequest.
        The endpoint type of the device - e.g. if the device is a gateway.

        :return: The endpoint_type of this DeviceDataPatchRequest.
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        """
        Sets the endpoint_type of this DeviceDataPatchRequest.
        The endpoint type of the device - e.g. if the device is a gateway.

        :param endpoint_type: The endpoint_type of this DeviceDataPatchRequest.
        :type: str
        """
        if endpoint_type is not None and len(endpoint_type) > 64:
            raise ValueError("Invalid value for `endpoint_type`, length must be less than or equal to `64`")

        self._endpoint_type = endpoint_type

    @property
    def ca_id(self):
        """
        Gets the ca_id of this DeviceDataPatchRequest.
        ID of the issuer of the certificate.

        :return: The ca_id of this DeviceDataPatchRequest.
        :rtype: str
        """
        return self._ca_id

    @ca_id.setter
    def ca_id(self, ca_id):
        """
        Sets the ca_id of this DeviceDataPatchRequest.
        ID of the issuer of the certificate.

        :param ca_id: The ca_id of this DeviceDataPatchRequest.
        :type: str
        """
        if ca_id is not None and len(ca_id) > 500:
            raise ValueError("Invalid value for `ca_id`, length must be less than or equal to `500`")

        self._ca_id = ca_id

    @property
    def name(self):
        """
        Gets the name of this DeviceDataPatchRequest.
        The name of the device.

        :return: The name of this DeviceDataPatchRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DeviceDataPatchRequest.
        The name of the device.

        :param name: The name of this DeviceDataPatchRequest.
        :type: str
        """
        if name is not None and len(name) > 128:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `128`")

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
        if not isinstance(other, DeviceDataPatchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
