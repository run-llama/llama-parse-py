# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import (
    ParsingGetResponse,
    ParsingListResponse,
    ParsingCreateResponse,
)
from llama_cloud._utils import parse_datetime
from llama_cloud.pagination import SyncPaginatedCursor, AsyncPaginatedCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParsing:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        parsing = client.parsing.create(
            tier="fast",
            version="latest",
        )
        assert_matches_type(ParsingCreateResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        parsing = client.parsing.create(
            tier="fast",
            version="latest",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agentic_options={"custom_prompt": "custom_prompt"},
            client_name="client_name",
            configuration_id="configuration_id",
            crop_box={
                "bottom": 0,
                "left": 0,
                "right": 0,
                "top": 0,
            },
            disable_cache=True,
            fast_options={},
            file_id="file_id",
            http_proxy="https:",
            input_options={
                "html": {
                    "make_all_elements_visible": True,
                    "remove_fixed_elements": True,
                    "remove_navigation_elements": True,
                },
                "image": {"camera_photo_correction": True},
                "pdf": {},
                "presentation": {
                    "out_of_bounds_content": True,
                    "skip_embedded_data": True,
                },
                "spreadsheet": {
                    "detect_sub_tables_in_sheets": True,
                    "force_formula_computation_in_sheets": True,
                    "include_hidden_sheets": True,
                },
            },
            output_options={
                "additional_outputs": ["stripped_md", "concatenated_stripped_txt", "word_bbox"],
                "extract_printed_page_number": True,
                "granular_bboxes": ["word", "line", "cell"],
                "images_to_save": ["embedded"],
                "markdown": {
                    "annotate_links": True,
                    "inline_images": True,
                    "tables": {
                        "compact_markdown_tables": True,
                        "markdown_table_multiline_separator": "markdown_table_multiline_separator",
                        "merge_continued_tables": True,
                        "output_tables_as_markdown": True,
                    },
                },
                "spatial_text": {
                    "do_not_unroll_columns": True,
                    "preserve_layout_alignment_across_pages": True,
                    "preserve_very_small_text": True,
                },
                "tables_as_spreadsheet": {
                    "enable": True,
                    "guess_sheet_name": True,
                },
            },
            page_ranges={
                "max_pages": 1,
                "target_pages": "target_pages",
            },
            processing_control={
                "job_failure_conditions": {
                    "allowed_page_failure_ratio": 1,
                    "fail_on_buggy_font": True,
                    "fail_on_image_extraction_error": True,
                    "fail_on_image_ocr_error": True,
                    "fail_on_markdown_reconstruction_error": True,
                },
                "timeouts": {
                    "base_in_seconds": 1,
                    "extra_time_per_page_in_seconds": 1,
                },
            },
            processing_options={
                "aggressive_table_extraction": True,
                "auto_mode_configuration": [
                    {
                        "parsing_conf": {
                            "adaptive_long_table": True,
                            "aggressive_table_extraction": True,
                            "crop_box": {
                                "bottom": 0,
                                "left": 0,
                                "right": 0,
                                "top": 0,
                            },
                            "custom_prompt": "custom_prompt",
                            "extract_layout": True,
                            "high_res_ocr": True,
                            "ignore": {
                                "ignore_diagonal_text": True,
                                "ignore_hidden_text": True,
                            },
                            "language": "language",
                            "outlined_table_extraction": True,
                            "presentation": {
                                "out_of_bounds_content": True,
                                "skip_embedded_data": True,
                            },
                            "spatial_text": {
                                "do_not_unroll_columns": True,
                                "preserve_layout_alignment_across_pages": True,
                                "preserve_very_small_text": True,
                            },
                            "specialized_chart_parsing": "agentic",
                            "tier": "agentic",
                            "version": "latest",
                        },
                        "filename_match_glob": "*.txt",
                        "filename_match_glob_list": ["string"],
                        "filename_regexp": "filename_regexp",
                        "filename_regexp_mode": "filename_regexp_mode",
                        "full_page_image_in_page": True,
                        "full_page_image_in_page_threshold": 0,
                        "image_in_page": True,
                        "layout_element_in_page": "layout_element_in_page",
                        "layout_element_in_page_confidence_threshold": 0,
                        "page_contains_at_least_n_charts": 0,
                        "page_contains_at_least_n_images": 0,
                        "page_contains_at_least_n_layout_elements": 0,
                        "page_contains_at_least_n_lines": 0,
                        "page_contains_at_least_n_links": 0,
                        "page_contains_at_least_n_numbers": 0,
                        "page_contains_at_least_n_percent_numbers": 0,
                        "page_contains_at_least_n_tables": 0,
                        "page_contains_at_least_n_words": 0,
                        "page_contains_at_most_n_charts": 0,
                        "page_contains_at_most_n_images": 0,
                        "page_contains_at_most_n_layout_elements": 0,
                        "page_contains_at_most_n_lines": 0,
                        "page_contains_at_most_n_links": 0,
                        "page_contains_at_most_n_numbers": 0,
                        "page_contains_at_most_n_percent_numbers": 0,
                        "page_contains_at_most_n_tables": 0,
                        "page_contains_at_most_n_words": 0,
                        "page_longer_than_n_chars": 0,
                        "page_md_error": True,
                        "page_shorter_than_n_chars": 0,
                        "regexp_in_page": "regexp_in_page",
                        "regexp_in_page_mode": "regexp_in_page_mode",
                        "table_in_page": True,
                        "text_in_page": "text_in_page",
                        "trigger_mode": "trigger_mode",
                    }
                ],
                "cost_optimizer": {"enable": True},
                "disable_heuristics": True,
                "ignore": {
                    "ignore_diagonal_text": True,
                    "ignore_hidden_text": True,
                    "ignore_text_in_image": True,
                },
                "ocr_parameters": {"languages": ["abq"]},
                "specialized_chart_parsing": "agentic",
            },
            source_url="https:",
            user_metadata={
                "owner": "jerry",
                "team": "research",
            },
            webhook_configuration_ids=["whc-...", "whc-..."],
            webhook_configurations=[
                {
                    "webhook_events": ["parse.success", "parse.error"],
                    "webhook_headers": {"foo": "bar"},
                    "webhook_output_format": "json",
                    "webhook_signing_secret": "webhook_signing_secret",
                    "webhook_url": "https:",
                }
            ],
        )
        assert_matches_type(ParsingCreateResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        response = client.parsing.with_raw_response.create(
            tier="fast",
            version="latest",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = response.parse()
        assert_matches_type(ParsingCreateResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with client.parsing.with_streaming_response.create(
            tier="fast",
            version="latest",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = response.parse()
            assert_matches_type(ParsingCreateResponse, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        parsing = client.parsing.list()
        assert_matches_type(SyncPaginatedCursor[ParsingListResponse], parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        parsing = client.parsing.list(
            created_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            job_ids=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="CANCELLED",
        )
        assert_matches_type(SyncPaginatedCursor[ParsingListResponse], parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        response = client.parsing.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = response.parse()
        assert_matches_type(SyncPaginatedCursor[ParsingListResponse], parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with client.parsing.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = response.parse()
            assert_matches_type(SyncPaginatedCursor[ParsingListResponse], parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        parsing = client.parsing.get(
            job_id="job_id",
        )
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_with_all_params(self, client: LlamaCloud) -> None:
        parsing = client.parsing.get(
            job_id="job_id",
            expand=["string"],
            image_filenames="image_filenames",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        response = client.parsing.with_raw_response.get(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = response.parse()
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with client.parsing.with_streaming_response.get(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = response.parse()
            assert_matches_type(ParsingGetResponse, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.parsing.with_raw_response.get(
                job_id="",
            )


class TestAsyncParsing:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.create(
            tier="fast",
            version="latest",
        )
        assert_matches_type(ParsingCreateResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.create(
            tier="fast",
            version="latest",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            agentic_options={"custom_prompt": "custom_prompt"},
            client_name="client_name",
            configuration_id="configuration_id",
            crop_box={
                "bottom": 0,
                "left": 0,
                "right": 0,
                "top": 0,
            },
            disable_cache=True,
            fast_options={},
            file_id="file_id",
            http_proxy="https:",
            input_options={
                "html": {
                    "make_all_elements_visible": True,
                    "remove_fixed_elements": True,
                    "remove_navigation_elements": True,
                },
                "image": {"camera_photo_correction": True},
                "pdf": {},
                "presentation": {
                    "out_of_bounds_content": True,
                    "skip_embedded_data": True,
                },
                "spreadsheet": {
                    "detect_sub_tables_in_sheets": True,
                    "force_formula_computation_in_sheets": True,
                    "include_hidden_sheets": True,
                },
            },
            output_options={
                "additional_outputs": ["stripped_md", "concatenated_stripped_txt", "word_bbox"],
                "extract_printed_page_number": True,
                "granular_bboxes": ["word", "line", "cell"],
                "images_to_save": ["embedded"],
                "markdown": {
                    "annotate_links": True,
                    "inline_images": True,
                    "tables": {
                        "compact_markdown_tables": True,
                        "markdown_table_multiline_separator": "markdown_table_multiline_separator",
                        "merge_continued_tables": True,
                        "output_tables_as_markdown": True,
                    },
                },
                "spatial_text": {
                    "do_not_unroll_columns": True,
                    "preserve_layout_alignment_across_pages": True,
                    "preserve_very_small_text": True,
                },
                "tables_as_spreadsheet": {
                    "enable": True,
                    "guess_sheet_name": True,
                },
            },
            page_ranges={
                "max_pages": 1,
                "target_pages": "target_pages",
            },
            processing_control={
                "job_failure_conditions": {
                    "allowed_page_failure_ratio": 1,
                    "fail_on_buggy_font": True,
                    "fail_on_image_extraction_error": True,
                    "fail_on_image_ocr_error": True,
                    "fail_on_markdown_reconstruction_error": True,
                },
                "timeouts": {
                    "base_in_seconds": 1,
                    "extra_time_per_page_in_seconds": 1,
                },
            },
            processing_options={
                "aggressive_table_extraction": True,
                "auto_mode_configuration": [
                    {
                        "parsing_conf": {
                            "adaptive_long_table": True,
                            "aggressive_table_extraction": True,
                            "crop_box": {
                                "bottom": 0,
                                "left": 0,
                                "right": 0,
                                "top": 0,
                            },
                            "custom_prompt": "custom_prompt",
                            "extract_layout": True,
                            "high_res_ocr": True,
                            "ignore": {
                                "ignore_diagonal_text": True,
                                "ignore_hidden_text": True,
                            },
                            "language": "language",
                            "outlined_table_extraction": True,
                            "presentation": {
                                "out_of_bounds_content": True,
                                "skip_embedded_data": True,
                            },
                            "spatial_text": {
                                "do_not_unroll_columns": True,
                                "preserve_layout_alignment_across_pages": True,
                                "preserve_very_small_text": True,
                            },
                            "specialized_chart_parsing": "agentic",
                            "tier": "agentic",
                            "version": "latest",
                        },
                        "filename_match_glob": "*.txt",
                        "filename_match_glob_list": ["string"],
                        "filename_regexp": "filename_regexp",
                        "filename_regexp_mode": "filename_regexp_mode",
                        "full_page_image_in_page": True,
                        "full_page_image_in_page_threshold": 0,
                        "image_in_page": True,
                        "layout_element_in_page": "layout_element_in_page",
                        "layout_element_in_page_confidence_threshold": 0,
                        "page_contains_at_least_n_charts": 0,
                        "page_contains_at_least_n_images": 0,
                        "page_contains_at_least_n_layout_elements": 0,
                        "page_contains_at_least_n_lines": 0,
                        "page_contains_at_least_n_links": 0,
                        "page_contains_at_least_n_numbers": 0,
                        "page_contains_at_least_n_percent_numbers": 0,
                        "page_contains_at_least_n_tables": 0,
                        "page_contains_at_least_n_words": 0,
                        "page_contains_at_most_n_charts": 0,
                        "page_contains_at_most_n_images": 0,
                        "page_contains_at_most_n_layout_elements": 0,
                        "page_contains_at_most_n_lines": 0,
                        "page_contains_at_most_n_links": 0,
                        "page_contains_at_most_n_numbers": 0,
                        "page_contains_at_most_n_percent_numbers": 0,
                        "page_contains_at_most_n_tables": 0,
                        "page_contains_at_most_n_words": 0,
                        "page_longer_than_n_chars": 0,
                        "page_md_error": True,
                        "page_shorter_than_n_chars": 0,
                        "regexp_in_page": "regexp_in_page",
                        "regexp_in_page_mode": "regexp_in_page_mode",
                        "table_in_page": True,
                        "text_in_page": "text_in_page",
                        "trigger_mode": "trigger_mode",
                    }
                ],
                "cost_optimizer": {"enable": True},
                "disable_heuristics": True,
                "ignore": {
                    "ignore_diagonal_text": True,
                    "ignore_hidden_text": True,
                    "ignore_text_in_image": True,
                },
                "ocr_parameters": {"languages": ["abq"]},
                "specialized_chart_parsing": "agentic",
            },
            source_url="https:",
            user_metadata={
                "owner": "jerry",
                "team": "research",
            },
            webhook_configuration_ids=["whc-...", "whc-..."],
            webhook_configurations=[
                {
                    "webhook_events": ["parse.success", "parse.error"],
                    "webhook_headers": {"foo": "bar"},
                    "webhook_output_format": "json",
                    "webhook_signing_secret": "webhook_signing_secret",
                    "webhook_url": "https:",
                }
            ],
        )
        assert_matches_type(ParsingCreateResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.with_raw_response.create(
            tier="fast",
            version="latest",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = await response.parse()
        assert_matches_type(ParsingCreateResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.with_streaming_response.create(
            tier="fast",
            version="latest",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = await response.parse()
            assert_matches_type(ParsingCreateResponse, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.list()
        assert_matches_type(AsyncPaginatedCursor[ParsingListResponse], parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.list(
            created_at_on_or_after=parse_datetime("2019-12-27T18:11:19.117Z"),
            created_at_on_or_before=parse_datetime("2019-12-27T18:11:19.117Z"),
            job_ids=["string", "string"],
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            page_size=0,
            page_token="page_token",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            status="CANCELLED",
        )
        assert_matches_type(AsyncPaginatedCursor[ParsingListResponse], parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = await response.parse()
        assert_matches_type(AsyncPaginatedCursor[ParsingListResponse], parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = await response.parse()
            assert_matches_type(AsyncPaginatedCursor[ParsingListResponse], parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.get(
            job_id="job_id",
        )
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        parsing = await async_client.parsing.get(
            job_id="job_id",
            expand=["string"],
            image_filenames="image_filenames",
            organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        response = await async_client.parsing.with_raw_response.get(
            job_id="job_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parsing = await response.parse()
        assert_matches_type(ParsingGetResponse, parsing, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        async with async_client.parsing.with_streaming_response.get(
            job_id="job_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parsing = await response.parse()
            assert_matches_type(ParsingGetResponse, parsing, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.parsing.with_raw_response.get(
                job_id="",
            )
