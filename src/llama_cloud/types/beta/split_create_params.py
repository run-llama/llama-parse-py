# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .split_category_param import SplitCategoryParam
from .split_document_input_param import SplitDocumentInputParam

__all__ = ["SplitCreateParams", "Configuration", "ConfigurationSplittingStrategy"]


class SplitCreateParams(TypedDict, total=False):
    document_input: Required[SplitDocumentInputParam]
    """Document to be split."""

    organization_id: Optional[str]

    project_id: Optional[str]

    configuration: Optional[Configuration]
    """Split configuration with categories and splitting strategy."""

    configuration_id: Optional[str]
    """Saved split configuration ID."""


class ConfigurationSplittingStrategy(TypedDict, total=False):
    """Strategy for splitting documents."""

    allow_uncategorized: Literal["forbid", "include", "omit"]
    """Controls handling of pages that don't match any category.

    'include': pages can be grouped as 'uncategorized' and included in results.
    'forbid': all pages must be assigned to a defined category. 'omit': pages can be
    classified as 'uncategorized' but are excluded from results.
    """


class Configuration(TypedDict, total=False):
    """Split configuration with categories and splitting strategy."""

    categories: Required[Iterable[SplitCategoryParam]]
    """Categories to split documents into."""

    splitting_strategy: ConfigurationSplittingStrategy
    """Strategy for splitting documents."""
