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
from Infoplus.api.business_transaction_api import BusinessTransactionApi  # noqa: E501
from Infoplus.rest import ApiException


class TestBusinessTransactionApi(unittest.TestCase):
    """BusinessTransactionApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.business_transaction_api.BusinessTransactionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_business_transaction(self):
        """Test case for add_business_transaction

        Create a businessTransaction  # noqa: E501
        """
        pass

    def test_add_business_transaction_audit(self):
        """Test case for add_business_transaction_audit

        Add new audit for a businessTransaction  # noqa: E501
        """
        pass

    def test_add_business_transaction_tag(self):
        """Test case for add_business_transaction_tag

        Add new tags for a businessTransaction.  # noqa: E501
        """
        pass

    def test_delete_business_transaction_tag(self):
        """Test case for delete_business_transaction_tag

        Delete a tag for a businessTransaction.  # noqa: E501
        """
        pass

    def test_get_business_transaction_by_filter(self):
        """Test case for get_business_transaction_by_filter

        Search businessTransactions by filter  # noqa: E501
        """
        pass

    def test_get_business_transaction_by_id(self):
        """Test case for get_business_transaction_by_id

        Get a businessTransaction by id  # noqa: E501
        """
        pass

    def test_get_business_transaction_tags(self):
        """Test case for get_business_transaction_tags

        Get the tags for a businessTransaction.  # noqa: E501
        """
        pass

    def test_get_duplicate_business_transaction_by_id(self):
        """Test case for get_duplicate_business_transaction_by_id

        Get a duplicated a businessTransaction by id  # noqa: E501
        """
        pass

    def test_update_business_transaction(self):
        """Test case for update_business_transaction

        Update a businessTransaction  # noqa: E501
        """
        pass

    def test_update_business_transaction_custom_fields(self):
        """Test case for update_business_transaction_custom_fields

        Update a businessTransaction custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
