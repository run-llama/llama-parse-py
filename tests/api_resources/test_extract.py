# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import (
    ExtractV2Job,
    ConfigurationCreate,
    ExtractV2SchemaValidateResponse,
)
from llama_cloud._utils import parse_datetime
from llama_cloud.pagination import SyncPaginatedCursor, AsyncPaginatedCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExtract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        extract = client.extract.create(
            file_input="dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        )
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        extract = client.extract.create(
            file_input="dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            configuration={
                "data_schema": {
                    "properties": {
                        "vendor_name": "bar",
                        "total_amount": "bar",
                    },
                    "required": ["vendor_name", "total_amount"],
                    "type": "object",
                },
                "cite_sources": True,
                "confidence_scores": True,
                "extraction_target": "per_doc",
                "max_pages": 10,
                "parse_config_id": "cfg-11111111-2222-3333-4444-555555555555",
                "parse_tier": "fast",
                "system_prompt": "Extract all monetary values in USD. If a currency is not specified, assume USD.",
                "target_pages": "1,3,5-7",
                "tier": "cost_effective",
                "version": "latest",
            },
            configuration_id="cfg-11111111-2222-3333-4444-555555555555",
            webhook_configurations=[
                {
                    "webhook_events": ["parse.success", "parse.error"],
                    "webhook_headers": {"Authorization": "Bearer sk-..."},
                    "webhook_output_format": "json",
                    "webhook_url": "https://example.com/webhooks/llamacloud",
                }
            ],
        )
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.extract.with_raw_response.create(
            file_input="dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.extract.with_streaming_response.create(
            file_input="dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractV2Job, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        extract = client.extract.list()
        assert_matches_type(SyncPaginatedCursor[ExtractV2Job], extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        extract = client.extract.list(
            configuration_id="cfg-11111111-2222-3333-4444-555555555555",
            created_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            document_input_type="document_input_type",
            document_input_value="document_input_value",
            expand=["string"],
            file_input="file_input",
            job_ids=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="PENDING",
        )
        assert_matches_type(SyncPaginatedCursor[ExtractV2Job], extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.extract.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(SyncPaginatedCursor[ExtractV2Job], extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.extract.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(SyncPaginatedCursor[ExtractV2Job], extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        extract = client.extract.delete(
            job_id="job_id",
        )
        assert_matches_type(object, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: LlamaCloud) -> None:
        extract = client.extract.delete(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        response = client.extract.with_raw_response.delete(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(object, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with client.extract.with_streaming_response.delete(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(object, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.with_raw_response.delete(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_schema(self, client: LlamaCloud) -> None:
        extract = client.extract.generate_schema()
        assert_matches_type(ConfigurationCreate, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_schema_with_all_params(self, client: LlamaCloud) -> None:
        extract = client.extract.generate_schema(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_schema={"foo": {"foo": "bar"}},
            file_id="dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            name="invoice_extraction",
            prompt="Extract vendor name, invoice number, date, line items with descriptions and amounts, and total amount from invoices.",
        )
        assert_matches_type(ConfigurationCreate, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_schema(self, client: LlamaCloud) -> None:
        response = client.extract.with_raw_response.generate_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ConfigurationCreate, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_schema(self, client: LlamaCloud) -> None:
        with client.extract.with_streaming_response.generate_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ConfigurationCreate, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        extract = client.extract.get(
            job_id="job_id",
        )
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        extract = client.extract.get(
            job_id="job_id",
            expand=["string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.extract.with_raw_response.get(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.extract.with_streaming_response.get(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractV2Job, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.extract.with_raw_response.get(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_validate_schema(self, client: LlamaCloud) -> None:
        extract = client.extract.validate_schema(
            data_schema={
                "properties": {
                    "vendor_name": "bar",
                    "invoice_number": "bar",
                    "total_amount": "bar",
                    "line_items": "bar",
                },
                "required": ["vendor_name", "invoice_number", "total_amount"],
                "type": "object",
            },
        )
        assert_matches_type(ExtractV2SchemaValidateResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_validate_schema(self, client: LlamaCloud) -> None:
        response = client.extract.with_raw_response.validate_schema(
            data_schema={
                "properties": {
                    "vendor_name": "bar",
                    "invoice_number": "bar",
                    "total_amount": "bar",
                    "line_items": "bar",
                },
                "required": ["vendor_name", "invoice_number", "total_amount"],
                "type": "object",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = response.parse()
        assert_matches_type(ExtractV2SchemaValidateResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_validate_schema(self, client: LlamaCloud) -> None:
        with client.extract.with_streaming_response.validate_schema(
            data_schema={
                "properties": {
                    "vendor_name": "bar",
                    "invoice_number": "bar",
                    "total_amount": "bar",
                    "line_items": "bar",
                },
                "required": ["vendor_name", "invoice_number", "total_amount"],
                "type": "object",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = response.parse()
            assert_matches_type(ExtractV2SchemaValidateResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncExtract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        extract = await async_client.extract.create(
            file_input="dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        )
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        extract = await async_client.extract.create(
            file_input="dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            configuration={
                "data_schema": {
                    "properties": {
                        "vendor_name": "bar",
                        "total_amount": "bar",
                    },
                    "required": ["vendor_name", "total_amount"],
                    "type": "object",
                },
                "cite_sources": True,
                "confidence_scores": True,
                "extraction_target": "per_doc",
                "max_pages": 10,
                "parse_config_id": "cfg-11111111-2222-3333-4444-555555555555",
                "parse_tier": "fast",
                "system_prompt": "Extract all monetary values in USD. If a currency is not specified, assume USD.",
                "target_pages": "1,3,5-7",
                "tier": "cost_effective",
                "version": "latest",
            },
            configuration_id="cfg-11111111-2222-3333-4444-555555555555",
            webhook_configurations=[
                {
                    "webhook_events": ["parse.success", "parse.error"],
                    "webhook_headers": {"Authorization": "Bearer sk-..."},
                    "webhook_output_format": "json",
                    "webhook_url": "https://example.com/webhooks/llamacloud",
                }
            ],
        )
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.with_raw_response.create(
            file_input="dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.with_streaming_response.create(
            file_input="dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractV2Job, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        extract = await async_client.extract.list()
        assert_matches_type(AsyncPaginatedCursor[ExtractV2Job], extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        extract = await async_client.extract.list(
            configuration_id="cfg-11111111-2222-3333-4444-555555555555",
            created_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            document_input_type="document_input_type",
            document_input_value="document_input_value",
            expand=["string"],
            file_input="file_input",
            job_ids=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="PENDING",
        )
        assert_matches_type(AsyncPaginatedCursor[ExtractV2Job], extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[ExtractV2Job], extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[ExtractV2Job], extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        extract = await async_client.extract.delete(
            job_id="job_id",
        )
        assert_matches_type(object, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        extract = await async_client.extract.delete(
            job_id="job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.with_raw_response.delete(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(object, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.with_streaming_response.delete(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(object, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.with_raw_response.delete(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_schema(self, async_client: AsyncLlamaCloud) -> None:
        extract = await async_client.extract.generate_schema()
        assert_matches_type(ConfigurationCreate, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_schema_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        extract = await async_client.extract.generate_schema(
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            data_schema={"foo": {"foo": "bar"}},
            file_id="dfl-aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee",
            name="invoice_extraction",
            prompt="Extract vendor name, invoice number, date, line items with descriptions and amounts, and total amount from invoices.",
        )
        assert_matches_type(ConfigurationCreate, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_schema(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.with_raw_response.generate_schema()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ConfigurationCreate, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_schema(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.with_streaming_response.generate_schema() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ConfigurationCreate, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        extract = await async_client.extract.get(
            job_id="job_id",
        )
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        extract = await async_client.extract.get(
            job_id="job_id",
            expand=["string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.with_raw_response.get(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractV2Job, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.with_streaming_response.get(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractV2Job, extract, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.extract.with_raw_response.get(
                job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_validate_schema(self, async_client: AsyncLlamaCloud) -> None:
        extract = await async_client.extract.validate_schema(
            data_schema={
                "properties": {
                    "vendor_name": "bar",
                    "invoice_number": "bar",
                    "total_amount": "bar",
                    "line_items": "bar",
                },
                "required": ["vendor_name", "invoice_number", "total_amount"],
                "type": "object",
            },
        )
        assert_matches_type(ExtractV2SchemaValidateResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_validate_schema(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.extract.with_raw_response.validate_schema(
            data_schema={
                "properties": {
                    "vendor_name": "bar",
                    "invoice_number": "bar",
                    "total_amount": "bar",
                    "line_items": "bar",
                },
                "required": ["vendor_name", "invoice_number", "total_amount"],
                "type": "object",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        extract = await response.parse()
        assert_matches_type(ExtractV2SchemaValidateResponse, extract, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_validate_schema(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.extract.with_streaming_response.validate_schema(
            data_schema={
                "properties": {
                    "vendor_name": "bar",
                    "invoice_number": "bar",
                    "total_amount": "bar",
                    "line_items": "bar",
                },
                "required": ["vendor_name", "invoice_number", "total_amount"],
                "type": "object",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            extract = await response.parse()
            assert_matches_type(ExtractV2SchemaValidateResponse, extract, path=["response"])

        assert cast(Any, response.is_closed) is True
