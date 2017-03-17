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


class Vendor(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Vendor - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'vendor_no': 'int',
            'lob_id': 'int',
            'name': 'str',
            'street': 'str',
            'street2': 'str',
            'city': 'str',
            'state': 'str',
            'country': 'str',
            'zip_code': 'str',
            'contact': 'str',
            'phone': 'str',
            'fax': 'str',
            'external_id': 'str',
            'terms': 'str',
            'fob': 'str',
            'ship_via': 'int',
            'request_days': 'int',
            'actual_days': 'int',
            'sales_tax_code': 'str',
            'product1': 'int',
            'product2': 'int',
            'product3': 'int',
            'product4': 'int',
            'product5': 'int',
            'product6': 'int',
            'product7': 'int',
            'product8': 'int',
            'product9': 'int',
            'pod_days': 'int',
            'charge_out': 'str',
            'ar_email': 'str',
            'order_email': 'str',
            'order_attach': 'str',
            'send_quantity_type': 'str',
            'minority': 'str',
            'send_outside': 'str',
            'pod_order_suffix': 'int',
            'pod_email': 'str',
            'create_date': 'datetime',
            'modify_date': 'datetime',
            'inactive': 'str',
            'custom_fields': 'dict(str, object)'
        }

        self.attribute_map = {
            'id': 'id',
            'vendor_no': 'vendorNo',
            'lob_id': 'lobId',
            'name': 'name',
            'street': 'street',
            'street2': 'street2',
            'city': 'city',
            'state': 'state',
            'country': 'country',
            'zip_code': 'zipCode',
            'contact': 'contact',
            'phone': 'phone',
            'fax': 'fax',
            'external_id': 'externalId',
            'terms': 'terms',
            'fob': 'fob',
            'ship_via': 'shipVia',
            'request_days': 'requestDays',
            'actual_days': 'actualDays',
            'sales_tax_code': 'salesTaxCode',
            'product1': 'product1',
            'product2': 'product2',
            'product3': 'product3',
            'product4': 'product4',
            'product5': 'product5',
            'product6': 'product6',
            'product7': 'product7',
            'product8': 'product8',
            'product9': 'product9',
            'pod_days': 'podDays',
            'charge_out': 'chargeOut',
            'ar_email': 'arEmail',
            'order_email': 'orderEmail',
            'order_attach': 'orderAttach',
            'send_quantity_type': 'sendQuantityType',
            'minority': 'minority',
            'send_outside': 'sendOutside',
            'pod_order_suffix': 'podOrderSuffix',
            'pod_email': 'podEmail',
            'create_date': 'createDate',
            'modify_date': 'modifyDate',
            'inactive': 'inactive',
            'custom_fields': 'customFields'
        }

        self._id = None
        self._vendor_no = None
        self._lob_id = None
        self._name = None
        self._street = None
        self._street2 = None
        self._city = None
        self._state = None
        self._country = None
        self._zip_code = None
        self._contact = None
        self._phone = None
        self._fax = None
        self._external_id = None
        self._terms = None
        self._fob = None
        self._ship_via = None
        self._request_days = None
        self._actual_days = None
        self._sales_tax_code = None
        self._product1 = None
        self._product2 = None
        self._product3 = None
        self._product4 = None
        self._product5 = None
        self._product6 = None
        self._product7 = None
        self._product8 = None
        self._product9 = None
        self._pod_days = None
        self._charge_out = None
        self._ar_email = None
        self._order_email = None
        self._order_attach = None
        self._send_quantity_type = None
        self._minority = None
        self._send_outside = None
        self._pod_order_suffix = None
        self._pod_email = None
        self._create_date = None
        self._modify_date = None
        self._inactive = None
        self._custom_fields = None

    @property
    def id(self):
        """
        Gets the id of this Vendor.


        :return: The id of this Vendor.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Vendor.


        :param id: The id of this Vendor.
        :type: int
        """
        self._id = id

    @property
    def vendor_no(self):
        """
        Gets the vendor_no of this Vendor.


        :return: The vendor_no of this Vendor.
        :rtype: int
        """
        return self._vendor_no

    @vendor_no.setter
    def vendor_no(self, vendor_no):
        """
        Sets the vendor_no of this Vendor.


        :param vendor_no: The vendor_no of this Vendor.
        :type: int
        """
        self._vendor_no = vendor_no

    @property
    def lob_id(self):
        """
        Gets the lob_id of this Vendor.


        :return: The lob_id of this Vendor.
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """
        Sets the lob_id of this Vendor.


        :param lob_id: The lob_id of this Vendor.
        :type: int
        """
        self._lob_id = lob_id

    @property
    def name(self):
        """
        Gets the name of this Vendor.


        :return: The name of this Vendor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Vendor.


        :param name: The name of this Vendor.
        :type: str
        """
        self._name = name

    @property
    def street(self):
        """
        Gets the street of this Vendor.


        :return: The street of this Vendor.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """
        Sets the street of this Vendor.


        :param street: The street of this Vendor.
        :type: str
        """
        self._street = street

    @property
    def street2(self):
        """
        Gets the street2 of this Vendor.


        :return: The street2 of this Vendor.
        :rtype: str
        """
        return self._street2

    @street2.setter
    def street2(self, street2):
        """
        Sets the street2 of this Vendor.


        :param street2: The street2 of this Vendor.
        :type: str
        """
        self._street2 = street2

    @property
    def city(self):
        """
        Gets the city of this Vendor.


        :return: The city of this Vendor.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Vendor.


        :param city: The city of this Vendor.
        :type: str
        """
        self._city = city

    @property
    def state(self):
        """
        Gets the state of this Vendor.


        :return: The state of this Vendor.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this Vendor.


        :param state: The state of this Vendor.
        :type: str
        """
        self._state = state

    @property
    def country(self):
        """
        Gets the country of this Vendor.


        :return: The country of this Vendor.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Vendor.


        :param country: The country of this Vendor.
        :type: str
        """
        self._country = country

    @property
    def zip_code(self):
        """
        Gets the zip_code of this Vendor.


        :return: The zip_code of this Vendor.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """
        Sets the zip_code of this Vendor.


        :param zip_code: The zip_code of this Vendor.
        :type: str
        """
        self._zip_code = zip_code

    @property
    def contact(self):
        """
        Gets the contact of this Vendor.


        :return: The contact of this Vendor.
        :rtype: str
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """
        Sets the contact of this Vendor.


        :param contact: The contact of this Vendor.
        :type: str
        """
        self._contact = contact

    @property
    def phone(self):
        """
        Gets the phone of this Vendor.


        :return: The phone of this Vendor.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Vendor.


        :param phone: The phone of this Vendor.
        :type: str
        """
        self._phone = phone

    @property
    def fax(self):
        """
        Gets the fax of this Vendor.


        :return: The fax of this Vendor.
        :rtype: str
        """
        return self._fax

    @fax.setter
    def fax(self, fax):
        """
        Sets the fax of this Vendor.


        :param fax: The fax of this Vendor.
        :type: str
        """
        self._fax = fax

    @property
    def external_id(self):
        """
        Gets the external_id of this Vendor.


        :return: The external_id of this Vendor.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """
        Sets the external_id of this Vendor.


        :param external_id: The external_id of this Vendor.
        :type: str
        """
        self._external_id = external_id

    @property
    def terms(self):
        """
        Gets the terms of this Vendor.


        :return: The terms of this Vendor.
        :rtype: str
        """
        return self._terms

    @terms.setter
    def terms(self, terms):
        """
        Sets the terms of this Vendor.


        :param terms: The terms of this Vendor.
        :type: str
        """
        self._terms = terms

    @property
    def fob(self):
        """
        Gets the fob of this Vendor.


        :return: The fob of this Vendor.
        :rtype: str
        """
        return self._fob

    @fob.setter
    def fob(self, fob):
        """
        Sets the fob of this Vendor.


        :param fob: The fob of this Vendor.
        :type: str
        """
        self._fob = fob

    @property
    def ship_via(self):
        """
        Gets the ship_via of this Vendor.


        :return: The ship_via of this Vendor.
        :rtype: int
        """
        return self._ship_via

    @ship_via.setter
    def ship_via(self, ship_via):
        """
        Sets the ship_via of this Vendor.


        :param ship_via: The ship_via of this Vendor.
        :type: int
        """
        self._ship_via = ship_via

    @property
    def request_days(self):
        """
        Gets the request_days of this Vendor.


        :return: The request_days of this Vendor.
        :rtype: int
        """
        return self._request_days

    @request_days.setter
    def request_days(self, request_days):
        """
        Sets the request_days of this Vendor.


        :param request_days: The request_days of this Vendor.
        :type: int
        """
        self._request_days = request_days

    @property
    def actual_days(self):
        """
        Gets the actual_days of this Vendor.


        :return: The actual_days of this Vendor.
        :rtype: int
        """
        return self._actual_days

    @actual_days.setter
    def actual_days(self, actual_days):
        """
        Sets the actual_days of this Vendor.


        :param actual_days: The actual_days of this Vendor.
        :type: int
        """
        self._actual_days = actual_days

    @property
    def sales_tax_code(self):
        """
        Gets the sales_tax_code of this Vendor.


        :return: The sales_tax_code of this Vendor.
        :rtype: str
        """
        return self._sales_tax_code

    @sales_tax_code.setter
    def sales_tax_code(self, sales_tax_code):
        """
        Sets the sales_tax_code of this Vendor.


        :param sales_tax_code: The sales_tax_code of this Vendor.
        :type: str
        """
        self._sales_tax_code = sales_tax_code

    @property
    def product1(self):
        """
        Gets the product1 of this Vendor.


        :return: The product1 of this Vendor.
        :rtype: int
        """
        return self._product1

    @product1.setter
    def product1(self, product1):
        """
        Sets the product1 of this Vendor.


        :param product1: The product1 of this Vendor.
        :type: int
        """
        self._product1 = product1

    @property
    def product2(self):
        """
        Gets the product2 of this Vendor.


        :return: The product2 of this Vendor.
        :rtype: int
        """
        return self._product2

    @product2.setter
    def product2(self, product2):
        """
        Sets the product2 of this Vendor.


        :param product2: The product2 of this Vendor.
        :type: int
        """
        self._product2 = product2

    @property
    def product3(self):
        """
        Gets the product3 of this Vendor.


        :return: The product3 of this Vendor.
        :rtype: int
        """
        return self._product3

    @product3.setter
    def product3(self, product3):
        """
        Sets the product3 of this Vendor.


        :param product3: The product3 of this Vendor.
        :type: int
        """
        self._product3 = product3

    @property
    def product4(self):
        """
        Gets the product4 of this Vendor.


        :return: The product4 of this Vendor.
        :rtype: int
        """
        return self._product4

    @product4.setter
    def product4(self, product4):
        """
        Sets the product4 of this Vendor.


        :param product4: The product4 of this Vendor.
        :type: int
        """
        self._product4 = product4

    @property
    def product5(self):
        """
        Gets the product5 of this Vendor.


        :return: The product5 of this Vendor.
        :rtype: int
        """
        return self._product5

    @product5.setter
    def product5(self, product5):
        """
        Sets the product5 of this Vendor.


        :param product5: The product5 of this Vendor.
        :type: int
        """
        self._product5 = product5

    @property
    def product6(self):
        """
        Gets the product6 of this Vendor.


        :return: The product6 of this Vendor.
        :rtype: int
        """
        return self._product6

    @product6.setter
    def product6(self, product6):
        """
        Sets the product6 of this Vendor.


        :param product6: The product6 of this Vendor.
        :type: int
        """
        self._product6 = product6

    @property
    def product7(self):
        """
        Gets the product7 of this Vendor.


        :return: The product7 of this Vendor.
        :rtype: int
        """
        return self._product7

    @product7.setter
    def product7(self, product7):
        """
        Sets the product7 of this Vendor.


        :param product7: The product7 of this Vendor.
        :type: int
        """
        self._product7 = product7

    @property
    def product8(self):
        """
        Gets the product8 of this Vendor.


        :return: The product8 of this Vendor.
        :rtype: int
        """
        return self._product8

    @product8.setter
    def product8(self, product8):
        """
        Sets the product8 of this Vendor.


        :param product8: The product8 of this Vendor.
        :type: int
        """
        self._product8 = product8

    @property
    def product9(self):
        """
        Gets the product9 of this Vendor.


        :return: The product9 of this Vendor.
        :rtype: int
        """
        return self._product9

    @product9.setter
    def product9(self, product9):
        """
        Sets the product9 of this Vendor.


        :param product9: The product9 of this Vendor.
        :type: int
        """
        self._product9 = product9

    @property
    def pod_days(self):
        """
        Gets the pod_days of this Vendor.


        :return: The pod_days of this Vendor.
        :rtype: int
        """
        return self._pod_days

    @pod_days.setter
    def pod_days(self, pod_days):
        """
        Sets the pod_days of this Vendor.


        :param pod_days: The pod_days of this Vendor.
        :type: int
        """
        self._pod_days = pod_days

    @property
    def charge_out(self):
        """
        Gets the charge_out of this Vendor.


        :return: The charge_out of this Vendor.
        :rtype: str
        """
        return self._charge_out

    @charge_out.setter
    def charge_out(self, charge_out):
        """
        Sets the charge_out of this Vendor.


        :param charge_out: The charge_out of this Vendor.
        :type: str
        """
        self._charge_out = charge_out

    @property
    def ar_email(self):
        """
        Gets the ar_email of this Vendor.


        :return: The ar_email of this Vendor.
        :rtype: str
        """
        return self._ar_email

    @ar_email.setter
    def ar_email(self, ar_email):
        """
        Sets the ar_email of this Vendor.


        :param ar_email: The ar_email of this Vendor.
        :type: str
        """
        self._ar_email = ar_email

    @property
    def order_email(self):
        """
        Gets the order_email of this Vendor.


        :return: The order_email of this Vendor.
        :rtype: str
        """
        return self._order_email

    @order_email.setter
    def order_email(self, order_email):
        """
        Sets the order_email of this Vendor.


        :param order_email: The order_email of this Vendor.
        :type: str
        """
        self._order_email = order_email

    @property
    def order_attach(self):
        """
        Gets the order_attach of this Vendor.


        :return: The order_attach of this Vendor.
        :rtype: str
        """
        return self._order_attach

    @order_attach.setter
    def order_attach(self, order_attach):
        """
        Sets the order_attach of this Vendor.


        :param order_attach: The order_attach of this Vendor.
        :type: str
        """
        self._order_attach = order_attach

    @property
    def send_quantity_type(self):
        """
        Gets the send_quantity_type of this Vendor.


        :return: The send_quantity_type of this Vendor.
        :rtype: str
        """
        return self._send_quantity_type

    @send_quantity_type.setter
    def send_quantity_type(self, send_quantity_type):
        """
        Sets the send_quantity_type of this Vendor.


        :param send_quantity_type: The send_quantity_type of this Vendor.
        :type: str
        """
        self._send_quantity_type = send_quantity_type

    @property
    def minority(self):
        """
        Gets the minority of this Vendor.


        :return: The minority of this Vendor.
        :rtype: str
        """
        return self._minority

    @minority.setter
    def minority(self, minority):
        """
        Sets the minority of this Vendor.


        :param minority: The minority of this Vendor.
        :type: str
        """
        self._minority = minority

    @property
    def send_outside(self):
        """
        Gets the send_outside of this Vendor.


        :return: The send_outside of this Vendor.
        :rtype: str
        """
        return self._send_outside

    @send_outside.setter
    def send_outside(self, send_outside):
        """
        Sets the send_outside of this Vendor.


        :param send_outside: The send_outside of this Vendor.
        :type: str
        """
        self._send_outside = send_outside

    @property
    def pod_order_suffix(self):
        """
        Gets the pod_order_suffix of this Vendor.


        :return: The pod_order_suffix of this Vendor.
        :rtype: int
        """
        return self._pod_order_suffix

    @pod_order_suffix.setter
    def pod_order_suffix(self, pod_order_suffix):
        """
        Sets the pod_order_suffix of this Vendor.


        :param pod_order_suffix: The pod_order_suffix of this Vendor.
        :type: int
        """
        self._pod_order_suffix = pod_order_suffix

    @property
    def pod_email(self):
        """
        Gets the pod_email of this Vendor.


        :return: The pod_email of this Vendor.
        :rtype: str
        """
        return self._pod_email

    @pod_email.setter
    def pod_email(self, pod_email):
        """
        Sets the pod_email of this Vendor.


        :param pod_email: The pod_email of this Vendor.
        :type: str
        """
        self._pod_email = pod_email

    @property
    def create_date(self):
        """
        Gets the create_date of this Vendor.


        :return: The create_date of this Vendor.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this Vendor.


        :param create_date: The create_date of this Vendor.
        :type: datetime
        """
        self._create_date = create_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this Vendor.


        :return: The modify_date of this Vendor.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this Vendor.


        :param modify_date: The modify_date of this Vendor.
        :type: datetime
        """
        self._modify_date = modify_date

    @property
    def inactive(self):
        """
        Gets the inactive of this Vendor.


        :return: The inactive of this Vendor.
        :rtype: str
        """
        return self._inactive

    @inactive.setter
    def inactive(self, inactive):
        """
        Sets the inactive of this Vendor.


        :param inactive: The inactive of this Vendor.
        :type: str
        """
        self._inactive = inactive

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this Vendor.


        :return: The custom_fields of this Vendor.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this Vendor.


        :param custom_fields: The custom_fields of this Vendor.
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

