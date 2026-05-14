# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import warnings
from typing import Any, Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPaginatedCursorPost, AsyncPaginatedCursorPost
from ...types.beta import (
    agent_data_get_params,
    agent_data_create_params,
    agent_data_delete_params,
    agent_data_search_params,
    agent_data_update_params,
    agent_data_aggregate_params,
    agent_data_delete_by_query_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.beta.agent_data import AgentData
from ...types.beta.agent_data_delete_response import AgentDataDeleteResponse
from ...types.beta.agent_data_aggregate_response import AgentDataAggregateResponse
from ...types.beta.agent_data_delete_by_query_response import AgentDataDeleteByQueryResponse

__all__ = ["AgentDataResource", "AsyncAgentDataResource"]


class AgentDataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AgentDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AgentDataResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        data: Dict[str, object],
        deployment_name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        collection: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentData:
        """
        Create new agent data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/agent-data",
            body=maybe_transform(
                {
                    "data": data,
                    "deployment_name": deployment_name,
                    "collection": collection,
                },
                agent_data_create_params.AgentDataCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_create_params.AgentDataCreateParams,
                ),
            ),
            cast_to=AgentData,
        )

    def agent_data(self, **kwargs: Any) -> AgentData:
        """Deprecated alias for :meth:`create`. Kept for backwards compatibility
        with earlier SDK versions that named the create endpoint ``agent_data``."""
        warnings.warn(
            "beta.agent_data.agent_data() is deprecated; use beta.agent_data.create() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.create(**kwargs)

    def update(
        self,
        item_id: str,
        *,
        data: Dict[str, object],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentData:
        """
        Update agent data by ID (overwrites).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._put(
            path_template("/api/v1/beta/agent-data/{item_id}", item_id=item_id),
            body=maybe_transform({"data": data}, agent_data_update_params.AgentDataUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_update_params.AgentDataUpdateParams,
                ),
            ),
            cast_to=AgentData,
        )

    def delete(
        self,
        item_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDataDeleteResponse:
        """
        Delete agent data by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._delete(
            path_template("/api/v1/beta/agent-data/{item_id}", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_delete_params.AgentDataDeleteParams,
                ),
            ),
            cast_to=AgentDataDeleteResponse,
        )

    def aggregate(
        self,
        *,
        deployment_name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        collection: str | Omit = omit,
        count: Optional[bool] | Omit = omit,
        filter: Optional[Dict[str, agent_data_aggregate_params.Filter]] | Omit = omit,
        first: Optional[bool] | Omit = omit,
        group_by: Optional[SequenceNotStr[str]] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        order_by: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursorPost[AgentDataAggregateResponse]:
        """
        Aggregate agent data with grouping and optional counting/first item retrieval.

        Args:
          deployment_name: The agent deployment's name to aggregate data for

          collection: The logical agent data collection to aggregate data for

          count: Whether to count the number of items in each group

          filter: A filter object or expression that filters resources listed in the response.

          first: Whether to return the first item in each group (Sorted by created_at)

          group_by: The fields to group by. If empty, the entire dataset is grouped on. e.g. if left
              out, can be used for simple count operations

          offset: The offset to start from. If not provided, the first page is returned

          order_by: A comma-separated list of fields to order by, sorted in ascending order. Use
              'field_name desc' to specify descending order.

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/agent-data/:aggregate",
            page=SyncPaginatedCursorPost[AgentDataAggregateResponse],
            body=maybe_transform(
                {
                    "deployment_name": deployment_name,
                    "collection": collection,
                    "count": count,
                    "filter": filter,
                    "first": first,
                    "group_by": group_by,
                    "offset": offset,
                    "order_by": order_by,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                agent_data_aggregate_params.AgentDataAggregateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_aggregate_params.AgentDataAggregateParams,
                ),
            ),
            model=AgentDataAggregateResponse,
            method="post",
        )

    def delete_by_query(
        self,
        *,
        deployment_name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        collection: str | Omit = omit,
        filter: Optional[Dict[str, agent_data_delete_by_query_params.Filter]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDataDeleteByQueryResponse:
        """
        Bulk delete agent data by query (deployment_name, collection, optional filters).

        Args:
          deployment_name: The agent deployment's name to delete data for

          collection: The logical agent data collection to delete from

          filter: Optional filters to select which items to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/agent-data/:delete",
            body=maybe_transform(
                {
                    "deployment_name": deployment_name,
                    "collection": collection,
                    "filter": filter,
                },
                agent_data_delete_by_query_params.AgentDataDeleteByQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_delete_by_query_params.AgentDataDeleteByQueryParams,
                ),
            ),
            cast_to=AgentDataDeleteByQueryResponse,
        )

    def get(
        self,
        item_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentData:
        """
        Get agent data by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._get(
            path_template("/api/v1/beta/agent-data/{item_id}", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_get_params.AgentDataGetParams,
                ),
            ),
            cast_to=AgentData,
        )

    def search(
        self,
        *,
        deployment_name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        collection: str | Omit = omit,
        filter: Optional[Dict[str, agent_data_search_params.Filter]] | Omit = omit,
        include_total: bool | Omit = omit,
        offset: Optional[int] | Omit = omit,
        order_by: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursorPost[AgentData]:
        """
        Search agent data with filtering, sorting, and pagination.

        Args:
          deployment_name: The agent deployment's name to search within

          collection: The logical agent data collection to search within

          filter: A filter object or expression that filters resources listed in the response.

          include_total: Whether to include the total number of items in the response

          offset: The offset to start from. If not provided, the first page is returned

          order_by: A comma-separated list of fields to order by, sorted in ascending order. Use
              'field_name desc' to specify descending order.

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/agent-data/:search",
            page=SyncPaginatedCursorPost[AgentData],
            body=maybe_transform(
                {
                    "deployment_name": deployment_name,
                    "collection": collection,
                    "filter": filter,
                    "include_total": include_total,
                    "offset": offset,
                    "order_by": order_by,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                agent_data_search_params.AgentDataSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_search_params.AgentDataSearchParams,
                ),
            ),
            model=AgentData,
            method="post",
        )


class AsyncAgentDataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentDataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentDataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentDataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncAgentDataResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        data: Dict[str, object],
        deployment_name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        collection: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentData:
        """
        Create new agent data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/agent-data",
            body=await async_maybe_transform(
                {
                    "data": data,
                    "deployment_name": deployment_name,
                    "collection": collection,
                },
                agent_data_create_params.AgentDataCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_create_params.AgentDataCreateParams,
                ),
            ),
            cast_to=AgentData,
        )

    async def agent_data(self, **kwargs: Any) -> AgentData:
        """Deprecated alias for :meth:`create`. Kept for backwards compatibility
        with earlier SDK versions that named the create endpoint ``agent_data``."""
        warnings.warn(
            "beta.agent_data.agent_data() is deprecated; use beta.agent_data.create() instead.",
            DeprecationWarning,
            stacklevel=2,
        )
        return await self.create(**kwargs)

    async def update(
        self,
        item_id: str,
        *,
        data: Dict[str, object],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentData:
        """
        Update agent data by ID (overwrites).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._put(
            path_template("/api/v1/beta/agent-data/{item_id}", item_id=item_id),
            body=await async_maybe_transform({"data": data}, agent_data_update_params.AgentDataUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_update_params.AgentDataUpdateParams,
                ),
            ),
            cast_to=AgentData,
        )

    async def delete(
        self,
        item_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDataDeleteResponse:
        """
        Delete agent data by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._delete(
            path_template("/api/v1/beta/agent-data/{item_id}", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_delete_params.AgentDataDeleteParams,
                ),
            ),
            cast_to=AgentDataDeleteResponse,
        )

    def aggregate(
        self,
        *,
        deployment_name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        collection: str | Omit = omit,
        count: Optional[bool] | Omit = omit,
        filter: Optional[Dict[str, agent_data_aggregate_params.Filter]] | Omit = omit,
        first: Optional[bool] | Omit = omit,
        group_by: Optional[SequenceNotStr[str]] | Omit = omit,
        offset: Optional[int] | Omit = omit,
        order_by: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AgentDataAggregateResponse, AsyncPaginatedCursorPost[AgentDataAggregateResponse]]:
        """
        Aggregate agent data with grouping and optional counting/first item retrieval.

        Args:
          deployment_name: The agent deployment's name to aggregate data for

          collection: The logical agent data collection to aggregate data for

          count: Whether to count the number of items in each group

          filter: A filter object or expression that filters resources listed in the response.

          first: Whether to return the first item in each group (Sorted by created_at)

          group_by: The fields to group by. If empty, the entire dataset is grouped on. e.g. if left
              out, can be used for simple count operations

          offset: The offset to start from. If not provided, the first page is returned

          order_by: A comma-separated list of fields to order by, sorted in ascending order. Use
              'field_name desc' to specify descending order.

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/agent-data/:aggregate",
            page=AsyncPaginatedCursorPost[AgentDataAggregateResponse],
            body=maybe_transform(
                {
                    "deployment_name": deployment_name,
                    "collection": collection,
                    "count": count,
                    "filter": filter,
                    "first": first,
                    "group_by": group_by,
                    "offset": offset,
                    "order_by": order_by,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                agent_data_aggregate_params.AgentDataAggregateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_aggregate_params.AgentDataAggregateParams,
                ),
            ),
            model=AgentDataAggregateResponse,
            method="post",
        )

    async def delete_by_query(
        self,
        *,
        deployment_name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        collection: str | Omit = omit,
        filter: Optional[Dict[str, agent_data_delete_by_query_params.Filter]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentDataDeleteByQueryResponse:
        """
        Bulk delete agent data by query (deployment_name, collection, optional filters).

        Args:
          deployment_name: The agent deployment's name to delete data for

          collection: The logical agent data collection to delete from

          filter: Optional filters to select which items to delete

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/agent-data/:delete",
            body=await async_maybe_transform(
                {
                    "deployment_name": deployment_name,
                    "collection": collection,
                    "filter": filter,
                },
                agent_data_delete_by_query_params.AgentDataDeleteByQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_delete_by_query_params.AgentDataDeleteByQueryParams,
                ),
            ),
            cast_to=AgentDataDeleteByQueryResponse,
        )

    async def get(
        self,
        item_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AgentData:
        """
        Get agent data by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._get(
            path_template("/api/v1/beta/agent-data/{item_id}", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_get_params.AgentDataGetParams,
                ),
            ),
            cast_to=AgentData,
        )

    def search(
        self,
        *,
        deployment_name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        collection: str | Omit = omit,
        filter: Optional[Dict[str, agent_data_search_params.Filter]] | Omit = omit,
        include_total: bool | Omit = omit,
        offset: Optional[int] | Omit = omit,
        order_by: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AgentData, AsyncPaginatedCursorPost[AgentData]]:
        """
        Search agent data with filtering, sorting, and pagination.

        Args:
          deployment_name: The agent deployment's name to search within

          collection: The logical agent data collection to search within

          filter: A filter object or expression that filters resources listed in the response.

          include_total: Whether to include the total number of items in the response

          offset: The offset to start from. If not provided, the first page is returned

          order_by: A comma-separated list of fields to order by, sorted in ascending order. Use
              'field_name desc' to specify descending order.

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/agent-data/:search",
            page=AsyncPaginatedCursorPost[AgentData],
            body=maybe_transform(
                {
                    "deployment_name": deployment_name,
                    "collection": collection,
                    "filter": filter,
                    "include_total": include_total,
                    "offset": offset,
                    "order_by": order_by,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                agent_data_search_params.AgentDataSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    agent_data_search_params.AgentDataSearchParams,
                ),
            ),
            model=AgentData,
            method="post",
        )


