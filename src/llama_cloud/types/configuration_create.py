# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .untyped_parameters import UntypedParameters
from .parse_v2_parameters import ParseV2Parameters
from .split_v1_parameters import SplitV1Parameters
from .extract_v2_parameters import ExtractV2Parameters
from .classify_v2_parameters import ClassifyV2Parameters

__all__ = ["ConfigurationCreate", "Parameters", "ParametersSpreadsheetV1Parameters"]


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
    """
    Whether to generate additional metadata (title, description) for each extracted
    region.
    """

    include_hidden_cells: Optional[bool] = None
    """Whether to include hidden cells when extracting regions from the spreadsheet."""

    sheet_names: Optional[List[str]] = None
    """The names of the sheets to extract regions from.

    If empty, all sheets will be processed.
    """

    specialization: Optional[str] = None
    """Optional specialization mode for domain-specific extraction.

    Supported values: 'financial-standard', 'financial-enhanced',
    'financial-precise'. Default None uses the general-purpose pipeline.
    """

    table_merge_sensitivity: Optional[Literal["strong", "weak"]] = None
    """Influences how likely similar-looking regions are merged into a single table.

    Useful for spreadsheets that either have sparse tables (strong merging) or many
    distinct tables close together (weak merging).
    """

    use_experimental_processing: Optional[bool] = None
    """Enables experimental processing. Accuracy may be impacted."""


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


class ConfigurationCreate(BaseModel):
    """Request body for creating a product configuration."""

    name: str
    """Human-readable name for this configuration."""

    parameters: Parameters
    """Product-specific configuration parameters."""
