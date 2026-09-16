# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
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


class SplitV1ParametersParam(TypedDict, total=False):
    """Typed parameters for a *split v1* product configuration."""

    categories: Required[Iterable[SplitCategoryParam]]
    """Categories to split documents into."""

    product_type: Required[Literal["split_v1"]]
    """Product type."""

    parse_config_id: Optional[str]
    """
    Saved parse configuration ID controlling how the document is read before
    splitting. Takes precedence over parse_tier. Configurations restricted to a page
    subset (target_pages or max_pages) are rejected, since split results always
    number pages relative to the full document. Ignored when a completed parse job
    is supplied as file_input.
    """

    parse_tier: Optional[Literal["agentic", "agentic_plus", "cost_effective", "fast"]]
    """Parse tier used to read the document before splitting.

    Defaults to fast. Ignored when a completed parse job is supplied as file_input.
    """

    splitting_strategy: SplittingStrategy
    """Strategy for splitting documents."""
