# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from tests.utils import assert_matches_type
from llama_cloud.types import (
    Pipeline,
    PipelineListResponse,
    PipelineRetrieveResponse,
    ManagedIngestionStatusResponse,
)

# pyright: reportDeprecated=false

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPipelines:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.create(
                name="x",
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.create(
                name="x",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_sink={
                    "component": {"foo": "bar"},
                    "name": "name",
                    "sink_type": "ASTRA_DB",
                },
                data_sink_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                embedding_config={
                    "component": {
                        "additional_kwargs": {"foo": "bar"},
                        "api_base": "api_base",
                        "api_key": "api_key",
                        "api_version": "api_version",
                        "azure_deployment": "azure_deployment",
                        "azure_endpoint": "azure_endpoint",
                        "class_name": "class_name",
                        "default_headers": {"foo": "string"},
                        "dimensions": 0,
                        "embed_batch_size": 1,
                        "max_retries": 0,
                        "model_name": "model_name",
                        "num_workers": 0,
                        "reuse_client": True,
                        "timeout": 0,
                    },
                    "type": "AZURE_EMBEDDING",
                },
                embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                llama_parse_parameters={
                    "adaptive_long_table": True,
                    "aggressive_table_extraction": True,
                    "annotate_links": True,
                    "auto_mode": True,
                    "auto_mode_configuration_json": "auto_mode_configuration_json",
                    "auto_mode_trigger_on_image_in_page": True,
                    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
                    "auto_mode_trigger_on_table_in_page": True,
                    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
                    "azure_openai_api_version": "azure_openai_api_version",
                    "azure_openai_deployment_name": "azure_openai_deployment_name",
                    "azure_openai_endpoint": "azure_openai_endpoint",
                    "azure_openai_key": "azure_openai_key",
                    "bbox_bottom": 0,
                    "bbox_left": 0,
                    "bbox_right": 0,
                    "bbox_top": 0,
                    "bounding_box": "bounding_box",
                    "compact_markdown_table": True,
                    "complemental_formatting_instruction": "complemental_formatting_instruction",
                    "content_guideline_instruction": "content_guideline_instruction",
                    "continuous_mode": True,
                    "disable_image_extraction": True,
                    "disable_ocr": True,
                    "disable_reconstruction": True,
                    "do_not_cache": True,
                    "do_not_unroll_columns": True,
                    "enable_cost_optimizer": True,
                    "extract_charts": True,
                    "extract_layout": True,
                    "extract_printed_page_number": True,
                    "fast_mode": True,
                    "formatting_instruction": "formatting_instruction",
                    "gpt4o_api_key": "gpt4o_api_key",
                    "gpt4o_mode": True,
                    "guess_xlsx_sheet_name": True,
                    "hide_footers": True,
                    "hide_headers": True,
                    "high_res_ocr": True,
                    "html_make_all_elements_visible": True,
                    "html_remove_fixed_elements": True,
                    "html_remove_navigation_elements": True,
                    "http_proxy": "http_proxy",
                    "ignore_document_elements_for_layout_detection": True,
                    "images_to_save": ["embedded"],
                    "inline_images_in_markdown": True,
                    "input_s3_path": "input_s3_path",
                    "input_s3_region": "input_s3_region",
                    "input_url": "input_url",
                    "internal_is_screenshot_job": True,
                    "invalidate_cache": True,
                    "is_formatting_instruction": True,
                    "job_timeout_extra_time_per_page_in_seconds": 0,
                    "job_timeout_in_seconds": 0,
                    "keep_page_separator_when_merging_tables": True,
                    "languages": ["abq"],
                    "layout_aware": True,
                    "line_level_bounding_box": True,
                    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
                    "max_pages": 0,
                    "max_pages_enforced": 0,
                    "merge_tables_across_pages_in_markdown": True,
                    "model": "model",
                    "outlined_table_extraction": True,
                    "output_pdf_of_document": True,
                    "output_s3_path_prefix": "output_s3_path_prefix",
                    "output_s3_region": "output_s3_region",
                    "output_tables_as_html": True,
                    "page_error_tolerance": 0,
                    "page_footer_prefix": "page_footer_prefix",
                    "page_footer_suffix": "page_footer_suffix",
                    "page_header_prefix": "page_header_prefix",
                    "page_header_suffix": "page_header_suffix",
                    "page_prefix": "page_prefix",
                    "page_separator": "page_separator",
                    "page_suffix": "page_suffix",
                    "parse_mode": "parse_document_with_agent",
                    "parsing_instruction": "parsing_instruction",
                    "precise_bounding_box": True,
                    "premium_mode": True,
                    "presentation_out_of_bounds_content": True,
                    "presentation_skip_embedded_data": True,
                    "preserve_layout_alignment_across_pages": True,
                    "preserve_very_small_text": True,
                    "preset": "preset",
                    "priority": "critical",
                    "project_id": "project_id",
                    "remove_hidden_text": True,
                    "replace_failed_page_mode": "blank_page",
                    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
                    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
                    "save_images": True,
                    "skip_diagonal_text": True,
                    "specialized_chart_parsing_agentic": True,
                    "specialized_chart_parsing_efficient": True,
                    "specialized_chart_parsing_plus": True,
                    "specialized_image_parsing": True,
                    "spreadsheet_extract_sub_tables": True,
                    "spreadsheet_force_formula_computation": True,
                    "spreadsheet_include_hidden_sheets": True,
                    "strict_mode_buggy_font": True,
                    "strict_mode_image_extraction": True,
                    "strict_mode_image_ocr": True,
                    "strict_mode_reconstruction": True,
                    "structured_output": True,
                    "structured_output_json_schema": "structured_output_json_schema",
                    "structured_output_json_schema_name": "structured_output_json_schema_name",
                    "system_prompt": "system_prompt",
                    "system_prompt_append": "system_prompt_append",
                    "take_screenshot": True,
                    "target_pages": "target_pages",
                    "tier": "tier",
                    "use_vendor_multimodal_model": True,
                    "user_prompt": "user_prompt",
                    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
                    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
                    "version": "version",
                    "webhook_configurations": [
                        {
                            "webhook_events": ["parse.success", "parse.error"],
                            "webhook_headers": {"Authorization": "Bearer sk-..."},
                            "webhook_output_format": "json",
                            "webhook_signing_secret": "whsec_...",
                            "webhook_url": "https://example.com/webhooks/llamacloud",
                        }
                    ],
                    "webhook_url": "webhook_url",
                },
                managed_pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metadata_config={
                    "excluded_embed_metadata_keys": ["string"],
                    "excluded_llm_metadata_keys": ["string"],
                },
                pipeline_type="MANAGED",
                preset_retrieval_parameters={
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
                sparse_model_config={
                    "class_name": "class_name",
                    "model_type": "auto",
                },
                status="status",
                transform_config={
                    "chunk_overlap": 0,
                    "chunk_size": 1,
                    "mode": "auto",
                },
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.with_raw_response.create(
                name="x",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.with_streaming_response.create(
                name="x",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = response.parse()
                assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.retrieve(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="x",
            )

        assert_matches_type(PipelineRetrieveResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.retrieve(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="x",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                alpha=0,
                class_name="class_name",
                dense_similarity_cutoff=0,
                dense_similarity_top_k=1,
                enable_reranking=True,
                files_top_k=1,
                rerank_top_n=1,
                retrieval_mode="auto_routed",
                retrieve_image_nodes=True,
                retrieve_page_figure_nodes=True,
                retrieve_page_screenshot_nodes=True,
                search_filters={
                    "filters": [
                        {
                            "key": "key",
                            "value": 0,
                            "operator": "!=",
                        }
                    ],
                    "condition": "and",
                },
                search_filters_inference_schema={"foo": {"foo": "bar"}},
                sparse_similarity_top_k=1,
            )

        assert_matches_type(PipelineRetrieveResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.with_raw_response.retrieve(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="x",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineRetrieveResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.with_streaming_response.retrieve(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="x",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = response.parse()
                assert_matches_type(PipelineRetrieveResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.with_raw_response.retrieve(
                    pipeline_id="",
                    query="x",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.update(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.update(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_sink={
                    "component": {"foo": "bar"},
                    "name": "name",
                    "sink_type": "ASTRA_DB",
                },
                data_sink_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                embedding_config={
                    "component": {
                        "additional_kwargs": {"foo": "bar"},
                        "api_base": "api_base",
                        "api_key": "api_key",
                        "api_version": "api_version",
                        "azure_deployment": "azure_deployment",
                        "azure_endpoint": "azure_endpoint",
                        "class_name": "class_name",
                        "default_headers": {"foo": "string"},
                        "dimensions": 0,
                        "embed_batch_size": 1,
                        "max_retries": 0,
                        "model_name": "model_name",
                        "num_workers": 0,
                        "reuse_client": True,
                        "timeout": 0,
                    },
                    "type": "AZURE_EMBEDDING",
                },
                embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                llama_parse_parameters={
                    "adaptive_long_table": True,
                    "aggressive_table_extraction": True,
                    "annotate_links": True,
                    "auto_mode": True,
                    "auto_mode_configuration_json": "auto_mode_configuration_json",
                    "auto_mode_trigger_on_image_in_page": True,
                    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
                    "auto_mode_trigger_on_table_in_page": True,
                    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
                    "azure_openai_api_version": "azure_openai_api_version",
                    "azure_openai_deployment_name": "azure_openai_deployment_name",
                    "azure_openai_endpoint": "azure_openai_endpoint",
                    "azure_openai_key": "azure_openai_key",
                    "bbox_bottom": 0,
                    "bbox_left": 0,
                    "bbox_right": 0,
                    "bbox_top": 0,
                    "bounding_box": "bounding_box",
                    "compact_markdown_table": True,
                    "complemental_formatting_instruction": "complemental_formatting_instruction",
                    "content_guideline_instruction": "content_guideline_instruction",
                    "continuous_mode": True,
                    "disable_image_extraction": True,
                    "disable_ocr": True,
                    "disable_reconstruction": True,
                    "do_not_cache": True,
                    "do_not_unroll_columns": True,
                    "enable_cost_optimizer": True,
                    "extract_charts": True,
                    "extract_layout": True,
                    "extract_printed_page_number": True,
                    "fast_mode": True,
                    "formatting_instruction": "formatting_instruction",
                    "gpt4o_api_key": "gpt4o_api_key",
                    "gpt4o_mode": True,
                    "guess_xlsx_sheet_name": True,
                    "hide_footers": True,
                    "hide_headers": True,
                    "high_res_ocr": True,
                    "html_make_all_elements_visible": True,
                    "html_remove_fixed_elements": True,
                    "html_remove_navigation_elements": True,
                    "http_proxy": "http_proxy",
                    "ignore_document_elements_for_layout_detection": True,
                    "images_to_save": ["embedded"],
                    "inline_images_in_markdown": True,
                    "input_s3_path": "input_s3_path",
                    "input_s3_region": "input_s3_region",
                    "input_url": "input_url",
                    "internal_is_screenshot_job": True,
                    "invalidate_cache": True,
                    "is_formatting_instruction": True,
                    "job_timeout_extra_time_per_page_in_seconds": 0,
                    "job_timeout_in_seconds": 0,
                    "keep_page_separator_when_merging_tables": True,
                    "languages": ["abq"],
                    "layout_aware": True,
                    "line_level_bounding_box": True,
                    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
                    "max_pages": 0,
                    "max_pages_enforced": 0,
                    "merge_tables_across_pages_in_markdown": True,
                    "model": "model",
                    "outlined_table_extraction": True,
                    "output_pdf_of_document": True,
                    "output_s3_path_prefix": "output_s3_path_prefix",
                    "output_s3_region": "output_s3_region",
                    "output_tables_as_html": True,
                    "page_error_tolerance": 0,
                    "page_footer_prefix": "page_footer_prefix",
                    "page_footer_suffix": "page_footer_suffix",
                    "page_header_prefix": "page_header_prefix",
                    "page_header_suffix": "page_header_suffix",
                    "page_prefix": "page_prefix",
                    "page_separator": "page_separator",
                    "page_suffix": "page_suffix",
                    "parse_mode": "parse_document_with_agent",
                    "parsing_instruction": "parsing_instruction",
                    "precise_bounding_box": True,
                    "premium_mode": True,
                    "presentation_out_of_bounds_content": True,
                    "presentation_skip_embedded_data": True,
                    "preserve_layout_alignment_across_pages": True,
                    "preserve_very_small_text": True,
                    "preset": "preset",
                    "priority": "critical",
                    "project_id": "project_id",
                    "remove_hidden_text": True,
                    "replace_failed_page_mode": "blank_page",
                    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
                    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
                    "save_images": True,
                    "skip_diagonal_text": True,
                    "specialized_chart_parsing_agentic": True,
                    "specialized_chart_parsing_efficient": True,
                    "specialized_chart_parsing_plus": True,
                    "specialized_image_parsing": True,
                    "spreadsheet_extract_sub_tables": True,
                    "spreadsheet_force_formula_computation": True,
                    "spreadsheet_include_hidden_sheets": True,
                    "strict_mode_buggy_font": True,
                    "strict_mode_image_extraction": True,
                    "strict_mode_image_ocr": True,
                    "strict_mode_reconstruction": True,
                    "structured_output": True,
                    "structured_output_json_schema": "structured_output_json_schema",
                    "structured_output_json_schema_name": "structured_output_json_schema_name",
                    "system_prompt": "system_prompt",
                    "system_prompt_append": "system_prompt_append",
                    "take_screenshot": True,
                    "target_pages": "target_pages",
                    "tier": "tier",
                    "use_vendor_multimodal_model": True,
                    "user_prompt": "user_prompt",
                    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
                    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
                    "version": "version",
                    "webhook_configurations": [
                        {
                            "webhook_events": ["parse.success", "parse.error"],
                            "webhook_headers": {"Authorization": "Bearer sk-..."},
                            "webhook_output_format": "json",
                            "webhook_signing_secret": "whsec_...",
                            "webhook_url": "https://example.com/webhooks/llamacloud",
                        }
                    ],
                    "webhook_url": "webhook_url",
                },
                managed_pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metadata_config={
                    "excluded_embed_metadata_keys": ["string"],
                    "excluded_llm_metadata_keys": ["string"],
                },
                name="name",
                preset_retrieval_parameters={
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
                sparse_model_config={
                    "class_name": "class_name",
                    "model_type": "auto",
                },
                status="status",
                transform_config={
                    "chunk_overlap": 0,
                    "chunk_size": 1,
                    "mode": "auto",
                },
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.with_raw_response.update(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.with_streaming_response.update(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = response.parse()
                assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.with_raw_response.update(
                    pipeline_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.list()

        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.list(
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_name="pipeline_name",
                pipeline_type="MANAGED",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_name="project_name",
            )

        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = response.parse()
                assert_matches_type(PipelineListResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.with_streaming_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = response.parse()
                assert pipeline is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.with_raw_response.delete(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.with_streaming_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = response.parse()
                assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.with_raw_response.get(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.get_status(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ManagedIngestionStatusResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.get_status(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                full_details=True,
            )

        assert_matches_type(ManagedIngestionStatusResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.with_raw_response.get_status(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(ManagedIngestionStatusResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.with_streaming_response.get_status(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = response.parse()
                assert_matches_type(ManagedIngestionStatusResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                client.pipelines.with_raw_response.get_status(
                    pipeline_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.upsert(
                name="x",
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upsert_with_all_params(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = client.pipelines.upsert(
                name="x",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_sink={
                    "component": {"foo": "bar"},
                    "name": "name",
                    "sink_type": "ASTRA_DB",
                },
                data_sink_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                embedding_config={
                    "component": {
                        "additional_kwargs": {"foo": "bar"},
                        "api_base": "api_base",
                        "api_key": "api_key",
                        "api_version": "api_version",
                        "azure_deployment": "azure_deployment",
                        "azure_endpoint": "azure_endpoint",
                        "class_name": "class_name",
                        "default_headers": {"foo": "string"},
                        "dimensions": 0,
                        "embed_batch_size": 1,
                        "max_retries": 0,
                        "model_name": "model_name",
                        "num_workers": 0,
                        "reuse_client": True,
                        "timeout": 0,
                    },
                    "type": "AZURE_EMBEDDING",
                },
                embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                llama_parse_parameters={
                    "adaptive_long_table": True,
                    "aggressive_table_extraction": True,
                    "annotate_links": True,
                    "auto_mode": True,
                    "auto_mode_configuration_json": "auto_mode_configuration_json",
                    "auto_mode_trigger_on_image_in_page": True,
                    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
                    "auto_mode_trigger_on_table_in_page": True,
                    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
                    "azure_openai_api_version": "azure_openai_api_version",
                    "azure_openai_deployment_name": "azure_openai_deployment_name",
                    "azure_openai_endpoint": "azure_openai_endpoint",
                    "azure_openai_key": "azure_openai_key",
                    "bbox_bottom": 0,
                    "bbox_left": 0,
                    "bbox_right": 0,
                    "bbox_top": 0,
                    "bounding_box": "bounding_box",
                    "compact_markdown_table": True,
                    "complemental_formatting_instruction": "complemental_formatting_instruction",
                    "content_guideline_instruction": "content_guideline_instruction",
                    "continuous_mode": True,
                    "disable_image_extraction": True,
                    "disable_ocr": True,
                    "disable_reconstruction": True,
                    "do_not_cache": True,
                    "do_not_unroll_columns": True,
                    "enable_cost_optimizer": True,
                    "extract_charts": True,
                    "extract_layout": True,
                    "extract_printed_page_number": True,
                    "fast_mode": True,
                    "formatting_instruction": "formatting_instruction",
                    "gpt4o_api_key": "gpt4o_api_key",
                    "gpt4o_mode": True,
                    "guess_xlsx_sheet_name": True,
                    "hide_footers": True,
                    "hide_headers": True,
                    "high_res_ocr": True,
                    "html_make_all_elements_visible": True,
                    "html_remove_fixed_elements": True,
                    "html_remove_navigation_elements": True,
                    "http_proxy": "http_proxy",
                    "ignore_document_elements_for_layout_detection": True,
                    "images_to_save": ["embedded"],
                    "inline_images_in_markdown": True,
                    "input_s3_path": "input_s3_path",
                    "input_s3_region": "input_s3_region",
                    "input_url": "input_url",
                    "internal_is_screenshot_job": True,
                    "invalidate_cache": True,
                    "is_formatting_instruction": True,
                    "job_timeout_extra_time_per_page_in_seconds": 0,
                    "job_timeout_in_seconds": 0,
                    "keep_page_separator_when_merging_tables": True,
                    "languages": ["abq"],
                    "layout_aware": True,
                    "line_level_bounding_box": True,
                    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
                    "max_pages": 0,
                    "max_pages_enforced": 0,
                    "merge_tables_across_pages_in_markdown": True,
                    "model": "model",
                    "outlined_table_extraction": True,
                    "output_pdf_of_document": True,
                    "output_s3_path_prefix": "output_s3_path_prefix",
                    "output_s3_region": "output_s3_region",
                    "output_tables_as_html": True,
                    "page_error_tolerance": 0,
                    "page_footer_prefix": "page_footer_prefix",
                    "page_footer_suffix": "page_footer_suffix",
                    "page_header_prefix": "page_header_prefix",
                    "page_header_suffix": "page_header_suffix",
                    "page_prefix": "page_prefix",
                    "page_separator": "page_separator",
                    "page_suffix": "page_suffix",
                    "parse_mode": "parse_document_with_agent",
                    "parsing_instruction": "parsing_instruction",
                    "precise_bounding_box": True,
                    "premium_mode": True,
                    "presentation_out_of_bounds_content": True,
                    "presentation_skip_embedded_data": True,
                    "preserve_layout_alignment_across_pages": True,
                    "preserve_very_small_text": True,
                    "preset": "preset",
                    "priority": "critical",
                    "project_id": "project_id",
                    "remove_hidden_text": True,
                    "replace_failed_page_mode": "blank_page",
                    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
                    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
                    "save_images": True,
                    "skip_diagonal_text": True,
                    "specialized_chart_parsing_agentic": True,
                    "specialized_chart_parsing_efficient": True,
                    "specialized_chart_parsing_plus": True,
                    "specialized_image_parsing": True,
                    "spreadsheet_extract_sub_tables": True,
                    "spreadsheet_force_formula_computation": True,
                    "spreadsheet_include_hidden_sheets": True,
                    "strict_mode_buggy_font": True,
                    "strict_mode_image_extraction": True,
                    "strict_mode_image_ocr": True,
                    "strict_mode_reconstruction": True,
                    "structured_output": True,
                    "structured_output_json_schema": "structured_output_json_schema",
                    "structured_output_json_schema_name": "structured_output_json_schema_name",
                    "system_prompt": "system_prompt",
                    "system_prompt_append": "system_prompt_append",
                    "take_screenshot": True,
                    "target_pages": "target_pages",
                    "tier": "tier",
                    "use_vendor_multimodal_model": True,
                    "user_prompt": "user_prompt",
                    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
                    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
                    "version": "version",
                    "webhook_configurations": [
                        {
                            "webhook_events": ["parse.success", "parse.error"],
                            "webhook_headers": {"Authorization": "Bearer sk-..."},
                            "webhook_output_format": "json",
                            "webhook_signing_secret": "whsec_...",
                            "webhook_url": "https://example.com/webhooks/llamacloud",
                        }
                    ],
                    "webhook_url": "webhook_url",
                },
                managed_pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metadata_config={
                    "excluded_embed_metadata_keys": ["string"],
                    "excluded_llm_metadata_keys": ["string"],
                },
                pipeline_type="MANAGED",
                preset_retrieval_parameters={
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
                sparse_model_config={
                    "class_name": "class_name",
                    "model_type": "auto",
                },
                status="status",
                transform_config={
                    "chunk_overlap": 0,
                    "chunk_size": 1,
                    "mode": "auto",
                },
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = client.pipelines.with_raw_response.upsert(
                name="x",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: LlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with client.pipelines.with_streaming_response.upsert(
                name="x",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = response.parse()
                assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPipelines:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.create(
                name="x",
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.create(
                name="x",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_sink={
                    "component": {"foo": "bar"},
                    "name": "name",
                    "sink_type": "ASTRA_DB",
                },
                data_sink_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                embedding_config={
                    "component": {
                        "additional_kwargs": {"foo": "bar"},
                        "api_base": "api_base",
                        "api_key": "api_key",
                        "api_version": "api_version",
                        "azure_deployment": "azure_deployment",
                        "azure_endpoint": "azure_endpoint",
                        "class_name": "class_name",
                        "default_headers": {"foo": "string"},
                        "dimensions": 0,
                        "embed_batch_size": 1,
                        "max_retries": 0,
                        "model_name": "model_name",
                        "num_workers": 0,
                        "reuse_client": True,
                        "timeout": 0,
                    },
                    "type": "AZURE_EMBEDDING",
                },
                embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                llama_parse_parameters={
                    "adaptive_long_table": True,
                    "aggressive_table_extraction": True,
                    "annotate_links": True,
                    "auto_mode": True,
                    "auto_mode_configuration_json": "auto_mode_configuration_json",
                    "auto_mode_trigger_on_image_in_page": True,
                    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
                    "auto_mode_trigger_on_table_in_page": True,
                    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
                    "azure_openai_api_version": "azure_openai_api_version",
                    "azure_openai_deployment_name": "azure_openai_deployment_name",
                    "azure_openai_endpoint": "azure_openai_endpoint",
                    "azure_openai_key": "azure_openai_key",
                    "bbox_bottom": 0,
                    "bbox_left": 0,
                    "bbox_right": 0,
                    "bbox_top": 0,
                    "bounding_box": "bounding_box",
                    "compact_markdown_table": True,
                    "complemental_formatting_instruction": "complemental_formatting_instruction",
                    "content_guideline_instruction": "content_guideline_instruction",
                    "continuous_mode": True,
                    "disable_image_extraction": True,
                    "disable_ocr": True,
                    "disable_reconstruction": True,
                    "do_not_cache": True,
                    "do_not_unroll_columns": True,
                    "enable_cost_optimizer": True,
                    "extract_charts": True,
                    "extract_layout": True,
                    "extract_printed_page_number": True,
                    "fast_mode": True,
                    "formatting_instruction": "formatting_instruction",
                    "gpt4o_api_key": "gpt4o_api_key",
                    "gpt4o_mode": True,
                    "guess_xlsx_sheet_name": True,
                    "hide_footers": True,
                    "hide_headers": True,
                    "high_res_ocr": True,
                    "html_make_all_elements_visible": True,
                    "html_remove_fixed_elements": True,
                    "html_remove_navigation_elements": True,
                    "http_proxy": "http_proxy",
                    "ignore_document_elements_for_layout_detection": True,
                    "images_to_save": ["embedded"],
                    "inline_images_in_markdown": True,
                    "input_s3_path": "input_s3_path",
                    "input_s3_region": "input_s3_region",
                    "input_url": "input_url",
                    "internal_is_screenshot_job": True,
                    "invalidate_cache": True,
                    "is_formatting_instruction": True,
                    "job_timeout_extra_time_per_page_in_seconds": 0,
                    "job_timeout_in_seconds": 0,
                    "keep_page_separator_when_merging_tables": True,
                    "languages": ["abq"],
                    "layout_aware": True,
                    "line_level_bounding_box": True,
                    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
                    "max_pages": 0,
                    "max_pages_enforced": 0,
                    "merge_tables_across_pages_in_markdown": True,
                    "model": "model",
                    "outlined_table_extraction": True,
                    "output_pdf_of_document": True,
                    "output_s3_path_prefix": "output_s3_path_prefix",
                    "output_s3_region": "output_s3_region",
                    "output_tables_as_html": True,
                    "page_error_tolerance": 0,
                    "page_footer_prefix": "page_footer_prefix",
                    "page_footer_suffix": "page_footer_suffix",
                    "page_header_prefix": "page_header_prefix",
                    "page_header_suffix": "page_header_suffix",
                    "page_prefix": "page_prefix",
                    "page_separator": "page_separator",
                    "page_suffix": "page_suffix",
                    "parse_mode": "parse_document_with_agent",
                    "parsing_instruction": "parsing_instruction",
                    "precise_bounding_box": True,
                    "premium_mode": True,
                    "presentation_out_of_bounds_content": True,
                    "presentation_skip_embedded_data": True,
                    "preserve_layout_alignment_across_pages": True,
                    "preserve_very_small_text": True,
                    "preset": "preset",
                    "priority": "critical",
                    "project_id": "project_id",
                    "remove_hidden_text": True,
                    "replace_failed_page_mode": "blank_page",
                    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
                    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
                    "save_images": True,
                    "skip_diagonal_text": True,
                    "specialized_chart_parsing_agentic": True,
                    "specialized_chart_parsing_efficient": True,
                    "specialized_chart_parsing_plus": True,
                    "specialized_image_parsing": True,
                    "spreadsheet_extract_sub_tables": True,
                    "spreadsheet_force_formula_computation": True,
                    "spreadsheet_include_hidden_sheets": True,
                    "strict_mode_buggy_font": True,
                    "strict_mode_image_extraction": True,
                    "strict_mode_image_ocr": True,
                    "strict_mode_reconstruction": True,
                    "structured_output": True,
                    "structured_output_json_schema": "structured_output_json_schema",
                    "structured_output_json_schema_name": "structured_output_json_schema_name",
                    "system_prompt": "system_prompt",
                    "system_prompt_append": "system_prompt_append",
                    "take_screenshot": True,
                    "target_pages": "target_pages",
                    "tier": "tier",
                    "use_vendor_multimodal_model": True,
                    "user_prompt": "user_prompt",
                    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
                    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
                    "version": "version",
                    "webhook_configurations": [
                        {
                            "webhook_events": ["parse.success", "parse.error"],
                            "webhook_headers": {"Authorization": "Bearer sk-..."},
                            "webhook_output_format": "json",
                            "webhook_signing_secret": "whsec_...",
                            "webhook_url": "https://example.com/webhooks/llamacloud",
                        }
                    ],
                    "webhook_url": "webhook_url",
                },
                managed_pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metadata_config={
                    "excluded_embed_metadata_keys": ["string"],
                    "excluded_llm_metadata_keys": ["string"],
                },
                pipeline_type="MANAGED",
                preset_retrieval_parameters={
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
                sparse_model_config={
                    "class_name": "class_name",
                    "model_type": "auto",
                },
                status="status",
                transform_config={
                    "chunk_overlap": 0,
                    "chunk_size": 1,
                    "mode": "auto",
                },
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.with_raw_response.create(
                name="x",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.with_streaming_response.create(
                name="x",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = await response.parse()
                assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.retrieve(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="x",
            )

        assert_matches_type(PipelineRetrieveResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.retrieve(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="x",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                alpha=0,
                class_name="class_name",
                dense_similarity_cutoff=0,
                dense_similarity_top_k=1,
                enable_reranking=True,
                files_top_k=1,
                rerank_top_n=1,
                retrieval_mode="auto_routed",
                retrieve_image_nodes=True,
                retrieve_page_figure_nodes=True,
                retrieve_page_screenshot_nodes=True,
                search_filters={
                    "filters": [
                        {
                            "key": "key",
                            "value": 0,
                            "operator": "!=",
                        }
                    ],
                    "condition": "and",
                },
                search_filters_inference_schema={"foo": {"foo": "bar"}},
                sparse_similarity_top_k=1,
            )

        assert_matches_type(PipelineRetrieveResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.with_raw_response.retrieve(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="x",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineRetrieveResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.with_streaming_response.retrieve(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                query="x",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = await response.parse()
                assert_matches_type(PipelineRetrieveResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.with_raw_response.retrieve(
                    pipeline_id="",
                    query="x",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.update(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.update(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_sink={
                    "component": {"foo": "bar"},
                    "name": "name",
                    "sink_type": "ASTRA_DB",
                },
                data_sink_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                embedding_config={
                    "component": {
                        "additional_kwargs": {"foo": "bar"},
                        "api_base": "api_base",
                        "api_key": "api_key",
                        "api_version": "api_version",
                        "azure_deployment": "azure_deployment",
                        "azure_endpoint": "azure_endpoint",
                        "class_name": "class_name",
                        "default_headers": {"foo": "string"},
                        "dimensions": 0,
                        "embed_batch_size": 1,
                        "max_retries": 0,
                        "model_name": "model_name",
                        "num_workers": 0,
                        "reuse_client": True,
                        "timeout": 0,
                    },
                    "type": "AZURE_EMBEDDING",
                },
                embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                llama_parse_parameters={
                    "adaptive_long_table": True,
                    "aggressive_table_extraction": True,
                    "annotate_links": True,
                    "auto_mode": True,
                    "auto_mode_configuration_json": "auto_mode_configuration_json",
                    "auto_mode_trigger_on_image_in_page": True,
                    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
                    "auto_mode_trigger_on_table_in_page": True,
                    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
                    "azure_openai_api_version": "azure_openai_api_version",
                    "azure_openai_deployment_name": "azure_openai_deployment_name",
                    "azure_openai_endpoint": "azure_openai_endpoint",
                    "azure_openai_key": "azure_openai_key",
                    "bbox_bottom": 0,
                    "bbox_left": 0,
                    "bbox_right": 0,
                    "bbox_top": 0,
                    "bounding_box": "bounding_box",
                    "compact_markdown_table": True,
                    "complemental_formatting_instruction": "complemental_formatting_instruction",
                    "content_guideline_instruction": "content_guideline_instruction",
                    "continuous_mode": True,
                    "disable_image_extraction": True,
                    "disable_ocr": True,
                    "disable_reconstruction": True,
                    "do_not_cache": True,
                    "do_not_unroll_columns": True,
                    "enable_cost_optimizer": True,
                    "extract_charts": True,
                    "extract_layout": True,
                    "extract_printed_page_number": True,
                    "fast_mode": True,
                    "formatting_instruction": "formatting_instruction",
                    "gpt4o_api_key": "gpt4o_api_key",
                    "gpt4o_mode": True,
                    "guess_xlsx_sheet_name": True,
                    "hide_footers": True,
                    "hide_headers": True,
                    "high_res_ocr": True,
                    "html_make_all_elements_visible": True,
                    "html_remove_fixed_elements": True,
                    "html_remove_navigation_elements": True,
                    "http_proxy": "http_proxy",
                    "ignore_document_elements_for_layout_detection": True,
                    "images_to_save": ["embedded"],
                    "inline_images_in_markdown": True,
                    "input_s3_path": "input_s3_path",
                    "input_s3_region": "input_s3_region",
                    "input_url": "input_url",
                    "internal_is_screenshot_job": True,
                    "invalidate_cache": True,
                    "is_formatting_instruction": True,
                    "job_timeout_extra_time_per_page_in_seconds": 0,
                    "job_timeout_in_seconds": 0,
                    "keep_page_separator_when_merging_tables": True,
                    "languages": ["abq"],
                    "layout_aware": True,
                    "line_level_bounding_box": True,
                    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
                    "max_pages": 0,
                    "max_pages_enforced": 0,
                    "merge_tables_across_pages_in_markdown": True,
                    "model": "model",
                    "outlined_table_extraction": True,
                    "output_pdf_of_document": True,
                    "output_s3_path_prefix": "output_s3_path_prefix",
                    "output_s3_region": "output_s3_region",
                    "output_tables_as_html": True,
                    "page_error_tolerance": 0,
                    "page_footer_prefix": "page_footer_prefix",
                    "page_footer_suffix": "page_footer_suffix",
                    "page_header_prefix": "page_header_prefix",
                    "page_header_suffix": "page_header_suffix",
                    "page_prefix": "page_prefix",
                    "page_separator": "page_separator",
                    "page_suffix": "page_suffix",
                    "parse_mode": "parse_document_with_agent",
                    "parsing_instruction": "parsing_instruction",
                    "precise_bounding_box": True,
                    "premium_mode": True,
                    "presentation_out_of_bounds_content": True,
                    "presentation_skip_embedded_data": True,
                    "preserve_layout_alignment_across_pages": True,
                    "preserve_very_small_text": True,
                    "preset": "preset",
                    "priority": "critical",
                    "project_id": "project_id",
                    "remove_hidden_text": True,
                    "replace_failed_page_mode": "blank_page",
                    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
                    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
                    "save_images": True,
                    "skip_diagonal_text": True,
                    "specialized_chart_parsing_agentic": True,
                    "specialized_chart_parsing_efficient": True,
                    "specialized_chart_parsing_plus": True,
                    "specialized_image_parsing": True,
                    "spreadsheet_extract_sub_tables": True,
                    "spreadsheet_force_formula_computation": True,
                    "spreadsheet_include_hidden_sheets": True,
                    "strict_mode_buggy_font": True,
                    "strict_mode_image_extraction": True,
                    "strict_mode_image_ocr": True,
                    "strict_mode_reconstruction": True,
                    "structured_output": True,
                    "structured_output_json_schema": "structured_output_json_schema",
                    "structured_output_json_schema_name": "structured_output_json_schema_name",
                    "system_prompt": "system_prompt",
                    "system_prompt_append": "system_prompt_append",
                    "take_screenshot": True,
                    "target_pages": "target_pages",
                    "tier": "tier",
                    "use_vendor_multimodal_model": True,
                    "user_prompt": "user_prompt",
                    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
                    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
                    "version": "version",
                    "webhook_configurations": [
                        {
                            "webhook_events": ["parse.success", "parse.error"],
                            "webhook_headers": {"Authorization": "Bearer sk-..."},
                            "webhook_output_format": "json",
                            "webhook_signing_secret": "whsec_...",
                            "webhook_url": "https://example.com/webhooks/llamacloud",
                        }
                    ],
                    "webhook_url": "webhook_url",
                },
                managed_pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metadata_config={
                    "excluded_embed_metadata_keys": ["string"],
                    "excluded_llm_metadata_keys": ["string"],
                },
                name="name",
                preset_retrieval_parameters={
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
                sparse_model_config={
                    "class_name": "class_name",
                    "model_type": "auto",
                },
                status="status",
                transform_config={
                    "chunk_overlap": 0,
                    "chunk_size": 1,
                    "mode": "auto",
                },
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.with_raw_response.update(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.with_streaming_response.update(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = await response.parse()
                assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.with_raw_response.update(
                    pipeline_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.list()

        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.list(
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                pipeline_name="pipeline_name",
                pipeline_type="MANAGED",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_name="project_name",
            )

        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(PipelineListResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.with_streaming_response.list() as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = await response.parse()
                assert_matches_type(PipelineListResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.with_raw_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert pipeline is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.with_streaming_response.delete(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = await response.parse()
                assert pipeline is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.with_raw_response.delete(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.with_raw_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.with_streaming_response.get(
                "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = await response.parse()
                assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.with_raw_response.get(
                    "",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.get_status(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert_matches_type(ManagedIngestionStatusResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.get_status(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                full_details=True,
            )

        assert_matches_type(ManagedIngestionStatusResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.with_raw_response.get_status(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(ManagedIngestionStatusResponse, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.with_streaming_response.get_status(
                pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = await response.parse()
                assert_matches_type(ManagedIngestionStatusResponse, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            with pytest.raises(ValueError, match=r"Expected a non-empty value for `pipeline_id` but received ''"):
                await async_client.pipelines.with_raw_response.get_status(
                    pipeline_id="",
                )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.upsert(
                name="x",
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upsert_with_all_params(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            pipeline = await async_client.pipelines.upsert(
                name="x",
                organization_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                project_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                data_sink={
                    "component": {"foo": "bar"},
                    "name": "name",
                    "sink_type": "ASTRA_DB",
                },
                data_sink_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                embedding_config={
                    "component": {
                        "additional_kwargs": {"foo": "bar"},
                        "api_base": "api_base",
                        "api_key": "api_key",
                        "api_version": "api_version",
                        "azure_deployment": "azure_deployment",
                        "azure_endpoint": "azure_endpoint",
                        "class_name": "class_name",
                        "default_headers": {"foo": "string"},
                        "dimensions": 0,
                        "embed_batch_size": 1,
                        "max_retries": 0,
                        "model_name": "model_name",
                        "num_workers": 0,
                        "reuse_client": True,
                        "timeout": 0,
                    },
                    "type": "AZURE_EMBEDDING",
                },
                embedding_model_config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                llama_parse_parameters={
                    "adaptive_long_table": True,
                    "aggressive_table_extraction": True,
                    "annotate_links": True,
                    "auto_mode": True,
                    "auto_mode_configuration_json": "auto_mode_configuration_json",
                    "auto_mode_trigger_on_image_in_page": True,
                    "auto_mode_trigger_on_regexp_in_page": "auto_mode_trigger_on_regexp_in_page",
                    "auto_mode_trigger_on_table_in_page": True,
                    "auto_mode_trigger_on_text_in_page": "auto_mode_trigger_on_text_in_page",
                    "azure_openai_api_version": "azure_openai_api_version",
                    "azure_openai_deployment_name": "azure_openai_deployment_name",
                    "azure_openai_endpoint": "azure_openai_endpoint",
                    "azure_openai_key": "azure_openai_key",
                    "bbox_bottom": 0,
                    "bbox_left": 0,
                    "bbox_right": 0,
                    "bbox_top": 0,
                    "bounding_box": "bounding_box",
                    "compact_markdown_table": True,
                    "complemental_formatting_instruction": "complemental_formatting_instruction",
                    "content_guideline_instruction": "content_guideline_instruction",
                    "continuous_mode": True,
                    "disable_image_extraction": True,
                    "disable_ocr": True,
                    "disable_reconstruction": True,
                    "do_not_cache": True,
                    "do_not_unroll_columns": True,
                    "enable_cost_optimizer": True,
                    "extract_charts": True,
                    "extract_layout": True,
                    "extract_printed_page_number": True,
                    "fast_mode": True,
                    "formatting_instruction": "formatting_instruction",
                    "gpt4o_api_key": "gpt4o_api_key",
                    "gpt4o_mode": True,
                    "guess_xlsx_sheet_name": True,
                    "hide_footers": True,
                    "hide_headers": True,
                    "high_res_ocr": True,
                    "html_make_all_elements_visible": True,
                    "html_remove_fixed_elements": True,
                    "html_remove_navigation_elements": True,
                    "http_proxy": "http_proxy",
                    "ignore_document_elements_for_layout_detection": True,
                    "images_to_save": ["embedded"],
                    "inline_images_in_markdown": True,
                    "input_s3_path": "input_s3_path",
                    "input_s3_region": "input_s3_region",
                    "input_url": "input_url",
                    "internal_is_screenshot_job": True,
                    "invalidate_cache": True,
                    "is_formatting_instruction": True,
                    "job_timeout_extra_time_per_page_in_seconds": 0,
                    "job_timeout_in_seconds": 0,
                    "keep_page_separator_when_merging_tables": True,
                    "languages": ["abq"],
                    "layout_aware": True,
                    "line_level_bounding_box": True,
                    "markdown_table_multiline_header_separator": "markdown_table_multiline_header_separator",
                    "max_pages": 0,
                    "max_pages_enforced": 0,
                    "merge_tables_across_pages_in_markdown": True,
                    "model": "model",
                    "outlined_table_extraction": True,
                    "output_pdf_of_document": True,
                    "output_s3_path_prefix": "output_s3_path_prefix",
                    "output_s3_region": "output_s3_region",
                    "output_tables_as_html": True,
                    "page_error_tolerance": 0,
                    "page_footer_prefix": "page_footer_prefix",
                    "page_footer_suffix": "page_footer_suffix",
                    "page_header_prefix": "page_header_prefix",
                    "page_header_suffix": "page_header_suffix",
                    "page_prefix": "page_prefix",
                    "page_separator": "page_separator",
                    "page_suffix": "page_suffix",
                    "parse_mode": "parse_document_with_agent",
                    "parsing_instruction": "parsing_instruction",
                    "precise_bounding_box": True,
                    "premium_mode": True,
                    "presentation_out_of_bounds_content": True,
                    "presentation_skip_embedded_data": True,
                    "preserve_layout_alignment_across_pages": True,
                    "preserve_very_small_text": True,
                    "preset": "preset",
                    "priority": "critical",
                    "project_id": "project_id",
                    "remove_hidden_text": True,
                    "replace_failed_page_mode": "blank_page",
                    "replace_failed_page_with_error_message_prefix": "replace_failed_page_with_error_message_prefix",
                    "replace_failed_page_with_error_message_suffix": "replace_failed_page_with_error_message_suffix",
                    "save_images": True,
                    "skip_diagonal_text": True,
                    "specialized_chart_parsing_agentic": True,
                    "specialized_chart_parsing_efficient": True,
                    "specialized_chart_parsing_plus": True,
                    "specialized_image_parsing": True,
                    "spreadsheet_extract_sub_tables": True,
                    "spreadsheet_force_formula_computation": True,
                    "spreadsheet_include_hidden_sheets": True,
                    "strict_mode_buggy_font": True,
                    "strict_mode_image_extraction": True,
                    "strict_mode_image_ocr": True,
                    "strict_mode_reconstruction": True,
                    "structured_output": True,
                    "structured_output_json_schema": "structured_output_json_schema",
                    "structured_output_json_schema_name": "structured_output_json_schema_name",
                    "system_prompt": "system_prompt",
                    "system_prompt_append": "system_prompt_append",
                    "take_screenshot": True,
                    "target_pages": "target_pages",
                    "tier": "tier",
                    "use_vendor_multimodal_model": True,
                    "user_prompt": "user_prompt",
                    "vendor_multimodal_api_key": "vendor_multimodal_api_key",
                    "vendor_multimodal_model_name": "vendor_multimodal_model_name",
                    "version": "version",
                    "webhook_configurations": [
                        {
                            "webhook_events": ["parse.success", "parse.error"],
                            "webhook_headers": {"Authorization": "Bearer sk-..."},
                            "webhook_output_format": "json",
                            "webhook_signing_secret": "whsec_...",
                            "webhook_url": "https://example.com/webhooks/llamacloud",
                        }
                    ],
                    "webhook_url": "webhook_url",
                },
                managed_pipeline_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                metadata_config={
                    "excluded_embed_metadata_keys": ["string"],
                    "excluded_llm_metadata_keys": ["string"],
                },
                pipeline_type="MANAGED",
                preset_retrieval_parameters={
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
                sparse_model_config={
                    "class_name": "class_name",
                    "model_type": "auto",
                },
                status="status",
                transform_config={
                    "chunk_overlap": 0,
                    "chunk_size": 1,
                    "mode": "auto",
                },
            )

        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            response = await async_client.pipelines.with_raw_response.upsert(
                name="x",
            )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pipeline = await response.parse()
        assert_matches_type(Pipeline, pipeline, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncLlamaCloud) -> None:
        with pytest.warns(DeprecationWarning):
            async with async_client.pipelines.with_streaming_response.upsert(
                name="x",
            ) as response:
                assert not response.is_closed
                assert response.http_request.headers.get("X-Stainless-Lang") == "python"

                pipeline = await response.parse()
                assert_matches_type(Pipeline, pipeline, path=["response"])

        assert cast(Any, response.is_closed) is True
