# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import job_data_point_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform
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
from ..types.job_data_point import JobDataPoint

__all__ = ["JobDataPointsResource", "AsyncJobDataPointsResource"]


class JobDataPointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobDataPointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return JobDataPointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobDataPointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return JobDataPointsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        job_type: Literal["classify", "extract", "parse"],
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        hours: int | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[JobDataPoint]:
        """
        Returns paginated job data points for the current project.

        Args:
          job_type: Job type to query.

          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          hours: Hours of history to include.

          page_size: Number of items per page.

          page_token: Cursor token for the next page.

          status: Filter by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/job-data-points",
            page=SyncPaginatedCursor[JobDataPoint],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "job_type": job_type,
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "hours": hours,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    job_data_point_list_params.JobDataPointListParams,
                ),
            ),
            model=JobDataPoint,
        )


class AsyncJobDataPointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobDataPointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncJobDataPointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobDataPointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncJobDataPointsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        job_type: Literal["classify", "extract", "parse"],
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        hours: int | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[JobDataPoint, AsyncPaginatedCursor[JobDataPoint]]:
        """
        Returns paginated job data points for the current project.

        Args:
          job_type: Job type to query.

          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          hours: Hours of history to include.

          page_size: Number of items per page.

          page_token: Cursor token for the next page.

          status: Filter by status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/job-data-points",
            page=AsyncPaginatedCursor[JobDataPoint],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "job_type": job_type,
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "hours": hours,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    job_data_point_list_params.JobDataPointListParams,
                ),
            ),
            model=JobDataPoint,
        )


class JobDataPointsResourceWithRawResponse:
    def __init__(self, job_data_points: JobDataPointsResource) -> None:
        self._job_data_points = job_data_points

        self.list = to_raw_response_wrapper(
            job_data_points.list,
        )


class AsyncJobDataPointsResourceWithRawResponse:
    def __init__(self, job_data_points: AsyncJobDataPointsResource) -> None:
        self._job_data_points = job_data_points

        self.list = async_to_raw_response_wrapper(
            job_data_points.list,
        )


class JobDataPointsResourceWithStreamingResponse:
    def __init__(self, job_data_points: JobDataPointsResource) -> None:
        self._job_data_points = job_data_points

        self.list = to_streamed_response_wrapper(
            job_data_points.list,
        )


class AsyncJobDataPointsResourceWithStreamingResponse:
    def __init__(self, job_data_points: AsyncJobDataPointsResource) -> None:
        self._job_data_points = job_data_points

        self.list = async_to_streamed_response_wrapper(
            job_data_points.list,
        )
