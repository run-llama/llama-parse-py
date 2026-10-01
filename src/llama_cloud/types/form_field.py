# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias, TypeAliasType

from pydantic import Field as FieldInfo

from .b_box import BBox
from .._utils import PropertyInfo
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "FormField",
    "Grounding",
    "GroundingID",
    "GroundingIDLine",
    "GroundingIDLineWord",
    "GroundingLabel",
    "GroundingLabelLine",
    "GroundingLabelLineWord",
    "GroundingValue",
    "GroundingValueLine",
    "GroundingValueLineWord",
    "ValueItem",
]


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


class GroundingValueLineWord(BaseModel):
    """One grounded word: a `[start, end)` span in the source text and its bbox."""

    bbox: BBox
    """Word bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""


class GroundingValueLine(BaseModel):
    """One grounded line of text with an optional per-word breakdown."""

    bbox: BBox
    """Line bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""

    words: Optional[List[GroundingValueLineWord]] = None
    """Per-word grounding within the line, when available"""


class GroundingValue(BaseModel):
    """
    Supported text with half-open UTF-8 byte spans into the complete property string.
    """

    lines: List[GroundingValueLine]
    """Supported lines.

    Word requests include supported words; gaps are valid. Boxes use final page
    coordinates and optional local rotation r.
    """


class Grounding(BaseModel):
    """
    Optional grounding for a field's printed text; boolean states have no text spans.
    """

    id: Optional[GroundingID] = None
    """
    Supported text with half-open UTF-8 byte spans into the complete property
    string.
    """

    label: Optional[GroundingLabel] = None
    """
    Supported text with half-open UTF-8 byte spans into the complete property
    string.
    """

    value: Optional[GroundingValue] = None
    """
    Supported text with half-open UTF-8 byte spans into the complete property
    string.
    """


if TYPE_CHECKING or not PYDANTIC_V1:
    ValueItem = TypeAliasType(
        "ValueItem", Annotated[Union["FormField", "FormSection", "FormTable"], PropertyInfo(discriminator="type")]
    )
else:
    ValueItem: TypeAlias = Annotated[Union["FormField", "FormSection", "FormTable"], PropertyInfo(discriminator="type")]


class FormField(BaseModel):
    """
    One labeled form entry: a text input, checkbox, select group, or signature line.
    """

    field: Literal["checkbox", "multi_select", "signature", "single_select", "text"]
    """
    Kind of entry: text (any free-text input), checkbox, single_select,
    multi_select, or signature
    """

    id: Optional[str] = None
    """Field number/letter printed on the form (e.g. '1a'), if any"""

    bbox: Optional[List[BBox]] = None
    """Bounding boxes of the field's fillable area on the page."""

    grounding: Optional[Grounding] = None
    """
    Optional grounding for a field's printed text; boolean states have no text
    spans.
    """

    is_empty: Optional[bool] = FieldInfo(alias="isEmpty", default=None)
    """True for a printed-but-blank text field (mutually exclusive with value)"""

    label: Optional[str] = None
    """Printed field caption, if any"""

    type: Optional[Literal["field"]] = None
    """Form field node"""

    value: Union[str, bool, None] = None
    """
    Entered content: verbatim text for text fields, or a boolean for checkbox
    (checked) and signature (signed). Absent on blank text fields and on select
    groups
    """

    value_items: Optional[List[ValueItem]] = FieldInfo(alias="valueItems", default=None)
    """Options of a single_select/multi_select group (only on select fields)"""


from .form_table import FormTable
from .form_section import FormSection
