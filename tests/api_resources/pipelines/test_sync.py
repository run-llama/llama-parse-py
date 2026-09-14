# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import Pipeline

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSync:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            sync = client.pipelines.sync.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(Pipeline, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.sync.with_raw_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Pipeline, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.sync.with_streaming_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                sync = response.parse()
                assert_matches_type(Pipeline, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.sync.with_raw_response.create(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            sync = client.pipelines.sync.cancel(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(Pipeline, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.sync.with_raw_response.cancel(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = response.parse()
        assert_matches_type(Pipeline, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.sync.with_streaming_response.cancel(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                sync = response.parse()
                assert_matches_type(Pipeline, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.sync.with_raw_response.cancel(
                    "",
                )


class TestAsyncSync:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            sync = await async_client.pipelines.sync.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(Pipeline, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.sync.with_raw_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Pipeline, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.sync.with_streaming_response.create(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                sync = await response.parse()
                assert_matches_type(Pipeline, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.sync.with_raw_response.create(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            sync = await async_client.pipelines.sync.cancel(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(Pipeline, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.sync.with_raw_response.cancel(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sync = await response.parse()
        assert_matches_type(Pipeline, sync, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.sync.with_streaming_response.cancel(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                sync = await response.parse()
                assert_matches_type(Pipeline, sync, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.sync.with_raw_response.cancel(
                    "",
                )
