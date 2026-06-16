# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import CompositeRetrievalMode
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.retrievers import query_search_params
from ...types.re_rank_config_param import ReRankConfigParam
from ...types.composite_retrieval_mode import CompositeRetrievalMode
from ...types.composite_retrieval_result import CompositeRetrievalResult

__all__ = ["QueryResource", "AsyncQueryResource"]


class QueryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return QueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return QueryResourceWithStreamingResponse(self)

    def search(
        self,
        retriever_id: str,
        *,
        query: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        mode: CompositeRetrievalMode | Omit = omit,
        rerank_config: ReRankConfigParam | Omit = omit,
        rerank_top_n: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompositeRetrievalResult:
        """
        Retrieve data using a Retriever.

        Args:
          query: The query to retrieve against.

          mode: The mode of composite retrieval.

          rerank_config: The rerank configuration for composite retrieval.

          rerank_top_n: (use rerank_config.top_n instead) The number of nodes to retrieve after
              reranking over retrieved nodes from all retrieval tools.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not retriever_id:
            raise ValueError(f"Expected a non-empty value for `retriever_id` but received {retriever_id!r}")
        return self._post(
            path_template("/api/v1/retrievers/{retriever_id}/retrieve", retriever_id=retriever_id),
            body=maybe_transform(
                {
                    "query": query,
                    "mode": mode,
                    "rerank_config": rerank_config,
                    "rerank_top_n": rerank_top_n,
                },
                query_search_params.QuerySearchParams,
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
                    query_search_params.QuerySearchParams,
                ),
            ),
            cast_to=CompositeRetrievalResult,
        )


class AsyncQueryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncQueryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncQueryResourceWithStreamingResponse(self)

    async def search(
        self,
        retriever_id: str,
        *,
        query: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        mode: CompositeRetrievalMode | Omit = omit,
        rerank_config: ReRankConfigParam | Omit = omit,
        rerank_top_n: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CompositeRetrievalResult:
        """
        Retrieve data using a Retriever.

        Args:
          query: The query to retrieve against.

          mode: The mode of composite retrieval.

          rerank_config: The rerank configuration for composite retrieval.

          rerank_top_n: (use rerank_config.top_n instead) The number of nodes to retrieve after
              reranking over retrieved nodes from all retrieval tools.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not retriever_id:
            raise ValueError(f"Expected a non-empty value for `retriever_id` but received {retriever_id!r}")
        return await self._post(
            path_template("/api/v1/retrievers/{retriever_id}/retrieve", retriever_id=retriever_id),
            body=await async_maybe_transform(
                {
                    "query": query,
                    "mode": mode,
                    "rerank_config": rerank_config,
                    "rerank_top_n": rerank_top_n,
                },
                query_search_params.QuerySearchParams,
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
                    query_search_params.QuerySearchParams,
                ),
            ),
            cast_to=CompositeRetrievalResult,
        )


class QueryResourceWithRawResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.search = to_raw_response_wrapper(
            query.search,
        )


class AsyncQueryResourceWithRawResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.search = async_to_raw_response_wrapper(
            query.search,
        )


class QueryResourceWithStreamingResponse:
    def __init__(self, query: QueryResource) -> None:
        self._query = query

        self.search = to_streamed_response_wrapper(
            query.search,
        )


class AsyncQueryResourceWithStreamingResponse:
    def __init__(self, query: AsyncQueryResource) -> None:
        self._query = query

        self.search = async_to_streamed_response_wrapper(
            query.search,
        )
