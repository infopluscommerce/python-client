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


class BillOfLadingCarrierInfoLine(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        BillOfLadingCarrierInfoLine - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'seq_no': 'int',
            'hu_quantity': 'int',
            'hu_type': 'str',
            'package_quantity': 'int',
            'package_type': 'str',
            'weight': 'int',
            'is_hazardous_material': 'bool',
            'commodity_description': 'str',
            'nfmc_no': 'str',
            'carrier_class': 'str'
        }

        self.attribute_map = {
            'seq_no': 'seqNo',
            'hu_quantity': 'huQuantity',
            'hu_type': 'huType',
            'package_quantity': 'packageQuantity',
            'package_type': 'packageType',
            'weight': 'weight',
            'is_hazardous_material': 'isHazardousMaterial',
            'commodity_description': 'commodityDescription',
            'nfmc_no': 'nfmcNo',
            'carrier_class': 'carrierClass'
        }

        self._seq_no = None
        self._hu_quantity = None
        self._hu_type = None
        self._package_quantity = None
        self._package_type = None
        self._weight = None
        self._is_hazardous_material = False
        self._commodity_description = None
        self._nfmc_no = None
        self._carrier_class = None

    @property
    def seq_no(self):
        """
        Gets the seq_no of this BillOfLadingCarrierInfoLine.


        :return: The seq_no of this BillOfLadingCarrierInfoLine.
        :rtype: int
        """
        return self._seq_no

    @seq_no.setter
    def seq_no(self, seq_no):
        """
        Sets the seq_no of this BillOfLadingCarrierInfoLine.


        :param seq_no: The seq_no of this BillOfLadingCarrierInfoLine.
        :type: int
        """
        self._seq_no = seq_no

    @property
    def hu_quantity(self):
        """
        Gets the hu_quantity of this BillOfLadingCarrierInfoLine.


        :return: The hu_quantity of this BillOfLadingCarrierInfoLine.
        :rtype: int
        """
        return self._hu_quantity

    @hu_quantity.setter
    def hu_quantity(self, hu_quantity):
        """
        Sets the hu_quantity of this BillOfLadingCarrierInfoLine.


        :param hu_quantity: The hu_quantity of this BillOfLadingCarrierInfoLine.
        :type: int
        """
        self._hu_quantity = hu_quantity

    @property
    def hu_type(self):
        """
        Gets the hu_type of this BillOfLadingCarrierInfoLine.


        :return: The hu_type of this BillOfLadingCarrierInfoLine.
        :rtype: str
        """
        return self._hu_type

    @hu_type.setter
    def hu_type(self, hu_type):
        """
        Sets the hu_type of this BillOfLadingCarrierInfoLine.


        :param hu_type: The hu_type of this BillOfLadingCarrierInfoLine.
        :type: str
        """
        self._hu_type = hu_type

    @property
    def package_quantity(self):
        """
        Gets the package_quantity of this BillOfLadingCarrierInfoLine.


        :return: The package_quantity of this BillOfLadingCarrierInfoLine.
        :rtype: int
        """
        return self._package_quantity

    @package_quantity.setter
    def package_quantity(self, package_quantity):
        """
        Sets the package_quantity of this BillOfLadingCarrierInfoLine.


        :param package_quantity: The package_quantity of this BillOfLadingCarrierInfoLine.
        :type: int
        """
        self._package_quantity = package_quantity

    @property
    def package_type(self):
        """
        Gets the package_type of this BillOfLadingCarrierInfoLine.


        :return: The package_type of this BillOfLadingCarrierInfoLine.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        """
        Sets the package_type of this BillOfLadingCarrierInfoLine.


        :param package_type: The package_type of this BillOfLadingCarrierInfoLine.
        :type: str
        """
        self._package_type = package_type

    @property
    def weight(self):
        """
        Gets the weight of this BillOfLadingCarrierInfoLine.


        :return: The weight of this BillOfLadingCarrierInfoLine.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """
        Sets the weight of this BillOfLadingCarrierInfoLine.


        :param weight: The weight of this BillOfLadingCarrierInfoLine.
        :type: int
        """
        self._weight = weight

    @property
    def is_hazardous_material(self):
        """
        Gets the is_hazardous_material of this BillOfLadingCarrierInfoLine.


        :return: The is_hazardous_material of this BillOfLadingCarrierInfoLine.
        :rtype: bool
        """
        return self._is_hazardous_material

    @is_hazardous_material.setter
    def is_hazardous_material(self, is_hazardous_material):
        """
        Sets the is_hazardous_material of this BillOfLadingCarrierInfoLine.


        :param is_hazardous_material: The is_hazardous_material of this BillOfLadingCarrierInfoLine.
        :type: bool
        """
        self._is_hazardous_material = is_hazardous_material

    @property
    def commodity_description(self):
        """
        Gets the commodity_description of this BillOfLadingCarrierInfoLine.


        :return: The commodity_description of this BillOfLadingCarrierInfoLine.
        :rtype: str
        """
        return self._commodity_description

    @commodity_description.setter
    def commodity_description(self, commodity_description):
        """
        Sets the commodity_description of this BillOfLadingCarrierInfoLine.


        :param commodity_description: The commodity_description of this BillOfLadingCarrierInfoLine.
        :type: str
        """
        self._commodity_description = commodity_description

    @property
    def nfmc_no(self):
        """
        Gets the nfmc_no of this BillOfLadingCarrierInfoLine.


        :return: The nfmc_no of this BillOfLadingCarrierInfoLine.
        :rtype: str
        """
        return self._nfmc_no

    @nfmc_no.setter
    def nfmc_no(self, nfmc_no):
        """
        Sets the nfmc_no of this BillOfLadingCarrierInfoLine.


        :param nfmc_no: The nfmc_no of this BillOfLadingCarrierInfoLine.
        :type: str
        """
        self._nfmc_no = nfmc_no

    @property
    def carrier_class(self):
        """
        Gets the carrier_class of this BillOfLadingCarrierInfoLine.


        :return: The carrier_class of this BillOfLadingCarrierInfoLine.
        :rtype: str
        """
        return self._carrier_class

    @carrier_class.setter
    def carrier_class(self, carrier_class):
        """
        Sets the carrier_class of this BillOfLadingCarrierInfoLine.


        :param carrier_class: The carrier_class of this BillOfLadingCarrierInfoLine.
        :type: str
        """
        self._carrier_class = carrier_class

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

