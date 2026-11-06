# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from .review import (
    ReviewResource,
    AsyncReviewResource,
    ReviewResourceWithRawResponse,
    AsyncReviewResourceWithRawResponse,
    ReviewResourceWithStreamingResponse,
    AsyncReviewResourceWithStreamingResponse,
)
from ...types import (
    extract_get_params,
    extract_list_params,
    extract_cancel_params,
    extract_create_params,
    extract_delete_params,
    extract_generate_schema_params,
    extract_validate_schema_params,
)
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
from ..._base_client import AsyncPaginator, make_request_options
from ...types.extract_v2_job import ExtractV2Job
from ...types.configuration_create import ConfigurationCreate
from ...types.extract_configuration_param import ExtractConfigurationParam
from ...types.extract_v2_schema_validate_response import ExtractV2SchemaValidateResponse

__all__ = ["ExtractResource", "AsyncExtractResource"]


class ExtractResource(SyncAPIResource):
    @cached_property
    def review(self) -> ReviewResource:
        return ReviewResource(self._client)

    @cached_property
    def with_raw_response(self) -> ExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return ExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return ExtractResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        file_input: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[ExtractConfigurationParam] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        webhook_configuration_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_configurations: Optional[Iterable[extract_create_params.WebhookConfiguration]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractV2Job:
        """
        Create an extraction job.

        Extracts structured data from a document using either a saved configuration or
        an inline JSON Schema.

        ## Input

        Provide exactly one of:

        - `configuration_id` — reference a saved extraction config
        - `configuration` — inline configuration with a `data_schema`

        ## Document input

        Set `file_input` to a file ID (`dfl-...`) or a completed parse job ID
        (`pjb-...`).

        The job runs asynchronously. Poll `GET /extract/{job_id}` or register a webhook
        to monitor completion.

        Args:
          file_input: File ID or parse job ID to extract from

          configuration: Extract configuration combining parse and extract settings.

          configuration_id: Saved configuration ID

          webhook_configuration_ids: IDs of saved webhook configurations to notify for this job.

          webhook_configurations: Outbound webhook endpoints to notify on job status changes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/extract",
            body=maybe_transform(
                {
                    "file_input": file_input,
                    "configuration": configuration,
                    "configuration_id": configuration_id,
                    "webhook_configuration_ids": webhook_configuration_ids,
                    "webhook_configurations": webhook_configurations,
                },
                extract_create_params.ExtractCreateParams,
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
                    extract_create_params.ExtractCreateParams,
                ),
            ),
            cast_to=ExtractV2Job,
        )

    def list(
        self,
        *,
        configuration_id: Optional[str] | Omit = omit,
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        document_input_type: Optional[str] | Omit = omit,
        document_input_value: Optional[str] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        file_input: Optional[str] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        review_status: Optional[Literal["approved", "none", "pending", "rejected"]] | Omit = omit,
        status: Optional[Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING", "THROTTLED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[ExtractV2Job]:
        """
        List extraction jobs with optional filtering and pagination.

        Filter by `configuration_id`, `status`, `file_input`, `review_status`, or
        creation date range. Results are returned newest-first. `review_status=pending`
        lists completed jobs waiting for review, unless `status` names another. A review
        stays pending when its job fails or is cancelled, so pass that `status` to list
        those. Use `expand=configuration` to include the full configuration used, and
        `expand=extract_metadata` for per-field metadata.

        Args:
          configuration_id: Filter by configuration ID

          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          document_input_type: Filter by document input type (file_id or parse_job_id)

          document_input_value: Deprecated: use file_input instead

          expand: Additional fields to include: configuration, extract_metadata

          file_input: Filter by file input value

          job_ids: Filter by specific job IDs

          page_size: Number of items per page

          page_token: Token for pagination

          review_status: Filter by review status; none is a job without a review

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/extract",
            page=SyncPaginatedCursor[ExtractV2Job],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "configuration_id": configuration_id,
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "document_input_type": document_input_type,
                        "document_input_value": document_input_value,
                        "expand": expand,
                        "file_input": file_input,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "review_status": review_status,
                        "status": status,
                    },
                    extract_list_params.ExtractListParams,
                ),
            ),
            model=ExtractV2Job,
        )

    def delete(
        self,
        job_id: str,
        *,
        force: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Delete an extraction job and its results.

        A non-terminal job is refused; cancel
        it first, or pass force=true to delete a job whose workflow is gone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._delete(
            path_template("/api/v2/extract/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "force": force,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    extract_delete_params.ExtractDeleteParams,
                ),
            ),
            cast_to=object,
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
    ) -> ExtractV2Job:
        """
        Cancel a running extraction job.

        Stops processing and marks the job as CANCELLED. Returns the updated job. Jobs
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
            path_template("/api/v2/extract/{job_id}/cancel", job_id=job_id),
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
                    extract_cancel_params.ExtractCancelParams,
                ),
            ),
            cast_to=ExtractV2Job,
        )

    def generate_schema(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_schema: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationCreate:
        """
        Generate a JSON schema and return a product configuration request.

        Args:
          data_schema: Optional schema to validate, refine, or extend

          file_id: Optional file ID to analyze for schema generation

          name: Name for the generated configuration (auto-generated if omitted)

          prompt: Natural language description of the data structure to extract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/extract/schema/generate",
            body=maybe_transform(
                {
                    "data_schema": data_schema,
                    "file_id": file_id,
                    "name": name,
                    "prompt": prompt,
                },
                extract_generate_schema_params.ExtractGenerateSchemaParams,
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
                    extract_generate_schema_params.ExtractGenerateSchemaParams,
                ),
            ),
            cast_to=ConfigurationCreate,
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
    ) -> ExtractV2Job:
        """
        Get a single extraction job by ID.

        Returns the job status and results when complete. Use `expand=configuration` to
        include the full configuration used, `expand=extract_metadata` for per-field
        metadata, and `expand=usage` for credits billed against the job.

        Args:
          expand: Additional fields to include: configuration, extract_metadata, usage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template("/api/v2/extract/{job_id}", job_id=job_id),
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
                    extract_get_params.ExtractGetParams,
                ),
            ),
            cast_to=ExtractV2Job,
        )

    def validate_schema(
        self,
        *,
        data_schema: Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractV2SchemaValidateResponse:
        """
        Validate a JSON schema for extraction.

        Args:
          data_schema: JSON Schema to validate for use with extract jobs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v2/extract/schema/validation",
            body=maybe_transform(
                {"data_schema": data_schema}, extract_validate_schema_params.ExtractValidateSchemaParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractV2SchemaValidateResponse,
        )


