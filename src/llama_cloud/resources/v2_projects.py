# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import v2_project_get_params, v2_project_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.v2_project_get_response import V2ProjectGetResponse
from ..types.v2_project_list_response import V2ProjectListResponse

__all__ = ["V2ProjectsResource", "AsyncV2ProjectsResource"]


class V2ProjectsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2ProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return V2ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return V2ProjectsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        name: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[V2ProjectListResponse]:
        """List projects in an organization.

        Requires `organization_id` or a project-scoped
        API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/projects",
            page=SyncPaginatedCursor[V2ProjectListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    v2_project_list_params.V2ProjectListParams,
                ),
            ),
            model=V2ProjectListResponse,
        )

    def get(
        self,
        project_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ProjectGetResponse:
        """
        Get a project by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._get(
            path_template("/api/v2/projects/{project_id}", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"organization_id": organization_id}, v2_project_get_params.V2ProjectGetParams),
            ),
            cast_to=V2ProjectGetResponse,
        )


class AsyncV2ProjectsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2ProjectsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ProjectsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ProjectsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncV2ProjectsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        name: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[V2ProjectListResponse, AsyncPaginatedCursor[V2ProjectListResponse]]:
        """List projects in an organization.

        Requires `organization_id` or a project-scoped
        API key.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v2/projects",
            page=AsyncPaginatedCursor[V2ProjectListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "name": name,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                    },
                    v2_project_list_params.V2ProjectListParams,
                ),
            ),
            model=V2ProjectListResponse,
        )

    async def get(
        self,
        project_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ProjectGetResponse:
        """
        Get a project by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._get(
            path_template("/api/v2/projects/{project_id}", project_id=project_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"organization_id": organization_id}, v2_project_get_params.V2ProjectGetParams
                ),
            ),
            cast_to=V2ProjectGetResponse,
        )


class V2ProjectsResourceWithRawResponse:
    def __init__(self, v2_projects: V2ProjectsResource) -> None:
        self._v2_projects = v2_projects

        self.list = to_raw_response_wrapper(
            v2_projects.list,
        )
        self.get = to_raw_response_wrapper(
            v2_projects.get,
        )


class AsyncV2ProjectsResourceWithRawResponse:
    def __init__(self, v2_projects: AsyncV2ProjectsResource) -> None:
        self._v2_projects = v2_projects

        self.list = async_to_raw_response_wrapper(
            v2_projects.list,
        )
        self.get = async_to_raw_response_wrapper(
            v2_projects.get,
        )


class V2ProjectsResourceWithStreamingResponse:
    def __init__(self, v2_projects: V2ProjectsResource) -> None:
        self._v2_projects = v2_projects

        self.list = to_streamed_response_wrapper(
            v2_projects.list,
        )
        self.get = to_streamed_response_wrapper(
            v2_projects.get,
        )


class AsyncV2ProjectsResourceWithStreamingResponse:
    def __init__(self, v2_projects: AsyncV2ProjectsResource) -> None:
        self._v2_projects = v2_projects

        self.list = async_to_streamed_response_wrapper(
            v2_projects.list,
        )
        self.get = async_to_streamed_response_wrapper(
            v2_projects.get,
        )
