# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class UpdateUserEasyPassword(object):
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
        'id': 'str',
        'new_pw': 'str',
        'reset_password': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'new_pw': 'NewPw',
        'reset_password': 'ResetPassword'
    }

    def __init__(self, id=None, new_pw=None, reset_password=None):  # noqa: E501
        """UpdateUserEasyPassword - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._new_pw = None
        self._reset_password = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if new_pw is not None:
            self.new_pw = new_pw
        if reset_password is not None:
            self.reset_password = reset_password

    @property
    def id(self):
        """Gets the id of this UpdateUserEasyPassword.  # noqa: E501


        :return: The id of this UpdateUserEasyPassword.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateUserEasyPassword.


        :param id: The id of this UpdateUserEasyPassword.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def new_pw(self):
        """Gets the new_pw of this UpdateUserEasyPassword.  # noqa: E501


        :return: The new_pw of this UpdateUserEasyPassword.  # noqa: E501
        :rtype: str
        """
        return self._new_pw

    @new_pw.setter
    def new_pw(self, new_pw):
        """Sets the new_pw of this UpdateUserEasyPassword.


        :param new_pw: The new_pw of this UpdateUserEasyPassword.  # noqa: E501
        :type: str
        """

        self._new_pw = new_pw

    @property
    def reset_password(self):
        """Gets the reset_password of this UpdateUserEasyPassword.  # noqa: E501


        :return: The reset_password of this UpdateUserEasyPassword.  # noqa: E501
        :rtype: bool
        """
        return self._reset_password

    @reset_password.setter
    def reset_password(self, reset_password):
        """Sets the reset_password of this UpdateUserEasyPassword.


        :param reset_password: The reset_password of this UpdateUserEasyPassword.  # noqa: E501
        :type: bool
        """

        self._reset_password = reset_password

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
        if issubclass(UpdateUserEasyPassword, dict):
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
        if not isinstance(other, UpdateUserEasyPassword):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
