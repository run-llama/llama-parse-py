# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookConfigResponse"]


class WebhookConfigResponse(BaseModel):
    """A stored webhook configuration. The signing secret is never included."""

    id: str
    """Unique identifier for the webhook configuration."""

    has_secret: bool
    """Whether a signing secret is configured for this endpoint."""

    tenant_id: str
    """Owner tenant ID."""

    tenant_type: Literal["project"]
    """Owner tenant type."""

    webhook_url: str
    """URL that receives webhook POST notifications."""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    updated_at: Optional[datetime] = None
    """Update datetime"""

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
    ] = None
    """Subscribed events (null = all events)."""

    webhook_headers: Optional[Dict[str, str]] = None
    """Custom HTTP headers sent with each request."""

    webhook_output_format: Optional[Literal["json", "string"]] = None
    """Response format sent to the webhook."""
