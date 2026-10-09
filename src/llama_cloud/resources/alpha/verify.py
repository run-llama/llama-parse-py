# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

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
from ...pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from ...types.alpha import (
    verify_get_params,
    verify_list_params,
    verify_cancel_params,
    verify_create_params,
    verify_get_details_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.alpha.verify_get_response import VerifyGetResponse
from ...types.alpha.verify_list_response import VerifyListResponse
from ...types.alpha.verify_cancel_response import VerifyCancelResponse
from ...types.alpha.verify_create_response import VerifyCreateResponse
from ...types.alpha.verify_get_details_response import VerifyGetDetailsResponse

__all__ = ["VerifyResource", "AsyncVerifyResource"]


class VerifyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VerifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return VerifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VerifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return VerifyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[verify_create_params.Configuration] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        file_input: Optional[str] | Omit = omit,
        transaction_id: Optional[str] | Omit = omit,
        webhook_configuration_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_configurations: Optional[Iterable[verify_create_params.WebhookConfiguration]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyCreateResponse:
        """
        Create a Verify job.

        Analyzes a document for signs of doctoring (splicing, copy-move, AI generation,
        metadata tampering, ...). Set `file_input` to a file ID (`dfl-...`). Optionally
        provide a `configuration` object to control the semantic agent.

        The job runs asynchronously. Poll `GET /verify/{job_id}` with `expand=result` to
        check status and retrieve results.

        Args:
          configuration: Configuration for a Verify job.

          file_id: Deprecated: use file_input instead

          file_input: File ID of the document to analyze

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
            "/api/alpha/verify",
            body=maybe_transform(
                {
                    "configuration": configuration,
                    "file_id": file_id,
                    "file_input": file_input,
                    "transaction_id": transaction_id,
                    "webhook_configuration_ids": webhook_configuration_ids,
                    "webhook_configurations": webhook_configurations,
                },
                verify_create_params.VerifyCreateParams,
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
                    verify_create_params.VerifyCreateParams,
                ),
            ),
            cast_to=VerifyCreateResponse,
        )

    def list(
        self,
        *,
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[VerifyListResponse]:
        """
        List Verify jobs with optional filtering and pagination.

        Filter by `status`, specific `job_ids`, or creation date range.

        Args:
          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          expand: Optional fields to include (e.g. `result`).

          job_ids: Filter by specific job IDs

          page_size: Number of items per page

          page_token: Token for pagination

          status: Filter by job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/alpha/verify",
            page=SyncPaginatedCursor[VerifyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "expand": expand,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    verify_list_params.VerifyListParams,
                ),
            ),
            model=VerifyListResponse,
        )

    def cancel(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyCancelResponse:
        """Cancel a running Verify job.

        Stops processing and marks the job as CANCELLED.

        Returns the updated job. Jobs
        already in a terminal state (COMPLETED, FAILED, CANCELLED) cannot be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._post(
            path_template("/api/alpha/verify/{job_id}/cancel", job_id=job_id),
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
                    verify_cancel_params.VerifyCancelParams,
                ),
            ),
            cast_to=VerifyCancelResponse,
        )

    def get(
        self,
        job_id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyGetResponse:
        """Get a Verify job by ID.

        Returns the job status and configuration.

        Pass `expand=result` to include the
        Verify result (overall score, verdict, confidence, composite scores, and suspect
        regions) when the job is complete.

        Raw per-signal detail is available via `GET /verify/{job_id}/details`.

        Args:
          expand: Optional fields to include (e.g. `result`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template("/api/alpha/verify/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    verify_get_params.VerifyGetParams,
                ),
            ),
            cast_to=VerifyGetResponse,
        )

    def get_details(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyGetDetailsResponse:
        """
        Get the raw per-signal detail for a completed Verify job.

        Forensic drill-down behind the simplified result: the full evidence list,
        per-family sub-scores, raw localized regions, and per-page forensic heatmap
        overlays (presigned image URLs).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template("/api/alpha/verify/{job_id}/details", job_id=job_id),
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
                    verify_get_details_params.VerifyGetDetailsParams,
                ),
            ),
            cast_to=VerifyGetDetailsResponse,
        )


class AsyncVerifyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVerifyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncVerifyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVerifyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncVerifyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[verify_create_params.Configuration] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        file_input: Optional[str] | Omit = omit,
        transaction_id: Optional[str] | Omit = omit,
        webhook_configuration_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_configurations: Optional[Iterable[verify_create_params.WebhookConfiguration]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyCreateResponse:
        """
        Create a Verify job.

        Analyzes a document for signs of doctoring (splicing, copy-move, AI generation,
        metadata tampering, ...). Set `file_input` to a file ID (`dfl-...`). Optionally
        provide a `configuration` object to control the semantic agent.

        The job runs asynchronously. Poll `GET /verify/{job_id}` with `expand=result` to
        check status and retrieve results.

        Args:
          configuration: Configuration for a Verify job.

          file_id: Deprecated: use file_input instead

          file_input: File ID of the document to analyze

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
            "/api/alpha/verify",
            body=await async_maybe_transform(
                {
                    "configuration": configuration,
                    "file_id": file_id,
                    "file_input": file_input,
                    "transaction_id": transaction_id,
                    "webhook_configuration_ids": webhook_configuration_ids,
                    "webhook_configurations": webhook_configurations,
                },
                verify_create_params.VerifyCreateParams,
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
                    verify_create_params.VerifyCreateParams,
                ),
            ),
            cast_to=VerifyCreateResponse,
        )

    def list(
        self,
        *,
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[VerifyListResponse, AsyncPaginatedCursor[VerifyListResponse]]:
        """
        List Verify jobs with optional filtering and pagination.

        Filter by `status`, specific `job_ids`, or creation date range.

        Args:
          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          expand: Optional fields to include (e.g. `result`).

          job_ids: Filter by specific job IDs

          page_size: Number of items per page

          page_token: Token for pagination

          status: Filter by job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/alpha/verify",
            page=AsyncPaginatedCursor[VerifyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "expand": expand,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    verify_list_params.VerifyListParams,
                ),
            ),
            model=VerifyListResponse,
        )

    async def cancel(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyCancelResponse:
        """Cancel a running Verify job.

        Stops processing and marks the job as CANCELLED.

        Returns the updated job. Jobs
        already in a terminal state (COMPLETED, FAILED, CANCELLED) cannot be cancelled.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._post(
            path_template("/api/alpha/verify/{job_id}/cancel", job_id=job_id),
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
                    verify_cancel_params.VerifyCancelParams,
                ),
            ),
            cast_to=VerifyCancelResponse,
        )

    async def get(
        self,
        job_id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyGetResponse:
        """Get a Verify job by ID.

        Returns the job status and configuration.

        Pass `expand=result` to include the
        Verify result (overall score, verdict, confidence, composite scores, and suspect
        regions) when the job is complete.

        Raw per-signal detail is available via `GET /verify/{job_id}/details`.

        Args:
          expand: Optional fields to include (e.g. `result`).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template("/api/alpha/verify/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expand": expand,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    verify_get_params.VerifyGetParams,
                ),
            ),
            cast_to=VerifyGetResponse,
        )

    async def get_details(
        self,
        job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VerifyGetDetailsResponse:
        """
        Get the raw per-signal detail for a completed Verify job.

        Forensic drill-down behind the simplified result: the full evidence list,
        per-family sub-scores, raw localized regions, and per-page forensic heatmap
        overlays (presigned image URLs).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template("/api/alpha/verify/{job_id}/details", job_id=job_id),
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
                    verify_get_details_params.VerifyGetDetailsParams,
                ),
            ),
            cast_to=VerifyGetDetailsResponse,
        )


