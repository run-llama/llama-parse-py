# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import TypedDict

from ..parsing_languages import ParsingLanguages

__all__ = ["ClassifyParsingConfigurationParam"]


class ClassifyParsingConfigurationParam(TypedDict, total=False):
    """Parsing configuration for a classify job."""

    lang: ParsingLanguages
    """The language to parse the files in"""

    max_pages: Optional[int]
    """The maximum number of pages to parse"""

    target_pages: Optional[Iterable[int]]
    """The pages to target for parsing (0-indexed, so first page is at 0)"""
