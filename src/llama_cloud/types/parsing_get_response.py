# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .code_item import CodeItem
from .link_item import LinkItem
from .text_item import TextItem
from .image_item import ImageItem
from .table_item import TableItem
from .heading_item import HeadingItem

__all__ = [
    "ParsingGetResponse",
    "Job",
    "Forms",
    "FormsPage",
    "FormsPageFormsResultPage",
    "FormsPageFormsResultPageForm",
    "FormsPageFormsResultPageFormJson",
    "FormsPageFormsResultPageFormJsonFormField",
    "FormsPageFormsResultPageFormJsonFormSection",
    "FormsPageFormsResultPageFormJsonFormTable",
    "FormsPageFormsResultPageFormList",
    "FormsPageFormsResultPageFormListItem",
    "FormsPageFormsResultPageFormListItemFormListTextItem",
    "FormsPageFailedFormsPage",
    "ImagesContentMetadata",
    "ImagesContentMetadataImage",
    "ImagesContentMetadataImageBbox",
    "Items",
    "ItemsPage",
    "ItemsPageStructuredResultPage",
    "ItemsPageStructuredResultPageItem",
    "ItemsPageFailedStructuredPage",
    "Markdown",
    "MarkdownPage",
    "MarkdownPageMarkdownResultPage",
    "MarkdownPageFailedMarkdownPage",
    "Metadata",
    "MetadataPage",
    "ResultContentMetadata",
    "Text",
    "TextPage",
]


class Job(BaseModel):
    """Parse job status and metadata"""

    id: str
    """Unique parse job identifier"""

    project_id: str
    """Project this job belongs to"""

    status: Literal["CANCELLED", "COMPLETED", "FAILED", "PENDING", "RUNNING"]
    """Current job status: PENDING, RUNNING, COMPLETED, FAILED, or CANCELLED"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    error_message: Optional[str] = None
    """Error details when status is FAILED"""

    name: Optional[str] = None
    """Optional display name for this parse job"""

    tier: Optional[str] = None
    """Parsing tier used for this job"""

    updated_at: Optional[datetime] = None
    """Update datetime"""

    user_metadata: Optional[Dict[str, str]] = None
    """Key/value tags associated with this job."""


class FormsPageFormsResultPageFormJsonFormField(BaseModel):
    """
    One labeled form entry: a text input, checkbox, select group, or signature line.
    """

    field: Literal["checkbox", "multi_select", "signature", "single_select", "text"]
    """
    Kind of entry: text (any free-text input), checkbox, single_select,
    multi_select, or signature
    """

    id: Optional[str] = None
    """Field number/letter printed on the form (e.g. '1a'), if any"""

    is_empty: Optional[bool] = FieldInfo(alias="isEmpty", default=None)
    """True for a printed-but-blank text field (mutually exclusive with value)"""

    label: Optional[str] = None
    """Printed field caption, if any"""

    type: Optional[Literal["field"]] = None
    """Form field node"""

    value: Union[str, bool, None] = None
    """
    Entered content: verbatim text for text fields, or a boolean for checkbox
    (checked) and signature (signed). Absent on blank text fields and on select
    groups
    """

    value_items: Optional[List[object]] = FieldInfo(alias="valueItems", default=None)
    """Options of a single_select/multi_select group (only on select fields)"""


class FormsPageFormsResultPageFormJsonFormSection(BaseModel):
    """A grouping of form content, in the form's reading order."""

    items: List[object]
    """Child form nodes in reading order"""

    id: Optional[str] = None
    """Identifier printed on the form (e.g. 'Part III'), if any"""

    label: Optional[str] = None
    """Printed section heading, if any"""

    type: Optional[Literal["section"]] = None
    """Form section node"""


class FormsPageFormsResultPageFormJsonFormTable(BaseModel):
    """
    A fillable grid printed on the form: repeating records or a row-by-column matrix.
    """

    rows: List[List[Union[str, object, None]]]
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


FormsPageFormsResultPageFormJson: TypeAlias = Annotated[
    Union[
        FormsPageFormsResultPageFormJsonFormField,
        FormsPageFormsResultPageFormJsonFormSection,
        FormsPageFormsResultPageFormJsonFormTable,
    ],
    PropertyInfo(discriminator="type"),
]


