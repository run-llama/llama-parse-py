# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..re_rank_config_param import ReRankConfigParam
from ..composite_retrieval_mode import CompositeRetrievalMode

__all__ = ["RetrieverSearchParams"]


class RetrieverSearchParams(TypedDict, total=False):
    query: Required[str]
    """The query to retrieve against."""

    organization_id: Optional[str]

    project_id: Optional[str]

    mode: CompositeRetrievalMode
    """The mode of composite retrieval."""

    rerank_config: ReRankConfigParam
    """The rerank configuration for composite retrieval."""

    rerank_top_n: Optional[int]
    """
    (use rerank_config.top_n instead) The number of nodes to retrieve after
    reranking over retrieved nodes from all retrieval tools.
    """
