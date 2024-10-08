# coding: utf-8

"""
    Emby REST API
"""

import pprint
import re  # noqa: F401

import six

class UpdatesPackageVersionInfo(object):
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
        'guid': 'str',
        'version_str': 'str',
        'classification': 'UpdatesPackageVersionClass',
        'description': 'str',
        'required_version_str': 'str',
        'source_url': 'str',
        'checksum': 'str',
        'target_filename': 'str',
        'info_url': 'str',
        'runtimes': 'str'
    }

    attribute_map = {
        'name': 'name',
        'guid': 'guid',
        'version_str': 'versionStr',
        'classification': 'classification',
        'description': 'description',
        'required_version_str': 'requiredVersionStr',
        'source_url': 'sourceUrl',
        'checksum': 'checksum',
        'target_filename': 'targetFilename',
        'info_url': 'infoUrl',
        'runtimes': 'runtimes'
    }

    def __init__(self, name=None, guid=None, version_str=None, classification=None, description=None, required_version_str=None, source_url=None, checksum=None, target_filename=None, info_url=None, runtimes=None):  # noqa: E501
        """UpdatesPackageVersionInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._guid = None
        self._version_str = None
        self._classification = None
        self._description = None
        self._required_version_str = None
        self._source_url = None
        self._checksum = None
        self._target_filename = None
        self._info_url = None
        self._runtimes = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if guid is not None:
            self.guid = guid
        if version_str is not None:
            self.version_str = version_str
        if classification is not None:
            self.classification = classification
        if description is not None:
            self.description = description
        if required_version_str is not None:
            self.required_version_str = required_version_str
        if source_url is not None:
            self.source_url = source_url
        if checksum is not None:
            self.checksum = checksum
        if target_filename is not None:
            self.target_filename = target_filename
        if info_url is not None:
            self.info_url = info_url
        if runtimes is not None:
            self.runtimes = runtimes

    @property
    def name(self):
        """Gets the name of this UpdatesPackageVersionInfo.  # noqa: E501


        :return: The name of this UpdatesPackageVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatesPackageVersionInfo.


        :param name: The name of this UpdatesPackageVersionInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def guid(self):
        """Gets the guid of this UpdatesPackageVersionInfo.  # noqa: E501


        :return: The guid of this UpdatesPackageVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this UpdatesPackageVersionInfo.


        :param guid: The guid of this UpdatesPackageVersionInfo.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def version_str(self):
        """Gets the version_str of this UpdatesPackageVersionInfo.  # noqa: E501


        :return: The version_str of this UpdatesPackageVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._version_str

    @version_str.setter
    def version_str(self, version_str):
        """Sets the version_str of this UpdatesPackageVersionInfo.


        :param version_str: The version_str of this UpdatesPackageVersionInfo.  # noqa: E501
        :type: str
        """

        self._version_str = version_str

    @property
    def classification(self):
        """Gets the classification of this UpdatesPackageVersionInfo.  # noqa: E501


        :return: The classification of this UpdatesPackageVersionInfo.  # noqa: E501
        :rtype: UpdatesPackageVersionClass
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this UpdatesPackageVersionInfo.


        :param classification: The classification of this UpdatesPackageVersionInfo.  # noqa: E501
        :type: UpdatesPackageVersionClass
        """

        self._classification = classification

    @property
    def description(self):
        """Gets the description of this UpdatesPackageVersionInfo.  # noqa: E501


        :return: The description of this UpdatesPackageVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatesPackageVersionInfo.


        :param description: The description of this UpdatesPackageVersionInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def required_version_str(self):
        """Gets the required_version_str of this UpdatesPackageVersionInfo.  # noqa: E501


        :return: The required_version_str of this UpdatesPackageVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._required_version_str

    @required_version_str.setter
    def required_version_str(self, required_version_str):
        """Sets the required_version_str of this UpdatesPackageVersionInfo.


        :param required_version_str: The required_version_str of this UpdatesPackageVersionInfo.  # noqa: E501
        :type: str
        """

        self._required_version_str = required_version_str

    @property
    def source_url(self):
        """Gets the source_url of this UpdatesPackageVersionInfo.  # noqa: E501


        :return: The source_url of this UpdatesPackageVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """Sets the source_url of this UpdatesPackageVersionInfo.


        :param source_url: The source_url of this UpdatesPackageVersionInfo.  # noqa: E501
        :type: str
        """

        self._source_url = source_url

    @property
    def checksum(self):
        """Gets the checksum of this UpdatesPackageVersionInfo.  # noqa: E501


        :return: The checksum of this UpdatesPackageVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._checksum

    @checksum.setter
    def checksum(self, checksum):
        """Sets the checksum of this UpdatesPackageVersionInfo.


        :param checksum: The checksum of this UpdatesPackageVersionInfo.  # noqa: E501
        :type: str
        """

        self._checksum = checksum

    @property
    def target_filename(self):
        """Gets the target_filename of this UpdatesPackageVersionInfo.  # noqa: E501


        :return: The target_filename of this UpdatesPackageVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._target_filename

    @target_filename.setter
    def target_filename(self, target_filename):
        """Sets the target_filename of this UpdatesPackageVersionInfo.


        :param target_filename: The target_filename of this UpdatesPackageVersionInfo.  # noqa: E501
        :type: str
        """

        self._target_filename = target_filename

    @property
    def info_url(self):
        """Gets the info_url of this UpdatesPackageVersionInfo.  # noqa: E501


        :return: The info_url of this UpdatesPackageVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._info_url

    @info_url.setter
    def info_url(self, info_url):
        """Sets the info_url of this UpdatesPackageVersionInfo.


        :param info_url: The info_url of this UpdatesPackageVersionInfo.  # noqa: E501
        :type: str
        """

        self._info_url = info_url

    @property
    def runtimes(self):
        """Gets the runtimes of this UpdatesPackageVersionInfo.  # noqa: E501


        :return: The runtimes of this UpdatesPackageVersionInfo.  # noqa: E501
        :rtype: str
        """
        return self._runtimes

    @runtimes.setter
    def runtimes(self, runtimes):
        """Sets the runtimes of this UpdatesPackageVersionInfo.


        :param runtimes: The runtimes of this UpdatesPackageVersionInfo.  # noqa: E501
        :type: str
        """

        self._runtimes = runtimes

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
        if issubclass(UpdatesPackageVersionInfo, dict):
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
        if not isinstance(other, UpdatesPackageVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
