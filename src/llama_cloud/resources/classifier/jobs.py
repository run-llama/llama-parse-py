# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import typing_extensions
from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from ..._base_client import AsyncPaginator, make_request_options
from ...types.classifier import (
    job_get_params,
    job_list_params,
    job_create_params,
    job_get_results_params,
)
from ...types.classifier.classify_job import ClassifyJob
from ...types.classifier.classifier_rule_param import ClassifierRuleParam
from ...types.classifier.job_get_results_response import JobGetResultsResponse
from ...types.classifier.classify_parsing_configuration_param import ClassifyParsingConfigurationParam

__all__ = ["JobsResource", "AsyncJobsResource"]


class JobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return JobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return JobsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("Please use `client.classify.create()`")
    def create(
        self,
        *,
        file_ids: SequenceNotStr[str],
        rules: Iterable[ClassifierRuleParam],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        mode: Literal["FAST", "MULTIMODAL"] | Omit = omit,
        parsing_configuration: ClassifyParsingConfigurationParam | Omit = omit,
        webhook_configurations: Iterable[job_create_params.WebhookConfiguration] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyJob:
        """Create a classify job.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          file_ids: The IDs of the files to classify

          rules: The rules to classify the files

          mode: The classification mode to use

          parsing_configuration: The configuration for the parsing job

          webhook_configurations: List of webhook configurations for notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/classifier/jobs",
            body=maybe_transform(
                {
                    "file_ids": file_ids,
                    "rules": rules,
                    "mode": mode,
                    "parsing_configuration": parsing_configuration,
                    "webhook_configurations": webhook_configurations,
                },
                job_create_params.JobCreateParams,
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
                    job_create_params.JobCreateParams,
                ),
            ),
            cast_to=ClassifyJob,
        )

    @typing_extensions.deprecated("Please use `client.classify.list()`")
    def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPaginatedCursor[ClassifyJob]:
        """List classify jobs.

        Experimental: This endpoint is not yet ready for production
        use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/classifier/jobs",
            page=SyncPaginatedCursor[ClassifyJob],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=ClassifyJob,
        )

    @typing_extensions.deprecated("Please use `client.classify.get()`")
    def get(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyJob:
        """Get a classify job.

        Experimental: This endpoint is not yet ready for production
        use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")
        return self._get(
            path_template("/api/v1/classifier/jobs/{classify_job_id}", classify_job_id=classify_job_id),
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
                    job_get_params.JobGetParams,
                ),
            ),
            cast_to=ClassifyJob,
        )

    @typing_extensions.deprecated("Please use `client.classify.get()`")
    def get_results(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetResultsResponse:
        """Get the results of a classify job.

        Experimental: This endpoint is not yet ready
        for production use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")
        return self._get(
            path_template("/api/v1/classifier/jobs/{classify_job_id}/results", classify_job_id=classify_job_id),
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
                    job_get_results_params.JobGetResultsParams,
                ),
            ),
            cast_to=JobGetResultsResponse,
        )


class AsyncJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncJobsResourceWithStreamingResponse(self)

    @typing_extensions.deprecated("Please use `client.classify.create()`")
    async def create(
        self,
        *,
        file_ids: SequenceNotStr[str],
        rules: Iterable[ClassifierRuleParam],
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        mode: Literal["FAST", "MULTIMODAL"] | Omit = omit,
        parsing_configuration: ClassifyParsingConfigurationParam | Omit = omit,
        webhook_configurations: Iterable[job_create_params.WebhookConfiguration] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyJob:
        """Create a classify job.

        Experimental: This endpoint is not yet ready for
        production use and is subject to change at any time.

        Args:
          file_ids: The IDs of the files to classify

          rules: The rules to classify the files

          mode: The classification mode to use

          parsing_configuration: The configuration for the parsing job

          webhook_configurations: List of webhook configurations for notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/classifier/jobs",
            body=await async_maybe_transform(
                {
                    "file_ids": file_ids,
                    "rules": rules,
                    "mode": mode,
                    "parsing_configuration": parsing_configuration,
                    "webhook_configurations": webhook_configurations,
                },
                job_create_params.JobCreateParams,
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
                    job_create_params.JobCreateParams,
                ),
            ),
            cast_to=ClassifyJob,
        )

    @typing_extensions.deprecated("Please use `client.classify.list()`")
    def list(
        self,
        *,
        organization_id: Optional[str] | Omit = omit,
        page_size: Optional[int] | Omit = omit,
        page_token: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ClassifyJob, AsyncPaginatedCursor[ClassifyJob]]:
        """List classify jobs.

        Experimental: This endpoint is not yet ready for production
        use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/api/v1/classifier/jobs",
            page=AsyncPaginatedCursor[ClassifyJob],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "organization_id": organization_id,
                        "page_size": page_size,
                        "page_token": page_token,
                        "project_id": project_id,
                    },
                    job_list_params.JobListParams,
                ),
            ),
            model=ClassifyJob,
        )

    @typing_extensions.deprecated("Please use `client.classify.get()`")
    async def get(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ClassifyJob:
        """Get a classify job.

        Experimental: This endpoint is not yet ready for production
        use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")
        return await self._get(
            path_template("/api/v1/classifier/jobs/{classify_job_id}", classify_job_id=classify_job_id),
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
                    job_get_params.JobGetParams,
                ),
            ),
            cast_to=ClassifyJob,
        )

    @typing_extensions.deprecated("Please use `client.classify.get()`")
    async def get_results(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JobGetResultsResponse:
        """Get the results of a classify job.

        Experimental: This endpoint is not yet ready
        for production use and is subject to change at any time.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")
        return await self._get(
            path_template("/api/v1/classifier/jobs/{classify_job_id}/results", classify_job_id=classify_job_id),
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
                    job_get_results_params.JobGetResultsParams,
                ),
            ),
            cast_to=JobGetResultsResponse,
        )


class JobsResourceWithRawResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                jobs.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                jobs.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                jobs.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_results = (  # pyright: ignore[reportDeprecated]
            to_raw_response_wrapper(
                jobs.get_results,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncJobsResourceWithRawResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                jobs.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                jobs.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                jobs.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_results = (  # pyright: ignore[reportDeprecated]
            async_to_raw_response_wrapper(
                jobs.get_results,  # pyright: ignore[reportDeprecated],
            )
        )


class JobsResourceWithStreamingResponse:
    def __init__(self, jobs: JobsResource) -> None:
        self._jobs = jobs

        self.create = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                jobs.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                jobs.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                jobs.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_results = (  # pyright: ignore[reportDeprecated]
            to_streamed_response_wrapper(
                jobs.get_results,  # pyright: ignore[reportDeprecated],
            )
        )


class AsyncJobsResourceWithStreamingResponse:
    def __init__(self, jobs: AsyncJobsResource) -> None:
        self._jobs = jobs

        self.create = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                jobs.create,  # pyright: ignore[reportDeprecated],
            )
        )
        self.list = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                jobs.list,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                jobs.get,  # pyright: ignore[reportDeprecated],
            )
        )
        self.get_results = (  # pyright: ignore[reportDeprecated]
            async_to_streamed_response_wrapper(
                jobs.get_results,  # pyright: ignore[reportDeprecated],
            )
        )
