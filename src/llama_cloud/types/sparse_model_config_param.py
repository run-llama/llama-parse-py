# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SparseModelConfigParam"]


class SparseModelConfigParam(TypedDict, total=False):
    """Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.
    """

    class_name: str

    model_type: Literal["auto", "bm25", "splade"]
    """The sparse model type to use.

    'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade'
    uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC
    uses term frequency, Cloud uses Splade).
    """
