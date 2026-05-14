# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ParsingGetParams"]


class ParsingGetParams(TypedDict, total=False):
    expand: SequenceNotStr[str]
    """
    Fields to include: text, markdown, items, metadata, job_metadata,
    text_content_metadata, markdown_content_metadata, items_content_metadata,
    metadata_content_metadata, raw_words_content_metadata, xlsx_content_metadata,
    output_pdf_content_metadata, images_content_metadata. Metadata fields include
    presigned URLs.
    """

    image_filenames: Optional[str]
    """Filter to specific image filenames (optional). Example: image_0.png,image_1.jpg"""

    organization_id: Optional[str]

    project_id: Optional[str]
