# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["IndexCreateParams", "Product"]


class IndexCreateParams(TypedDict, total=False):
    source_directory_id: Required[str]
    """ID of the source directory containing your documents."""

    organization_id: Optional[str]

    project_id: Optional[str]

    description: Optional[str]
    """Optional description of the index."""

    products: Optional[Iterable[Product]]
    """Product configurations for syncing.

    Omit to use a default parse configuration. Include an explicit entry per product
    type (e.g. parse, extract) to override the default.
    """


class Product(TypedDict, total=False):
    """A product configuration to include in a sync."""

    product_config_id: Required[str]
    """ID of the product configuration."""

    product_type: Required[Literal["parse", "extract"]]
    """Product type: parse or extract."""
