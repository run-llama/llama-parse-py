# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud._utils import parse_datetime
from llama_cloud.pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from llama_cloud.types.beta import (
    SplitGetResponse,
    SplitListResponse,
    SplitCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSplit:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        split = client.beta.split.create(
            document_input={
                "type": "type",
                "value": "value",
            },
        )
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        split = client.beta.split.create(
            document_input={
                "type": "type",
                "value": "value",
            },
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            configuration={
                "categories": [
                    {
                        "name": "x",
                        "description": "x",
                    }
                ],
                "splitting_strategy": {"allow_uncategorized": "forbid"},
            },
            configuration_id="configuration_id",
        )
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.beta.split.with_raw_response.create(
            document_input={
                "type": "type",
                "value": "value",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = response.parse()
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.beta.split.with_streaming_response.create(
            document_input={
                "type": "type",
                "value": "value",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = response.parse()
            assert_matches_type(SplitCreateResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        split = client.beta.split.list()
        assert_matches_type(SyncPaginatedCursor[SplitListResponse], split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        split = client.beta.split.list(
            created_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            job_ids=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="cancelled",
        )
        assert_matches_type(SyncPaginatedCursor[SplitListResponse], split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.beta.split.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = response.parse()
        assert_matches_type(SyncPaginatedCursor[SplitListResponse], split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.beta.split.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = response.parse()
            assert_matches_type(SyncPaginatedCursor[SplitListResponse], split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        split = client.beta.split.get(
            split_job_id="split_job_id",
        )
        assert_matches_type(SplitGetResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        split = client.beta.split.get(
            split_job_id="split_job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SplitGetResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.beta.split.with_raw_response.get(
            split_job_id="split_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = response.parse()
        assert_matches_type(SplitGetResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.beta.split.with_streaming_response.get(
            split_job_id="split_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = response.parse()
            assert_matches_type(SplitGetResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `split_job_id` but received ''"):
            client.beta.split.with_raw_response.get(
                split_job_id="",
            )


class TestAsyncSplit:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        split = await async_client.beta.split.create(
            document_input={
                "type": "type",
                "value": "value",
            },
        )
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        split = await async_client.beta.split.create(
            document_input={
                "type": "type",
                "value": "value",
            },
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            configuration={
                "categories": [
                    {
                        "name": "x",
                        "description": "x",
                    }
                ],
                "splitting_strategy": {"allow_uncategorized": "forbid"},
            },
            configuration_id="configuration_id",
        )
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.split.with_raw_response.create(
            document_input={
                "type": "type",
                "value": "value",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = await response.parse()
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.split.with_streaming_response.create(
            document_input={
                "type": "type",
                "value": "value",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = await response.parse()
            assert_matches_type(SplitCreateResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        split = await async_client.beta.split.list()
        assert_matches_type(AsyncPaginatedCursor[SplitListResponse], split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        split = await async_client.beta.split.list(
            created_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            job_ids=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="cancelled",
        )
        assert_matches_type(AsyncPaginatedCursor[SplitListResponse], split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.split.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[SplitListResponse], split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.split.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[SplitListResponse], split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        split = await async_client.beta.split.get(
            split_job_id="split_job_id",
        )
        assert_matches_type(SplitGetResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        split = await async_client.beta.split.get(
            split_job_id="split_job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SplitGetResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.beta.split.with_raw_response.get(
            split_job_id="split_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = await response.parse()
        assert_matches_type(SplitGetResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.beta.split.with_streaming_response.get(
            split_job_id="split_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = await response.parse()
            assert_matches_type(SplitGetResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `split_job_id` but received ''"):
            await async_client.beta.split.with_raw_response.get(
                split_job_id="",
            )
