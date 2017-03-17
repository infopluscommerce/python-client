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


class Kit(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Kit - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'lob_id': 'int',
            'id': 'int',
            'kit_sku_id': 'int',
            'packaging_type': 'str',
            'other': 'str',
            'number_of_components': 'int',
            'create_date': 'datetime',
            'modify_date': 'datetime',
            'line1': 'str',
            'line2': 'str',
            'line3': 'str',
            'line4': 'str',
            'line5': 'str',
            'line6': 'str',
            'line7': 'str',
            'line8': 'str',
            'touches': 'int',
            'min_inv_qty': 'int',
            'mid_inv_qty': 'int',
            'max_inv_qty': 'int',
            'is_kod': 'str',
            'kod_type': 'str',
            'custom_fields': 'dict(str, object)'
        }

        self.attribute_map = {
            'lob_id': 'lobId',
            'id': 'id',
            'kit_sku_id': 'kitSKUId',
            'packaging_type': 'packagingType',
            'other': 'other',
            'number_of_components': 'numberOfComponents',
            'create_date': 'createDate',
            'modify_date': 'modifyDate',
            'line1': 'line1',
            'line2': 'line2',
            'line3': 'line3',
            'line4': 'line4',
            'line5': 'line5',
            'line6': 'line6',
            'line7': 'line7',
            'line8': 'line8',
            'touches': 'touches',
            'min_inv_qty': 'minInvQty',
            'mid_inv_qty': 'midInvQty',
            'max_inv_qty': 'maxInvQty',
            'is_kod': 'isKOD',
            'kod_type': 'kodType',
            'custom_fields': 'customFields'
        }

        self._lob_id = None
        self._id = None
        self._kit_sku_id = None
        self._packaging_type = None
        self._other = None
        self._number_of_components = None
        self._create_date = None
        self._modify_date = None
        self._line1 = None
        self._line2 = None
        self._line3 = None
        self._line4 = None
        self._line5 = None
        self._line6 = None
        self._line7 = None
        self._line8 = None
        self._touches = None
        self._min_inv_qty = None
        self._mid_inv_qty = None
        self._max_inv_qty = None
        self._is_kod = None
        self._kod_type = None
        self._custom_fields = None

    @property
    def lob_id(self):
        """
        Gets the lob_id of this Kit.


        :return: The lob_id of this Kit.
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """
        Sets the lob_id of this Kit.


        :param lob_id: The lob_id of this Kit.
        :type: int
        """
        self._lob_id = lob_id

    @property
    def id(self):
        """
        Gets the id of this Kit.


        :return: The id of this Kit.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Kit.


        :param id: The id of this Kit.
        :type: int
        """
        self._id = id

    @property
    def kit_sku_id(self):
        """
        Gets the kit_sku_id of this Kit.


        :return: The kit_sku_id of this Kit.
        :rtype: int
        """
        return self._kit_sku_id

    @kit_sku_id.setter
    def kit_sku_id(self, kit_sku_id):
        """
        Sets the kit_sku_id of this Kit.


        :param kit_sku_id: The kit_sku_id of this Kit.
        :type: int
        """
        self._kit_sku_id = kit_sku_id

    @property
    def packaging_type(self):
        """
        Gets the packaging_type of this Kit.


        :return: The packaging_type of this Kit.
        :rtype: str
        """
        return self._packaging_type

    @packaging_type.setter
    def packaging_type(self, packaging_type):
        """
        Sets the packaging_type of this Kit.


        :param packaging_type: The packaging_type of this Kit.
        :type: str
        """
        self._packaging_type = packaging_type

    @property
    def other(self):
        """
        Gets the other of this Kit.


        :return: The other of this Kit.
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        """
        Sets the other of this Kit.


        :param other: The other of this Kit.
        :type: str
        """
        self._other = other

    @property
    def number_of_components(self):
        """
        Gets the number_of_components of this Kit.


        :return: The number_of_components of this Kit.
        :rtype: int
        """
        return self._number_of_components

    @number_of_components.setter
    def number_of_components(self, number_of_components):
        """
        Sets the number_of_components of this Kit.


        :param number_of_components: The number_of_components of this Kit.
        :type: int
        """
        self._number_of_components = number_of_components

    @property
    def create_date(self):
        """
        Gets the create_date of this Kit.


        :return: The create_date of this Kit.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this Kit.


        :param create_date: The create_date of this Kit.
        :type: datetime
        """
        self._create_date = create_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this Kit.


        :return: The modify_date of this Kit.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this Kit.


        :param modify_date: The modify_date of this Kit.
        :type: datetime
        """
        self._modify_date = modify_date

    @property
    def line1(self):
        """
        Gets the line1 of this Kit.


        :return: The line1 of this Kit.
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """
        Sets the line1 of this Kit.


        :param line1: The line1 of this Kit.
        :type: str
        """
        self._line1 = line1

    @property
    def line2(self):
        """
        Gets the line2 of this Kit.


        :return: The line2 of this Kit.
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """
        Sets the line2 of this Kit.


        :param line2: The line2 of this Kit.
        :type: str
        """
        self._line2 = line2

    @property
    def line3(self):
        """
        Gets the line3 of this Kit.


        :return: The line3 of this Kit.
        :rtype: str
        """
        return self._line3

    @line3.setter
    def line3(self, line3):
        """
        Sets the line3 of this Kit.


        :param line3: The line3 of this Kit.
        :type: str
        """
        self._line3 = line3

    @property
    def line4(self):
        """
        Gets the line4 of this Kit.


        :return: The line4 of this Kit.
        :rtype: str
        """
        return self._line4

    @line4.setter
    def line4(self, line4):
        """
        Sets the line4 of this Kit.


        :param line4: The line4 of this Kit.
        :type: str
        """
        self._line4 = line4

    @property
    def line5(self):
        """
        Gets the line5 of this Kit.


        :return: The line5 of this Kit.
        :rtype: str
        """
        return self._line5

    @line5.setter
    def line5(self, line5):
        """
        Sets the line5 of this Kit.


        :param line5: The line5 of this Kit.
        :type: str
        """
        self._line5 = line5

    @property
    def line6(self):
        """
        Gets the line6 of this Kit.


        :return: The line6 of this Kit.
        :rtype: str
        """
        return self._line6

    @line6.setter
    def line6(self, line6):
        """
        Sets the line6 of this Kit.


        :param line6: The line6 of this Kit.
        :type: str
        """
        self._line6 = line6

    @property
    def line7(self):
        """
        Gets the line7 of this Kit.


        :return: The line7 of this Kit.
        :rtype: str
        """
        return self._line7

    @line7.setter
    def line7(self, line7):
        """
        Sets the line7 of this Kit.


        :param line7: The line7 of this Kit.
        :type: str
        """
        self._line7 = line7

    @property
    def line8(self):
        """
        Gets the line8 of this Kit.


        :return: The line8 of this Kit.
        :rtype: str
        """
        return self._line8

    @line8.setter
    def line8(self, line8):
        """
        Sets the line8 of this Kit.


        :param line8: The line8 of this Kit.
        :type: str
        """
        self._line8 = line8

    @property
    def touches(self):
        """
        Gets the touches of this Kit.


        :return: The touches of this Kit.
        :rtype: int
        """
        return self._touches

    @touches.setter
    def touches(self, touches):
        """
        Sets the touches of this Kit.


        :param touches: The touches of this Kit.
        :type: int
        """
        self._touches = touches

    @property
    def min_inv_qty(self):
        """
        Gets the min_inv_qty of this Kit.


        :return: The min_inv_qty of this Kit.
        :rtype: int
        """
        return self._min_inv_qty

    @min_inv_qty.setter
    def min_inv_qty(self, min_inv_qty):
        """
        Sets the min_inv_qty of this Kit.


        :param min_inv_qty: The min_inv_qty of this Kit.
        :type: int
        """
        self._min_inv_qty = min_inv_qty

    @property
    def mid_inv_qty(self):
        """
        Gets the mid_inv_qty of this Kit.


        :return: The mid_inv_qty of this Kit.
        :rtype: int
        """
        return self._mid_inv_qty

    @mid_inv_qty.setter
    def mid_inv_qty(self, mid_inv_qty):
        """
        Sets the mid_inv_qty of this Kit.


        :param mid_inv_qty: The mid_inv_qty of this Kit.
        :type: int
        """
        self._mid_inv_qty = mid_inv_qty

    @property
    def max_inv_qty(self):
        """
        Gets the max_inv_qty of this Kit.


        :return: The max_inv_qty of this Kit.
        :rtype: int
        """
        return self._max_inv_qty

    @max_inv_qty.setter
    def max_inv_qty(self, max_inv_qty):
        """
        Sets the max_inv_qty of this Kit.


        :param max_inv_qty: The max_inv_qty of this Kit.
        :type: int
        """
        self._max_inv_qty = max_inv_qty

    @property
    def is_kod(self):
        """
        Gets the is_kod of this Kit.


        :return: The is_kod of this Kit.
        :rtype: str
        """
        return self._is_kod

    @is_kod.setter
    def is_kod(self, is_kod):
        """
        Sets the is_kod of this Kit.


        :param is_kod: The is_kod of this Kit.
        :type: str
        """
        self._is_kod = is_kod

    @property
    def kod_type(self):
        """
        Gets the kod_type of this Kit.


        :return: The kod_type of this Kit.
        :rtype: str
        """
        return self._kod_type

    @kod_type.setter
    def kod_type(self, kod_type):
        """
        Sets the kod_type of this Kit.


        :param kod_type: The kod_type of this Kit.
        :type: str
        """
        self._kod_type = kod_type

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this Kit.


        :return: The custom_fields of this Kit.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this Kit.


        :param custom_fields: The custom_fields of this Kit.
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

