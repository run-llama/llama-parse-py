# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .b_box import BBox
from .._utils import PropertyInfo
from .._models import BaseModel
from .code_item import CodeItem
from .link_item import LinkItem
from .text_item import TextItem
from .image_item import ImageItem
from .table_item import TableItem
from .heading_item import HeadingItem

__all__ = ["FooterItem", "Item"]

Item: TypeAlias = Annotated[
    Union[CodeItem, HeadingItem, ImageItem, LinkItem, "ListItem", TableItem, TextItem],
    PropertyInfo(discriminator="type"),
]


class FooterItem(BaseModel):
    items: List[Item]
    """List of items within the footer"""

    md: str
    """Markdown representation preserving formatting"""

    bbox: Optional[List[BBox]] = None
    """List of bounding boxes"""

    type: Optional[Literal["footer"]] = None
    """Page footer container"""


from .list_item import ListItem
