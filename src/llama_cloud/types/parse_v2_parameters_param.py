# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .parsing_languages import ParsingLanguages

__all__ = [
    "ParseV2ParametersParam",
    "AgenticOptions",
    "CropBox",
    "InputOptions",
    "InputOptionsHTML",
    "InputOptionsPresentation",
    "InputOptionsSpreadsheet",
    "OutputOptions",
    "OutputOptionsMarkdown",
    "OutputOptionsMarkdownTables",
    "OutputOptionsSpatialText",
    "OutputOptionsTablesAsSpreadsheet",
    "PageRanges",
    "ProcessingControl",
    "ProcessingControlJobFailureConditions",
    "ProcessingControlTimeouts",
    "ProcessingOptions",
    "ProcessingOptionsAutoModeConfiguration",
    "ProcessingOptionsAutoModeConfigurationParsingConf",
    "ProcessingOptionsAutoModeConfigurationParsingConfCropBox",
    "ProcessingOptionsAutoModeConfigurationParsingConfIgnore",
    "ProcessingOptionsAutoModeConfigurationParsingConfPresentation",
    "ProcessingOptionsAutoModeConfigurationParsingConfSpatialText",
    "ProcessingOptionsCostOptimizer",
    "ProcessingOptionsIgnore",
    "ProcessingOptionsOcrParameters",
    "WebhookConfiguration",
]


class AgenticOptions(TypedDict, total=False):
    """Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

    These options customize how the AI processes and interprets document content.
    Only applicable when using non-fast tiers.
    """

    custom_prompt: Optional[str]
    """Custom instructions for the AI parser.

    Use to guide extraction behavior, specify output formatting, or provide
    domain-specific context. Example: 'Extract financial tables with currency
    symbols. Format dates as YYYY-MM-DD.'
    """


class CropBox(TypedDict, total=False):
    """Crop boundaries to process only a portion of each page.

    Values are ratios 0-1 from page edges
    """

    bottom: Optional[float]
    """Bottom boundary as ratio (0-1).

    0=top edge, 1=bottom edge. Content below this line is excluded
    """

    left: Optional[float]
    """Left boundary as ratio (0-1).

    0=left edge, 1=right edge. Content left of this line is excluded
    """

    right: Optional[float]
    """Right boundary as ratio (0-1).

    0=left edge, 1=right edge. Content right of this line is excluded
    """

    top: Optional[float]
    """Top boundary as ratio (0-1).

    0=top edge, 1=bottom edge. Content above this line is excluded
    """


class InputOptionsHTML(TypedDict, total=False):
    """HTML/web page parsing options (applies to .html, .htm files)"""

    make_all_elements_visible: Optional[bool]
    """
    Force all HTML elements to be visible by overriding CSS display/visibility
    properties. Useful for parsing pages with hidden content or collapsed sections
    """

    remove_fixed_elements: Optional[bool]
    """
    Remove fixed-position elements (headers, footers, floating buttons) that appear
    on every page render
    """

    remove_navigation_elements: Optional[bool]
    """Remove navigation elements (nav bars, sidebars, menus) to focus on main content"""


class InputOptionsPresentation(TypedDict, total=False):
    """Presentation parsing options (applies to .pptx, .ppt, .odp, .key files)"""

    out_of_bounds_content: Optional[bool]
    """Extract content positioned outside the visible slide area.

    Some presentations have hidden notes or content that extends beyond slide
    boundaries
    """

    skip_embedded_data: Optional[bool]
    """Skip extraction of embedded chart data tables.

    When true, only the visual representation of charts is captured, not the
    underlying data
    """


class InputOptionsSpreadsheet(TypedDict, total=False):
    """Spreadsheet parsing options (applies to .xlsx, .xls, .csv, .ods files)"""

    detect_sub_tables_in_sheets: Optional[bool]
    """Detect and extract multiple tables within a single sheet.

    Useful when spreadsheets contain several data regions separated by blank
    rows/columns
    """

    force_formula_computation_in_sheets: Optional[bool]
    """Compute formula results instead of extracting formula text.

    Use when you need calculated values rather than formula definitions
    """

    include_hidden_sheets: Optional[bool]
    """Parse hidden sheets in addition to visible ones.

    By default, hidden sheets are skipped
    """


