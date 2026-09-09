# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["SheetsParsingConfigParam"]


class SheetsParsingConfigParam(TypedDict, total=False):
    """Configuration for spreadsheet parsing and region extraction"""

    extraction_range: Optional[str]
    """A1 notation of the range to extract a single region from.

    If None, the entire sheet is used.
    """

    flatten_hierarchical_tables: bool
    """
    Return a flattened dataframe when a detected table is recognized as
    hierarchical.
    """

    generate_additional_metadata: bool
    """Deprecated: controlled by `tier`.

    Whether to generate additional metadata (title, description) for each extracted
    region. Honored only on `agentic`.
    """

    include_hidden_cells: bool
    """Whether to include hidden cells when extracting regions from the spreadsheet."""

    sheet_names: Optional[SequenceNotStr[str]]
    """The names of the sheets to extract regions from.

    If empty, all sheets will be processed.
    """

    specialization: Optional[str]
    """Deprecated: controlled by `tier`.

    Optional specialization mode for domain-specific extraction. Supported values:
    'financial-standard', 'financial-enhanced', 'financial-precise'. Default None
    uses the general-purpose pipeline. Honored only on `agentic`.
    """

    table_merge_sensitivity: Literal["strong", "weak"]
    """Deprecated: controlled by `tier`.

    Influences how likely similar-looking regions are merged into a single table.
    Honored only on `agentic`.
    """

    tier: Literal["agentic", "cost_effective"]
    """Spreadsheet extraction tier.

    `cost_effective` uses the rule-based/ML-only pipeline; `agentic` uses the full
    pipeline.
    """

    use_experimental_processing: bool
    """Deprecated: controlled by `tier`.

    Enables experimental processing. Honored only on `agentic`.
    """
