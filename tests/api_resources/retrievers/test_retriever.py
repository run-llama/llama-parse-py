# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import CompositeRetrievalResult

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetriever:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.retriever.search(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        )
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.retriever.search(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mode="routing",
            rerank_config={
                "top_n": 1,
                "type": "system_default",
            },
            rerank_top_n=0,
        )
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: LlamaCloud) -> None:
        response = client.retrievers.retriever.with_raw_response.search(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = response.parse()
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: LlamaCloud) -> None:
        with client.retrievers.retriever.with_streaming_response.search(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = response.parse()
            assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_search(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `retriever_id` but received ''"):
            client.retrievers.retriever.with_raw_response.search(
                retriever_id="",
                query="x",
            )


class TestAsyncRetriever:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.retriever.search(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        )
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.retriever.search(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mode="routing",
            rerank_config={
                "top_n": 1,
                "type": "system_default",
            },
            rerank_top_n=0,
        )
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.retrievers.retriever.with_raw_response.search(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = await response.parse()
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.retrievers.retriever.with_streaming_response.search(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = await response.parse()
            assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_search(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `retriever_id` but received ''"):
            await async_client.retrievers.retriever.with_raw_response.search(
                retriever_id="",
                query="x",
            )
