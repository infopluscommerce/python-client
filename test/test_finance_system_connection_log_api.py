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
from Infoplus.api.finance_system_connection_log_api import FinanceSystemConnectionLogApi  # noqa: E501
from Infoplus.rest import ApiException


class TestFinanceSystemConnectionLogApi(unittest.TestCase):
    """FinanceSystemConnectionLogApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.finance_system_connection_log_api.FinanceSystemConnectionLogApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_finance_system_connection_log_audit(self):
        """Test case for add_finance_system_connection_log_audit

        Add new audit for a financeSystemConnectionLog  # noqa: E501
        """
        pass

    def test_add_finance_system_connection_log_file(self):
        """Test case for add_finance_system_connection_log_file

        Attach a file to a financeSystemConnectionLog  # noqa: E501
        """
        pass

    def test_add_finance_system_connection_log_file_by_url(self):
        """Test case for add_finance_system_connection_log_file_by_url

        Attach a file to a financeSystemConnectionLog by URL.  # noqa: E501
        """
        pass

    def test_add_finance_system_connection_log_tag(self):
        """Test case for add_finance_system_connection_log_tag

        Add new tags for a financeSystemConnectionLog.  # noqa: E501
        """
        pass

    def test_delete_finance_system_connection_log_file(self):
        """Test case for delete_finance_system_connection_log_file

        Delete a file for a financeSystemConnectionLog.  # noqa: E501
        """
        pass

    def test_delete_finance_system_connection_log_tag(self):
        """Test case for delete_finance_system_connection_log_tag

        Delete a tag for a financeSystemConnectionLog.  # noqa: E501
        """
        pass

    def test_get_duplicate_finance_system_connection_log_by_id(self):
        """Test case for get_duplicate_finance_system_connection_log_by_id

        Get a duplicated a financeSystemConnectionLog by id  # noqa: E501
        """
        pass

    def test_get_finance_system_connection_log_by_filter(self):
        """Test case for get_finance_system_connection_log_by_filter

        Search financeSystemConnectionLogs by filter  # noqa: E501
        """
        pass

    def test_get_finance_system_connection_log_by_id(self):
        """Test case for get_finance_system_connection_log_by_id

        Get a financeSystemConnectionLog by id  # noqa: E501
        """
        pass

    def test_get_finance_system_connection_log_files(self):
        """Test case for get_finance_system_connection_log_files

        Get the files for a financeSystemConnectionLog.  # noqa: E501
        """
        pass

    def test_get_finance_system_connection_log_tags(self):
        """Test case for get_finance_system_connection_log_tags

        Get the tags for a financeSystemConnectionLog.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()