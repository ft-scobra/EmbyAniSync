# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class MediaEncodingApiOnPlaybackProgress(object):
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
        'playlist_index': 'int',
        'playlist_length': 'int',
        'event_name': 'ProgressEvent'
    }

    attribute_map = {
        'playlist_index': 'PlaylistIndex',
        'playlist_length': 'PlaylistLength',
        'event_name': 'EventName'
    }

    def __init__(self, playlist_index=None, playlist_length=None, event_name=None):  # noqa: E501
        """MediaEncodingApiOnPlaybackProgress - a model defined in Swagger"""  # noqa: E501
        self._playlist_index = None
        self._playlist_length = None
        self._event_name = None
        self.discriminator = None
        if playlist_index is not None:
            self.playlist_index = playlist_index
        if playlist_length is not None:
            self.playlist_length = playlist_length
        if event_name is not None:
            self.event_name = event_name

    @property
    def playlist_index(self):
        """Gets the playlist_index of this MediaEncodingApiOnPlaybackProgress.  # noqa: E501


        :return: The playlist_index of this MediaEncodingApiOnPlaybackProgress.  # noqa: E501
        :rtype: int
        """
        return self._playlist_index

    @playlist_index.setter
    def playlist_index(self, playlist_index):
        """Sets the playlist_index of this MediaEncodingApiOnPlaybackProgress.


        :param playlist_index: The playlist_index of this MediaEncodingApiOnPlaybackProgress.  # noqa: E501
        :type: int
        """

        self._playlist_index = playlist_index

    @property
    def playlist_length(self):
        """Gets the playlist_length of this MediaEncodingApiOnPlaybackProgress.  # noqa: E501


        :return: The playlist_length of this MediaEncodingApiOnPlaybackProgress.  # noqa: E501
        :rtype: int
        """
        return self._playlist_length

    @playlist_length.setter
    def playlist_length(self, playlist_length):
        """Sets the playlist_length of this MediaEncodingApiOnPlaybackProgress.


        :param playlist_length: The playlist_length of this MediaEncodingApiOnPlaybackProgress.  # noqa: E501
        :type: int
        """

        self._playlist_length = playlist_length

    @property
    def event_name(self):
        """Gets the event_name of this MediaEncodingApiOnPlaybackProgress.  # noqa: E501


        :return: The event_name of this MediaEncodingApiOnPlaybackProgress.  # noqa: E501
        :rtype: ProgressEvent
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this MediaEncodingApiOnPlaybackProgress.


        :param event_name: The event_name of this MediaEncodingApiOnPlaybackProgress.  # noqa: E501
        :type: ProgressEvent
        """

        self._event_name = event_name

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
        if issubclass(MediaEncodingApiOnPlaybackProgress, dict):
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
        if not isinstance(other, MediaEncodingApiOnPlaybackProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
