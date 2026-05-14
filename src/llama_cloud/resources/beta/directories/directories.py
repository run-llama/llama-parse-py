# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from ....types.beta import (
    directory_get_params,
    directory_list_params,
    directory_create_params,
    directory_delete_params,
    directory_update_params,
)
from ...._base_client import AsyncPaginator, make_request_options
from ....types.beta.directory_get_response import DirectoryGetResponse
from ....types.beta.directory_list_response import DirectoryListResponse
from ....types.beta.directory_create_response import DirectoryCreateResponse
from ....types.beta.directory_update_response import DirectoryUpdateResponse

__all__ = ["DirectoriesResource", "AsyncDirectoriesResource"]


class DirectoriesResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> DirectoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return DirectoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return DirectoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryCreateResponse:
        """
        Create a new directory within the specified project.

        Args:
          name: Human-readable name for the directory.

          description: Optional description shown to users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/directories",
            body=maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                directory_create_params.DirectoryCreateParams,
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
                    directory_create_params.DirectoryCreateParams,
                ),
            ),
            cast_to=DirectoryCreateResponse,
        )

    def update(
        self,
        directory_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryUpdateResponse:
        """
        Update directory metadata.

        Args:
          description: Updated description for the directory.

          name: Updated name for the directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return self._patch(
            path_template("/api/v1/beta/directories/{directory_id}", directory_id=directory_id),
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                directory_update_params.DirectoryUpdateParams,
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
                    directory_update_params.DirectoryUpdateParams,
                ),
            ),
            cast_to=DirectoryUpdateResponse,
        )

    def list(
        self,
        *,
        include_deleted: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        type: Optional[Literal["user", "index"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[DirectoryListResponse]:
        """
        List Directories

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/directories",
            page=SyncPaginatedCursor[DirectoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_deleted": include_deleted,
                        "name": name,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "type": type,
                    },
                    directory_list_params.DirectoryListParams,
                ),
            ),
            model=DirectoryListResponse,
        )

    def delete(
        self,
        directory_id: str,
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
        Permanently delete a directory.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/beta/directories/{directory_id}", directory_id=directory_id),
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
                    directory_delete_params.DirectoryDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        directory_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryGetResponse:
        """
        Retrieve a directory by its identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return self._get(
            path_template("/api/v1/beta/directories/{directory_id}", directory_id=directory_id),
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
                    directory_get_params.DirectoryGetParams,
                ),
            ),
            cast_to=DirectoryGetResponse,
        )


class AsyncDirectoriesResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDirectoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncDirectoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncDirectoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryCreateResponse:
        """
        Create a new directory within the specified project.

        Args:
          name: Human-readable name for the directory.

          description: Optional description shown to users.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/directories",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "description": description,
                },
                directory_create_params.DirectoryCreateParams,
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
                    directory_create_params.DirectoryCreateParams,
                ),
            ),
            cast_to=DirectoryCreateResponse,
        )

    async def update(
        self,
        directory_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        description: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryUpdateResponse:
        """
        Update directory metadata.

        Args:
          description: Updated description for the directory.

          name: Updated name for the directory.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return await self._patch(
            path_template("/api/v1/beta/directories/{directory_id}", directory_id=directory_id),
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                },
                directory_update_params.DirectoryUpdateParams,
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
                    directory_update_params.DirectoryUpdateParams,
                ),
            ),
            cast_to=DirectoryUpdateResponse,
        )

    def list(
        self,
        *,
        include_deleted: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        type: Optional[Literal["user", "index"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[DirectoryListResponse, AsyncPaginatedCursor[DirectoryListResponse]]:
        """
        List Directories

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/directories",
            page=AsyncPaginatedCursor[DirectoryListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_deleted": include_deleted,
                        "name": name,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "type": type,
                    },
                    directory_list_params.DirectoryListParams,
                ),
            ),
            model=DirectoryListResponse,
        )

    async def delete(
        self,
        directory_id: str,
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
        Permanently delete a directory.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/beta/directories/{directory_id}", directory_id=directory_id),
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
                    directory_delete_params.DirectoryDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        directory_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryGetResponse:
        """
        Retrieve a directory by its identifier.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return await self._get(
            path_template("/api/v1/beta/directories/{directory_id}", directory_id=directory_id),
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
                    directory_get_params.DirectoryGetParams,
                ),
            ),
            cast_to=DirectoryGetResponse,
        )


class DirectoriesResourceWithRawResponse:
    def __init__(self, directories: DirectoriesResource) -> None:
        self._directories = directories

        self.create = to_raw_response_wrapper(
            directories.create,
        )
        self.update = to_raw_response_wrapper(
            directories.update,
        )
        self.list = to_raw_response_wrapper(
            directories.list,
        )
        self.delete = to_raw_response_wrapper(
            directories.delete,
        )
        self.get = to_raw_response_wrapper(
            directories.get,
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._directories.files)


class AsyncDirectoriesResourceWithRawResponse:
    def __init__(self, directories: AsyncDirectoriesResource) -> None:
        self._directories = directories

        self.create = async_to_raw_response_wrapper(
            directories.create,
        )
        self.update = async_to_raw_response_wrapper(
            directories.update,
        )
        self.list = async_to_raw_response_wrapper(
            directories.list,
        )
        self.delete = async_to_raw_response_wrapper(
            directories.delete,
        )
        self.get = async_to_raw_response_wrapper(
            directories.get,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._directories.files)


class DirectoriesResourceWithStreamingResponse:
    def __init__(self, directories: DirectoriesResource) -> None:
        self._directories = directories

        self.create = to_streamed_response_wrapper(
            directories.create,
        )
        self.update = to_streamed_response_wrapper(
            directories.update,
        )
        self.list = to_streamed_response_wrapper(
            directories.list,
        )
        self.delete = to_streamed_response_wrapper(
            directories.delete,
        )
        self.get = to_streamed_response_wrapper(
            directories.get,
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._directories.files)


class AsyncDirectoriesResourceWithStreamingResponse:
    def __init__(self, directories: AsyncDirectoriesResource) -> None:
        self._directories = directories

        self.create = async_to_streamed_response_wrapper(
            directories.create,
        )
        self.update = async_to_streamed_response_wrapper(
            directories.update,
        )
        self.list = async_to_streamed_response_wrapper(
            directories.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            directories.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            directories.get,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._directories.files)
