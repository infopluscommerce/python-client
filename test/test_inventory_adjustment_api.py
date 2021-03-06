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
from Infoplus.api.inventory_adjustment_api import InventoryAdjustmentApi  # noqa: E501
from Infoplus.rest import ApiException


class TestInventoryAdjustmentApi(unittest.TestCase):
    """InventoryAdjustmentApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.inventory_adjustment_api.InventoryAdjustmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_inventory_adjustment_audit(self):
        """Test case for add_inventory_adjustment_audit

        Add new audit for an inventoryAdjustment  # noqa: E501
        """
        pass

    def test_add_inventory_adjustment_file(self):
        """Test case for add_inventory_adjustment_file

        Attach a file to an inventoryAdjustment  # noqa: E501
        """
        pass

    def test_add_inventory_adjustment_file_by_url(self):
        """Test case for add_inventory_adjustment_file_by_url

        Attach a file to an inventoryAdjustment by URL.  # noqa: E501
        """
        pass

    def test_add_inventory_adjustment_tag(self):
        """Test case for add_inventory_adjustment_tag

        Add new tags for an inventoryAdjustment.  # noqa: E501
        """
        pass

    def test_delete_inventory_adjustment_file(self):
        """Test case for delete_inventory_adjustment_file

        Delete a file for an inventoryAdjustment.  # noqa: E501
        """
        pass

    def test_delete_inventory_adjustment_tag(self):
        """Test case for delete_inventory_adjustment_tag

        Delete a tag for an inventoryAdjustment.  # noqa: E501
        """
        pass

    def test_get_duplicate_inventory_adjustment_by_id(self):
        """Test case for get_duplicate_inventory_adjustment_by_id

        Get a duplicated an inventoryAdjustment by id  # noqa: E501
        """
        pass

    def test_get_inventory_adjustment_by_filter(self):
        """Test case for get_inventory_adjustment_by_filter

        Search inventoryAdjustments by filter  # noqa: E501
        """
        pass

    def test_get_inventory_adjustment_by_id(self):
        """Test case for get_inventory_adjustment_by_id

        Get an inventoryAdjustment by id  # noqa: E501
        """
        pass

    def test_get_inventory_adjustment_files(self):
        """Test case for get_inventory_adjustment_files

        Get the files for an inventoryAdjustment.  # noqa: E501
        """
        pass

    def test_get_inventory_adjustment_tags(self):
        """Test case for get_inventory_adjustment_tags

        Get the tags for an inventoryAdjustment.  # noqa: E501
        """
        pass

    def test_update_inventory_adjustment_custom_fields(self):
        """Test case for update_inventory_adjustment_custom_fields

        Update an inventoryAdjustment custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
