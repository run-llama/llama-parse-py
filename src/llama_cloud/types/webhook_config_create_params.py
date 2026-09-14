# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookConfigCreateParams"]


class WebhookConfigCreateParams(TypedDict, total=False):
    webhook_url: Required[str]
    """URL to receive webhook POST notifications."""

    organization_id: Optional[str]

    project_id: Optional[str]

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
    """Events to subscribe to. If null, all events are delivered."""

    webhook_headers: Optional[Dict[str, str]]
    """Custom HTTP headers sent with each webhook request."""

    webhook_output_format: Optional[Literal["json", "string"]]
    """Response format sent to the webhook: 'string' (default) or 'json'."""

    webhook_signing_secret: Optional[str]
    """Shared secret used to sign deliveries to this endpoint.

    Write-only: it is never returned in responses.
    """
