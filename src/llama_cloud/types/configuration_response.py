# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .untyped_parameters import UntypedParameters
from .parse_v2_parameters import ParseV2Parameters
from .split_v1_parameters import SplitV1Parameters
from .extract_v2_parameters import ExtractV2Parameters
from .classify_v2_parameters import ClassifyV2Parameters

__all__ = ["ConfigurationResponse", "Parameters", "ParametersSpreadsheetV1Parameters"]


class ParametersSpreadsheetV1Parameters(BaseModel):
    """Typed parameters for a *spreadsheet v1* product configuration."""

    product_type: Literal["spreadsheet_v1"]
    """Product type."""

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


Parameters: TypeAlias = Annotated[
    Union[
        ClassifyV2Parameters,
        ExtractV2Parameters,
        ParseV2Parameters,
        SplitV1Parameters,
        ParametersSpreadsheetV1Parameters,
        UntypedParameters,
    ],
    PropertyInfo(discriminator="product_type"),
]


class ConfigurationResponse(BaseModel):
    """Response schema for a single product configuration."""

    id: str
    """Unique configuration ID."""

    name: str
    """Configuration name."""

    parameters: Parameters
    """Product-specific configuration parameters."""

    product_type: Literal["classify_v2", "extract_v2", "parse_v2", "split_v1", "spreadsheet_v1", "unknown"]
    """Product type."""

    version: str
    """Version identifier (datetime string)."""

    created_at: Optional[datetime] = None
    """Creation timestamp."""

    updated_at: Optional[datetime] = None
    """Last update timestamp."""
