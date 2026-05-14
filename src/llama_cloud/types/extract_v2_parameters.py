# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ExtractV2Parameters"]


class ExtractV2Parameters(BaseModel):
    """Typed parameters for an *extract v2* product configuration."""

    data_schema: Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]
    """JSON Schema defining the fields to extract.

    Validate with the /schema/validate endpoint first.
    """

    product_type: Literal["extract_v2"]
    """Product type."""

    cite_sources: Optional[bool] = None
    """Include citations in results"""

    confidence_scores: Optional[bool] = None
    """Include confidence scores in results"""

    extract_version: Optional[str] = None
    """Extract algorithm version.

    Use 'latest' for the default pipeline or a date string (e.g. '2026-01-08') to
    pin to a specific release.
    """

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
    extraction
    """

    parse_tier: Optional[str] = None
    """Parse tier to use before extraction.

    Defaults to the extract tier if not specified.
    """

    system_prompt: Optional[str] = None
    """Custom system prompt to guide extraction behavior"""

    target_pages: Optional[str] = None
    """Comma-separated page numbers or ranges to process (1-based).

    Omit to process all pages.
    """

    tier: Optional[Literal["cost_effective", "agentic"]] = None
    """Extract tier: cost_effective (5 credits/page) or agentic (15 credits/page)"""
