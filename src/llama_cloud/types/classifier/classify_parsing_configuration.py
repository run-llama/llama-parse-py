# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from ..parsing_languages import ParsingLanguages

__all__ = ["ClassifyParsingConfiguration"]


class ClassifyParsingConfiguration(BaseModel):
    """Parsing configuration for a classify job."""

    lang: Optional[ParsingLanguages] = None
    """The language to parse the files in"""

    max_pages: Optional[int] = None
    """The maximum number of pages to parse"""

    target_pages: Optional[List[int]] = None
    """The pages to target for parsing (0-indexed, so first page is at 0)"""
