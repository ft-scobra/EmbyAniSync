# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class QueryResultLiveTvTimerInfoDto(object):
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
        'items': 'list[LiveTvTimerInfoDto]',
        'total_record_count': 'int'
    }

    attribute_map = {
        'items': 'Items',
        'total_record_count': 'TotalRecordCount'
    }

    def __init__(self, items=None, total_record_count=None):  # noqa: E501
        """QueryResultLiveTvTimerInfoDto - a model defined in Swagger"""  # noqa: E501
        self._items = None
        self._total_record_count = None
        self.discriminator = None
        if items is not None:
            self.items = items
        if total_record_count is not None:
            self.total_record_count = total_record_count

    @property
    def items(self):
        """Gets the items of this QueryResultLiveTvTimerInfoDto.  # noqa: E501


        :return: The items of this QueryResultLiveTvTimerInfoDto.  # noqa: E501
        :rtype: list[LiveTvTimerInfoDto]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this QueryResultLiveTvTimerInfoDto.


        :param items: The items of this QueryResultLiveTvTimerInfoDto.  # noqa: E501
        :type: list[LiveTvTimerInfoDto]
        """

        self._items = items

    @property
    def total_record_count(self):
        """Gets the total_record_count of this QueryResultLiveTvTimerInfoDto.  # noqa: E501


        :return: The total_record_count of this QueryResultLiveTvTimerInfoDto.  # noqa: E501
        :rtype: int
        """
        return self._total_record_count

    @total_record_count.setter
    def total_record_count(self, total_record_count):
        """Sets the total_record_count of this QueryResultLiveTvTimerInfoDto.


        :param total_record_count: The total_record_count of this QueryResultLiveTvTimerInfoDto.  # noqa: E501
        :type: int
        """

        self._total_record_count = total_record_count

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
        if issubclass(QueryResultLiveTvTimerInfoDto, dict):
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
        if not isinstance(other, QueryResultLiveTvTimerInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
