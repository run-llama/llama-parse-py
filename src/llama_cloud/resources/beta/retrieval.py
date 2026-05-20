# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPaginatedCursorPost, AsyncPaginatedCursorPost
from ...types.beta import retrieval_find_params, retrieval_grep_params, retrieval_read_params, retrieval_retrieve_params
from ..._base_client import AsyncPaginator, make_request_options
from ...types.beta.retrieval_find_response import RetrievalFindResponse
from ...types.beta.retrieval_grep_response import RetrievalGrepResponse
from ...types.beta.retrieval_read_response import RetrievalReadResponse
from ...types.beta.retrieval_retrieve_response import RetrievalRetrieveResponse

__all__ = ["RetrievalResource", "AsyncRetrievalResource"]


class RetrievalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RetrievalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return RetrievalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrievalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return RetrievalResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        index_id: str,
        query: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        custom_filters: Optional[Dict[str, Optional[retrieval_retrieve_params.CustomFilters]]] | Omit = omit,
        full_text_pipeline_weight: Optional[float] | Omit = omit,
        num_candidates: Optional[int] | Omit = omit,
        rerank: retrieval_retrieve_params.Rerank | Omit = omit,
        score_threshold: Optional[float] | Omit = omit,
        static_filters: Optional[retrieval_retrieve_params.StaticFilters] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        vector_pipeline_weight: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalRetrieveResponse:
        """
        Retrieve relevant chunks via hybrid search (vector + full-text), with filtering
        on built-in or user-defined metadata.

        Args:
          index_id: ID of the index to retrieve against.

          query: Natural-language query to retrieve relevant chunks.

          custom_filters: Filters on user-defined metadata fields.

          full_text_pipeline_weight: Weight of the full-text search pipeline (0-1).

          num_candidates: Number of candidates for approximate nearest neighbor search.

          rerank: Reranking configuration applied after hybrid search. Enabled by default.

          score_threshold: Minimum score threshold for returned results.

          static_filters: Filters on built-in document fields (page range, chunk index, etc.).

          top_k: Maximum number of results to return.

          vector_pipeline_weight: Weight of the vector search pipeline (0-1).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/retrieval/retrieve",
            body=maybe_transform(
                {
                    "index_id": index_id,
                    "query": query,
                    "custom_filters": custom_filters,
                    "full_text_pipeline_weight": full_text_pipeline_weight,
                    "num_candidates": num_candidates,
                    "rerank": rerank,
                    "score_threshold": score_threshold,
                    "static_filters": static_filters,
                    "top_k": top_k,
                    "vector_pipeline_weight": vector_pipeline_weight,
                },
                retrieval_retrieve_params.RetrievalRetrieveParams,
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
                    retrieval_retrieve_params.RetrievalRetrieveParams,
                ),
            ),
            cast_to=RetrievalRetrieveResponse,
        )

    def find(
        self,
        *,
        index_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        file_name_contains: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursorPost[RetrievalFindResponse]:
        """
        Search for files by name.

        Args:
          index_id: ID of the index to search within.

          file_name: Exact file name to match.

          file_name_contains: Substring match on file name (case-insensitive).

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/retrieval/files/find",
            page=SyncPaginatedCursorPost[RetrievalFindResponse],
            body=maybe_transform(
                {
                    "index_id": index_id,
                    "file_name": file_name,
                    "file_name_contains": file_name_contains,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                retrieval_find_params.RetrievalFindParams,
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
                    retrieval_find_params.RetrievalFindParams,
                ),
            ),
            model=RetrievalFindResponse,
            method="post",
        )

    def grep(
        self,
        *,
        file_id: str,
        index_id: str,
        pattern: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        context_chars: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursorPost[RetrievalGrepResponse]:
        """
        Grep within a file's parsed content using a regex pattern.

        Args:
          file_id: ID of the file to grep.

          index_id: ID of the index the file belongs to.

          pattern: Regex pattern to search for.

          context_chars: Number of characters of context to include before and after the matched pattern
              in the content field of the response

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/retrieval/files/grep",
            page=SyncPaginatedCursorPost[RetrievalGrepResponse],
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "index_id": index_id,
                    "pattern": pattern,
                    "context_chars": context_chars,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                retrieval_grep_params.RetrievalGrepParams,
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
                    retrieval_grep_params.RetrievalGrepParams,
                ),
            ),
            model=RetrievalGrepResponse,
            method="post",
        )

    def read(
        self,
        *,
        file_id: str,
        index_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        max_length: Optional[int] | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalReadResponse:
        """
        Read the parsed text content of a specific file.

        Args:
          file_id: ID of the file to read.

          index_id: ID of the index the file belongs to.

          max_length: Maximum number of characters to read from the offset.

          offset: Starting character offset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/retrieval/files/read",
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "index_id": index_id,
                    "max_length": max_length,
                    "offset": offset,
                },
                retrieval_read_params.RetrievalReadParams,
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
                    retrieval_read_params.RetrievalReadParams,
                ),
            ),
            cast_to=RetrievalReadResponse,
        )


class AsyncRetrievalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRetrievalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrievalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrievalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncRetrievalResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        index_id: str,
        query: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        custom_filters: Optional[Dict[str, Optional[retrieval_retrieve_params.CustomFilters]]] | Omit = omit,
        full_text_pipeline_weight: Optional[float] | Omit = omit,
        num_candidates: Optional[int] | Omit = omit,
        rerank: retrieval_retrieve_params.Rerank | Omit = omit,
        score_threshold: Optional[float] | Omit = omit,
        static_filters: Optional[retrieval_retrieve_params.StaticFilters] | Omit = omit,
        top_k: Optional[int] | Omit = omit,
        vector_pipeline_weight: Optional[float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalRetrieveResponse:
        """
        Retrieve relevant chunks via hybrid search (vector + full-text), with filtering
        on built-in or user-defined metadata.

        Args:
          index_id: ID of the index to retrieve against.

          query: Natural-language query to retrieve relevant chunks.

          custom_filters: Filters on user-defined metadata fields.

          full_text_pipeline_weight: Weight of the full-text search pipeline (0-1).

          num_candidates: Number of candidates for approximate nearest neighbor search.

          rerank: Reranking configuration applied after hybrid search. Enabled by default.

          score_threshold: Minimum score threshold for returned results.

          static_filters: Filters on built-in document fields (page range, chunk index, etc.).

          top_k: Maximum number of results to return.

          vector_pipeline_weight: Weight of the vector search pipeline (0-1).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/retrieval/retrieve",
            body=await async_maybe_transform(
                {
                    "index_id": index_id,
                    "query": query,
                    "custom_filters": custom_filters,
                    "full_text_pipeline_weight": full_text_pipeline_weight,
                    "num_candidates": num_candidates,
                    "rerank": rerank,
                    "score_threshold": score_threshold,
                    "static_filters": static_filters,
                    "top_k": top_k,
                    "vector_pipeline_weight": vector_pipeline_weight,
                },
                retrieval_retrieve_params.RetrievalRetrieveParams,
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
                    retrieval_retrieve_params.RetrievalRetrieveParams,
                ),
            ),
            cast_to=RetrievalRetrieveResponse,
        )

    def find(
        self,
        *,
        index_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        file_name: Optional[str] | Omit = omit,
        file_name_contains: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RetrievalFindResponse, AsyncPaginatedCursorPost[RetrievalFindResponse]]:
        """
        Search for files by name.

        Args:
          index_id: ID of the index to search within.

          file_name: Exact file name to match.

          file_name_contains: Substring match on file name (case-insensitive).

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/retrieval/files/find",
            page=AsyncPaginatedCursorPost[RetrievalFindResponse],
            body=maybe_transform(
                {
                    "index_id": index_id,
                    "file_name": file_name,
                    "file_name_contains": file_name_contains,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                retrieval_find_params.RetrievalFindParams,
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
                    retrieval_find_params.RetrievalFindParams,
                ),
            ),
            model=RetrievalFindResponse,
            method="post",
        )

    def grep(
        self,
        *,
        file_id: str,
        index_id: str,
        pattern: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        context_chars: Optional[int] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[RetrievalGrepResponse, AsyncPaginatedCursorPost[RetrievalGrepResponse]]:
        """
        Grep within a file's parsed content using a regex pattern.

        Args:
          file_id: ID of the file to grep.

          index_id: ID of the index the file belongs to.

          pattern: Regex pattern to search for.

          context_chars: Number of characters of context to include before and after the matched pattern
              in the content field of the response

          page_size: The maximum number of items to return. The service may return fewer than this
              value. If unspecified, a default page size will be used. The maximum value is
              typically 1000; values above this will be coerced to the maximum.

          page_token: A page token, received from a previous list call. Provide this to retrieve the
              subsequent page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/retrieval/files/grep",
            page=AsyncPaginatedCursorPost[RetrievalGrepResponse],
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "index_id": index_id,
                    "pattern": pattern,
                    "context_chars": context_chars,
                    "page_size": page_size,
                    "page_token": page_token,
                },
                retrieval_grep_params.RetrievalGrepParams,
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
                    retrieval_grep_params.RetrievalGrepParams,
                ),
            ),
            model=RetrievalGrepResponse,
            method="post",
        )

    async def read(
        self,
        *,
        file_id: str,
        index_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        max_length: Optional[int] | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrievalReadResponse:
        """
        Read the parsed text content of a specific file.

        Args:
          file_id: ID of the file to read.

          index_id: ID of the index the file belongs to.

          max_length: Maximum number of characters to read from the offset.

          offset: Starting character offset.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/retrieval/files/read",
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "index_id": index_id,
                    "max_length": max_length,
                    "offset": offset,
                },
                retrieval_read_params.RetrievalReadParams,
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
                    retrieval_read_params.RetrievalReadParams,
                ),
            ),
            cast_to=RetrievalReadResponse,
        )


