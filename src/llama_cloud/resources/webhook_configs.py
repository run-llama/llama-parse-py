# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    webhook_config_list_params,
    webhook_config_create_params,
    webhook_config_delete_params,
    webhook_config_update_params,
    webhook_config_retrieve_params,
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
from .._base_client import make_request_options
from ..types.webhook_config_response import WebhookConfigResponse
from ..types.webhook_config_list_response import WebhookConfigListResponse

__all__ = ["WebhookConfigsResource", "AsyncWebhookConfigsResource"]


class WebhookConfigsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebhookConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return WebhookConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhookConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return WebhookConfigsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        webhook_url: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        webhook_events: Optional[
            List[
                Literal[
                    "batch.cancelled",
                    "batch.error",
                    "batch.pending",
                    "batch.running",
                    "batch.success",
                    "classify.cancelled",
                    "classify.error",
                    "classify.partial_success",
                    "classify.pending",
                    "classify.running",
                    "classify.success",
                    "extract.cancelled",
                    "extract.error",
                    "extract.partial_success",
                    "extract.pending",
                    "extract.success",
                    "parse.cancelled",
                    "parse.error",
                    "parse.partial_success",
                    "parse.pending",
                    "parse.running",
                    "parse.success",
                    "sheets.cancelled",
                    "sheets.error",
                    "sheets.partial_success",
                    "sheets.pending",
                    "sheets.success",
                    "split.cancelled",
                    "split.error",
                    "split.pending",
                    "split.processing",
                    "split.success",
                    "unmapped_event",
                ]
            ]
        ]
        | Omit = omit,
        webhook_headers: Optional[Dict[str, str]] | Omit = omit,
        webhook_output_format: Optional[Literal["json", "string"]] | Omit = omit,
        webhook_signing_secret: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookConfigResponse:
        """
        Create a reusable webhook configuration for the current project.

        Args:
          webhook_url: URL to receive webhook POST notifications.

          webhook_events: Events to subscribe to. If null, all events are delivered.

          webhook_headers: Custom HTTP headers sent with each webhook request.

          webhook_output_format: Response format sent to the webhook: 'string' (default) or 'json'.

          webhook_signing_secret: Shared secret used to sign deliveries to this endpoint. Write-only: it is never
              returned in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/beta/webhook-configs",
            body=maybe_transform(
                {
                    "webhook_url": webhook_url,
                    "webhook_events": webhook_events,
                    "webhook_headers": webhook_headers,
                    "webhook_output_format": webhook_output_format,
                    "webhook_signing_secret": webhook_signing_secret,
                },
                webhook_config_create_params.WebhookConfigCreateParams,
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
                    webhook_config_create_params.WebhookConfigCreateParams,
                ),
            ),
            cast_to=WebhookConfigResponse,
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
    ) -> WebhookConfigResponse:
        """
        Get a single webhook configuration by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return self._get(
            path_template("/api/v1/beta/webhook-configs/{config_id}", config_id=config_id),
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
                    webhook_config_retrieve_params.WebhookConfigRetrieveParams,
                ),
            ),
            cast_to=WebhookConfigResponse,
        )

    def update(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        webhook_events: Optional[
            List[
                Literal[
                    "batch.cancelled",
                    "batch.error",
                    "batch.pending",
                    "batch.running",
                    "batch.success",
                    "classify.cancelled",
                    "classify.error",
                    "classify.partial_success",
                    "classify.pending",
                    "classify.running",
                    "classify.success",
                    "extract.cancelled",
                    "extract.error",
                    "extract.partial_success",
                    "extract.pending",
                    "extract.success",
                    "parse.cancelled",
                    "parse.error",
                    "parse.partial_success",
                    "parse.pending",
                    "parse.running",
                    "parse.success",
                    "sheets.cancelled",
                    "sheets.error",
                    "sheets.partial_success",
                    "sheets.pending",
                    "sheets.success",
                    "split.cancelled",
                    "split.error",
                    "split.pending",
                    "split.processing",
                    "split.success",
                    "unmapped_event",
                ]
            ]
        ]
        | Omit = omit,
        webhook_headers: Optional[Dict[str, str]] | Omit = omit,
        webhook_output_format: Optional[Literal["json", "string"]] | Omit = omit,
        webhook_signing_secret: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookConfigResponse:
        """Update a webhook configuration.

        Only fields present in the request change.

        Args:
          webhook_events: Updated event subscriptions.

          webhook_headers: Updated headers.

          webhook_output_format: Updated output format.

          webhook_signing_secret: Updated signing secret (write-only). Send to rotate the secret.

          webhook_url: Updated webhook URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return self._put(
            path_template("/api/v1/beta/webhook-configs/{config_id}", config_id=config_id),
            body=maybe_transform(
                {
                    "webhook_events": webhook_events,
                    "webhook_headers": webhook_headers,
                    "webhook_output_format": webhook_output_format,
                    "webhook_signing_secret": webhook_signing_secret,
                    "webhook_url": webhook_url,
                },
                webhook_config_update_params.WebhookConfigUpdateParams,
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
                    webhook_config_update_params.WebhookConfigUpdateParams,
                ),
            ),
            cast_to=WebhookConfigResponse,
        )

    def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookConfigListResponse:
        """
        List the webhook configurations for the current project, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v1/beta/webhook-configs",
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
                    webhook_config_list_params.WebhookConfigListParams,
                ),
            ),
            cast_to=WebhookConfigListResponse,
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
        Delete a webhook configuration.

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
            path_template("/api/v1/beta/webhook-configs/{config_id}", config_id=config_id),
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
                    webhook_config_delete_params.WebhookConfigDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncWebhookConfigsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebhookConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhookConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhookConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncWebhookConfigsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        webhook_url: str,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        webhook_events: Optional[
            List[
                Literal[
                    "batch.cancelled",
                    "batch.error",
                    "batch.pending",
                    "batch.running",
                    "batch.success",
                    "classify.cancelled",
                    "classify.error",
                    "classify.partial_success",
                    "classify.pending",
                    "classify.running",
                    "classify.success",
                    "extract.cancelled",
                    "extract.error",
                    "extract.partial_success",
                    "extract.pending",
                    "extract.success",
                    "parse.cancelled",
                    "parse.error",
                    "parse.partial_success",
                    "parse.pending",
                    "parse.running",
                    "parse.success",
                    "sheets.cancelled",
                    "sheets.error",
                    "sheets.partial_success",
                    "sheets.pending",
                    "sheets.success",
                    "split.cancelled",
                    "split.error",
                    "split.pending",
                    "split.processing",
                    "split.success",
                    "unmapped_event",
                ]
            ]
        ]
        | Omit = omit,
        webhook_headers: Optional[Dict[str, str]] | Omit = omit,
        webhook_output_format: Optional[Literal["json", "string"]] | Omit = omit,
        webhook_signing_secret: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookConfigResponse:
        """
        Create a reusable webhook configuration for the current project.

        Args:
          webhook_url: URL to receive webhook POST notifications.

          webhook_events: Events to subscribe to. If null, all events are delivered.

          webhook_headers: Custom HTTP headers sent with each webhook request.

          webhook_output_format: Response format sent to the webhook: 'string' (default) or 'json'.

          webhook_signing_secret: Shared secret used to sign deliveries to this endpoint. Write-only: it is never
              returned in responses.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/beta/webhook-configs",
            body=await async_maybe_transform(
                {
                    "webhook_url": webhook_url,
                    "webhook_events": webhook_events,
                    "webhook_headers": webhook_headers,
                    "webhook_output_format": webhook_output_format,
                    "webhook_signing_secret": webhook_signing_secret,
                },
                webhook_config_create_params.WebhookConfigCreateParams,
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
                    webhook_config_create_params.WebhookConfigCreateParams,
                ),
            ),
            cast_to=WebhookConfigResponse,
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
    ) -> WebhookConfigResponse:
        """
        Get a single webhook configuration by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return await self._get(
            path_template("/api/v1/beta/webhook-configs/{config_id}", config_id=config_id),
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
                    webhook_config_retrieve_params.WebhookConfigRetrieveParams,
                ),
            ),
            cast_to=WebhookConfigResponse,
        )

    async def update(
        self,
        config_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        webhook_events: Optional[
            List[
                Literal[
                    "batch.cancelled",
                    "batch.error",
                    "batch.pending",
                    "batch.running",
                    "batch.success",
                    "classify.cancelled",
                    "classify.error",
                    "classify.partial_success",
                    "classify.pending",
                    "classify.running",
                    "classify.success",
                    "extract.cancelled",
                    "extract.error",
                    "extract.partial_success",
                    "extract.pending",
                    "extract.success",
                    "parse.cancelled",
                    "parse.error",
                    "parse.partial_success",
                    "parse.pending",
                    "parse.running",
                    "parse.success",
                    "sheets.cancelled",
                    "sheets.error",
                    "sheets.partial_success",
                    "sheets.pending",
                    "sheets.success",
                    "split.cancelled",
                    "split.error",
                    "split.pending",
                    "split.processing",
                    "split.success",
                    "unmapped_event",
                ]
            ]
        ]
        | Omit = omit,
        webhook_headers: Optional[Dict[str, str]] | Omit = omit,
        webhook_output_format: Optional[Literal["json", "string"]] | Omit = omit,
        webhook_signing_secret: Optional[str] | Omit = omit,
        webhook_url: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookConfigResponse:
        """Update a webhook configuration.

        Only fields present in the request change.

        Args:
          webhook_events: Updated event subscriptions.

          webhook_headers: Updated headers.

          webhook_output_format: Updated output format.

          webhook_signing_secret: Updated signing secret (write-only). Send to rotate the secret.

          webhook_url: Updated webhook URL.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return await self._put(
            path_template("/api/v1/beta/webhook-configs/{config_id}", config_id=config_id),
            body=await async_maybe_transform(
                {
                    "webhook_events": webhook_events,
                    "webhook_headers": webhook_headers,
                    "webhook_output_format": webhook_output_format,
                    "webhook_signing_secret": webhook_signing_secret,
                    "webhook_url": webhook_url,
                },
                webhook_config_update_params.WebhookConfigUpdateParams,
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
                    webhook_config_update_params.WebhookConfigUpdateParams,
                ),
            ),
            cast_to=WebhookConfigResponse,
        )

    async def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebhookConfigListResponse:
        """
        List the webhook configurations for the current project, newest first.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v1/beta/webhook-configs",
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
                    webhook_config_list_params.WebhookConfigListParams,
                ),
            ),
            cast_to=WebhookConfigListResponse,
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
        Delete a webhook configuration.

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
            path_template("/api/v1/beta/webhook-configs/{config_id}", config_id=config_id),
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
                    webhook_config_delete_params.WebhookConfigDeleteParams,
                ),
            ),
            cast_to=NoneType,
        )


