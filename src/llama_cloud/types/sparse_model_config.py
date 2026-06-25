# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SparseModelConfig"]


class SparseModelConfig(BaseModel):
    """Configuration for sparse embedding models used in hybrid search.

    This allows users to choose between Splade and BM25 models for
    sparse retrieval in managed data sinks.
    """

    class_name: Optional[str] = None

    api_model_type: Optional[Literal["auto", "bm25", "splade"]] = FieldInfo(alias="model_type", default=None)
    """The sparse model type to use.

    'bm25' uses Qdrant's FastEmbed BM25 model (default for new pipelines), 'splade'
    uses HuggingFace Splade model, 'auto' selects based on deployment mode (BYOC
    uses term frequency, Cloud uses Splade).
    """
