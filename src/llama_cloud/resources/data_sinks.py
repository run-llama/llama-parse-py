# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Optional
from typing_extensions import Literal

import httpx

from ..types import (
    data_sink_list_params,
    data_sink_create_params,
    data_sink_update_params,
    data_sink_list_paginated_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.data_sink import DataSink
from ..types.data_sink_list_response import DataSinkListResponse

__all__ = ["DataSinksResource", "AsyncDataSinksResource"]


class DataSinksResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataSinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return DataSinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataSinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return DataSinksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        component: data_sink_create_params.Component,
        name: str,
        sink_type: Literal["ASTRA_DB", "AZUREAI_SEARCH", "MILVUS", "MONGODB_ATLAS", "PINECONE", "POSTGRES", "QDRANT"],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSink:
        """
        Create a new data sink.

        Args:
          component: Component that implements the data sink

          name: The name of the data sink.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/data-sinks",
            body=maybe_transform(
                {
                    "component": component,
                    "name": name,
                    "sink_type": sink_type,
                },
                data_sink_create_params.DataSinkCreateParams,
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
                    data_sink_create_params.DataSinkCreateParams,
                ),
            ),
            cast_to=DataSink,
        )

    def update(
        self,
        data_sink_id: str,
        *,
        sink_type: Literal["ASTRA_DB", "AZUREAI_SEARCH", "MILVUS", "MONGODB_ATLAS", "PINECONE", "POSTGRES", "QDRANT"],
        component: Optional[data_sink_update_params.Component] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSink:
        """
        Update a data sink by ID.

        Args:
          component: Component that implements the data sink

          name: The name of the data sink.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_sink_id:
            raise ValueError(f"Expected a non-empty value for `data_sink_id` but received {data_sink_id!r}")
        return self._put(
            path_template("/api/v1/data-sinks/{data_sink_id}", data_sink_id=data_sink_id),
            body=maybe_transform(
                {
                    "sink_type": sink_type,
                    "component": component,
                    "name": name,
                },
                data_sink_update_params.DataSinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSink,
        )

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSinkListResponse:
        """List a project's data sinks.

        Returns at most the first 50.

        Deprecated: use `GET /api/v1/beta/data-sinks`, which is paginated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/data-sinks",
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
                    data_sink_list_params.DataSinkListParams,
                ),
            ),
            cast_to=DataSinkListResponse,
        )

    def delete(
        self,
        data_sink_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a data sink by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_sink_id:
            raise ValueError(f"Expected a non-empty value for `data_sink_id` but received {data_sink_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/data-sinks/{data_sink_id}", data_sink_id=data_sink_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        data_sink_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSink:
        """
        Get a data sink by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_sink_id:
            raise ValueError(f"Expected a non-empty value for `data_sink_id` but received {data_sink_id!r}")
        return self._get(
            path_template("/api/v1/data-sinks/{data_sink_id}", data_sink_id=data_sink_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSink,
        )

    def list_paginated(
        self,
        *,
        include_total: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[DataSink]:
        """
        List the data sinks in a project, newest first.

        Args:
          include_total: Return `total_size`, a count of every row matching the filter. It is a second
              query on every page, so it is off unless asked for.

          page_size: Number of items per page

          page_token: Cursor from the previous page's `next_page_token`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/data-sinks",
            page=SyncPaginatedCursor[DataSink],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_total": include_total,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    data_sink_list_paginated_params.DataSinkListPaginatedParams,
                ),
            ),
            model=DataSink,
        )


class AsyncDataSinksResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataSinksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncDataSinksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataSinksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncDataSinksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        component: data_sink_create_params.Component,
        name: str,
        sink_type: Literal["ASTRA_DB", "AZUREAI_SEARCH", "MILVUS", "MONGODB_ATLAS", "PINECONE", "POSTGRES", "QDRANT"],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSink:
        """
        Create a new data sink.

        Args:
          component: Component that implements the data sink

          name: The name of the data sink.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/data-sinks",
            body=await async_maybe_transform(
                {
                    "component": component,
                    "name": name,
                    "sink_type": sink_type,
                },
                data_sink_create_params.DataSinkCreateParams,
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
                    data_sink_create_params.DataSinkCreateParams,
                ),
            ),
            cast_to=DataSink,
        )

    async def update(
        self,
        data_sink_id: str,
        *,
        sink_type: Literal["ASTRA_DB", "AZUREAI_SEARCH", "MILVUS", "MONGODB_ATLAS", "PINECONE", "POSTGRES", "QDRANT"],
        component: Optional[data_sink_update_params.Component] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSink:
        """
        Update a data sink by ID.

        Args:
          component: Component that implements the data sink

          name: The name of the data sink.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_sink_id:
            raise ValueError(f"Expected a non-empty value for `data_sink_id` but received {data_sink_id!r}")
        return await self._put(
            path_template("/api/v1/data-sinks/{data_sink_id}", data_sink_id=data_sink_id),
            body=await async_maybe_transform(
                {
                    "sink_type": sink_type,
                    "component": component,
                    "name": name,
                },
                data_sink_update_params.DataSinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSink,
        )

    @typing_extensions.deprecated("deprecated")
    async def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSinkListResponse:
        """List a project's data sinks.

        Returns at most the first 50.

        Deprecated: use `GET /api/v1/beta/data-sinks`, which is paginated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/data-sinks",
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
                    data_sink_list_params.DataSinkListParams,
                ),
            ),
            cast_to=DataSinkListResponse,
        )

    async def delete(
        self,
        data_sink_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a data sink by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_sink_id:
            raise ValueError(f"Expected a non-empty value for `data_sink_id` but received {data_sink_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/data-sinks/{data_sink_id}", data_sink_id=data_sink_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        data_sink_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSink:
        """
        Get a data sink by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_sink_id:
            raise ValueError(f"Expected a non-empty value for `data_sink_id` but received {data_sink_id!r}")
        return await self._get(
            path_template("/api/v1/data-sinks/{data_sink_id}", data_sink_id=data_sink_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSink,
        )

    def list_paginated(
        self,
        *,
        include_total: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DataSink, AsyncPaginatedCursor[DataSink]]:
        """
        List the data sinks in a project, newest first.

        Args:
          include_total: Return `total_size`, a count of every row matching the filter. It is a second
              query on every page, so it is off unless asked for.

          page_size: Number of items per page

          page_token: Cursor from the previous page's `next_page_token`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/data-sinks",
            page=AsyncPaginatedCursor[DataSink],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_total": include_total,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    data_sink_list_paginated_params.DataSinkListPaginatedParams,
                ),
            ),
            model=DataSink,
        )


