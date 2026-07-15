# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel
from .form_list_text_item import FormListTextItem

__all__ = ["FormListItem", "Item"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Item = TypeAliasType("Item", Union[FormListTextItem, "FormListItem"])
else:
    Item: TypeAlias = Union[FormListTextItem, "FormListItem"]


class FormListItem(BaseModel):
    """The list representation of form content: nested lists of rendered field lines."""

    items: List[Item]
    """Nested lines and sub-lists, in the form's reading order"""

    md: str
    """Markdown representation of this list"""

    ordered: bool
    """Whether the list is ordered"""

    type: Optional[Literal["list"]] = None
    """List node"""
