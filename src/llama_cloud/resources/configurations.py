# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    configuration_list_params,
    configuration_create_params,
    configuration_delete_params,
    configuration_update_params,
    configuration_retrieve_params,
)
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.configuration_response import ConfigurationResponse

__all__ = ["ConfigurationsResource", "AsyncConfigurationsResource"]


class ConfigurationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return ConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return ConfigurationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        parameters: configuration_create_params.Parameters,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationResponse:
        """
        Create or update a product configuration.

        If a configuration with the same name already exists for this product type and
        project, it will be updated (upsert semantics).

        Args:
          name: Human-readable name for this configuration.

          parameters: Product-specific configuration parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/configurations",
            body=maybe_transform(
                {
                    "name": name,
                    "parameters": parameters,
                },
                configuration_create_params.ConfigurationCreateParams,
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
                    configuration_create_params.ConfigurationCreateParams,
                ),
            ),
            cast_to=ConfigurationResponse,
        )

    def retrieve(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationResponse:
        """
        Get a single product configuration by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return self._get(
            path_template("/api/v1/beta/configurations/{config_id}", config_id=config_id),
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
                    configuration_retrieve_params.ConfigurationRetrieveParams,
                ),
            ),
            cast_to=ConfigurationResponse,
        )

    def update(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        parameters: Optional[configuration_update_params.Parameters] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationResponse:
        """
        Update an existing product configuration.

        Args:
          name: Updated name (omit to leave unchanged).

          parameters: Updated parameters (omit to leave unchanged).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return self._put(
            path_template("/api/v1/beta/configurations/{config_id}", config_id=config_id),
            body=maybe_transform(
                {
                    "name": name,
                    "parameters": parameters,
                },
                configuration_update_params.ConfigurationUpdateParams,
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
                    configuration_update_params.ConfigurationUpdateParams,
                ),
            ),
            cast_to=ConfigurationResponse,
        )

    def list(
        self,
        *,
        latest_only: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        product_type: Optional[
            List[Literal["split_v1", "extract_v2", "classify_v2", "parse_v2", "spreadsheet_v1", "unknown"]]
        ]
        | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[ConfigurationResponse]:
        """
        List product configurations for the current project.

        Args:
          latest_only: Return only the latest version per configuration name.

          name: Filter by configuration name.

          page_size: Number of items per page.

          page_token: Pagination token.

          product_type: Filter by one or more product types. Repeat the parameter for multiple values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/configurations",
            page=SyncPaginatedCursor[ConfigurationResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "latest_only": latest_only,
                        "name": name,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "product_type": product_type,
                        "project_id": project_id,
                    },
                    configuration_list_params.ConfigurationListParams,
                ),
            ),
            model=ConfigurationResponse,
        )

    def delete(
        self,
        config_id: str,
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
        Delete a product configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/api/v1/beta/configurations/{config_id}", config_id=config_id),
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
                    configuration_delete_params.ConfigurationDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncConfigurationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncConfigurationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        parameters: configuration_create_params.Parameters,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationResponse:
        """
        Create or update a product configuration.

        If a configuration with the same name already exists for this product type and
        project, it will be updated (upsert semantics).

        Args:
          name: Human-readable name for this configuration.

          parameters: Product-specific configuration parameters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/configurations",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parameters": parameters,
                },
                configuration_create_params.ConfigurationCreateParams,
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
                    configuration_create_params.ConfigurationCreateParams,
                ),
            ),
            cast_to=ConfigurationResponse,
        )

    async def retrieve(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationResponse:
        """
        Get a single product configuration by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return await self._get(
            path_template("/api/v1/beta/configurations/{config_id}", config_id=config_id),
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
                    configuration_retrieve_params.ConfigurationRetrieveParams,
                ),
            ),
            cast_to=ConfigurationResponse,
        )

    async def update(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        parameters: Optional[configuration_update_params.Parameters] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationResponse:
        """
        Update an existing product configuration.

        Args:
          name: Updated name (omit to leave unchanged).

          parameters: Updated parameters (omit to leave unchanged).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return await self._put(
            path_template("/api/v1/beta/configurations/{config_id}", config_id=config_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parameters": parameters,
                },
                configuration_update_params.ConfigurationUpdateParams,
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
                    configuration_update_params.ConfigurationUpdateParams,
                ),
            ),
            cast_to=ConfigurationResponse,
        )

    def list(
        self,
        *,
        latest_only: bool | Omit = omit,
        name: Optional[str] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        product_type: Optional[
            List[Literal["split_v1", "extract_v2", "classify_v2", "parse_v2", "spreadsheet_v1", "unknown"]]
        ]
        | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ConfigurationResponse, AsyncPaginatedCursor[ConfigurationResponse]]:
        """
        List product configurations for the current project.

        Args:
          latest_only: Return only the latest version per configuration name.

          name: Filter by configuration name.

          page_size: Number of items per page.

          page_token: Pagination token.

          product_type: Filter by one or more product types. Repeat the parameter for multiple values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/beta/configurations",
            page=AsyncPaginatedCursor[ConfigurationResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "latest_only": latest_only,
                        "name": name,
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "product_type": product_type,
                        "project_id": project_id,
                    },
                    configuration_list_params.ConfigurationListParams,
                ),
            ),
            model=ConfigurationResponse,
        )

    async def delete(
        self,
        config_id: str,
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
        Delete a product configuration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/api/v1/beta/configurations/{config_id}", config_id=config_id),
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
                    configuration_delete_params.ConfigurationDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class ConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = to_raw_response_wrapper(
            configurations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            configurations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            configurations.update,
        )
        self.list = to_raw_response_wrapper(
            configurations.list,
        )
        self.delete = to_raw_response_wrapper(
            configurations.delete,
        )


class AsyncConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = async_to_raw_response_wrapper(
            configurations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            configurations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            configurations.update,
        )
        self.list = async_to_raw_response_wrapper(
            configurations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            configurations.delete,
        )


class ConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = to_streamed_response_wrapper(
            configurations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            configurations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            configurations.update,
        )
        self.list = to_streamed_response_wrapper(
            configurations.list,
        )
        self.delete = to_streamed_response_wrapper(
            configurations.delete,
        )


class AsyncConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = async_to_streamed_response_wrapper(
            configurations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            configurations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            configurations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            configurations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            configurations.delete,
        )
