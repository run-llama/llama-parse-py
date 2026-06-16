# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...types import (
    CompositeRetrievalMode,
    retriever_get_params,
    retriever_list_params,
    retriever_create_params,
    retriever_delete_params,
    retriever_search_params,
    retriever_update_params,
    retriever_upsert_params,
)
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .retriever import (
    RetrieverResource,
    AsyncRetrieverResource,
    RetrieverResourceWithRawResponse,
    AsyncRetrieverResourceWithRawResponse,
    RetrieverResourceWithStreamingResponse,
    AsyncRetrieverResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.retriever import Retriever
from ...types.re_rank_config_param import ReRankConfigParam
from ...types.retriever_list_response import RetrieverListResponse
from ...types.composite_retrieval_mode import CompositeRetrievalMode
from ...types.retriever_pipeline_param import RetrieverPipelineParam
from ...types.composite_retrieval_result import CompositeRetrievalResult

__all__ = ["RetrieversResource", "AsyncRetrieversResource"]


class RetrieversResource(SyncAPIResource):
    @cached_property
    def retriever(self) -> RetrieverResource:
        return RetrieverResource(self._client)

    @cached_property
    def with_raw_response(self) -> RetrieversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return RetrieversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RetrieversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return RetrieversResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        pipelines: Iterable[RetrieverPipelineParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Retriever:
        """Create a new Retriever.

        Args:
          name: A name for the retriever tool.

        Will default to the pipeline name if not
              provided.

          pipelines: The pipelines this retriever uses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/retrievers",
            body=maybe_transform(
                {
                    "name": name,
                    "pipelines": pipelines,
                },
                retriever_create_params.RetrieverCreateParams,
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
                    retriever_create_params.RetrieverCreateParams,
                ),
            ),
            cast_to=Retriever,
        )

    def update(
        self,
        retriever_id: str,
        *,
        pipelines: Optional[Iterable[RetrieverPipelineParam]],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Retriever:
        """
        Update an existing Retriever.

        Args:
          pipelines: The pipelines this retriever uses.

          name: A name for the retriever.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not retriever_id:
            raise ValueError(f"Expected a non-empty value for `retriever_id` but received {retriever_id!r}")
        return self._put(
            path_template("/api/v1/retrievers/{retriever_id}", retriever_id=retriever_id),
            body=maybe_transform(
                {
                    "pipelines": pipelines,
                    "name": name,
                },
                retriever_update_params.RetrieverUpdateParams,
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
                    retriever_update_params.RetrieverUpdateParams,
                ),
            ),
            cast_to=Retriever,
        )

    def list(
        self,
        *,
        name: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrieverListResponse:
        """
        List Retrievers for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/retrievers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    retriever_list_params.RetrieverListParams,
                ),
            ),
            cast_to=RetrieverListResponse,
        )

    def delete(
        self,
        retriever_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Retriever by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not retriever_id:
            raise ValueError(f"Expected a non-empty value for `retriever_id` but received {retriever_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/retrievers/{retriever_id}", retriever_id=retriever_id),
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
                    retriever_delete_params.RetrieverDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        retriever_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Retriever:
        """
        Get a Retriever by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not retriever_id:
            raise ValueError(f"Expected a non-empty value for `retriever_id` but received {retriever_id!r}")
        return self._get(
            path_template("/api/v1/retrievers/{retriever_id}", retriever_id=retriever_id),
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
                    retriever_get_params.RetrieverGetParams,
                ),
            ),
            cast_to=Retriever,
        )

    def search(
        self,
        *,
        query: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        mode: CompositeRetrievalMode | Omit = omit,
        pipelines: Iterable[RetrieverPipelineParam] | Omit = omit,
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
        Retrieve data using specified pipelines without creating a persistent retriever.

        Args:
          query: The query to retrieve against.

          mode: The mode of composite retrieval.

          pipelines: The pipelines to use for retrieval.

          rerank_config: The rerank configuration for composite retrieval.

          rerank_top_n: (use rerank_config.top_n instead) The number of nodes to retrieve after
              reranking over retrieved nodes from all retrieval tools.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/retrievers/retrieve",
            body=maybe_transform(
                {
                    "query": query,
                    "mode": mode,
                    "pipelines": pipelines,
                    "rerank_config": rerank_config,
                    "rerank_top_n": rerank_top_n,
                },
                retriever_search_params.RetrieverSearchParams,
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
                    retriever_search_params.RetrieverSearchParams,
                ),
            ),
            cast_to=CompositeRetrievalResult,
        )

    def upsert(
        self,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        pipelines: Iterable[RetrieverPipelineParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Retriever:
        """Upsert a new Retriever.

        Args:
          name: A name for the retriever tool.

        Will default to the pipeline name if not
              provided.

          pipelines: The pipelines this retriever uses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/api/v1/retrievers",
            body=maybe_transform(
                {
                    "name": name,
                    "pipelines": pipelines,
                },
                retriever_upsert_params.RetrieverUpsertParams,
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
                    retriever_upsert_params.RetrieverUpsertParams,
                ),
            ),
            cast_to=Retriever,
        )


class AsyncRetrieversResource(AsyncAPIResource):
    @cached_property
    def retriever(self) -> AsyncRetrieverResource:
        return AsyncRetrieverResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRetrieversResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncRetrieversResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRetrieversResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncRetrieversResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        pipelines: Iterable[RetrieverPipelineParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Retriever:
        """Create a new Retriever.

        Args:
          name: A name for the retriever tool.

        Will default to the pipeline name if not
              provided.

          pipelines: The pipelines this retriever uses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/retrievers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "pipelines": pipelines,
                },
                retriever_create_params.RetrieverCreateParams,
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
                    retriever_create_params.RetrieverCreateParams,
                ),
            ),
            cast_to=Retriever,
        )

    async def update(
        self,
        retriever_id: str,
        *,
        pipelines: Optional[Iterable[RetrieverPipelineParam]],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Retriever:
        """
        Update an existing Retriever.

        Args:
          pipelines: The pipelines this retriever uses.

          name: A name for the retriever.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not retriever_id:
            raise ValueError(f"Expected a non-empty value for `retriever_id` but received {retriever_id!r}")
        return await self._put(
            path_template("/api/v1/retrievers/{retriever_id}", retriever_id=retriever_id),
            body=await async_maybe_transform(
                {
                    "pipelines": pipelines,
                    "name": name,
                },
                retriever_update_params.RetrieverUpdateParams,
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
                    retriever_update_params.RetrieverUpdateParams,
                ),
            ),
            cast_to=Retriever,
        )

    async def list(
        self,
        *,
        name: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RetrieverListResponse:
        """
        List Retrievers for a project.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/retrievers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "name": name,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    retriever_list_params.RetrieverListParams,
                ),
            ),
            cast_to=RetrieverListResponse,
        )

    async def delete(
        self,
        retriever_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Retriever by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not retriever_id:
            raise ValueError(f"Expected a non-empty value for `retriever_id` but received {retriever_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/retrievers/{retriever_id}", retriever_id=retriever_id),
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
                    retriever_delete_params.RetrieverDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        retriever_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Retriever:
        """
        Get a Retriever by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not retriever_id:
            raise ValueError(f"Expected a non-empty value for `retriever_id` but received {retriever_id!r}")
        return await self._get(
            path_template("/api/v1/retrievers/{retriever_id}", retriever_id=retriever_id),
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
                    retriever_get_params.RetrieverGetParams,
                ),
            ),
            cast_to=Retriever,
        )

    async def search(
        self,
        *,
        query: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        mode: CompositeRetrievalMode | Omit = omit,
        pipelines: Iterable[RetrieverPipelineParam] | Omit = omit,
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
        Retrieve data using specified pipelines without creating a persistent retriever.

        Args:
          query: The query to retrieve against.

          mode: The mode of composite retrieval.

          pipelines: The pipelines to use for retrieval.

          rerank_config: The rerank configuration for composite retrieval.

          rerank_top_n: (use rerank_config.top_n instead) The number of nodes to retrieve after
              reranking over retrieved nodes from all retrieval tools.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/retrievers/retrieve",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "mode": mode,
                    "pipelines": pipelines,
                    "rerank_config": rerank_config,
                    "rerank_top_n": rerank_top_n,
                },
                retriever_search_params.RetrieverSearchParams,
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
                    retriever_search_params.RetrieverSearchParams,
                ),
            ),
            cast_to=CompositeRetrievalResult,
        )

    async def upsert(
        self,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        pipelines: Iterable[RetrieverPipelineParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Retriever:
        """Upsert a new Retriever.

        Args:
          name: A name for the retriever tool.

        Will default to the pipeline name if not
              provided.

          pipelines: The pipelines this retriever uses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/api/v1/retrievers",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "pipelines": pipelines,
                },
                retriever_upsert_params.RetrieverUpsertParams,
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
                    retriever_upsert_params.RetrieverUpsertParams,
                ),
            ),
            cast_to=Retriever,
        )


