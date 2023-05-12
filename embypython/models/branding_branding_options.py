# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class BrandingBrandingOptions(object):
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
        'login_disclaimer': 'str',
        'custom_css': 'str'
    }

    attribute_map = {
        'login_disclaimer': 'LoginDisclaimer',
        'custom_css': 'CustomCss'
    }

    def __init__(self, login_disclaimer=None, custom_css=None):  # noqa: E501
        """BrandingBrandingOptions - a model defined in Swagger"""  # noqa: E501
        self._login_disclaimer = None
        self._custom_css = None
        self.discriminator = None
        if login_disclaimer is not None:
            self.login_disclaimer = login_disclaimer
        if custom_css is not None:
            self.custom_css = custom_css

    @property
    def login_disclaimer(self):
        """Gets the login_disclaimer of this BrandingBrandingOptions.  # noqa: E501


        :return: The login_disclaimer of this BrandingBrandingOptions.  # noqa: E501
        :rtype: str
        """
        return self._login_disclaimer

    @login_disclaimer.setter
    def login_disclaimer(self, login_disclaimer):
        """Sets the login_disclaimer of this BrandingBrandingOptions.


        :param login_disclaimer: The login_disclaimer of this BrandingBrandingOptions.  # noqa: E501
        :type: str
        """

        self._login_disclaimer = login_disclaimer

    @property
    def custom_css(self):
        """Gets the custom_css of this BrandingBrandingOptions.  # noqa: E501


        :return: The custom_css of this BrandingBrandingOptions.  # noqa: E501
        :rtype: str
        """
        return self._custom_css

    @custom_css.setter
    def custom_css(self, custom_css):
        """Sets the custom_css of this BrandingBrandingOptions.


        :param custom_css: The custom_css of this BrandingBrandingOptions.  # noqa: E501
        :type: str
        """

        self._custom_css = custom_css

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
        if issubclass(BrandingBrandingOptions, dict):
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
        if not isinstance(other, BrandingBrandingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
