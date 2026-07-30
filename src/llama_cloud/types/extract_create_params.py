# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr
from .extract_configuration_param import ExtractConfigurationParam

__all__ = ["ExtractCreateParams", "WebhookConfiguration"]


class ExtractCreateParams(TypedDict, total=False):
    file_input: Required[str]
    """File ID or parse job ID to extract from"""

    organization_id: Optional[str]

    project_id: Optional[str]

    configuration: Optional[ExtractConfigurationParam]
    """Extract configuration combining parse and extract settings."""

    configuration_id: Optional[str]
    """Saved configuration ID"""

    webhook_configuration_ids: Optional[SequenceNotStr[str]]
    """IDs of saved webhook configurations to notify for this job."""

    webhook_configurations: Optional[Iterable[WebhookConfiguration]]
    """Outbound webhook endpoints to notify on job status changes"""


class WebhookConfiguration(TypedDict, total=False):
    """Configuration for a single outbound webhook endpoint."""

    webhook_events: Optional[
        List[
            Literal[
                "batch.cancelled",
                "batch.error",
                "batch.pending",
                "batch.running",
                "batch.success",
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
    ]
    """Events to subscribe to (e.g.

    'parse.success', 'extract.error'). If null, all events are delivered.
    """

    webhook_headers: Optional[Dict[str, str]]
    """Custom HTTP headers sent with each webhook request (e.g. auth tokens)"""

    webhook_output_format: Optional[str]
    """Response format sent to the webhook: 'string' (default) or 'json'"""

    webhook_signing_secret: Optional[str]
    """Shared signing secret used to sign webhook deliveries.

    When set, each request includes an HMAC-SHA256 signature of the request body in
    the 'LC-Signature' header (value 'sha256=<hex>'). Recompute the HMAC over the
    raw request body with this secret to verify the delivery is authentic.
    """

    webhook_url: Optional[str]
    """URL to receive webhook POST notifications"""
