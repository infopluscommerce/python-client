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


class ReqManualSubstitutionInputAPIModel(object):
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
        'order_no_list': 'list[float]',
        'original_sku': 'str',
        'original_kit_sku': 'str',
        'original_quantity': 'int',
        'original_component_sku': 'str',
        'new_sku': 'str',
        'new_quantity': 'int',
        'edit_type': 'str'
    }

    attribute_map = {
        'order_no_list': 'orderNoList',
        'original_sku': 'originalSKU',
        'original_kit_sku': 'originalKitSKU',
        'original_quantity': 'originalQuantity',
        'original_component_sku': 'originalComponentSKU',
        'new_sku': 'newSKU',
        'new_quantity': 'newQuantity',
        'edit_type': 'editType'
    }

    def __init__(self, order_no_list=None, original_sku=None, original_kit_sku=None, original_quantity=None, original_component_sku=None, new_sku=None, new_quantity=None, edit_type=None):  # noqa: E501
        """ReqManualSubstitutionInputAPIModel - a model defined in Swagger"""  # noqa: E501

        self._order_no_list = None
        self._original_sku = None
        self._original_kit_sku = None
        self._original_quantity = None
        self._original_component_sku = None
        self._new_sku = None
        self._new_quantity = None
        self._edit_type = None
        self.discriminator = None

        if order_no_list is not None:
            self.order_no_list = order_no_list
        if original_sku is not None:
            self.original_sku = original_sku
        if original_kit_sku is not None:
            self.original_kit_sku = original_kit_sku
        if original_quantity is not None:
            self.original_quantity = original_quantity
        if original_component_sku is not None:
            self.original_component_sku = original_component_sku
        if new_sku is not None:
            self.new_sku = new_sku
        if new_quantity is not None:
            self.new_quantity = new_quantity
        self.edit_type = edit_type

    @property
    def order_no_list(self):
        """Gets the order_no_list of this ReqManualSubstitutionInputAPIModel.  # noqa: E501


        :return: The order_no_list of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :rtype: list[float]
        """
        return self._order_no_list

    @order_no_list.setter
    def order_no_list(self, order_no_list):
        """Sets the order_no_list of this ReqManualSubstitutionInputAPIModel.


        :param order_no_list: The order_no_list of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :type: list[float]
        """

        self._order_no_list = order_no_list

    @property
    def original_sku(self):
        """Gets the original_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501


        :return: The original_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :rtype: str
        """
        return self._original_sku

    @original_sku.setter
    def original_sku(self, original_sku):
        """Sets the original_sku of this ReqManualSubstitutionInputAPIModel.


        :param original_sku: The original_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :type: str
        """

        self._original_sku = original_sku

    @property
    def original_kit_sku(self):
        """Gets the original_kit_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501


        :return: The original_kit_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :rtype: str
        """
        return self._original_kit_sku

    @original_kit_sku.setter
    def original_kit_sku(self, original_kit_sku):
        """Sets the original_kit_sku of this ReqManualSubstitutionInputAPIModel.


        :param original_kit_sku: The original_kit_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :type: str
        """

        self._original_kit_sku = original_kit_sku

    @property
    def original_quantity(self):
        """Gets the original_quantity of this ReqManualSubstitutionInputAPIModel.  # noqa: E501


        :return: The original_quantity of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :rtype: int
        """
        return self._original_quantity

    @original_quantity.setter
    def original_quantity(self, original_quantity):
        """Sets the original_quantity of this ReqManualSubstitutionInputAPIModel.


        :param original_quantity: The original_quantity of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :type: int
        """

        self._original_quantity = original_quantity

    @property
    def original_component_sku(self):
        """Gets the original_component_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501


        :return: The original_component_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :rtype: str
        """
        return self._original_component_sku

    @original_component_sku.setter
    def original_component_sku(self, original_component_sku):
        """Sets the original_component_sku of this ReqManualSubstitutionInputAPIModel.


        :param original_component_sku: The original_component_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :type: str
        """

        self._original_component_sku = original_component_sku

    @property
    def new_sku(self):
        """Gets the new_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501


        :return: The new_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :rtype: str
        """
        return self._new_sku

    @new_sku.setter
    def new_sku(self, new_sku):
        """Sets the new_sku of this ReqManualSubstitutionInputAPIModel.


        :param new_sku: The new_sku of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :type: str
        """

        self._new_sku = new_sku

    @property
    def new_quantity(self):
        """Gets the new_quantity of this ReqManualSubstitutionInputAPIModel.  # noqa: E501


        :return: The new_quantity of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :rtype: int
        """
        return self._new_quantity

    @new_quantity.setter
    def new_quantity(self, new_quantity):
        """Sets the new_quantity of this ReqManualSubstitutionInputAPIModel.


        :param new_quantity: The new_quantity of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :type: int
        """

        self._new_quantity = new_quantity

    @property
    def edit_type(self):
        """Gets the edit_type of this ReqManualSubstitutionInputAPIModel.  # noqa: E501


        :return: The edit_type of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :rtype: str
        """
        return self._edit_type

    @edit_type.setter
    def edit_type(self, edit_type):
        """Sets the edit_type of this ReqManualSubstitutionInputAPIModel.


        :param edit_type: The edit_type of this ReqManualSubstitutionInputAPIModel.  # noqa: E501
        :type: str
        """
        if edit_type is None:
            raise ValueError("Invalid value for `edit_type`, must not be `None`")  # noqa: E501

        self._edit_type = edit_type

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
        if not isinstance(other, ReqManualSubstitutionInputAPIModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