class DataSinksResourceWithRawResponse:
    def __init__(self, data_sinks: DataSinksResource) -> None:
        self._data_sinks = data_sinks

        self.create = to_raw_response_wrapper(
            data_sinks.create,
        )
        self.update = to_raw_response_wrapper(
            data_sinks.update,
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                data_sinks.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = to_raw_response_wrapper(
            data_sinks.delete,
        )
        self.get = to_raw_response_wrapper(
            data_sinks.get,
        )
        self.list_paginated = to_raw_response_wrapper(
            data_sinks.list_paginated,
        )


class AsyncDataSinksResourceWithRawResponse:
    def __init__(self, data_sinks: AsyncDataSinksResource) -> None:
        self._data_sinks = data_sinks

        self.create = async_to_raw_response_wrapper(
            data_sinks.create,
        )
        self.update = async_to_raw_response_wrapper(
            data_sinks.update,
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                data_sinks.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = async_to_raw_response_wrapper(
            data_sinks.delete,
        )
        self.get = async_to_raw_response_wrapper(
            data_sinks.get,
        )
        self.list_paginated = async_to_raw_response_wrapper(
            data_sinks.list_paginated,
        )


class DataSinksResourceWithStreamingResponse:
    def __init__(self, data_sinks: DataSinksResource) -> None:
        self._data_sinks = data_sinks

        self.create = to_streamed_response_wrapper(
            data_sinks.create,
        )
        self.update = to_streamed_response_wrapper(
            data_sinks.update,
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                data_sinks.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = to_streamed_response_wrapper(
            data_sinks.delete,
        )
        self.get = to_streamed_response_wrapper(
            data_sinks.get,
        )
        self.list_paginated = to_streamed_response_wrapper(
            data_sinks.list_paginated,
        )


class AsyncDataSinksResourceWithStreamingResponse:
    def __init__(self, data_sinks: AsyncDataSinksResource) -> None:
        self._data_sinks = data_sinks

        self.create = async_to_streamed_response_wrapper(
            data_sinks.create,
        )
        self.update = async_to_streamed_response_wrapper(
            data_sinks.update,
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                data_sinks.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = async_to_streamed_response_wrapper(
            data_sinks.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            data_sinks.get,
        )
        self.list_paginated = async_to_streamed_response_wrapper(
            data_sinks.list_paginated,
        )
