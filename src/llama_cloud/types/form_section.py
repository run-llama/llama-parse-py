# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias, TypeAliasType

from .b_box import BBox
from .._utils import PropertyInfo
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = [
    "FormSection",
    "Item",
    "Grounding",
    "GroundingID",
    "GroundingIDLine",
    "GroundingIDLineWord",
    "GroundingLabel",
    "GroundingLabelLine",
    "GroundingLabelLineWord",
]

if TYPE_CHECKING or not PYDANTIC_V1:
    Item = TypeAliasType(
        "Item", Annotated[Union["FormField", "FormSection", "FormTable"], PropertyInfo(discriminator="type")]
    )
else:
    Item: TypeAlias = Annotated[Union["FormField", "FormSection", "FormTable"], PropertyInfo(discriminator="type")]


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


class Grounding(BaseModel):
    """Optional grounding for printed identifiers and headings."""

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


class FormSection(BaseModel):
    """A grouping of form content, in the form's reading order."""

    items: List[Item]
    """Child form nodes in reading order"""

    id: Optional[str] = None
    """Identifier printed on the form (e.g. 'Part III'), if any"""

    grounding: Optional[Grounding] = None
    """Optional grounding for printed identifiers and headings."""

    label: Optional[str] = None
    """Printed section heading, if any"""

    type: Optional[Literal["section"]] = None
    """Form section node"""


from .form_field import FormField
from .form_table import FormTable
