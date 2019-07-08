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
from Infoplus.api.carrier_api import CarrierApi  # noqa: E501
from Infoplus.rest import ApiException


class TestCarrierApi(unittest.TestCase):
    """CarrierApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.carrier_api.CarrierApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_carrier_by_id(self):
        """Test case for get_carrier_by_id

        Get a carrier by id  # noqa: E501
        """
        pass

    def test_get_carrier_by_search_text(self):
        """Test case for get_carrier_by_search_text

        Search carriers  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()