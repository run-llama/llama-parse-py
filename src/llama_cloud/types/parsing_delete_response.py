# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["ParsingDeleteResponse"]


class ParsingDeleteResponse(BaseModel):
    """Confirmation that a parse job was deleted.

    A deleted job can no longer be fetched, so the response echoes back what it
    was rather than pointing at it. Returning the identifiers instead of an
    empty body lets a caller assert on the delete it just made without a
    follow-up request.
    """

    id: str
    """Identifier of the deleted parse job"""

    project_id: str
    """Project the deleted job belonged to"""
