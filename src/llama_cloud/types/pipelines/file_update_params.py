# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

__all__ = ["FileUpdateParams"]


class FileUpdateParams(TypedDict, total=False):
    pipeline_id: Required[str]

    custom_metadata: Optional[Dict[str, Union[Dict[str, object], Iterable[object], str, float, bool, None]]]
    """Custom metadata for the file"""
