# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from Infoplus.models.order import Order  # noqa: F401,E501
from Infoplus.models.packed_carton import PackedCarton  # noqa: F401,E501
from Infoplus.models.packed_item import PackedItem  # noqa: F401,E501
from Infoplus.models.packed_master_carton import PackedMasterCarton  # noqa: F401,E501
from Infoplus.models.packed_pallet import PackedPallet  # noqa: F401,E501


class GetOrderPackDataOutput(object):
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
        'order_no': 'str',
        'order': 'Order',
        'pallet_list': 'list[PackedPallet]',
        'master_carton_list': 'list[PackedMasterCarton]',
        'carton_list': 'list[PackedCarton]',
        'full_item_list': 'list[PackedItem]',
        'unpacked_item_list': 'list[PackedItem]'
    }

    attribute_map = {
        'order_no': 'orderNo',
        'order': 'order',
        'pallet_list': 'palletList',
        'master_carton_list': 'masterCartonList',
        'carton_list': 'cartonList',
        'full_item_list': 'fullItemList',
        'unpacked_item_list': 'unpackedItemList'
    }

    def __init__(self, order_no=None, order=None, pallet_list=None, master_carton_list=None, carton_list=None, full_item_list=None, unpacked_item_list=None):  # noqa: E501
        """GetOrderPackDataOutput - a model defined in Swagger"""  # noqa: E501

        self._order_no = None
        self._order = None
        self._pallet_list = None
        self._master_carton_list = None
        self._carton_list = None
        self._full_item_list = None
        self._unpacked_item_list = None
        self.discriminator = None

        if order_no is not None:
            self.order_no = order_no
        if order is not None:
            self.order = order
        if pallet_list is not None:
            self.pallet_list = pallet_list
        if master_carton_list is not None:
            self.master_carton_list = master_carton_list
        if carton_list is not None:
            self.carton_list = carton_list
        if full_item_list is not None:
            self.full_item_list = full_item_list
        if unpacked_item_list is not None:
            self.unpacked_item_list = unpacked_item_list

    @property
    def order_no(self):
        """Gets the order_no of this GetOrderPackDataOutput.  # noqa: E501


        :return: The order_no of this GetOrderPackDataOutput.  # noqa: E501
        :rtype: str
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """Sets the order_no of this GetOrderPackDataOutput.


        :param order_no: The order_no of this GetOrderPackDataOutput.  # noqa: E501
        :type: str
        """

        self._order_no = order_no

    @property
    def order(self):
        """Gets the order of this GetOrderPackDataOutput.  # noqa: E501


        :return: The order of this GetOrderPackDataOutput.  # noqa: E501
        :rtype: Order
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this GetOrderPackDataOutput.


        :param order: The order of this GetOrderPackDataOutput.  # noqa: E501
        :type: Order
        """

        self._order = order

    @property
    def pallet_list(self):
        """Gets the pallet_list of this GetOrderPackDataOutput.  # noqa: E501


        :return: The pallet_list of this GetOrderPackDataOutput.  # noqa: E501
        :rtype: list[PackedPallet]
        """
        return self._pallet_list

    @pallet_list.setter
    def pallet_list(self, pallet_list):
        """Sets the pallet_list of this GetOrderPackDataOutput.


        :param pallet_list: The pallet_list of this GetOrderPackDataOutput.  # noqa: E501
        :type: list[PackedPallet]
        """

        self._pallet_list = pallet_list

    @property
    def master_carton_list(self):
        """Gets the master_carton_list of this GetOrderPackDataOutput.  # noqa: E501


        :return: The master_carton_list of this GetOrderPackDataOutput.  # noqa: E501
        :rtype: list[PackedMasterCarton]
        """
        return self._master_carton_list

    @master_carton_list.setter
    def master_carton_list(self, master_carton_list):
        """Sets the master_carton_list of this GetOrderPackDataOutput.


        :param master_carton_list: The master_carton_list of this GetOrderPackDataOutput.  # noqa: E501
        :type: list[PackedMasterCarton]
        """

        self._master_carton_list = master_carton_list

    @property
    def carton_list(self):
        """Gets the carton_list of this GetOrderPackDataOutput.  # noqa: E501


        :return: The carton_list of this GetOrderPackDataOutput.  # noqa: E501
        :rtype: list[PackedCarton]
        """
        return self._carton_list

    @carton_list.setter
    def carton_list(self, carton_list):
        """Sets the carton_list of this GetOrderPackDataOutput.


        :param carton_list: The carton_list of this GetOrderPackDataOutput.  # noqa: E501
        :type: list[PackedCarton]
        """

        self._carton_list = carton_list

    @property
    def full_item_list(self):
        """Gets the full_item_list of this GetOrderPackDataOutput.  # noqa: E501


        :return: The full_item_list of this GetOrderPackDataOutput.  # noqa: E501
        :rtype: list[PackedItem]
        """
        return self._full_item_list

    @full_item_list.setter
    def full_item_list(self, full_item_list):
        """Sets the full_item_list of this GetOrderPackDataOutput.


        :param full_item_list: The full_item_list of this GetOrderPackDataOutput.  # noqa: E501
        :type: list[PackedItem]
        """

        self._full_item_list = full_item_list

    @property
    def unpacked_item_list(self):
        """Gets the unpacked_item_list of this GetOrderPackDataOutput.  # noqa: E501


        :return: The unpacked_item_list of this GetOrderPackDataOutput.  # noqa: E501
        :rtype: list[PackedItem]
        """
        return self._unpacked_item_list

    @unpacked_item_list.setter
    def unpacked_item_list(self, unpacked_item_list):
        """Sets the unpacked_item_list of this GetOrderPackDataOutput.


        :param unpacked_item_list: The unpacked_item_list of this GetOrderPackDataOutput.  # noqa: E501
        :type: list[PackedItem]
        """

        self._unpacked_item_list = unpacked_item_list

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
        if not isinstance(other, GetOrderPackDataOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other