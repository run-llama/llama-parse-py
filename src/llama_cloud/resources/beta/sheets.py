# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ...types import StatusEnum
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._polling import (
    DEFAULT_TIMEOUT,
    BackoffStrategy,
    poll_until_complete,
    poll_until_complete_async,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from ...types.beta import (
    sheet_get_params,
    sheet_list_params,
    sheet_create_params,
    sheet_delete_job_params,
    sheet_get_result_table_params,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.status_enum import StatusEnum
from ...types.presigned_url import PresignedURL
from ...types.beta.sheets_job import SheetsJob
from ...types.beta.sheets_parsing_config_param import SheetsParsingConfigParam

__all__ = ["SheetsResource", "AsyncSheetsResource"]


class SheetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SheetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return SheetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SheetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return SheetsResourceWithStreamingResponse(self)

    def parse(
        self,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: SheetsParsingConfigParam | Omit = omit,
        # Polling parameters
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SheetsJob:
        """
        Create a spreadsheet parsing job and wait for it to complete, returning the job with results.

        This is a convenience method that combines create() and wait_for_completion()
        into a single call for the most common end-to-end workflow.

        Args:
            file_id: The ID of the file to parse

            organization_id: Optional organization ID

            project_id: Optional project ID

            config: Configuration for the parsing job

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed SheetsJob with results included

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # One-shot: create job, wait for completion, and get results
            job = client.beta.sheets.parse(
                file_id="file_123",
                verbose=True,
            )

            # Results are ready to use immediately
            for region in job.extracted_regions:
                print(f"Region {region.id}: {region.type}")
            ```
        """
        # Create the job
        job = self.create(
            file_id=file_id,
            organization_id=organization_id,
            project_id=project_id,
            config=config,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion and return results
        return self.wait_for_completion(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

    def wait_for_completion(
        self,
        spreadsheet_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SheetsJob:
        """
        Wait for a spreadsheet parsing job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Args:
            spreadsheet_job_id: The ID of the spreadsheet job to wait for

            organization_id: Optional organization ID

            project_id: Optional project ID

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed SheetsJob with results included

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # Create a spreadsheet parsing job
            job = client.beta.sheets.create(file_id="file_123")

            # Wait for it to complete
            completed_job = client.beta.sheets.wait_for_completion(job.id, verbose=True)

            # Access the results
            for region in completed_job.extracted_regions:
                print(f"Region {region.id}: {region.type}")
            ```
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")

        def get_status() -> SheetsJob:
            return self.get(
                spreadsheet_job_id,
                include_results=True,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: SheetsJob) -> bool:
            return job.status in ("SUCCESS", "PARTIAL_SUCCESS")

        def is_error(job: SheetsJob) -> bool:
            return job.status in ("ERROR", "CANCELLED")

        def get_error_message(job: SheetsJob) -> str:
            error_parts = [f"Job {spreadsheet_job_id} failed with status: {job.status}"]
            if job.errors:
                error_parts.append(f"Errors: {job.errors}")
            return " | ".join(error_parts)

        return poll_until_complete(
            get_status_fn=get_status,
            is_complete_fn=is_complete,
            is_error_fn=is_error,
            get_error_message_fn=get_error_message,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
        )

    def create(
        self,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: SheetsParsingConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SheetsJob:
        """Create a spreadsheet parsing job.

        Experimental: This endpoint is not yet ready
        for production use and is subject to change at any time.

        Args:
          file_id: The ID of the file to parse

          config: Configuration for the parsing job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/sheets/jobs",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "config": config,
                },
                sheet_create_params.SheetCreateParams,
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
                    sheet_create_params.SheetCreateParams,
                ),
            ),
            cast_to=SheetsJob,
        )

    def list(
        self,
        *,
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        include_results: bool | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[StatusEnum] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[SheetsJob]:
        """List spreadsheet parsing jobs.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          job_ids: Filter by specific job IDs

          status: Filter by job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/sheets/jobs",
            page=SyncPaginatedCursor[SheetsJob],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "include_results": include_results,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    sheet_list_params.SheetListParams,
                ),
            ),
            model=SheetsJob,
        )

    def delete_job(
        self,
        spreadsheet_job_id: str,
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
        """Delete a spreadsheet parsing job and its associated data.

        Experimental: This
        endpoint is not yet ready for production use and is subject to change at any
        time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        return self._delete(
            path_template("/api/v1/beta/sheets/jobs/{spreadsheet_job_id}", spreadsheet_job_id=spreadsheet_job_id),
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
                    sheet_delete_job_params.SheetDeleteJobParams,
                ),
            ),
            cast_to=object,
        )

    def get(
        self,
        spreadsheet_job_id: str,
        *,
        include_results: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SheetsJob:
        """
        Get a spreadsheet parsing job.

        When include_results=True (default), the response will include extracted regions
        and results if the job is complete, eliminating the need for a separate /results
        call.

        Experimental: This endpoint is not yet ready for production use and is subject
        to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        return self._get(
            path_template("/api/v1/beta/sheets/jobs/{spreadsheet_job_id}", spreadsheet_job_id=spreadsheet_job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_results": include_results,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    sheet_get_params.SheetGetParams,
                ),
            ),
            cast_to=SheetsJob,
        )

    def get_result_table(
        self,
        region_type: Literal["table", "extra", "cell_metadata"],
        *,
        spreadsheet_job_id: str,
        region_id: str,
        expires_at_seconds: Optional[int] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresignedURL:
        """Generate a presigned URL to download a specific extracted region.

        Experimental:
        This endpoint is not yet ready for production use and is subject to change at
        any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        if not region_id:
            raise ValueError(f"Expected a non-empty value for `region_id` but received {region_id!r}")
        if not region_type:
            raise ValueError(f"Expected a non-empty value for `region_type` but received {region_type!r}")
        return self._get(
            path_template(
                "/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}",
                spreadsheet_job_id=spreadsheet_job_id,
                region_id=region_id,
                region_type=region_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expires_at_seconds": expires_at_seconds,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    sheet_get_result_table_params.SheetGetResultTableParams,
                ),
            ),
            cast_to=PresignedURL,
        )


class AsyncSheetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSheetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncSheetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSheetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncSheetsResourceWithStreamingResponse(self)

    async def parse(
        self,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: SheetsParsingConfigParam | Omit = omit,
        # Polling parameters
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SheetsJob:
        """
        Create a spreadsheet parsing job and wait for it to complete, returning the job with results.

        This is a convenience method that combines create() and wait_for_completion()
        into a single call for the most common end-to-end workflow.

        Args:
            file_id: The ID of the file to parse

            organization_id: Optional organization ID

            project_id: Optional project ID

            config: Configuration for the parsing job

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed SheetsJob with results included

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            # One-shot: create job, wait for completion, and get results
            job = await client.beta.sheets.parse(
                file_id="file_123",
                verbose=True,
            )

            # Results are ready to use immediately
            for region in job.extracted_regions:
                print(f"Region {region.id}: {region.type}")
            ```
        """
        # Create the job
        job = await self.create(
            file_id=file_id,
            organization_id=organization_id,
            project_id=project_id,
            config=config,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion and return results
        return await self.wait_for_completion(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

    async def wait_for_completion(
        self,
        spreadsheet_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> SheetsJob:
        """
        Wait for a spreadsheet parsing job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Args:
            spreadsheet_job_id: The ID of the spreadsheet job to wait for

            organization_id: Optional organization ID

            project_id: Optional project ID

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed SheetsJob with results included

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            # Create a spreadsheet parsing job
            job = await client.beta.sheets.create(file_id="file_123")

            # Wait for it to complete
            completed_job = await client.beta.sheets.wait_for_completion(job.id, verbose=True)

            # Access the results
            for region in completed_job.extracted_regions:
                print(f"Region {region.id}: {region.type}")
            ```
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")

        async def get_status() -> SheetsJob:
            return await self.get(
                spreadsheet_job_id,
                include_results=True,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: SheetsJob) -> bool:
            return job.status in ("SUCCESS", "PARTIAL_SUCCESS")

        def is_error(job: SheetsJob) -> bool:
            return job.status in ("ERROR", "CANCELLED")

        def get_error_message(job: SheetsJob) -> str:
            error_parts = [f"Job {spreadsheet_job_id} failed with status: {job.status}"]
            if job.errors:
                error_parts.append(f"Errors: {job.errors}")
            return " | ".join(error_parts)

        return await poll_until_complete_async(
            get_status_fn=get_status,
            is_complete_fn=is_complete,
            is_error_fn=is_error,
            get_error_message_fn=get_error_message,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
        )

    async def create(
        self,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        config: SheetsParsingConfigParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SheetsJob:
        """Create a spreadsheet parsing job.

        Experimental: This endpoint is not yet ready
        for production use and is subject to change at any time.

        Args:
          file_id: The ID of the file to parse

          config: Configuration for the parsing job

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/sheets/jobs",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "config": config,
                },
                sheet_create_params.SheetCreateParams,
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
                    sheet_create_params.SheetCreateParams,
                ),
            ),
            cast_to=SheetsJob,
        )

    def list(
        self,
        *,
        created_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        created_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        include_results: bool | Omit = omit,
        job_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        status: Optional[StatusEnum] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[SheetsJob, AsyncPaginatedCursor[SheetsJob]]:
        """List spreadsheet parsing jobs.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          job_ids: Filter by specific job IDs

          status: Filter by job status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/sheets/jobs",
            page=AsyncPaginatedCursor[SheetsJob],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "created_at_on_or_after": created_at_on_or_after,
                        "created_at_on_or_before": created_at_on_or_before,
                        "include_results": include_results,
                        "job_ids": job_ids,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "status": status,
                    },
                    sheet_list_params.SheetListParams,
                ),
            ),
            model=SheetsJob,
        )

    async def delete_job(
        self,
        spreadsheet_job_id: str,
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
        """Delete a spreadsheet parsing job and its associated data.

        Experimental: This
        endpoint is not yet ready for production use and is subject to change at any
        time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        return await self._delete(
            path_template("/api/v1/beta/sheets/jobs/{spreadsheet_job_id}", spreadsheet_job_id=spreadsheet_job_id),
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
                    sheet_delete_job_params.SheetDeleteJobParams,
                ),
            ),
            cast_to=object,
        )

    async def get(
        self,
        spreadsheet_job_id: str,
        *,
        include_results: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SheetsJob:
        """
        Get a spreadsheet parsing job.

        When include_results=True (default), the response will include extracted regions
        and results if the job is complete, eliminating the need for a separate /results
        call.

        Experimental: This endpoint is not yet ready for production use and is subject
        to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        return await self._get(
            path_template("/api/v1/beta/sheets/jobs/{spreadsheet_job_id}", spreadsheet_job_id=spreadsheet_job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_results": include_results,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    sheet_get_params.SheetGetParams,
                ),
            ),
            cast_to=SheetsJob,
        )

    async def get_result_table(
        self,
        region_type: Literal["table", "extra", "cell_metadata"],
        *,
        spreadsheet_job_id: str,
        region_id: str,
        expires_at_seconds: Optional[int] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PresignedURL:
        """Generate a presigned URL to download a specific extracted region.

        Experimental:
        This endpoint is not yet ready for production use and is subject to change at
        any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not spreadsheet_job_id:
            raise ValueError(f"Expected a non-empty value for `spreadsheet_job_id` but received {spreadsheet_job_id!r}")
        if not region_id:
            raise ValueError(f"Expected a non-empty value for `region_id` but received {region_id!r}")
        if not region_type:
            raise ValueError(f"Expected a non-empty value for `region_type` but received {region_type!r}")
        return await self._get(
            path_template(
                "/api/v1/beta/sheets/jobs/{spreadsheet_job_id}/regions/{region_id}/result/{region_type}",
                spreadsheet_job_id=spreadsheet_job_id,
                region_id=region_id,
                region_type=region_type,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expires_at_seconds": expires_at_seconds,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    sheet_get_result_table_params.SheetGetResultTableParams,
                ),
            ),
            cast_to=PresignedURL,
        )


