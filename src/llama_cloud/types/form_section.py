# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias, TypeAliasType

from .._utils import PropertyInfo
from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["FormSection", "Item"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Item = TypeAliasType(
        "Item", Annotated[Union["FormField", "FormSection", "FormTable"], PropertyInfo(discriminator="type")]
    )
else:
    Item: TypeAlias = Annotated[Union["FormField", "FormSection", "FormTable"], PropertyInfo(discriminator="type")]


class FormSection(BaseModel):
    """A grouping of form content, in the form's reading order."""

    items: List[Item]
    """Child form nodes in reading order"""

    id: Optional[str] = None
    """Identifier printed on the form (e.g. 'Part III'), if any"""

    label: Optional[str] = None
    """Printed section heading, if any"""

    type: Optional[Literal["section"]] = None
    """Form section node"""


from .form_field import FormField
from .form_table import FormTable
