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
from Infoplus.api.inventory_snapshot_api import InventorySnapshotApi  # noqa: E501
from Infoplus.rest import ApiException


class TestInventorySnapshotApi(unittest.TestCase):
    """InventorySnapshotApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.inventory_snapshot_api.InventorySnapshotApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_inventory_snapshot_audit(self):
        """Test case for add_inventory_snapshot_audit

        Add new audit for an inventorySnapshot  # noqa: E501
        """
        pass

    def test_add_inventory_snapshot_file(self):
        """Test case for add_inventory_snapshot_file

        Attach a file to an inventorySnapshot  # noqa: E501
        """
        pass

    def test_add_inventory_snapshot_file_by_url(self):
        """Test case for add_inventory_snapshot_file_by_url

        Attach a file to an inventorySnapshot by URL.  # noqa: E501
        """
        pass

    def test_add_inventory_snapshot_tag(self):
        """Test case for add_inventory_snapshot_tag

        Add new tags for an inventorySnapshot.  # noqa: E501
        """
        pass

    def test_delete_inventory_snapshot_file(self):
        """Test case for delete_inventory_snapshot_file

        Delete a file for an inventorySnapshot.  # noqa: E501
        """
        pass

    def test_delete_inventory_snapshot_tag(self):
        """Test case for delete_inventory_snapshot_tag

        Delete a tag for an inventorySnapshot.  # noqa: E501
        """
        pass

    def test_get_duplicate_inventory_snapshot_by_id(self):
        """Test case for get_duplicate_inventory_snapshot_by_id

        Get a duplicated an inventorySnapshot by id  # noqa: E501
        """
        pass

    def test_get_inventory_snapshot_by_filter(self):
        """Test case for get_inventory_snapshot_by_filter

        Search inventorySnapshots by filter  # noqa: E501
        """
        pass

    def test_get_inventory_snapshot_by_id(self):
        """Test case for get_inventory_snapshot_by_id

        Get an inventorySnapshot by id  # noqa: E501
        """
        pass

    def test_get_inventory_snapshot_files(self):
        """Test case for get_inventory_snapshot_files

        Get the files for an inventorySnapshot.  # noqa: E501
        """
        pass

    def test_get_inventory_snapshot_tags(self):
        """Test case for get_inventory_snapshot_tags

        Get the tags for an inventorySnapshot.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
