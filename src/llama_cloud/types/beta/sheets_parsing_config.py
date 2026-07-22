# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SheetsParsingConfig"]


class SheetsParsingConfig(BaseModel):
    """Configuration for spreadsheet parsing and region extraction"""

    extraction_range: Optional[str] = None
    """A1 notation of the range to extract a single region from.

    If None, the entire sheet is used.
    """

    flatten_hierarchical_tables: Optional[bool] = None
    """
    Return a flattened dataframe when a detected table is recognized as
    hierarchical.
    """

    generate_additional_metadata: Optional[bool] = None
    """Deprecated: controlled by `tier`.

    Whether to generate additional metadata (title, description) for each extracted
    region. Honored only on `agentic`.
    """

    include_hidden_cells: Optional[bool] = None
    """Whether to include hidden cells when extracting regions from the spreadsheet."""

    sheet_names: Optional[List[str]] = None
    """The names of the sheets to extract regions from.

    If empty, all sheets will be processed.
    """

    specialization: Optional[str] = None
    """Deprecated: controlled by `tier`.

    Optional specialization mode for domain-specific extraction. Supported values:
    'financial-standard', 'financial-enhanced', 'financial-precise'. Default None
    uses the general-purpose pipeline. Honored only on `agentic`.
    """

    table_merge_sensitivity: Optional[Literal["strong", "weak"]] = None
    """Deprecated: controlled by `tier`.

    Influences how likely similar-looking regions are merged into a single table.
    Honored only on `agentic`.
    """

    tier: Optional[Literal["agentic", "cost_effective"]] = None
    """Spreadsheet extraction tier.

    `cost_effective` uses the rule-based/ML-only pipeline; `agentic` uses the full
    pipeline.
    """

    use_experimental_processing: Optional[bool] = None
    """Deprecated: controlled by `tier`.

    Enables experimental processing. Honored only on `agentic`.
    """
