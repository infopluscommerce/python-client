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
from Infoplus.api.item_serial_scheme_api import ItemSerialSchemeApi  # noqa: E501
from Infoplus.rest import ApiException


class TestItemSerialSchemeApi(unittest.TestCase):
    """ItemSerialSchemeApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.item_serial_scheme_api.ItemSerialSchemeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_item_serial_scheme(self):
        """Test case for add_item_serial_scheme

        Create an itemSerialScheme  # noqa: E501
        """
        pass

    def test_add_item_serial_scheme_audit(self):
        """Test case for add_item_serial_scheme_audit

        Add new audit for an itemSerialScheme  # noqa: E501
        """
        pass

    def test_add_item_serial_scheme_file(self):
        """Test case for add_item_serial_scheme_file

        Attach a file to an itemSerialScheme  # noqa: E501
        """
        pass

    def test_add_item_serial_scheme_tag(self):
        """Test case for add_item_serial_scheme_tag

        Add new tags for an itemSerialScheme.  # noqa: E501
        """
        pass

    def test_delete_item_serial_scheme(self):
        """Test case for delete_item_serial_scheme

        Delete an itemSerialScheme  # noqa: E501
        """
        pass

    def test_delete_item_serial_scheme_tag(self):
        """Test case for delete_item_serial_scheme_tag

        Delete a tag for an itemSerialScheme.  # noqa: E501
        """
        pass

    def test_get_duplicate_item_serial_scheme_by_id(self):
        """Test case for get_duplicate_item_serial_scheme_by_id

        Get a duplicated an itemSerialScheme by id  # noqa: E501
        """
        pass

    def test_get_item_serial_scheme_by_filter(self):
        """Test case for get_item_serial_scheme_by_filter

        Search itemSerialSchemes by filter  # noqa: E501
        """
        pass

    def test_get_item_serial_scheme_by_id(self):
        """Test case for get_item_serial_scheme_by_id

        Get an itemSerialScheme by id  # noqa: E501
        """
        pass

    def test_get_item_serial_scheme_tags(self):
        """Test case for get_item_serial_scheme_tags

        Get the tags for an itemSerialScheme.  # noqa: E501
        """
        pass

    def test_update_item_serial_scheme(self):
        """Test case for update_item_serial_scheme

        Update an itemSerialScheme  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()