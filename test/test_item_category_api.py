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
from Infoplus.api.item_category_api import ItemCategoryApi  # noqa: E501
from Infoplus.rest import ApiException


class TestItemCategoryApi(unittest.TestCase):
    """ItemCategoryApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.item_category_api.ItemCategoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_item_category(self):
        """Test case for add_item_category

        Create an itemCategory  # noqa: E501
        """
        pass

    def test_add_item_category_audit(self):
        """Test case for add_item_category_audit

        Add new audit for an itemCategory  # noqa: E501
        """
        pass

    def test_add_item_category_file(self):
        """Test case for add_item_category_file

        Attach a file to an itemCategory  # noqa: E501
        """
        pass

    def test_add_item_category_file_by_url(self):
        """Test case for add_item_category_file_by_url

        Attach a file to an itemCategory by URL.  # noqa: E501
        """
        pass

    def test_add_item_category_tag(self):
        """Test case for add_item_category_tag

        Add new tags for an itemCategory.  # noqa: E501
        """
        pass

    def test_delete_item_category(self):
        """Test case for delete_item_category

        Delete an itemCategory  # noqa: E501
        """
        pass

    def test_delete_item_category_file(self):
        """Test case for delete_item_category_file

        Delete a file for an itemCategory.  # noqa: E501
        """
        pass

    def test_delete_item_category_tag(self):
        """Test case for delete_item_category_tag

        Delete a tag for an itemCategory.  # noqa: E501
        """
        pass

    def test_get_duplicate_item_category_by_id(self):
        """Test case for get_duplicate_item_category_by_id

        Get a duplicated an itemCategory by id  # noqa: E501
        """
        pass

    def test_get_item_category_by_filter(self):
        """Test case for get_item_category_by_filter

        Search itemCategorys by filter  # noqa: E501
        """
        pass

    def test_get_item_category_by_id(self):
        """Test case for get_item_category_by_id

        Get an itemCategory by id  # noqa: E501
        """
        pass

    def test_get_item_category_files(self):
        """Test case for get_item_category_files

        Get the files for an itemCategory.  # noqa: E501
        """
        pass

    def test_get_item_category_tags(self):
        """Test case for get_item_category_tags

        Get the tags for an itemCategory.  # noqa: E501
        """
        pass

    def test_update_item_category(self):
        """Test case for update_item_category

        Update an itemCategory  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
