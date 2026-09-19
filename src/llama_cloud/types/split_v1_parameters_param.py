# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .beta.split_category_param import SplitCategoryParam

__all__ = ["SplitV1ParametersParam", "SplittingStrategy"]


class SplittingStrategy(TypedDict, total=False):
    """Strategy for splitting documents."""

    allow_uncategorized: Literal["forbid", "include", "omit"]
    """Controls handling of pages that don't match any category.

    'include': pages can be grouped as 'uncategorized' and included in results.
    'forbid': all pages must be assigned to a defined category. 'omit': pages can be
    classified as 'uncategorized' but are excluded from results.
    """

    custom_instructions: Optional[str]
    """Free-form guidance for where segment boundaries are placed."""

    min_pages_per_split: int
    """Minimum pages per segment.

    Shorter segments are merged into an adjacent segment; 1 disables merging.
    """


class SplitV1ParametersParam(TypedDict, total=False):
    """Typed parameters for a *split v1* product configuration."""

    categories: Required[Iterable[SplitCategoryParam]]
    """Categories to split documents into."""

    product_type: Required[Literal["split_v1"]]
    """Product type."""

    parse_config_id: Optional[str]
    """
    Saved parse configuration ID to control how the document is parsed before
    splitting. Takes precedence over parse_tier. Configurations that restrict pages
    (`target_pages` or `max_pages` on the parse configuration) are rejected: split
    results number pages relative to the full document. Ignored when a completed
    parse job is supplied as file_input.
    """

    parse_tier: Optional[Literal["agentic", "agentic_plus", "cost_effective", "fast"]]
    """Parse tier used to read the document before splitting.

    Defaults to fast. Ignored when a completed parse job is supplied as file_input.
    """

    splitting_strategy: SplittingStrategy
    """Strategy for splitting documents."""

    target_pages: Optional[str]
    """Comma-separated page numbers or ranges to split (1-based).

    Omit to split all pages. Requires a completed parse job as file_input.
    """

    version: Optional[str]
    """Split version to run.

    Omit for the current release. Preview versions are selectable by name and never
    resolved automatically.
    """
