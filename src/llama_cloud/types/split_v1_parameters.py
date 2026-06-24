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

    splitting_strategy: Optional[SplittingStrategy] = None
    """Strategy for splitting documents."""
