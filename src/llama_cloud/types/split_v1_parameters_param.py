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

    splitting_strategy: SplittingStrategy
    """Strategy for splitting documents."""
