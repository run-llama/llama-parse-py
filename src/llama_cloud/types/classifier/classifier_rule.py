# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ClassifierRule"]


class ClassifierRule(BaseModel):
    """A rule for classifying documents - v0 simplified version.

    This represents a single classification rule that will be applied to documents.
    All rules are content-based and use natural language descriptions.
    """

    description: str
    """Natural language description of what to classify.

    Be specific about the content characteristics that identify this document type.
    """

    type: str
    """
    The document type to assign when this rule matches (e.g., 'invoice', 'receipt',
    'contract')
    """
