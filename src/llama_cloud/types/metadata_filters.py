# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["MetadataFilters", "Filter", "FilterMetadataFilter"]


class FilterMetadataFilter(BaseModel):
    """Comprehensive metadata filter for vector stores to support more operators.

    Value uses Strict types, as int, float and str are compatible types and were all
    converted to string before.

    See: https://docs.pydantic.dev/latest/usage/types/#strict-types
    """

    key: str

    value: Union[float, str, List[str], List[float], List[int], None] = None

    operator: Optional[
        Literal[
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
    ] = None
    """Vector store filter operator."""


if TYPE_CHECKING or not PYDANTIC_V1:
    Filter = TypeAliasType("Filter", Union[FilterMetadataFilter, "MetadataFilters"])
else:
    Filter: TypeAlias = Union[FilterMetadataFilter, "MetadataFilters"]


class MetadataFilters(BaseModel):
    """Metadata filters for vector stores."""

    filters: List[Filter]

    condition: Optional[Literal["and", "not", "or"]] = None
    """Vector store filter conditions to combine different filters."""
