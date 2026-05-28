# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import (
    BatchGetResponse,
    BatchListResponse,
    BatchCreateResponse,
)
from llama_cloud._utils import parse_datetime
from llama_cloud.pagination import SyncPaginatedCursor, AsyncPaginatedCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatches:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        batch = client.batches.create(
            config={
                "job": {
                    "configuration_id": "cfg-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "type": "parse_v2",
                }
            },
            source_directory_id="dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        batch = client.batches.create(
            config={
                "job": {
                    "configuration_id": "cfg-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "type": "parse_v2",
                }
            },
            source_directory_id="dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.batches.with_raw_response.create(
            config={
                "job": {
                    "configuration_id": "cfg-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "type": "parse_v2",
                }
            },
            source_directory_id="dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.batches.with_streaming_response.create(
            config={
                "job": {
                    "configuration_id": "cfg-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "type": "parse_v2",
                }
            },
            source_directory_id="dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchCreateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        batch = client.batches.list()
        assert_matches_type(SyncPaginatedCursor[BatchListResponse], batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        batch = client.batches.list(
            created_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_directory_id="source_directory_id",
            status="PENDING",
        )
        assert_matches_type(SyncPaginatedCursor[BatchListResponse], batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.batches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(SyncPaginatedCursor[BatchListResponse], batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.batches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(SyncPaginatedCursor[BatchListResponse], batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        batch = client.batches.get(
            batch_id="batch_id",
        )
        assert_matches_type(BatchGetResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        batch = client.batches.get(
            batch_id="batch_id",
            expand=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BatchGetResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.batches.with_raw_response.get(
            batch_id="batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchGetResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.batches.with_streaming_response.get(
            batch_id="batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchGetResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.batches.with_raw_response.get(
                batch_id="",
            )


class TestAsyncBatches:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        batch = await async_client.batches.create(
            config={
                "job": {
                    "configuration_id": "cfg-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "type": "parse_v2",
                }
            },
            source_directory_id="dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        batch = await async_client.batches.create(
            config={
                "job": {
                    "configuration_id": "cfg-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "type": "parse_v2",
                }
            },
            source_directory_id="dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.batches.with_raw_response.create(
            config={
                "job": {
                    "configuration_id": "cfg-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "type": "parse_v2",
                }
            },
            source_directory_id="dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchCreateResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.batches.with_streaming_response.create(
            config={
                "job": {
                    "configuration_id": "cfg-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
                    "type": "parse_v2",
                }
            },
            source_directory_id="dir-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchCreateResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        batch = await async_client.batches.list()
        assert_matches_type(AsyncPaginatedCursor[BatchListResponse], batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        batch = await async_client.batches.list(
            created_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            source_directory_id="source_directory_id",
            status="PENDING",
        )
        assert_matches_type(AsyncPaginatedCursor[BatchListResponse], batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.batches.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[BatchListResponse], batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.batches.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[BatchListResponse], batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        batch = await async_client.batches.get(
            batch_id="batch_id",
        )
        assert_matches_type(BatchGetResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        batch = await async_client.batches.get(
            batch_id="batch_id",
            expand=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(BatchGetResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.batches.with_raw_response.get(
            batch_id="batch_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchGetResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.batches.with_streaming_response.get(
            batch_id="batch_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchGetResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.batches.with_raw_response.get(
                batch_id="",
            )
