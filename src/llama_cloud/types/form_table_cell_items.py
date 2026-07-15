# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union
from typing_extensions import Annotated, TypeAlias, TypeAliasType

from .._utils import PropertyInfo
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["FormTableCellItems", "Item"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Item = TypeAliasType(
        "Item", Annotated[Union["FormField", "FormSection", "FormTable"], PropertyInfo(discriminator="type")]
    )
else:
    Item: TypeAlias = Annotated[Union["FormField", "FormSection", "FormTable"], PropertyInfo(discriminator="type")]


class FormTableCellItems(BaseModel):
    """A table cell holding its own form nodes (e.g. a checkbox column)."""

    items: List[Item]
    """Form nodes inside the cell"""


from .form_field import FormField
from .form_table import FormTable
from .form_section import FormSection
