# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .b_box import BBox
from .._models import BaseModel

__all__ = [
    "FormText",
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


class FormText(BaseModel):
    """
    Printed text that is not part of a field, section heading or table: a title, an
    instruction, a note. With it the form JSON holds every printed word of its region.
    """

    value: str
    """The printed text, verbatim"""

    bbox: Optional[List[BBox]] = None
    """Bounding boxes of the text on the page, if attributed."""

    grounding: Optional[Grounding] = None
    """
    Optional grounding for a field's printed text; boolean states have no text
    spans.
    """

    type: Optional[Literal["text"]] = None
    """Form text node"""