class InputOptions(TypedDict, total=False):
    """Format-specific options (HTML, PDF, spreadsheet, presentation).

    Applied based on detected input file type
    """

    html: InputOptionsHTML
    """HTML/web page parsing options (applies to .html, .htm files)"""

    pdf: object
    """PDF-specific parsing options (applies to .pdf files)"""

    presentation: InputOptionsPresentation
    """Presentation parsing options (applies to .pptx, .ppt, .odp, .key files)"""

    spreadsheet: InputOptionsSpreadsheet
    """Spreadsheet parsing options (applies to .xlsx, .xls, .csv, .ods files)"""


class OutputOptionsMarkdownTables(TypedDict, total=False):
    """Table formatting options including markdown vs HTML format and merging behavior"""

    compact_markdown_tables: Optional[bool]
    """Remove extra whitespace padding in markdown table cells for more compact output"""

    markdown_table_multiline_separator: Optional[str]
    """Separator string for multiline cell content in markdown tables.

    Example: '&lt;br&gt;' to preserve line breaks, ' ' to join with spaces
    """

    merge_continued_tables: Optional[bool]
    """Automatically merge tables that span multiple pages into a single table.

    The merged table appears on the first page with merged_from_pages metadata
    """

    output_tables_as_markdown: Optional[bool]
    """Output tables as markdown pipe tables instead of HTML &lt;table&gt; tags.

    Markdown tables are simpler but cannot represent complex structures like merged
    cells
    """


class OutputOptionsMarkdown(TypedDict, total=False):
    """Markdown formatting options including table styles and link annotations"""

    annotate_links: Optional[bool]
    """Add link annotations to markdown output in the format [text](url).

    When false, only the link text is included
    """

    inline_images: Optional[bool]
    """
    Embed images directly in markdown as base64 data URIs instead of extracting them
    as separate files. Useful for self-contained markdown output
    """

    tables: OutputOptionsMarkdownTables
    """Table formatting options including markdown vs HTML format and merging behavior"""


class OutputOptionsSpatialText(TypedDict, total=False):
    """Spatial text output options for preserving document layout structure"""

    do_not_unroll_columns: Optional[bool]
    """
    Keep multi-column layouts intact instead of linearizing columns into sequential
    text. Automatically enabled for non-fast tiers
    """

    preserve_layout_alignment_across_pages: Optional[bool]
    """Maintain consistent text column alignment across page boundaries.

    Automatically enabled for document-level parsing modes
    """

    preserve_very_small_text: Optional[bool]
    """Include text below the normal size threshold.

    Useful for footnotes, watermarks, or fine print that might otherwise be filtered
    out
    """


class OutputOptionsTablesAsSpreadsheet(TypedDict, total=False):
    """Options for exporting tables as XLSX spreadsheets"""

    enable: Optional[bool]
    """Whether this option is enabled"""

    guess_sheet_name: bool
    """
    Automatically generate descriptive sheet names from table context (headers,
    surrounding text) instead of using generic names like 'Table_1'
    """


class OutputOptions(TypedDict, total=False):
    """Output formatting options for markdown, text, and extracted images"""

    additional_outputs: SequenceNotStr[str]
    """Optional additional output artifacts to save alongside the primary parse output.

    Each value opts in to generating and persisting one extra file; the empty list
    (default) saves none. The three accepted values are: 'stripped_md' — per-page
    markdown stripped of formatting (links, bold/italic, images, HTML), saved as
    JSON for full-text-search indexing; fetch via
    `expand=stripped_markdown_content_metadata`. 'concatenated_stripped_txt' — all
    stripped pages concatenated into a single plain-text file with `\n\n---\n\n`
    between pages, useful for feeding the document into search or embedding
    pipelines as one blob; fetch via
    `expand=concatenated_stripped_markdown_content_metadata`. 'word_bbox' — raw
    word-level bounding boxes (one JSON object per word, with page number and
    x/y/w/h coordinates) saved as JSONL, useful for highlighting or grounding
    extracted answers back to the source document; fetch via
    `expand=raw_words_content_metadata`.
    """

    extract_printed_page_number: Optional[bool]
    """
    Extract the printed page number as it appears in the document (e.g., 'Page 5 of
    10', 'v', 'A-3'). Useful for referencing original page numbers
    """

    images_to_save: List[Literal["screenshot", "embedded", "layout"]]
    """Image categories to extract and save.

    Options: 'screenshot' (full page renders useful for visual QA), 'embedded'
    (images found within the document), 'layout' (cropped regions from layout
    detection like figures and diagrams). Empty list saves no images
    """

    markdown: OutputOptionsMarkdown
    """Markdown formatting options including table styles and link annotations"""

    spatial_text: OutputOptionsSpatialText
    """Spatial text output options for preserving document layout structure"""

    tables_as_spreadsheet: OutputOptionsTablesAsSpreadsheet
    """Options for exporting tables as XLSX spreadsheets"""