class FormsPageFormsResultPageFormListItemFormListTextItem(BaseModel):
    """One line of a form's list representation."""

    md: str
    """Markdown representation of the line"""

    value: str
    """Line content (e.g. '[1a] Wages: 29,513')"""

    type: Optional[Literal["text"]] = None
    """Text line"""


FormsPageFormsResultPageFormListItem: TypeAlias = Union[FormsPageFormsResultPageFormListItemFormListTextItem, object]


class FormsPageFormsResultPageFormList(BaseModel):
    """Flattened list representation of the same content"""

    items: List[FormsPageFormsResultPageFormListItem]
    """Nested lines and sub-lists, in the form's reading order"""

    md: str
    """Markdown representation of this list"""

    ordered: bool
    """Whether the list is ordered"""

    type: Optional[Literal["list"]] = None
    """List node"""


class FormsPageFormsResultPageForm(BaseModel):
    """One form detected on a page, in two representations of the same content."""

    json_: List[FormsPageFormsResultPageFormJson] = FieldInfo(alias="json")
    """Structured representation: an ordered tree of sections, fields, and tables"""

    list: FormsPageFormsResultPageFormList
    """Flattened list representation of the same content"""


class FormsPageFormsResultPage(BaseModel):
    """Forms found on one page. Pages without form content have an empty forms list."""

    forms: List[FormsPageFormsResultPageForm]
    """Forms detected on the page"""

    page_number: int
    """Page number of the document"""

    success: Literal[True]
    """Success indicator"""


class FormsPageFailedFormsPage(BaseModel):
    """A page whose processing failed."""

    error: str
    """Error message describing the failure"""

    page_number: int
    """Page number of the document"""

    success: Literal[False]
    """Failure indicator"""


FormsPage: TypeAlias = Union[FormsPageFormsResultPage, FormsPageFailedFormsPage]


class Forms(BaseModel):
    """Per-page form analysis results (one entry per page)."""

    pages: List[FormsPage]
    """List of form pages or failed page entries"""


class ImagesContentMetadataImageBbox(BaseModel):
    """Bounding box for an image on its page."""

    h: int
    """Height of the bounding box"""

    w: int
    """Width of the bounding box"""

    x: int
    """X coordinate of the bounding box"""

    y: int
    """Y coordinate of the bounding box"""


class ImagesContentMetadataImage(BaseModel):
    """Metadata for a single extracted image."""

    filename: str
    """Image filename (e.g., 'image_0.png')"""

    index: int
    """Index of the image in the extraction order"""

    bbox: Optional[ImagesContentMetadataImageBbox] = None
    """Bounding box for an image on its page."""

    category: Optional[Literal["embedded", "layout", "screenshot"]] = None
    """
    Image category: 'screenshot' (full page), 'embedded' (images in document), or
    'layout' (cropped from layout detection)
    """

    content_type: Optional[str] = None
    """MIME type of the image"""

    presigned_url: Optional[str] = None
    """Presigned URL to download the image"""

    size_bytes: Optional[int] = None
    """Deprecated: always returns None. Will be removed in a future release."""


class ImagesContentMetadata(BaseModel):
    """Metadata for all extracted images."""

    images: List[ImagesContentMetadataImage]
    """List of image metadata with presigned URLs"""

    total_count: int
    """Total number of extracted images"""


ItemsPageStructuredResultPageItem: TypeAlias = Annotated[
    Union[CodeItem, "FooterItem", "HeaderItem", HeadingItem, ImageItem, LinkItem, "ListItem", TableItem, TextItem],
    PropertyInfo(discriminator="type"),
]


class ItemsPageStructuredResultPage(BaseModel):
    items: List[ItemsPageStructuredResultPageItem]
    """List of structured items on the page"""

    page_height: float
    """Height of the page in points"""

    page_number: int
    """Page number of the document"""

    page_width: float
    """Width of the page in points"""

    success: Literal[True]
    """Success indicator"""


