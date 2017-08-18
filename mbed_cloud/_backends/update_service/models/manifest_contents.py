# coding: utf-8

"""
    Update Service API

    This is the API Documentation for the mbed deployment service which is part of the update service.

    OpenAPI spec version: 3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ManifestContents(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, class_id=None, vendor_id=None, manifest_version=None, description=None, nonce=None, timestamp=None, encryption_mode=None, apply_immediately=None, device_id=None, payload=None):
        """
        ManifestContents - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'class_id': 'str',
            'vendor_id': 'str',
            'manifest_version': 'int',
            'description': 'str',
            'nonce': 'str',
            'timestamp': 'int',
            'encryption_mode': 'ManifestContentsEncryptionMode',
            'apply_immediately': 'bool',
            'device_id': 'str',
            'payload': 'ManifestContentsPayload'
        }

        self.attribute_map = {
            'class_id': 'classId',
            'vendor_id': 'vendorId',
            'manifest_version': 'manifestVersion',
            'description': 'description',
            'nonce': 'nonce',
            'timestamp': 'timestamp',
            'encryption_mode': 'encryptionMode',
            'apply_immediately': 'applyImmediately',
            'device_id': 'deviceId',
            'payload': 'payload'
        }

        self._class_id = class_id
        self._vendor_id = vendor_id
        self._manifest_version = manifest_version
        self._description = description
        self._nonce = nonce
        self._timestamp = timestamp
        self._encryption_mode = encryption_mode
        self._apply_immediately = apply_immediately
        self._device_id = device_id
        self._payload = payload

    @property
    def class_id(self):
        """
        Gets the class_id of this ManifestContents.
        Hex representation of the 128-bit RFC4122 GUID that represents the device class that the update targets.

        :return: The class_id of this ManifestContents.
        :rtype: str
        """
        return self._class_id

    @class_id.setter
    def class_id(self, class_id):
        """
        Sets the class_id of this ManifestContents.
        Hex representation of the 128-bit RFC4122 GUID that represents the device class that the update targets.

        :param class_id: The class_id of this ManifestContents.
        :type: str
        """

        self._class_id = class_id

    @property
    def vendor_id(self):
        """
        Gets the vendor_id of this ManifestContents.
        Hex representation of the 128-bit RFC4122 GUID that represents the vendor.

        :return: The vendor_id of this ManifestContents.
        :rtype: str
        """
        return self._vendor_id

    @vendor_id.setter
    def vendor_id(self, vendor_id):
        """
        Sets the vendor_id of this ManifestContents.
        Hex representation of the 128-bit RFC4122 GUID that represents the vendor.

        :param vendor_id: The vendor_id of this ManifestContents.
        :type: str
        """

        self._vendor_id = vendor_id

    @property
    def manifest_version(self):
        """
        Gets the manifest_version of this ManifestContents.
        The version of the manifest format being used.

        :return: The manifest_version of this ManifestContents.
        :rtype: int
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        """
        Sets the manifest_version of this ManifestContents.
        The version of the manifest format being used.

        :param manifest_version: The manifest_version of this ManifestContents.
        :type: int
        """

        self._manifest_version = manifest_version

    @property
    def description(self):
        """
        Gets the description of this ManifestContents.
        A short description of the update.

        :return: The description of this ManifestContents.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ManifestContents.
        A short description of the update.

        :param description: The description of this ManifestContents.
        :type: str
        """

        self._description = description

    @property
    def nonce(self):
        """
        Gets the nonce of this ManifestContents.
        A 128-bit random field. This is provided by the manifest tool to ensure that the signing algorithm is safe from timing side-channel attacks.

        :return: The nonce of this ManifestContents.
        :rtype: str
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce):
        """
        Sets the nonce of this ManifestContents.
        A 128-bit random field. This is provided by the manifest tool to ensure that the signing algorithm is safe from timing side-channel attacks.

        :param nonce: The nonce of this ManifestContents.
        :type: str
        """

        self._nonce = nonce

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ManifestContents.
        The time the manifest was created. The timestamp is stored as Unix time.

        :return: The timestamp of this ManifestContents.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ManifestContents.
        The time the manifest was created. The timestamp is stored as Unix time.

        :param timestamp: The timestamp of this ManifestContents.
        :type: int
        """

        self._timestamp = timestamp

    @property
    def encryption_mode(self):
        """
        Gets the encryption_mode of this ManifestContents.

        :return: The encryption_mode of this ManifestContents.
        :rtype: ManifestContentsEncryptionMode
        """
        return self._encryption_mode

    @encryption_mode.setter
    def encryption_mode(self, encryption_mode):
        """
        Sets the encryption_mode of this ManifestContents.

        :param encryption_mode: The encryption_mode of this ManifestContents.
        :type: ManifestContentsEncryptionMode
        """

        self._encryption_mode = encryption_mode

    @property
    def apply_immediately(self):
        """
        Gets the apply_immediately of this ManifestContents.
        A flag that indicates that the update described by the manifest should be applied as soon as possible.

        :return: The apply_immediately of this ManifestContents.
        :rtype: bool
        """
        return self._apply_immediately

    @apply_immediately.setter
    def apply_immediately(self, apply_immediately):
        """
        Sets the apply_immediately of this ManifestContents.
        A flag that indicates that the update described by the manifest should be applied as soon as possible.

        :param apply_immediately: The apply_immediately of this ManifestContents.
        :type: bool
        """

        self._apply_immediately = apply_immediately

    @property
    def device_id(self):
        """
        Gets the device_id of this ManifestContents.
        Hex representation of the 128-bit RFC4122 GUID that uniquely identifies the device. Each device has a single, unique device ID.

        :return: The device_id of this ManifestContents.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this ManifestContents.
        Hex representation of the 128-bit RFC4122 GUID that uniquely identifies the device. Each device has a single, unique device ID.

        :param device_id: The device_id of this ManifestContents.
        :type: str
        """

        self._device_id = device_id

    @property
    def payload(self):
        """
        Gets the payload of this ManifestContents.

        :return: The payload of this ManifestContents.
        :rtype: ManifestContentsPayload
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """
        Sets the payload of this ManifestContents.

        :param payload: The payload of this ManifestContents.
        :type: ManifestContentsPayload
        """

        self._payload = payload

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
        if not isinstance(other, ManifestContents):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