class PageRanges(TypedDict, total=False):
    """Page selection: limit total pages or specify exact pages to process"""

    max_pages: Optional[int]
    """Maximum number of pages to process.

    Pages are processed in order starting from page 1. If both max_pages and
    target_pages are set, target_pages takes precedence
    """

    target_pages: Optional[str]
    """Comma-separated list of specific pages to process using 1-based indexing.

    Supports individual pages and ranges. Examples: '1,3,5' (pages 1, 3, 5), '1-5'
    (pages 1 through 5 inclusive), '1,3,5-8,10' (pages 1, 3, 5-8, and 10). Pages are
    sorted and deduplicated automatically. Duplicate pages cause an error
    """


class ProcessingControlJobFailureConditions(TypedDict, total=False):
    """
    Quality thresholds that determine when a job should fail vs complete with partial results
    """

    allowed_page_failure_ratio: Optional[float]
    """Maximum ratio of pages allowed to fail before the job fails (0-1).

    Example: 0.1 means job fails if more than 10% of pages fail. Default is 0.05
    (5%)
    """

    fail_on_buggy_font: Optional[bool]
    """
    Fail the job if a problematic font is detected that may cause incorrect text
    extraction. Buggy fonts can produce garbled or missing characters
    """

    fail_on_image_extraction_error: Optional[bool]
    """Fail the entire job if any embedded image cannot be extracted.

    By default, image extraction errors are logged but don't fail the job
    """

    fail_on_image_ocr_error: Optional[bool]
    """Fail the entire job if OCR fails on any image.

    By default, OCR errors result in empty text for that image
    """

    fail_on_markdown_reconstruction_error: Optional[bool]
    """Fail the entire job if markdown cannot be reconstructed for any page.

    By default, failed pages use fallback text extraction
    """


class ProcessingControlTimeouts(TypedDict, total=False):
    """Timeout settings for job execution. Increase for large or complex documents"""

    base_in_seconds: Optional[int]
    """Base timeout for the job in seconds (max 7200 = 2 hours).

    This is the minimum time allowed regardless of document size
    """

    extra_time_per_page_in_seconds: Optional[int]
    """Additional timeout per page in seconds (max 300 = 5 minutes).

    Total timeout = base + (this value × page count)
    """


class ProcessingControl(TypedDict, total=False):
    """Job execution controls including timeouts and failure thresholds"""

    job_failure_conditions: ProcessingControlJobFailureConditions
    """
    Quality thresholds that determine when a job should fail vs complete with
    partial results
    """

    timeouts: ProcessingControlTimeouts
    """Timeout settings for job execution. Increase for large or complex documents"""


class ProcessingOptionsAutoModeConfigurationParsingConfCropBox(TypedDict, total=False):
    """Crop box options for auto mode parsing configuration."""

    bottom: Optional[float]
    """Bottom boundary of crop box as ratio (0-1)"""

    left: Optional[float]
    """Left boundary of crop box as ratio (0-1)"""

    right: Optional[float]
    """Right boundary of crop box as ratio (0-1)"""

    top: Optional[float]
    """Top boundary of crop box as ratio (0-1)"""


class ProcessingOptionsAutoModeConfigurationParsingConfIgnore(TypedDict, total=False):
    """Ignore options for auto mode parsing configuration."""

    ignore_diagonal_text: Optional[bool]
    """Whether to ignore diagonal text in the document"""

    ignore_hidden_text: Optional[bool]
    """Whether to ignore hidden text in the document"""


class ProcessingOptionsAutoModeConfigurationParsingConfPresentation(TypedDict, total=False):
    """Presentation-specific options for auto mode parsing configuration."""

    out_of_bounds_content: Optional[bool]
    """Extract out of bounds content in presentation slides"""

    skip_embedded_data: Optional[bool]
    """Skip extraction of embedded data for charts in presentation slides"""


