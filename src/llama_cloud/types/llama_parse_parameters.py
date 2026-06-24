# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .parsing_mode import ParsingMode
from .fail_page_mode import FailPageMode
from .parsing_languages import ParsingLanguages

__all__ = ["LlamaParseParameters", "WebhookConfiguration"]


class WebhookConfiguration(BaseModel):
    """Configuration for a single outbound webhook endpoint."""

    webhook_events: Optional[
        List[
            Literal[
                "classify.cancelled",
                "classify.error",
                "classify.partial_success",
                "classify.pending",
                "classify.running",
                "classify.success",
                "extract.cancelled",
                "extract.error",
                "extract.partial_success",
                "extract.pending",
                "extract.success",
                "parse.cancelled",
                "parse.error",
                "parse.partial_success",
                "parse.pending",
                "parse.running",
                "parse.success",
                "sheets.cancelled",
                "sheets.error",
                "sheets.partial_success",
                "sheets.pending",
                "sheets.success",
                "split.cancelled",
                "split.error",
                "split.pending",
                "split.processing",
                "split.success",
                "unmapped_event",
            ]
        ]
    ] = None
    """Events to subscribe to (e.g.

    'parse.success', 'extract.error'). If null, all events are delivered.
    """

    webhook_headers: Optional[Dict[str, str]] = None
    """Custom HTTP headers sent with each webhook request (e.g. auth tokens)"""

    webhook_output_format: Optional[str] = None
    """Response format sent to the webhook: 'string' (default) or 'json'"""

    webhook_url: Optional[str] = None
    """URL to receive webhook POST notifications"""


