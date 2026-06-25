# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .shared.cloud_milvus_vector_store import CloudMilvusVectorStore
from .shared.cloud_qdrant_vector_store import CloudQdrantVectorStore
from .shared.cloud_astra_db_vector_store import CloudAstraDBVectorStore
from .shared.cloud_pinecone_vector_store import CloudPineconeVectorStore
from .shared.cloud_postgres_vector_store import CloudPostgresVectorStore
from .shared.cloud_mongodb_atlas_vector_search import CloudMongoDBAtlasVectorSearch
from .shared.cloud_azure_ai_search_vector_store import CloudAzureAISearchVectorStore

__all__ = ["DataSink", "Component"]

Component: TypeAlias = Union[
    Dict[str, object],
    CloudPineconeVectorStore,
    CloudPostgresVectorStore,
    CloudQdrantVectorStore,
    CloudAzureAISearchVectorStore,
    CloudMongoDBAtlasVectorSearch,
    CloudMilvusVectorStore,
    CloudAstraDBVectorStore,
]


class DataSink(BaseModel):
    """Schema for a data sink."""

    id: str
    """Unique identifier"""

    component: Component
    """Component that implements the data sink"""

    name: str
    """The name of the data sink."""

    project_id: str

    sink_type: Literal["ASTRA_DB", "AZUREAI_SEARCH", "MILVUS", "MONGODB_ATLAS", "PINECONE", "POSTGRES", "QDRANT"]

    created_at: Optional[datetime] = None
    """Creation datetime"""

    updated_at: Optional[datetime] = None
    """Update datetime"""
