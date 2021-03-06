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
from Infoplus.api.pick_face_assignment_api import PickFaceAssignmentApi  # noqa: E501
from Infoplus.rest import ApiException


class TestPickFaceAssignmentApi(unittest.TestCase):
    """PickFaceAssignmentApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.pick_face_assignment_api.PickFaceAssignmentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_pick_face_assignment(self):
        """Test case for add_pick_face_assignment

        Create a pickFaceAssignment  # noqa: E501
        """
        pass

    def test_add_pick_face_assignment_audit(self):
        """Test case for add_pick_face_assignment_audit

        Add new audit for a pickFaceAssignment  # noqa: E501
        """
        pass

    def test_add_pick_face_assignment_file(self):
        """Test case for add_pick_face_assignment_file

        Attach a file to a pickFaceAssignment  # noqa: E501
        """
        pass

    def test_add_pick_face_assignment_file_by_url(self):
        """Test case for add_pick_face_assignment_file_by_url

        Attach a file to a pickFaceAssignment by URL.  # noqa: E501
        """
        pass

    def test_add_pick_face_assignment_tag(self):
        """Test case for add_pick_face_assignment_tag

        Add new tags for a pickFaceAssignment.  # noqa: E501
        """
        pass

    def test_delete_pick_face_assignment(self):
        """Test case for delete_pick_face_assignment

        Delete a pickFaceAssignment  # noqa: E501
        """
        pass

    def test_delete_pick_face_assignment_file(self):
        """Test case for delete_pick_face_assignment_file

        Delete a file for a pickFaceAssignment.  # noqa: E501
        """
        pass

    def test_delete_pick_face_assignment_tag(self):
        """Test case for delete_pick_face_assignment_tag

        Delete a tag for a pickFaceAssignment.  # noqa: E501
        """
        pass

    def test_get_duplicate_pick_face_assignment_by_id(self):
        """Test case for get_duplicate_pick_face_assignment_by_id

        Get a duplicated a pickFaceAssignment by id  # noqa: E501
        """
        pass

    def test_get_pick_face_assignment_by_filter(self):
        """Test case for get_pick_face_assignment_by_filter

        Search pickFaceAssignments by filter  # noqa: E501
        """
        pass

    def test_get_pick_face_assignment_by_id(self):
        """Test case for get_pick_face_assignment_by_id

        Get a pickFaceAssignment by id  # noqa: E501
        """
        pass

    def test_get_pick_face_assignment_files(self):
        """Test case for get_pick_face_assignment_files

        Get the files for a pickFaceAssignment.  # noqa: E501
        """
        pass

    def test_get_pick_face_assignment_tags(self):
        """Test case for get_pick_face_assignment_tags

        Get the tags for a pickFaceAssignment.  # noqa: E501
        """
        pass

    def test_update_pick_face_assignment(self):
        """Test case for update_pick_face_assignment

        Update a pickFaceAssignment  # noqa: E501
        """
        pass

    def test_update_pick_face_assignment_custom_fields(self):
        """Test case for update_pick_face_assignment_custom_fields

        Update a pickFaceAssignment custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
