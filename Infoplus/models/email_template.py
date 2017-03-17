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


class EmailTemplate(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        EmailTemplate - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'lob_id': 'int',
            'subject_text': 'str',
            'name': 'str',
            'from_name': 'str',
            'from_address': 'str',
            'email_template_type': 'str',
            'create_date': 'datetime',
            'modify_date': 'datetime',
            'custom_fields': 'dict(str, object)'
        }

        self.attribute_map = {
            'id': 'id',
            'lob_id': 'lobId',
            'subject_text': 'subjectText',
            'name': 'name',
            'from_name': 'fromName',
            'from_address': 'fromAddress',
            'email_template_type': 'emailTemplateType',
            'create_date': 'createDate',
            'modify_date': 'modifyDate',
            'custom_fields': 'customFields'
        }

        self._id = None
        self._lob_id = None
        self._subject_text = None
        self._name = None
        self._from_name = None
        self._from_address = None
        self._email_template_type = None
        self._create_date = None
        self._modify_date = None
        self._custom_fields = None

    @property
    def id(self):
        """
        Gets the id of this EmailTemplate.


        :return: The id of this EmailTemplate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EmailTemplate.


        :param id: The id of this EmailTemplate.
        :type: int
        """
        self._id = id

    @property
    def lob_id(self):
        """
        Gets the lob_id of this EmailTemplate.


        :return: The lob_id of this EmailTemplate.
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """
        Sets the lob_id of this EmailTemplate.


        :param lob_id: The lob_id of this EmailTemplate.
        :type: int
        """
        self._lob_id = lob_id

    @property
    def subject_text(self):
        """
        Gets the subject_text of this EmailTemplate.


        :return: The subject_text of this EmailTemplate.
        :rtype: str
        """
        return self._subject_text

    @subject_text.setter
    def subject_text(self, subject_text):
        """
        Sets the subject_text of this EmailTemplate.


        :param subject_text: The subject_text of this EmailTemplate.
        :type: str
        """
        self._subject_text = subject_text

    @property
    def name(self):
        """
        Gets the name of this EmailTemplate.


        :return: The name of this EmailTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this EmailTemplate.


        :param name: The name of this EmailTemplate.
        :type: str
        """
        self._name = name

    @property
    def from_name(self):
        """
        Gets the from_name of this EmailTemplate.


        :return: The from_name of this EmailTemplate.
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """
        Sets the from_name of this EmailTemplate.


        :param from_name: The from_name of this EmailTemplate.
        :type: str
        """
        self._from_name = from_name

    @property
    def from_address(self):
        """
        Gets the from_address of this EmailTemplate.


        :return: The from_address of this EmailTemplate.
        :rtype: str
        """
        return self._from_address

    @from_address.setter
    def from_address(self, from_address):
        """
        Sets the from_address of this EmailTemplate.


        :param from_address: The from_address of this EmailTemplate.
        :type: str
        """
        self._from_address = from_address

    @property
    def email_template_type(self):
        """
        Gets the email_template_type of this EmailTemplate.


        :return: The email_template_type of this EmailTemplate.
        :rtype: str
        """
        return self._email_template_type

    @email_template_type.setter
    def email_template_type(self, email_template_type):
        """
        Sets the email_template_type of this EmailTemplate.


        :param email_template_type: The email_template_type of this EmailTemplate.
        :type: str
        """
        self._email_template_type = email_template_type

    @property
    def create_date(self):
        """
        Gets the create_date of this EmailTemplate.


        :return: The create_date of this EmailTemplate.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this EmailTemplate.


        :param create_date: The create_date of this EmailTemplate.
        :type: datetime
        """
        self._create_date = create_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this EmailTemplate.


        :return: The modify_date of this EmailTemplate.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this EmailTemplate.


        :param modify_date: The modify_date of this EmailTemplate.
        :type: datetime
        """
        self._modify_date = modify_date

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this EmailTemplate.


        :return: The custom_fields of this EmailTemplate.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this EmailTemplate.


        :param custom_fields: The custom_fields of this EmailTemplate.
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

