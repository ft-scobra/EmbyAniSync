# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class RemoteImageInfo(object):
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
        'provider_name': 'str',
        'url': 'str',
        'thumbnail_url': 'str',
        'height': 'int',
        'width': 'int',
        'community_rating': 'float',
        'vote_count': 'int',
        'language': 'str',
        'display_language': 'str',
        'type': 'ImageType',
        'rating_type': 'RatingType'
    }

    attribute_map = {
        'provider_name': 'ProviderName',
        'url': 'Url',
        'thumbnail_url': 'ThumbnailUrl',
        'height': 'Height',
        'width': 'Width',
        'community_rating': 'CommunityRating',
        'vote_count': 'VoteCount',
        'language': 'Language',
        'display_language': 'DisplayLanguage',
        'type': 'Type',
        'rating_type': 'RatingType'
    }

    def __init__(self, provider_name=None, url=None, thumbnail_url=None, height=None, width=None, community_rating=None, vote_count=None, language=None, display_language=None, type=None, rating_type=None):  # noqa: E501
        """RemoteImageInfo - a model defined in Swagger"""  # noqa: E501
        self._provider_name = None
        self._url = None
        self._thumbnail_url = None
        self._height = None
        self._width = None
        self._community_rating = None
        self._vote_count = None
        self._language = None
        self._display_language = None
        self._type = None
        self._rating_type = None
        self.discriminator = None
        if provider_name is not None:
            self.provider_name = provider_name
        if url is not None:
            self.url = url
        if thumbnail_url is not None:
            self.thumbnail_url = thumbnail_url
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if community_rating is not None:
            self.community_rating = community_rating
        if vote_count is not None:
            self.vote_count = vote_count
        if language is not None:
            self.language = language
        if display_language is not None:
            self.display_language = display_language
        if type is not None:
            self.type = type
        if rating_type is not None:
            self.rating_type = rating_type

    @property
    def provider_name(self):
        """Gets the provider_name of this RemoteImageInfo.  # noqa: E501


        :return: The provider_name of this RemoteImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this RemoteImageInfo.


        :param provider_name: The provider_name of this RemoteImageInfo.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def url(self):
        """Gets the url of this RemoteImageInfo.  # noqa: E501


        :return: The url of this RemoteImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RemoteImageInfo.


        :param url: The url of this RemoteImageInfo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this RemoteImageInfo.  # noqa: E501


        :return: The thumbnail_url of this RemoteImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this RemoteImageInfo.


        :param thumbnail_url: The thumbnail_url of this RemoteImageInfo.  # noqa: E501
        :type: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def height(self):
        """Gets the height of this RemoteImageInfo.  # noqa: E501


        :return: The height of this RemoteImageInfo.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this RemoteImageInfo.


        :param height: The height of this RemoteImageInfo.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def width(self):
        """Gets the width of this RemoteImageInfo.  # noqa: E501


        :return: The width of this RemoteImageInfo.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this RemoteImageInfo.


        :param width: The width of this RemoteImageInfo.  # noqa: E501
        :type: int
        """

        self._width = width

    @property
    def community_rating(self):
        """Gets the community_rating of this RemoteImageInfo.  # noqa: E501


        :return: The community_rating of this RemoteImageInfo.  # noqa: E501
        :rtype: float
        """
        return self._community_rating

    @community_rating.setter
    def community_rating(self, community_rating):
        """Sets the community_rating of this RemoteImageInfo.


        :param community_rating: The community_rating of this RemoteImageInfo.  # noqa: E501
        :type: float
        """

        self._community_rating = community_rating

    @property
    def vote_count(self):
        """Gets the vote_count of this RemoteImageInfo.  # noqa: E501


        :return: The vote_count of this RemoteImageInfo.  # noqa: E501
        :rtype: int
        """
        return self._vote_count

    @vote_count.setter
    def vote_count(self, vote_count):
        """Sets the vote_count of this RemoteImageInfo.


        :param vote_count: The vote_count of this RemoteImageInfo.  # noqa: E501
        :type: int
        """

        self._vote_count = vote_count

    @property
    def language(self):
        """Gets the language of this RemoteImageInfo.  # noqa: E501


        :return: The language of this RemoteImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this RemoteImageInfo.


        :param language: The language of this RemoteImageInfo.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def display_language(self):
        """Gets the display_language of this RemoteImageInfo.  # noqa: E501


        :return: The display_language of this RemoteImageInfo.  # noqa: E501
        :rtype: str
        """
        return self._display_language

    @display_language.setter
    def display_language(self, display_language):
        """Sets the display_language of this RemoteImageInfo.


        :param display_language: The display_language of this RemoteImageInfo.  # noqa: E501
        :type: str
        """

        self._display_language = display_language

    @property
    def type(self):
        """Gets the type of this RemoteImageInfo.  # noqa: E501


        :return: The type of this RemoteImageInfo.  # noqa: E501
        :rtype: ImageType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RemoteImageInfo.


        :param type: The type of this RemoteImageInfo.  # noqa: E501
        :type: ImageType
        """

        self._type = type

    @property
    def rating_type(self):
        """Gets the rating_type of this RemoteImageInfo.  # noqa: E501


        :return: The rating_type of this RemoteImageInfo.  # noqa: E501
        :rtype: RatingType
        """
        return self._rating_type

    @rating_type.setter
    def rating_type(self, rating_type):
        """Sets the rating_type of this RemoteImageInfo.


        :param rating_type: The rating_type of this RemoteImageInfo.  # noqa: E501
        :type: RatingType
        """

        self._rating_type = rating_type

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
        if issubclass(RemoteImageInfo, dict):
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
        if not isinstance(other, RemoteImageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
