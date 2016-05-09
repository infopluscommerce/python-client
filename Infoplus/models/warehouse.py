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


class Warehouse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Warehouse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'client': 'int',
            'name': 'str',
            'address': 'str',
            'company': 'str',
            'street1': 'str',
            'street2': 'str',
            'street3': 'str',
            'city': 'str',
            'state': 'str',
            'zip': 'str',
            'country': 'str',
            'phone': 'str',
            'location_barcode_prefix': 'str',
            'lpn_prefix': 'str',
            'create_date': 'datetime',
            'modify_date': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'client': 'client',
            'name': 'name',
            'address': 'address',
            'company': 'company',
            'street1': 'street1',
            'street2': 'street2',
            'street3': 'street3',
            'city': 'city',
            'state': 'state',
            'zip': 'zip',
            'country': 'country',
            'phone': 'phone',
            'location_barcode_prefix': 'locationBarcodePrefix',
            'lpn_prefix': 'lpnPrefix',
            'create_date': 'createDate',
            'modify_date': 'modifyDate'
        }

        self._id = None
        self._client = None
        self._name = None
        self._address = None
        self._company = None
        self._street1 = None
        self._street2 = None
        self._street3 = None
        self._city = None
        self._state = None
        self._zip = None
        self._country = None
        self._phone = None
        self._location_barcode_prefix = None
        self._lpn_prefix = None
        self._create_date = None
        self._modify_date = None

    @property
    def id(self):
        """
        Gets the id of this Warehouse.


        :return: The id of this Warehouse.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Warehouse.


        :param id: The id of this Warehouse.
        :type: int
        """
        self._id = id

    @property
    def client(self):
        """
        Gets the client of this Warehouse.


        :return: The client of this Warehouse.
        :rtype: int
        """
        return self._client

    @client.setter
    def client(self, client):
        """
        Sets the client of this Warehouse.


        :param client: The client of this Warehouse.
        :type: int
        """
        self._client = client

    @property
    def name(self):
        """
        Gets the name of this Warehouse.


        :return: The name of this Warehouse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Warehouse.


        :param name: The name of this Warehouse.
        :type: str
        """
        self._name = name

    @property
    def address(self):
        """
        Gets the address of this Warehouse.


        :return: The address of this Warehouse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """
        Sets the address of this Warehouse.


        :param address: The address of this Warehouse.
        :type: str
        """
        self._address = address

    @property
    def company(self):
        """
        Gets the company of this Warehouse.


        :return: The company of this Warehouse.
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """
        Sets the company of this Warehouse.


        :param company: The company of this Warehouse.
        :type: str
        """
        self._company = company

    @property
    def street1(self):
        """
        Gets the street1 of this Warehouse.


        :return: The street1 of this Warehouse.
        :rtype: str
        """
        return self._street1

    @street1.setter
    def street1(self, street1):
        """
        Sets the street1 of this Warehouse.


        :param street1: The street1 of this Warehouse.
        :type: str
        """
        self._street1 = street1

    @property
    def street2(self):
        """
        Gets the street2 of this Warehouse.


        :return: The street2 of this Warehouse.
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """
        Sets the street2 of this Warehouse.


        :param street2: The street2 of this Warehouse.
        :type: str
        """
        self._street2 = street2

    @property
    def street3(self):
        """
        Gets the street3 of this Warehouse.


        :return: The street3 of this Warehouse.
        :rtype: str
        """
        return self._street3

    @street3.setter
    def street3(self, street3):
        """
        Sets the street3 of this Warehouse.


        :param street3: The street3 of this Warehouse.
        :type: str
        """
        self._street3 = street3

    @property
    def city(self):
        """
        Gets the city of this Warehouse.


        :return: The city of this Warehouse.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Warehouse.


        :param city: The city of this Warehouse.
        :type: str
        """
        self._city = city

    @property
    def state(self):
        """
        Gets the state of this Warehouse.


        :return: The state of this Warehouse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Warehouse.


        :param state: The state of this Warehouse.
        :type: str
        """
        self._state = state

    @property
    def zip(self):
        """
        Gets the zip of this Warehouse.


        :return: The zip of this Warehouse.
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """
        Sets the zip of this Warehouse.


        :param zip: The zip of this Warehouse.
        :type: str
        """
        self._zip = zip

    @property
    def country(self):
        """
        Gets the country of this Warehouse.


        :return: The country of this Warehouse.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Warehouse.


        :param country: The country of this Warehouse.
        :type: str
        """
        self._country = country

    @property
    def phone(self):
        """
        Gets the phone of this Warehouse.


        :return: The phone of this Warehouse.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Warehouse.


        :param phone: The phone of this Warehouse.
        :type: str
        """
        self._phone = phone

    @property
    def location_barcode_prefix(self):
        """
        Gets the location_barcode_prefix of this Warehouse.


        :return: The location_barcode_prefix of this Warehouse.
        :rtype: str
        """
        return self._location_barcode_prefix

    @location_barcode_prefix.setter
    def location_barcode_prefix(self, location_barcode_prefix):
        """
        Sets the location_barcode_prefix of this Warehouse.


        :param location_barcode_prefix: The location_barcode_prefix of this Warehouse.
        :type: str
        """
        self._location_barcode_prefix = location_barcode_prefix

    @property
    def lpn_prefix(self):
        """
        Gets the lpn_prefix of this Warehouse.


        :return: The lpn_prefix of this Warehouse.
        :rtype: str
        """
        return self._lpn_prefix

    @lpn_prefix.setter
    def lpn_prefix(self, lpn_prefix):
        """
        Sets the lpn_prefix of this Warehouse.


        :param lpn_prefix: The lpn_prefix of this Warehouse.
        :type: str
        """
        self._lpn_prefix = lpn_prefix

    @property
    def create_date(self):
        """
        Gets the create_date of this Warehouse.


        :return: The create_date of this Warehouse.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this Warehouse.


        :param create_date: The create_date of this Warehouse.
        :type: datetime
        """
        self._create_date = create_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this Warehouse.


        :return: The modify_date of this Warehouse.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this Warehouse.


        :param modify_date: The modify_date of this Warehouse.
        :type: datetime
        """
        self._modify_date = modify_date

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

