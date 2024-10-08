# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class GlobalizationCultureDto(object):
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
        'display_name': 'str',
        'two_letter_iso_language_name': 'str',
        'three_letter_iso_language_name': 'str',
        'three_letter_iso_language_names': 'list[str]',
        'two_letter_iso_language_names': 'list[str]'
    }

    attribute_map = {
        'name': 'Name',
        'display_name': 'DisplayName',
        'two_letter_iso_language_name': 'TwoLetterISOLanguageName',
        'three_letter_iso_language_name': 'ThreeLetterISOLanguageName',
        'three_letter_iso_language_names': 'ThreeLetterISOLanguageNames',
        'two_letter_iso_language_names': 'TwoLetterISOLanguageNames'
    }

    def __init__(self, name=None, display_name=None, two_letter_iso_language_name=None, three_letter_iso_language_name=None, three_letter_iso_language_names=None, two_letter_iso_language_names=None):  # noqa: E501
        """GlobalizationCultureDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._display_name = None
        self._two_letter_iso_language_name = None
        self._three_letter_iso_language_name = None
        self._three_letter_iso_language_names = None
        self._two_letter_iso_language_names = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if two_letter_iso_language_name is not None:
            self.two_letter_iso_language_name = two_letter_iso_language_name
        if three_letter_iso_language_name is not None:
            self.three_letter_iso_language_name = three_letter_iso_language_name
        if three_letter_iso_language_names is not None:
            self.three_letter_iso_language_names = three_letter_iso_language_names
        if two_letter_iso_language_names is not None:
            self.two_letter_iso_language_names = two_letter_iso_language_names

    @property
    def name(self):
        """Gets the name of this GlobalizationCultureDto.  # noqa: E501


        :return: The name of this GlobalizationCultureDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GlobalizationCultureDto.


        :param name: The name of this GlobalizationCultureDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this GlobalizationCultureDto.  # noqa: E501


        :return: The display_name of this GlobalizationCultureDto.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GlobalizationCultureDto.


        :param display_name: The display_name of this GlobalizationCultureDto.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def two_letter_iso_language_name(self):
        """Gets the two_letter_iso_language_name of this GlobalizationCultureDto.  # noqa: E501


        :return: The two_letter_iso_language_name of this GlobalizationCultureDto.  # noqa: E501
        :rtype: str
        """
        return self._two_letter_iso_language_name

    @two_letter_iso_language_name.setter
    def two_letter_iso_language_name(self, two_letter_iso_language_name):
        """Sets the two_letter_iso_language_name of this GlobalizationCultureDto.


        :param two_letter_iso_language_name: The two_letter_iso_language_name of this GlobalizationCultureDto.  # noqa: E501
        :type: str
        """

        self._two_letter_iso_language_name = two_letter_iso_language_name

    @property
    def three_letter_iso_language_name(self):
        """Gets the three_letter_iso_language_name of this GlobalizationCultureDto.  # noqa: E501


        :return: The three_letter_iso_language_name of this GlobalizationCultureDto.  # noqa: E501
        :rtype: str
        """
        return self._three_letter_iso_language_name

    @three_letter_iso_language_name.setter
    def three_letter_iso_language_name(self, three_letter_iso_language_name):
        """Sets the three_letter_iso_language_name of this GlobalizationCultureDto.


        :param three_letter_iso_language_name: The three_letter_iso_language_name of this GlobalizationCultureDto.  # noqa: E501
        :type: str
        """

        self._three_letter_iso_language_name = three_letter_iso_language_name

    @property
    def three_letter_iso_language_names(self):
        """Gets the three_letter_iso_language_names of this GlobalizationCultureDto.  # noqa: E501


        :return: The three_letter_iso_language_names of this GlobalizationCultureDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._three_letter_iso_language_names

    @three_letter_iso_language_names.setter
    def three_letter_iso_language_names(self, three_letter_iso_language_names):
        """Sets the three_letter_iso_language_names of this GlobalizationCultureDto.


        :param three_letter_iso_language_names: The three_letter_iso_language_names of this GlobalizationCultureDto.  # noqa: E501
        :type: list[str]
        """

        self._three_letter_iso_language_names = three_letter_iso_language_names

    @property
    def two_letter_iso_language_names(self):
        """Gets the two_letter_iso_language_names of this GlobalizationCultureDto.  # noqa: E501


        :return: The two_letter_iso_language_names of this GlobalizationCultureDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._two_letter_iso_language_names

    @two_letter_iso_language_names.setter
    def two_letter_iso_language_names(self, two_letter_iso_language_names):
        """Sets the two_letter_iso_language_names of this GlobalizationCultureDto.


        :param two_letter_iso_language_names: The two_letter_iso_language_names of this GlobalizationCultureDto.  # noqa: E501
        :type: list[str]
        """

        self._two_letter_iso_language_names = two_letter_iso_language_names

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
        if issubclass(GlobalizationCultureDto, dict):
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
        if not isinstance(other, GlobalizationCultureDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
