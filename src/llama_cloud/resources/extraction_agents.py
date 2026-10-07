# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import extraction_agent_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.extract_agent import ExtractAgent

__all__ = ["ExtractionAgentsResource", "AsyncExtractionAgentsResource"]


class ExtractionAgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExtractionAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return ExtractionAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExtractionAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return ExtractionAgentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        include_default: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[ExtractAgent]:
        """
        List the extraction agents in a project, newest first.

        Args:
          include_default: Whether to include default agents in the results

          page_size: Number of items per page

          page_token: Cursor from the previous page's `next_page_token`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/extraction-agents",
            page=SyncPaginatedCursor[ExtractAgent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_default": include_default,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    extraction_agent_list_params.ExtractionAgentListParams,
                ),
            ),
            model=ExtractAgent,
        )


class AsyncExtractionAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExtractionAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncExtractionAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExtractionAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncExtractionAgentsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        include_default: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: int | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ExtractAgent, AsyncPaginatedCursor[ExtractAgent]]:
        """
        List the extraction agents in a project, newest first.

        Args:
          include_default: Whether to include default agents in the results

          page_size: Number of items per page

          page_token: Cursor from the previous page's `next_page_token`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/extraction-agents",
            page=AsyncPaginatedCursor[ExtractAgent],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_default": include_default,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    extraction_agent_list_params.ExtractionAgentListParams,
                ),
            ),
            model=ExtractAgent,
        )


class ExtractionAgentsResourceWithRawResponse:
    def __init__(self, extraction_agents: ExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.list = to_raw_response_wrapper(
            extraction_agents.list,
        )


class AsyncExtractionAgentsResourceWithRawResponse:
    def __init__(self, extraction_agents: AsyncExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.list = async_to_raw_response_wrapper(
            extraction_agents.list,
        )


class ExtractionAgentsResourceWithStreamingResponse:
    def __init__(self, extraction_agents: ExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.list = to_streamed_response_wrapper(
            extraction_agents.list,
        )


class AsyncExtractionAgentsResourceWithStreamingResponse:
    def __init__(self, extraction_agents: AsyncExtractionAgentsResource) -> None:
        self._extraction_agents = extraction_agents

        self.list = async_to_streamed_response_wrapper(
            extraction_agents.list,
        )
