# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExtractConfigurationParam"]


class ExtractConfigurationParam(TypedDict, total=False):
    """Extract configuration combining parse and extract settings."""

    data_schema: Required[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """JSON Schema defining the fields to extract.

    Validate with the /schema/validate endpoint first.
    """

    cite_sources: bool
    """Include citations in results"""

    confidence_scores: bool
    """Include confidence scores in results"""

    extraction_target: Literal["per_doc", "per_page", "per_table_row"]
    """
    Granularity of extraction: per_doc returns one object per document, per_page
    returns one object per page, per_table_row returns one object per table row
    """

    max_pages: Optional[int]
    """Maximum number of pages to process. Omit for no limit."""

    parse_config_id: Optional[str]
    """
    Saved parse configuration ID to control how the document is parsed before
    extraction
    """

    parse_tier: Optional[str]
    """Parse tier to use before extraction.

    Defaults to the extract tier if not specified.
    """

    system_prompt: Optional[str]
    """Custom system prompt to guide extraction behavior"""

    target_pages: Optional[str]
    """Comma-separated page numbers or ranges to process (1-based).

    Omit to process all pages.
    """

    tier: Literal["agentic", "agentic_plus", "cost_effective"]
    """
    Extract tier: cost_effective (5 credits/page), agentic (15 credits/page), or
    agentic_plus (50 credits/page)
    """

    version: str
    """
    Use 'latest' for the latest release for the selected tier or a date string
    (YYYY-MM-DD format) to pin to the nearest release at or before that date. Job
    responses always report the concrete resolved version the job runs, fixed at job
    creation; saved configurations keep the value as provided.
    """
