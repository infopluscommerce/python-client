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
from Infoplus.api.external_shipping_system_api import ExternalShippingSystemApi  # noqa: E501
from Infoplus.rest import ApiException


class TestExternalShippingSystemApi(unittest.TestCase):
    """ExternalShippingSystemApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.external_shipping_system_api.ExternalShippingSystemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_external_shipping_system(self):
        """Test case for add_external_shipping_system

        Create an externalShippingSystem  # noqa: E501
        """
        pass

    def test_add_external_shipping_system_audit(self):
        """Test case for add_external_shipping_system_audit

        Add new audit for an externalShippingSystem  # noqa: E501
        """
        pass

    def test_add_external_shipping_system_file(self):
        """Test case for add_external_shipping_system_file

        Attach a file to an externalShippingSystem  # noqa: E501
        """
        pass

    def test_add_external_shipping_system_file_by_url(self):
        """Test case for add_external_shipping_system_file_by_url

        Attach a file to an externalShippingSystem by URL.  # noqa: E501
        """
        pass

    def test_add_external_shipping_system_tag(self):
        """Test case for add_external_shipping_system_tag

        Add new tags for an externalShippingSystem.  # noqa: E501
        """
        pass

    def test_delete_external_shipping_system(self):
        """Test case for delete_external_shipping_system

        Delete an externalShippingSystem  # noqa: E501
        """
        pass

    def test_delete_external_shipping_system_file(self):
        """Test case for delete_external_shipping_system_file

        Delete a file for an externalShippingSystem.  # noqa: E501
        """
        pass

    def test_delete_external_shipping_system_tag(self):
        """Test case for delete_external_shipping_system_tag

        Delete a tag for an externalShippingSystem.  # noqa: E501
        """
        pass

    def test_get_duplicate_external_shipping_system_by_id(self):
        """Test case for get_duplicate_external_shipping_system_by_id

        Get a duplicated an externalShippingSystem by id  # noqa: E501
        """
        pass

    def test_get_external_shipping_system_by_filter(self):
        """Test case for get_external_shipping_system_by_filter

        Search externalShippingSystems by filter  # noqa: E501
        """
        pass

    def test_get_external_shipping_system_by_id(self):
        """Test case for get_external_shipping_system_by_id

        Get an externalShippingSystem by id  # noqa: E501
        """
        pass

    def test_get_external_shipping_system_files(self):
        """Test case for get_external_shipping_system_files

        Get the files for an externalShippingSystem.  # noqa: E501
        """
        pass

    def test_get_external_shipping_system_tags(self):
        """Test case for get_external_shipping_system_tags

        Get the tags for an externalShippingSystem.  # noqa: E501
        """
        pass

    def test_update_external_shipping_system(self):
        """Test case for update_external_shipping_system

        Update an externalShippingSystem  # noqa: E501
        """
        pass

    def test_update_external_shipping_system_custom_fields(self):
        """Test case for update_external_shipping_system_custom_fields

        Update an externalShippingSystem custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
