# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict, TypeAliasType

from .._types import SequenceNotStr
from .._compat import PYDANTIC_V1

__all__ = ["MetadataFiltersParam", "Filter", "FilterMetadataFilter"]


class FilterMetadataFilter(TypedDict, total=False):
    """Comprehensive metadata filter for vector stores to support more operators.

    Value uses Strict types, as int, float and str are compatible types and were all
    converted to string before.

    See: https://docs.pydantic.dev/latest/usage/types/#strict-types
    """

    key: Required[str]

    value: Required[Union[float, str, SequenceNotStr[str], Iterable[float], Iterable[int], None]]

    operator: Literal[
        "!=",
        "<",
        "<=",
        "==",
        ">",
        ">=",
        "all",
        "any",
        "contains",
        "in",
        "is_empty",
        "nin",
        "text_match",
        "text_match_insensitive",
    ]
    """Vector store filter operator."""


if TYPE_CHECKING or not PYDANTIC_V1:
    Filter = TypeAliasType("Filter", Union[FilterMetadataFilter, "MetadataFiltersParam"])
else:
    Filter: TypeAlias = Union[FilterMetadataFilter, "MetadataFiltersParam"]


class MetadataFiltersParam(TypedDict, total=False):
    """Metadata filters for vector stores."""

    filters: Required[Iterable[Filter]]

    condition: Optional[Literal["and", "not", "or"]]
    """Vector store filter conditions to combine different filters."""