class ProcessingOptionsAutoModeConfigurationParsingConfSpatialText(TypedDict, total=False):
    """Spatial text options for auto mode parsing configuration."""

    do_not_unroll_columns: Optional[bool]
    """Keep column structure intact without unrolling"""

    preserve_layout_alignment_across_pages: Optional[bool]
    """Preserve text alignment across page boundaries"""

    preserve_very_small_text: Optional[bool]
    """Include very small text in spatial output"""


class ProcessingOptionsAutoModeConfigurationParsingConf(TypedDict, total=False):
    """Parsing configuration to apply when trigger conditions are met"""

    adaptive_long_table: Optional[bool]
    """Whether to use adaptive long table handling"""

    aggressive_table_extraction: Optional[bool]
    """Whether to use aggressive table extraction"""

    crop_box: Optional[ProcessingOptionsAutoModeConfigurationParsingConfCropBox]
    """Crop box options for auto mode parsing configuration."""

    custom_prompt: Optional[str]
    """Custom AI instructions for matched pages. Overrides the base custom_prompt"""

    extract_layout: Optional[bool]
    """Whether to extract layout information"""

    high_res_ocr: Optional[bool]
    """Whether to use high resolution OCR"""

    ignore: Optional[ProcessingOptionsAutoModeConfigurationParsingConfIgnore]
    """Ignore options for auto mode parsing configuration."""

    language: Optional[str]
    """Primary language of the document"""

    outlined_table_extraction: Optional[bool]
    """Whether to use outlined table extraction"""

    presentation: Optional[ProcessingOptionsAutoModeConfigurationParsingConfPresentation]
    """Presentation-specific options for auto mode parsing configuration."""

    spatial_text: Optional[ProcessingOptionsAutoModeConfigurationParsingConfSpatialText]
    """Spatial text options for auto mode parsing configuration."""

    specialized_chart_parsing: Optional[Literal["agentic_plus", "agentic", "efficient"]]
    """Enable specialized chart parsing with the specified mode"""

    tier: Optional[Literal["fast", "cost_effective", "agentic", "agentic_plus"]]
    """Override the parsing tier for matched pages. Must be paired with version"""

    version: Union[Literal["latest", "2026-05-13", "2026-05-11", "2026-04-09", "2025-12-11"], str, None]
    """Tier version when overriding tier. Required when tier is specified"""


class ProcessingOptionsAutoModeConfiguration(TypedDict, total=False):
    """A single auto mode rule with trigger conditions and parsing configuration.

    Auto mode allows conditional parsing where different configurations are applied
    based on page content, structure, or filename. When triggers match, the
    parsing_conf overrides default settings for that page.
    """

    parsing_conf: Required[ProcessingOptionsAutoModeConfigurationParsingConf]
    """Parsing configuration to apply when trigger conditions are met"""

    filename_match_glob: Optional[str]
    """Single glob pattern to match against filename"""

    filename_match_glob_list: Optional[SequenceNotStr[str]]
    """List of glob patterns to match against filename"""

    filename_regexp: Optional[str]
    """Regex pattern to match against filename"""

    filename_regexp_mode: Optional[str]
    """Regex mode flags (e.g., 'i' for case-insensitive)"""

    full_page_image_in_page: Optional[bool]
    """Trigger if page contains a full-page image (scanned page detection)"""

    full_page_image_in_page_threshold: Union[float, str, None]
    """Threshold for full page image detection (0.0-1.0, default 0.8)"""

    image_in_page: Optional[bool]
    """Trigger if page contains non-screenshot images"""

    layout_element_in_page: Optional[str]
    """Trigger if page contains this layout element type"""

    layout_element_in_page_confidence_threshold: Union[float, str, None]
    """Confidence threshold for layout element detection"""

    page_contains_at_least_n_charts: Union[int, str, None]
    """Trigger if page has more than N charts"""

    page_contains_at_least_n_images: Union[int, str, None]
    """Trigger if page has more than N images"""

    page_contains_at_least_n_layout_elements: Union[int, str, None]
    """Trigger if page has more than N layout elements"""

    page_contains_at_least_n_lines: Union[int, str, None]
    """Trigger if page has more than N lines"""

    page_contains_at_least_n_links: Union[int, str, None]
    """Trigger if page has more than N links"""

    page_contains_at_least_n_numbers: Union[int, str, None]
    """Trigger if page has more than N numeric words"""

    page_contains_at_least_n_percent_numbers: Union[int, str, None]
    """Trigger if page has more than N% numeric words"""

    page_contains_at_least_n_tables: Union[int, str, None]
    """Trigger if page has more than N tables"""

    page_contains_at_least_n_words: Union[int, str, None]
    """Trigger if page has more than N words"""

    page_contains_at_most_n_charts: Union[int, str, None]
    """Trigger if page has fewer than N charts"""

    page_contains_at_most_n_images: Union[int, str, None]
    """Trigger if page has fewer than N images"""

    page_contains_at_most_n_layout_elements: Union[int, str, None]
    """Trigger if page has fewer than N layout elements"""

    page_contains_at_most_n_lines: Union[int, str, None]
    """Trigger if page has fewer than N lines"""

    page_contains_at_most_n_links: Union[int, str, None]
    """Trigger if page has fewer than N links"""

    page_contains_at_most_n_numbers: Union[int, str, None]
    """Trigger if page has fewer than N numeric words"""

    page_contains_at_most_n_percent_numbers: Union[int, str, None]
    """Trigger if page has fewer than N% numeric words"""

    page_contains_at_most_n_tables: Union[int, str, None]
    """Trigger if page has fewer than N tables"""

    page_contains_at_most_n_words: Union[int, str, None]
    """Trigger if page has fewer than N words"""

    page_longer_than_n_chars: Union[int, str, None]
    """Trigger if page has more than N characters"""

    page_md_error: Optional[bool]
    """Trigger on pages with markdown extraction errors"""

    page_shorter_than_n_chars: Union[int, str, None]
    """Trigger if page has fewer than N characters"""

    regexp_in_page: Optional[str]
    """Regex pattern to match in page content"""

    regexp_in_page_mode: Optional[str]
    """Regex mode flags for regexp_in_page"""

    table_in_page: Optional[bool]
    """Trigger if page contains a table"""

    text_in_page: Optional[str]
    """Trigger if page text/markdown contains this string"""

    trigger_mode: Optional[str]
    """
    How to combine multiple trigger conditions: 'and' (all conditions must match,
    this is the default) or 'or' (any single condition can trigger)
    """


