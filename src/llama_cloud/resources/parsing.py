# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import json
from typing import Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import parsing_get_params, parsing_list_params, parsing_create_params, parsing_upload_file_params
from .._files import to_httpx_files, async_to_httpx_files
from .._types import Body, Omit, Query, Headers, NotGiven, FileTypes, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._polling import DEFAULT_TIMEOUT, BackoffStrategy, poll_until_complete, poll_until_complete_async
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from .._base_client import AsyncPaginator, make_request_options
from ..types.parsing_get_response import ParsingGetResponse
from ..types.parsing_list_response import ParsingListResponse
from ..types.parsing_create_response import ParsingCreateResponse

__all__ = ["ParsingResource", "AsyncParsingResource"]


class ParsingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParsingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return ParsingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParsingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return ParsingResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        tier: Literal["fast", "cost_effective", "agentic", "agentic_plus"],
        version: Union[Literal["latest", "2026-05-13", "2026-05-11", "2026-04-09", "2025-12-11"], str],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        agentic_options: Optional[parsing_create_params.AgenticOptions] | Omit = omit,
        client_name: Optional[str] | Omit = omit,
        crop_box: parsing_create_params.CropBox | Omit = omit,
        disable_cache: Optional[bool] | Omit = omit,
        fast_options: Optional[object] | Omit = omit,
        upload_file: Optional[FileTypes] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        http_proxy: Optional[str] | Omit = omit,
        input_options: parsing_create_params.InputOptions | Omit = omit,
        output_options: parsing_create_params.OutputOptions | Omit = omit,
        page_ranges: parsing_create_params.PageRanges | Omit = omit,
        processing_control: parsing_create_params.ProcessingControl | Omit = omit,
        processing_options: parsing_create_params.ProcessingOptions | Omit = omit,
        source_url: Optional[str] | Omit = omit,
        webhook_configurations: Iterable[parsing_create_params.WebhookConfiguration] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingCreateResponse:
        """
        Parse a file by file ID, URL, or direct file upload.

        Provide either `file_id` (a previously uploaded file) or `source_url` (a
        publicly accessible URL). Configure parsing with options like `tier`,
        `target_pages`, and `lang`.

        ## Tiers

        - `fast` — rule-based, cheapest, no AI
        - `cost_effective` — balanced speed and quality
        - `agentic` — full AI-powered parsing
        - `agentic_plus` — premium AI with specialized features

        The job runs asynchronously. Poll `GET /parse/{job_id}` with `expand=text` or
        `expand=markdown` to retrieve results.

        Args:
          tier: Parsing tier: 'fast' (rule-based, cheapest), 'cost_effective' (balanced),
              'agentic' (AI-powered with custom prompts), or 'agentic_plus' (premium AI with
              highest accuracy)

          version: Tier version. Use 'latest' for the current stable version, or pin a dated
              version for reproducible results. See GET /api/v2/parse/versions for the
              per-tier list.

          agentic_options: Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

              These options customize how the AI processes and interprets document content.
              Only applicable when using non-fast tiers.

          client_name: Identifier for the client/application making the request. Used for analytics and
              debugging. Example: 'my-app-v2'

          crop_box: Crop boundaries to process only a portion of each page. Values are ratios 0-1
              from page edges

          disable_cache: Bypass result caching and force re-parsing. Use when document content may have
              changed or you need fresh results

          upload_file: File to upload and parse (uses multipart/form-data upload endpoint)

          fast_options: Options for fast tier parsing (rule-based, no AI).

              Fast tier uses deterministic algorithms for text extraction without AI
              enhancement. It's the fastest and most cost-effective option, best suited for
              simple documents with standard layouts. Currently has no configurable options
              but reserved for future expansion.

          file_id: ID of an existing file in the project to parse. Mutually exclusive with
              source_url

          http_proxy: HTTP/HTTPS proxy for fetching source_url. Ignored if using file_id

          input_options: Format-specific options (HTML, PDF, spreadsheet, presentation). Applied based on
              detected input file type

          output_options: Output formatting options for markdown, text, and extracted images

          page_ranges: Page selection: limit total pages or specify exact pages to process

          processing_control: Job execution controls including timeouts and failure thresholds

          processing_options: Document processing options including OCR, table extraction, and chart parsing

          source_url: Public URL of the document to parse. Mutually exclusive with file_id

          webhook_configurations: Webhook endpoints for job status notifications. Multiple webhooks can be
              configured for different events or services

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # If file is provided, use multipart upload endpoint
        if upload_file is not omit and upload_file is not None:
            # Prepare configuration as JSON string
            configuration = {
                "tier": tier,
                "version": version,
                "agentic_options": agentic_options if agentic_options is not omit else None,
                "client_name": client_name if client_name is not omit else None,
                "crop_box": crop_box if crop_box is not omit else None,
                "disable_cache": disable_cache if disable_cache is not omit else None,
                "fast_options": fast_options if fast_options is not omit else None,
                "http_proxy": http_proxy if http_proxy is not omit else None,
                "input_options": input_options if input_options is not omit else None,
                "output_options": output_options if output_options is not omit else None,
                "page_ranges": page_ranges if page_ranges is not omit else None,
                "processing_control": processing_control if processing_control is not omit else None,
                "processing_options": processing_options if processing_options is not omit else None,
                "source_url": source_url if source_url is not omit else None,
                "webhook_configurations": webhook_configurations if webhook_configurations is not omit else None,
            }
            # Remove None values
            configuration = {k: v for k, v in configuration.items() if v is not None}

            # Convert file for upload
            httpx_files = to_httpx_files({"file": cast(FileTypes, upload_file)})

            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
            return self._post(
                "/api/v2/parse/upload",
                body={"configuration": json.dumps(configuration)},
                files=httpx_files,
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
                        parsing_upload_file_params.ParsingUploadFileParams,
                    ),
                ),
                cast_to=ParsingCreateResponse,
            )

        # Otherwise use regular JSON endpoint
        return self._post(
            "/api/v2/parse",
            body=maybe_transform(
                {
                    "tier": tier,
                    "version": version,
                    "agentic_options": agentic_options,
                    "client_name": client_name,
                    "crop_box": crop_box,
                    "disable_cache": disable_cache,
                    "fast_options": fast_options,
                    "file_id": file_id,
                    "http_proxy": http_proxy,
                    "input_options": input_options,
                    "output_options": output_options,
                    "page_ranges": page_ranges,
                    "processing_control": processing_control,
                    "processing_options": processing_options,
                    "source_url": source_url,
                    "webhook_configurations": webhook_configurations,
                },
                parsing_create_params.ParsingCreateParams,
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
                    parsing_create_params.ParsingCreateParams,
                ),
            ),
            cast_to=ParsingCreateResponse,
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
        status: Optional[Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[ParsingListResponse]:
        """
        List parse jobs for the current project.

        Filter by `status` or creation date range. Results are paginated — use
        `page_token` from the response to fetch subsequent pages.

        Args:
          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          job_ids: Filter by specific job IDs

          page_size: Number of items per page

          page_token: Token for pagination

          status: Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/parse",
            page=SyncPaginatedCursor[ParsingListResponse],
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
                    parsing_list_params.ParsingListParams,
                ),
            ),
            model=ParsingListResponse,
        )

    def get(
        self,
        job_id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        image_filenames: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingGetResponse:
        """
        Retrieve a parse job with optional expanded content.

        By default returns job metadata only. Use `expand` to include parsed content:

        - `text` — plain text output
        - `markdown` — markdown output
        - `items` — structured page-by-page output
        - `job_metadata` — usage and processing details

        Content metadata fields (e.g. `text_content_metadata`) return presigned URLs for
        downloading large results.

        Args:
          expand: Fields to include: text, markdown, items, metadata, job_metadata,
              text_content_metadata, markdown_content_metadata, items_content_metadata,
              metadata_content_metadata, raw_words_content_metadata, xlsx_content_metadata,
              output_pdf_content_metadata, images_content_metadata. Metadata fields include
              presigned URLs.

          image_filenames: Filter to specific image filenames (optional). Example: image_0.png,image_1.jpg

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            path_template("/api/v2/parse/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "image_filenames": image_filenames,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    parsing_get_params.ParsingGetParams,
                ),
            ),
            cast_to=ParsingGetResponse,
        )

    def parse(
        self,
        *,
        tier: Literal["fast", "cost_effective", "agentic", "agentic_plus"],
        version: Union[Literal["2026-01-08", "2025-12-31", "2025-12-18", "2025-12-11", "latest"], str],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        agentic_options: Optional[parsing_create_params.AgenticOptions] | Omit = omit,
        client_name: Optional[str] | Omit = omit,
        crop_box: parsing_create_params.CropBox | Omit = omit,
        disable_cache: Optional[bool] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        fast_options: Optional[object] | Omit = omit,
        upload_file: Optional[FileTypes] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        http_proxy: Optional[str] | Omit = omit,
        input_options: parsing_create_params.InputOptions | Omit = omit,
        output_options: parsing_create_params.OutputOptions | Omit = omit,
        page_ranges: parsing_create_params.PageRanges | Omit = omit,
        processing_control: parsing_create_params.ProcessingControl | Omit = omit,
        processing_options: parsing_create_params.ProcessingOptions | Omit = omit,
        source_url: Optional[str] | Omit = omit,
        webhook_configurations: Iterable[parsing_create_params.WebhookConfiguration] | Omit = omit,
        image_filenames: Optional[str] | Omit = omit,
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
    ) -> ParsingGetResponse:
        """
        Parse a file and wait for it to complete, returning the result.

        This is a convenience method that combines create(), wait_for_completion(),
        and get() into a single call for the most common end-to-end workflow.

        Args:
            tier: The parsing tier to use

            version: Version of the tier configuration

            organization_id: Optional organization ID

            project_id: Optional project ID

            agentic_options: Options for agentic tier parsing (with AI agents).

            client_name: Name of the client making the parsing request

            crop_box: Document crop box boundaries

            disable_cache: Whether to disable caching for this parsing job

            expand: Fields to include: text, markdown, items, text_content_metadata,
              markdown_content_metadata, items_content_metadata, xlsx_content_metadata,
              output_pdf_content_metadata, images_content_metadata. Metadata fields include
              presigned URLs.

            fast_options: Options for fast tier parsing (without AI).

            file: File to upload and parse

            file_id: ID of an existing file in the project to parse

            http_proxy: HTTP proxy URL for network requests (only used with source_url)

            input_options: Input format-specific parsing options

            output_options: Output format and styling options

            page_ranges: Page range selection options

            processing_control: Job processing control and failure handling

            processing_options: Processing options shared across all tiers

            source_url: Source URL to fetch document from

            webhook_configurations: List of webhook configurations for notifications

            image_filenames: Comma-delimited list of image filenames to fetch.

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
            The parse result (ParsingGetResponse) with job status and optional result data

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # One-shot: parse, wait for completion, and get result
            result = client.parsing.parse(
                tier="fast",
                version="latest",
                source_url="https://example.com/document.pdf",
                expand=["text", "markdown"],
                verbose=True,
            )

            # Result is ready to use immediately
            print(result.text)
            print(result.markdown)
            ```
        """
        if isinstance(expand, Omit) or (not isinstance(expand, Omit) and len(expand) == 0):
            raise ValueError("You should provide a non-empty sequence for the `expand` parameter")
        # Create the parsing job
        job = self.create(
            tier=tier,
            version=version,
            organization_id=organization_id,
            project_id=project_id,
            agentic_options=agentic_options,
            client_name=client_name,
            crop_box=crop_box,
            disable_cache=disable_cache,
            fast_options=fast_options,
            upload_file=upload_file,
            file_id=file_id,
            http_proxy=http_proxy,
            input_options=input_options,
            output_options=output_options,
            page_ranges=page_ranges,
            processing_control=processing_control,
            processing_options=processing_options,
            source_url=source_url,
            webhook_configurations=webhook_configurations,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion
        self.wait_for_completion(
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

        # Get and return the result
        return self.get(
            job.id,
            image_filenames=image_filenames,
            expand=expand,
            organization_id=organization_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

    def wait_for_completion(
        self,
        job_id: str,
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
    ) -> ParsingCreateResponse:
        """
        Wait for a parse job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Args:
            job_id: The ID of the parse job to wait for

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
            The completed parse job

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # Create a parse job
            job = client.parsing.create(tier="fast", version="latest", source_url="https://example.com/doc.pdf")

            # Wait for it to complete
            completed_job = client.parsing.wait_for_completion(job.id, verbose=True)

            # Get the result
            result = client.parsing.get(job.id, expand=["text"])
            ```
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")

        def get_status() -> ParsingCreateResponse:
            response = self.get(
                job_id,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )
            # Convert ParsingGetResponse to ParsingCreateResponse (just the job part)
            return ParsingCreateResponse(
                id=response.job.id,
                project_id=response.job.project_id,
                status=response.job.status,
                created_at=response.job.created_at,
                error_message=response.job.error_message,
                updated_at=response.job.updated_at,
            )

        def is_complete(job: ParsingCreateResponse) -> bool:
            return job.status == "COMPLETED"

        def is_error(job: ParsingCreateResponse) -> bool:
            return job.status in ("FAILED", "CANCELLED")

        def get_error_message(job: ParsingCreateResponse) -> str:
            error_parts = [f"Job {job_id} failed with status: {job.status}"]
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


class AsyncParsingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParsingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncParsingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParsingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncParsingResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        tier: Literal["fast", "cost_effective", "agentic", "agentic_plus"],
        version: Union[Literal["latest", "2026-05-13", "2026-05-11", "2026-04-09", "2025-12-11"], str],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        agentic_options: Optional[parsing_create_params.AgenticOptions] | Omit = omit,
        client_name: Optional[str] | Omit = omit,
        crop_box: parsing_create_params.CropBox | Omit = omit,
        disable_cache: Optional[bool] | Omit = omit,
        fast_options: Optional[object] | Omit = omit,
        upload_file: Optional[FileTypes] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        http_proxy: Optional[str] | Omit = omit,
        input_options: parsing_create_params.InputOptions | Omit = omit,
        output_options: parsing_create_params.OutputOptions | Omit = omit,
        page_ranges: parsing_create_params.PageRanges | Omit = omit,
        processing_control: parsing_create_params.ProcessingControl | Omit = omit,
        processing_options: parsing_create_params.ProcessingOptions | Omit = omit,
        source_url: Optional[str] | Omit = omit,
        webhook_configurations: Iterable[parsing_create_params.WebhookConfiguration] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingCreateResponse:
        """
        Parse a file by file ID, URL, or direct file upload.

        Provide either `file_id` (a previously uploaded file) or `source_url` (a
        publicly accessible URL). Configure parsing with options like `tier`,
        `target_pages`, and `lang`.

        ## Tiers

        - `fast` — rule-based, cheapest, no AI
        - `cost_effective` — balanced speed and quality
        - `agentic` — full AI-powered parsing
        - `agentic_plus` — premium AI with specialized features

        The job runs asynchronously. Poll `GET /parse/{job_id}` with `expand=text` or
        `expand=markdown` to retrieve results.

        Args:
          tier: Parsing tier: 'fast' (rule-based, cheapest), 'cost_effective' (balanced),
              'agentic' (AI-powered with custom prompts), or 'agentic_plus' (premium AI with
              highest accuracy)

          version: Tier version. Use 'latest' for the current stable version, or pin a dated
              version for reproducible results. See GET /api/v2/parse/versions for the
              per-tier list.

          agentic_options: Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

              These options customize how the AI processes and interprets document content.
              Only applicable when using non-fast tiers.

          client_name: Identifier for the client/application making the request. Used for analytics and
              debugging. Example: 'my-app-v2'

          crop_box: Crop boundaries to process only a portion of each page. Values are ratios 0-1
              from page edges

          disable_cache: Bypass result caching and force re-parsing. Use when document content may have
              changed or you need fresh results

          upload_file: File to upload and parse (uses multipart/form-data upload endpoint)

          fast_options: Options for fast tier parsing (rule-based, no AI).

              Fast tier uses deterministic algorithms for text extraction without AI
              enhancement. It's the fastest and most cost-effective option, best suited for
              simple documents with standard layouts. Currently has no configurable options
              but reserved for future expansion.

          file_id: ID of an existing file in the project to parse. Mutually exclusive with
              source_url

          http_proxy: HTTP/HTTPS proxy for fetching source_url. Ignored if using file_id

          input_options: Format-specific options (HTML, PDF, spreadsheet, presentation). Applied based on
              detected input file type

          output_options: Output formatting options for markdown, text, and extracted images

          page_ranges: Page selection: limit total pages or specify exact pages to process

          processing_control: Job execution controls including timeouts and failure thresholds

          processing_options: Document processing options including OCR, table extraction, and chart parsing

          source_url: Public URL of the document to parse. Mutually exclusive with file_id

          webhook_configurations: Webhook endpoints for job status notifications. Multiple webhooks can be
              configured for different events or services

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        # If upload_file is provided, use multipart upload endpoint
        if upload_file is not omit and upload_file is not None:
            # Prepare configuration as JSON string
            configuration = {
                "tier": tier,
                "version": version,
                "agentic_options": agentic_options if agentic_options is not omit else None,
                "client_name": client_name if client_name is not omit else None,
                "crop_box": crop_box if crop_box is not omit else None,
                "disable_cache": disable_cache if disable_cache is not omit else None,
                "fast_options": fast_options if fast_options is not omit else None,
                "http_proxy": http_proxy if http_proxy is not omit else None,
                "input_options": input_options if input_options is not omit else None,
                "output_options": output_options if output_options is not omit else None,
                "page_ranges": page_ranges if page_ranges is not omit else None,
                "processing_control": processing_control if processing_control is not omit else None,
                "processing_options": processing_options if processing_options is not omit else None,
                "source_url": source_url if source_url is not omit else None,
                "webhook_configurations": webhook_configurations if webhook_configurations is not omit else None,
            }
            # Remove None values
            configuration = {k: v for k, v in configuration.items() if v is not None}

            # Convert file for upload
            httpx_files = await async_to_httpx_files({"file": cast(FileTypes, upload_file)})

            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
            return await self._post(
                "/api/v2/parse/upload",
                body={"configuration": json.dumps(configuration)},
                files=httpx_files,
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
                        parsing_upload_file_params.ParsingUploadFileParams,
                    ),
                ),
                cast_to=ParsingCreateResponse,
            )

        # Otherwise use regular JSON endpoint
        return await self._post(
            "/api/v2/parse",
            body=await async_maybe_transform(
                {
                    "tier": tier,
                    "version": version,
                    "agentic_options": agentic_options,
                    "client_name": client_name,
                    "crop_box": crop_box,
                    "disable_cache": disable_cache,
                    "fast_options": fast_options,
                    "file_id": file_id,
                    "http_proxy": http_proxy,
                    "input_options": input_options,
                    "output_options": output_options,
                    "page_ranges": page_ranges,
                    "processing_control": processing_control,
                    "processing_options": processing_options,
                    "source_url": source_url,
                    "webhook_configurations": webhook_configurations,
                },
                parsing_create_params.ParsingCreateParams,
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
                    parsing_create_params.ParsingCreateParams,
                ),
            ),
            cast_to=ParsingCreateResponse,
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
        status: Optional[Literal["PENDING", "RUNNING", "COMPLETED", "FAILED", "CANCELLED"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ParsingListResponse, AsyncPaginatedCursor[ParsingListResponse]]:
        """
        List parse jobs for the current project.

        Filter by `status` or creation date range. Results are paginated — use
        `page_token` from the response to fetch subsequent pages.

        Args:
          created_at_on_or_after: Include items created at or after this timestamp (inclusive)

          created_at_on_or_before: Include items created at or before this timestamp (inclusive)

          job_ids: Filter by specific job IDs

          page_size: Number of items per page

          page_token: Token for pagination

          status: Filter by job status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/parse",
            page=AsyncPaginatedCursor[ParsingListResponse],
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
                    parsing_list_params.ParsingListParams,
                ),
            ),
            model=ParsingListResponse,
        )

    async def get(
        self,
        job_id: str,
        *,
        expand: SequenceNotStr[str] | Omit = omit,
        image_filenames: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParsingGetResponse:
        """
        Retrieve a parse job with optional expanded content.

        By default returns job metadata only. Use `expand` to include parsed content:

        - `text` — plain text output
        - `markdown` — markdown output
        - `items` — structured page-by-page output
        - `job_metadata` — usage and processing details

        Content metadata fields (e.g. `text_content_metadata`) return presigned URLs for
        downloading large results.

        Args:
          expand: Fields to include: text, markdown, items, metadata, job_metadata,
              text_content_metadata, markdown_content_metadata, items_content_metadata,
              metadata_content_metadata, raw_words_content_metadata, xlsx_content_metadata,
              output_pdf_content_metadata, images_content_metadata. Metadata fields include
              presigned URLs.

          image_filenames: Filter to specific image filenames (optional). Example: image_0.png,image_1.jpg

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            path_template("/api/v2/parse/{job_id}", job_id=job_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expand": expand,
                        "image_filenames": image_filenames,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    parsing_get_params.ParsingGetParams,
                ),
            ),
            cast_to=ParsingGetResponse,
        )

    async def parse(
        self,
        *,
        tier: Literal["fast", "cost_effective", "agentic", "agentic_plus"],
        version: Union[Literal["2026-01-08", "2025-12-31", "2025-12-18", "2025-12-11", "latest"], str],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        agentic_options: Optional[parsing_create_params.AgenticOptions] | Omit = omit,
        client_name: Optional[str] | Omit = omit,
        crop_box: parsing_create_params.CropBox | Omit = omit,
        disable_cache: Optional[bool] | Omit = omit,
        expand: SequenceNotStr[str] | Omit = omit,
        fast_options: Optional[object] | Omit = omit,
        upload_file: Optional[FileTypes] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        http_proxy: Optional[str] | Omit = omit,
        input_options: parsing_create_params.InputOptions | Omit = omit,
        output_options: parsing_create_params.OutputOptions | Omit = omit,
        page_ranges: parsing_create_params.PageRanges | Omit = omit,
        processing_control: parsing_create_params.ProcessingControl | Omit = omit,
        processing_options: parsing_create_params.ProcessingOptions | Omit = omit,
        source_url: Optional[str] | Omit = omit,
        webhook_configurations: Iterable[parsing_create_params.WebhookConfiguration] | Omit = omit,
        image_filenames: Optional[str] | Omit = omit,
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
    ) -> ParsingGetResponse:
        """
        Parse a file and wait for it to complete, returning the result.

        This is a convenience method that combines create(), wait_for_completion(),
        and get() into a single call for the most common end-to-end workflow.

        Args:
            tier: The parsing tier to use

            version: Version of the tier configuration

            organization_id: Optional organization ID

            project_id: Optional project ID

            agentic_options: Options for agentic tier parsing (with AI agents).

            client_name: Name of the client making the parsing request

            crop_box: Document crop box boundaries

            disable_cache: Whether to disable caching for this parsing job

            expand: Fields to include: text, markdown, items, text_content_metadata,
              markdown_content_metadata, items_content_metadata, xlsx_content_metadata,
              output_pdf_content_metadata, images_content_metadata. Metadata fields include
              presigned URLs.

            fast_options: Options for fast tier parsing (without AI).

            upload_file: File to upload and parse

            file_id: ID of an existing file in the project to parse

            http_proxy: HTTP proxy URL for network requests (only used with source_url)

            input_options: Input format-specific parsing options

            output_options: Output format and styling options

            page_ranges: Page range selection options

            processing_control: Job processing control and failure handling

            processing_options: Processing options shared across all tiers

            source_url: Source URL to fetch document from

            webhook_configurations: List of webhook configurations for notifications

            image_filenames: Comma-delimited list of image filenames to fetch.

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
            The parse result (ParsingGetResponse) with job status and optional result data

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            # One-shot: parse, wait for completion, and get result
            result = await client.parsing.parse(
                tier="cost_effective",
                version="latest",
                source_url="https://example.com/document.pdf",
                expand=["text", "markdown"],
                verbose=True,
            )

            # Result is ready to use immediately
            print(result.text)
            print(result.markdown)
            ```
        """
        if isinstance(expand, Omit) or (not isinstance(expand, Omit) and len(expand) == 0):
            raise ValueError("You should provide a non-empty sequence for the `expand` parameter")
        # Create the parsing job
        job = await self.create(
            tier=tier,
            organization_id=organization_id,
            project_id=project_id,
            agentic_options=agentic_options,
            client_name=client_name,
            crop_box=crop_box,
            disable_cache=disable_cache,
            fast_options=fast_options,
            upload_file=upload_file,
            file_id=file_id,
            http_proxy=http_proxy,
            input_options=input_options,
            output_options=output_options,
            page_ranges=page_ranges,
            processing_control=processing_control,
            processing_options=processing_options,
            source_url=source_url,
            version=version,
            webhook_configurations=webhook_configurations,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion
        await self.wait_for_completion(
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

        # Get and return the result
        return await self.get(
            job.id,
            image_filenames=image_filenames,
            expand=expand,
            organization_id=organization_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

    async def wait_for_completion(
        self,
        job_id: str,
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
    ) -> ParsingCreateResponse:
        """
        Wait for a parse job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Args:
            job_id: The ID of the parse job to wait for

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
            The completed parse job

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            # Create a parse job
            job = await client.parsing.create(tier="fast", version="latest", source_url="https://example.com/doc.pdf")

            # Wait for it to complete
            completed_job = await client.parsing.wait_for_completion(job.id, verbose=True)

            # Get the result
            result = await client.parsing.get(job.id, expand=["text"])
            ```
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")

        async def get_status() -> ParsingCreateResponse:
            response = await self.get(
                job_id,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )
            # Convert ParsingGetResponse to ParsingCreateResponse (just the job part)
            return ParsingCreateResponse(
                id=response.job.id,
                project_id=response.job.project_id,
                status=response.job.status,
                created_at=response.job.created_at,
                error_message=response.job.error_message,
                updated_at=response.job.updated_at,
            )

        def is_complete(job: ParsingCreateResponse) -> bool:
            return job.status == "COMPLETED"

        def is_error(job: ParsingCreateResponse) -> bool:
            return job.status in ("FAILED", "CANCELLED")

        def get_error_message(job: ParsingCreateResponse) -> str:
            error_parts = [f"Job {job_id} failed with status: {job.status}"]
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


class ParsingResourceWithRawResponse:
    def __init__(self, parsing: ParsingResource) -> None:
        self._parsing = parsing

        self.create = to_raw_response_wrapper(
            parsing.create,
        )
        self.list = to_raw_response_wrapper(
            parsing.list,
        )
        self.get = to_raw_response_wrapper(
            parsing.get,
        )


class AsyncParsingResourceWithRawResponse:
    def __init__(self, parsing: AsyncParsingResource) -> None:
        self._parsing = parsing

        self.create = async_to_raw_response_wrapper(
            parsing.create,
        )
        self.list = async_to_raw_response_wrapper(
            parsing.list,
        )
        self.get = async_to_raw_response_wrapper(
            parsing.get,
        )


class ParsingResourceWithStreamingResponse:
    def __init__(self, parsing: ParsingResource) -> None:
        self._parsing = parsing

        self.create = to_streamed_response_wrapper(
            parsing.create,
        )
        self.list = to_streamed_response_wrapper(
            parsing.list,
        )
        self.get = to_streamed_response_wrapper(
            parsing.get,
        )


class AsyncParsingResourceWithStreamingResponse:
    def __init__(self, parsing: AsyncParsingResource) -> None:
        self._parsing = parsing

        self.create = async_to_streamed_response_wrapper(
            parsing.create,
        )
        self.list = async_to_streamed_response_wrapper(
            parsing.list,
        )
        self.get = async_to_streamed_response_wrapper(
            parsing.get,
        )
