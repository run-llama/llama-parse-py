# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias, TypeAliasType

from .b_box import BBox
from .._utils import PropertyInfo
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "FormTableCellItems",
    "Item",
    "ItemFormText",
    "ItemFormTextGrounding",
    "ItemFormTextGroundingID",
    "ItemFormTextGroundingIDLine",
    "ItemFormTextGroundingIDLineWord",
    "ItemFormTextGroundingLabel",
    "ItemFormTextGroundingLabelLine",
    "ItemFormTextGroundingLabelLineWord",
    "ItemFormTextGroundingValue",
    "ItemFormTextGroundingValueLine",
    "ItemFormTextGroundingValueLineWord",
]


class ItemFormTextGroundingIDLineWord(BaseModel):
    """One grounded word: a `[start, end)` span in the source text and its bbox."""

    bbox: BBox
    """Word bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""


class ItemFormTextGroundingIDLine(BaseModel):
    """One grounded line of text with an optional per-word breakdown."""

    bbox: BBox
    """Line bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""

    words: Optional[List[ItemFormTextGroundingIDLineWord]] = None
    """Per-word grounding within the line, when available"""


class ItemFormTextGroundingID(BaseModel):
    """
    Supported text with half-open UTF-8 byte spans into the complete property string.
    """

    lines: List[ItemFormTextGroundingIDLine]
    """Supported lines.

    Word requests include supported words; gaps are valid. Boxes use final page
    coordinates and optional local rotation r.
    """


class ItemFormTextGroundingLabelLineWord(BaseModel):
    """One grounded word: a `[start, end)` span in the source text and its bbox."""

    bbox: BBox
    """Word bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""


class ItemFormTextGroundingLabelLine(BaseModel):
    """One grounded line of text with an optional per-word breakdown."""

    bbox: BBox
    """Line bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""

    words: Optional[List[ItemFormTextGroundingLabelLineWord]] = None
    """Per-word grounding within the line, when available"""


class ItemFormTextGroundingLabel(BaseModel):
    """
    Supported text with half-open UTF-8 byte spans into the complete property string.
    """

    lines: List[ItemFormTextGroundingLabelLine]
    """Supported lines.

    Word requests include supported words; gaps are valid. Boxes use final page
    coordinates and optional local rotation r.
    """


class ItemFormTextGroundingValueLineWord(BaseModel):
    """One grounded word: a `[start, end)` span in the source text and its bbox."""

    bbox: BBox
    """Word bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""


class ItemFormTextGroundingValueLine(BaseModel):
    """One grounded line of text with an optional per-word breakdown."""

    bbox: BBox
    """Line bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""

    words: Optional[List[ItemFormTextGroundingValueLineWord]] = None
    """Per-word grounding within the line, when available"""


class ItemFormTextGroundingValue(BaseModel):
    """
    Supported text with half-open UTF-8 byte spans into the complete property string.
    """

    lines: List[ItemFormTextGroundingValueLine]
    """Supported lines.

    Word requests include supported words; gaps are valid. Boxes use final page
    coordinates and optional local rotation r.
    """


class ItemFormTextGrounding(BaseModel):
    """
    Optional grounding for a field's printed text; boolean states have no text spans.
    """

    id: Optional[ItemFormTextGroundingID] = None
    """
    Supported text with half-open UTF-8 byte spans into the complete property
    string.
    """

    label: Optional[ItemFormTextGroundingLabel] = None
    """
    Supported text with half-open UTF-8 byte spans into the complete property
    string.
    """

    value: Optional[ItemFormTextGroundingValue] = None
    """
    Supported text with half-open UTF-8 byte spans into the complete property
    string.
    """


class ItemFormText(BaseModel):
    """
    Printed text that is not part of a field, section heading or table: a title, an
    instruction, a note. With it the form JSON holds every printed word of its region.
    """

    value: str
    """The printed text, verbatim"""

    bbox: Optional[List[BBox]] = None
    """Bounding boxes of the text on the page, if attributed."""

    grounding: Optional[ItemFormTextGrounding] = None
    """
    Optional grounding for a field's printed text; boolean states have no text
    spans.
    """

    type: Optional[Literal["text"]] = None
    """Form text node"""


if TYPE_CHECKING or not PYDANTIC_V1:
    Item = TypeAliasType(
        "Item",
        Annotated[Union["FormField", "FormSection", "FormTable", ItemFormText], PropertyInfo(discriminator="type")],
    )
else:
    Item: TypeAlias = Annotated[
        Union["FormField", "FormSection", "FormTable", ItemFormText], PropertyInfo(discriminator="type")
    ]


class FormTableCellItems(BaseModel):
    """A table cell holding its own form nodes (e.g. a checkbox column)."""

    items: List[Item]
    """Form nodes inside the cell"""


from .form_field import FormField
from .form_table import FormTable
from .form_section import FormSection
