# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    """Schema for a file."""

    id: str
    """Unique identifier"""

    name: str

    project_id: str
    """The ID of the project that the file belongs to"""

    created_at: Optional[datetime] = None
    """Creation datetime"""

    data_source_id: Optional[str] = None
    """The ID of the data source that the file belongs to"""

    expires_at: Optional[datetime] = None
    """The expiration date for the file. Files past this date can be deleted."""

    external_file_id: Optional[str] = None
    """The ID of the file in the external system"""

    file_size: Optional[int] = None
    """Size of the file in bytes"""

    file_type: Optional[str] = None
    """File type (e.g. pdf, docx, etc.)"""

    last_modified_at: Optional[datetime] = None
    """The last modified time of the file"""

    permission_info: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """Permission information for the file"""

    purpose: Optional[str] = None
    """
    The intended purpose of the file (e.g., 'user_data', 'parse', 'extract',
    'split', 'classify')
    """

    resource_info: Optional[Dict[str, Union[Dict[str, object], List[object], str, float, bool, None]]] = None
    """Resource information for the file"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
