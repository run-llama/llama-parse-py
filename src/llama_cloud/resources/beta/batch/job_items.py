# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPaginatedBatchItems, AsyncPaginatedBatchItems
from ...._base_client import AsyncPaginator, make_request_options
from ....types.beta.batch import job_item_list_params, job_item_get_processing_results_params
from ....types.beta.batch.job_item_list_response import JobItemListResponse
from ....types.beta.batch.job_item_get_processing_results_response import JobItemGetProcessingResultsResponse

__all__ = ["JobItemsResource", "AsyncJobItemsResource"]


class JobItemsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return JobItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return JobItemsResourceWithStreamingResponse(self)

    def list(
        self,
        job_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["pending", "processing", "completed", "failed", "skipped", "cancelled"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedBatchItems[JobItemListResponse]:
        """
        List items in a batch job with optional status filtering.

        Useful for finding failed items, viewing completed items, or debugging
        processing issues.

        Args:
          limit: Maximum number of items to return

          offset: Number of items to skip

          status: Filter items by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get_api_list(
            path_template("/api/v1/beta/batch-processing/{job_id}/items", job_id=job_id),
            page=SyncPaginatedBatchItems[JobItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "organization_id": organization_id,
                        "project_id": project_id,
                        "status": status,
                    },
                    job_item_list_params.JobItemListParams,
                ),
            ),
            model=JobItemListResponse,
        )

    def get_processing_results(
        self,
        item_id: str,
        *,
        job_type: Optional[Literal["parse", "extract", "classify"]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobItemGetProcessingResultsResponse:
        """
        Get all processing results for a specific item.

        Returns the complete processing history for an item including what operations
        were performed, parameters used, and where outputs are stored. Optionally filter
        by `job_type`.

        Args:
          job_type: Filter results by job type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return self._get(
            path_template("/api/v1/beta/batch-processing/items/{item_id}/processing-results", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "job_type": job_type,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    job_item_get_processing_results_params.JobItemGetProcessingResultsParams,
                ),
            ),
            cast_to=JobItemGetProcessingResultsResponse,
        )


class AsyncJobItemsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobItemsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncJobItemsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobItemsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncJobItemsResourceWithStreamingResponse(self)

    def list(
        self,
        job_id: str,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["pending", "processing", "completed", "failed", "skipped", "cancelled"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[JobItemListResponse, AsyncPaginatedBatchItems[JobItemListResponse]]:
        """
        List items in a batch job with optional status filtering.

        Useful for finding failed items, viewing completed items, or debugging
        processing issues.

        Args:
          limit: Maximum number of items to return

          offset: Number of items to skip

          status: Filter items by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get_api_list(
            path_template("/api/v1/beta/batch-processing/{job_id}/items", job_id=job_id),
            page=AsyncPaginatedBatchItems[JobItemListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "organization_id": organization_id,
                        "project_id": project_id,
                        "status": status,
                    },
                    job_item_list_params.JobItemListParams,
                ),
            ),
            model=JobItemListResponse,
        )

    async def get_processing_results(
        self,
        item_id: str,
        *,
        job_type: Optional[Literal["parse", "extract", "classify"]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobItemGetProcessingResultsResponse:
        """
        Get all processing results for a specific item.

        Returns the complete processing history for an item including what operations
        were performed, parameters used, and where outputs are stored. Optionally filter
        by `job_type`.

        Args:
          job_type: Filter results by job type

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not item_id:
            raise ValueError(f"Expected a non-empty value for `item_id` but received {item_id!r}")
        return await self._get(
            path_template("/api/v1/beta/batch-processing/items/{item_id}/processing-results", item_id=item_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "job_type": job_type,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    job_item_get_processing_results_params.JobItemGetProcessingResultsParams,
                ),
            ),
            cast_to=JobItemGetProcessingResultsResponse,
        )


class JobItemsResourceWithRawResponse:
    def __init__(self, job_items: JobItemsResource) -> None:
        self._job_items = job_items

        self.list = to_raw_response_wrapper(
            job_items.list,
        )
        self.get_processing_results = to_raw_response_wrapper(
            job_items.get_processing_results,
        )


class AsyncJobItemsResourceWithRawResponse:
    def __init__(self, job_items: AsyncJobItemsResource) -> None:
        self._job_items = job_items

        self.list = async_to_raw_response_wrapper(
            job_items.list,
        )
        self.get_processing_results = async_to_raw_response_wrapper(
            job_items.get_processing_results,
        )


class JobItemsResourceWithStreamingResponse:
    def __init__(self, job_items: JobItemsResource) -> None:
        self._job_items = job_items

        self.list = to_streamed_response_wrapper(
            job_items.list,
        )
        self.get_processing_results = to_streamed_response_wrapper(
            job_items.get_processing_results,
        )


class AsyncJobItemsResourceWithStreamingResponse:
    def __init__(self, job_items: AsyncJobItemsResource) -> None:
        self._job_items = job_items

        self.list = async_to_streamed_response_wrapper(
            job_items.list,
        )
        self.get_processing_results = async_to_streamed_response_wrapper(
            job_items.get_processing_results,
        )
