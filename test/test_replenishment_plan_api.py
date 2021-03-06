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
from Infoplus.api.replenishment_plan_api import ReplenishmentPlanApi  # noqa: E501
from Infoplus.rest import ApiException


class TestReplenishmentPlanApi(unittest.TestCase):
    """ReplenishmentPlanApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.replenishment_plan_api.ReplenishmentPlanApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_replenishment_plan(self):
        """Test case for add_replenishment_plan

        Create a replenishmentPlan  # noqa: E501
        """
        pass

    def test_add_replenishment_plan_audit(self):
        """Test case for add_replenishment_plan_audit

        Add new audit for a replenishmentPlan  # noqa: E501
        """
        pass

    def test_add_replenishment_plan_file(self):
        """Test case for add_replenishment_plan_file

        Attach a file to a replenishmentPlan  # noqa: E501
        """
        pass

    def test_add_replenishment_plan_file_by_url(self):
        """Test case for add_replenishment_plan_file_by_url

        Attach a file to a replenishmentPlan by URL.  # noqa: E501
        """
        pass

    def test_add_replenishment_plan_tag(self):
        """Test case for add_replenishment_plan_tag

        Add new tags for a replenishmentPlan.  # noqa: E501
        """
        pass

    def test_delete_replenishment_plan(self):
        """Test case for delete_replenishment_plan

        Delete a replenishmentPlan  # noqa: E501
        """
        pass

    def test_delete_replenishment_plan_file(self):
        """Test case for delete_replenishment_plan_file

        Delete a file for a replenishmentPlan.  # noqa: E501
        """
        pass

    def test_delete_replenishment_plan_tag(self):
        """Test case for delete_replenishment_plan_tag

        Delete a tag for a replenishmentPlan.  # noqa: E501
        """
        pass

    def test_get_duplicate_replenishment_plan_by_id(self):
        """Test case for get_duplicate_replenishment_plan_by_id

        Get a duplicated a replenishmentPlan by id  # noqa: E501
        """
        pass

    def test_get_replenishment_plan_by_filter(self):
        """Test case for get_replenishment_plan_by_filter

        Search replenishmentPlans by filter  # noqa: E501
        """
        pass

    def test_get_replenishment_plan_by_id(self):
        """Test case for get_replenishment_plan_by_id

        Get a replenishmentPlan by id  # noqa: E501
        """
        pass

    def test_get_replenishment_plan_files(self):
        """Test case for get_replenishment_plan_files

        Get the files for a replenishmentPlan.  # noqa: E501
        """
        pass

    def test_get_replenishment_plan_tags(self):
        """Test case for get_replenishment_plan_tags

        Get the tags for a replenishmentPlan.  # noqa: E501
        """
        pass

    def test_update_replenishment_plan(self):
        """Test case for update_replenishment_plan

        Update a replenishmentPlan  # noqa: E501
        """
        pass

    def test_update_replenishment_plan_custom_fields(self):
        """Test case for update_replenishment_plan_custom_fields

        Update a replenishmentPlan custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
