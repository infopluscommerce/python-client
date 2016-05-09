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


class Work(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Work - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'source_warehouse_id': 'int',
            'source_building_id': 'int',
            'source_location': 'str',
            'destination_warehouse_id': 'int',
            'destination_building_id': 'int',
            'destination_location': 'str',
            'type': 'str',
            'create_date': 'datetime',
            'modify_date': 'datetime',
            'priority_code': 'int',
            'status': 'str',
            'user_id': 'int',
            'work_batch_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'source_warehouse_id': 'sourceWarehouseId',
            'source_building_id': 'sourceBuildingId',
            'source_location': 'sourceLocation',
            'destination_warehouse_id': 'destinationWarehouseId',
            'destination_building_id': 'destinationBuildingId',
            'destination_location': 'destinationLocation',
            'type': 'type',
            'create_date': 'createDate',
            'modify_date': 'modifyDate',
            'priority_code': 'priorityCode',
            'status': 'status',
            'user_id': 'userId',
            'work_batch_id': 'workBatchId'
        }

        self._id = None
        self._source_warehouse_id = None
        self._source_building_id = None
        self._source_location = None
        self._destination_warehouse_id = None
        self._destination_building_id = None
        self._destination_location = None
        self._type = None
        self._create_date = None
        self._modify_date = None
        self._priority_code = None
        self._status = None
        self._user_id = None
        self._work_batch_id = None

    @property
    def id(self):
        """
        Gets the id of this Work.


        :return: The id of this Work.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Work.


        :param id: The id of this Work.
        :type: int
        """
        self._id = id

    @property
    def source_warehouse_id(self):
        """
        Gets the source_warehouse_id of this Work.


        :return: The source_warehouse_id of this Work.
        :rtype: int
        """
        return self._source_warehouse_id

    @source_warehouse_id.setter
    def source_warehouse_id(self, source_warehouse_id):
        """
        Sets the source_warehouse_id of this Work.


        :param source_warehouse_id: The source_warehouse_id of this Work.
        :type: int
        """
        self._source_warehouse_id = source_warehouse_id

    @property
    def source_building_id(self):
        """
        Gets the source_building_id of this Work.


        :return: The source_building_id of this Work.
        :rtype: int
        """
        return self._source_building_id

    @source_building_id.setter
    def source_building_id(self, source_building_id):
        """
        Sets the source_building_id of this Work.


        :param source_building_id: The source_building_id of this Work.
        :type: int
        """
        self._source_building_id = source_building_id

    @property
    def source_location(self):
        """
        Gets the source_location of this Work.


        :return: The source_location of this Work.
        :rtype: str
        """
        return self._source_location

    @source_location.setter
    def source_location(self, source_location):
        """
        Sets the source_location of this Work.


        :param source_location: The source_location of this Work.
        :type: str
        """
        self._source_location = source_location

    @property
    def destination_warehouse_id(self):
        """
        Gets the destination_warehouse_id of this Work.


        :return: The destination_warehouse_id of this Work.
        :rtype: int
        """
        return self._destination_warehouse_id

    @destination_warehouse_id.setter
    def destination_warehouse_id(self, destination_warehouse_id):
        """
        Sets the destination_warehouse_id of this Work.


        :param destination_warehouse_id: The destination_warehouse_id of this Work.
        :type: int
        """
        self._destination_warehouse_id = destination_warehouse_id

    @property
    def destination_building_id(self):
        """
        Gets the destination_building_id of this Work.


        :return: The destination_building_id of this Work.
        :rtype: int
        """
        return self._destination_building_id

    @destination_building_id.setter
    def destination_building_id(self, destination_building_id):
        """
        Sets the destination_building_id of this Work.


        :param destination_building_id: The destination_building_id of this Work.
        :type: int
        """
        self._destination_building_id = destination_building_id

    @property
    def destination_location(self):
        """
        Gets the destination_location of this Work.


        :return: The destination_location of this Work.
        :rtype: str
        """
        return self._destination_location

    @destination_location.setter
    def destination_location(self, destination_location):
        """
        Sets the destination_location of this Work.


        :param destination_location: The destination_location of this Work.
        :type: str
        """
        self._destination_location = destination_location

    @property
    def type(self):
        """
        Gets the type of this Work.


        :return: The type of this Work.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Work.


        :param type: The type of this Work.
        :type: str
        """
        self._type = type

    @property
    def create_date(self):
        """
        Gets the create_date of this Work.


        :return: The create_date of this Work.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this Work.


        :param create_date: The create_date of this Work.
        :type: datetime
        """
        self._create_date = create_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this Work.


        :return: The modify_date of this Work.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this Work.


        :param modify_date: The modify_date of this Work.
        :type: datetime
        """
        self._modify_date = modify_date

    @property
    def priority_code(self):
        """
        Gets the priority_code of this Work.


        :return: The priority_code of this Work.
        :rtype: int
        """
        return self._priority_code

    @priority_code.setter
    def priority_code(self, priority_code):
        """
        Sets the priority_code of this Work.


        :param priority_code: The priority_code of this Work.
        :type: int
        """
        self._priority_code = priority_code

    @property
    def status(self):
        """
        Gets the status of this Work.


        :return: The status of this Work.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Work.


        :param status: The status of this Work.
        :type: str
        """
        self._status = status

    @property
    def user_id(self):
        """
        Gets the user_id of this Work.


        :return: The user_id of this Work.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this Work.


        :param user_id: The user_id of this Work.
        :type: int
        """
        self._user_id = user_id

    @property
    def work_batch_id(self):
        """
        Gets the work_batch_id of this Work.


        :return: The work_batch_id of this Work.
        :rtype: int
        """
        return self._work_batch_id

    @work_batch_id.setter
    def work_batch_id(self, work_batch_id):
        """
        Sets the work_batch_id of this Work.


        :param work_batch_id: The work_batch_id of this Work.
        :type: int
        """
        self._work_batch_id = work_batch_id

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

