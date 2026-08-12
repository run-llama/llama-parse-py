# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import split_get_params, split_list_params, split_cancel_params, split_create_params, split_delete_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.split_get_response import SplitGetResponse
from ..types.split_list_response import SplitListResponse
from ..types.split_cancel_response import SplitCancelResponse
from ..types.split_create_response import SplitCreateResponse

__all__ = ["SplitResource", "AsyncSplitResource"]


class SplitResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SplitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return SplitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SplitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return SplitResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file_input: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[split_create_params.Configuration] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        transaction_id: Optional[str] | Omit = omit,
        webhook_configuration_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_configurations: Optional[Iterable[split_create_params.WebhookConfiguration]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitCreateResponse:
        """
        Create a document split job.

        Args:
          file_input: File ID or parse job ID

          configuration: Split configuration with categories and splitting strategy.

          configuration_id: Saved configuration ID

          transaction_id: Idempotency key scoped to the project. Reusing a key returns the original job;
              the new request body is ignored.

          webhook_configuration_ids: IDs of saved webhook configurations to notify for this job.

          webhook_configurations: Outbound webhook endpoints to notify on job status changes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/split/jobs",
            body=maybe_transform(
                {
                    "file_input": file_input,
                    "configuration": configuration,
                    "configuration_id": configuration_id,
                    "transaction_id": transaction_id,
                    "webhook_configuration_ids": webhook_configuration_ids,
                    "webhook_configurations": webhook_configurations,
                },
                split_create_params.SplitCreateParams,
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
                    split_create_params.SplitCreateParams,
                ),
            ),
            cast_to=SplitCreateResponse,
        )

    def list(
        self,
        *,
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["cancelled", "completed", "failed", "pending", "processing"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[SplitListResponse]:
        """
        List document split jobs.

        Args:
          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          job_ids: Filter by specific job IDs

          status: Filter by job status (pending, processing, completed, failed, cancelled)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/split/jobs",
            page=SyncPaginatedCursor[SplitListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    split_list_params.SplitListParams,
                ),
            ),
            model=SplitListResponse,
        )

    def delete(
        self,
        split_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a split job and its results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")
        return self._delete(
            path_template("/api/v1/split/jobs/{split_job_id}", split_job_id=split_job_id),
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
                    split_delete_params.SplitDeleteParams,
                ),
            ),
            cast_to=object,
        )

    def cancel(
        self,
        split_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitCancelResponse:
        """
        Cancel a running split job.

        Requests cancellation; the job transitions to CANCELLED asynchronously once
        processing stops. Returns the job, which may still be in its current
        non-terminal state. Jobs already in a terminal state (COMPLETED, FAILED,
        CANCELLED) cannot be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")
        return self._post(
            path_template("/api/v1/split/jobs/{split_job_id}/cancel", split_job_id=split_job_id),
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
                    split_cancel_params.SplitCancelParams,
                ),
            ),
            cast_to=SplitCancelResponse,
        )

    def get(
        self,
        split_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitGetResponse:
        """
        Get a document split job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")
        return self._get(
            path_template("/api/v1/split/jobs/{split_job_id}", split_job_id=split_job_id),
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
                    split_get_params.SplitGetParams,
                ),
            ),
            cast_to=SplitGetResponse,
        )


class AsyncSplitResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSplitResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSplitResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSplitResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncSplitResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file_input: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[split_create_params.Configuration] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        transaction_id: Optional[str] | Omit = omit,
        webhook_configuration_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_configurations: Optional[Iterable[split_create_params.WebhookConfiguration]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitCreateResponse:
        """
        Create a document split job.

        Args:
          file_input: File ID or parse job ID

          configuration: Split configuration with categories and splitting strategy.

          configuration_id: Saved configuration ID

          transaction_id: Idempotency key scoped to the project. Reusing a key returns the original job;
              the new request body is ignored.

          webhook_configuration_ids: IDs of saved webhook configurations to notify for this job.

          webhook_configurations: Outbound webhook endpoints to notify on job status changes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/split/jobs",
            body=await async_maybe_transform(
                {
                    "file_input": file_input,
                    "configuration": configuration,
                    "configuration_id": configuration_id,
                    "transaction_id": transaction_id,
                    "webhook_configuration_ids": webhook_configuration_ids,
                    "webhook_configurations": webhook_configurations,
                },
                split_create_params.SplitCreateParams,
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
                    split_create_params.SplitCreateParams,
                ),
            ),
            cast_to=SplitCreateResponse,
        )

    def list(
        self,
        *,
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["cancelled", "completed", "failed", "pending", "processing"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SplitListResponse, AsyncPaginatedCursor[SplitListResponse]]:
        """
        List document split jobs.

        Args:
          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          job_ids: Filter by specific job IDs

          status: Filter by job status (pending, processing, completed, failed, cancelled)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/split/jobs",
            page=AsyncPaginatedCursor[SplitListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    split_list_params.SplitListParams,
                ),
            ),
            model=SplitListResponse,
        )

    async def delete(
        self,
        split_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Delete a split job and its results.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")
        return await self._delete(
            path_template("/api/v1/split/jobs/{split_job_id}", split_job_id=split_job_id),
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
                    split_delete_params.SplitDeleteParams,
                ),
            ),
            cast_to=object,
        )

    async def cancel(
        self,
        split_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitCancelResponse:
        """
        Cancel a running split job.

        Requests cancellation; the job transitions to CANCELLED asynchronously once
        processing stops. Returns the job, which may still be in its current
        non-terminal state. Jobs already in a terminal state (COMPLETED, FAILED,
        CANCELLED) cannot be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")
        return await self._post(
            path_template("/api/v1/split/jobs/{split_job_id}/cancel", split_job_id=split_job_id),
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
                    split_cancel_params.SplitCancelParams,
                ),
            ),
            cast_to=SplitCancelResponse,
        )

    async def get(
        self,
        split_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SplitGetResponse:
        """
        Get a document split job.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")
        return await self._get(
            path_template("/api/v1/split/jobs/{split_job_id}", split_job_id=split_job_id),
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
                    split_get_params.SplitGetParams,
                ),
            ),
            cast_to=SplitGetResponse,
        )


class SplitResourceWithRawResponse:
    def __init__(self, split: SplitResource) -> None:
        self._split = split

        self.create = to_raw_response_wrapper(
            split.create,
        )
        self.list = to_raw_response_wrapper(
            split.list,
        )
        self.delete = to_raw_response_wrapper(
            split.delete,
        )
        self.cancel = to_raw_response_wrapper(
            split.cancel,
        )
        self.get = to_raw_response_wrapper(
            split.get,
        )


class AsyncSplitResourceWithRawResponse:
    def __init__(self, split: AsyncSplitResource) -> None:
        self._split = split

        self.create = async_to_raw_response_wrapper(
            split.create,
        )
        self.list = async_to_raw_response_wrapper(
            split.list,
        )
        self.delete = async_to_raw_response_wrapper(
            split.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            split.cancel,
        )
        self.get = async_to_raw_response_wrapper(
            split.get,
        )


class SplitResourceWithStreamingResponse:
    def __init__(self, split: SplitResource) -> None:
        self._split = split

        self.create = to_streamed_response_wrapper(
            split.create,
        )
        self.list = to_streamed_response_wrapper(
            split.list,
        )
        self.delete = to_streamed_response_wrapper(
            split.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            split.cancel,
        )
        self.get = to_streamed_response_wrapper(
            split.get,
        )


class AsyncSplitResourceWithStreamingResponse:
    def __init__(self, split: AsyncSplitResource) -> None:
        self._split = split

        self.create = async_to_streamed_response_wrapper(
            split.create,
        )
        self.list = async_to_streamed_response_wrapper(
            split.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            split.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            split.cancel,
        )
        self.get = async_to_streamed_response_wrapper(
            split.get,
        )
