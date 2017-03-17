# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Substitution(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Substitution - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'lob_id': 'int',
            'create_date': 'datetime',
            'modify_date': 'datetime',
            'id': 'int',
            'order_sku_id': 'int',
            'substitute_sku_id': 'int',
            'period': 'str',
            'type': 'str',
            'substitution_quantity': 'float',
            'custom_fields': 'dict(str, object)'
        }

        self.attribute_map = {
            'lob_id': 'lobId',
            'create_date': 'createDate',
            'modify_date': 'modifyDate',
            'id': 'id',
            'order_sku_id': 'orderSKUId',
            'substitute_sku_id': 'substituteSKUId',
            'period': 'period',
            'type': 'type',
            'substitution_quantity': 'substitutionQuantity',
            'custom_fields': 'customFields'
        }

        self._lob_id = None
        self._create_date = None
        self._modify_date = None
        self._id = None
        self._order_sku_id = None
        self._substitute_sku_id = None
        self._period = None
        self._type = None
        self._substitution_quantity = None
        self._custom_fields = None

    @property
    def lob_id(self):
        """
        Gets the lob_id of this Substitution.


        :return: The lob_id of this Substitution.
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """
        Sets the lob_id of this Substitution.


        :param lob_id: The lob_id of this Substitution.
        :type: int
        """
        self._lob_id = lob_id

    @property
    def create_date(self):
        """
        Gets the create_date of this Substitution.


        :return: The create_date of this Substitution.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this Substitution.


        :param create_date: The create_date of this Substitution.
        :type: datetime
        """
        self._create_date = create_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this Substitution.


        :return: The modify_date of this Substitution.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this Substitution.


        :param modify_date: The modify_date of this Substitution.
        :type: datetime
        """
        self._modify_date = modify_date

    @property
    def id(self):
        """
        Gets the id of this Substitution.


        :return: The id of this Substitution.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Substitution.


        :param id: The id of this Substitution.
        :type: int
        """
        self._id = id

    @property
    def order_sku_id(self):
        """
        Gets the order_sku_id of this Substitution.


        :return: The order_sku_id of this Substitution.
        :rtype: int
        """
        return self._order_sku_id

    @order_sku_id.setter
    def order_sku_id(self, order_sku_id):
        """
        Sets the order_sku_id of this Substitution.


        :param order_sku_id: The order_sku_id of this Substitution.
        :type: int
        """
        self._order_sku_id = order_sku_id

    @property
    def substitute_sku_id(self):
        """
        Gets the substitute_sku_id of this Substitution.


        :return: The substitute_sku_id of this Substitution.
        :rtype: int
        """
        return self._substitute_sku_id

    @substitute_sku_id.setter
    def substitute_sku_id(self, substitute_sku_id):
        """
        Sets the substitute_sku_id of this Substitution.


        :param substitute_sku_id: The substitute_sku_id of this Substitution.
        :type: int
        """
        self._substitute_sku_id = substitute_sku_id

    @property
    def period(self):
        """
        Gets the period of this Substitution.


        :return: The period of this Substitution.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Sets the period of this Substitution.


        :param period: The period of this Substitution.
        :type: str
        """
        self._period = period

    @property
    def type(self):
        """
        Gets the type of this Substitution.


        :return: The type of this Substitution.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Substitution.


        :param type: The type of this Substitution.
        :type: str
        """
        self._type = type

    @property
    def substitution_quantity(self):
        """
        Gets the substitution_quantity of this Substitution.


        :return: The substitution_quantity of this Substitution.
        :rtype: float
        """
        return self._substitution_quantity

    @substitution_quantity.setter
    def substitution_quantity(self, substitution_quantity):
        """
        Sets the substitution_quantity of this Substitution.


        :param substitution_quantity: The substitution_quantity of this Substitution.
        :type: float
        """
        self._substitution_quantity = substitution_quantity

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this Substitution.


        :return: The custom_fields of this Substitution.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this Substitution.


        :param custom_fields: The custom_fields of this Substitution.
        :type: dict(str, object)
        """
        self._custom_fields = custom_fields

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

