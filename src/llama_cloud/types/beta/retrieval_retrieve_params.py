# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "RetrievalRetrieveParams",
    "CustomFilters",
    "CustomFiltersFilterTypeUnionStrIntBoolFloat",
    "CustomFiltersUnionMember1",
    "Rerank",
    "StaticFilters",
    "StaticFiltersParsedDirectoryFileID",
]


class RetrievalRetrieveParams(TypedDict, total=False):
    index_id: Required[str]
    """ID of the index to retrieve against."""

    query: Required[str]
    """Natural-language query to retrieve relevant chunks."""

    organization_id: Optional[str]

    project_id: Optional[str]

    custom_filters: Optional[Dict[str, Optional[CustomFilters]]]
    """Filters on user-defined metadata fields."""

    full_text_pipeline_weight: Optional[float]
    """Weight of the full-text search pipeline (0-1)."""

    num_candidates: Optional[int]
    """Number of candidates for approximate nearest neighbor search."""

    rerank: Rerank
    """Reranking configuration applied after hybrid search. Enabled by default."""

    score_threshold: Optional[float]
    """Minimum score threshold for returned results."""

    static_filters: Optional[StaticFilters]
    """Filters on built-in document fields (page range, chunk index, etc.)."""

    top_k: Optional[int]
    """Maximum number of results to return."""

    vector_pipeline_weight: Optional[float]
    """Weight of the vector search pipeline (0-1)."""


class CustomFiltersFilterTypeUnionStrIntBoolFloat(TypedDict, total=False):
    operator: Required[Literal["eq", "ne", "gt", "lt", "gte", "lte", "in", "nin"]]

    value: Required[Union[str, bool, float, SequenceNotStr[Union[str, bool, float]]]]


class CustomFiltersUnionMember1(TypedDict, total=False):
    operator: Required[Literal["eq", "ne", "gt", "lt", "gte", "lte", "in", "nin"]]

    value: Required[Union[float, Iterable[float]]]


CustomFilters: TypeAlias = Union[CustomFiltersFilterTypeUnionStrIntBoolFloat, Iterable[CustomFiltersUnionMember1]]


class Rerank(TypedDict, total=False):
    """Reranking configuration applied after hybrid search. Enabled by default."""

    enabled: bool
    """Set to false to disable reranking."""

    top_n: Optional[int]
    """Number of results to return after reranking."""


class StaticFiltersParsedDirectoryFileID(TypedDict, total=False):
    operator: Required[Literal["eq", "ne", "gt", "lt", "gte", "lte", "in", "nin"]]

    value: Required[Union[str, SequenceNotStr[str]]]


class StaticFilters(TypedDict, total=False):
    """Filters on built-in document fields (page range, chunk index, etc.)."""

    parsed_directory_file_id: Optional[StaticFiltersParsedDirectoryFileID]
