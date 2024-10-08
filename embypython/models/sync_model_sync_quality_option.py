# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class SyncModelSyncQualityOption(object):
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
        'name': 'str',
        'description': 'str',
        'id': 'str',
        'is_default': 'bool',
        'is_original_quality': 'bool'
    }

    attribute_map = {
        'name': 'Name',
        'description': 'Description',
        'id': 'Id',
        'is_default': 'IsDefault',
        'is_original_quality': 'IsOriginalQuality'
    }

    def __init__(self, name=None, description=None, id=None, is_default=None, is_original_quality=None):  # noqa: E501
        """SyncModelSyncQualityOption - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._id = None
        self._is_default = None
        self._is_original_quality = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_default is not None:
            self.is_default = is_default
        if is_original_quality is not None:
            self.is_original_quality = is_original_quality

    @property
    def name(self):
        """Gets the name of this SyncModelSyncQualityOption.  # noqa: E501


        :return: The name of this SyncModelSyncQualityOption.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SyncModelSyncQualityOption.


        :param name: The name of this SyncModelSyncQualityOption.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this SyncModelSyncQualityOption.  # noqa: E501


        :return: The description of this SyncModelSyncQualityOption.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SyncModelSyncQualityOption.


        :param description: The description of this SyncModelSyncQualityOption.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this SyncModelSyncQualityOption.  # noqa: E501


        :return: The id of this SyncModelSyncQualityOption.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SyncModelSyncQualityOption.


        :param id: The id of this SyncModelSyncQualityOption.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_default(self):
        """Gets the is_default of this SyncModelSyncQualityOption.  # noqa: E501


        :return: The is_default of this SyncModelSyncQualityOption.  # noqa: E501
        :rtype: bool
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """Sets the is_default of this SyncModelSyncQualityOption.


        :param is_default: The is_default of this SyncModelSyncQualityOption.  # noqa: E501
        :type: bool
        """

        self._is_default = is_default

    @property
    def is_original_quality(self):
        """Gets the is_original_quality of this SyncModelSyncQualityOption.  # noqa: E501


        :return: The is_original_quality of this SyncModelSyncQualityOption.  # noqa: E501
        :rtype: bool
        """
        return self._is_original_quality

    @is_original_quality.setter
    def is_original_quality(self, is_original_quality):
        """Sets the is_original_quality of this SyncModelSyncQualityOption.


        :param is_original_quality: The is_original_quality of this SyncModelSyncQualityOption.  # noqa: E501
        :type: bool
        """

        self._is_original_quality = is_original_quality

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
        if issubclass(SyncModelSyncQualityOption, dict):
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
        if not isinstance(other, SyncModelSyncQualityOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
