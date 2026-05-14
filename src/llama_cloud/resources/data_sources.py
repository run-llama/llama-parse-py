# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import data_source_list_params, data_source_create_params, data_source_update_params
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
from .._base_client import make_request_options
from ..types.data_source import DataSource
from ..types.data_source_list_response import DataSourceListResponse

__all__ = ["DataSourcesResource", "AsyncDataSourcesResource"]


class DataSourcesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DataSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return DataSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DataSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return DataSourcesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        component: data_source_create_params.Component,
        name: str,
        source_type: Literal[
            "S3",
            "AZURE_STORAGE_BLOB",
            "GOOGLE_DRIVE",
            "MICROSOFT_ONEDRIVE",
            "MICROSOFT_SHAREPOINT",
            "SLACK",
            "NOTION_PAGE",
            "CONFLUENCE",
            "JIRA",
            "JIRA_V2",
            "BOX",
        ],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSource:
        """
        Create a new data source.

        Args:
          component: Component that implements the data source

          name: The name of the data source.

          custom_metadata: Custom metadata that will be present on all data loaded from the data source

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/data-sources",
            body=maybe_transform(
                {
                    "component": component,
                    "name": name,
                    "source_type": source_type,
                    "custom_metadata": custom_metadata,
                },
                data_source_create_params.DataSourceCreateParams,
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
                    data_source_create_params.DataSourceCreateParams,
                ),
            ),
            cast_to=DataSource,
        )

    def update(
        self,
        data_source_id: str,
        *,
        source_type: Literal[
            "S3",
            "AZURE_STORAGE_BLOB",
            "GOOGLE_DRIVE",
            "MICROSOFT_ONEDRIVE",
            "MICROSOFT_SHAREPOINT",
            "SLACK",
            "NOTION_PAGE",
            "CONFLUENCE",
            "JIRA",
            "JIRA_V2",
            "BOX",
        ],
        component: Optional[data_source_update_params.Component] | Omit = omit,
        custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSource:
        """
        Update a data source by ID.

        Args:
          component: Component that implements the data source

          custom_metadata: Custom metadata that will be present on all data loaded from the data source

          name: The name of the data source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return self._put(
            path_template("/api/v1/data-sources/{data_source_id}", data_source_id=data_source_id),
            body=maybe_transform(
                {
                    "source_type": source_type,
                    "component": component,
                    "custom_metadata": custom_metadata,
                    "name": name,
                },
                data_source_update_params.DataSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )

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
    ) -> DataSourceListResponse:
        """List data sources for a given project.

        If project_id is not provided, uses the
        default project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/data-sources",
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
                    data_source_list_params.DataSourceListParams,
                ),
            ),
            cast_to=DataSourceListResponse,
        )

    def delete(
        self,
        data_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a data source by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/data-sources/{data_source_id}", data_source_id=data_source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        data_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSource:
        """
        Get a data source by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return self._get(
            path_template("/api/v1/data-sources/{data_source_id}", data_source_id=data_source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )


class AsyncDataSourcesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDataSourcesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncDataSourcesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDataSourcesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncDataSourcesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        component: data_source_create_params.Component,
        name: str,
        source_type: Literal[
            "S3",
            "AZURE_STORAGE_BLOB",
            "GOOGLE_DRIVE",
            "MICROSOFT_ONEDRIVE",
            "MICROSOFT_SHAREPOINT",
            "SLACK",
            "NOTION_PAGE",
            "CONFLUENCE",
            "JIRA",
            "JIRA_V2",
            "BOX",
        ],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSource:
        """
        Create a new data source.

        Args:
          component: Component that implements the data source

          name: The name of the data source.

          custom_metadata: Custom metadata that will be present on all data loaded from the data source

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/data-sources",
            body=await async_maybe_transform(
                {
                    "component": component,
                    "name": name,
                    "source_type": source_type,
                    "custom_metadata": custom_metadata,
                },
                data_source_create_params.DataSourceCreateParams,
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
                    data_source_create_params.DataSourceCreateParams,
                ),
            ),
            cast_to=DataSource,
        )

    async def update(
        self,
        data_source_id: str,
        *,
        source_type: Literal[
            "S3",
            "AZURE_STORAGE_BLOB",
            "GOOGLE_DRIVE",
            "MICROSOFT_ONEDRIVE",
            "MICROSOFT_SHAREPOINT",
            "SLACK",
            "NOTION_PAGE",
            "CONFLUENCE",
            "JIRA",
            "JIRA_V2",
            "BOX",
        ],
        component: Optional[data_source_update_params.Component] | Omit = omit,
        custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSource:
        """
        Update a data source by ID.

        Args:
          component: Component that implements the data source

          custom_metadata: Custom metadata that will be present on all data loaded from the data source

          name: The name of the data source.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return await self._put(
            path_template("/api/v1/data-sources/{data_source_id}", data_source_id=data_source_id),
            body=await async_maybe_transform(
                {
                    "source_type": source_type,
                    "component": component,
                    "custom_metadata": custom_metadata,
                    "name": name,
                },
                data_source_update_params.DataSourceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )

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
    ) -> DataSourceListResponse:
        """List data sources for a given project.

        If project_id is not provided, uses the
        default project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/data-sources",
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
                    data_source_list_params.DataSourceListParams,
                ),
            ),
            cast_to=DataSourceListResponse,
        )

    async def delete(
        self,
        data_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a data source by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/data-sources/{data_source_id}", data_source_id=data_source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        data_source_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSource:
        """
        Get a data source by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return await self._get(
            path_template("/api/v1/data-sources/{data_source_id}", data_source_id=data_source_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSource,
        )


class DataSourcesResourceWithRawResponse:
    def __init__(self, data_sources: DataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = to_raw_response_wrapper(
            data_sources.create,
        )
        self.update = to_raw_response_wrapper(
            data_sources.update,
        )
        self.list = to_raw_response_wrapper(
            data_sources.list,
        )
        self.delete = to_raw_response_wrapper(
            data_sources.delete,
        )
        self.get = to_raw_response_wrapper(
            data_sources.get,
        )


class AsyncDataSourcesResourceWithRawResponse:
    def __init__(self, data_sources: AsyncDataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = async_to_raw_response_wrapper(
            data_sources.create,
        )
        self.update = async_to_raw_response_wrapper(
            data_sources.update,
        )
        self.list = async_to_raw_response_wrapper(
            data_sources.list,
        )
        self.delete = async_to_raw_response_wrapper(
            data_sources.delete,
        )
        self.get = async_to_raw_response_wrapper(
            data_sources.get,
        )


class DataSourcesResourceWithStreamingResponse:
    def __init__(self, data_sources: DataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = to_streamed_response_wrapper(
            data_sources.create,
        )
        self.update = to_streamed_response_wrapper(
            data_sources.update,
        )
        self.list = to_streamed_response_wrapper(
            data_sources.list,
        )
        self.delete = to_streamed_response_wrapper(
            data_sources.delete,
        )
        self.get = to_streamed_response_wrapper(
            data_sources.get,
        )


class AsyncDataSourcesResourceWithStreamingResponse:
    def __init__(self, data_sources: AsyncDataSourcesResource) -> None:
        self._data_sources = data_sources

        self.create = async_to_streamed_response_wrapper(
            data_sources.create,
        )
        self.update = async_to_streamed_response_wrapper(
            data_sources.update,
        )
        self.list = async_to_streamed_response_wrapper(
            data_sources.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            data_sources.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            data_sources.get,
        )
