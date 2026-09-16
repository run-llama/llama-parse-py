# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .beta.split_category import SplitCategory

__all__ = ["SplitV1Parameters", "SplittingStrategy"]


class SplittingStrategy(BaseModel):
    """Strategy for splitting documents."""

    allow_uncategorized: Optional[Literal["forbid", "include", "omit"]] = None
    """Controls handling of pages that don't match any category.

    'include': pages can be grouped as 'uncategorized' and included in results.
    'forbid': all pages must be assigned to a defined category. 'omit': pages can be
    classified as 'uncategorized' but are excluded from results.
    """


class SplitV1Parameters(BaseModel):
    """Typed parameters for a *split v1* product configuration."""

    categories: List[SplitCategory]
    """Categories to split documents into."""

    product_type: Literal["split_v1"]
    """Product type."""

    parse_config_id: Optional[str] = None
    """
    Saved parse configuration ID controlling how the document is read before
    splitting. Takes precedence over parse_tier. Configurations restricted to a page
    subset (target_pages or max_pages) are rejected, since split results always
    number pages relative to the full document. Ignored when a completed parse job
    is supplied as file_input.
    """

    parse_tier: Optional[Literal["agentic", "agentic_plus", "cost_effective", "fast"]] = None
    """Parse tier used to read the document before splitting.

    Defaults to fast. Ignored when a completed parse job is supplied as file_input.
    """

    splitting_strategy: Optional[SplittingStrategy] = None
    """Strategy for splitting documents."""
