# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["ReRankConfigParam"]


class ReRankConfigParam(TypedDict, total=False):
    top_n: int
    """
    The number of nodes to retrieve after reranking over retrieved nodes from all
    retrieval tools.
    """

    type: Literal["bedrock", "cohere", "disabled", "llm", "score", "system_default"]
    """The type of reranker to use."""
