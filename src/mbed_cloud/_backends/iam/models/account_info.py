# coding: utf-8

"""
    Account Management API

    API for managing accounts, users, creating API keys, uploading trusted certificates

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AccountInfo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address_line1': 'str',
        'address_line2': 'str',
        'aliases': 'list[str]',
        'city': 'str',
        'company': 'str',
        'contact': 'str',
        'contract_number': 'str',
        'country': 'str',
        'created_at': 'datetime',
        'custom_fields': 'dict(str, str)',
        'customer_number': 'str',
        'display_name': 'str',
        'email': 'str',
        'end_market': 'str',
        'etag': 'str',
        'expiration_warning_threshold': 'str',
        'id': 'str',
        'idle_timeout': 'str',
        'limits': 'dict(str, str)',
        'mfa_status': 'str',
        'notification_emails': 'list[str]',
        'object': 'str',
        'parent_id': 'str',
        'password_policy': 'PasswordPolicy',
        'phone_number': 'str',
        'policies': 'list[FeaturePolicy]',
        'postal_code': 'str',
        'reason': 'str',
        'reference_note': 'str',
        'sales_contact': 'str',
        'state': 'str',
        'status': 'str',
        'sub_accounts': 'list[AccountInfo]',
        'template_id': 'str',
        'tier': 'str',
        'updated_at': 'datetime',
        'upgraded_at': 'datetime'
    }

    attribute_map = {
        'address_line1': 'address_line1',
        'address_line2': 'address_line2',
        'aliases': 'aliases',
        'city': 'city',
        'company': 'company',
        'contact': 'contact',
        'contract_number': 'contract_number',
        'country': 'country',
        'created_at': 'created_at',
        'custom_fields': 'custom_fields',
        'customer_number': 'customer_number',
        'display_name': 'display_name',
        'email': 'email',
        'end_market': 'end_market',
        'etag': 'etag',
        'expiration_warning_threshold': 'expiration_warning_threshold',
        'id': 'id',
        'idle_timeout': 'idle_timeout',
        'limits': 'limits',
        'mfa_status': 'mfa_status',
        'notification_emails': 'notification_emails',
        'object': 'object',
        'parent_id': 'parent_id',
        'password_policy': 'password_policy',
        'phone_number': 'phone_number',
        'policies': 'policies',
        'postal_code': 'postal_code',
        'reason': 'reason',
        'reference_note': 'reference_note',
        'sales_contact': 'sales_contact',
        'state': 'state',
        'status': 'status',
        'sub_accounts': 'sub_accounts',
        'template_id': 'template_id',
        'tier': 'tier',
        'updated_at': 'updated_at',
        'upgraded_at': 'upgraded_at'
    }

    def __init__(self, address_line1=None, address_line2=None, aliases=None, city=None, company=None, contact=None, contract_number=None, country=None, created_at=None, custom_fields=None, customer_number=None, display_name=None, email=None, end_market=None, etag=None, expiration_warning_threshold=None, id=None, idle_timeout=None, limits=None, mfa_status=None, notification_emails=None, object=None, parent_id=None, password_policy=None, phone_number=None, policies=None, postal_code=None, reason=None, reference_note=None, sales_contact=None, state=None, status=None, sub_accounts=None, template_id=None, tier=None, updated_at=None, upgraded_at=None):
        """
        AccountInfo - a model defined in Swagger
        """

        self._address_line1 = address_line1
        self._address_line2 = address_line2
        self._aliases = aliases
        self._city = city
        self._company = company
        self._contact = contact
        self._contract_number = contract_number
        self._country = country
        self._created_at = created_at
        self._custom_fields = custom_fields
        self._customer_number = customer_number
        self._display_name = display_name
        self._email = email
        self._end_market = end_market
        self._etag = etag
        self._expiration_warning_threshold = expiration_warning_threshold
        self._id = id
        self._idle_timeout = idle_timeout
        self._limits = limits
        self._mfa_status = mfa_status
        self._notification_emails = notification_emails
        self._object = object
        self._parent_id = parent_id
        self._password_policy = password_policy
        self._phone_number = phone_number
        self._policies = policies
        self._postal_code = postal_code
        self._reason = reason
        self._reference_note = reference_note
        self._sales_contact = sales_contact
        self._state = state
        self._status = status
        self._sub_accounts = sub_accounts
        self._template_id = template_id
        self._tier = tier
        self._updated_at = updated_at
        self._upgraded_at = upgraded_at
        self.discriminator = None

    @property
    def address_line1(self):
        """
        Gets the address_line1 of this AccountInfo.
        Postal address line 1.

        :return: The address_line1 of this AccountInfo.
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """
        Sets the address_line1 of this AccountInfo.
        Postal address line 1.

        :param address_line1: The address_line1 of this AccountInfo.
        :type: str
        """

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """
        Gets the address_line2 of this AccountInfo.
        Postal address line 2.

        :return: The address_line2 of this AccountInfo.
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """
        Sets the address_line2 of this AccountInfo.
        Postal address line 2.

        :param address_line2: The address_line2 of this AccountInfo.
        :type: str
        """

        self._address_line2 = address_line2

    @property
    def aliases(self):
        """
        Gets the aliases of this AccountInfo.
        An array of aliases.

        :return: The aliases of this AccountInfo.
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """
        Sets the aliases of this AccountInfo.
        An array of aliases.

        :param aliases: The aliases of this AccountInfo.
        :type: list[str]
        """
        if aliases is None:
            raise ValueError("Invalid value for `aliases`, must not be `None`")

        self._aliases = aliases

    @property
    def city(self):
        """
        Gets the city of this AccountInfo.
        The city part of the postal address.

        :return: The city of this AccountInfo.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this AccountInfo.
        The city part of the postal address.

        :param city: The city of this AccountInfo.
        :type: str
        """

        self._city = city

    @property
    def company(self):
        """
        Gets the company of this AccountInfo.
        The name of the company.

        :return: The company of this AccountInfo.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this AccountInfo.
        The name of the company.

        :param company: The company of this AccountInfo.
        :type: str
        """

        self._company = company

    @property
    def contact(self):
        """
        Gets the contact of this AccountInfo.
        The name of the contact person for this account.

        :return: The contact of this AccountInfo.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this AccountInfo.
        The name of the contact person for this account.

        :param contact: The contact of this AccountInfo.
        :type: str
        """

        self._contact = contact

    @property
    def contract_number(self):
        """
        Gets the contract_number of this AccountInfo.
        Contract number of the customer.

        :return: The contract_number of this AccountInfo.
        :rtype: str
        """
        return self._contract_number

    @contract_number.setter
    def contract_number(self, contract_number):
        """
        Sets the contract_number of this AccountInfo.
        Contract number of the customer.

        :param contract_number: The contract_number of this AccountInfo.
        :type: str
        """

        self._contract_number = contract_number

    @property
    def country(self):
        """
        Gets the country of this AccountInfo.
        The country part of the postal address.

        :return: The country of this AccountInfo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this AccountInfo.
        The country part of the postal address.

        :param country: The country of this AccountInfo.
        :type: str
        """

        self._country = country

    @property
    def created_at(self):
        """
        Gets the created_at of this AccountInfo.
        Creation UTC time RFC3339.

        :return: The created_at of this AccountInfo.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """
        Sets the created_at of this AccountInfo.
        Creation UTC time RFC3339.

        :param created_at: The created_at of this AccountInfo.
        :type: datetime
        """

        self._created_at = created_at

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this AccountInfo.
        Account's custom properties as key-value pairs.

        :return: The custom_fields of this AccountInfo.
        :rtype: dict(str, str)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this AccountInfo.
        Account's custom properties as key-value pairs.

        :param custom_fields: The custom_fields of this AccountInfo.
        :type: dict(str, str)
        """

        self._custom_fields = custom_fields

    @property
    def customer_number(self):
        """
        Gets the customer_number of this AccountInfo.
        Customer number of the customer.

        :return: The customer_number of this AccountInfo.
        :rtype: str
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """
        Sets the customer_number of this AccountInfo.
        Customer number of the customer.

        :param customer_number: The customer_number of this AccountInfo.
        :type: str
        """

        self._customer_number = customer_number

    @property
    def display_name(self):
        """
        Gets the display_name of this AccountInfo.
        The display name for the account.

        :return: The display_name of this AccountInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AccountInfo.
        The display name for the account.

        :param display_name: The display_name of this AccountInfo.
        :type: str
        """

        self._display_name = display_name

    @property
    def email(self):
        """
        Gets the email of this AccountInfo.
        The company email address for this account.

        :return: The email of this AccountInfo.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this AccountInfo.
        The company email address for this account.

        :param email: The email of this AccountInfo.
        :type: str
        """

        self._email = email

    @property
    def end_market(self):
        """
        Gets the end_market of this AccountInfo.
        Account end market.

        :return: The end_market of this AccountInfo.
        :rtype: str
        """
        return self._end_market

    @end_market.setter
    def end_market(self, end_market):
        """
        Sets the end_market of this AccountInfo.
        Account end market.

        :param end_market: The end_market of this AccountInfo.
        :type: str
        """
        if end_market is None:
            raise ValueError("Invalid value for `end_market`, must not be `None`")

        self._end_market = end_market

    @property
    def etag(self):
        """
        Gets the etag of this AccountInfo.
        API resource entity version.

        :return: The etag of this AccountInfo.
        :rtype: str
        """
        return self._etag

    @etag.setter
    def etag(self, etag):
        """
        Sets the etag of this AccountInfo.
        API resource entity version.

        :param etag: The etag of this AccountInfo.
        :type: str
        """
        if etag is None:
            raise ValueError("Invalid value for `etag`, must not be `None`")

        self._etag = etag

    @property
    def expiration_warning_threshold(self):
        """
        Gets the expiration_warning_threshold of this AccountInfo.
        Indicates how many days (1-180) before account expiration a notification email should be sent.

        :return: The expiration_warning_threshold of this AccountInfo.
        :rtype: str
        """
        return self._expiration_warning_threshold

    @expiration_warning_threshold.setter
    def expiration_warning_threshold(self, expiration_warning_threshold):
        """
        Sets the expiration_warning_threshold of this AccountInfo.
        Indicates how many days (1-180) before account expiration a notification email should be sent.

        :param expiration_warning_threshold: The expiration_warning_threshold of this AccountInfo.
        :type: str
        """

        self._expiration_warning_threshold = expiration_warning_threshold

    @property
    def id(self):
        """
        Gets the id of this AccountInfo.
        Account ID.

        :return: The id of this AccountInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AccountInfo.
        Account ID.

        :param id: The id of this AccountInfo.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def idle_timeout(self):
        """
        Gets the idle_timeout of this AccountInfo.
        The reference token expiration time in minutes for this account.

        :return: The idle_timeout of this AccountInfo.
        :rtype: str
        """
        return self._idle_timeout

    @idle_timeout.setter
    def idle_timeout(self, idle_timeout):
        """
        Sets the idle_timeout of this AccountInfo.
        The reference token expiration time in minutes for this account.

        :param idle_timeout: The idle_timeout of this AccountInfo.
        :type: str
        """

        self._idle_timeout = idle_timeout

    @property
    def limits(self):
        """
        Gets the limits of this AccountInfo.
        List of limits as key-value pairs if requested.

        :return: The limits of this AccountInfo.
        :rtype: dict(str, str)
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        """
        Sets the limits of this AccountInfo.
        List of limits as key-value pairs if requested.

        :param limits: The limits of this AccountInfo.
        :type: dict(str, str)
        """

        self._limits = limits

    @property
    def mfa_status(self):
        """
        Gets the mfa_status of this AccountInfo.
        The enforcement status of the multi-factor authentication, either 'enforced' or 'optional'.

        :return: The mfa_status of this AccountInfo.
        :rtype: str
        """
        return self._mfa_status

    @mfa_status.setter
    def mfa_status(self, mfa_status):
        """
        Sets the mfa_status of this AccountInfo.
        The enforcement status of the multi-factor authentication, either 'enforced' or 'optional'.

        :param mfa_status: The mfa_status of this AccountInfo.
        :type: str
        """
        allowed_values = ["enforced", "optional"]
        if mfa_status not in allowed_values:
            raise ValueError(
                "Invalid value for `mfa_status` ({0}), must be one of {1}"
                .format(mfa_status, allowed_values)
            )

        self._mfa_status = mfa_status

    @property
    def notification_emails(self):
        """
        Gets the notification_emails of this AccountInfo.
        A list of notification email addresses.

        :return: The notification_emails of this AccountInfo.
        :rtype: list[str]
        """
        return self._notification_emails

    @notification_emails.setter
    def notification_emails(self, notification_emails):
        """
        Sets the notification_emails of this AccountInfo.
        A list of notification email addresses.

        :param notification_emails: The notification_emails of this AccountInfo.
        :type: list[str]
        """

        self._notification_emails = notification_emails

    @property
    def object(self):
        """
        Gets the object of this AccountInfo.
        Entity name: always 'account'

        :return: The object of this AccountInfo.
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """
        Sets the object of this AccountInfo.
        Entity name: always 'account'

        :param object: The object of this AccountInfo.
        :type: str
        """
        if object is None:
            raise ValueError("Invalid value for `object`, must not be `None`")
        allowed_values = ["account"]
        if object not in allowed_values:
            raise ValueError(
                "Invalid value for `object` ({0}), must be one of {1}"
                .format(object, allowed_values)
            )

        self._object = object

    @property
    def parent_id(self):
        """
        Gets the parent_id of this AccountInfo.
        The ID of the parent account, if it has any.

        :return: The parent_id of this AccountInfo.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this AccountInfo.
        The ID of the parent account, if it has any.

        :param parent_id: The parent_id of this AccountInfo.
        :type: str
        """

        self._parent_id = parent_id

    @property
    def password_policy(self):
        """
        Gets the password_policy of this AccountInfo.
        The password policy for this account.

        :return: The password_policy of this AccountInfo.
        :rtype: PasswordPolicy
        """
        return self._password_policy

    @password_policy.setter
    def password_policy(self, password_policy):
        """
        Sets the password_policy of this AccountInfo.
        The password policy for this account.

        :param password_policy: The password_policy of this AccountInfo.
        :type: PasswordPolicy
        """

        self._password_policy = password_policy

    @property
    def phone_number(self):
        """
        Gets the phone_number of this AccountInfo.
        The phone number of a representative of the company.

        :return: The phone_number of this AccountInfo.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this AccountInfo.
        The phone number of a representative of the company.

        :param phone_number: The phone_number of this AccountInfo.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def policies(self):
        """
        Gets the policies of this AccountInfo.
        List of policies if requested.

        :return: The policies of this AccountInfo.
        :rtype: list[FeaturePolicy]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """
        Sets the policies of this AccountInfo.
        List of policies if requested.

        :param policies: The policies of this AccountInfo.
        :type: list[FeaturePolicy]
        """

        self._policies = policies

    @property
    def postal_code(self):
        """
        Gets the postal_code of this AccountInfo.
        The postal code part of the postal address.

        :return: The postal_code of this AccountInfo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this AccountInfo.
        The postal code part of the postal address.

        :param postal_code: The postal_code of this AccountInfo.
        :type: str
        """

        self._postal_code = postal_code

    @property
    def reason(self):
        """
        Gets the reason of this AccountInfo.
        A reason note for updating the status of the account

        :return: The reason of this AccountInfo.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason of this AccountInfo.
        A reason note for updating the status of the account

        :param reason: The reason of this AccountInfo.
        :type: str
        """

        self._reason = reason

    @property
    def reference_note(self):
        """
        Gets the reference_note of this AccountInfo.
        A reference note for updating the status of the account

        :return: The reference_note of this AccountInfo.
        :rtype: str
        """
        return self._reference_note

    @reference_note.setter
    def reference_note(self, reference_note):
        """
        Sets the reference_note of this AccountInfo.
        A reference note for updating the status of the account

        :param reference_note: The reference_note of this AccountInfo.
        :type: str
        """

        self._reference_note = reference_note

    @property
    def sales_contact(self):
        """
        Gets the sales_contact of this AccountInfo.
        Email address of the sales contact.

        :return: The sales_contact of this AccountInfo.
        :rtype: str
        """
        return self._sales_contact

    @sales_contact.setter
    def sales_contact(self, sales_contact):
        """
        Sets the sales_contact of this AccountInfo.
        Email address of the sales contact.

        :param sales_contact: The sales_contact of this AccountInfo.
        :type: str
        """

        self._sales_contact = sales_contact

    @property
    def state(self):
        """
        Gets the state of this AccountInfo.
        The state part of the postal address.

        :return: The state of this AccountInfo.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AccountInfo.
        The state part of the postal address.

        :param state: The state of this AccountInfo.
        :type: str
        """

        self._state = state

    @property
    def status(self):
        """
        Gets the status of this AccountInfo.
        The status of the account.

        :return: The status of this AccountInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AccountInfo.
        The status of the account.

        :param status: The status of this AccountInfo.
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")
        allowed_values = ["ENROLLING", "ACTIVE", "RESTRICTED", "SUSPENDED"]
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def sub_accounts(self):
        """
        Gets the sub_accounts of this AccountInfo.
        List of sub accounts. Not available for developer users.

        :return: The sub_accounts of this AccountInfo.
        :rtype: list[AccountInfo]
        """
        return self._sub_accounts

    @sub_accounts.setter
    def sub_accounts(self, sub_accounts):
        """
        Sets the sub_accounts of this AccountInfo.
        List of sub accounts. Not available for developer users.

        :param sub_accounts: The sub_accounts of this AccountInfo.
        :type: list[AccountInfo]
        """

        self._sub_accounts = sub_accounts

    @property
    def template_id(self):
        """
        Gets the template_id of this AccountInfo.
        Account template ID.

        :return: The template_id of this AccountInfo.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """
        Sets the template_id of this AccountInfo.
        Account template ID.

        :param template_id: The template_id of this AccountInfo.
        :type: str
        """

        self._template_id = template_id

    @property
    def tier(self):
        """
        Gets the tier of this AccountInfo.
        The tier level of the account; '0': free tier, '1': commercial account, '2': partner tier. Other values are reserved for the future.

        :return: The tier of this AccountInfo.
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """
        Sets the tier of this AccountInfo.
        The tier level of the account; '0': free tier, '1': commercial account, '2': partner tier. Other values are reserved for the future.

        :param tier: The tier of this AccountInfo.
        :type: str
        """
        if tier is None:
            raise ValueError("Invalid value for `tier`, must not be `None`")

        self._tier = tier

    @property
    def updated_at(self):
        """
        Gets the updated_at of this AccountInfo.
        Last update UTC time RFC3339.

        :return: The updated_at of this AccountInfo.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """
        Sets the updated_at of this AccountInfo.
        Last update UTC time RFC3339.

        :param updated_at: The updated_at of this AccountInfo.
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def upgraded_at(self):
        """
        Gets the upgraded_at of this AccountInfo.
        Time when upgraded to commercial account in UTC format RFC3339.

        :return: The upgraded_at of this AccountInfo.
        :rtype: datetime
        """
        return self._upgraded_at

    @upgraded_at.setter
    def upgraded_at(self, upgraded_at):
        """
        Sets the upgraded_at of this AccountInfo.
        Time when upgraded to commercial account in UTC format RFC3339.

        :param upgraded_at: The upgraded_at of this AccountInfo.
        :type: datetime
        """

        self._upgraded_at = upgraded_at

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
        if not isinstance(other, AccountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