class VerifyResourceWithRawResponse:
    def __init__(self, verify: VerifyResource) -> None:
        self._verify = verify

        self.create = to_raw_response_wrapper(
            verify.create,
        )
        self.list = to_raw_response_wrapper(
            verify.list,
        )
        self.cancel = to_raw_response_wrapper(
            verify.cancel,
        )
        self.get = to_raw_response_wrapper(
            verify.get,
        )
        self.get_details = to_raw_response_wrapper(
            verify.get_details,
        )


class AsyncVerifyResourceWithRawResponse:
    def __init__(self, verify: AsyncVerifyResource) -> None:
        self._verify = verify

        self.create = async_to_raw_response_wrapper(
            verify.create,
        )
        self.list = async_to_raw_response_wrapper(
            verify.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            verify.cancel,
        )
        self.get = async_to_raw_response_wrapper(
            verify.get,
        )
        self.get_details = async_to_raw_response_wrapper(
            verify.get_details,
        )


class VerifyResourceWithStreamingResponse:
    def __init__(self, verify: VerifyResource) -> None:
        self._verify = verify

        self.create = to_streamed_response_wrapper(
            verify.create,
        )
        self.list = to_streamed_response_wrapper(
            verify.list,
        )
        self.cancel = to_streamed_response_wrapper(
            verify.cancel,
        )
        self.get = to_streamed_response_wrapper(
            verify.get,
        )
        self.get_details = to_streamed_response_wrapper(
            verify.get_details,
        )


class AsyncVerifyResourceWithStreamingResponse:
    def __init__(self, verify: AsyncVerifyResource) -> None:
        self._verify = verify

        self.create = async_to_streamed_response_wrapper(
            verify.create,
        )
        self.list = async_to_streamed_response_wrapper(
            verify.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            verify.cancel,
        )
        self.get = async_to_streamed_response_wrapper(
            verify.get,
        )
        self.get_details = async_to_streamed_response_wrapper(
            verify.get_details,
        )
