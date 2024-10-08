# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class NetEndPointInfo(object):
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
        'is_local': 'bool',
        'is_in_network': 'bool'
    }

    attribute_map = {
        'is_local': 'IsLocal',
        'is_in_network': 'IsInNetwork'
    }

    def __init__(self, is_local=None, is_in_network=None):  # noqa: E501
        """NetEndPointInfo - a model defined in Swagger"""  # noqa: E501
        self._is_local = None
        self._is_in_network = None
        self.discriminator = None
        if is_local is not None:
            self.is_local = is_local
        if is_in_network is not None:
            self.is_in_network = is_in_network

    @property
    def is_local(self):
        """Gets the is_local of this NetEndPointInfo.  # noqa: E501


        :return: The is_local of this NetEndPointInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_local

    @is_local.setter
    def is_local(self, is_local):
        """Sets the is_local of this NetEndPointInfo.


        :param is_local: The is_local of this NetEndPointInfo.  # noqa: E501
        :type: bool
        """

        self._is_local = is_local

    @property
    def is_in_network(self):
        """Gets the is_in_network of this NetEndPointInfo.  # noqa: E501


        :return: The is_in_network of this NetEndPointInfo.  # noqa: E501
        :rtype: bool
        """
        return self._is_in_network

    @is_in_network.setter
    def is_in_network(self, is_in_network):
        """Sets the is_in_network of this NetEndPointInfo.


        :param is_in_network: The is_in_network of this NetEndPointInfo.  # noqa: E501
        :type: bool
        """

        self._is_in_network = is_in_network

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
        if issubclass(NetEndPointInfo, dict):
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
        if not isinstance(other, NetEndPointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
