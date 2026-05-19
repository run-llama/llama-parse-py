# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types.beta import (
    RetrievalGrepResponse,
    RetrievalReadResponse,
    RetrievalSearchResponse,
    RetrievalRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetrieval:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LlamaCloud) -> None:
        retrieval = client.beta.retrieval.retrieve(
            index_id="idx-abc123",
            query="What are the key findings?",
        )
        assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaCloud) -> None:
        retrieval = client.beta.retrieval.retrieve(
            index_id="idx-abc123",
            query="What are the key findings?",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_filters={
                "foo": {
                    "operator": "eq",
                    "value": "string",
                }
            },
            full_text_pipeline_weight=0,
            num_candidates=0,
            rerank={
                "enabled": True,
                "top_n": 5,
            },
            score_threshold=0,
            static_filters={
                "parsed_directory_file_id": {
                    "operator": "eq",
                    "value": "string",
                }
            },
            top_k=10,
            vector_pipeline_weight=0,
        )
        assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaCloud) -> None:
        response = client.beta.retrieval.with_raw_response.retrieve(
            index_id="idx-abc123",
            query="What are the key findings?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaCloud) -> None:
        with client.beta.retrieval.with_streaming_response.retrieve(
            index_id="idx-abc123",
            query="What are the key findings?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_grep(self, client: LlamaCloud) -> None:
        retrieval = client.beta.retrieval.grep(
            file_id="file_id",
            index_id="idx-abc123",
            pattern="revenue|profit",
        )
        assert_matches_type(RetrievalGrepResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_grep_with_all_params(self, client: LlamaCloud) -> None:
        retrieval = client.beta.retrieval.grep(
            file_id="file_id",
            index_id="idx-abc123",
            pattern="revenue|profit",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context_chars=0,
            limit=0,
        )
        assert_matches_type(RetrievalGrepResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_grep(self, client: LlamaCloud) -> None:
        response = client.beta.retrieval.with_raw_response.grep(
            file_id="file_id",
            index_id="idx-abc123",
            pattern="revenue|profit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(RetrievalGrepResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_grep(self, client: LlamaCloud) -> None:
        with client.beta.retrieval.with_streaming_response.grep(
            file_id="file_id",
            index_id="idx-abc123",
            pattern="revenue|profit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(RetrievalGrepResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_read(self, client: LlamaCloud) -> None:
        retrieval = client.beta.retrieval.read(
            file_id="file_id",
            index_id="idx-abc123",
        )
        assert_matches_type(RetrievalReadResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_read_with_all_params(self, client: LlamaCloud) -> None:
        retrieval = client.beta.retrieval.read(
            file_id="file_id",
            index_id="idx-abc123",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_length=0,
            offset=0,
        )
        assert_matches_type(RetrievalReadResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_read(self, client: LlamaCloud) -> None:
        response = client.beta.retrieval.with_raw_response.read(
            file_id="file_id",
            index_id="idx-abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(RetrievalReadResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_read(self, client: LlamaCloud) -> None:
        with client.beta.retrieval.with_streaming_response.read(
            file_id="file_id",
            index_id="idx-abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(RetrievalReadResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: LlamaCloud) -> None:
        retrieval = client.beta.retrieval.search(
            index_id="idx-abc123",
        )
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: LlamaCloud) -> None:
        retrieval = client.beta.retrieval.search(
            index_id="idx-abc123",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_name="file_name",
            file_name_contains="file_name_contains",
            limit=0,
        )
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: LlamaCloud) -> None:
        response = client.beta.retrieval.with_raw_response.search(
            index_id="idx-abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = response.parse()
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: LlamaCloud) -> None:
        with client.beta.retrieval.with_streaming_response.search(
            index_id="idx-abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = response.parse()
            assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRetrieval:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        retrieval = await async_client.beta.retrieval.retrieve(
            index_id="idx-abc123",
            query="What are the key findings?",
        )
        assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retrieval = await async_client.beta.retrieval.retrieve(
            index_id="idx-abc123",
            query="What are the key findings?",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            custom_filters={
                "foo": {
                    "operator": "eq",
                    "value": "string",
                }
            },
            full_text_pipeline_weight=0,
            num_candidates=0,
            rerank={
                "enabled": True,
                "top_n": 5,
            },
            score_threshold=0,
            static_filters={
                "parsed_directory_file_id": {
                    "operator": "eq",
                    "value": "string",
                }
            },
            top_k=10,
            vector_pipeline_weight=0,
        )
        assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.retrieval.with_raw_response.retrieve(
            index_id="idx-abc123",
            query="What are the key findings?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.retrieval.with_streaming_response.retrieve(
            index_id="idx-abc123",
            query="What are the key findings?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(RetrievalRetrieveResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_grep(self, async_client: AsyncLlamaCloud) -> None:
        retrieval = await async_client.beta.retrieval.grep(
            file_id="file_id",
            index_id="idx-abc123",
            pattern="revenue|profit",
        )
        assert_matches_type(RetrievalGrepResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_grep_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retrieval = await async_client.beta.retrieval.grep(
            file_id="file_id",
            index_id="idx-abc123",
            pattern="revenue|profit",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context_chars=0,
            limit=0,
        )
        assert_matches_type(RetrievalGrepResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_grep(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.retrieval.with_raw_response.grep(
            file_id="file_id",
            index_id="idx-abc123",
            pattern="revenue|profit",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(RetrievalGrepResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_grep(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.retrieval.with_streaming_response.grep(
            file_id="file_id",
            index_id="idx-abc123",
            pattern="revenue|profit",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(RetrievalGrepResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_read(self, async_client: AsyncLlamaCloud) -> None:
        retrieval = await async_client.beta.retrieval.read(
            file_id="file_id",
            index_id="idx-abc123",
        )
        assert_matches_type(RetrievalReadResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_read_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retrieval = await async_client.beta.retrieval.read(
            file_id="file_id",
            index_id="idx-abc123",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            max_length=0,
            offset=0,
        )
        assert_matches_type(RetrievalReadResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_read(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.retrieval.with_raw_response.read(
            file_id="file_id",
            index_id="idx-abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(RetrievalReadResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_read(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.retrieval.with_streaming_response.read(
            file_id="file_id",
            index_id="idx-abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(RetrievalReadResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncLlamaCloud) -> None:
        retrieval = await async_client.beta.retrieval.search(
            index_id="idx-abc123",
        )
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retrieval = await async_client.beta.retrieval.search(
            index_id="idx-abc123",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file_name="file_name",
            file_name_contains="file_name_contains",
            limit=0,
        )
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.retrieval.with_raw_response.search(
            index_id="idx-abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retrieval = await response.parse()
        assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.retrieval.with_streaming_response.search(
            index_id="idx-abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retrieval = await response.parse()
            assert_matches_type(RetrievalSearchResponse, retrieval, path=["response"])

        assert cast(Any, response.is_closed) is True
