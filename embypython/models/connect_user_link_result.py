# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class ConnectUserLinkResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'is_pending': 'bool',
        'is_new_user_invitation': 'bool',
        'guest_display_name': 'str'
    }

    attribute_map = {
        'is_pending': 'IsPending',
        'is_new_user_invitation': 'IsNewUserInvitation',
        'guest_display_name': 'GuestDisplayName'
    }

    def __init__(self, is_pending=None, is_new_user_invitation=None, guest_display_name=None):  # noqa: E501
        """ConnectUserLinkResult - a model defined in Swagger"""  # noqa: E501
        self._is_pending = None
        self._is_new_user_invitation = None
        self._guest_display_name = None
        self.discriminator = None
        if is_pending is not None:
            self.is_pending = is_pending
        if is_new_user_invitation is not None:
            self.is_new_user_invitation = is_new_user_invitation
        if guest_display_name is not None:
            self.guest_display_name = guest_display_name

    @property
    def is_pending(self):
        """Gets the is_pending of this ConnectUserLinkResult.  # noqa: E501


        :return: The is_pending of this ConnectUserLinkResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_pending

    @is_pending.setter
    def is_pending(self, is_pending):
        """Sets the is_pending of this ConnectUserLinkResult.


        :param is_pending: The is_pending of this ConnectUserLinkResult.  # noqa: E501
        :type: bool
        """

        self._is_pending = is_pending

    @property
    def is_new_user_invitation(self):
        """Gets the is_new_user_invitation of this ConnectUserLinkResult.  # noqa: E501


        :return: The is_new_user_invitation of this ConnectUserLinkResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_new_user_invitation

    @is_new_user_invitation.setter
    def is_new_user_invitation(self, is_new_user_invitation):
        """Sets the is_new_user_invitation of this ConnectUserLinkResult.


        :param is_new_user_invitation: The is_new_user_invitation of this ConnectUserLinkResult.  # noqa: E501
        :type: bool
        """

        self._is_new_user_invitation = is_new_user_invitation

    @property
    def guest_display_name(self):
        """Gets the guest_display_name of this ConnectUserLinkResult.  # noqa: E501


        :return: The guest_display_name of this ConnectUserLinkResult.  # noqa: E501
        :rtype: str
        """
        return self._guest_display_name

    @guest_display_name.setter
    def guest_display_name(self, guest_display_name):
        """Sets the guest_display_name of this ConnectUserLinkResult.


        :param guest_display_name: The guest_display_name of this ConnectUserLinkResult.  # noqa: E501
        :type: str
        """

        self._guest_display_name = guest_display_name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ConnectUserLinkResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConnectUserLinkResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
