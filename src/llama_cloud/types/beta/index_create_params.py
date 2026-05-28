# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["IndexCreateParams", "Product"]


class IndexCreateParams(TypedDict, total=False):
    source_directory_id: Required[str]
    """ID of the source directory containing your documents."""

    organization_id: Optional[str]

    project_id: Optional[str]

    description: Optional[str]
    """Optional description of the index."""

    name: Optional[str]
    """Optional display name for the index.

    If omitted, the index is named after the source directory.
    """

    products: Optional[Iterable[Product]]
    """Product configurations for syncing.

    Omit to use a default parse configuration. Include an explicit entry per product
    type (e.g. parse, extract) to override the default.
    """

    store_attachments: Optional[SequenceNotStr[str]]
    """Attachment kinds to store alongside parsed output.

    Each entry must be one of: screenshots, items. For example, ['screenshots']
    renders and stores per-page screenshots; ['items'] stores structured items with
    bounding boxes. Omit or pass an empty list to skip attachments.
    """

    sync_frequency: str
    """How often to re-run the sync.

    One of: manual, daily, on_source_change. Defaults to manual.
    """

    vector_target: Literal["DEFAULT", "DISABLED"]
    """Vector export destination for the index.

    'DEFAULT' exports to the managed vector DB destination resolved from
    configuration. 'DISABLED' skips vector export — the export destination falls
    back to 'Download'.
    """


class Product(TypedDict, total=False):
    """A product configuration to include in an index's sync.

    Structurally mirrors ``directory_sync.SyncProductEntryRequest`` but is a
    distinct class so the Index API surface stays SDK-gen-isolated from
    directory-sync internals. Translation between the two happens in
    ``index/api_utils.py``.
    """

    product_config_id: Required[str]
    """ID of the product configuration."""

    product_type: Required[str]
    """Product type. One of: parse, extract."""
