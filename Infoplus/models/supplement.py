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


class Supplement(object):
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
        'lob_id': 'int',
        'id': 'int',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'original_sku_id': 'int',
        'supplement_sku_id': 'int',
        'type': 'str',
        'supplement_quantity': 'float',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'lob_id': 'lobId',
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'original_sku_id': 'originalSKUId',
        'supplement_sku_id': 'supplementSKUId',
        'type': 'type',
        'supplement_quantity': 'supplementQuantity',
        'custom_fields': 'customFields'
    }

    def __init__(self, lob_id=None, id=None, create_date=None, modify_date=None, original_sku_id=None, supplement_sku_id=None, type=None, supplement_quantity=None, custom_fields=None):  # noqa: E501
        """Supplement - a model defined in Swagger"""  # noqa: E501

        self._lob_id = None
        self._id = None
        self._create_date = None
        self._modify_date = None
        self._original_sku_id = None
        self._supplement_sku_id = None
        self._type = None
        self._supplement_quantity = None
        self._custom_fields = None
        self.discriminator = None

        self.lob_id = lob_id
        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        self.original_sku_id = original_sku_id
        self.supplement_sku_id = supplement_sku_id
        self.type = type
        self.supplement_quantity = supplement_quantity
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def lob_id(self):
        """Gets the lob_id of this Supplement.  # noqa: E501


        :return: The lob_id of this Supplement.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this Supplement.


        :param lob_id: The lob_id of this Supplement.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def id(self):
        """Gets the id of this Supplement.  # noqa: E501


        :return: The id of this Supplement.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Supplement.


        :param id: The id of this Supplement.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this Supplement.  # noqa: E501


        :return: The create_date of this Supplement.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this Supplement.


        :param create_date: The create_date of this Supplement.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this Supplement.  # noqa: E501


        :return: The modify_date of this Supplement.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this Supplement.


        :param modify_date: The modify_date of this Supplement.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def original_sku_id(self):
        """Gets the original_sku_id of this Supplement.  # noqa: E501


        :return: The original_sku_id of this Supplement.  # noqa: E501
        :rtype: int
        """
        return self._original_sku_id

    @original_sku_id.setter
    def original_sku_id(self, original_sku_id):
        """Sets the original_sku_id of this Supplement.


        :param original_sku_id: The original_sku_id of this Supplement.  # noqa: E501
        :type: int
        """
        if original_sku_id is None:
            raise ValueError("Invalid value for `original_sku_id`, must not be `None`")  # noqa: E501

        self._original_sku_id = original_sku_id

    @property
    def supplement_sku_id(self):
        """Gets the supplement_sku_id of this Supplement.  # noqa: E501


        :return: The supplement_sku_id of this Supplement.  # noqa: E501
        :rtype: int
        """
        return self._supplement_sku_id

    @supplement_sku_id.setter
    def supplement_sku_id(self, supplement_sku_id):
        """Sets the supplement_sku_id of this Supplement.


        :param supplement_sku_id: The supplement_sku_id of this Supplement.  # noqa: E501
        :type: int
        """
        if supplement_sku_id is None:
            raise ValueError("Invalid value for `supplement_sku_id`, must not be `None`")  # noqa: E501

        self._supplement_sku_id = supplement_sku_id

    @property
    def type(self):
        """Gets the type of this Supplement.  # noqa: E501


        :return: The type of this Supplement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Supplement.


        :param type: The type of this Supplement.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def supplement_quantity(self):
        """Gets the supplement_quantity of this Supplement.  # noqa: E501


        :return: The supplement_quantity of this Supplement.  # noqa: E501
        :rtype: float
        """
        return self._supplement_quantity

    @supplement_quantity.setter
    def supplement_quantity(self, supplement_quantity):
        """Sets the supplement_quantity of this Supplement.


        :param supplement_quantity: The supplement_quantity of this Supplement.  # noqa: E501
        :type: float
        """
        if supplement_quantity is None:
            raise ValueError("Invalid value for `supplement_quantity`, must not be `None`")  # noqa: E501

        self._supplement_quantity = supplement_quantity

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Supplement.  # noqa: E501


        :return: The custom_fields of this Supplement.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Supplement.


        :param custom_fields: The custom_fields of this Supplement.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

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
        if not isinstance(other, Supplement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other