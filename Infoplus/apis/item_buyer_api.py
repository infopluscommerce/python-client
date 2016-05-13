# coding: utf-8

"""
ItemBuyerApi.py
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


class ItemBuyerApi(object):
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

    def get_item_buyer_by_search_text(self, **kwargs):
        """
        Search itemBuyers
        Returns the list of itemBuyers that match the given searchText.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_item_buyer_by_search_text(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str search_text: Search text, used to filter results.
        :param int page: Result page number.  Defaults to 1.
        :param int limit: Maximum results per page.  Defaults to 20.  Max allowed value is 250.
        :return: list[ItemBuyer]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['search_text', 'page', 'limit']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_item_buyer_by_search_text" % key
                )
            params[key] = val
        del params['kwargs']


        resource_path = '/v1.0/itemBuyer/search'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'search_text' in params:
            query_params['searchText'] = params['search_text']
        if 'page' in params:
            query_params['page'] = params['page']
        if 'limit' in params:
            query_params['limit'] = params['limit']

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
                                            response_type='list[ItemBuyer]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response

    def get_translate_buyer_by_id(self, item_buyer_id, **kwargs):
        """
        Get an itemBuyer by id
        Returns the itemBuyer identified by the specified id.

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_translate_buyer_by_id(item_buyer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str item_buyer_id: Id of itemBuyer to be returned. (required)
        :return: ItemBuyer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['item_buyer_id']
        all_params.append('callback')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_translate_buyer_by_id" % key
                )
            params[key] = val
        del params['kwargs']

        # verify the required parameter 'item_buyer_id' is set
        if ('item_buyer_id' not in params) or (params['item_buyer_id'] is None):
            raise ValueError("Missing the required parameter `item_buyer_id` when calling `get_translate_buyer_by_id`")

        resource_path = '/v1.0/itemBuyer/{itemBuyerId}'.replace('{format}', 'json')
        path_params = {}
        if 'item_buyer_id' in params:
            path_params['itemBuyerId'] = params['item_buyer_id']

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
                                            response_type='ItemBuyer',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'))
        return response
