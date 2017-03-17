# coding: utf-8

"""
ThirdPartyParcelAccountApi.py
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


class ThirdPartyParcelAccountApi(object):
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

    def add_third_party_parcel_account(self, body, **kwargs):
        """
        Create a thirdPartyParcelAccount
        Inserts a new thirdPartyParcelAccount using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_third_party_parcel_account(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ThirdPartyParcelAccount body: ThirdPartyParcelAccount to be inserted. (required)
        :return: ThirdPartyParcelAccount
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
                    " to method add_third_party_parcel_account" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_third_party_parcel_account`")

        resource_path = '/beta/thirdPartyParcelAccount'.replace('{format}', 'json')
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
                                            response_type='ThirdPartyParcelAccount',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def add_third_party_parcel_account_audit(self, third_party_parcel_account_id, third_party_parcel_account_audit, **kwargs):
        """
        Add new audit for a thirdPartyParcelAccount
        Adds an audit to an existing thirdPartyParcelAccount.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_third_party_parcel_account_audit(third_party_parcel_account_id, third_party_parcel_account_audit, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int third_party_parcel_account_id: Id of the thirdPartyParcelAccount to add an audit to (required)
        :param str third_party_parcel_account_audit: The audit to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['third_party_parcel_account_id', 'third_party_parcel_account_audit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_third_party_parcel_account_audit" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'third_party_parcel_account_id' is set
        if ('third_party_parcel_account_id' not in params) or (params['third_party_parcel_account_id'] is None):
            raise ValueError("Missing the required parameter `third_party_parcel_account_id` when calling `add_third_party_parcel_account_audit`")
        # verify the required parameter 'third_party_parcel_account_audit' is set
        if ('third_party_parcel_account_audit' not in params) or (params['third_party_parcel_account_audit'] is None):
            raise ValueError("Missing the required parameter `third_party_parcel_account_audit` when calling `add_third_party_parcel_account_audit`")

        resource_path = '/beta/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/audit/{thirdPartyParcelAccountAudit}'.replace('{format}', 'json')
        path_params = {}
        if 'third_party_parcel_account_id' in params:
            path_params['thirdPartyParcelAccountId'] = params['third_party_parcel_account_id']
        if 'third_party_parcel_account_audit' in params:
            path_params['thirdPartyParcelAccountAudit'] = params['third_party_parcel_account_audit']

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

    def add_third_party_parcel_account_tag(self, third_party_parcel_account_id, third_party_parcel_account_tag, **kwargs):
        """
        Add new tags for a thirdPartyParcelAccount.
        Adds a tag to an existing thirdPartyParcelAccount.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_third_party_parcel_account_tag(third_party_parcel_account_id, third_party_parcel_account_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int third_party_parcel_account_id: Id of the thirdPartyParcelAccount to add a tag to (required)
        :param str third_party_parcel_account_tag: The tag to add (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['third_party_parcel_account_id', 'third_party_parcel_account_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_third_party_parcel_account_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'third_party_parcel_account_id' is set
        if ('third_party_parcel_account_id' not in params) or (params['third_party_parcel_account_id'] is None):
            raise ValueError("Missing the required parameter `third_party_parcel_account_id` when calling `add_third_party_parcel_account_tag`")
        # verify the required parameter 'third_party_parcel_account_tag' is set
        if ('third_party_parcel_account_tag' not in params) or (params['third_party_parcel_account_tag'] is None):
            raise ValueError("Missing the required parameter `third_party_parcel_account_tag` when calling `add_third_party_parcel_account_tag`")

        resource_path = '/beta/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/tag/{thirdPartyParcelAccountTag}'.replace('{format}', 'json')
        path_params = {}
        if 'third_party_parcel_account_id' in params:
            path_params['thirdPartyParcelAccountId'] = params['third_party_parcel_account_id']
        if 'third_party_parcel_account_tag' in params:
            path_params['thirdPartyParcelAccountTag'] = params['third_party_parcel_account_tag']

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

    def delete_third_party_parcel_account(self, third_party_parcel_account_id, **kwargs):
        """
        Delete a thirdPartyParcelAccount
        Deletes the thirdPartyParcelAccount identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_third_party_parcel_account(third_party_parcel_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int third_party_parcel_account_id: Id of the thirdPartyParcelAccount to be deleted. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['third_party_parcel_account_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_third_party_parcel_account" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'third_party_parcel_account_id' is set
        if ('third_party_parcel_account_id' not in params) or (params['third_party_parcel_account_id'] is None):
            raise ValueError("Missing the required parameter `third_party_parcel_account_id` when calling `delete_third_party_parcel_account`")

        resource_path = '/beta/thirdPartyParcelAccount/{thirdPartyParcelAccountId}'.replace('{format}', 'json')
        path_params = {}
        if 'third_party_parcel_account_id' in params:
            path_params['thirdPartyParcelAccountId'] = params['third_party_parcel_account_id']

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

    def delete_third_party_parcel_account_tag(self, third_party_parcel_account_id, third_party_parcel_account_tag, **kwargs):
        """
        Delete a tag for a thirdPartyParcelAccount.
        Deletes an existing thirdPartyParcelAccount tag using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_third_party_parcel_account_tag(third_party_parcel_account_id, third_party_parcel_account_tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int third_party_parcel_account_id: Id of the thirdPartyParcelAccount to remove tag from (required)
        :param str third_party_parcel_account_tag: The tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['third_party_parcel_account_id', 'third_party_parcel_account_tag']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_third_party_parcel_account_tag" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'third_party_parcel_account_id' is set
        if ('third_party_parcel_account_id' not in params) or (params['third_party_parcel_account_id'] is None):
            raise ValueError("Missing the required parameter `third_party_parcel_account_id` when calling `delete_third_party_parcel_account_tag`")
        # verify the required parameter 'third_party_parcel_account_tag' is set
        if ('third_party_parcel_account_tag' not in params) or (params['third_party_parcel_account_tag'] is None):
            raise ValueError("Missing the required parameter `third_party_parcel_account_tag` when calling `delete_third_party_parcel_account_tag`")

        resource_path = '/beta/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/tag/{thirdPartyParcelAccountTag}'.replace('{format}', 'json')
        path_params = {}
        if 'third_party_parcel_account_id' in params:
            path_params['thirdPartyParcelAccountId'] = params['third_party_parcel_account_id']
        if 'third_party_parcel_account_tag' in params:
            path_params['thirdPartyParcelAccountTag'] = params['third_party_parcel_account_tag']

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

    def get_duplicate_third_party_parcel_account_by_id(self, third_party_parcel_account_id, **kwargs):
        """
        Get a duplicated a thirdPartyParcelAccount by id
        Returns a duplicated thirdPartyParcelAccount identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_duplicate_third_party_parcel_account_by_id(third_party_parcel_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int third_party_parcel_account_id: Id of the thirdPartyParcelAccount to be duplicated. (required)
        :return: ThirdPartyParcelAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['third_party_parcel_account_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_duplicate_third_party_parcel_account_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'third_party_parcel_account_id' is set
        if ('third_party_parcel_account_id' not in params) or (params['third_party_parcel_account_id'] is None):
            raise ValueError("Missing the required parameter `third_party_parcel_account_id` when calling `get_duplicate_third_party_parcel_account_by_id`")

        resource_path = '/beta/thirdPartyParcelAccount/duplicate/{thirdPartyParcelAccountId}'.replace('{format}', 'json')
        path_params = {}
        if 'third_party_parcel_account_id' in params:
            path_params['thirdPartyParcelAccountId'] = params['third_party_parcel_account_id']

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
                                            response_type='ThirdPartyParcelAccount',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_third_party_parcel_account_by_filter(self, **kwargs):
        """
        Search thirdPartyParcelAccounts by filter
        Returns the list of thirdPartyParcelAccounts that match the given filter.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_third_party_parcel_account_by_filter(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str filter: Query string, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :param str sort: Sort results by specified field.
        :return: list[ThirdPartyParcelAccount]
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
                    " to method get_third_party_parcel_account_by_filter" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/beta/thirdPartyParcelAccount/search'.replace('{format}', 'json')
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
                                            response_type='list[ThirdPartyParcelAccount]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_third_party_parcel_account_by_id(self, third_party_parcel_account_id, **kwargs):
        """
        Get a thirdPartyParcelAccount by id
        Returns the thirdPartyParcelAccount identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_third_party_parcel_account_by_id(third_party_parcel_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int third_party_parcel_account_id: Id of the thirdPartyParcelAccount to be returned. (required)
        :return: ThirdPartyParcelAccount
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['third_party_parcel_account_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_third_party_parcel_account_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'third_party_parcel_account_id' is set
        if ('third_party_parcel_account_id' not in params) or (params['third_party_parcel_account_id'] is None):
            raise ValueError("Missing the required parameter `third_party_parcel_account_id` when calling `get_third_party_parcel_account_by_id`")

        resource_path = '/beta/thirdPartyParcelAccount/{thirdPartyParcelAccountId}'.replace('{format}', 'json')
        path_params = {}
        if 'third_party_parcel_account_id' in params:
            path_params['thirdPartyParcelAccountId'] = params['third_party_parcel_account_id']

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
                                            response_type='ThirdPartyParcelAccount',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_third_party_parcel_account_tags(self, third_party_parcel_account_id, **kwargs):
        """
        Get the tags for a thirdPartyParcelAccount.
        Get all existing thirdPartyParcelAccount tags.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_third_party_parcel_account_tags(third_party_parcel_account_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int third_party_parcel_account_id: Id of the thirdPartyParcelAccount to get tags for (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['third_party_parcel_account_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_third_party_parcel_account_tags" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'third_party_parcel_account_id' is set
        if ('third_party_parcel_account_id' not in params) or (params['third_party_parcel_account_id'] is None):
            raise ValueError("Missing the required parameter `third_party_parcel_account_id` when calling `get_third_party_parcel_account_tags`")

        resource_path = '/beta/thirdPartyParcelAccount/{thirdPartyParcelAccountId}/tag'.replace('{format}', 'json')
        path_params = {}
        if 'third_party_parcel_account_id' in params:
            path_params['thirdPartyParcelAccountId'] = params['third_party_parcel_account_id']

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

    def update_third_party_parcel_account(self, body, **kwargs):
        """
        Update a thirdPartyParcelAccount
        Updates an existing thirdPartyParcelAccount using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_third_party_parcel_account(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ThirdPartyParcelAccount body: ThirdPartyParcelAccount to be updated. (required)
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
                    " to method update_third_party_parcel_account" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_third_party_parcel_account`")

        resource_path = '/beta/thirdPartyParcelAccount'.replace('{format}', 'json')
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

    def update_third_party_parcel_account_custom_fields(self, body, **kwargs):
        """
        Update a thirdPartyParcelAccount custom fields
        Updates an existing thirdPartyParcelAccount custom fields using the specified data.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_third_party_parcel_account_custom_fields(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param ThirdPartyParcelAccount body: ThirdPartyParcelAccount to be updated. (required)
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
                    " to method update_third_party_parcel_account_custom_fields" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_third_party_parcel_account_custom_fields`")

        resource_path = '/beta/thirdPartyParcelAccount/customFields'.replace('{format}', 'json')
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
