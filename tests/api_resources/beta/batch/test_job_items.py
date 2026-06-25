# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.pagination import SyncPaginatedBatchItems, AsyncPaginatedBatchItems
from llama_cloud.types.beta.batch import (
    JobItemListResponse,
    JobItemGetProcessingResultsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobItems:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        job_item = client.beta.batch.job_items.list(
            job_id="job_id",
        )
        assert_matches_type(SyncPaginatedBatchItems[JobItemListResponse], job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        job_item = client.beta.batch.job_items.list(
            job_id="job_id",
            limit=1,
            offset=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="cancelled",
        )
        assert_matches_type(SyncPaginatedBatchItems[JobItemListResponse], job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.beta.batch.job_items.with_raw_response.list(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_item = response.parse()
        assert_matches_type(SyncPaginatedBatchItems[JobItemListResponse], job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.beta.batch.job_items.with_streaming_response.list(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_item = response.parse()
            assert_matches_type(SyncPaginatedBatchItems[JobItemListResponse], job_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.beta.batch.job_items.with_raw_response.list(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_processing_results(self, client: LlamaCloud) -> None:
        job_item = client.beta.batch.job_items.get_processing_results(
            item_id="item_id",
        )
        assert_matches_type(JobItemGetProcessingResultsResponse, job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_processing_results_with_all_params(self, client: LlamaCloud) -> None:
        job_item = client.beta.batch.job_items.get_processing_results(
            item_id="item_id",
            job_type="classify",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobItemGetProcessingResultsResponse, job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_processing_results(self, client: LlamaCloud) -> None:
        response = client.beta.batch.job_items.with_raw_response.get_processing_results(
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_item = response.parse()
        assert_matches_type(JobItemGetProcessingResultsResponse, job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_processing_results(self, client: LlamaCloud) -> None:
        with client.beta.batch.job_items.with_streaming_response.get_processing_results(
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_item = response.parse()
            assert_matches_type(JobItemGetProcessingResultsResponse, job_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_processing_results(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            client.beta.batch.job_items.with_raw_response.get_processing_results(
                item_id="",
            )


class TestAsyncJobItems:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        job_item = await async_client.beta.batch.job_items.list(
            job_id="job_id",
        )
        assert_matches_type(AsyncPaginatedBatchItems[JobItemListResponse], job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        job_item = await async_client.beta.batch.job_items.list(
            job_id="job_id",
            limit=1,
            offset=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="cancelled",
        )
        assert_matches_type(AsyncPaginatedBatchItems[JobItemListResponse], job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.batch.job_items.with_raw_response.list(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_item = await response.parse()
        assert_matches_type(AsyncPaginatedBatchItems[JobItemListResponse], job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.batch.job_items.with_streaming_response.list(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_item = await response.parse()
            assert_matches_type(AsyncPaginatedBatchItems[JobItemListResponse], job_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.beta.batch.job_items.with_raw_response.list(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_processing_results(self, async_client: AsyncLlamaCloud) -> None:
        job_item = await async_client.beta.batch.job_items.get_processing_results(
            item_id="item_id",
        )
        assert_matches_type(JobItemGetProcessingResultsResponse, job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_processing_results_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        job_item = await async_client.beta.batch.job_items.get_processing_results(
            item_id="item_id",
            job_type="classify",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(JobItemGetProcessingResultsResponse, job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_processing_results(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.batch.job_items.with_raw_response.get_processing_results(
            item_id="item_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job_item = await response.parse()
        assert_matches_type(JobItemGetProcessingResultsResponse, job_item, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_processing_results(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.batch.job_items.with_streaming_response.get_processing_results(
            item_id="item_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job_item = await response.parse()
            assert_matches_type(JobItemGetProcessingResultsResponse, job_item, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_processing_results(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `item_id` but received ''"):
            await async_client.beta.batch.job_items.with_raw_response.get_processing_results(
                item_id="",
            )