class AsyncExtractResource(AsyncAPIResource):
    @cached_property
    def review(self) -> AsyncReviewResource:
        return AsyncReviewResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncExtractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncExtractResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        file_input: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[ExtractConfigurationParam] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        webhook_configuration_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_configurations: Optional[Iterable[extract_create_params.WebhookConfiguration]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractV2Job:
        """
        Create an extraction job.

        Extracts structured data from a document using either a saved configuration or
        an inline JSON Schema.

        ## Input

        Provide exactly one of:

        - `configuration_id` — reference a saved extraction config
        - `configuration` — inline configuration with a `data_schema`

        ## Document input

        Set `file_input` to a file ID (`dfl-...`) or a completed parse job ID
        (`pjb-...`).

        The job runs asynchronously. Poll `GET /extract/{job_id}` or register a webhook
        to monitor completion.

        Args:
          file_input: File ID or parse job ID to extract from

          configuration: Extract configuration combining parse and extract settings.

          configuration_id: Saved configuration ID

          webhook_configuration_ids: IDs of saved webhook configurations to notify for this job.

          webhook_configurations: Outbound webhook endpoints to notify on job status changes

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/extract",
            body=await async_maybe_transform(
                {
                    "file_input": file_input,
                    "configuration": configuration,
                    "configuration_id": configuration_id,
                    "webhook_configuration_ids": webhook_configuration_ids,
                    "webhook_configurations": webhook_configurations,
                },
                extract_create_params.ExtractCreateParams,
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
                    extract_create_params.ExtractCreateParams,
                ),
            ),
            cast_to=ExtractV2Job,
        )

    def list(
        self,
        *,
        configuration_id: Optional[str] | Omit = omit,
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        document_input_type: Optional[str] | Omit = omit,
        document_input_value: Optional[str] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        file_input: Optional[str] | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        review_status: Optional[Literal["approved", "none", "pending", "rejected"]] | Omit = omit,
        status: Optional[Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING", "THROTTLED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExtractV2Job, AsyncPaginatedCursor[ExtractV2Job]]:
        """
        List extraction jobs with optional filtering and pagination.

        Filter by `configuration_id`, `status`, `file_input`, `review_status`, or
        creation date range. Results are returned newest-first. `review_status=pending`
        lists completed jobs waiting for review, unless `status` names another. A review
        stays pending when its job fails or is cancelled, so pass that `status` to list
        those. Use `expand=configuration` to include the full configuration used, and
        `expand=extract_metadata` for per-field metadata.

        Args:
          configuration_id: Filter by configuration ID

          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          document_input_type: Filter by document input type (file_id or parse_job_id)

          document_input_value: Deprecated: use file_input instead

          expand: Additional fields to include: configuration, extract_metadata

          file_input: Filter by file input value

          job_ids: Filter by specific job IDs

          page_size: Number of items per page

          page_token: Token for pagination

          review_status: Filter by review status; none is a job without a review

          status: Filter by status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/extract",
            page=AsyncPaginatedCursor[ExtractV2Job],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "configuration_id": configuration_id,
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "document_input_type": document_input_type,
                        "document_input_value": document_input_value,
                        "expand": expand,
                        "file_input": file_input,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "review_status": review_status,
                        "status": status,
                    },
                    extract_list_params.ExtractListParams,
                ),
            ),
            model=ExtractV2Job,
        )

    async def delete(
        self,
        job_id: str,
        *,
        force: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """Delete an extraction job and its results.

        A non-terminal job is refused; cancel
        it first, or pass force=true to delete a job whose workflow is gone.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._delete(
            path_template("/api/v2/extract/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "force": force,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    extract_delete_params.ExtractDeleteParams,
                ),
            ),
            cast_to=object,
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
    ) -> ExtractV2Job:
        """
        Cancel a running extraction job.

        Stops processing and marks the job as CANCELLED. Returns the updated job. Jobs
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
            path_template("/api/v2/extract/{job_id}/cancel", job_id=job_id),
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
                    extract_cancel_params.ExtractCancelParams,
                ),
            ),
            cast_to=ExtractV2Job,
        )

    async def generate_schema(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        data_schema: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
        | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        prompt: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationCreate:
        """
        Generate a JSON schema and return a product configuration request.

        Args:
          data_schema: Optional schema to validate, refine, or extend

          file_id: Optional file ID to analyze for schema generation

          name: Name for the generated configuration (auto-generated if omitted)

          prompt: Natural language description of the data structure to extract

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/extract/schema/generate",
            body=await async_maybe_transform(
                {
                    "data_schema": data_schema,
                    "file_id": file_id,
                    "name": name,
                    "prompt": prompt,
                },
                extract_generate_schema_params.ExtractGenerateSchemaParams,
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
                    extract_generate_schema_params.ExtractGenerateSchemaParams,
                ),
            ),
            cast_to=ConfigurationCreate,
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
    ) -> ExtractV2Job:
        """
        Get a single extraction job by ID.

        Returns the job status and results when complete. Use `expand=configuration` to
        include the full configuration used, `expand=extract_metadata` for per-field
        metadata, and `expand=usage` for credits billed against the job.

        Args:
          expand: Additional fields to include: configuration, extract_metadata, usage

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template("/api/v2/extract/{job_id}", job_id=job_id),
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
                    extract_get_params.ExtractGetParams,
                ),
            ),
            cast_to=ExtractV2Job,
        )

    async def validate_schema(
        self,
        *,
        data_schema: Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ExtractV2SchemaValidateResponse:
        """
        Validate a JSON schema for extraction.

        Args:
          data_schema: JSON Schema to validate for use with extract jobs

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v2/extract/schema/validation",
            body=await async_maybe_transform(
                {"data_schema": data_schema}, extract_validate_schema_params.ExtractValidateSchemaParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExtractV2SchemaValidateResponse,
        )


class ExtractResourceWithRawResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create = to_raw_response_wrapper(
            extract.create,
        )
        self.list = to_raw_response_wrapper(
            extract.list,
        )
        self.delete = to_raw_response_wrapper(
            extract.delete,
        )
        self.cancel = to_raw_response_wrapper(
            extract.cancel,
        )
        self.generate_schema = to_raw_response_wrapper(
            extract.generate_schema,
        )
        self.get = to_raw_response_wrapper(
            extract.get,
        )
        self.validate_schema = to_raw_response_wrapper(
            extract.validate_schema,
        )

    @cached_property
    def review(self) -> ReviewResourceWithRawResponse:
        return ReviewResourceWithRawResponse(self._extract.review)


class AsyncExtractResourceWithRawResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create = async_to_raw_response_wrapper(
            extract.create,
        )
        self.list = async_to_raw_response_wrapper(
            extract.list,
        )
        self.delete = async_to_raw_response_wrapper(
            extract.delete,
        )
        self.cancel = async_to_raw_response_wrapper(
            extract.cancel,
        )
        self.generate_schema = async_to_raw_response_wrapper(
            extract.generate_schema,
        )
        self.get = async_to_raw_response_wrapper(
            extract.get,
        )
        self.validate_schema = async_to_raw_response_wrapper(
            extract.validate_schema,
        )

    @cached_property
    def review(self) -> AsyncReviewResourceWithRawResponse:
        return AsyncReviewResourceWithRawResponse(self._extract.review)


class ExtractResourceWithStreamingResponse:
    def __init__(self, extract: ExtractResource) -> None:
        self._extract = extract

        self.create = to_streamed_response_wrapper(
            extract.create,
        )
        self.list = to_streamed_response_wrapper(
            extract.list,
        )
        self.delete = to_streamed_response_wrapper(
            extract.delete,
        )
        self.cancel = to_streamed_response_wrapper(
            extract.cancel,
        )
        self.generate_schema = to_streamed_response_wrapper(
            extract.generate_schema,
        )
        self.get = to_streamed_response_wrapper(
            extract.get,
        )
        self.validate_schema = to_streamed_response_wrapper(
            extract.validate_schema,
        )

    @cached_property
    def review(self) -> ReviewResourceWithStreamingResponse:
        return ReviewResourceWithStreamingResponse(self._extract.review)


class AsyncExtractResourceWithStreamingResponse:
    def __init__(self, extract: AsyncExtractResource) -> None:
        self._extract = extract

        self.create = async_to_streamed_response_wrapper(
            extract.create,
        )
        self.list = async_to_streamed_response_wrapper(
            extract.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            extract.delete,
        )
        self.cancel = async_to_streamed_response_wrapper(
            extract.cancel,
        )
        self.generate_schema = async_to_streamed_response_wrapper(
            extract.generate_schema,
        )
        self.get = async_to_streamed_response_wrapper(
            extract.get,
        )
        self.validate_schema = async_to_streamed_response_wrapper(
            extract.validate_schema,
        )

    @cached_property
    def review(self) -> AsyncReviewResourceWithStreamingResponse:
        return AsyncReviewResourceWithStreamingResponse(self._extract.review)