class SheetsResourceWithRawResponse:
    def __init__(self, sheets: SheetsResource) -> None:
        self._sheets = sheets

        self.create = to_raw_response_wrapper(
            sheets.create,
        )
        self.list = to_raw_response_wrapper(
            sheets.list,
        )
        self.delete_job = to_raw_response_wrapper(
            sheets.delete_job,
        )
        self.get = to_raw_response_wrapper(
            sheets.get,
        )
        self.get_result_table = to_raw_response_wrapper(
            sheets.get_result_table,
        )


class AsyncSheetsResourceWithRawResponse:
    def __init__(self, sheets: AsyncSheetsResource) -> None:
        self._sheets = sheets

        self.create = async_to_raw_response_wrapper(
            sheets.create,
        )
        self.list = async_to_raw_response_wrapper(
            sheets.list,
        )
        self.delete_job = async_to_raw_response_wrapper(
            sheets.delete_job,
        )
        self.get = async_to_raw_response_wrapper(
            sheets.get,
        )
        self.get_result_table = async_to_raw_response_wrapper(
            sheets.get_result_table,
        )


class SheetsResourceWithStreamingResponse:
    def __init__(self, sheets: SheetsResource) -> None:
        self._sheets = sheets

        self.create = to_streamed_response_wrapper(
            sheets.create,
        )
        self.list = to_streamed_response_wrapper(
            sheets.list,
        )
        self.delete_job = to_streamed_response_wrapper(
            sheets.delete_job,
        )
        self.get = to_streamed_response_wrapper(
            sheets.get,
        )
        self.get_result_table = to_streamed_response_wrapper(
            sheets.get_result_table,
        )


class AsyncSheetsResourceWithStreamingResponse:
    def __init__(self, sheets: AsyncSheetsResource) -> None:
        self._sheets = sheets

        self.create = async_to_streamed_response_wrapper(
            sheets.create,
        )
        self.list = async_to_streamed_response_wrapper(
            sheets.list,
        )
        self.delete_job = async_to_streamed_response_wrapper(
            sheets.delete_job,
        )
        self.get = async_to_streamed_response_wrapper(
            sheets.get,
        )
        self.get_result_table = async_to_streamed_response_wrapper(
            sheets.get_result_table,
        )
