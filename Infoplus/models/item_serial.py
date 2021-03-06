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


class ItemSerial(object):
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
        'id': 'int',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'item_receipt_id': 'int',
        'lob_id': 'int',
        'asn_id': 'int',
        'order_no_id': 'float',
        'serial': 'str',
        'received_date': 'datetime',
        'shipped_date': 'datetime',
        'in_inventory': 'bool',
        's0': 'str',
        's1': 'str',
        's2': 'str',
        's3': 'str',
        's4': 'str',
        's5': 'str',
        's6': 'str',
        's7': 'str',
        's8': 'str',
        's9': 'str',
        's10': 'str',
        's11': 'str',
        's12': 'str',
        's13': 'str',
        's14': 'str',
        's15': 'str',
        's16': 'str',
        's17': 'str',
        's18': 'str',
        's19': 'str',
        'custom_fields': 'dict(str, object)',
        'sku': 'str'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'item_receipt_id': 'itemReceiptId',
        'lob_id': 'lobId',
        'asn_id': 'asnId',
        'order_no_id': 'orderNoId',
        'serial': 'serial',
        'received_date': 'receivedDate',
        'shipped_date': 'shippedDate',
        'in_inventory': 'inInventory',
        's0': 's0',
        's1': 's1',
        's2': 's2',
        's3': 's3',
        's4': 's4',
        's5': 's5',
        's6': 's6',
        's7': 's7',
        's8': 's8',
        's9': 's9',
        's10': 's10',
        's11': 's11',
        's12': 's12',
        's13': 's13',
        's14': 's14',
        's15': 's15',
        's16': 's16',
        's17': 's17',
        's18': 's18',
        's19': 's19',
        'custom_fields': 'customFields',
        'sku': 'sku'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, item_receipt_id=None, lob_id=None, asn_id=None, order_no_id=None, serial=None, received_date=None, shipped_date=None, in_inventory=False, s0=None, s1=None, s2=None, s3=None, s4=None, s5=None, s6=None, s7=None, s8=None, s9=None, s10=None, s11=None, s12=None, s13=None, s14=None, s15=None, s16=None, s17=None, s18=None, s19=None, custom_fields=None, sku=None):  # noqa: E501
        """ItemSerial - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._item_receipt_id = None
        self._lob_id = None
        self._asn_id = None
        self._order_no_id = None
        self._serial = None
        self._received_date = None
        self._shipped_date = None
        self._in_inventory = None
        self._s0 = None
        self._s1 = None
        self._s2 = None
        self._s3 = None
        self._s4 = None
        self._s5 = None
        self._s6 = None
        self._s7 = None
        self._s8 = None
        self._s9 = None
        self._s10 = None
        self._s11 = None
        self._s12 = None
        self._s13 = None
        self._s14 = None
        self._s15 = None
        self._s16 = None
        self._s17 = None
        self._s18 = None
        self._s19 = None
        self._custom_fields = None
        self._sku = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if item_receipt_id is not None:
            self.item_receipt_id = item_receipt_id
        self.lob_id = lob_id
        if asn_id is not None:
            self.asn_id = asn_id
        if order_no_id is not None:
            self.order_no_id = order_no_id
        self.serial = serial
        if received_date is not None:
            self.received_date = received_date
        if shipped_date is not None:
            self.shipped_date = shipped_date
        if in_inventory is not None:
            self.in_inventory = in_inventory
        if s0 is not None:
            self.s0 = s0
        if s1 is not None:
            self.s1 = s1
        if s2 is not None:
            self.s2 = s2
        if s3 is not None:
            self.s3 = s3
        if s4 is not None:
            self.s4 = s4
        if s5 is not None:
            self.s5 = s5
        if s6 is not None:
            self.s6 = s6
        if s7 is not None:
            self.s7 = s7
        if s8 is not None:
            self.s8 = s8
        if s9 is not None:
            self.s9 = s9
        if s10 is not None:
            self.s10 = s10
        if s11 is not None:
            self.s11 = s11
        if s12 is not None:
            self.s12 = s12
        if s13 is not None:
            self.s13 = s13
        if s14 is not None:
            self.s14 = s14
        if s15 is not None:
            self.s15 = s15
        if s16 is not None:
            self.s16 = s16
        if s17 is not None:
            self.s17 = s17
        if s18 is not None:
            self.s18 = s18
        if s19 is not None:
            self.s19 = s19
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if sku is not None:
            self.sku = sku

    @property
    def id(self):
        """Gets the id of this ItemSerial.  # noqa: E501


        :return: The id of this ItemSerial.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ItemSerial.


        :param id: The id of this ItemSerial.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this ItemSerial.  # noqa: E501


        :return: The create_date of this ItemSerial.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ItemSerial.


        :param create_date: The create_date of this ItemSerial.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this ItemSerial.  # noqa: E501


        :return: The modify_date of this ItemSerial.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this ItemSerial.


        :param modify_date: The modify_date of this ItemSerial.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def item_receipt_id(self):
        """Gets the item_receipt_id of this ItemSerial.  # noqa: E501


        :return: The item_receipt_id of this ItemSerial.  # noqa: E501
        :rtype: int
        """
        return self._item_receipt_id

    @item_receipt_id.setter
    def item_receipt_id(self, item_receipt_id):
        """Sets the item_receipt_id of this ItemSerial.


        :param item_receipt_id: The item_receipt_id of this ItemSerial.  # noqa: E501
        :type: int
        """

        self._item_receipt_id = item_receipt_id

    @property
    def lob_id(self):
        """Gets the lob_id of this ItemSerial.  # noqa: E501


        :return: The lob_id of this ItemSerial.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this ItemSerial.


        :param lob_id: The lob_id of this ItemSerial.  # noqa: E501
        :type: int
        """
        if lob_id is None:
            raise ValueError("Invalid value for `lob_id`, must not be `None`")  # noqa: E501

        self._lob_id = lob_id

    @property
    def asn_id(self):
        """Gets the asn_id of this ItemSerial.  # noqa: E501


        :return: The asn_id of this ItemSerial.  # noqa: E501
        :rtype: int
        """
        return self._asn_id

    @asn_id.setter
    def asn_id(self, asn_id):
        """Sets the asn_id of this ItemSerial.


        :param asn_id: The asn_id of this ItemSerial.  # noqa: E501
        :type: int
        """

        self._asn_id = asn_id

    @property
    def order_no_id(self):
        """Gets the order_no_id of this ItemSerial.  # noqa: E501


        :return: The order_no_id of this ItemSerial.  # noqa: E501
        :rtype: float
        """
        return self._order_no_id

    @order_no_id.setter
    def order_no_id(self, order_no_id):
        """Sets the order_no_id of this ItemSerial.


        :param order_no_id: The order_no_id of this ItemSerial.  # noqa: E501
        :type: float
        """

        self._order_no_id = order_no_id

    @property
    def serial(self):
        """Gets the serial of this ItemSerial.  # noqa: E501


        :return: The serial of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this ItemSerial.


        :param serial: The serial of this ItemSerial.  # noqa: E501
        :type: str
        """
        if serial is None:
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501

        self._serial = serial

    @property
    def received_date(self):
        """Gets the received_date of this ItemSerial.  # noqa: E501


        :return: The received_date of this ItemSerial.  # noqa: E501
        :rtype: datetime
        """
        return self._received_date

    @received_date.setter
    def received_date(self, received_date):
        """Sets the received_date of this ItemSerial.


        :param received_date: The received_date of this ItemSerial.  # noqa: E501
        :type: datetime
        """

        self._received_date = received_date

    @property
    def shipped_date(self):
        """Gets the shipped_date of this ItemSerial.  # noqa: E501


        :return: The shipped_date of this ItemSerial.  # noqa: E501
        :rtype: datetime
        """
        return self._shipped_date

    @shipped_date.setter
    def shipped_date(self, shipped_date):
        """Sets the shipped_date of this ItemSerial.


        :param shipped_date: The shipped_date of this ItemSerial.  # noqa: E501
        :type: datetime
        """

        self._shipped_date = shipped_date

    @property
    def in_inventory(self):
        """Gets the in_inventory of this ItemSerial.  # noqa: E501


        :return: The in_inventory of this ItemSerial.  # noqa: E501
        :rtype: bool
        """
        return self._in_inventory

    @in_inventory.setter
    def in_inventory(self, in_inventory):
        """Sets the in_inventory of this ItemSerial.


        :param in_inventory: The in_inventory of this ItemSerial.  # noqa: E501
        :type: bool
        """

        self._in_inventory = in_inventory

    @property
    def s0(self):
        """Gets the s0 of this ItemSerial.  # noqa: E501


        :return: The s0 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s0

    @s0.setter
    def s0(self, s0):
        """Sets the s0 of this ItemSerial.


        :param s0: The s0 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s0 = s0

    @property
    def s1(self):
        """Gets the s1 of this ItemSerial.  # noqa: E501


        :return: The s1 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s1

    @s1.setter
    def s1(self, s1):
        """Sets the s1 of this ItemSerial.


        :param s1: The s1 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s1 = s1

    @property
    def s2(self):
        """Gets the s2 of this ItemSerial.  # noqa: E501


        :return: The s2 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s2

    @s2.setter
    def s2(self, s2):
        """Sets the s2 of this ItemSerial.


        :param s2: The s2 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s2 = s2

    @property
    def s3(self):
        """Gets the s3 of this ItemSerial.  # noqa: E501


        :return: The s3 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this ItemSerial.


        :param s3: The s3 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s3 = s3

    @property
    def s4(self):
        """Gets the s4 of this ItemSerial.  # noqa: E501


        :return: The s4 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s4

    @s4.setter
    def s4(self, s4):
        """Sets the s4 of this ItemSerial.


        :param s4: The s4 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s4 = s4

    @property
    def s5(self):
        """Gets the s5 of this ItemSerial.  # noqa: E501


        :return: The s5 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s5

    @s5.setter
    def s5(self, s5):
        """Sets the s5 of this ItemSerial.


        :param s5: The s5 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s5 = s5

    @property
    def s6(self):
        """Gets the s6 of this ItemSerial.  # noqa: E501


        :return: The s6 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s6

    @s6.setter
    def s6(self, s6):
        """Sets the s6 of this ItemSerial.


        :param s6: The s6 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s6 = s6

    @property
    def s7(self):
        """Gets the s7 of this ItemSerial.  # noqa: E501


        :return: The s7 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s7

    @s7.setter
    def s7(self, s7):
        """Sets the s7 of this ItemSerial.


        :param s7: The s7 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s7 = s7

    @property
    def s8(self):
        """Gets the s8 of this ItemSerial.  # noqa: E501


        :return: The s8 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s8

    @s8.setter
    def s8(self, s8):
        """Sets the s8 of this ItemSerial.


        :param s8: The s8 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s8 = s8

    @property
    def s9(self):
        """Gets the s9 of this ItemSerial.  # noqa: E501


        :return: The s9 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s9

    @s9.setter
    def s9(self, s9):
        """Sets the s9 of this ItemSerial.


        :param s9: The s9 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s9 = s9

    @property
    def s10(self):
        """Gets the s10 of this ItemSerial.  # noqa: E501


        :return: The s10 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s10

    @s10.setter
    def s10(self, s10):
        """Sets the s10 of this ItemSerial.


        :param s10: The s10 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s10 = s10

    @property
    def s11(self):
        """Gets the s11 of this ItemSerial.  # noqa: E501


        :return: The s11 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s11

    @s11.setter
    def s11(self, s11):
        """Sets the s11 of this ItemSerial.


        :param s11: The s11 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s11 = s11

    @property
    def s12(self):
        """Gets the s12 of this ItemSerial.  # noqa: E501


        :return: The s12 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s12

    @s12.setter
    def s12(self, s12):
        """Sets the s12 of this ItemSerial.


        :param s12: The s12 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s12 = s12

    @property
    def s13(self):
        """Gets the s13 of this ItemSerial.  # noqa: E501


        :return: The s13 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s13

    @s13.setter
    def s13(self, s13):
        """Sets the s13 of this ItemSerial.


        :param s13: The s13 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s13 = s13

    @property
    def s14(self):
        """Gets the s14 of this ItemSerial.  # noqa: E501


        :return: The s14 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s14

    @s14.setter
    def s14(self, s14):
        """Sets the s14 of this ItemSerial.


        :param s14: The s14 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s14 = s14

    @property
    def s15(self):
        """Gets the s15 of this ItemSerial.  # noqa: E501


        :return: The s15 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s15

    @s15.setter
    def s15(self, s15):
        """Sets the s15 of this ItemSerial.


        :param s15: The s15 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s15 = s15

    @property
    def s16(self):
        """Gets the s16 of this ItemSerial.  # noqa: E501


        :return: The s16 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s16

    @s16.setter
    def s16(self, s16):
        """Sets the s16 of this ItemSerial.


        :param s16: The s16 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s16 = s16

    @property
    def s17(self):
        """Gets the s17 of this ItemSerial.  # noqa: E501


        :return: The s17 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s17

    @s17.setter
    def s17(self, s17):
        """Sets the s17 of this ItemSerial.


        :param s17: The s17 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s17 = s17

    @property
    def s18(self):
        """Gets the s18 of this ItemSerial.  # noqa: E501


        :return: The s18 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s18

    @s18.setter
    def s18(self, s18):
        """Sets the s18 of this ItemSerial.


        :param s18: The s18 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s18 = s18

    @property
    def s19(self):
        """Gets the s19 of this ItemSerial.  # noqa: E501


        :return: The s19 of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._s19

    @s19.setter
    def s19(self, s19):
        """Sets the s19 of this ItemSerial.


        :param s19: The s19 of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._s19 = s19

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ItemSerial.  # noqa: E501


        :return: The custom_fields of this ItemSerial.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ItemSerial.


        :param custom_fields: The custom_fields of this ItemSerial.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def sku(self):
        """Gets the sku of this ItemSerial.  # noqa: E501


        :return: The sku of this ItemSerial.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this ItemSerial.


        :param sku: The sku of this ItemSerial.  # noqa: E501
        :type: str
        """

        self._sku = sku

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
        if not isinstance(other, ItemSerial):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