class RetrieversResourceWithRawResponse:
    def __init__(self, retrievers: RetrieversResource) -> None:
        self._retrievers = retrievers

        self.create = to_raw_response_wrapper(
            retrievers.create,
        )
        self.update = to_raw_response_wrapper(
            retrievers.update,
        )
        self.list = to_raw_response_wrapper(
            retrievers.list,
        )
        self.delete = to_raw_response_wrapper(
            retrievers.delete,
        )
        self.get = to_raw_response_wrapper(
            retrievers.get,
        )
        self.search = to_raw_response_wrapper(
            retrievers.search,
        )
        self.upsert = to_raw_response_wrapper(
            retrievers.upsert,
        )

    @cached_property
    def retriever(self) -> RetrieverResourceWithRawResponse:
        return RetrieverResourceWithRawResponse(self._retrievers.retriever)


class AsyncRetrieversResourceWithRawResponse:
    def __init__(self, retrievers: AsyncRetrieversResource) -> None:
        self._retrievers = retrievers

        self.create = async_to_raw_response_wrapper(
            retrievers.create,
        )
        self.update = async_to_raw_response_wrapper(
            retrievers.update,
        )
        self.list = async_to_raw_response_wrapper(
            retrievers.list,
        )
        self.delete = async_to_raw_response_wrapper(
            retrievers.delete,
        )
        self.get = async_to_raw_response_wrapper(
            retrievers.get,
        )
        self.search = async_to_raw_response_wrapper(
            retrievers.search,
        )
        self.upsert = async_to_raw_response_wrapper(
            retrievers.upsert,
        )

    @cached_property
    def retriever(self) -> AsyncRetrieverResourceWithRawResponse:
        return AsyncRetrieverResourceWithRawResponse(self._retrievers.retriever)


