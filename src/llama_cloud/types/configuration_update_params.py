# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .untyped_parameters_param import UntypedParametersParam
from .parse_v2_parameters_param import ParseV2ParametersParam
from .split_v1_parameters_param import SplitV1ParametersParam
from .extract_v2_parameters_param import ExtractV2ParametersParam
from .classify_v2_parameters_param import ClassifyV2ParametersParam

__all__ = ["ConfigurationUpdateParams", "Parameters", "ParametersSpreadsheetV1Parameters"]


class ConfigurationUpdateParams(TypedDict, total=False):
    organization_id: Optional[str]

    project_id: Optional[str]

    name: Optional[str]
    """Updated name (omit to leave unchanged)."""

    parameters: Optional[Parameters]
    """Updated parameters (omit to leave unchanged)."""


class ParametersSpreadsheetV1Parameters(TypedDict, total=False):
    """Typed parameters for a *spreadsheet v1* product configuration."""

    product_type: Required[Literal["spreadsheet_v1"]]
    """Product type."""

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
    """
    Whether to generate additional metadata (title, description) for each extracted
    region.
    """

    include_hidden_cells: bool
    """Whether to include hidden cells when extracting regions from the spreadsheet."""

    sheet_names: Optional[SequenceNotStr[str]]
    """The names of the sheets to extract regions from.

    If empty, all sheets will be processed.
    """

    specialization: Optional[str]
    """Optional specialization mode for domain-specific extraction.

    Supported values: 'financial-standard', 'financial-enhanced',
    'financial-precise'. Default None uses the general-purpose pipeline.
    """

    table_merge_sensitivity: Literal["strong", "weak"]
    """Influences how likely similar-looking regions are merged into a single table.

    Useful for spreadsheets that either have sparse tables (strong merging) or many
    distinct tables close together (weak merging).
    """

    use_experimental_processing: bool
    """Enables experimental processing. Accuracy may be impacted."""


Parameters: TypeAlias = Union[
    ClassifyV2ParametersParam,
    ExtractV2ParametersParam,
    ParseV2ParametersParam,
    SplitV1ParametersParam,
    ParametersSpreadsheetV1Parameters,
    UntypedParametersParam,
]
