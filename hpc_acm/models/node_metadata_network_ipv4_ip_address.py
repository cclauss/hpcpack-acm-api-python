# coding: utf-8

"""
    HPC Web API

    Preview  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from hpc_acm.models.ip_v4 import IpV4  # noqa: F401,E501


class NodeMetadataNetworkIpv4IpAddress(object):
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
        'private_ip_address': 'IpV4',
        'public_ip_address': 'IpV4'
    }

    attribute_map = {
        'private_ip_address': 'privateIpAddress',
        'public_ip_address': 'publicIpAddress'
    }

    def __init__(self, private_ip_address=None, public_ip_address=None):  # noqa: E501
        """NodeMetadataNetworkIpv4IpAddress - a model defined in Swagger"""  # noqa: E501

        self._private_ip_address = None
        self._public_ip_address = None
        self.discriminator = None

        if private_ip_address is not None:
            self.private_ip_address = private_ip_address
        if public_ip_address is not None:
            self.public_ip_address = public_ip_address

    @property
    def private_ip_address(self):
        """Gets the private_ip_address of this NodeMetadataNetworkIpv4IpAddress.  # noqa: E501


        :return: The private_ip_address of this NodeMetadataNetworkIpv4IpAddress.  # noqa: E501
        :rtype: IpV4
        """
        return self._private_ip_address

    @private_ip_address.setter
    def private_ip_address(self, private_ip_address):
        """Sets the private_ip_address of this NodeMetadataNetworkIpv4IpAddress.


        :param private_ip_address: The private_ip_address of this NodeMetadataNetworkIpv4IpAddress.  # noqa: E501
        :type: IpV4
        """

        self._private_ip_address = private_ip_address

    @property
    def public_ip_address(self):
        """Gets the public_ip_address of this NodeMetadataNetworkIpv4IpAddress.  # noqa: E501


        :return: The public_ip_address of this NodeMetadataNetworkIpv4IpAddress.  # noqa: E501
        :rtype: IpV4
        """
        return self._public_ip_address

    @public_ip_address.setter
    def public_ip_address(self, public_ip_address):
        """Sets the public_ip_address of this NodeMetadataNetworkIpv4IpAddress.


        :param public_ip_address: The public_ip_address of this NodeMetadataNetworkIpv4IpAddress.  # noqa: E501
        :type: IpV4
        """

        self._public_ip_address = public_ip_address

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodeMetadataNetworkIpv4IpAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
