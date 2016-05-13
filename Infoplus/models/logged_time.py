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


class LoggedTime(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        LoggedTime - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'create_date': 'datetime',
            'modify_date': 'datetime',
            'start': 'datetime',
            'end': 'datetime',
            'duration': 'int',
            'description': 'str',
            'client': 'int',
            'user_id': 'int',
            'lob_id': 'int',
            'warehouse_id': 'int',
            'logged_time_type_id': 'int',
            'app_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'create_date': 'createDate',
            'modify_date': 'modifyDate',
            'start': 'start',
            'end': 'end',
            'duration': 'duration',
            'description': 'description',
            'client': 'client',
            'user_id': 'userId',
            'lob_id': 'lobId',
            'warehouse_id': 'warehouseId',
            'logged_time_type_id': 'loggedTimeTypeId',
            'app_id': 'appId'
        }

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._start = None
        self._end = None
        self._duration = None
        self._description = None
        self._client = None
        self._user_id = None
        self._lob_id = None
        self._warehouse_id = None
        self._logged_time_type_id = None
        self._app_id = None

    @property
    def id(self):
        """
        Gets the id of this LoggedTime.


        :return: The id of this LoggedTime.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this LoggedTime.


        :param id: The id of this LoggedTime.
        :type: int
        """
        self._id = id

    @property
    def create_date(self):
        """
        Gets the create_date of this LoggedTime.


        :return: The create_date of this LoggedTime.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this LoggedTime.


        :param create_date: The create_date of this LoggedTime.
        :type: datetime
        """
        self._create_date = create_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this LoggedTime.


        :return: The modify_date of this LoggedTime.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this LoggedTime.


        :param modify_date: The modify_date of this LoggedTime.
        :type: datetime
        """
        self._modify_date = modify_date

    @property
    def start(self):
        """
        Gets the start of this LoggedTime.


        :return: The start of this LoggedTime.
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this LoggedTime.


        :param start: The start of this LoggedTime.
        :type: datetime
        """
        self._start = start

    @property
    def end(self):
        """
        Gets the end of this LoggedTime.


        :return: The end of this LoggedTime.
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """
        Sets the end of this LoggedTime.


        :param end: The end of this LoggedTime.
        :type: datetime
        """
        self._end = end

    @property
    def duration(self):
        """
        Gets the duration of this LoggedTime.


        :return: The duration of this LoggedTime.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this LoggedTime.


        :param duration: The duration of this LoggedTime.
        :type: int
        """
        self._duration = duration

    @property
    def description(self):
        """
        Gets the description of this LoggedTime.


        :return: The description of this LoggedTime.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this LoggedTime.


        :param description: The description of this LoggedTime.
        :type: str
        """
        self._description = description

    @property
    def client(self):
        """
        Gets the client of this LoggedTime.


        :return: The client of this LoggedTime.
        :rtype: int
        """
        return self._client

    @client.setter
    def client(self, client):
        """
        Sets the client of this LoggedTime.


        :param client: The client of this LoggedTime.
        :type: int
        """
        self._client = client

    @property
    def user_id(self):
        """
        Gets the user_id of this LoggedTime.


        :return: The user_id of this LoggedTime.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this LoggedTime.


        :param user_id: The user_id of this LoggedTime.
        :type: int
        """
        self._user_id = user_id

    @property
    def lob_id(self):
        """
        Gets the lob_id of this LoggedTime.


        :return: The lob_id of this LoggedTime.
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """
        Sets the lob_id of this LoggedTime.


        :param lob_id: The lob_id of this LoggedTime.
        :type: int
        """
        self._lob_id = lob_id

    @property
    def warehouse_id(self):
        """
        Gets the warehouse_id of this LoggedTime.


        :return: The warehouse_id of this LoggedTime.
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """
        Sets the warehouse_id of this LoggedTime.


        :param warehouse_id: The warehouse_id of this LoggedTime.
        :type: int
        """
        self._warehouse_id = warehouse_id

    @property
    def logged_time_type_id(self):
        """
        Gets the logged_time_type_id of this LoggedTime.


        :return: The logged_time_type_id of this LoggedTime.
        :rtype: int
        """
        return self._logged_time_type_id

    @logged_time_type_id.setter
    def logged_time_type_id(self, logged_time_type_id):
        """
        Sets the logged_time_type_id of this LoggedTime.


        :param logged_time_type_id: The logged_time_type_id of this LoggedTime.
        :type: int
        """
        self._logged_time_type_id = logged_time_type_id

    @property
    def app_id(self):
        """
        Gets the app_id of this LoggedTime.


        :return: The app_id of this LoggedTime.
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """
        Sets the app_id of this LoggedTime.


        :param app_id: The app_id of this LoggedTime.
        :type: int
        """
        self._app_id = app_id

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

