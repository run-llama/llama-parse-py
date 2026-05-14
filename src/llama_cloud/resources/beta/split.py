# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

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
from ...types.beta import split_get_params, split_list_params, split_create_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.beta.split_get_response import SplitGetResponse
from ...types.beta.split_list_response import SplitListResponse
from ...types.beta.split_category_param import SplitCategoryParam
from ...types.beta.split_create_response import SplitCreateResponse
from ...types.beta.split_document_input_param import SplitDocumentInputParam

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
        document_input: SplitDocumentInputParam,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[split_create_params.Configuration] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
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
          document_input: Document to be split.

          configuration: Split configuration with categories and splitting strategy.

          configuration_id: Saved split configuration ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/split/jobs",
            body=maybe_transform(
                {
                    "document_input": document_input,
                    "configuration": configuration,
                    "configuration_id": configuration_id,
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
        status: Optional[Literal["pending", "processing", "completed", "failed", "cancelled"]] | Omit = omit,
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
            "/api/v1/beta/split/jobs",
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
            path_template("/api/v1/beta/split/jobs/{split_job_id}", split_job_id=split_job_id),
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

    def split(
        self,
        *,
        categories: Iterable[SplitCategoryParam],
        document_input: SplitDocumentInputParam,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        splitting_strategy: split_create_params.ConfigurationSplittingStrategy | Omit = omit,
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
    ) -> SplitGetResponse:
        """
        Create a document split job and wait for it to complete, returning the result.

        This is a convenience method that combines create() and wait_for_completion()
        into a single call for the most common end-to-end workflow.

        Experimental: This endpoint is not yet ready for production use and is subject
        to change at any time.

        Args:
            categories: Categories to split the document into.

            document_input: Document to be split.

            organization_id: The organization ID to use for the split job.

            project_id: The project ID to use for the split job.

            splitting_strategy: Strategy for splitting the document.

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2000.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed split job with result (SplitGetResponse)

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # One-shot: create job, wait for completion, and get result
            result = client.beta.split.split(
                categories=[
                    {"name": "Resume", "description": "Resume/CV documents"},
                    {"name": "Cover Letter", "description": "Cover letter documents"},
                ],
                document_input={"type": "file_id", "value": "your-file-id"},
                verbose=True,
            )

            # Result is ready to use immediately
            for segment in result.result.segments:
                print(f"Category: {segment.category}, Pages: {segment.pages}")
            ```
        """
        # Create the job with categories wrapped in configuration
        config: dict[str, object] = {"categories": list(categories)}
        if splitting_strategy is not omit:
            config["splitting_strategy"] = splitting_strategy
        job = self.create(
            document_input=document_input,
            organization_id=organization_id,
            project_id=project_id,
            configuration=config,  # type: ignore[arg-type]
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion and return the result
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
        split_job_id: str,
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
    ) -> SplitGetResponse:
        """
        Wait for a split job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Experimental: This endpoint is not yet ready for production use and is subject
        to change at any time.

        Args:
            split_job_id: The ID of the split job to wait for

            organization_id: The organization ID

            project_id: The project ID

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2000.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed SplitGetResponse with result

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # Create a split job
            job = client.beta.split.create(
                categories=[{"name": "Resume"}, {"name": "Cover Letter"}],
                document_input={"type": "file_id", "value": "your-file-id"},
            )

            # Wait for it to complete
            completed_job = client.beta.split.wait_for_completion(job.id, verbose=True)

            # Access the result
            for segment in completed_job.result.segments:
                print(f"Category: {segment.category}, Pages: {segment.pages}")
            ```
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")

        def get_status() -> SplitGetResponse:
            return self.get(
                split_job_id,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: SplitGetResponse) -> bool:
            return job.status == "completed"

        def is_error(job: SplitGetResponse) -> bool:
            return job.status == "failed"

        def get_error_message(job: SplitGetResponse) -> str:
            error_parts = [f"Job {split_job_id} failed with status: {job.status}"]
            if job.error_message:
                error_parts.append(f"Error: {job.error_message}")
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
        document_input: SplitDocumentInputParam,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        configuration: Optional[split_create_params.Configuration] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
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
          document_input: Document to be split.

          configuration: Split configuration with categories and splitting strategy.

          configuration_id: Saved split configuration ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/split/jobs",
            body=await async_maybe_transform(
                {
                    "document_input": document_input,
                    "configuration": configuration,
                    "configuration_id": configuration_id,
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
        status: Optional[Literal["pending", "processing", "completed", "failed", "cancelled"]] | Omit = omit,
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
            "/api/v1/beta/split/jobs",
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
            path_template("/api/v1/beta/split/jobs/{split_job_id}", split_job_id=split_job_id),
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

    async def split(
        self,
        *,
        categories: Iterable[SplitCategoryParam],
        document_input: SplitDocumentInputParam,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        splitting_strategy: split_create_params.ConfigurationSplittingStrategy | Omit = omit,
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
    ) -> SplitGetResponse:
        """
        Create a document split job and wait for it to complete, returning the result.

        This is a convenience method that combines create() and wait_for_completion()
        into a single call for the most common end-to-end workflow.

        Experimental: This endpoint is not yet ready for production use and is subject
        to change at any time.

        Args:
            categories: Categories to split the document into.

            document_input: Document to be split.

            organization_id: The organization ID to use for the split job.

            project_id: The project ID to use for the split job.

            splitting_strategy: Strategy for splitting the document.

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2000.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed split job with result (SplitGetResponse)

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            # One-shot: create job, wait for completion, and get result
            result = await client.beta.split.split(
                categories=[
                    {"name": "Resume", "description": "Resume/CV documents"},
                    {"name": "Cover Letter", "description": "Cover letter documents"},
                ],
                document_input={"type": "file_id", "value": "your-file-id"},
                verbose=True,
            )

            # Result is ready to use immediately
            for segment in result.result.segments:
                print(f"Category: {segment.category}, Pages: {segment.pages}")
            ```
        """
        # Create the job with categories wrapped in configuration
        config: dict[str, object] = {"categories": list(categories)}
        if splitting_strategy is not omit:
            config["splitting_strategy"] = splitting_strategy
        job = await self.create(
            document_input=document_input,
            organization_id=organization_id,
            project_id=project_id,
            configuration=config,  # type: ignore[arg-type]
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion and return the result
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
        split_job_id: str,
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
    ) -> SplitGetResponse:
        """
        Wait for a split job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Experimental: This endpoint is not yet ready for production use and is subject
        to change at any time.

        Args:
            split_job_id: The ID of the split job to wait for

            organization_id: The organization ID

            project_id: The project ID

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 2000.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed SplitGetResponse with result

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            # Create a split job
            job = await client.beta.split.create(
                categories=[{"name": "Resume"}, {"name": "Cover Letter"}],
                document_input={"type": "file_id", "value": "your-file-id"},
            )

            # Wait for it to complete
            completed_job = await client.beta.split.wait_for_completion(job.id, verbose=True)

            # Access the result
            for segment in completed_job.result.segments:
                print(f"Category: {segment.category}, Pages: {segment.pages}")
            ```
        """
        if not split_job_id:
            raise ValueError(f"Expected a non-empty value for `split_job_id` but received {split_job_id!r}")

        async def get_status() -> SplitGetResponse:
            return await self.get(
                split_job_id,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: SplitGetResponse) -> bool:
            return job.status == "completed"

        def is_error(job: SplitGetResponse) -> bool:
            return job.status == "failed"

        def get_error_message(job: SplitGetResponse) -> str:
            error_parts = [f"Job {split_job_id} failed with status: {job.status}"]
            if job.error_message:
                error_parts.append(f"Error: {job.error_message}")
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


class SplitResourceWithRawResponse:
    def __init__(self, split: SplitResource) -> None:
        self._split = split

        self.create = to_raw_response_wrapper(
            split.create,
        )
        self.list = to_raw_response_wrapper(
            split.list,
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
        self.get = async_to_streamed_response_wrapper(
            split.get,
        )
