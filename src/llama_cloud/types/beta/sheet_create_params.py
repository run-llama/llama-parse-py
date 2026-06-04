# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .sheets_parsing_config_param import SheetsParsingConfigParam

__all__ = ["SheetCreateParams", "WebhookConfiguration"]


class SheetCreateParams(TypedDict, total=False):
    file_id: Required[str]
    """The ID of the file to parse"""

    organization_id: Optional[str]

    project_id: Optional[str]

    config: Optional[SheetsParsingConfigParam]
    """Configuration for spreadsheet parsing and region extraction"""

    configuration: Optional[SheetsParsingConfigParam]
    """Configuration for spreadsheet parsing and region extraction"""

    configuration_id: Optional[str]
    """Saved configuration ID"""

    webhook_configurations: Optional[Iterable[WebhookConfiguration]]
    """Outbound webhook endpoints to notify on job status changes"""


class WebhookConfiguration(TypedDict, total=False):
    """Configuration for a single outbound webhook endpoint."""

    webhook_events: Optional[
        List[
            Literal[
                "extract.pending",
                "extract.success",
                "extract.error",
                "extract.partial_success",
                "extract.cancelled",
                "parse.pending",
                "parse.running",
                "parse.success",
                "parse.error",
                "parse.partial_success",
                "parse.cancelled",
                "classify.pending",
                "classify.running",
                "classify.success",
                "classify.error",
                "classify.partial_success",
                "classify.cancelled",
                "sheets.pending",
                "sheets.success",
                "sheets.error",
                "sheets.partial_success",
                "sheets.cancelled",
                "unmapped_event",
            ]
        ]
    ]
    """Events to subscribe to (e.g.

    'parse.success', 'extract.error'). If null, all events are delivered.
    """

    webhook_headers: Optional[Dict[str, str]]
    """Custom HTTP headers sent with each webhook request (e.g. auth tokens)"""

    webhook_output_format: Optional[str]
    """Response format sent to the webhook: 'string' (default) or 'json'"""

    webhook_url: Optional[str]
    """URL to receive webhook POST notifications"""
