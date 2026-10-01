# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .b_box import BBox
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "FormTable",
    "Row",
    "Grounding",
    "GroundingID",
    "GroundingIDLine",
    "GroundingIDLineWord",
    "GroundingColumn",
    "GroundingColumnLine",
    "GroundingColumnLineWord",
    "GroundingLabel",
    "GroundingLabelLine",
    "GroundingLabelLineWord",
    "GroundingRow",
    "GroundingRowLine",
    "GroundingRowLineWord",
]

if TYPE_CHECKING or not PYDANTIC_V1:
    Row = TypeAliasType("Row", Union[str, "FormTableCellItems", None])
else:
    Row: TypeAlias = Union[str, "FormTableCellItems", None]


class GroundingIDLineWord(BaseModel):
    """One grounded word: a `[start, end)` span in the source text and its bbox."""

    bbox: BBox
    """Word bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""


class GroundingIDLine(BaseModel):
    """One grounded line of text with an optional per-word breakdown."""

    bbox: BBox
    """Line bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""

    words: Optional[List[GroundingIDLineWord]] = None
    """Per-word grounding within the line, when available"""


class GroundingID(BaseModel):
    """
    Supported text with half-open UTF-8 byte spans into the complete property string.
    """

    lines: List[GroundingIDLine]
    """Supported lines.

    Word requests include supported words; gaps are valid. Boxes use final page
    coordinates and optional local rotation r.
    """


class GroundingColumnLineWord(BaseModel):
    """One grounded word: a `[start, end)` span in the source text and its bbox."""

    bbox: BBox
    """Word bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""


class GroundingColumnLine(BaseModel):
    """One grounded line of text with an optional per-word breakdown."""

    bbox: BBox
    """Line bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""

    words: Optional[List[GroundingColumnLineWord]] = None
    """Per-word grounding within the line, when available"""


class GroundingColumn(BaseModel):
    """
    Supported text with half-open UTF-8 byte spans into the complete property string.
    """

    lines: List[GroundingColumnLine]
    """Supported lines.

    Word requests include supported words; gaps are valid. Boxes use final page
    coordinates and optional local rotation r.
    """


class GroundingLabelLineWord(BaseModel):
    """One grounded word: a `[start, end)` span in the source text and its bbox."""

    bbox: BBox
    """Word bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""


class GroundingLabelLine(BaseModel):
    """One grounded line of text with an optional per-word breakdown."""

    bbox: BBox
    """Line bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""

    words: Optional[List[GroundingLabelLineWord]] = None
    """Per-word grounding within the line, when available"""


class GroundingLabel(BaseModel):
    """
    Supported text with half-open UTF-8 byte spans into the complete property string.
    """

    lines: List[GroundingLabelLine]
    """Supported lines.

    Word requests include supported words; gaps are valid. Boxes use final page
    coordinates and optional local rotation r.
    """


class GroundingRowLineWord(BaseModel):
    """One grounded word: a `[start, end)` span in the source text and its bbox."""

    bbox: BBox
    """Word bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""


class GroundingRowLine(BaseModel):
    """One grounded line of text with an optional per-word breakdown."""

    bbox: BBox
    """Line bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""

    words: Optional[List[GroundingRowLineWord]] = None
    """Per-word grounding within the line, when available"""


class GroundingRow(BaseModel):
    """
    Supported text with half-open UTF-8 byte spans into the complete property string.
    """

    lines: List[GroundingRowLine]
    """Supported lines.

    Word requests include supported words; gaps are valid. Boxes use final page
    coordinates and optional local rotation r.
    """


class Grounding(BaseModel):
    """Scalar text grounding aligned with the table's columns and ragged rows."""

    id: Optional[GroundingID] = None
    """
    Supported text with half-open UTF-8 byte spans into the complete property
    string.
    """

    columns: Optional[List[GroundingColumn]] = None
    """Column text grounding in source order; blank slots have empty lines"""

    label: Optional[GroundingLabel] = None
    """
    Supported text with half-open UTF-8 byte spans into the complete property
    string.
    """

    rows: Optional[List[List[GroundingRow]]] = None
    """
    Scalar cell text grounding aligned with rows; blank and structured slots have
    empty lines. Structured children carry their own grounding.
    """


class FormTable(BaseModel):
    """
    A fillable grid printed on the form: repeating records or a row-by-column matrix.
    """

    rows: List[List[Optional[Row]]]
    """
    Table cells: a verbatim string, null for a printed-but-blank cell, or an object
    holding the cell's own form nodes
    """

    id: Optional[str] = None
    """Identifier printed on the form, if any"""

    bbox: Optional[List[BBox]] = None
    """Bounding boxes of the table's fillable regions on the page."""

    columns: Optional[List[str]] = None
    """Printed column headers in order, if any"""

    grounding: Optional[Grounding] = None
    """Scalar text grounding aligned with the table's columns and ragged rows."""

    label: Optional[str] = None
    """Printed table caption, if any"""

    type: Optional[Literal["table"]] = None
    """Form table node"""


from .form_table_cell_items import FormTableCellItems
