# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .shared_params.cloud_milvus_vector_store import CloudMilvusVectorStore
from .shared_params.cloud_qdrant_vector_store import CloudQdrantVectorStore
from .shared_params.cloud_astra_db_vector_store import CloudAstraDBVectorStore
from .shared_params.cloud_pinecone_vector_store import CloudPineconeVectorStore
from .shared_params.cloud_postgres_vector_store import CloudPostgresVectorStore
from .shared_params.cloud_mongodb_atlas_vector_search import CloudMongoDBAtlasVectorSearch
from .shared_params.cloud_azure_ai_search_vector_store import CloudAzureAISearchVectorStore

__all__ = ["DataSinkCreateParams", "Component"]


class DataSinkCreateParams(TypedDict, total=False):
    component: Required[Component]
    """Component that implements the data sink"""

    name: Required[str]
    """The name of the data sink."""

    sink_type: Required[
        Literal["ASTRA_DB", "AZUREAI_SEARCH", "MILVUS", "MONGODB_ATLAS", "PINECONE", "POSTGRES", "QDRANT"]
    ]

    organization_id: Optional[str]

    project_id: Optional[str]


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