class RetrieversResourceWithStreamingResponse:
    def __init__(self, retrievers: RetrieversResource) -> None:
        self._retrievers = retrievers

        self.create = to_streamed_response_wrapper(
            retrievers.create,
        )
        self.update = to_streamed_response_wrapper(
            retrievers.update,
        )
        self.list = to_streamed_response_wrapper(
            retrievers.list,
        )
        self.delete = to_streamed_response_wrapper(
            retrievers.delete,
        )
        self.get = to_streamed_response_wrapper(
            retrievers.get,
        )
        self.search = to_streamed_response_wrapper(
            retrievers.search,
        )
        self.upsert = to_streamed_response_wrapper(
            retrievers.upsert,
        )

    @cached_property
    def retriever(self) -> RetrieverResourceWithStreamingResponse:
        return RetrieverResourceWithStreamingResponse(self._retrievers.retriever)


class AsyncRetrieversResourceWithStreamingResponse:
    def __init__(self, retrievers: AsyncRetrieversResource) -> None:
        self._retrievers = retrievers

        self.create = async_to_streamed_response_wrapper(
            retrievers.create,
        )
        self.update = async_to_streamed_response_wrapper(
            retrievers.update,
        )
        self.list = async_to_streamed_response_wrapper(
            retrievers.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            retrievers.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            retrievers.get,
        )
        self.search = async_to_streamed_response_wrapper(
            retrievers.search,
        )
        self.upsert = async_to_streamed_response_wrapper(
            retrievers.upsert,
        )

    @cached_property
    def retriever(self) -> AsyncRetrieverResourceWithStreamingResponse:
        return AsyncRetrieverResourceWithStreamingResponse(self._retrievers.retriever)