class ItemsPageFailedStructuredPage(BaseModel):
    error: str
    """Error message describing the failure"""

    page_number: int
    """Page number of the document"""

    success: Literal[False]
    """Failure indicator"""


ItemsPage: TypeAlias = Union[ItemsPageStructuredResultPage, ItemsPageFailedStructuredPage]


class Items(BaseModel):
    """Structured JSON result (if requested)"""

    pages: List[ItemsPage]
    """List of structured pages or failed page entries"""


class MarkdownPageMarkdownResultPage(BaseModel):
    markdown: str
    """Markdown content of the page"""

    page_number: int
    """Page number of the document"""

    success: Literal[True]
    """Success indicator"""

    footer: Optional[str] = None
    """Footer of the page in markdown"""

    header: Optional[str] = None
    """Header of the page in markdown"""


class MarkdownPageFailedMarkdownPage(BaseModel):
    error: str
    """Error message describing the failure"""

    page_number: int
    """Page number of the document"""

    success: Literal[False]
    """Failure indicator"""


MarkdownPage: TypeAlias = Union[MarkdownPageMarkdownResultPage, MarkdownPageFailedMarkdownPage]


class Markdown(BaseModel):
    """Markdown result (if requested)"""

    pages: List[MarkdownPage]
    """List of markdown pages or failed page entries"""


class MetadataPage(BaseModel):
    """Page-level metadata including confidence scores and presentation-specific data."""

    page_number: int
    """Page number of the document"""

    confidence: Optional[float] = None
    """Confidence score for the page parsing (0-1)"""

    cost_optimized: Optional[bool] = None
    """Whether cost-optimized parsing was used for the page"""

    original_orientation_angle: Optional[int] = None
    """Original orientation angle of the page in degrees"""

    printed_page_number: Optional[str] = None
    """Printed page number as it appears in the document"""

    slide_section_name: Optional[str] = None
    """Section name from presentation slides"""

    speaker_notes: Optional[str] = None
    """Speaker notes from presentation slides"""

    triggered_auto_mode: Optional[bool] = None
    """Whether auto mode was triggered for the page"""


class Metadata(BaseModel):
    """Result containing metadata (page level and general) for the parsed document."""

    pages: List[MetadataPage]
    """List of page metadata entries"""


class ResultContentMetadata(BaseModel):
    """Metadata about a specific result type stored in S3."""

    size_bytes: int
    """Size of the result file in bytes"""

    exists: Optional[bool] = None
    """Whether the result file exists in S3"""

    presigned_url: Optional[str] = None
    """Presigned URL to download the result file"""


class TextPage(BaseModel):
    page_number: int
    """Page number of the document"""

    text: str
    """Plain text content of the page"""


class Text(BaseModel):
    """Plain text result (if requested)"""

    pages: List[TextPage]
    """List of text pages"""


class ParsingGetResponse(BaseModel):
    """Parse result response with job status and optional content or metadata.

    The job field is always included. Other fields are included based on expand parameters.
    """

    job: Job
    """Parse job status and metadata"""

    forms: Optional[Forms] = None
    """Per-page form analysis results (one entry per page)."""

    images_content_metadata: Optional[ImagesContentMetadata] = None
    """Metadata for all extracted images."""

    items: Optional[Items] = None
    """Structured JSON result (if requested)"""

    job_metadata: Optional[Dict[str, object]] = None
    """Job execution metadata (if requested)"""

    markdown: Optional[Markdown] = None
    """Markdown result (if requested)"""

    markdown_full: Optional[str] = None
    """Full raw markdown content (if requested)"""

    metadata: Optional[Metadata] = None
    """Result containing metadata (page level and general) for the parsed document."""

    raw_parameters: Optional[Dict[str, object]] = None

    result_content_metadata: Optional[Dict[str, ResultContentMetadata]] = None
    """Metadata including size, existence, and presigned URLs for result files"""

    text: Optional[Text] = None
    """Plain text result (if requested)"""

    text_full: Optional[str] = None
    """Full raw text content (if requested)"""


from .list_item import ListItem
from .footer_item import FooterItem
from .header_item import HeaderItem
