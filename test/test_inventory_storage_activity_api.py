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
from Infoplus.api.inventory_storage_activity_api import InventoryStorageActivityApi  # noqa: E501
from Infoplus.rest import ApiException


class TestInventoryStorageActivityApi(unittest.TestCase):
    """InventoryStorageActivityApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.inventory_storage_activity_api.InventoryStorageActivityApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_inventory_storage_activity(self):
        """Test case for add_inventory_storage_activity

        Create an inventoryStorageActivity  # noqa: E501
        """
        pass

    def test_add_inventory_storage_activity_audit(self):
        """Test case for add_inventory_storage_activity_audit

        Add new audit for an inventoryStorageActivity  # noqa: E501
        """
        pass

    def test_add_inventory_storage_activity_file(self):
        """Test case for add_inventory_storage_activity_file

        Attach a file to an inventoryStorageActivity  # noqa: E501
        """
        pass

    def test_add_inventory_storage_activity_file_by_url(self):
        """Test case for add_inventory_storage_activity_file_by_url

        Attach a file to an inventoryStorageActivity by URL.  # noqa: E501
        """
        pass

    def test_add_inventory_storage_activity_tag(self):
        """Test case for add_inventory_storage_activity_tag

        Add new tags for an inventoryStorageActivity.  # noqa: E501
        """
        pass

    def test_delete_inventory_storage_activity(self):
        """Test case for delete_inventory_storage_activity

        Delete an inventoryStorageActivity  # noqa: E501
        """
        pass

    def test_delete_inventory_storage_activity_file(self):
        """Test case for delete_inventory_storage_activity_file

        Delete a file for an inventoryStorageActivity.  # noqa: E501
        """
        pass

    def test_delete_inventory_storage_activity_tag(self):
        """Test case for delete_inventory_storage_activity_tag

        Delete a tag for an inventoryStorageActivity.  # noqa: E501
        """
        pass

    def test_get_duplicate_inventory_storage_activity_by_id(self):
        """Test case for get_duplicate_inventory_storage_activity_by_id

        Get a duplicated an inventoryStorageActivity by id  # noqa: E501
        """
        pass

    def test_get_inventory_storage_activity_by_filter(self):
        """Test case for get_inventory_storage_activity_by_filter

        Search inventoryStorageActivitys by filter  # noqa: E501
        """
        pass

    def test_get_inventory_storage_activity_by_id(self):
        """Test case for get_inventory_storage_activity_by_id

        Get an inventoryStorageActivity by id  # noqa: E501
        """
        pass

    def test_get_inventory_storage_activity_files(self):
        """Test case for get_inventory_storage_activity_files

        Get the files for an inventoryStorageActivity.  # noqa: E501
        """
        pass

    def test_get_inventory_storage_activity_tags(self):
        """Test case for get_inventory_storage_activity_tags

        Get the tags for an inventoryStorageActivity.  # noqa: E501
        """
        pass

    def test_update_inventory_storage_activity(self):
        """Test case for update_inventory_storage_activity

        Update an inventoryStorageActivity  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
