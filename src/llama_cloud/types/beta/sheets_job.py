# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from ..file import File
from ..._models import BaseModel
from .sheets_parsing_config import SheetsParsingConfig

__all__ = ["SheetsJob", "Parameters", "ParametersWebhookConfiguration", "Region", "WorksheetMetadata"]


class ParametersWebhookConfiguration(BaseModel):
    """Configuration for a single outbound webhook endpoint."""

    webhook_events: Optional[
        List[
            Literal[
                "classify.cancelled",
                "classify.error",
                "classify.partial_success",
                "classify.pending",
                "classify.running",
                "classify.success",
                "extract.cancelled",
                "extract.error",
                "extract.partial_success",
                "extract.pending",
                "extract.success",
                "parse.cancelled",
                "parse.error",
                "parse.partial_success",
                "parse.pending",
                "parse.running",
                "parse.success",
                "sheets.cancelled",
                "sheets.error",
                "sheets.partial_success",
                "sheets.pending",
                "sheets.success",
                "split.cancelled",
                "split.error",
                "split.pending",
                "split.processing",
                "split.success",
                "unmapped_event",
            ]
        ]
    ] = None
    """Events to subscribe to (e.g.

    'parse.success', 'extract.error'). If null, all events are delivered.
    """

    webhook_headers: Optional[Dict[str, str]] = None
    """Custom HTTP headers sent with each webhook request (e.g. auth tokens)"""

    webhook_output_format: Optional[str] = None
    """Response format sent to the webhook: 'string' (default) or 'json'"""

    webhook_signing_secret: Optional[str] = None
    """Shared signing secret used to sign webhook deliveries.

    When set, each request includes an HMAC-SHA256 signature of the request body in
    the 'LC-Signature' header (value 'sha256=<hex>'). Recompute the HMAC over the
    raw request body with this secret to verify the delivery is authentic.
    """

    webhook_url: Optional[str] = None
    """URL to receive webhook POST notifications"""


class Parameters(BaseModel):
    """Job-time parameters such as webhook configurations."""

    webhook_configurations: Optional[List[ParametersWebhookConfiguration]] = None
    """Webhook configurations for job status notifications."""


class Region(BaseModel):
    """A summary of a single extracted region from a spreadsheet"""

    location: str
    """Location of the region in the spreadsheet"""

    region_type: str
    """Type of the extracted region"""

    sheet_name: str
    """Worksheet name where region was found"""

    description: Optional[str] = None
    """Generated description for the region"""

    region_id: Optional[str] = None
    """Unique identifier for this region within the file"""

    title: Optional[str] = None
    """Generated title for the region"""


class WorksheetMetadata(BaseModel):
    """Metadata about a worksheet in a spreadsheet"""

    sheet_name: str
    """Name of the worksheet"""

    description: Optional[str] = None
    """Generated description of the worksheet"""

    title: Optional[str] = None
    """Generated title for the worksheet"""


class SheetsJob(BaseModel):
    """A spreadsheet parsing job."""

    id: str
    """The ID of the job"""

    configuration: SheetsParsingConfig
    """
    Configuration applied to the parsing job (inline or resolved from a saved
    preset).
    """

    created_at: str
    """When the job was created"""

    file_id: Optional[str] = None
    """The ID of the input file"""

    project_id: str
    """The ID of the project"""

    status: Literal["CANCELLED", "ERROR", "PARTIAL_SUCCESS", "PENDING", "SUCCESS"]
    """The status of the parsing job"""

    updated_at: str
    """When the job was last updated"""

    user_id: str
    """The ID of the user"""

    config: Optional[SheetsParsingConfig] = None
    """Configuration for spreadsheet parsing and region extraction"""

    configuration_id: Optional[str] = None
    """The saved product configuration ID used at create time, if any."""

    errors: Optional[List[str]] = None
    """Any errors encountered"""

    file: Optional[File] = None
    """Schema for a file."""

    metadata_state_transitions: Optional[Dict[str, object]] = None
    """Per-status entry timestamps.

    Returned only when requested via `?expand=metadata_state_transitions`.
    """

    parameters: Optional[Parameters] = None
    """Job-time parameters such as webhook configurations."""

    regions: Optional[List[Region]] = None
    """All extracted regions (populated when job is complete)"""

    success: Optional[bool] = None
    """Whether the job completed successfully"""

    worksheet_metadata: Optional[List[WorksheetMetadata]] = None
    """Metadata for each processed worksheet (populated when job is complete)"""