class LlamaParseParameters(BaseModel):
    adaptive_long_table: Optional[bool] = None

    aggressive_table_extraction: Optional[bool] = None

    annotate_links: Optional[bool] = None

    auto_mode: Optional[bool] = None

    auto_mode_configuration_json: Optional[str] = None

    auto_mode_trigger_on_image_in_page: Optional[bool] = None

    auto_mode_trigger_on_regexp_in_page: Optional[str] = None

    auto_mode_trigger_on_table_in_page: Optional[bool] = None

    auto_mode_trigger_on_text_in_page: Optional[str] = None

    azure_openai_api_version: Optional[str] = None

    azure_openai_deployment_name: Optional[str] = None

    azure_openai_endpoint: Optional[str] = None

    azure_openai_key: Optional[str] = None

    bbox_bottom: Optional[float] = None

    bbox_left: Optional[float] = None

    bbox_right: Optional[float] = None

    bbox_top: Optional[float] = None

    bounding_box: Optional[str] = None

    compact_markdown_table: Optional[bool] = None

    complemental_formatting_instruction: Optional[str] = None

    content_guideline_instruction: Optional[str] = None

    continuous_mode: Optional[bool] = None

    disable_image_extraction: Optional[bool] = None

    disable_ocr: Optional[bool] = None

    disable_reconstruction: Optional[bool] = None

    do_not_cache: Optional[bool] = None

    do_not_unroll_columns: Optional[bool] = None

    enable_cost_optimizer: Optional[bool] = None

    extract_charts: Optional[bool] = None

    extract_layout: Optional[bool] = None

    extract_printed_page_number: Optional[bool] = None

    fast_mode: Optional[bool] = None

    formatting_instruction: Optional[str] = None

    gpt4o_api_key: Optional[str] = None

    gpt4o_mode: Optional[bool] = None

    guess_xlsx_sheet_name: Optional[bool] = None

    hide_footers: Optional[bool] = None

    hide_headers: Optional[bool] = None

    high_res_ocr: Optional[bool] = None

    html_make_all_elements_visible: Optional[bool] = None

    html_remove_fixed_elements: Optional[bool] = None

    html_remove_navigation_elements: Optional[bool] = None

    http_proxy: Optional[str] = None

    ignore_document_elements_for_layout_detection: Optional[bool] = None

    images_to_save: Optional[List[Literal["embedded", "layout", "screenshot"]]] = None

    inline_images_in_markdown: Optional[bool] = None

    input_s3_path: Optional[str] = None

    input_s3_region: Optional[str] = None

    input_url: Optional[str] = None

    internal_is_screenshot_job: Optional[bool] = None

    invalidate_cache: Optional[bool] = None

    is_formatting_instruction: Optional[bool] = None

    job_timeout_extra_time_per_page_in_seconds: Optional[float] = None

    job_timeout_in_seconds: Optional[float] = None

    keep_page_separator_when_merging_tables: Optional[bool] = None

    languages: Optional[List[ParsingLanguages]] = None

    layout_aware: Optional[bool] = None

    line_level_bounding_box: Optional[bool] = None

    markdown_table_multiline_header_separator: Optional[str] = None

    max_pages: Optional[int] = None

    max_pages_enforced: Optional[int] = None

    merge_tables_across_pages_in_markdown: Optional[bool] = None

    model: Optional[str] = None

    outlined_table_extraction: Optional[bool] = None

    output_pdf_of_document: Optional[bool] = None

    output_s3_path_prefix: Optional[str] = None

    output_s3_region: Optional[str] = None

    output_tables_as_html: Optional[bool] = FieldInfo(alias="output_tables_as_HTML", default=None)

    page_error_tolerance: Optional[float] = None

    page_footer_prefix: Optional[str] = None

    page_footer_suffix: Optional[str] = None

    page_header_prefix: Optional[str] = None

    page_header_suffix: Optional[str] = None

    page_prefix: Optional[str] = None

    page_separator: Optional[str] = None

    page_suffix: Optional[str] = None

    parse_mode: Optional[ParsingMode] = None
    """Enum for representing the mode of parsing to be used."""

    parsing_instruction: Optional[str] = None

    precise_bounding_box: Optional[bool] = None

    premium_mode: Optional[bool] = None

    presentation_out_of_bounds_content: Optional[bool] = None

    presentation_skip_embedded_data: Optional[bool] = None

    preserve_layout_alignment_across_pages: Optional[bool] = None

    preserve_very_small_text: Optional[bool] = None

    preset: Optional[str] = None

    priority: Optional[Literal["critical", "high", "low", "medium"]] = None
    """The priority for the request.

    This field may be ignored or overwritten depending on the organization tier.
    """

    project_id: Optional[str] = None

    remove_hidden_text: Optional[bool] = None

    replace_failed_page_mode: Optional[FailPageMode] = None
    """Enum for representing the different available page error handling modes."""

    replace_failed_page_with_error_message_prefix: Optional[str] = None

    replace_failed_page_with_error_message_suffix: Optional[str] = None

    save_images: Optional[bool] = None

    skip_diagonal_text: Optional[bool] = None

    specialized_chart_parsing_agentic: Optional[bool] = None

    specialized_chart_parsing_efficient: Optional[bool] = None

    specialized_chart_parsing_plus: Optional[bool] = None

    specialized_image_parsing: Optional[bool] = None

    spreadsheet_extract_sub_tables: Optional[bool] = None

    spreadsheet_force_formula_computation: Optional[bool] = None

    spreadsheet_include_hidden_sheets: Optional[bool] = None

    strict_mode_buggy_font: Optional[bool] = None

    strict_mode_image_extraction: Optional[bool] = None

    strict_mode_image_ocr: Optional[bool] = None

    strict_mode_reconstruction: Optional[bool] = None

    structured_output: Optional[bool] = None

    structured_output_json_schema: Optional[str] = None

    structured_output_json_schema_name: Optional[str] = None

    system_prompt: Optional[str] = None

    system_prompt_append: Optional[str] = None

    take_screenshot: Optional[bool] = None

    target_pages: Optional[str] = None

    tier: Optional[str] = None

    use_vendor_multimodal_model: Optional[bool] = None

    user_prompt: Optional[str] = None

    vendor_multimodal_api_key: Optional[str] = None

    vendor_multimodal_model_name: Optional[str] = None

    version: Optional[str] = None

    webhook_configurations: Optional[List[WebhookConfiguration]] = None
    """Outbound webhook endpoints to notify on job status changes"""

    webhook_url: Optional[str] = None
