# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import (
    ConfigurationResponse,
)
from llama_cloud.pagination import SyncPaginatedCursor, AsyncPaginatedCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfigurations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        configuration = client.configurations.create(
            name="x",
            parameters={
                "product_type": "classify_v2",
                "rules": [
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            },
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        configuration = client.configurations.create(
            name="x",
            parameters={
                "product_type": "classify_v2",
                "rules": [
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
                "mode": "FAST",
                "parsing_configuration": {
                    "lang": "en",
                    "max_pages": 10,
                    "target_pages": "1,3,5-7",
                },
            },
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.configurations.with_raw_response.create(
            name="x",
            parameters={
                "product_type": "classify_v2",
                "rules": [
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.configurations.with_streaming_response.create(
            name="x",
            parameters={
                "product_type": "classify_v2",
                "rules": [
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LlamaCloud) -> None:
        configuration = client.configurations.retrieve(
            config_id="config_id",
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaCloud) -> None:
        configuration = client.configurations.retrieve(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaCloud) -> None:
        response = client.configurations.with_raw_response.retrieve(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaCloud) -> None:
        with client.configurations.with_streaming_response.retrieve(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.configurations.with_raw_response.retrieve(
                config_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LlamaCloud) -> None:
        configuration = client.configurations.update(
            config_id="config_id",
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LlamaCloud) -> None:
        configuration = client.configurations.update(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            parameters={
                "product_type": "classify_v2",
                "rules": [
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
                "mode": "FAST",
                "parsing_configuration": {
                    "lang": "en",
                    "max_pages": 10,
                    "target_pages": "1,3,5-7",
                },
            },
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LlamaCloud) -> None:
        response = client.configurations.with_raw_response.update(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LlamaCloud) -> None:
        with client.configurations.with_streaming_response.update(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(ConfigurationResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.configurations.with_raw_response.update(
                config_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        configuration = client.configurations.list()
        assert_matches_type(SyncPaginatedCursor[ConfigurationResponse], configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        configuration = client.configurations.list(
            latest_only=True,
            name="name",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            product_type=["classify_v2", "extract_v2"],
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncPaginatedCursor[ConfigurationResponse], configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert_matches_type(SyncPaginatedCursor[ConfigurationResponse], configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert_matches_type(SyncPaginatedCursor[ConfigurationResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        configuration = client.configurations.delete(
            config_id="config_id",
        )
        assert configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: LlamaCloud) -> None:
        configuration = client.configurations.delete(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        response = client.configurations.with_raw_response.delete(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = response.parse()
        assert configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with client.configurations.with_streaming_response.delete(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = response.parse()
            assert configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            client.configurations.with_raw_response.delete(
                config_id="",
            )


class TestAsyncConfigurations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        configuration = await async_client.configurations.create(
            name="x",
            parameters={
                "product_type": "classify_v2",
                "rules": [
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            },
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        configuration = await async_client.configurations.create(
            name="x",
            parameters={
                "product_type": "classify_v2",
                "rules": [
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
                "mode": "FAST",
                "parsing_configuration": {
                    "lang": "en",
                    "max_pages": 10,
                    "target_pages": "1,3,5-7",
                },
            },
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.configurations.with_raw_response.create(
            name="x",
            parameters={
                "product_type": "classify_v2",
                "rules": [
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.configurations.with_streaming_response.create(
            name="x",
            parameters={
                "product_type": "classify_v2",
                "rules": [
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        configuration = await async_client.configurations.retrieve(
            config_id="config_id",
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        configuration = await async_client.configurations.retrieve(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.configurations.with_raw_response.retrieve(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.configurations.with_streaming_response.retrieve(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.configurations.with_raw_response.retrieve(
                config_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLlamaCloud) -> None:
        configuration = await async_client.configurations.update(
            config_id="config_id",
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        configuration = await async_client.configurations.update(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            parameters={
                "product_type": "classify_v2",
                "rules": [
                    {
                        "description": "contains invoice number, line items, and total amount",
                        "type": "invoice",
                    }
                ],
                "mode": "FAST",
                "parsing_configuration": {
                    "lang": "en",
                    "max_pages": 10,
                    "target_pages": "1,3,5-7",
                },
            },
        )
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.configurations.with_raw_response.update(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(ConfigurationResponse, configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.configurations.with_streaming_response.update(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(ConfigurationResponse, configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.configurations.with_raw_response.update(
                config_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        configuration = await async_client.configurations.list()
        assert_matches_type(AsyncPaginatedCursor[ConfigurationResponse], configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        configuration = await async_client.configurations.list(
            latest_only=True,
            name="name",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            product_type=["classify_v2", "extract_v2"],
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncPaginatedCursor[ConfigurationResponse], configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.configurations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[ConfigurationResponse], configuration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.configurations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[ConfigurationResponse], configuration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        configuration = await async_client.configurations.delete(
            config_id="config_id",
        )
        assert configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        configuration = await async_client.configurations.delete(
            config_id="config_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.configurations.with_raw_response.delete(
            config_id="config_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        configuration = await response.parse()
        assert configuration is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.configurations.with_streaming_response.delete(
            config_id="config_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            configuration = await response.parse()
            assert configuration is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `config_id` but received ''"):
            await async_client.configurations.with_raw_response.delete(
                config_id="",
            )
