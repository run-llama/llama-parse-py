# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .cloud_document_create_param import CloudDocumentCreateParam

__all__ = ["DocumentCreateParams"]


class DocumentCreateParams(TypedDict, total=False):
    body: Required[Iterable[CloudDocumentCreateParam]]

    project_id: Optional[str]
