# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from llama_cloud.types.beta import (
    IndexGetResponse,
    IndexListResponse,
    IndexCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIndexes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        index = client.beta.indexes.create(
            source_directory_id="dir-abc123",
        )
        assert_matches_type(IndexCreateResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        index = client.beta.indexes.create(
            source_directory_id="dir-abc123",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
            products=[
                {
                    "product_config_id": "cfg-abc123",
                    "product_type": "parse",
                }
            ],
            store_attachments=["screenshots"],
            sync_frequency="manual",
            vector_target="DEFAULT",
        )
        assert_matches_type(IndexCreateResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.beta.indexes.with_raw_response.create(
            source_directory_id="dir-abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(IndexCreateResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.beta.indexes.with_streaming_response.create(
            source_directory_id="dir-abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(IndexCreateResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        index = client.beta.indexes.list()
        assert_matches_type(SyncPaginatedCursor[IndexListResponse], index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        index = client.beta.indexes.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_directory_id="source_directory_id",
        )
        assert_matches_type(SyncPaginatedCursor[IndexListResponse], index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.beta.indexes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(SyncPaginatedCursor[IndexListResponse], index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.beta.indexes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(SyncPaginatedCursor[IndexListResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        index = client.beta.indexes.delete(
            index_id="index_id",
        )
        assert index is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: LlamaCloud) -> None:
        index = client.beta.indexes.delete(
            index_id="index_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert index is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        response = client.beta.indexes.with_raw_response.delete(
            index_id="index_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert index is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with client.beta.indexes.with_streaming_response.delete(
            index_id="index_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert index is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_id` but received ''"):
            client.beta.indexes.with_raw_response.delete(
                index_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        index = client.beta.indexes.get(
            index_id="index_id",
        )
        assert_matches_type(IndexGetResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        index = client.beta.indexes.get(
            index_id="index_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IndexGetResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.beta.indexes.with_raw_response.get(
            index_id="index_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(IndexGetResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.beta.indexes.with_streaming_response.get(
            index_id="index_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(IndexGetResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_id` but received ''"):
            client.beta.indexes.with_raw_response.get(
                index_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sync(self, client: LlamaCloud) -> None:
        index = client.beta.indexes.sync(
            index_id="index_id",
        )
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_sync_with_all_params(self, client: LlamaCloud) -> None:
        index = client.beta.indexes.sync(
            index_id="index_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_sync(self, client: LlamaCloud) -> None:
        response = client.beta.indexes.with_raw_response.sync(
            index_id="index_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = response.parse()
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_sync(self, client: LlamaCloud) -> None:
        with client.beta.indexes.with_streaming_response.sync(
            index_id="index_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_sync(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_id` but received ''"):
            client.beta.indexes.with_raw_response.sync(
                index_id="",
            )


class TestAsyncIndexes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        index = await async_client.beta.indexes.create(
            source_directory_id="dir-abc123",
        )
        assert_matches_type(IndexCreateResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        index = await async_client.beta.indexes.create(
            source_directory_id="dir-abc123",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            name="name",
            products=[
                {
                    "product_config_id": "cfg-abc123",
                    "product_type": "parse",
                }
            ],
            store_attachments=["screenshots"],
            sync_frequency="manual",
            vector_target="DEFAULT",
        )
        assert_matches_type(IndexCreateResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.indexes.with_raw_response.create(
            source_directory_id="dir-abc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(IndexCreateResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.indexes.with_streaming_response.create(
            source_directory_id="dir-abc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(IndexCreateResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        index = await async_client.beta.indexes.list()
        assert_matches_type(AsyncPaginatedCursor[IndexListResponse], index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        index = await async_client.beta.indexes.list(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_directory_id="source_directory_id",
        )
        assert_matches_type(AsyncPaginatedCursor[IndexListResponse], index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.indexes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[IndexListResponse], index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.indexes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[IndexListResponse], index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        index = await async_client.beta.indexes.delete(
            index_id="index_id",
        )
        assert index is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        index = await async_client.beta.indexes.delete(
            index_id="index_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert index is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.indexes.with_raw_response.delete(
            index_id="index_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert index is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.indexes.with_streaming_response.delete(
            index_id="index_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert index is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_id` but received ''"):
            await async_client.beta.indexes.with_raw_response.delete(
                index_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        index = await async_client.beta.indexes.get(
            index_id="index_id",
        )
        assert_matches_type(IndexGetResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        index = await async_client.beta.indexes.get(
            index_id="index_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(IndexGetResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.indexes.with_raw_response.get(
            index_id="index_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(IndexGetResponse, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.indexes.with_streaming_response.get(
            index_id="index_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(IndexGetResponse, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_id` but received ''"):
            await async_client.beta.indexes.with_raw_response.get(
                index_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sync(self, async_client: AsyncLlamaCloud) -> None:
        index = await async_client.beta.indexes.sync(
            index_id="index_id",
        )
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_sync_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        index = await async_client.beta.indexes.sync(
            index_id="index_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_sync(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.indexes.with_raw_response.sync(
            index_id="index_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        index = await response.parse()
        assert_matches_type(object, index, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_sync(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.indexes.with_streaming_response.sync(
            index_id="index_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            index = await response.parse()
            assert_matches_type(object, index, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_sync(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `index_id` but received ''"):
            await async_client.beta.indexes.with_raw_response.sync(
                index_id="",
            )
