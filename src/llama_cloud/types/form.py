# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .b_box import BBox
from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "Form",
    "Json",
    "JsonFormText",
    "JsonFormTextGrounding",
    "JsonFormTextGroundingID",
    "JsonFormTextGroundingIDLine",
    "JsonFormTextGroundingIDLineWord",
    "JsonFormTextGroundingLabel",
    "JsonFormTextGroundingLabelLine",
    "JsonFormTextGroundingLabelLineWord",
    "JsonFormTextGroundingValue",
    "JsonFormTextGroundingValueLine",
    "JsonFormTextGroundingValueLineWord",
]


class JsonFormTextGroundingIDLineWord(BaseModel):
    """One grounded word: a `[start, end)` span in the source text and its bbox."""

    bbox: BBox
    """Word bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""


class JsonFormTextGroundingIDLine(BaseModel):
    """One grounded line of text with an optional per-word breakdown."""

    bbox: BBox
    """Line bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""

    words: Optional[List[JsonFormTextGroundingIDLineWord]] = None
    """Per-word grounding within the line, when available"""


class JsonFormTextGroundingID(BaseModel):
    """
    Supported text with half-open UTF-8 byte spans into the complete property string.
    """

    lines: List[JsonFormTextGroundingIDLine]
    """Supported lines.

    Word requests include supported words; gaps are valid. Boxes use final page
    coordinates and optional local rotation r.
    """


class JsonFormTextGroundingLabelLineWord(BaseModel):
    """One grounded word: a `[start, end)` span in the source text and its bbox."""

    bbox: BBox
    """Word bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""


class JsonFormTextGroundingLabelLine(BaseModel):
    """One grounded line of text with an optional per-word breakdown."""

    bbox: BBox
    """Line bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""

    words: Optional[List[JsonFormTextGroundingLabelLineWord]] = None
    """Per-word grounding within the line, when available"""


class JsonFormTextGroundingLabel(BaseModel):
    """
    Supported text with half-open UTF-8 byte spans into the complete property string.
    """

    lines: List[JsonFormTextGroundingLabelLine]
    """Supported lines.

    Word requests include supported words; gaps are valid. Boxes use final page
    coordinates and optional local rotation r.
    """


class JsonFormTextGroundingValueLineWord(BaseModel):
    """One grounded word: a `[start, end)` span in the source text and its bbox."""

    bbox: BBox
    """Word bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""


class JsonFormTextGroundingValueLine(BaseModel):
    """One grounded line of text with an optional per-word breakdown."""

    bbox: BBox
    """Line bounding box"""

    span: List[object]
    """`[start, end)` UTF-8 byte span in the complete source property string"""

    words: Optional[List[JsonFormTextGroundingValueLineWord]] = None
    """Per-word grounding within the line, when available"""


class JsonFormTextGroundingValue(BaseModel):
    """
    Supported text with half-open UTF-8 byte spans into the complete property string.
    """

    lines: List[JsonFormTextGroundingValueLine]
    """Supported lines.

    Word requests include supported words; gaps are valid. Boxes use final page
    coordinates and optional local rotation r.
    """


class JsonFormTextGrounding(BaseModel):
    """
    Optional grounding for a field's printed text; boolean states have no text spans.
    """

    id: Optional[JsonFormTextGroundingID] = None
    """
    Supported text with half-open UTF-8 byte spans into the complete property
    string.
    """

    label: Optional[JsonFormTextGroundingLabel] = None
    """
    Supported text with half-open UTF-8 byte spans into the complete property
    string.
    """

    value: Optional[JsonFormTextGroundingValue] = None
    """
    Supported text with half-open UTF-8 byte spans into the complete property
    string.
    """


class JsonFormText(BaseModel):
    """
    Printed text that is not part of a field, section heading or table: a title, an
    instruction, a note. With it the form JSON holds every printed word of its region.
    """

    value: str
    """The printed text, verbatim"""

    bbox: Optional[List[BBox]] = None
    """Bounding boxes of the text on the page, if attributed."""

    grounding: Optional[JsonFormTextGrounding] = None
    """
    Optional grounding for a field's printed text; boolean states have no text
    spans.
    """

    type: Optional[Literal["text"]] = None
    """Form text node"""


Json: TypeAlias = Annotated[
    Union["FormField", "FormSection", "FormTable", JsonFormText], PropertyInfo(discriminator="type")
]


class Form(BaseModel):
    """One form detected on a page, in two representations of the same content."""

    json_: List[Json] = FieldInfo(alias="json")
    """Structured representation: an ordered tree of sections, fields, and tables"""

    list: "FormListItem"
    """Flattened list representation of the same content"""


from .form_field import FormField
from .form_table import FormTable
from .form_section import FormSection
from .form_list_item import FormListItem
