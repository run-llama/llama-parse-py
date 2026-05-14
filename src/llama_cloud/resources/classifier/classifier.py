# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Literal, Iterable, Optional

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, SequenceNotStr, omit
from ..._compat import cached_property
from ..._polling import (
    DEFAULT_TIMEOUT,
    BackoffStrategy,
    poll_until_complete,
    poll_until_complete_async,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.classifier.classify_job import ClassifyJob
from ...types.classifier.classifier_rule_param import ClassifierRuleParam
from ...types.classifier.job_get_results_response import JobGetResultsResponse
from ...types.classifier.classify_parsing_configuration_param import ClassifyParsingConfigurationParam

__all__ = ["ClassifierResource", "AsyncClassifierResource"]


class ClassifierResource(SyncAPIResource):
    def classify(
        self,
        *,
        file_ids: SequenceNotStr[str],
        rules: Iterable[ClassifierRuleParam],
        mode: Literal["FAST", "MULTIMODAL"] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        parsing_configuration: ClassifyParsingConfigurationParam | Omit = omit,
        # Polling parameters
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> JobGetResultsResponse:
        """
        Create a classify job and wait for it to complete, returning the results.

        This is a convenience method that combines create(), wait_for_completion(),
        and get_results() into a single call for the most common end-to-end workflow.

        Args:
            file_ids: The IDs of the files to classify

            rules: The rules to classify the files

            mode: The classification mode to use ("FAST" or "MULTIMODAL")

            organization_id: Optional organization ID

            project_id: Optional project ID

            parsing_configuration: The configuration for the parsing job

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The classification results (JobGetResultsResponse)

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # One-shot: create job, wait for completion, and get results
            results = client.classifier.jobs.create_and_wait(
                file_ids=["file1", "file2", "file3"],
                rules=[
                    {"name": "invoice", "description": "Invoice documents"},
                    {"name": "receipt", "description": "Receipt documents"},
                ],
                verbose=True,
            )

            # Results are ready to use immediately
            for file_result in results.files:
                print(f"File {file_result.file_id}: {file_result.classification}")
            ```
        """
        # Create the job
        job = self.jobs.create(  # pyright: ignore[reportDeprecated]
            file_ids=file_ids,
            rules=rules,
            mode=mode,
            organization_id=organization_id,
            project_id=project_id,
            parsing_configuration=parsing_configuration,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion
        self.wait_for_completion(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Get and return the results
        return self.jobs.get_results(  # pyright: ignore[reportDeprecated]
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

    def wait_for_completion(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ClassifyJob:
        """
        Wait for a classify job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Args:
            classify_job_id: The ID of the classify job to wait for

            organization_id: Optional organization ID

            project_id: Optional project ID

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed ClassifyJob

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # Create a classify job
            job = client.classifier.jobs.create(file_ids=["file1", "file2"], rules=[...])

            # Wait for it to complete
            completed_job = client.classifier.jobs.wait_for_completion(job.id, verbose=True)

            # Get the results
            results = client.classifier.jobs.get_results(job.id)
            ```
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")

        def get_status() -> ClassifyJob:
            return self.jobs.get(  # pyright: ignore[reportDeprecated]
                classify_job_id,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: ClassifyJob) -> bool:
            return job.status in ("SUCCESS", "PARTIAL_SUCCESS")

        def is_error(job: ClassifyJob) -> bool:
            return job.status in ("ERROR", "CANCELLED")

        def get_error_message(job: ClassifyJob) -> str:
            error_parts = [f"Job {classify_job_id} failed with status: {job.status}"]
            if job.error_message:
                error_parts.append(f"Error: {job.error_message}")
            return " | ".join(error_parts)

        return poll_until_complete(
            get_status_fn=get_status,
            is_complete_fn=is_complete,
            is_error_fn=is_error,
            get_error_message_fn=get_error_message,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
        )

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ClassifierResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return ClassifierResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ClassifierResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return ClassifierResourceWithStreamingResponse(self)


class AsyncClassifierResource(AsyncAPIResource):
    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncClassifierResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/run-llama/llama-parse-py#accessing-raw-response-data-eg-headers
        """
        return AsyncClassifierResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncClassifierResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/run-llama/llama-parse-py#with_streaming_response
        """
        return AsyncClassifierResourceWithStreamingResponse(self)

    async def classify(
        self,
        *,
        file_ids: SequenceNotStr[str],
        rules: Iterable[ClassifierRuleParam],
        mode: Literal["FAST", "MULTIMODAL"] | Omit = omit,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        parsing_configuration: ClassifyParsingConfigurationParam | Omit = omit,
        # Polling parameters
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> JobGetResultsResponse:
        """
        Create a classify job and wait for it to complete, returning the results.

        This is a convenience method that combines create(), wait_for_completion(),
        and get_results() into a single call for the most common end-to-end workflow.

        Args:
            file_ids: The IDs of the files to classify

            rules: The rules to classify the files

            mode: The classification mode to use ("FAST" or "MULTIMODAL")

            organization_id: Optional organization ID

            project_id: Optional project ID

            parsing_configuration: The configuration for the parsing job

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The classification results (JobGetResultsResponse)

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import AsyncLlamaCloud

            client = AsyncLlamaCloud(api_key="...")

            # One-shot: create job, wait for completion, and get results
            results = await client.classifier.jobs.create_and_wait(
                file_ids=["file1", "file2", "file3"],
                rules=[
                    {"name": "invoice", "description": "Invoice documents"},
                    {"name": "receipt", "description": "Receipt documents"},
                ],
                verbose=True,
            )

            # Results are ready to use immediately
            for file_result in results.files:
                print(f"File {file_result.file_id}: {file_result.classification}")
            ```
        """
        # Create the job
        job = await self.jobs.create(  # pyright: ignore[reportDeprecated]
            file_ids=file_ids,
            rules=rules,
            mode=mode,
            organization_id=organization_id,
            project_id=project_id,
            parsing_configuration=parsing_configuration,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Wait for completion
        await self.wait_for_completion(
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

        # Get and return the results
        return await self.jobs.get_results(  # pyright: ignore[reportDeprecated]
            job.id,
            organization_id=organization_id,
            project_id=project_id,
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
        )

    async def wait_for_completion(
        self,
        classify_job_id: str,
        *,
        organization_id: Optional[str] | Omit = omit,
        project_id: Optional[str] | Omit = omit,
        polling_interval: float = 1.0,
        max_interval: float = 5.0,
        timeout: float = DEFAULT_TIMEOUT,
        backoff: BackoffStrategy = "linear",
        verbose: bool = False,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
    ) -> ClassifyJob:
        """
        Wait for a classify job to complete by polling until it reaches a terminal state.

        This method polls the job status at regular intervals until the job completes
        successfully or fails. It uses configurable backoff strategies to optimize
        polling behavior.

        Args:
            classify_job_id: The ID of the classify job to wait for

            organization_id: Optional organization ID

            project_id: Optional project ID

            polling_interval: Initial polling interval in seconds (default: 1.0)

            max_interval: Maximum polling interval for backoff in seconds (default: 5.0)

            timeout: Maximum time to wait in seconds (default: 300.0)

            backoff: Backoff strategy for polling intervals. Options:
                - "constant": Keep the same polling interval
                - "linear": Increase interval by 1 second each poll (default)
                - "exponential": Double the interval each poll

            verbose: Print progress indicators every 10 polls (default: False)

            extra_headers: Send extra headers

            extra_query: Add additional query parameters to the request

            extra_body: Add additional JSON properties to the request

        Returns:
            The completed ClassifyJob

        Raises:
            PollingTimeoutError: If the job doesn't complete within the timeout period

            PollingError: If the job fails or is cancelled

        Example:
            ```python
            from llama_cloud import LlamaCloud

            client = LlamaCloud(api_key="...")

            # Create a classify job
            job = await client.classifier.jobs.create(file_ids=["file1", "file2"], rules=[...])

            # Wait for it to complete
            completed_job = await client.classifier.jobs.wait_for_completion(job.id, verbose=True)

            # Get the results
            results = await client.classifier.jobs.get_results(job.id)
            ```
        """
        if not classify_job_id:
            raise ValueError(f"Expected a non-empty value for `classify_job_id` but received {classify_job_id!r}")

        async def get_status() -> ClassifyJob:
            return await self.jobs.get(  # pyright: ignore[reportDeprecated]
                classify_job_id,
                organization_id=organization_id,
                project_id=project_id,
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
            )

        def is_complete(job: ClassifyJob) -> bool:
            return job.status in ("SUCCESS", "PARTIAL_SUCCESS")

        def is_error(job: ClassifyJob) -> bool:
            return job.status in ("ERROR", "CANCELLED")

        def get_error_message(job: ClassifyJob) -> str:
            error_parts = [f"Job {classify_job_id} failed with status: {job.status}"]
            if job.error_message:
                error_parts.append(f"Error: {job.error_message}")
            return " | ".join(error_parts)

        return await poll_until_complete_async(
            get_status_fn=get_status,
            is_complete_fn=is_complete,
            is_error_fn=is_error,
            get_error_message_fn=get_error_message,
            polling_interval=polling_interval,
            max_interval=max_interval,
            timeout=timeout,
            backoff=backoff,
            verbose=verbose,
        )


class ClassifierResourceWithRawResponse:
    def __init__(self, classifier: ClassifierResource) -> None:
        self._classifier = classifier

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._classifier.jobs)


class AsyncClassifierResourceWithRawResponse:
    def __init__(self, classifier: AsyncClassifierResource) -> None:
        self._classifier = classifier

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._classifier.jobs)


class ClassifierResourceWithStreamingResponse:
    def __init__(self, classifier: ClassifierResource) -> None:
        self._classifier = classifier

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._classifier.jobs)


class AsyncClassifierResourceWithStreamingResponse:
    def __init__(self, classifier: AsyncClassifierResource) -> None:
        self._classifier = classifier

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._classifier.jobs)