class RetrievalResourceWithRawResponse:
    def __init__(self, retrieval: RetrievalResource) -> None:
        self._retrieval = retrieval

        self.retrieve = to_raw_response_wrapper(
            retrieval.retrieve,
        )
        self.find = to_raw_response_wrapper(
            retrieval.find,
        )
        self.grep = to_raw_response_wrapper(
            retrieval.grep,
        )
        self.read = to_raw_response_wrapper(
            retrieval.read,
        )


class AsyncRetrievalResourceWithRawResponse:
    def __init__(self, retrieval: AsyncRetrievalResource) -> None:
        self._retrieval = retrieval

        self.retrieve = async_to_raw_response_wrapper(
            retrieval.retrieve,
        )
        self.find = async_to_raw_response_wrapper(
            retrieval.find,
        )
        self.grep = async_to_raw_response_wrapper(
            retrieval.grep,
        )
        self.read = async_to_raw_response_wrapper(
            retrieval.read,
        )


class RetrievalResourceWithStreamingResponse:
    def __init__(self, retrieval: RetrievalResource) -> None:
        self._retrieval = retrieval

        self.retrieve = to_streamed_response_wrapper(
            retrieval.retrieve,
        )
        self.find = to_streamed_response_wrapper(
            retrieval.find,
        )
        self.grep = to_streamed_response_wrapper(
            retrieval.grep,
        )
        self.read = to_streamed_response_wrapper(
            retrieval.read,
        )


class AsyncRetrievalResourceWithStreamingResponse:
    def __init__(self, retrieval: AsyncRetrievalResource) -> None:
        self._retrieval = retrieval

        self.retrieve = async_to_streamed_response_wrapper(
            retrieval.retrieve,
        )
        self.find = async_to_streamed_response_wrapper(
            retrieval.find,
        )
        self.grep = async_to_streamed_response_wrapper(
            retrieval.grep,
        )
        self.read = async_to_streamed_response_wrapper(
            retrieval.read,
        )
