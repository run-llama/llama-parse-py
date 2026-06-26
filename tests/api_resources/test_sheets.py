# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import (
    PresignedURL,
)
from llama_cloud._utils import parse_datetime
from llama_cloud.pagination import SyncPaginatedCursor, AsyncPaginatedCursor
from llama_cloud.types.beta import SheetsJob

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSheets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        sheet = client.sheets.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        sheet = client.sheets.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={
                "extraction_range": "extraction_range",
                "flatten_hierarchical_tables": True,
                "generate_additional_metadata": True,
                "include_hidden_cells": True,
                "sheet_names": ["string"],
                "specialization": "specialization",
                "table_merge_sensitivity": "strong",
                "use_experimental_processing": True,
            },
            configuration={
                "extraction_range": "extraction_range",
                "flatten_hierarchical_tables": True,
                "generate_additional_metadata": True,
                "include_hidden_cells": True,
                "sheet_names": ["string"],
                "specialization": "specialization",
                "table_merge_sensitivity": "strong",
                "use_experimental_processing": True,
            },
            configuration_id="cfg-11111111-2222-3333-4444-555555555555",
            webhook_configurations=[
                {
                    "webhook_events": ["parse.success", "parse.error"],
                    "webhook_headers": {"Authorization": "Bearer sk-..."},
                    "webhook_output_format": "json",
                    "webhook_signing_secret": "whsec_...",
                    "webhook_url": "https://example.com/webhooks/llamacloud",
                }
            ],
        )
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.sheets.with_raw_response.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sheet = response.parse()
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.sheets.with_streaming_response.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sheet = response.parse()
            assert_matches_type(SheetsJob, sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        sheet = client.sheets.list()
        assert_matches_type(SyncPaginatedCursor[SheetsJob], sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        sheet = client.sheets.list(
            configuration_id="configuration_id",
            created_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_results=True,
            job_ids=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="CANCELLED",
        )
        assert_matches_type(SyncPaginatedCursor[SheetsJob], sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.sheets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sheet = response.parse()
        assert_matches_type(SyncPaginatedCursor[SheetsJob], sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.sheets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sheet = response.parse()
            assert_matches_type(SyncPaginatedCursor[SheetsJob], sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_job(self, client: LlamaCloud) -> None:
        sheet = client.sheets.delete_job(
            spreadsheet_job_id="spreadsheet_job_id",
        )
        assert_matches_type(object, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_job_with_all_params(self, client: LlamaCloud) -> None:
        sheet = client.sheets.delete_job(
            spreadsheet_job_id="spreadsheet_job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_job(self, client: LlamaCloud) -> None:
        response = client.sheets.with_raw_response.delete_job(
            spreadsheet_job_id="spreadsheet_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sheet = response.parse()
        assert_matches_type(object, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_job(self, client: LlamaCloud) -> None:
        with client.sheets.with_streaming_response.delete_job(
            spreadsheet_job_id="spreadsheet_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sheet = response.parse()
            assert_matches_type(object, sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_job(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `spreadsheet_job_id` but received ''"):
            client.sheets.with_raw_response.delete_job(
                spreadsheet_job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        sheet = client.sheets.get(
            spreadsheet_job_id="spreadsheet_job_id",
        )
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        sheet = client.sheets.get(
            spreadsheet_job_id="spreadsheet_job_id",
            expand=["string"],
            include_results=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.sheets.with_raw_response.get(
            spreadsheet_job_id="spreadsheet_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sheet = response.parse()
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.sheets.with_streaming_response.get(
            spreadsheet_job_id="spreadsheet_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sheet = response.parse()
            assert_matches_type(SheetsJob, sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `spreadsheet_job_id` but received ''"):
            client.sheets.with_raw_response.get(
                spreadsheet_job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_result_table(self, client: LlamaCloud) -> None:
        sheet = client.sheets.get_result_table(
            region_type="cell_metadata",
            spreadsheet_job_id="spreadsheet_job_id",
            region_id="region_id",
        )
        assert_matches_type(PresignedURL, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_result_table_with_all_params(self, client: LlamaCloud) -> None:
        sheet = client.sheets.get_result_table(
            region_type="cell_metadata",
            spreadsheet_job_id="spreadsheet_job_id",
            region_id="region_id",
            expires_at_seconds=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PresignedURL, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_result_table(self, client: LlamaCloud) -> None:
        response = client.sheets.with_raw_response.get_result_table(
            region_type="cell_metadata",
            spreadsheet_job_id="spreadsheet_job_id",
            region_id="region_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sheet = response.parse()
        assert_matches_type(PresignedURL, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_result_table(self, client: LlamaCloud) -> None:
        with client.sheets.with_streaming_response.get_result_table(
            region_type="cell_metadata",
            spreadsheet_job_id="spreadsheet_job_id",
            region_id="region_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sheet = response.parse()
            assert_matches_type(PresignedURL, sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_result_table(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `spreadsheet_job_id` but received ''"):
            client.sheets.with_raw_response.get_result_table(
                region_type="cell_metadata",
                spreadsheet_job_id="",
                region_id="region_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `region_id` but received ''"):
            client.sheets.with_raw_response.get_result_table(
                region_type="cell_metadata",
                spreadsheet_job_id="spreadsheet_job_id",
                region_id="",
            )


class TestAsyncSheets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        sheet = await async_client.sheets.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        sheet = await async_client.sheets.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config={
                "extraction_range": "extraction_range",
                "flatten_hierarchical_tables": True,
                "generate_additional_metadata": True,
                "include_hidden_cells": True,
                "sheet_names": ["string"],
                "specialization": "specialization",
                "table_merge_sensitivity": "strong",
                "use_experimental_processing": True,
            },
            configuration={
                "extraction_range": "extraction_range",
                "flatten_hierarchical_tables": True,
                "generate_additional_metadata": True,
                "include_hidden_cells": True,
                "sheet_names": ["string"],
                "specialization": "specialization",
                "table_merge_sensitivity": "strong",
                "use_experimental_processing": True,
            },
            configuration_id="cfg-11111111-2222-3333-4444-555555555555",
            webhook_configurations=[
                {
                    "webhook_events": ["parse.success", "parse.error"],
                    "webhook_headers": {"Authorization": "Bearer sk-..."},
                    "webhook_output_format": "json",
                    "webhook_signing_secret": "whsec_...",
                    "webhook_url": "https://example.com/webhooks/llamacloud",
                }
            ],
        )
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.sheets.with_raw_response.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sheet = await response.parse()
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.sheets.with_streaming_response.create(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sheet = await response.parse()
            assert_matches_type(SheetsJob, sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        sheet = await async_client.sheets.list()
        assert_matches_type(AsyncPaginatedCursor[SheetsJob], sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        sheet = await async_client.sheets.list(
            configuration_id="configuration_id",
            created_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            include_results=True,
            job_ids=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="CANCELLED",
        )
        assert_matches_type(AsyncPaginatedCursor[SheetsJob], sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.sheets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sheet = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[SheetsJob], sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.sheets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sheet = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[SheetsJob], sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_job(self, async_client: AsyncLlamaCloud) -> None:
        sheet = await async_client.sheets.delete_job(
            spreadsheet_job_id="spreadsheet_job_id",
        )
        assert_matches_type(object, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_job_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        sheet = await async_client.sheets.delete_job(
            spreadsheet_job_id="spreadsheet_job_id",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_job(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.sheets.with_raw_response.delete_job(
            spreadsheet_job_id="spreadsheet_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sheet = await response.parse()
        assert_matches_type(object, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_job(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.sheets.with_streaming_response.delete_job(
            spreadsheet_job_id="spreadsheet_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sheet = await response.parse()
            assert_matches_type(object, sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_job(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `spreadsheet_job_id` but received ''"):
            await async_client.sheets.with_raw_response.delete_job(
                spreadsheet_job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        sheet = await async_client.sheets.get(
            spreadsheet_job_id="spreadsheet_job_id",
        )
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        sheet = await async_client.sheets.get(
            spreadsheet_job_id="spreadsheet_job_id",
            expand=["string"],
            include_results=True,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.sheets.with_raw_response.get(
            spreadsheet_job_id="spreadsheet_job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sheet = await response.parse()
        assert_matches_type(SheetsJob, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.sheets.with_streaming_response.get(
            spreadsheet_job_id="spreadsheet_job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sheet = await response.parse()
            assert_matches_type(SheetsJob, sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `spreadsheet_job_id` but received ''"):
            await async_client.sheets.with_raw_response.get(
                spreadsheet_job_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_result_table(self, async_client: AsyncLlamaCloud) -> None:
        sheet = await async_client.sheets.get_result_table(
            region_type="cell_metadata",
            spreadsheet_job_id="spreadsheet_job_id",
            region_id="region_id",
        )
        assert_matches_type(PresignedURL, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_result_table_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        sheet = await async_client.sheets.get_result_table(
            region_type="cell_metadata",
            spreadsheet_job_id="spreadsheet_job_id",
            region_id="region_id",
            expires_at_seconds=0,
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(PresignedURL, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_result_table(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.sheets.with_raw_response.get_result_table(
            region_type="cell_metadata",
            spreadsheet_job_id="spreadsheet_job_id",
            region_id="region_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sheet = await response.parse()
        assert_matches_type(PresignedURL, sheet, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_result_table(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.sheets.with_streaming_response.get_result_table(
            region_type="cell_metadata",
            spreadsheet_job_id="spreadsheet_job_id",
            region_id="region_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sheet = await response.parse()
            assert_matches_type(PresignedURL, sheet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_result_table(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `spreadsheet_job_id` but received ''"):
            await async_client.sheets.with_raw_response.get_result_table(
                region_type="cell_metadata",
                spreadsheet_job_id="",
                region_id="region_id",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `region_id` but received ''"):
            await async_client.sheets.with_raw_response.get_result_table(
                region_type="cell_metadata",
                spreadsheet_job_id="spreadsheet_job_id",
                region_id="",
            )