class ProcessingOptionsCostOptimizer(TypedDict, total=False):
    """Cost optimizer configuration for reducing parsing costs on simpler pages.

    When enabled, the parser analyzes each page and routes simpler pages to faster,
    cheaper processing while preserving quality for complex pages. Only works with
    'agentic' or 'agentic_plus' tiers.
    """

    enable: Optional[bool]
    """Enable cost-optimized parsing.

    Routes simpler pages to faster processing while complex pages use full AI
    analysis. May reduce speed on some documents. IMPORTANT: Only available with
    'agentic' or 'agentic_plus' tiers
    """


class ProcessingOptionsIgnore(TypedDict, total=False):
    """Options for ignoring specific text types (diagonal, hidden, text in images)"""

    ignore_diagonal_text: Optional[bool]
    """Skip text rotated at an angle (not horizontal/vertical).

    Useful for ignoring watermarks or decorative angled text
    """

    ignore_hidden_text: Optional[bool]
    """Skip text marked as hidden in the document structure.

    Some PDFs contain invisible text layers used for accessibility or search
    indexing
    """

    ignore_text_in_image: Optional[bool]
    """Skip OCR text extraction from embedded images.

    Use when images contain irrelevant text (watermarks, logos) that shouldn't be in
    the output
    """


class ProcessingOptionsOcrParameters(TypedDict, total=False):
    """OCR configuration including language detection settings"""

    languages: Optional[List[ParsingLanguages]]
    """Languages to use for OCR text recognition.

    Specify multiple languages if document contains mixed-language content. Order
    matters - put primary language first. Example: ['en', 'es'] for English with
    Spanish
    """


