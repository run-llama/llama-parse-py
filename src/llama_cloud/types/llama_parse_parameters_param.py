# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo
from .parsing_mode import ParsingMode
from .fail_page_mode import FailPageMode
from .parsing_languages import ParsingLanguages

__all__ = ["LlamaParseParametersParam", "WebhookConfiguration"]


class WebhookConfiguration(TypedDict, total=False):
    """Configuration for a single outbound webhook endpoint."""

    webhook_events: Optional[
        List[
            Literal[
                "batch.cancelled",
                "batch.error",
                "batch.pending",
                "batch.running",
                "batch.success",
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
    ]
    """Events to subscribe to (e.g.

    'parse.success', 'extract.error'). If null, all events are delivered.
    """

    webhook_headers: Optional[Dict[str, str]]
    """Custom HTTP headers sent with each webhook request (e.g. auth tokens)"""

    webhook_output_format: Optional[str]
    """Response format sent to the webhook: 'string' (default) or 'json'"""

    webhook_signing_secret: Optional[str]
    """Shared signing secret used to sign webhook deliveries.

    When set, each request includes an HMAC-SHA256 signature of the request body in
    the 'LC-Signature' header (value 'sha256=<hex>'). Recompute the HMAC over the
    raw request body with this secret to verify the delivery is authentic.
    """

    webhook_url: Optional[str]
    """URL to receive webhook POST notifications"""


class LlamaParseParametersParam(TypedDict, total=False):
    adaptive_long_table: Optional[bool]

    aggressive_table_extraction: Optional[bool]

    annotate_links: Optional[bool]

    annotate_revisions: Optional[bool]

    auto_mode: Optional[bool]

    auto_mode_configuration_json: Optional[str]

    auto_mode_trigger_on_image_in_page: Optional[bool]

    auto_mode_trigger_on_regexp_in_page: Optional[str]

    auto_mode_trigger_on_table_in_page: Optional[bool]

    auto_mode_trigger_on_text_in_page: Optional[str]

    azure_openai_api_version: Optional[str]

    azure_openai_deployment_name: Optional[str]

    azure_openai_endpoint: Optional[str]

    azure_openai_key: Optional[str]

    bbox_bottom: Optional[float]

    bbox_left: Optional[float]

    bbox_right: Optional[float]

    bbox_top: Optional[float]

    bounding_box: Optional[str]

    compact_markdown_table: Optional[bool]

    complemental_formatting_instruction: Optional[str]

    confidence_score_effort: Optional[str]

    content_guideline_instruction: Optional[str]

    continuous_mode: Optional[bool]

    disable_image_extraction: Optional[bool]

    disable_ocr: Optional[bool]

    disable_reconstruction: Optional[bool]

    do_not_cache: Optional[bool]

    do_not_unroll_columns: Optional[bool]

    enable_cost_optimizer: Optional[bool]

    extract_charts: Optional[bool]

    extract_layout: Optional[bool]

    extract_printed_page_number: Optional[bool]

    fast_mode: Optional[bool]

    formatting_instruction: Optional[str]

    gpt4o_api_key: Optional[str]

    gpt4o_mode: Optional[bool]

    guess_xlsx_sheet_name: Optional[bool]

    hide_footers: Optional[bool]

    hide_headers: Optional[bool]

    high_res_ocr: Optional[bool]

    html_make_all_elements_visible: Optional[bool]

    html_remove_fixed_elements: Optional[bool]

    html_remove_navigation_elements: Optional[bool]

    http_proxy: Optional[str]

    ignore_document_elements_for_layout_detection: Optional[bool]

    images_to_save: Optional[List[Literal["embedded", "layout", "screenshot"]]]

    inline_images_in_markdown: Optional[bool]

    input_s3_path: Optional[str]

    input_s3_region: Optional[str]

    input_url: Optional[str]

    internal_is_screenshot_job: Optional[bool]

    invalidate_cache: Optional[bool]

    is_formatting_instruction: Optional[bool]

    job_timeout_extra_time_per_page_in_seconds: Optional[float]

    job_timeout_in_seconds: Optional[float]

    keep_page_separator_when_merging_tables: Optional[bool]

    languages: List[ParsingLanguages]

    layout_aware: Optional[bool]

    line_level_bounding_box: Optional[bool]

    markdown_table_multiline_header_separator: Optional[str]

    max_pages: Optional[int]

    max_pages_enforced: Optional[int]

    merge_tables_across_pages_in_markdown: Optional[bool]

    model: Optional[str]

    outlined_table_extraction: Optional[bool]

    output_pdf_of_document: Optional[bool]

    output_s3_path_prefix: Optional[str]

    output_s3_region: Optional[str]

    output_tables_as_html: Annotated[Optional[bool], PropertyInfo(alias="output_tables_as_HTML")]

    page_error_tolerance: Optional[float]

    page_footer_prefix: Optional[str]

    page_footer_suffix: Optional[str]

    page_header_prefix: Optional[str]

    page_header_suffix: Optional[str]

    page_prefix: Optional[str]

    page_separator: Optional[str]

    page_suffix: Optional[str]

    parse_mode: Optional[ParsingMode]
    """Enum for representing the mode of parsing to be used."""

    parsing_instruction: Optional[str]

    precise_bounding_box: Optional[bool]

    premium_mode: Optional[bool]

    presentation_out_of_bounds_content: Optional[bool]

    presentation_skip_embedded_data: Optional[bool]

    preserve_layout_alignment_across_pages: Optional[bool]

    preserve_very_small_text: Optional[bool]

    preset: Optional[str]

    priority: Optional[Literal["critical", "high", "low", "medium"]]
    """The priority for the request.

    This field may be ignored or overwritten depending on the organization tier.
    """

    project_id: Optional[str]

    remove_hidden_text: Optional[bool]

    replace_failed_page_mode: Optional[FailPageMode]
    """Enum for representing the different available page error handling modes."""

    replace_failed_page_with_error_message_prefix: Optional[str]

    replace_failed_page_with_error_message_suffix: Optional[str]

    save_images: Optional[bool]

    skip_diagonal_text: Optional[bool]

    specialized_chart_parsing_agentic: Optional[bool]

    specialized_chart_parsing_efficient: Optional[bool]

    specialized_chart_parsing_plus: Optional[bool]

    specialized_image_parsing: Optional[bool]

    spreadsheet_extract_sub_tables: Optional[bool]

    spreadsheet_force_formula_computation: Optional[bool]

    spreadsheet_include_hidden_sheets: Optional[bool]

    strict_mode_buggy_font: Optional[bool]

    strict_mode_image_extraction: Optional[bool]

    strict_mode_image_ocr: Optional[bool]

    strict_mode_reconstruction: Optional[bool]

    structured_output: Optional[bool]

    structured_output_json_schema: Optional[str]

    structured_output_json_schema_name: Optional[str]

    system_prompt: Optional[str]

    system_prompt_append: Optional[str]

    take_screenshot: Optional[bool]

    target_pages: Optional[str]

    tier: Optional[str]

    use_vendor_multimodal_model: Optional[bool]

    user_prompt: Optional[str]

    vendor_multimodal_api_key: Optional[str]

    vendor_multimodal_model_name: Optional[str]

    version: Optional[str]

    webhook_configurations: Optional[Iterable[WebhookConfiguration]]
    """Outbound webhook endpoints to notify on job status changes"""

    webhook_url: Optional[str]
