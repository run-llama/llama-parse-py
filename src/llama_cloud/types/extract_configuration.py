# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExtractConfiguration"]


class ExtractConfiguration(BaseModel):
    """Extract configuration combining parse and extract settings."""

    data_schema: Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]
    """JSON Schema defining the fields to extract.

    Validate with the /schema/validate endpoint first.
    """

    cite_sources: Optional[bool] = None
    """Include citations in results.

    Returned under `extract_metadata` (auto-included when set). Text-level on
    `turbo` (no bounding boxes).
    """

    confidence_scores: Optional[bool] = None
    """Include confidence scores in results.

    Returned under `extract_metadata` (auto-included when set).
    """

    disable_cache: Optional[bool] = None
    """Disable reuse and storage of Extract results"""

    extraction_target: Optional[Literal["per_doc", "per_page", "per_table_row"]] = None
    """
    Granularity of extraction: per_doc returns one object per document, per_page
    returns one object per page, per_table_row returns one object per table row
    """

    max_pages: Optional[int] = None
    """Maximum number of pages to process. Omit for no limit."""

    parse_config_id: Optional[str] = None
    """
    Saved parse configuration ID to control how the document is parsed before
    extraction. Turbo extract does not support parse configuration or produce a
    parse output; use another tier if your workflow requires parsed text.
    """

    parse_tier: Optional[str] = None
    """Parse tier to use before extraction.

    Defaults to the extract tier if not specified. Turbo extract does not support
    parse configuration or produce a parse output; use another tier if your workflow
    requires parsed text.
    """

    sheet_names: Optional[List[str]] = None
    """Optional worksheet names to extract when spreadsheet_mode is on.

    Overrides target_pages for spreadsheets; omit to extract every sheet. Names are
    matched exactly (case-sensitive) — pass them as a list, e.g. ["Sheet 1", "My
    Sheet"].
    """

    spreadsheet_mode: Optional[bool] = None
    """Beta.

    When true, extract structured data directly from a spreadsheet workbook
    (.xlsx/.xls/.csv) — the agent reads cells straight from the workbook instead of
    the standard document path. Off by default (spreadsheets keep the standard
    path). Requires the agentic_plus tier. Billed on the standard per-page extract
    rate, against a page count derived from workbook size. Citations and confidence
    scores are not available in this mode.
    """

    system_prompt: Optional[str] = None
    """Custom system prompt to guide extraction behavior"""

    target_pages: Optional[str] = None
    """Comma-separated page numbers or ranges to process (1-based).

    Omit to process all pages.
    """

    tier: Optional[Literal["agentic", "agentic_plus", "cost_effective", "turbo"]] = None
    """
    Extract tier: cost_effective (5 credits/page), agentic (15 credits/page),
    agentic_plus (50 credits/page), or turbo (35 credits/page, experimental)
    """

    version: Optional[str] = None
    """
    Use 'latest' for the latest release for the selected tier or a date string
    (YYYY-MM-DD format) to pin to the nearest release at or before that date. Job
    responses always report the concrete resolved version the job runs, fixed at job
    creation; saved configurations keep the value as provided.
    """
