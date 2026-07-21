# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["Form", "Json"]

Json: TypeAlias = Annotated[Union["FormField", "FormSection", "FormTable"], PropertyInfo(discriminator="type")]


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