class ProcessingOptions(TypedDict, total=False):
    """Document processing options including OCR, table extraction, and chart parsing"""

    aggressive_table_extraction: Optional[bool]
    """
    Use aggressive heuristics to detect table boundaries, even without visible
    borders. Useful for documents with borderless or complex tables
    """

    auto_mode_configuration: Optional[Iterable[ProcessingOptionsAutoModeConfiguration]]
    """
    Conditional processing rules that apply different parsing options based on page
    content, document structure, or filename patterns. Each entry defines trigger
    conditions and the parsing configuration to apply when triggered
    """

    cost_optimizer: Optional[ProcessingOptionsCostOptimizer]
    """Cost optimizer configuration for reducing parsing costs on simpler pages.

    When enabled, the parser analyzes each page and routes simpler pages to faster,
    cheaper processing while preserving quality for complex pages. Only works with
    'agentic' or 'agentic_plus' tiers.
    """

    disable_heuristics: Optional[bool]
    """
    Disable automatic heuristics including outlined table extraction and adaptive
    long table handling. Use when heuristics produce incorrect results
    """

    ignore: ProcessingOptionsIgnore
    """Options for ignoring specific text types (diagonal, hidden, text in images)"""

    ocr_parameters: ProcessingOptionsOcrParameters
    """OCR configuration including language detection settings"""

    specialized_chart_parsing: Optional[Literal["agentic_plus", "agentic", "efficient"]]
    """Enable AI-powered chart analysis.

    Modes: 'efficient' (fast, lower cost), 'agentic' (balanced), 'agentic_plus'
    (highest accuracy). Automatically enables extract_layout and
    precise_bounding_box when set
    """


class WebhookConfiguration(TypedDict, total=False):
    """Webhook configuration for receiving parsing job notifications.

    Webhooks are called when specified events occur during job processing.
    Configure multiple webhook configurations to send to different endpoints.
    """

    webhook_events: Optional[SequenceNotStr[str]]
    """Events that trigger this webhook.

    Options: 'parse.success' (job completed), 'parse.failure' (job failed),
    'parse.partial' (some pages failed). If not specified, webhook fires for all
    events
    """

    webhook_headers: Optional[Dict[str, object]]
    """Custom HTTP headers to include in webhook requests.

    Use for authentication tokens or custom routing. Example: {'Authorization':
    'Bearer xyz'}
    """

    webhook_url: Optional[str]
    """HTTPS URL to receive webhook POST requests. Must be publicly accessible"""


class ParseV2ParametersParam(TypedDict, total=False):
    """Configuration for LlamaParse v2 document parsing.

    Includes tier selection, processing options, output formatting,
    page targeting, and webhook delivery. Refer to the LlamaParse
    documentation for details on each field.
    """

    product_type: Required[Literal["parse_v2"]]
    """Product type."""

    tier: Required[Literal["fast", "cost_effective", "agentic", "agentic_plus"]]
    """
    Parsing tier: 'fast' (rule-based, cheapest), 'cost_effective' (balanced),
    'agentic' (AI-powered with custom prompts), or 'agentic_plus' (premium AI with
    highest accuracy)
    """

    version: Required[Union[Literal["latest", "2026-05-13", "2026-05-11", "2026-04-09", "2025-12-11"], str]]
    """Tier version.

    Use 'latest' for the current stable version, or pin a dated version for
    reproducible results. See GET /api/v2/parse/versions for the per-tier list.
    """

    agentic_options: Optional[AgenticOptions]
    """Options for AI-powered parsing tiers (cost_effective, agentic, agentic_plus).

    These options customize how the AI processes and interprets document content.
    Only applicable when using non-fast tiers.
    """

    client_name: Optional[str]
    """Identifier for the client/application making the request.

    Used for analytics and debugging. Example: 'my-app-v2'
    """

    crop_box: CropBox
    """Crop boundaries to process only a portion of each page.

    Values are ratios 0-1 from page edges
    """

    disable_cache: Optional[bool]
    """Bypass result caching and force re-parsing.

    Use when document content may have changed or you need fresh results
    """

    fast_options: Optional[object]
    """Options for fast tier parsing (rule-based, no AI).

    Fast tier uses deterministic algorithms for text extraction without AI
    enhancement. It's the fastest and most cost-effective option, best suited for
    simple documents with standard layouts. Currently has no configurable options
    but reserved for future expansion.
    """

    input_options: InputOptions
    """Format-specific options (HTML, PDF, spreadsheet, presentation).

    Applied based on detected input file type
    """

    output_options: OutputOptions
    """Output formatting options for markdown, text, and extracted images"""

    page_ranges: PageRanges
    """Page selection: limit total pages or specify exact pages to process"""

    processing_control: ProcessingControl
    """Job execution controls including timeouts and failure thresholds"""

    processing_options: ProcessingOptions
    """Document processing options including OCR, table extraction, and chart parsing"""

    webhook_configurations: Iterable[WebhookConfiguration]
    """Webhook endpoints for job status notifications.

    Multiple webhooks can be configured for different events or services
    """
