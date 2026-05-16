# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Mapping, Optional, cast
from datetime import datetime

import httpx

from ...._files import deepcopy_with_paths
from ...._types import (
    Body,
    Omit,
    Query,
    Headers,
    NoneType,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ...._utils import extract_files, path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from ...._base_client import AsyncPaginator, make_request_options
from ....types.beta.directories import (
    file_add_params,
    file_get_params,
    file_list_params,
    file_delete_params,
    file_update_params,
    file_upload_params,
)
from ....types.beta.directories.file_add_response import FileAddResponse
from ....types.beta.directories.file_get_response import FileGetResponse
from ....types.beta.directories.file_list_response import FileListResponse
from ....types.beta.directories.file_update_response import FileUpdateResponse
from ....types.beta.directories.file_upload_response import FileUploadResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def update(
        self,
        directory_file_id: str,
        *,
        path_directory_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        body_directory_id: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool, SequenceNotStr[str], None]]] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpdateResponse:
        """
        Update file metadata within the specified directory.

        Supports moving files to a different directory by setting directory_id.

        Note: This endpoint uses directory_file_id (the internal ID). If you're trying
        to update a file by its unique_id, use the list endpoint with a filter to find
        the directory_file_id first.

        Args:
          body_directory_id: Move file to a different directory.

          display_name: Updated display name.

          metadata: User-defined metadata key-value pairs. Replaces the user metadata layer.

          unique_id: Updated unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_directory_id:
            raise ValueError(f"Expected a non-empty value for `path_directory_id` but received {path_directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        return self._patch(
            path_template(
                "/api/v1/beta/directories/{path_directory_id}/files/{directory_file_id}",
                path_directory_id=path_directory_id,
                directory_file_id=directory_file_id,
            ),
            body=maybe_transform(
                {
                    "body_directory_id": body_directory_id,
                    "display_name": display_name,
                    "metadata": metadata,
                    "unique_id": unique_id,
                },
                file_update_params.FileUpdateParams,
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
                    file_update_params.FileUpdateParams,
                ),
            ),
            cast_to=FileUpdateResponse,
        )

    def list(
        self,
        directory_id: str,
        *,
        display_name: Optional[str] | Omit = omit,
        display_name_contains: Optional[str] | Omit = omit,
        expand: Optional[SequenceNotStr[str]] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        include_deleted: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        updated_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        updated_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[FileListResponse]:
        """
        List all files within the specified directory with optional filtering and
        pagination.

        Args:
          expand: Fields to expand on each directory file.

          updated_at_on_or_after: Include items updated at or after this timestamp (inclusive)

          updated_at_on_or_before: Include items updated at or before this timestamp (inclusive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return self._get_api_list(
            path_template("/api/v1/beta/directories/{directory_id}/files", directory_id=directory_id),
            page=SyncPaginatedCursor[FileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "display_name": display_name,
                        "display_name_contains": display_name_contains,
                        "expand": expand,
                        "file_id": file_id,
                        "include_deleted": include_deleted,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "unique_id": unique_id,
                        "updated_at_on_or_after": updated_at_on_or_after,
                        "updated_at_on_or_before": updated_at_on_or_before,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=FileListResponse,
        )

    def delete(
        self,
        directory_file_id: str,
        *,
        directory_id: str,
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
        Delete a file from the specified directory.

        Note: This endpoint uses directory_file_id (the internal ID). If you're trying
        to delete a file by its unique_id, use the list endpoint with a filter to find
        the directory_file_id first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/api/v1/beta/directories/{directory_id}/files/{directory_file_id}",
                directory_id=directory_id,
                directory_file_id=directory_file_id,
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
                    file_delete_params.FileDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    def add(
        self,
        directory_id: str,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool, SequenceNotStr[str], None]]] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileAddResponse:
        """
        Create a new file within the specified directory.

        The directory must exist and belong to the project passed in. The file_id must
        be provided and exist in the project.

        Args:
          file_id: File ID for the storage location (required).

          display_name: Display name for the file. If not provided, will use the file's name.

          metadata: User-defined metadata key-value pairs to associate with the file.

          unique_id: Unique identifier for the file in the directory. If not provided, will use the
              file's external_file_id or name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return self._post(
            path_template("/api/v1/beta/directories/{directory_id}/files", directory_id=directory_id),
            body=maybe_transform(
                {
                    "file_id": file_id,
                    "display_name": display_name,
                    "metadata": metadata,
                    "unique_id": unique_id,
                },
                file_add_params.FileAddParams,
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
                    file_add_params.FileAddParams,
                ),
            ),
            cast_to=FileAddResponse,
        )

    def get(
        self,
        directory_file_id: str,
        *,
        directory_id: str,
        expand: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileGetResponse:
        """Get a file by its directory_file_id within the specified directory.

        If you're
        trying to get a file by its unique_id, use the list endpoint with a filter
        instead.

        Args:
          expand: Fields to expand.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        return self._get(
            path_template(
                "/api/v1/beta/directories/{directory_id}/files/{directory_file_id}",
                directory_id=directory_id,
                directory_file_id=directory_file_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "expand": expand,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_get_params.FileGetParams,
                ),
            ),
            cast_to=FileGetResponse,
        )

    def upload(
        self,
        directory_id: str,
        *,
        upload_file: FileTypes,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        external_file_id: Optional[str] | Omit = omit,
        metadata: Optional[str] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUploadResponse:
        """
        Upload a file directly to a directory.

        Uploads a file and creates a directory file entry in a single operation. If
        unique_id or display_name are not provided, they will be derived from the file
        metadata.

        Args:
          metadata: User metadata as a JSON object string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        body = deepcopy_with_paths(
            {
                "upload_file": upload_file,
                "display_name": display_name,
                "external_file_id": external_file_id,
                "metadata": metadata,
                "unique_id": unique_id,
            },
            [["upload_file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["upload_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            path_template("/api/v1/beta/directories/{directory_id}/files/upload", directory_id=directory_id),
            body=maybe_transform(body, file_upload_params.FileUploadParams),
            files=files,
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
                    file_upload_params.FileUploadParams,
                ),
            ),
            cast_to=FileUploadResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def update(
        self,
        directory_file_id: str,
        *,
        path_directory_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        body_directory_id: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool, SequenceNotStr[str], None]]] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpdateResponse:
        """
        Update file metadata within the specified directory.

        Supports moving files to a different directory by setting directory_id.

        Note: This endpoint uses directory_file_id (the internal ID). If you're trying
        to update a file by its unique_id, use the list endpoint with a filter to find
        the directory_file_id first.

        Args:
          body_directory_id: Move file to a different directory.

          display_name: Updated display name.

          metadata: User-defined metadata key-value pairs. Replaces the user metadata layer.

          unique_id: Updated unique identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_directory_id:
            raise ValueError(f"Expected a non-empty value for `path_directory_id` but received {path_directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        return await self._patch(
            path_template(
                "/api/v1/beta/directories/{path_directory_id}/files/{directory_file_id}",
                path_directory_id=path_directory_id,
                directory_file_id=directory_file_id,
            ),
            body=await async_maybe_transform(
                {
                    "body_directory_id": body_directory_id,
                    "display_name": display_name,
                    "metadata": metadata,
                    "unique_id": unique_id,
                },
                file_update_params.FileUpdateParams,
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
                    file_update_params.FileUpdateParams,
                ),
            ),
            cast_to=FileUpdateResponse,
        )

    def list(
        self,
        directory_id: str,
        *,
        display_name: Optional[str] | Omit = omit,
        display_name_contains: Optional[str] | Omit = omit,
        expand: Optional[SequenceNotStr[str]] | Omit = omit,
        file_id: Optional[str] | Omit = omit,
        include_deleted: bool | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        updated_at_on_or_after: Union[str, datetime, None] | Omit = omit,
        updated_at_on_or_before: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[FileListResponse, AsyncPaginatedCursor[FileListResponse]]:
        """
        List all files within the specified directory with optional filtering and
        pagination.

        Args:
          expand: Fields to expand on each directory file.

          updated_at_on_or_after: Include items updated at or after this timestamp (inclusive)

          updated_at_on_or_before: Include items updated at or before this timestamp (inclusive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return self._get_api_list(
            path_template("/api/v1/beta/directories/{directory_id}/files", directory_id=directory_id),
            page=AsyncPaginatedCursor[FileListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "display_name": display_name,
                        "display_name_contains": display_name_contains,
                        "expand": expand,
                        "file_id": file_id,
                        "include_deleted": include_deleted,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                        "unique_id": unique_id,
                        "updated_at_on_or_after": updated_at_on_or_after,
                        "updated_at_on_or_before": updated_at_on_or_before,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            model=FileListResponse,
        )

    async def delete(
        self,
        directory_file_id: str,
        *,
        directory_id: str,
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
        Delete a file from the specified directory.

        Note: This endpoint uses directory_file_id (the internal ID). If you're trying
        to delete a file by its unique_id, use the list endpoint with a filter to find
        the directory_file_id first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/api/v1/beta/directories/{directory_id}/files/{directory_file_id}",
                directory_id=directory_id,
                directory_file_id=directory_file_id,
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
                    file_delete_params.FileDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def add(
        self,
        directory_id: str,
        *,
        file_id: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        metadata: Optional[Dict[str, Union[str, float, bool, SequenceNotStr[str], None]]] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileAddResponse:
        """
        Create a new file within the specified directory.

        The directory must exist and belong to the project passed in. The file_id must
        be provided and exist in the project.

        Args:
          file_id: File ID for the storage location (required).

          display_name: Display name for the file. If not provided, will use the file's name.

          metadata: User-defined metadata key-value pairs to associate with the file.

          unique_id: Unique identifier for the file in the directory. If not provided, will use the
              file's external_file_id or name.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        return await self._post(
            path_template("/api/v1/beta/directories/{directory_id}/files", directory_id=directory_id),
            body=await async_maybe_transform(
                {
                    "file_id": file_id,
                    "display_name": display_name,
                    "metadata": metadata,
                    "unique_id": unique_id,
                },
                file_add_params.FileAddParams,
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
                    file_add_params.FileAddParams,
                ),
            ),
            cast_to=FileAddResponse,
        )

    async def get(
        self,
        directory_file_id: str,
        *,
        directory_id: str,
        expand: Optional[SequenceNotStr[str]] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileGetResponse:
        """Get a file by its directory_file_id within the specified directory.

        If you're
        trying to get a file by its unique_id, use the list endpoint with a filter
        instead.

        Args:
          expand: Fields to expand.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        if not directory_file_id:
            raise ValueError(f"Expected a non-empty value for `directory_file_id` but received {directory_file_id!r}")
        return await self._get(
            path_template(
                "/api/v1/beta/directories/{directory_id}/files/{directory_file_id}",
                directory_id=directory_id,
                directory_file_id=directory_file_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "expand": expand,
                        "organization_id": organization_id,
                        "project_id": project_id,
                    },
                    file_get_params.FileGetParams,
                ),
            ),
            cast_to=FileGetResponse,
        )

    async def upload(
        self,
        directory_id: str,
        *,
        upload_file: FileTypes,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        display_name: Optional[str] | Omit = omit,
        external_file_id: Optional[str] | Omit = omit,
        metadata: Optional[str] | Omit = omit,
        unique_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUploadResponse:
        """
        Upload a file directly to a directory.

        Uploads a file and creates a directory file entry in a single operation. If
        unique_id or display_name are not provided, they will be derived from the file
        metadata.

        Args:
          metadata: User metadata as a JSON object string.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not directory_id:
            raise ValueError(f"Expected a non-empty value for `directory_id` but received {directory_id!r}")
        body = deepcopy_with_paths(
            {
                "upload_file": upload_file,
                "display_name": display_name,
                "external_file_id": external_file_id,
                "metadata": metadata,
                "unique_id": unique_id,
            },
            [["upload_file"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["upload_file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            path_template("/api/v1/beta/directories/{directory_id}/files/upload", directory_id=directory_id),
            body=await async_maybe_transform(body, file_upload_params.FileUploadParams),
            files=files,
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
                    file_upload_params.FileUploadParams,
                ),
            ),
            cast_to=FileUploadResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.update = to_raw_response_wrapper(
            files.update,
        )
        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.add = to_raw_response_wrapper(
            files.add,
        )
        self.get = to_raw_response_wrapper(
            files.get,
        )
        self.upload = to_raw_response_wrapper(
            files.upload,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.update = async_to_raw_response_wrapper(
            files.update,
        )
        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.add = async_to_raw_response_wrapper(
            files.add,
        )
        self.get = async_to_raw_response_wrapper(
            files.get,
        )
        self.upload = async_to_raw_response_wrapper(
            files.upload,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.update = to_streamed_response_wrapper(
            files.update,
        )
        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.add = to_streamed_response_wrapper(
            files.add,
        )
        self.get = to_streamed_response_wrapper(
            files.get,
        )
        self.upload = to_streamed_response_wrapper(
            files.upload,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.update = async_to_streamed_response_wrapper(
            files.update,
        )
        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            files.add,
        )
        self.get = async_to_streamed_response_wrapper(
            files.get,
        )
        self.upload = async_to_streamed_response_wrapper(
            files.upload,
        )
