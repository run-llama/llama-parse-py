# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import parsing_get_params, parsing_list_params, parsing_create_params
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
        tier: Union[Literal["fast", "cost_effective", "agentic", "agentic_plus"], str],
        version: Union[Literal["latest", "2026-06-18", "2025-12-11"], str],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        agentic_options: Optional[parsing_create_params.AgenticOptions] | Omit = omit,
        client_name: Optional[str] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        crop_box: parsing_create_params.CropBox | Omit = omit,
        disable_cache: Optional[bool] | Omit = omit,
        fast_options: Optional[object] | Omit = omit,
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
        Parse a file by file ID or URL.

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

          version: Version for the selected tier. Use `latest`, or pin one of that tier's dated
              versions.

              Current `latest` by tier:

              - `fast`: `2025-12-11`
              - `cost_effective`: `2026-06-18`
              - `agentic`: `2026-06-18`
              - `agentic_plus`: `2026-06-18`

              Full list: `GET /api/v2/parse/versions`.

          agentic_options: Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

              These options customize how the AI processes and interprets document content.
              Only applicable when using non-fast tiers.

          client_name: Identifier for the client/application making the request. Used for analytics and
              debugging. Example: 'my-app-v2'

          configuration_id: ID of a saved parse configuration. When set, `tier` and `version` default to the
              saved configuration's values — omit them or pass `'configured'`.

          crop_box: Crop boundaries to process only a portion of each page. Values are ratios 0-1
              from page edges

          disable_cache: Bypass result caching and force re-parsing. Use when document content may have
              changed or you need fresh results

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
        return self._post(
            "/api/v2/parse",
            body=maybe_transform(
                {
                    "tier": tier,
                    "version": version,
                    "agentic_options": agentic_options,
                    "client_name": client_name,
                    "configuration_id": configuration_id,
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
        tier: Union[Literal["fast", "cost_effective", "agentic", "agentic_plus"], str],
        version: Union[Literal["latest", "2026-06-18", "2025-12-11"], str],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        agentic_options: Optional[parsing_create_params.AgenticOptions] | Omit = omit,
        client_name: Optional[str] | Omit = omit,
        configuration_id: Optional[str] | Omit = omit,
        crop_box: parsing_create_params.CropBox | Omit = omit,
        disable_cache: Optional[bool] | Omit = omit,
        fast_options: Optional[object] | Omit = omit,
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
        Parse a file by file ID or URL.

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

          version: Version for the selected tier. Use `latest`, or pin one of that tier's dated
              versions.

              Current `latest` by tier:

              - `fast`: `2025-12-11`
              - `cost_effective`: `2026-06-18`
              - `agentic`: `2026-06-18`
              - `agentic_plus`: `2026-06-18`

              Full list: `GET /api/v2/parse/versions`.

          agentic_options: Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

              These options customize how the AI processes and interprets document content.
              Only applicable when using non-fast tiers.

          client_name: Identifier for the client/application making the request. Used for analytics and
              debugging. Example: 'my-app-v2'

          configuration_id: ID of a saved parse configuration. When set, `tier` and `version` default to the
              saved configuration's values — omit them or pass `'configured'`.

          crop_box: Crop boundaries to process only a portion of each page. Values are ratios 0-1
              from page edges

          disable_cache: Bypass result caching and force re-parsing. Use when document content may have
              changed or you need fresh results

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
        return await self._post(
            "/api/v2/parse",
            body=await async_maybe_transform(
                {
                    "tier": tier,
                    "version": version,
                    "agentic_options": agentic_options,
                    "client_name": client_name,
                    "configuration_id": configuration_id,
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
