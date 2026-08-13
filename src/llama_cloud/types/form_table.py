# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Union, Optional
from typing_extensions import Literal, TypeAlias, TypeAliasType

from .._compat import PYDANTIC_V1
from .._models import BaseModel

__all__ = ["FormTable", "Row"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Row = TypeAliasType("Row", Union[str, "FormTableCellItems", None])
else:
    Row: TypeAlias = Union[str, "FormTableCellItems", None]


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

    columns: Optional[List[str]] = None
    """Printed column headers in order, if any"""

    label: Optional[str] = None
    """Printed table caption, if any"""

    type: Optional[Literal["table"]] = None
    """Form table node"""


from .form_table_cell_items import FormTableCellItems