class AgentDataResourceWithRawResponse:
    def __init__(self, agent_data: AgentDataResource) -> None:
        self._agent_data = agent_data

        self.create = to_raw_response_wrapper(
            agent_data.create,
        )
        self.agent_data = to_raw_response_wrapper(
            agent_data.agent_data,
        )
        self.update = to_raw_response_wrapper(
            agent_data.update,
        )
        self.delete = to_raw_response_wrapper(
            agent_data.delete,
        )
        self.aggregate = to_raw_response_wrapper(
            agent_data.aggregate,
        )
        self.delete_by_query = to_raw_response_wrapper(
            agent_data.delete_by_query,
        )
        self.get = to_raw_response_wrapper(
            agent_data.get,
        )
        self.search = to_raw_response_wrapper(
            agent_data.search,
        )


class AsyncAgentDataResourceWithRawResponse:
    def __init__(self, agent_data: AsyncAgentDataResource) -> None:
        self._agent_data = agent_data

        self.create = async_to_raw_response_wrapper(
            agent_data.create,
        )
        self.agent_data = async_to_raw_response_wrapper(
            agent_data.agent_data,
        )
        self.update = async_to_raw_response_wrapper(
            agent_data.update,
        )
        self.delete = async_to_raw_response_wrapper(
            agent_data.delete,
        )
        self.aggregate = async_to_raw_response_wrapper(
            agent_data.aggregate,
        )
        self.delete_by_query = async_to_raw_response_wrapper(
            agent_data.delete_by_query,
        )
        self.get = async_to_raw_response_wrapper(
            agent_data.get,
        )
        self.search = async_to_raw_response_wrapper(
            agent_data.search,
        )


