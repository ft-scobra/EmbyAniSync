# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class LiveTvKeywordInfo(object):
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
        'keyword_type': 'LiveTvKeywordType',
        'keyword': 'str'
    }

    attribute_map = {
        'keyword_type': 'KeywordType',
        'keyword': 'Keyword'
    }

    def __init__(self, keyword_type=None, keyword=None):  # noqa: E501
        """LiveTvKeywordInfo - a model defined in Swagger"""  # noqa: E501
        self._keyword_type = None
        self._keyword = None
        self.discriminator = None
        if keyword_type is not None:
            self.keyword_type = keyword_type
        if keyword is not None:
            self.keyword = keyword

    @property
    def keyword_type(self):
        """Gets the keyword_type of this LiveTvKeywordInfo.  # noqa: E501


        :return: The keyword_type of this LiveTvKeywordInfo.  # noqa: E501
        :rtype: LiveTvKeywordType
        """
        return self._keyword_type

    @keyword_type.setter
    def keyword_type(self, keyword_type):
        """Sets the keyword_type of this LiveTvKeywordInfo.


        :param keyword_type: The keyword_type of this LiveTvKeywordInfo.  # noqa: E501
        :type: LiveTvKeywordType
        """

        self._keyword_type = keyword_type

    @property
    def keyword(self):
        """Gets the keyword of this LiveTvKeywordInfo.  # noqa: E501


        :return: The keyword of this LiveTvKeywordInfo.  # noqa: E501
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this LiveTvKeywordInfo.


        :param keyword: The keyword of this LiveTvKeywordInfo.  # noqa: E501
        :type: str
        """

        self._keyword = keyword

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
        if issubclass(LiveTvKeywordInfo, dict):
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
        if not isinstance(other, LiveTvKeywordInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
