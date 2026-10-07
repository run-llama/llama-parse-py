# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ClassifyDeleteResponse"]


class ClassifyDeleteResponse(BaseModel):
    """Identifiers for a deleted classify job."""

    id: str
    """Identifier of the deleted classify job"""

    project_id: Optional[str] = None
    """Project the deleted job belonged to"""
