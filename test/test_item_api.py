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
from Infoplus.api.item_api import ItemApi  # noqa: E501
from Infoplus.rest import ApiException


class TestItemApi(unittest.TestCase):
    """ItemApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.item_api.ItemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_item(self):
        """Test case for add_item

        Create an item  # noqa: E501
        """
        pass

    def test_add_item_audit(self):
        """Test case for add_item_audit

        Add new audit for an item  # noqa: E501
        """
        pass

    def test_add_item_file(self):
        """Test case for add_item_file

        Attach a file to an item  # noqa: E501
        """
        pass

    def test_add_item_file_by_url(self):
        """Test case for add_item_file_by_url

        Attach a file to an item by URL.  # noqa: E501
        """
        pass

    def test_add_item_tag(self):
        """Test case for add_item_tag

        Add new tags for an item.  # noqa: E501
        """
        pass

    def test_delete_item(self):
        """Test case for delete_item

        Delete an item  # noqa: E501
        """
        pass

    def test_delete_item_file(self):
        """Test case for delete_item_file

        Delete a file for an item.  # noqa: E501
        """
        pass

    def test_delete_item_tag(self):
        """Test case for delete_item_tag

        Delete a tag for an item.  # noqa: E501
        """
        pass

    def test_get_by_sku(self):
        """Test case for get_by_sku

        Get an item by SKU  # noqa: E501
        """
        pass

    def test_get_duplicate_item_by_id(self):
        """Test case for get_duplicate_item_by_id

        Get a duplicated an item by id  # noqa: E501
        """
        pass

    def test_get_item_by_filter(self):
        """Test case for get_item_by_filter

        Search items by filter  # noqa: E501
        """
        pass

    def test_get_item_by_id(self):
        """Test case for get_item_by_id

        Get an item by id  # noqa: E501
        """
        pass

    def test_get_item_files(self):
        """Test case for get_item_files

        Get the files for an item.  # noqa: E501
        """
        pass

    def test_get_item_tags(self):
        """Test case for get_item_tags

        Get the tags for an item.  # noqa: E501
        """
        pass

    def test_update_item(self):
        """Test case for update_item

        Update an item  # noqa: E501
        """
        pass

    def test_update_item_custom_fields(self):
        """Test case for update_item_custom_fields

        Update an item custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