class WebhookConfigsResourceWithRawResponse:
    def __init__(self, webhook_configs: WebhookConfigsResource) -> None:
        self._webhook_configs = webhook_configs

        self.create = to_raw_response_wrapper(
            webhook_configs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            webhook_configs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            webhook_configs.update,
        )
        self.list = to_raw_response_wrapper(
            webhook_configs.list,
        )
        self.delete = to_raw_response_wrapper(
            webhook_configs.delete,
        )


class AsyncWebhookConfigsResourceWithRawResponse:
    def __init__(self, webhook_configs: AsyncWebhookConfigsResource) -> None:
        self._webhook_configs = webhook_configs

        self.create = async_to_raw_response_wrapper(
            webhook_configs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            webhook_configs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            webhook_configs.update,
        )
        self.list = async_to_raw_response_wrapper(
            webhook_configs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            webhook_configs.delete,
        )


class WebhookConfigsResourceWithStreamingResponse:
    def __init__(self, webhook_configs: WebhookConfigsResource) -> None:
        self._webhook_configs = webhook_configs

        self.create = to_streamed_response_wrapper(
            webhook_configs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            webhook_configs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            webhook_configs.update,
        )
        self.list = to_streamed_response_wrapper(
            webhook_configs.list,
        )
        self.delete = to_streamed_response_wrapper(
            webhook_configs.delete,
        )


class AsyncWebhookConfigsResourceWithStreamingResponse:
    def __init__(self, webhook_configs: AsyncWebhookConfigsResource) -> None:
        self._webhook_configs = webhook_configs

        self.create = async_to_streamed_response_wrapper(
            webhook_configs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            webhook_configs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            webhook_configs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            webhook_configs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            webhook_configs.delete,
        )
