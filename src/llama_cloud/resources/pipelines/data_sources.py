# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ..._base_client import make_request_options
from ...types.pipeline import Pipeline
from ...types.pipelines import (
    data_source_sync_params,
    data_source_update_params,
    data_source_update_data_sources_params,
)
from ...types.pipelines.pipeline_data_source import PipelineDataSource
from ...types.managed_ingestion_status_response import ManagedIngestionStatusResponse
from ...types.pipelines.data_source_get_data_sources_response import DataSourceGetDataSourcesResponse
from ...types.pipelines.data_source_update_data_sources_response import DataSourceUpdateDataSourcesResponse

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

    def update(
        self,
        data_source_id: str,
        *,
        pipeline_id: str,
        sync_interval: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineDataSource:
        """
        Update the configuration of a data source in a pipeline.

        Args:
          sync_interval: The interval at which the data source should be synced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return self._put(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}",
                pipeline_id=pipeline_id,
                data_source_id=data_source_id,
            ),
            body=maybe_transform({"sync_interval": sync_interval}, data_source_update_params.DataSourceUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineDataSource,
        )

    def get_data_sources(
        self,
        pipeline_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceGetDataSourcesResponse:
        """
        Get data sources for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get(
            path_template("/api/v1/pipelines/{pipeline_id}/data-sources", pipeline_id=pipeline_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceGetDataSourcesResponse,
        )

    def get_status(
        self,
        data_source_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedIngestionStatusResponse:
        """
        Get the status of a data source for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return self._get(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/status",
                pipeline_id=pipeline_id,
                data_source_id=data_source_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedIngestionStatusResponse,
        )

    def sync(
        self,
        data_source_id: str,
        *,
        pipeline_id: str,
        pipeline_file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Run ingestion for the pipeline data source by incrementally updating the
        data-sink with upstream changes from data-source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return self._post(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/sync",
                pipeline_id=pipeline_id,
                data_source_id=data_source_id,
            ),
            body=maybe_transform(
                {"pipeline_file_ids": pipeline_file_ids}, data_source_sync_params.DataSourceSyncParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    def update_data_sources(
        self,
        pipeline_id: str,
        *,
        body: Iterable[data_source_update_data_sources_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceUpdateDataSourcesResponse:
        """
        Add data sources to a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._put(
            path_template("/api/v1/pipelines/{pipeline_id}/data-sources", pipeline_id=pipeline_id),
            body=maybe_transform(body, Iterable[data_source_update_data_sources_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceUpdateDataSourcesResponse,
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

    async def update(
        self,
        data_source_id: str,
        *,
        pipeline_id: str,
        sync_interval: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PipelineDataSource:
        """
        Update the configuration of a data source in a pipeline.

        Args:
          sync_interval: The interval at which the data source should be synced.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return await self._put(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}",
                pipeline_id=pipeline_id,
                data_source_id=data_source_id,
            ),
            body=await async_maybe_transform(
                {"sync_interval": sync_interval}, data_source_update_params.DataSourceUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PipelineDataSource,
        )

    async def get_data_sources(
        self,
        pipeline_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceGetDataSourcesResponse:
        """
        Get data sources for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._get(
            path_template("/api/v1/pipelines/{pipeline_id}/data-sources", pipeline_id=pipeline_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceGetDataSourcesResponse,
        )

    async def get_status(
        self,
        data_source_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedIngestionStatusResponse:
        """
        Get the status of a data source for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return await self._get(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/status",
                pipeline_id=pipeline_id,
                data_source_id=data_source_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedIngestionStatusResponse,
        )

    async def sync(
        self,
        data_source_id: str,
        *,
        pipeline_id: str,
        pipeline_file_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Pipeline:
        """
        Run ingestion for the pipeline data source by incrementally updating the
        data-sink with upstream changes from data-source.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not data_source_id:
            raise ValueError(f"Expected a non-empty value for `data_source_id` but received {data_source_id!r}")
        return await self._post(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/data-sources/{data_source_id}/sync",
                pipeline_id=pipeline_id,
                data_source_id=data_source_id,
            ),
            body=await async_maybe_transform(
                {"pipeline_file_ids": pipeline_file_ids}, data_source_sync_params.DataSourceSyncParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Pipeline,
        )

    async def update_data_sources(
        self,
        pipeline_id: str,
        *,
        body: Iterable[data_source_update_data_sources_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DataSourceUpdateDataSourcesResponse:
        """
        Add data sources to a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._put(
            path_template("/api/v1/pipelines/{pipeline_id}/data-sources", pipeline_id=pipeline_id),
            body=await async_maybe_transform(body, Iterable[data_source_update_data_sources_params.Body]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DataSourceUpdateDataSourcesResponse,
        )


class DataSourcesResourceWithRawResponse:
    def __init__(self, data_sources: DataSourcesResource) -> None:
        self._data_sources = data_sources

        self.update = to_raw_response_wrapper(
            data_sources.update,
        )
        self.get_data_sources = to_raw_response_wrapper(
            data_sources.get_data_sources,
        )
        self.get_status = to_raw_response_wrapper(
            data_sources.get_status,
        )
        self.sync = to_raw_response_wrapper(
            data_sources.sync,
        )
        self.update_data_sources = to_raw_response_wrapper(
            data_sources.update_data_sources,
        )


class AsyncDataSourcesResourceWithRawResponse:
    def __init__(self, data_sources: AsyncDataSourcesResource) -> None:
        self._data_sources = data_sources

        self.update = async_to_raw_response_wrapper(
            data_sources.update,
        )
        self.get_data_sources = async_to_raw_response_wrapper(
            data_sources.get_data_sources,
        )
        self.get_status = async_to_raw_response_wrapper(
            data_sources.get_status,
        )
        self.sync = async_to_raw_response_wrapper(
            data_sources.sync,
        )
        self.update_data_sources = async_to_raw_response_wrapper(
            data_sources.update_data_sources,
        )


class DataSourcesResourceWithStreamingResponse:
    def __init__(self, data_sources: DataSourcesResource) -> None:
        self._data_sources = data_sources

        self.update = to_streamed_response_wrapper(
            data_sources.update,
        )
        self.get_data_sources = to_streamed_response_wrapper(
            data_sources.get_data_sources,
        )
        self.get_status = to_streamed_response_wrapper(
            data_sources.get_status,
        )
        self.sync = to_streamed_response_wrapper(
            data_sources.sync,
        )
        self.update_data_sources = to_streamed_response_wrapper(
            data_sources.update_data_sources,
        )


class AsyncDataSourcesResourceWithStreamingResponse:
    def __init__(self, data_sources: AsyncDataSourcesResource) -> None:
        self._data_sources = data_sources

        self.update = async_to_streamed_response_wrapper(
            data_sources.update,
        )
        self.get_data_sources = async_to_streamed_response_wrapper(
            data_sources.get_data_sources,
        )
        self.get_status = async_to_streamed_response_wrapper(
            data_sources.get_status,
        )
        self.sync = async_to_streamed_response_wrapper(
            data_sources.sync,
        )
        self.update_data_sources = async_to_streamed_response_wrapper(
            data_sources.update_data_sources,
        )
