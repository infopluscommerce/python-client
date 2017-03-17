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


class FulfillmentPlan(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FulfillmentPlan - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'create_date': 'datetime',
            'modify_date': 'datetime',
            'name': 'str',
            'description': 'str',
            'warehouse_id': 'int',
            'last_run_time': 'datetime',
            'order_smart_filter_id': 'int',
            'location_smart_filter_id': 'int',
            'maximum_number_of_orders': 'int',
            'create_pick_work': 'bool',
            'picking_rule': 'str',
            'layout_rule': 'str',
            'pick_sort_rule': 'str',
            'create_pick_list': 'bool',
            'pick_list_format': 'str',
            'pick_list_layout': 'str',
            'pick_list_group': 'str',
            'pick_list_sort': 'str',
            'create_pick_summary': 'bool',
            'pick_summary_format': 'str',
            'pick_summary_layout': 'str',
            'pick_summary_sort': 'str',
            'pick_scan_scheme_id': 'int',
            'cartonize_orders': 'bool',
            'auto_ship_casebreak_cartons': 'bool',
            'pre_generate_parcel_labels': 'bool',
            'create_packing_slip': 'str',
            'override_packing_slip_template_id': 'int',
            'create_order_assembly_guide': 'bool',
            'create_order_invoice': 'str',
            'override_order_invoice_template_id': 'int',
            'send_to_external_shipping_system': 'bool',
            'external_shipping_system_id': 'int',
            'custom_fields': 'dict(str, object)'
        }

        self.attribute_map = {
            'id': 'id',
            'create_date': 'createDate',
            'modify_date': 'modifyDate',
            'name': 'name',
            'description': 'description',
            'warehouse_id': 'warehouseId',
            'last_run_time': 'lastRunTime',
            'order_smart_filter_id': 'orderSmartFilterId',
            'location_smart_filter_id': 'locationSmartFilterId',
            'maximum_number_of_orders': 'maximumNumberOfOrders',
            'create_pick_work': 'createPickWork',
            'picking_rule': 'pickingRule',
            'layout_rule': 'layoutRule',
            'pick_sort_rule': 'pickSortRule',
            'create_pick_list': 'createPickList',
            'pick_list_format': 'pickListFormat',
            'pick_list_layout': 'pickListLayout',
            'pick_list_group': 'pickListGroup',
            'pick_list_sort': 'pickListSort',
            'create_pick_summary': 'createPickSummary',
            'pick_summary_format': 'pickSummaryFormat',
            'pick_summary_layout': 'pickSummaryLayout',
            'pick_summary_sort': 'pickSummarySort',
            'pick_scan_scheme_id': 'pickScanSchemeId',
            'cartonize_orders': 'cartonizeOrders',
            'auto_ship_casebreak_cartons': 'autoShipCasebreakCartons',
            'pre_generate_parcel_labels': 'preGenerateParcelLabels',
            'create_packing_slip': 'createPackingSlip',
            'override_packing_slip_template_id': 'overridePackingSlipTemplateId',
            'create_order_assembly_guide': 'createOrderAssemblyGuide',
            'create_order_invoice': 'createOrderInvoice',
            'override_order_invoice_template_id': 'overrideOrderInvoiceTemplateId',
            'send_to_external_shipping_system': 'sendToExternalShippingSystem',
            'external_shipping_system_id': 'externalShippingSystemId',
            'custom_fields': 'customFields'
        }

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._name = None
        self._description = None
        self._warehouse_id = None
        self._last_run_time = None
        self._order_smart_filter_id = None
        self._location_smart_filter_id = None
        self._maximum_number_of_orders = None
        self._create_pick_work = False
        self._picking_rule = None
        self._layout_rule = None
        self._pick_sort_rule = None
        self._create_pick_list = False
        self._pick_list_format = None
        self._pick_list_layout = None
        self._pick_list_group = None
        self._pick_list_sort = None
        self._create_pick_summary = False
        self._pick_summary_format = None
        self._pick_summary_layout = None
        self._pick_summary_sort = None
        self._pick_scan_scheme_id = None
        self._cartonize_orders = False
        self._auto_ship_casebreak_cartons = False
        self._pre_generate_parcel_labels = False
        self._create_packing_slip = None
        self._override_packing_slip_template_id = None
        self._create_order_assembly_guide = False
        self._create_order_invoice = None
        self._override_order_invoice_template_id = None
        self._send_to_external_shipping_system = False
        self._external_shipping_system_id = None
        self._custom_fields = None

    @property
    def id(self):
        """
        Gets the id of this FulfillmentPlan.


        :return: The id of this FulfillmentPlan.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this FulfillmentPlan.


        :param id: The id of this FulfillmentPlan.
        :type: int
        """
        self._id = id

    @property
    def create_date(self):
        """
        Gets the create_date of this FulfillmentPlan.


        :return: The create_date of this FulfillmentPlan.
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """
        Sets the create_date of this FulfillmentPlan.


        :param create_date: The create_date of this FulfillmentPlan.
        :type: datetime
        """
        self._create_date = create_date

    @property
    def modify_date(self):
        """
        Gets the modify_date of this FulfillmentPlan.


        :return: The modify_date of this FulfillmentPlan.
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """
        Sets the modify_date of this FulfillmentPlan.


        :param modify_date: The modify_date of this FulfillmentPlan.
        :type: datetime
        """
        self._modify_date = modify_date

    @property
    def name(self):
        """
        Gets the name of this FulfillmentPlan.


        :return: The name of this FulfillmentPlan.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this FulfillmentPlan.


        :param name: The name of this FulfillmentPlan.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this FulfillmentPlan.


        :return: The description of this FulfillmentPlan.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this FulfillmentPlan.


        :param description: The description of this FulfillmentPlan.
        :type: str
        """
        self._description = description

    @property
    def warehouse_id(self):
        """
        Gets the warehouse_id of this FulfillmentPlan.


        :return: The warehouse_id of this FulfillmentPlan.
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """
        Sets the warehouse_id of this FulfillmentPlan.


        :param warehouse_id: The warehouse_id of this FulfillmentPlan.
        :type: int
        """
        self._warehouse_id = warehouse_id

    @property
    def last_run_time(self):
        """
        Gets the last_run_time of this FulfillmentPlan.


        :return: The last_run_time of this FulfillmentPlan.
        :rtype: datetime
        """
        return self._last_run_time

    @last_run_time.setter
    def last_run_time(self, last_run_time):
        """
        Sets the last_run_time of this FulfillmentPlan.


        :param last_run_time: The last_run_time of this FulfillmentPlan.
        :type: datetime
        """
        self._last_run_time = last_run_time

    @property
    def order_smart_filter_id(self):
        """
        Gets the order_smart_filter_id of this FulfillmentPlan.


        :return: The order_smart_filter_id of this FulfillmentPlan.
        :rtype: int
        """
        return self._order_smart_filter_id

    @order_smart_filter_id.setter
    def order_smart_filter_id(self, order_smart_filter_id):
        """
        Sets the order_smart_filter_id of this FulfillmentPlan.


        :param order_smart_filter_id: The order_smart_filter_id of this FulfillmentPlan.
        :type: int
        """
        self._order_smart_filter_id = order_smart_filter_id

    @property
    def location_smart_filter_id(self):
        """
        Gets the location_smart_filter_id of this FulfillmentPlan.


        :return: The location_smart_filter_id of this FulfillmentPlan.
        :rtype: int
        """
        return self._location_smart_filter_id

    @location_smart_filter_id.setter
    def location_smart_filter_id(self, location_smart_filter_id):
        """
        Sets the location_smart_filter_id of this FulfillmentPlan.


        :param location_smart_filter_id: The location_smart_filter_id of this FulfillmentPlan.
        :type: int
        """
        self._location_smart_filter_id = location_smart_filter_id

    @property
    def maximum_number_of_orders(self):
        """
        Gets the maximum_number_of_orders of this FulfillmentPlan.


        :return: The maximum_number_of_orders of this FulfillmentPlan.
        :rtype: int
        """
        return self._maximum_number_of_orders

    @maximum_number_of_orders.setter
    def maximum_number_of_orders(self, maximum_number_of_orders):
        """
        Sets the maximum_number_of_orders of this FulfillmentPlan.


        :param maximum_number_of_orders: The maximum_number_of_orders of this FulfillmentPlan.
        :type: int
        """
        self._maximum_number_of_orders = maximum_number_of_orders

    @property
    def create_pick_work(self):
        """
        Gets the create_pick_work of this FulfillmentPlan.


        :return: The create_pick_work of this FulfillmentPlan.
        :rtype: bool
        """
        return self._create_pick_work

    @create_pick_work.setter
    def create_pick_work(self, create_pick_work):
        """
        Sets the create_pick_work of this FulfillmentPlan.


        :param create_pick_work: The create_pick_work of this FulfillmentPlan.
        :type: bool
        """
        self._create_pick_work = create_pick_work

    @property
    def picking_rule(self):
        """
        Gets the picking_rule of this FulfillmentPlan.


        :return: The picking_rule of this FulfillmentPlan.
        :rtype: str
        """
        return self._picking_rule

    @picking_rule.setter
    def picking_rule(self, picking_rule):
        """
        Sets the picking_rule of this FulfillmentPlan.


        :param picking_rule: The picking_rule of this FulfillmentPlan.
        :type: str
        """
        self._picking_rule = picking_rule

    @property
    def layout_rule(self):
        """
        Gets the layout_rule of this FulfillmentPlan.


        :return: The layout_rule of this FulfillmentPlan.
        :rtype: str
        """
        return self._layout_rule

    @layout_rule.setter
    def layout_rule(self, layout_rule):
        """
        Sets the layout_rule of this FulfillmentPlan.


        :param layout_rule: The layout_rule of this FulfillmentPlan.
        :type: str
        """
        self._layout_rule = layout_rule

    @property
    def pick_sort_rule(self):
        """
        Gets the pick_sort_rule of this FulfillmentPlan.


        :return: The pick_sort_rule of this FulfillmentPlan.
        :rtype: str
        """
        return self._pick_sort_rule

    @pick_sort_rule.setter
    def pick_sort_rule(self, pick_sort_rule):
        """
        Sets the pick_sort_rule of this FulfillmentPlan.


        :param pick_sort_rule: The pick_sort_rule of this FulfillmentPlan.
        :type: str
        """
        self._pick_sort_rule = pick_sort_rule

    @property
    def create_pick_list(self):
        """
        Gets the create_pick_list of this FulfillmentPlan.


        :return: The create_pick_list of this FulfillmentPlan.
        :rtype: bool
        """
        return self._create_pick_list

    @create_pick_list.setter
    def create_pick_list(self, create_pick_list):
        """
        Sets the create_pick_list of this FulfillmentPlan.


        :param create_pick_list: The create_pick_list of this FulfillmentPlan.
        :type: bool
        """
        self._create_pick_list = create_pick_list

    @property
    def pick_list_format(self):
        """
        Gets the pick_list_format of this FulfillmentPlan.


        :return: The pick_list_format of this FulfillmentPlan.
        :rtype: str
        """
        return self._pick_list_format

    @pick_list_format.setter
    def pick_list_format(self, pick_list_format):
        """
        Sets the pick_list_format of this FulfillmentPlan.


        :param pick_list_format: The pick_list_format of this FulfillmentPlan.
        :type: str
        """
        self._pick_list_format = pick_list_format

    @property
    def pick_list_layout(self):
        """
        Gets the pick_list_layout of this FulfillmentPlan.


        :return: The pick_list_layout of this FulfillmentPlan.
        :rtype: str
        """
        return self._pick_list_layout

    @pick_list_layout.setter
    def pick_list_layout(self, pick_list_layout):
        """
        Sets the pick_list_layout of this FulfillmentPlan.


        :param pick_list_layout: The pick_list_layout of this FulfillmentPlan.
        :type: str
        """
        self._pick_list_layout = pick_list_layout

    @property
    def pick_list_group(self):
        """
        Gets the pick_list_group of this FulfillmentPlan.


        :return: The pick_list_group of this FulfillmentPlan.
        :rtype: str
        """
        return self._pick_list_group

    @pick_list_group.setter
    def pick_list_group(self, pick_list_group):
        """
        Sets the pick_list_group of this FulfillmentPlan.


        :param pick_list_group: The pick_list_group of this FulfillmentPlan.
        :type: str
        """
        self._pick_list_group = pick_list_group

    @property
    def pick_list_sort(self):
        """
        Gets the pick_list_sort of this FulfillmentPlan.


        :return: The pick_list_sort of this FulfillmentPlan.
        :rtype: str
        """
        return self._pick_list_sort

    @pick_list_sort.setter
    def pick_list_sort(self, pick_list_sort):
        """
        Sets the pick_list_sort of this FulfillmentPlan.


        :param pick_list_sort: The pick_list_sort of this FulfillmentPlan.
        :type: str
        """
        self._pick_list_sort = pick_list_sort

    @property
    def create_pick_summary(self):
        """
        Gets the create_pick_summary of this FulfillmentPlan.


        :return: The create_pick_summary of this FulfillmentPlan.
        :rtype: bool
        """
        return self._create_pick_summary

    @create_pick_summary.setter
    def create_pick_summary(self, create_pick_summary):
        """
        Sets the create_pick_summary of this FulfillmentPlan.


        :param create_pick_summary: The create_pick_summary of this FulfillmentPlan.
        :type: bool
        """
        self._create_pick_summary = create_pick_summary

    @property
    def pick_summary_format(self):
        """
        Gets the pick_summary_format of this FulfillmentPlan.


        :return: The pick_summary_format of this FulfillmentPlan.
        :rtype: str
        """
        return self._pick_summary_format

    @pick_summary_format.setter
    def pick_summary_format(self, pick_summary_format):
        """
        Sets the pick_summary_format of this FulfillmentPlan.


        :param pick_summary_format: The pick_summary_format of this FulfillmentPlan.
        :type: str
        """
        self._pick_summary_format = pick_summary_format

    @property
    def pick_summary_layout(self):
        """
        Gets the pick_summary_layout of this FulfillmentPlan.


        :return: The pick_summary_layout of this FulfillmentPlan.
        :rtype: str
        """
        return self._pick_summary_layout

    @pick_summary_layout.setter
    def pick_summary_layout(self, pick_summary_layout):
        """
        Sets the pick_summary_layout of this FulfillmentPlan.


        :param pick_summary_layout: The pick_summary_layout of this FulfillmentPlan.
        :type: str
        """
        self._pick_summary_layout = pick_summary_layout

    @property
    def pick_summary_sort(self):
        """
        Gets the pick_summary_sort of this FulfillmentPlan.


        :return: The pick_summary_sort of this FulfillmentPlan.
        :rtype: str
        """
        return self._pick_summary_sort

    @pick_summary_sort.setter
    def pick_summary_sort(self, pick_summary_sort):
        """
        Sets the pick_summary_sort of this FulfillmentPlan.


        :param pick_summary_sort: The pick_summary_sort of this FulfillmentPlan.
        :type: str
        """
        self._pick_summary_sort = pick_summary_sort

    @property
    def pick_scan_scheme_id(self):
        """
        Gets the pick_scan_scheme_id of this FulfillmentPlan.


        :return: The pick_scan_scheme_id of this FulfillmentPlan.
        :rtype: int
        """
        return self._pick_scan_scheme_id

    @pick_scan_scheme_id.setter
    def pick_scan_scheme_id(self, pick_scan_scheme_id):
        """
        Sets the pick_scan_scheme_id of this FulfillmentPlan.


        :param pick_scan_scheme_id: The pick_scan_scheme_id of this FulfillmentPlan.
        :type: int
        """
        self._pick_scan_scheme_id = pick_scan_scheme_id

    @property
    def cartonize_orders(self):
        """
        Gets the cartonize_orders of this FulfillmentPlan.


        :return: The cartonize_orders of this FulfillmentPlan.
        :rtype: bool
        """
        return self._cartonize_orders

    @cartonize_orders.setter
    def cartonize_orders(self, cartonize_orders):
        """
        Sets the cartonize_orders of this FulfillmentPlan.


        :param cartonize_orders: The cartonize_orders of this FulfillmentPlan.
        :type: bool
        """
        self._cartonize_orders = cartonize_orders

    @property
    def auto_ship_casebreak_cartons(self):
        """
        Gets the auto_ship_casebreak_cartons of this FulfillmentPlan.


        :return: The auto_ship_casebreak_cartons of this FulfillmentPlan.
        :rtype: bool
        """
        return self._auto_ship_casebreak_cartons

    @auto_ship_casebreak_cartons.setter
    def auto_ship_casebreak_cartons(self, auto_ship_casebreak_cartons):
        """
        Sets the auto_ship_casebreak_cartons of this FulfillmentPlan.


        :param auto_ship_casebreak_cartons: The auto_ship_casebreak_cartons of this FulfillmentPlan.
        :type: bool
        """
        self._auto_ship_casebreak_cartons = auto_ship_casebreak_cartons

    @property
    def pre_generate_parcel_labels(self):
        """
        Gets the pre_generate_parcel_labels of this FulfillmentPlan.


        :return: The pre_generate_parcel_labels of this FulfillmentPlan.
        :rtype: bool
        """
        return self._pre_generate_parcel_labels

    @pre_generate_parcel_labels.setter
    def pre_generate_parcel_labels(self, pre_generate_parcel_labels):
        """
        Sets the pre_generate_parcel_labels of this FulfillmentPlan.


        :param pre_generate_parcel_labels: The pre_generate_parcel_labels of this FulfillmentPlan.
        :type: bool
        """
        self._pre_generate_parcel_labels = pre_generate_parcel_labels

    @property
    def create_packing_slip(self):
        """
        Gets the create_packing_slip of this FulfillmentPlan.


        :return: The create_packing_slip of this FulfillmentPlan.
        :rtype: str
        """
        return self._create_packing_slip

    @create_packing_slip.setter
    def create_packing_slip(self, create_packing_slip):
        """
        Sets the create_packing_slip of this FulfillmentPlan.


        :param create_packing_slip: The create_packing_slip of this FulfillmentPlan.
        :type: str
        """
        self._create_packing_slip = create_packing_slip

    @property
    def override_packing_slip_template_id(self):
        """
        Gets the override_packing_slip_template_id of this FulfillmentPlan.


        :return: The override_packing_slip_template_id of this FulfillmentPlan.
        :rtype: int
        """
        return self._override_packing_slip_template_id

    @override_packing_slip_template_id.setter
    def override_packing_slip_template_id(self, override_packing_slip_template_id):
        """
        Sets the override_packing_slip_template_id of this FulfillmentPlan.


        :param override_packing_slip_template_id: The override_packing_slip_template_id of this FulfillmentPlan.
        :type: int
        """
        self._override_packing_slip_template_id = override_packing_slip_template_id

    @property
    def create_order_assembly_guide(self):
        """
        Gets the create_order_assembly_guide of this FulfillmentPlan.


        :return: The create_order_assembly_guide of this FulfillmentPlan.
        :rtype: bool
        """
        return self._create_order_assembly_guide

    @create_order_assembly_guide.setter
    def create_order_assembly_guide(self, create_order_assembly_guide):
        """
        Sets the create_order_assembly_guide of this FulfillmentPlan.


        :param create_order_assembly_guide: The create_order_assembly_guide of this FulfillmentPlan.
        :type: bool
        """
        self._create_order_assembly_guide = create_order_assembly_guide

    @property
    def create_order_invoice(self):
        """
        Gets the create_order_invoice of this FulfillmentPlan.


        :return: The create_order_invoice of this FulfillmentPlan.
        :rtype: str
        """
        return self._create_order_invoice

    @create_order_invoice.setter
    def create_order_invoice(self, create_order_invoice):
        """
        Sets the create_order_invoice of this FulfillmentPlan.


        :param create_order_invoice: The create_order_invoice of this FulfillmentPlan.
        :type: str
        """
        self._create_order_invoice = create_order_invoice

    @property
    def override_order_invoice_template_id(self):
        """
        Gets the override_order_invoice_template_id of this FulfillmentPlan.


        :return: The override_order_invoice_template_id of this FulfillmentPlan.
        :rtype: int
        """
        return self._override_order_invoice_template_id

    @override_order_invoice_template_id.setter
    def override_order_invoice_template_id(self, override_order_invoice_template_id):
        """
        Sets the override_order_invoice_template_id of this FulfillmentPlan.


        :param override_order_invoice_template_id: The override_order_invoice_template_id of this FulfillmentPlan.
        :type: int
        """
        self._override_order_invoice_template_id = override_order_invoice_template_id

    @property
    def send_to_external_shipping_system(self):
        """
        Gets the send_to_external_shipping_system of this FulfillmentPlan.


        :return: The send_to_external_shipping_system of this FulfillmentPlan.
        :rtype: bool
        """
        return self._send_to_external_shipping_system

    @send_to_external_shipping_system.setter
    def send_to_external_shipping_system(self, send_to_external_shipping_system):
        """
        Sets the send_to_external_shipping_system of this FulfillmentPlan.


        :param send_to_external_shipping_system: The send_to_external_shipping_system of this FulfillmentPlan.
        :type: bool
        """
        self._send_to_external_shipping_system = send_to_external_shipping_system

    @property
    def external_shipping_system_id(self):
        """
        Gets the external_shipping_system_id of this FulfillmentPlan.


        :return: The external_shipping_system_id of this FulfillmentPlan.
        :rtype: int
        """
        return self._external_shipping_system_id

    @external_shipping_system_id.setter
    def external_shipping_system_id(self, external_shipping_system_id):
        """
        Sets the external_shipping_system_id of this FulfillmentPlan.


        :param external_shipping_system_id: The external_shipping_system_id of this FulfillmentPlan.
        :type: int
        """
        self._external_shipping_system_id = external_shipping_system_id

    @property
    def custom_fields(self):
        """
        Gets the custom_fields of this FulfillmentPlan.


        :return: The custom_fields of this FulfillmentPlan.
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """
        Sets the custom_fields of this FulfillmentPlan.


        :param custom_fields: The custom_fields of this FulfillmentPlan.
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