class AgentDataResourceWithStreamingResponse:
    def __init__(self, agent_data: AgentDataResource) -> None:
        self._agent_data = agent_data

        self.create = to_streamed_response_wrapper(
            agent_data.create,
        )
        self.agent_data = to_streamed_response_wrapper(
            agent_data.agent_data,
        )
        self.update = to_streamed_response_wrapper(
            agent_data.update,
        )
        self.delete = to_streamed_response_wrapper(
            agent_data.delete,
        )
        self.aggregate = to_streamed_response_wrapper(
            agent_data.aggregate,
        )
        self.delete_by_query = to_streamed_response_wrapper(
            agent_data.delete_by_query,
        )
        self.get = to_streamed_response_wrapper(
            agent_data.get,
        )
        self.search = to_streamed_response_wrapper(
            agent_data.search,
        )


class AsyncAgentDataResourceWithStreamingResponse:
    def __init__(self, agent_data: AsyncAgentDataResource) -> None:
        self._agent_data = agent_data

        self.create = async_to_streamed_response_wrapper(
            agent_data.create,
        )
        self.agent_data = async_to_streamed_response_wrapper(
            agent_data.agent_data,
        )
        self.update = async_to_streamed_response_wrapper(
            agent_data.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            agent_data.delete,
        )
        self.aggregate = async_to_streamed_response_wrapper(
            agent_data.aggregate,
        )
        self.delete_by_query = async_to_streamed_response_wrapper(
            agent_data.delete_by_query,
        )
        self.get = async_to_streamed_response_wrapper(
            agent_data.get,
        )
        self.search = async_to_streamed_response_wrapper(
            agent_data.search,
        )
