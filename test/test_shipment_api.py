# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import Infoplus
from Infoplus.api.shipment_api import ShipmentApi  # noqa: E501
from Infoplus.rest import ApiException


class TestShipmentApi(unittest.TestCase):
    """ShipmentApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.shipment_api.ShipmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_shipment_audit(self):
        """Test case for add_shipment_audit

        Add new audit for a shipment  # noqa: E501
        """
        pass

    def test_add_shipment_file(self):
        """Test case for add_shipment_file

        Attach a file to a shipment  # noqa: E501
        """
        pass

    def test_add_shipment_file_by_url(self):
        """Test case for add_shipment_file_by_url

        Attach a file to a shipment by URL.  # noqa: E501
        """
        pass

    def test_add_shipment_tag(self):
        """Test case for add_shipment_tag

        Add new tags for a shipment.  # noqa: E501
        """
        pass

    def test_delete_shipment_file(self):
        """Test case for delete_shipment_file

        Delete a file for a shipment.  # noqa: E501
        """
        pass

    def test_delete_shipment_tag(self):
        """Test case for delete_shipment_tag

        Delete a tag for a shipment.  # noqa: E501
        """
        pass

    def test_get_duplicate_shipment_by_id(self):
        """Test case for get_duplicate_shipment_by_id

        Get a duplicated a shipment by id  # noqa: E501
        """
        pass

    def test_get_shipment_by_filter(self):
        """Test case for get_shipment_by_filter

        Search shipments by filter  # noqa: E501
        """
        pass

    def test_get_shipment_by_id(self):
        """Test case for get_shipment_by_id

        Get a shipment by id  # noqa: E501
        """
        pass

    def test_get_shipment_files(self):
        """Test case for get_shipment_files

        Get the files for a shipment.  # noqa: E501
        """
        pass

    def test_get_shipment_tags(self):
        """Test case for get_shipment_tags

        Get the tags for a shipment.  # noqa: E501
        """
        pass

    def test_update_shipment_custom_fields(self):
        """Test case for update_shipment_custom_fields

        Update a shipment custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
