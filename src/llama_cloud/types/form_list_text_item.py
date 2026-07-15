# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FormListTextItem"]


class FormListTextItem(BaseModel):
    """One line of a form's list representation."""

    md: str
    """Markdown representation of the line"""

    value: str
    """Line content (e.g. '[1a] Wages: 29,513')"""

    type: Optional[Literal["text"]] = None
    """Text line"""
