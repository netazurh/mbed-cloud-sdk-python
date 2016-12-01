# coding: utf-8

"""
    Deployment Service API

    This is the API Documentation for the mbed deployment service which is part of the update service.

    OpenAPI spec version: 0.1
    
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


class CampaignDeviceMetadataSerializer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, description=None, campaign=None, created_at=None, object=None, updated_at=None, mechanism=None, name=None, etag=None, mechanism_url=None, deployment_state=None, id=None, device_id=None):
        """
        CampaignDeviceMetadataSerializer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'description': 'str',
            'campaign': 'str',
            'created_at': 'datetime',
            'object': 'str',
            'updated_at': 'datetime',
            'mechanism': 'str',
            'name': 'str',
            'etag': 'datetime',
            'mechanism_url': 'str',
            'deployment_state': 'str',
            'id': 'str',
            'device_id': 'str'
        }

        self.attribute_map = {
            'description': 'description',
            'campaign': 'campaign',
            'created_at': 'created_at',
            'object': 'object',
            'updated_at': 'updated_at',
            'mechanism': 'mechanism',
            'name': 'name',
            'etag': 'etag',
            'mechanism_url': 'mechanism_url',
            'deployment_state': 'deployment_state',
            'id': 'id',
            'device_id': 'device_id'
        }

        self._description = description
        self._campaign = campaign
        self._created_at = created_at
        self._object = object
        self._updated_at = updated_at
        self._mechanism = mechanism
        self._name = name
        self._etag = etag
        self._mechanism_url = mechanism_url
        self._deployment_state = deployment_state
        self._id = id
        self._device_id = device_id

    @property
    def description(self):
        """
        Gets the description of this CampaignDeviceMetadataSerializer.
        The description of the object

        :return: The description of this CampaignDeviceMetadataSerializer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CampaignDeviceMetadataSerializer.
        The description of the object

        :param description: The description of this CampaignDeviceMetadataSerializer.
        :type: str
        """

        self._description = description

    @property
    def campaign(self):
        """
        Gets the campaign of this CampaignDeviceMetadataSerializer.
        The update campaign to which this device belongs

        :return: The campaign of this CampaignDeviceMetadataSerializer.
        :rtype: str
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """
        Sets the campaign of this CampaignDeviceMetadataSerializer.
        The update campaign to which this device belongs

        :param campaign: The campaign of this CampaignDeviceMetadataSerializer.
        :type: str
        """

        self._campaign = campaign

    @property
    def created_at(self):
        """
        Gets the created_at of this CampaignDeviceMetadataSerializer.
        The time the object was created

        :return: The created_at of this CampaignDeviceMetadataSerializer.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this CampaignDeviceMetadataSerializer.
        The time the object was created

        :param created_at: The created_at of this CampaignDeviceMetadataSerializer.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def object(self):
        """
        Gets the object of this CampaignDeviceMetadataSerializer.
        The API resource entity

        :return: The object of this CampaignDeviceMetadataSerializer.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this CampaignDeviceMetadataSerializer.
        The API resource entity

        :param object: The object of this CampaignDeviceMetadataSerializer.
        :type: str
        """

        self._object = object

    @property
    def updated_at(self):
        """
        Gets the updated_at of this CampaignDeviceMetadataSerializer.
        The time the object was updated

        :return: The updated_at of this CampaignDeviceMetadataSerializer.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this CampaignDeviceMetadataSerializer.
        The time the object was updated

        :param updated_at: The updated_at of this CampaignDeviceMetadataSerializer.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def mechanism(self):
        """
        Gets the mechanism of this CampaignDeviceMetadataSerializer.
        The ID of the channel used to communicated with the device

        :return: The mechanism of this CampaignDeviceMetadataSerializer.
        :rtype: str
        """
        return self._mechanism

    @mechanism.setter
    def mechanism(self, mechanism):
        """
        Sets the mechanism of this CampaignDeviceMetadataSerializer.
        The ID of the channel used to communicated with the device

        :param mechanism: The mechanism of this CampaignDeviceMetadataSerializer.
        :type: str
        """

        self._mechanism = mechanism

    @property
    def name(self):
        """
        Gets the name of this CampaignDeviceMetadataSerializer.
        The name of the object

        :return: The name of this CampaignDeviceMetadataSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CampaignDeviceMetadataSerializer.
        The name of the object

        :param name: The name of this CampaignDeviceMetadataSerializer.
        :type: str
        """

        self._name = name

    @property
    def etag(self):
        """
        Gets the etag of this CampaignDeviceMetadataSerializer.
        The entity instance signature

        :return: The etag of this CampaignDeviceMetadataSerializer.
        :rtype: datetime
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this CampaignDeviceMetadataSerializer.
        The entity instance signature

        :param etag: The etag of this CampaignDeviceMetadataSerializer.
        :type: datetime
        """

        self._etag = etag

    @property
    def mechanism_url(self):
        """
        Gets the mechanism_url of this CampaignDeviceMetadataSerializer.
        The address of the Connector to use

        :return: The mechanism_url of this CampaignDeviceMetadataSerializer.
        :rtype: str
        """
        return self._mechanism_url

    @mechanism_url.setter
    def mechanism_url(self, mechanism_url):
        """
        Sets the mechanism_url of this CampaignDeviceMetadataSerializer.
        The address of the Connector to use

        :param mechanism_url: The mechanism_url of this CampaignDeviceMetadataSerializer.
        :type: str
        """

        self._mechanism_url = mechanism_url

    @property
    def deployment_state(self):
        """
        Gets the deployment_state of this CampaignDeviceMetadataSerializer.
        The state of the deployment

        :return: The deployment_state of this CampaignDeviceMetadataSerializer.
        :rtype: str
        """
        return self._deployment_state

    @deployment_state.setter
    def deployment_state(self, deployment_state):
        """
        Sets the deployment_state of this CampaignDeviceMetadataSerializer.
        The state of the deployment

        :param deployment_state: The deployment_state of this CampaignDeviceMetadataSerializer.
        :type: str
        """
        allowed_values = ["pending", "updated_device_catalog", "updated_connector_channel", "deployed", "manifestremoved"]
        if deployment_state not in allowed_values:
            raise ValueError(
                "Invalid value for `deployment_state` ({0}), must be one of {1}"
                .format(deployment_state, allowed_values)
            )

        self._deployment_state = deployment_state

    @property
    def id(self):
        """
        Gets the id of this CampaignDeviceMetadataSerializer.
        The ID of the metadata concerning this device/campaign

        :return: The id of this CampaignDeviceMetadataSerializer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this CampaignDeviceMetadataSerializer.
        The ID of the metadata concerning this device/campaign

        :param id: The id of this CampaignDeviceMetadataSerializer.
        :type: str
        """

        self._id = id

    @property
    def device_id(self):
        """
        Gets the device_id of this CampaignDeviceMetadataSerializer.
        The ID of the device to deploy

        :return: The device_id of this CampaignDeviceMetadataSerializer.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """
        Sets the device_id of this CampaignDeviceMetadataSerializer.
        The ID of the device to deploy

        :param device_id: The device_id of this CampaignDeviceMetadataSerializer.
        :type: str
        """

        self._device_id = device_id

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