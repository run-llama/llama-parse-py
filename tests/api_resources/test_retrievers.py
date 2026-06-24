# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import (
    Retriever,
    RetrieverListResponse,
    CompositeRetrievalResult,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRetrievers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.create(
            name="x",
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.create(
            name="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preset_retrieval_parameters": {
                        "alpha": 0,
                        "class_name": "class_name",
                        "dense_similarity_cutoff": 0,
                        "dense_similarity_top_k": 1,
                        "enable_reranking": True,
                        "files_top_k": 1,
                        "rerank_top_n": 1,
                        "retrieval_mode": "auto_routed",
                        "retrieve_image_nodes": True,
                        "retrieve_page_figure_nodes": True,
                        "retrieve_page_screenshot_nodes": True,
                        "search_filters": {
                            "filters": [
                                {
                                    "key": "key",
                                    "value": 0,
                                    "operator": "!=",
                                }
                            ],
                            "condition": "and",
                        },
                        "search_filters_inference_schema": {"foo": {"foo": "bar"}},
                        "sparse_similarity_top_k": 1,
                    },
                }
            ],
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.retrievers.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = response.parse()
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.retrievers.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = response.parse()
            assert_matches_type(Retriever, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.update(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.update(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preset_retrieval_parameters": {
                        "alpha": 0,
                        "class_name": "class_name",
                        "dense_similarity_cutoff": 0,
                        "dense_similarity_top_k": 1,
                        "enable_reranking": True,
                        "files_top_k": 1,
                        "rerank_top_n": 1,
                        "retrieval_mode": "auto_routed",
                        "retrieve_image_nodes": True,
                        "retrieve_page_figure_nodes": True,
                        "retrieve_page_screenshot_nodes": True,
                        "search_filters": {
                            "filters": [
                                {
                                    "key": "key",
                                    "value": 0,
                                    "operator": "!=",
                                }
                            ],
                            "condition": "and",
                        },
                        "search_filters_inference_schema": {"foo": {"foo": "bar"}},
                        "sparse_similarity_top_k": 1,
                    },
                }
            ],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LlamaCloud) -> None:
        response = client.retrievers.with_raw_response.update(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = response.parse()
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LlamaCloud) -> None:
        with client.retrievers.with_streaming_response.update(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = response.parse()
            assert_matches_type(Retriever, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `retriever_id` but received ''"):
            client.retrievers.with_raw_response.update(
                retriever_id="",
                pipelines=[
                    {
                        "description": "description",
                        "name": "x",
                        "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.list()
        assert_matches_type(RetrieverListResponse, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.list(
            name="name",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RetrieverListResponse, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.retrievers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = response.parse()
        assert_matches_type(RetrieverListResponse, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.retrievers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = response.parse()
            assert_matches_type(RetrieverListResponse, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.delete(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert retriever is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.delete(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert retriever is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        response = client.retrievers.with_raw_response.delete(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = response.parse()
        assert retriever is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with client.retrievers.with_streaming_response.delete(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = response.parse()
            assert retriever is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `retriever_id` but received ''"):
            client.retrievers.with_raw_response.delete(
                retriever_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.get(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.get(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.retrievers.with_raw_response.get(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = response.parse()
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.retrievers.with_streaming_response.get(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = response.parse()
            assert_matches_type(Retriever, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `retriever_id` but received ''"):
            client.retrievers.with_raw_response.get(
                retriever_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.search(
            query="x",
        )
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.search(
            query="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mode="full",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preset_retrieval_parameters": {
                        "alpha": 0,
                        "class_name": "class_name",
                        "dense_similarity_cutoff": 0,
                        "dense_similarity_top_k": 1,
                        "enable_reranking": True,
                        "files_top_k": 1,
                        "rerank_top_n": 1,
                        "retrieval_mode": "auto_routed",
                        "retrieve_image_nodes": True,
                        "retrieve_page_figure_nodes": True,
                        "retrieve_page_screenshot_nodes": True,
                        "search_filters": {
                            "filters": [
                                {
                                    "key": "key",
                                    "value": 0,
                                    "operator": "!=",
                                }
                            ],
                            "condition": "and",
                        },
                        "search_filters_inference_schema": {"foo": {"foo": "bar"}},
                        "sparse_similarity_top_k": 1,
                    },
                }
            ],
            rerank_config={
                "top_n": 1,
                "type": "bedrock",
            },
            rerank_top_n=0,
        )
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: LlamaCloud) -> None:
        response = client.retrievers.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = response.parse()
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: LlamaCloud) -> None:
        with client.retrievers.with_streaming_response.search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = response.parse()
            assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.upsert(
            name="x",
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: LlamaCloud) -> None:
        retriever = client.retrievers.upsert(
            name="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preset_retrieval_parameters": {
                        "alpha": 0,
                        "class_name": "class_name",
                        "dense_similarity_cutoff": 0,
                        "dense_similarity_top_k": 1,
                        "enable_reranking": True,
                        "files_top_k": 1,
                        "rerank_top_n": 1,
                        "retrieval_mode": "auto_routed",
                        "retrieve_image_nodes": True,
                        "retrieve_page_figure_nodes": True,
                        "retrieve_page_screenshot_nodes": True,
                        "search_filters": {
                            "filters": [
                                {
                                    "key": "key",
                                    "value": 0,
                                    "operator": "!=",
                                }
                            ],
                            "condition": "and",
                        },
                        "search_filters_inference_schema": {"foo": {"foo": "bar"}},
                        "sparse_similarity_top_k": 1,
                    },
                }
            ],
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: LlamaCloud) -> None:
        response = client.retrievers.with_raw_response.upsert(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = response.parse()
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: LlamaCloud) -> None:
        with client.retrievers.with_streaming_response.upsert(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = response.parse()
            assert_matches_type(Retriever, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRetrievers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.create(
            name="x",
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.create(
            name="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preset_retrieval_parameters": {
                        "alpha": 0,
                        "class_name": "class_name",
                        "dense_similarity_cutoff": 0,
                        "dense_similarity_top_k": 1,
                        "enable_reranking": True,
                        "files_top_k": 1,
                        "rerank_top_n": 1,
                        "retrieval_mode": "auto_routed",
                        "retrieve_image_nodes": True,
                        "retrieve_page_figure_nodes": True,
                        "retrieve_page_screenshot_nodes": True,
                        "search_filters": {
                            "filters": [
                                {
                                    "key": "key",
                                    "value": 0,
                                    "operator": "!=",
                                }
                            ],
                            "condition": "and",
                        },
                        "search_filters_inference_schema": {"foo": {"foo": "bar"}},
                        "sparse_similarity_top_k": 1,
                    },
                }
            ],
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.retrievers.with_raw_response.create(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = await response.parse()
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.retrievers.with_streaming_response.create(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = await response.parse()
            assert_matches_type(Retriever, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.update(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.update(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preset_retrieval_parameters": {
                        "alpha": 0,
                        "class_name": "class_name",
                        "dense_similarity_cutoff": 0,
                        "dense_similarity_top_k": 1,
                        "enable_reranking": True,
                        "files_top_k": 1,
                        "rerank_top_n": 1,
                        "retrieval_mode": "auto_routed",
                        "retrieve_image_nodes": True,
                        "retrieve_page_figure_nodes": True,
                        "retrieve_page_screenshot_nodes": True,
                        "search_filters": {
                            "filters": [
                                {
                                    "key": "key",
                                    "value": 0,
                                    "operator": "!=",
                                }
                            ],
                            "condition": "and",
                        },
                        "search_filters_inference_schema": {"foo": {"foo": "bar"}},
                        "sparse_similarity_top_k": 1,
                    },
                }
            ],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.retrievers.with_raw_response.update(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = await response.parse()
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.retrievers.with_streaming_response.update(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = await response.parse()
            assert_matches_type(Retriever, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `retriever_id` but received ''"):
            await async_client.retrievers.with_raw_response.update(
                retriever_id="",
                pipelines=[
                    {
                        "description": "description",
                        "name": "x",
                        "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    }
                ],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.list()
        assert_matches_type(RetrieverListResponse, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.list(
            name="name",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RetrieverListResponse, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.retrievers.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = await response.parse()
        assert_matches_type(RetrieverListResponse, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.retrievers.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = await response.parse()
            assert_matches_type(RetrieverListResponse, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.delete(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert retriever is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.delete(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert retriever is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.retrievers.with_raw_response.delete(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = await response.parse()
        assert retriever is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.retrievers.with_streaming_response.delete(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = await response.parse()
            assert retriever is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `retriever_id` but received ''"):
            await async_client.retrievers.with_raw_response.delete(
                retriever_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.get(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.get(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.retrievers.with_raw_response.get(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = await response.parse()
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.retrievers.with_streaming_response.get(
            retriever_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = await response.parse()
            assert_matches_type(Retriever, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `retriever_id` but received ''"):
            await async_client.retrievers.with_raw_response.get(
                retriever_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.search(
            query="x",
        )
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.search(
            query="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            mode="full",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preset_retrieval_parameters": {
                        "alpha": 0,
                        "class_name": "class_name",
                        "dense_similarity_cutoff": 0,
                        "dense_similarity_top_k": 1,
                        "enable_reranking": True,
                        "files_top_k": 1,
                        "rerank_top_n": 1,
                        "retrieval_mode": "auto_routed",
                        "retrieve_image_nodes": True,
                        "retrieve_page_figure_nodes": True,
                        "retrieve_page_screenshot_nodes": True,
                        "search_filters": {
                            "filters": [
                                {
                                    "key": "key",
                                    "value": 0,
                                    "operator": "!=",
                                }
                            ],
                            "condition": "and",
                        },
                        "search_filters_inference_schema": {"foo": {"foo": "bar"}},
                        "sparse_similarity_top_k": 1,
                    },
                }
            ],
            rerank_config={
                "top_n": 1,
                "type": "bedrock",
            },
            rerank_top_n=0,
        )
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.retrievers.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = await response.parse()
        assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.retrievers.with_streaming_response.search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = await response.parse()
            assert_matches_type(CompositeRetrievalResult, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.upsert(
            name="x",
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        retriever = await async_client.retrievers.upsert(
            name="x",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            pipelines=[
                {
                    "description": "description",
                    "name": "x",
                    "pipeline_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "preset_retrieval_parameters": {
                        "alpha": 0,
                        "class_name": "class_name",
                        "dense_similarity_cutoff": 0,
                        "dense_similarity_top_k": 1,
                        "enable_reranking": True,
                        "files_top_k": 1,
                        "rerank_top_n": 1,
                        "retrieval_mode": "auto_routed",
                        "retrieve_image_nodes": True,
                        "retrieve_page_figure_nodes": True,
                        "retrieve_page_screenshot_nodes": True,
                        "search_filters": {
                            "filters": [
                                {
                                    "key": "key",
                                    "value": 0,
                                    "operator": "!=",
                                }
                            ],
                            "condition": "and",
                        },
                        "search_filters_inference_schema": {"foo": {"foo": "bar"}},
                        "sparse_similarity_top_k": 1,
                    },
                }
            ],
        )
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.retrievers.with_raw_response.upsert(
            name="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        retriever = await response.parse()
        assert_matches_type(Retriever, retriever, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.retrievers.with_streaming_response.upsert(
            name="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            retriever = await response.parse()
            assert_matches_type(Retriever, retriever, path=["response"])

        assert cast(Any, response.is_closed) is True
