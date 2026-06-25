# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from llama_cloud.types.classifier import (
    ClassifyJob,
    JobGetResultsResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = client.classifier.jobs.create(
                file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                rules=[
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            )

        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = client.classifier.jobs.create(
                file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                rules=[
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mode="FAST",
                parsing_configuration={
                    "lang": "abq",
                    "max_pages": 0,
                    "target_pages": [0],
                },
                webhook_configurations=[
                    {
                        "webhook_events": ["parse.success", "parse.error"],
                        "webhook_headers": {"foo": "bar"},
                        "webhook_output_format": "json",
                        "webhook_url": "https:",
                    }
                ],
            )

        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.classifier.jobs.with_raw_response.create(
                file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                rules=[
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.classifier.jobs.with_streaming_response.create(
                file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                rules=[
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                job = response.parse()
                assert_matches_type(ClassifyJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = client.classifier.jobs.list()

        assert_matches_type(SyncPaginatedCursor[ClassifyJob], job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = client.classifier.jobs.list(
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                page_size=0,
                page_token="page_token",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(SyncPaginatedCursor[ClassifyJob], job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.classifier.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(SyncPaginatedCursor[ClassifyJob], job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.classifier.jobs.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                job = response.parse()
                assert_matches_type(SyncPaginatedCursor[ClassifyJob], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = client.classifier.jobs.get(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = client.classifier.jobs.get(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.classifier.jobs.with_raw_response.get(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.classifier.jobs.with_streaming_response.get(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                job = response.parse()
                assert_matches_type(ClassifyJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `classify_job_id` but received ''"):
                client.classifier.jobs.with_raw_response.get(
                    classify_job_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_results(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = client.classifier.jobs.get_results(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(JobGetResultsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_results_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = client.classifier.jobs.get_results(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(JobGetResultsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_results(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.classifier.jobs.with_raw_response.get_results(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(JobGetResultsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_results(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.classifier.jobs.with_streaming_response.get_results(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                job = response.parse()
                assert_matches_type(JobGetResultsResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_results(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `classify_job_id` but received ''"):
                client.classifier.jobs.with_raw_response.get_results(
                    classify_job_id="",
                )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = await async_client.classifier.jobs.create(
                file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                rules=[
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            )

        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = await async_client.classifier.jobs.create(
                file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                rules=[
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                mode="FAST",
                parsing_configuration={
                    "lang": "abq",
                    "max_pages": 0,
                    "target_pages": [0],
                },
                webhook_configurations=[
                    {
                        "webhook_events": ["parse.success", "parse.error"],
                        "webhook_headers": {"foo": "bar"},
                        "webhook_output_format": "json",
                        "webhook_url": "https:",
                    }
                ],
            )

        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.classifier.jobs.with_raw_response.create(
                file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                rules=[
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.classifier.jobs.with_streaming_response.create(
                file_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                rules=[
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                job = await response.parse()
                assert_matches_type(ClassifyJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = await async_client.classifier.jobs.list()

        assert_matches_type(AsyncPaginatedCursor[ClassifyJob], job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = await async_client.classifier.jobs.list(
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                page_size=0,
                page_token="page_token",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(AsyncPaginatedCursor[ClassifyJob], job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.classifier.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[ClassifyJob], job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.classifier.jobs.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                job = await response.parse()
                assert_matches_type(AsyncPaginatedCursor[ClassifyJob], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = await async_client.classifier.jobs.get(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = await async_client.classifier.jobs.get(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.classifier.jobs.with_raw_response.get(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(ClassifyJob, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.classifier.jobs.with_streaming_response.get(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                job = await response.parse()
                assert_matches_type(ClassifyJob, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `classify_job_id` but received ''"):
                await async_client.classifier.jobs.with_raw_response.get(
                    classify_job_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_results(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = await async_client.classifier.jobs.get_results(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(JobGetResultsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_results_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            job = await async_client.classifier.jobs.get_results(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(JobGetResultsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_results(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.classifier.jobs.with_raw_response.get_results(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(JobGetResultsResponse, job, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_results(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.classifier.jobs.with_streaming_response.get_results(
                classify_job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                job = await response.parse()
                assert_matches_type(JobGetResultsResponse, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_results(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `classify_job_id` but received ''"):
                await async_client.classifier.jobs.with_raw_response.get_results(
                    classify_job_id="",
                )
