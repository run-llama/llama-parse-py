# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPaginatedCloudDocuments, AsyncPaginatedCloudDocuments
from ..._base_client import AsyncPaginator, make_request_options
from ...types.pipelines import (
    document_list_params,
    document_get_status_counts_params,
)
from ...types.pipelines.cloud_document import CloudDocument
from ...types.managed_ingestion_status_response import ManagedIngestionStatusResponse
from ...types.pipelines.document_create_response import DocumentCreateResponse
from ...types.pipelines.document_upsert_response import DocumentUpsertResponse
from ...types.pipelines.cloud_document_create_param import CloudDocumentCreateParam
from ...types.pipelines.document_get_chunks_response import DocumentGetChunksResponse
from ...types.pipelines.document_get_status_counts_response import DocumentGetStatusCountsResponse

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return DocumentsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    def create(
        self,
        pipeline_id: str,
        *,
        body: Iterable[CloudDocumentCreateParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateResponse:
        """
        Batch create documents for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._post(
            path_template("/api/v1/pipelines/{pipeline_id}/documents", pipeline_id=pipeline_id),
            body=maybe_transform(body, Iterable[CloudDocumentCreateParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        pipeline_id: str,
        *,
        file_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        only_api_data_source_documents: Optional[bool] | Omit = omit,
        only_direct_upload: Optional[bool] | Omit = omit,
        skip: int | Omit = omit,
        status_refresh_policy: Literal["cached", "ttl"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCloudDocuments[CloudDocument]:
        """
        Return a list of documents for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get_api_list(
            path_template("/api/v1/pipelines/{pipeline_id}/documents/paginated", pipeline_id=pipeline_id),
            page=SyncPaginatedCloudDocuments[CloudDocument],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "file_id": file_id,
                        "limit": limit,
                        "only_api_data_source_documents": only_api_data_source_documents,
                        "only_direct_upload": only_direct_upload,
                        "skip": skip,
                        "status_refresh_policy": status_refresh_policy,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=CloudDocument,
        )

    @typing_extensions.deprecated("deprecated")
    def delete(
        self,
        document_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a document from a pipeline; runs async (vectors first, then MongoDB
        record).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/documents/{document_id}",
                pipeline_id=pipeline_id,
                document_id=document_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    def get(
        self,
        document_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloudDocument:
        """
        Return a single document for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/documents/{document_id}",
                pipeline_id=pipeline_id,
                document_id=document_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudDocument,
        )

    @typing_extensions.deprecated("deprecated")
    def get_chunks(
        self,
        document_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGetChunksResponse:
        """
        Return a list of chunks for a pipeline document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/documents/{document_id}/chunks",
                pipeline_id=pipeline_id,
                document_id=document_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetChunksResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def get_status(
        self,
        document_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedIngestionStatusResponse:
        """
        Return a single document for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/documents/{document_id}/status",
                pipeline_id=pipeline_id,
                document_id=document_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedIngestionStatusResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def get_status_counts(
        self,
        pipeline_id: str,
        *,
        data_source_id: Optional[str] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        only_direct_upload: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGetStatusCountsResponse:
        """
        Count the documents in a pipeline, grouped by ingestion status.

        Counts reflect each document's last recorded status rather than a freshly
        computed one, so a document that changed status in the last few moments may
        still be counted under its previous one. Use
        `GET /pipelines/{pipeline_id}/documents/{document_id}/status` when a single
        document's status has to be up to the moment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get(
            path_template("/api/v1/pipelines/{pipeline_id}/documents/status-counts", pipeline_id=pipeline_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "data_source_id": data_source_id,
                        "file_id": file_id,
                        "only_direct_upload": only_direct_upload,
                    },
                    document_get_status_counts_params.DocumentGetStatusCountsParams,
                ),
            ),
            cast_to=DocumentGetStatusCountsResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def sync(
        self,
        document_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Sync a specific document for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._post(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync",
                pipeline_id=pipeline_id,
                document_id=document_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @typing_extensions.deprecated("deprecated")
    def upsert(
        self,
        pipeline_id: str,
        *,
        body: Iterable[CloudDocumentCreateParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpsertResponse:
        """
        Batch create or update a document for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._put(
            path_template("/api/v1/pipelines/{pipeline_id}/documents", pipeline_id=pipeline_id),
            body=maybe_transform(body, Iterable[CloudDocumentCreateParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpsertResponse,
        )


class AsyncDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncDocumentsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("deprecated")
    async def create(
        self,
        pipeline_id: str,
        *,
        body: Iterable[CloudDocumentCreateParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateResponse:
        """
        Batch create documents for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._post(
            path_template("/api/v1/pipelines/{pipeline_id}/documents", pipeline_id=pipeline_id),
            body=await async_maybe_transform(body, Iterable[CloudDocumentCreateParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateResponse,
        )

    @typing_extensions.deprecated("deprecated")
    def list(
        self,
        pipeline_id: str,
        *,
        file_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        only_api_data_source_documents: Optional[bool] | Omit = omit,
        only_direct_upload: Optional[bool] | Omit = omit,
        skip: int | Omit = omit,
        status_refresh_policy: Literal["cached", "ttl"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[CloudDocument, AsyncPaginatedCloudDocuments[CloudDocument]]:
        """
        Return a list of documents for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return self._get_api_list(
            path_template("/api/v1/pipelines/{pipeline_id}/documents/paginated", pipeline_id=pipeline_id),
            page=AsyncPaginatedCloudDocuments[CloudDocument],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "file_id": file_id,
                        "limit": limit,
                        "only_api_data_source_documents": only_api_data_source_documents,
                        "only_direct_upload": only_direct_upload,
                        "skip": skip,
                        "status_refresh_policy": status_refresh_policy,
                    },
                    document_list_params.DocumentListParams,
                ),
            ),
            model=CloudDocument,
        )

    @typing_extensions.deprecated("deprecated")
    async def delete(
        self,
        document_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a document from a pipeline; runs async (vectors first, then MongoDB
        record).

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/documents/{document_id}",
                pipeline_id=pipeline_id,
                document_id=document_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    @typing_extensions.deprecated("deprecated")
    async def get(
        self,
        document_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CloudDocument:
        """
        Return a single document for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/documents/{document_id}",
                pipeline_id=pipeline_id,
                document_id=document_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CloudDocument,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_chunks(
        self,
        document_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGetChunksResponse:
        """
        Return a list of chunks for a pipeline document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/documents/{document_id}/chunks",
                pipeline_id=pipeline_id,
                document_id=document_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetChunksResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_status(
        self,
        document_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ManagedIngestionStatusResponse:
        """
        Return a single document for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/documents/{document_id}/status",
                pipeline_id=pipeline_id,
                document_id=document_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ManagedIngestionStatusResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def get_status_counts(
        self,
        pipeline_id: str,
        *,
        data_source_id: Optional[str] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        only_direct_upload: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGetStatusCountsResponse:
        """
        Count the documents in a pipeline, grouped by ingestion status.

        Counts reflect each document's last recorded status rather than a freshly
        computed one, so a document that changed status in the last few moments may
        still be counted under its previous one. Use
        `GET /pipelines/{pipeline_id}/documents/{document_id}/status` when a single
        document's status has to be up to the moment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._get(
            path_template("/api/v1/pipelines/{pipeline_id}/documents/status-counts", pipeline_id=pipeline_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "data_source_id": data_source_id,
                        "file_id": file_id,
                        "only_direct_upload": only_direct_upload,
                    },
                    document_get_status_counts_params.DocumentGetStatusCountsParams,
                ),
            ),
            cast_to=DocumentGetStatusCountsResponse,
        )

    @typing_extensions.deprecated("deprecated")
    async def sync(
        self,
        document_id: str,
        *,
        pipeline_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Sync a specific document for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._post(
            path_template(
                "/api/v1/pipelines/{pipeline_id}/documents/{document_id}/sync",
                pipeline_id=pipeline_id,
                document_id=document_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    @typing_extensions.deprecated("deprecated")
    async def upsert(
        self,
        pipeline_id: str,
        *,
        body: Iterable[CloudDocumentCreateParam],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpsertResponse:
        """
        Batch create or update a document for a pipeline.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not pipeline_id:
            raise ValueError(f"Expected a non-empty value for `pipeline_id` but received {pipeline_id!r}")
        return await self._put(
            path_template("/api/v1/pipelines/{pipeline_id}/documents", pipeline_id=pipeline_id),
            body=await async_maybe_transform(body, Iterable[CloudDocumentCreateParam]),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpsertResponse,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                documents.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                documents.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                documents.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                documents.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_chunks = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                documents.get_chunks,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_status = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                documents.get_status,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_status_counts = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                documents.get_status_counts,  # pyright: ignore[reportDeprecated],
            )
        )
        self.sync = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                documents.sync,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upsert = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                documents.upsert,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                documents.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                documents.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                documents.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                documents.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_chunks = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                documents.get_chunks,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_status = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                documents.get_status,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_status_counts = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                documents.get_status_counts,  # pyright: ignore[reportDeprecated],
            )
        )
        self.sync = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                documents.sync,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upsert = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                documents.upsert,  # pyright: ignore[reportDeprecated],
            )
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                documents.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                documents.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                documents.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                documents.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_chunks = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                documents.get_chunks,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_status = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                documents.get_status,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_status_counts = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                documents.get_status_counts,  # pyright: ignore[reportDeprecated],
            )
        )
        self.sync = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                documents.sync,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upsert = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                documents.upsert,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                documents.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                documents.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.delete = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                documents.delete,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                documents.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_chunks = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                documents.get_chunks,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_status = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                documents.get_status,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_status_counts = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                documents.get_status_counts,  # pyright: ignore[reportDeprecated],
            )
        )
        self.sync = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                documents.sync,  # pyright: ignore[reportDeprecated],
            )
        )
        self.upsert = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                documents.upsert,  # pyright: ignore[reportDeprecated],
            )
        )
