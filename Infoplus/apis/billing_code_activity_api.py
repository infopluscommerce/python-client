# coding: utf-8

"""
BillingCodeActivityApi.py
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import absolute_import

import sys
import os

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class BillingCodeActivityApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_billing_code_activity(self, body, **kwargs):
        """
        Create a billingCodeActivity
        Inserts a new billingCodeActivity using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_billing_code_activity(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BillingCodeActivity body: BillingCodeActivity to be inserted. (required)
        :return: BillingCodeActivity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_billing_code_activity" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_billing_code_activity`")

        resource_path = '/beta/billingCodeActivity'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BillingCodeActivity',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def add_billing_code_activity_audit(self, billing_code_activity_id, billing_code_activity_audit, **kwargs):
        """
        Add new audit for a billingCodeActivity
        Adds an audit to an existing billingCodeActivity.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_billing_code_activity_audit(billing_code_activity_id, billing_code_activity_audit, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int billing_code_activity_id: Id of the billingCodeActivity to add an audit to (required)
        :param str billing_code_activity_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_code_activity_id', 'billing_code_activity_audit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_billing_code_activity_audit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'billing_code_activity_id' is set
        if ('billing_code_activity_id' not in params) or (params['billing_code_activity_id'] is None):
            raise ValueError("Missing the required parameter `billing_code_activity_id` when calling `add_billing_code_activity_audit`")
        # verify the required parameter 'billing_code_activity_audit' is set
        if ('billing_code_activity_audit' not in params) or (params['billing_code_activity_audit'] is None):
            raise ValueError("Missing the required parameter `billing_code_activity_audit` when calling `add_billing_code_activity_audit`")

        resource_path = '/beta/billingCodeActivity/{billingCodeActivityId}/audit/{billingCodeActivityAudit}'.replace('{format}', 'json')
        path_params = {}
        if 'billing_code_activity_id' in params:
            path_params['billingCodeActivityId'] = params['billing_code_activity_id']
        if 'billing_code_activity_audit' in params:
            path_params['billingCodeActivityAudit'] = params['billing_code_activity_audit']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def add_billing_code_activity_tag(self, billing_code_activity_id, billing_code_activity_tag, **kwargs):
        """
        Add new tags for a billingCodeActivity.
        Adds a tag to an existing billingCodeActivity.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_billing_code_activity_tag(billing_code_activity_id, billing_code_activity_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int billing_code_activity_id: Id of the billingCodeActivity to add a tag to (required)
        :param str billing_code_activity_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_code_activity_id', 'billing_code_activity_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_billing_code_activity_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'billing_code_activity_id' is set
        if ('billing_code_activity_id' not in params) or (params['billing_code_activity_id'] is None):
            raise ValueError("Missing the required parameter `billing_code_activity_id` when calling `add_billing_code_activity_tag`")
        # verify the required parameter 'billing_code_activity_tag' is set
        if ('billing_code_activity_tag' not in params) or (params['billing_code_activity_tag'] is None):
            raise ValueError("Missing the required parameter `billing_code_activity_tag` when calling `add_billing_code_activity_tag`")

        resource_path = '/beta/billingCodeActivity/{billingCodeActivityId}/tag/{billingCodeActivityTag}'.replace('{format}', 'json')
        path_params = {}
        if 'billing_code_activity_id' in params:
            path_params['billingCodeActivityId'] = params['billing_code_activity_id']
        if 'billing_code_activity_tag' in params:
            path_params['billingCodeActivityTag'] = params['billing_code_activity_tag']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_billing_code_activity(self, billing_code_activity_id, **kwargs):
        """
        Delete a billingCodeActivity
        Deletes the billingCodeActivity identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_billing_code_activity(billing_code_activity_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int billing_code_activity_id: Id of the billingCodeActivity to be deleted. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_code_activity_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_billing_code_activity" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'billing_code_activity_id' is set
        if ('billing_code_activity_id' not in params) or (params['billing_code_activity_id'] is None):
            raise ValueError("Missing the required parameter `billing_code_activity_id` when calling `delete_billing_code_activity`")

        resource_path = '/beta/billingCodeActivity/{billingCodeActivityId}'.replace('{format}', 'json')
        path_params = {}
        if 'billing_code_activity_id' in params:
            path_params['billingCodeActivityId'] = params['billing_code_activity_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def delete_billing_code_activity_tag(self, billing_code_activity_id, billing_code_activity_tag, **kwargs):
        """
        Delete a tag for a billingCodeActivity.
        Deletes an existing billingCodeActivity tag using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_billing_code_activity_tag(billing_code_activity_id, billing_code_activity_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int billing_code_activity_id: Id of the billingCodeActivity to remove tag from (required)
        :param str billing_code_activity_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_code_activity_id', 'billing_code_activity_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_billing_code_activity_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'billing_code_activity_id' is set
        if ('billing_code_activity_id' not in params) or (params['billing_code_activity_id'] is None):
            raise ValueError("Missing the required parameter `billing_code_activity_id` when calling `delete_billing_code_activity_tag`")
        # verify the required parameter 'billing_code_activity_tag' is set
        if ('billing_code_activity_tag' not in params) or (params['billing_code_activity_tag'] is None):
            raise ValueError("Missing the required parameter `billing_code_activity_tag` when calling `delete_billing_code_activity_tag`")

        resource_path = '/beta/billingCodeActivity/{billingCodeActivityId}/tag/{billingCodeActivityTag}'.replace('{format}', 'json')
        path_params = {}
        if 'billing_code_activity_id' in params:
            path_params['billingCodeActivityId'] = params['billing_code_activity_id']
        if 'billing_code_activity_tag' in params:
            path_params['billingCodeActivityTag'] = params['billing_code_activity_tag']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'DELETE',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_billing_code_activity_by_filter(self, **kwargs):
        """
        Search billingCodeActivitys by filter
        Returns the list of billingCodeActivitys that match the given filter.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_billing_code_activity_by_filter(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[BillingCodeActivity]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'page', 'limit', 'sort']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_billing_code_activity_by_filter" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/beta/billingCodeActivity/search'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'filter' in params:
            query_params['filter'] = params['filter']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'sort' in params:
            query_params['sort'] = params['sort']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[BillingCodeActivity]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_billing_code_activity_by_id(self, billing_code_activity_id, **kwargs):
        """
        Get a billingCodeActivity by id
        Returns the billingCodeActivity identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_billing_code_activity_by_id(billing_code_activity_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int billing_code_activity_id: Id of the billingCodeActivity to be returned. (required)
        :return: BillingCodeActivity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_code_activity_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_billing_code_activity_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'billing_code_activity_id' is set
        if ('billing_code_activity_id' not in params) or (params['billing_code_activity_id'] is None):
            raise ValueError("Missing the required parameter `billing_code_activity_id` when calling `get_billing_code_activity_by_id`")

        resource_path = '/beta/billingCodeActivity/{billingCodeActivityId}'.replace('{format}', 'json')
        path_params = {}
        if 'billing_code_activity_id' in params:
            path_params['billingCodeActivityId'] = params['billing_code_activity_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BillingCodeActivity',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_billing_code_activity_tags(self, billing_code_activity_id, **kwargs):
        """
        Get the tags for a billingCodeActivity.
        Get all existing billingCodeActivity tags.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_billing_code_activity_tags(billing_code_activity_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int billing_code_activity_id: Id of the billingCodeActivity to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_code_activity_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_billing_code_activity_tags" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'billing_code_activity_id' is set
        if ('billing_code_activity_id' not in params) or (params['billing_code_activity_id'] is None):
            raise ValueError("Missing the required parameter `billing_code_activity_id` when calling `get_billing_code_activity_tags`")

        resource_path = '/beta/billingCodeActivity/{billingCodeActivityId}/tag'.replace('{format}', 'json')
        path_params = {}
        if 'billing_code_activity_id' in params:
            path_params['billingCodeActivityId'] = params['billing_code_activity_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_duplicate_billing_code_activity_by_id(self, billing_code_activity_id, **kwargs):
        """
        Get a duplicated a billingCodeActivity by id
        Returns a duplicated billingCodeActivity identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_duplicate_billing_code_activity_by_id(billing_code_activity_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int billing_code_activity_id: Id of the billingCodeActivity to be duplicated. (required)
        :return: BillingCodeActivity
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['billing_code_activity_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_billing_code_activity_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'billing_code_activity_id' is set
        if ('billing_code_activity_id' not in params) or (params['billing_code_activity_id'] is None):
            raise ValueError("Missing the required parameter `billing_code_activity_id` when calling `get_duplicate_billing_code_activity_by_id`")

        resource_path = '/beta/billingCodeActivity/duplicate/{billingCodeActivityId}'.replace('{format}', 'json')
        path_params = {}
        if 'billing_code_activity_id' in params:
            path_params['billingCodeActivityId'] = params['billing_code_activity_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='BillingCodeActivity',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def update_billing_code_activity(self, body, **kwargs):
        """
        Update a billingCodeActivity
        Updates an existing billingCodeActivity using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_billing_code_activity(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param BillingCodeActivity body: BillingCodeActivity to be updated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_billing_code_activity" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_billing_code_activity`")

        resource_path = '/beta/billingCodeActivity'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['api_key']

        response = self.api_client.call_api(resource_path, 'PUT',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
