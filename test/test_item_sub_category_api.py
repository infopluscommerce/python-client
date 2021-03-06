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
from Infoplus.api.item_sub_category_api import ItemSubCategoryApi  # noqa: E501
from Infoplus.rest import ApiException


class TestItemSubCategoryApi(unittest.TestCase):
    """ItemSubCategoryApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.item_sub_category_api.ItemSubCategoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_item_sub_category(self):
        """Test case for add_item_sub_category

        Create an itemSubCategory  # noqa: E501
        """
        pass

    def test_add_item_sub_category_audit(self):
        """Test case for add_item_sub_category_audit

        Add new audit for an itemSubCategory  # noqa: E501
        """
        pass

    def test_add_item_sub_category_file(self):
        """Test case for add_item_sub_category_file

        Attach a file to an itemSubCategory  # noqa: E501
        """
        pass

    def test_add_item_sub_category_file_by_url(self):
        """Test case for add_item_sub_category_file_by_url

        Attach a file to an itemSubCategory by URL.  # noqa: E501
        """
        pass

    def test_add_item_sub_category_tag(self):
        """Test case for add_item_sub_category_tag

        Add new tags for an itemSubCategory.  # noqa: E501
        """
        pass

    def test_delete_item_sub_category(self):
        """Test case for delete_item_sub_category

        Delete an itemSubCategory  # noqa: E501
        """
        pass

    def test_delete_item_sub_category_file(self):
        """Test case for delete_item_sub_category_file

        Delete a file for an itemSubCategory.  # noqa: E501
        """
        pass

    def test_delete_item_sub_category_tag(self):
        """Test case for delete_item_sub_category_tag

        Delete a tag for an itemSubCategory.  # noqa: E501
        """
        pass

    def test_get_duplicate_item_sub_category_by_id(self):
        """Test case for get_duplicate_item_sub_category_by_id

        Get a duplicated an itemSubCategory by id  # noqa: E501
        """
        pass

    def test_get_item_sub_category_by_filter(self):
        """Test case for get_item_sub_category_by_filter

        Search itemSubCategorys by filter  # noqa: E501
        """
        pass

    def test_get_item_sub_category_by_id(self):
        """Test case for get_item_sub_category_by_id

        Get an itemSubCategory by id  # noqa: E501
        """
        pass

    def test_get_item_sub_category_files(self):
        """Test case for get_item_sub_category_files

        Get the files for an itemSubCategory.  # noqa: E501
        """
        pass

    def test_get_item_sub_category_tags(self):
        """Test case for get_item_sub_category_tags

        Get the tags for an itemSubCategory.  # noqa: E501
        """
        pass

    def test_update_item_sub_category(self):
        """Test case for update_item_sub_category

        Update an itemSubCategory  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
