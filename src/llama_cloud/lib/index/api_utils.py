# Index/sheets helpers intentionally use the deprecated v1 pipelines / beta.sheets API;
# migration to the indexes/retrievers + top-level sheets API is tracked separately.
# pyright: reportDeprecated=false
from __future__ import annotations

import uuid
import base64
from typing import Any, Dict, List, Tuple, Optional

from llama_index.core.schema import ImageNode, NodeWithScore
from llama_index.core.async_utils import run_jobs

from llama_cloud import LlamaCloud, AsyncLlamaCloud
from llama_cloud.types import Retriever, PageFigureNodeWithScore, AutoTransformConfigParam, PageScreenshotNodeWithScore
from llama_cloud.types.project import Project
from llama_cloud.types.pipeline import Pipeline


def default_transform_config() -> AutoTransformConfigParam:
    return AutoTransformConfigParam()


def resolve_retriever(
    client: LlamaCloud,
    project: Project,
    retriever_name: Optional[str] = None,
    retriever_id: Optional[str] = None,
    persisted: Optional[bool] = True,
) -> Optional[Retriever]:
    if not persisted:
        return Retriever(
            id=str(uuid.uuid4()),
            project_id=project.id,
            name=retriever_name or f"retriever-{uuid.uuid4()}",
            pipelines=[],
        )
    if retriever_id:
        return client.retrievers.get(retriever_id=retriever_id, project_id=project.id)
    elif retriever_name:
        retrievers = client.retrievers.list(project_id=project.id, name=retriever_name)
        return next(
            (retriever for retriever in retrievers if retriever.name == retriever_name),
            None,
        )
    else:
        return None


def resolve_project(
    client: LlamaCloud,
    project_name: Optional[str],
    project_id: Optional[str],
    organization_id: Optional[str],
) -> Project:
    project: Optional[Project] = None
    if project_id is not None:
        project = client.projects.get(project_id=project_id)
    elif project_name is not None:
        projects = client.projects.list(organization_id=organization_id)
        project = next((p for p in projects if p.name == project_name), None)
        if project is None:
            raise ValueError(f"Project with name '{project_name}' not found.")
    else:
        raise ValueError("Either project_id or project_name must be provided.")

    return project


def resolve_project_and_pipeline(
    client: LlamaCloud,
    name: Optional[str],
    pipeline_id: Optional[str],
    project_name: Optional[str],
    project_id: Optional[str],
    organization_id: Optional[str],
) -> Tuple[Project, Pipeline]:
    project = resolve_project(
        client=client,
        project_name=project_name,
        project_id=project_id,
        organization_id=organization_id,
    )

    pipeline: Optional[Pipeline] = None
    if pipeline_id is not None:
        pipeline = client.pipelines.get(pipeline_id=pipeline_id)
    elif name is not None:
        pipelines = client.pipelines.list(organization_id=organization_id, project_id=project.id, pipeline_name=name)
        pipeline = next((p for p in pipelines if p.name == name), None)
        if pipeline is None:
            raise ValueError(f"Pipeline with name '{name}' not found in project '{project.name}'.")
    else:
        raise ValueError("Either pipeline_id or name must be provided.")

    return project, pipeline


def page_screenshot_nodes_to_node_with_score(
    client: LlamaCloud,
    raw_image_nodes: Optional[List[PageScreenshotNodeWithScore]],
    project_id: str,
    metadata: Optional[Dict[str, Any]] = None,
) -> List[NodeWithScore]:
    if not raw_image_nodes:
        return []

    image_nodes: List[NodeWithScore] = []
    for raw_image_node in raw_image_nodes:
        image_bytes_str = client.pipelines.images.get_page_screenshot(
            page_index=raw_image_node.node.page_index,
            id=raw_image_node.node.file_id,
            project_id=project_id,
        )
        image_base64 = base64.b64encode(str(image_bytes_str).encode("utf-8")).decode("utf-8")
        image_node_metadata: Dict[str, Any] = {
            **(raw_image_node.node.metadata or {}),
            **(metadata or {}),
            "file_id": raw_image_node.node.file_id,
            "page_index": raw_image_node.node.page_index,
        }
        image_node_with_score = NodeWithScore(
            node=ImageNode(image=image_base64, metadata=image_node_metadata),
            score=raw_image_node.score,
        )
        image_nodes.append(image_node_with_score)

    return image_nodes


def image_nodes_to_node_with_score(
    client: LlamaCloud,
    raw_image_nodes: Optional[List[PageScreenshotNodeWithScore]],
    project_id: str,
    metadata: Optional[Dict[str, Any]] = None,
) -> List[NodeWithScore]:
    """
    Legacy method to alias page_screenshot_nodes_to_node_with_score.
    """
    if not raw_image_nodes:
        return []

    return page_screenshot_nodes_to_node_with_score(
        client=client,
        raw_image_nodes=raw_image_nodes,
        project_id=project_id,
        metadata=metadata,
    )


def page_figure_nodes_to_node_with_score(
    client: LlamaCloud,
    raw_figure_nodes: Optional[List[PageFigureNodeWithScore]],
    project_id: str,
    metadata: Optional[Dict[str, Any]] = None,
) -> List[NodeWithScore]:
    if not raw_figure_nodes:
        return []

    figure_nodes: List[NodeWithScore] = []
    for raw_figure_node in raw_figure_nodes:
        figure_bytes_str = client.pipelines.images.get_page_figure(
            page_index=raw_figure_node.node.page_index,
            id=raw_figure_node.node.file_id,
            figure_name=raw_figure_node.node.figure_name,
            project_id=project_id,
        )
        figure_base64 = base64.b64encode(str(figure_bytes_str).encode("utf-8")).decode("utf-8")
        figure_node_metadata: Dict[str, Any] = {
            **(raw_figure_node.node.metadata or {}),
            **(metadata or {}),
            "file_id": raw_figure_node.node.file_id,
            "page_index": raw_figure_node.node.page_index,
            "figure_name": raw_figure_node.node.figure_name,
        }
        figure_node_with_score = NodeWithScore(
            node=ImageNode(image=figure_base64, metadata=figure_node_metadata),
            score=raw_figure_node.score,
        )
        figure_nodes.append(figure_node_with_score)
    return figure_nodes


async def apage_screenshot_nodes_to_node_with_score(
    client: AsyncLlamaCloud,
    raw_image_nodes: Optional[List[PageScreenshotNodeWithScore]],
    project_id: str,
    metadata: Optional[Dict[str, Any]] = None,
) -> List[NodeWithScore]:
    if not raw_image_nodes:
        return []

    async def _get_page_screenshot(
        client: AsyncLlamaCloud,
        file_id: str,
        page_index: int,
        project_id: str,
    ) -> str:
        resp = await client.pipelines.images.with_raw_response.get_page_screenshot(
            page_index=page_index,
            id=file_id,
            project_id=project_id,
        )
        figure_bytes = await resp.read()
        return base64.b64encode(figure_bytes).decode("utf-8")

    image_nodes: List[NodeWithScore] = []
    tasks = [
        _get_page_screenshot(
            client=client,
            file_id=raw_image_node.node.file_id,
            page_index=raw_image_node.node.page_index,
            project_id=project_id,
        )
        for raw_image_node in raw_image_nodes
    ]

    image_bytes_list = await run_jobs(tasks)
    for image_base64, raw_image_node in zip(image_bytes_list, raw_image_nodes):
        image_node_metadata: Dict[str, Any] = {
            **(raw_image_node.node.metadata or {}),
            **(metadata or {}),
            "file_id": raw_image_node.node.file_id,
            "page_index": raw_image_node.node.page_index,
        }
        image_node_with_score = NodeWithScore(
            node=ImageNode(image=image_base64, metadata=image_node_metadata),
            score=raw_image_node.score,
        )
        image_nodes.append(image_node_with_score)
    return image_nodes


async def aimage_nodes_to_node_with_score(
    client: AsyncLlamaCloud,
    raw_image_nodes: Optional[List[PageScreenshotNodeWithScore]],
    project_id: str,
    metadata: Optional[Dict[str, Any]] = None,
) -> List[NodeWithScore]:
    """
    Legacy method to alias apage_screenshot_nodes_to_node_with_score.
    """
    if not raw_image_nodes:
        return []

    return await apage_screenshot_nodes_to_node_with_score(
        client=client,
        raw_image_nodes=raw_image_nodes,
        project_id=project_id,
        metadata=metadata,
    )


async def apage_figure_nodes_to_node_with_score(
    client: AsyncLlamaCloud,
    raw_figure_nodes: Optional[List[PageFigureNodeWithScore]],
    project_id: str,
    metadata: Optional[Dict[str, Any]] = None,
) -> List[NodeWithScore]:
    if not raw_figure_nodes:
        return []

    async def _get_page_figure(
        client: AsyncLlamaCloud,
        file_id: str,
        figure_name: str,
        page_index: int,
        project_id: str,
    ) -> str:
        resp = await client.pipelines.images.with_raw_response.get_page_figure(
            page_index=page_index,
            figure_name=figure_name,
            id=file_id,
            project_id=project_id,
        )
        figure_bytes = await resp.read()
        return base64.b64encode(figure_bytes).decode("utf-8")

    figure_nodes: List[NodeWithScore] = []
    tasks = [
        _get_page_figure(
            client=client,
            file_id=raw_figure_node.node.file_id,
            page_index=raw_figure_node.node.page_index,
            figure_name=raw_figure_node.node.figure_name,
            project_id=project_id,
        )
        for raw_figure_node in raw_figure_nodes
    ]

    figure_bytes_list = await run_jobs(tasks)
    for figure_base64, raw_figure_node in zip(figure_bytes_list, raw_figure_nodes):
        figure_node_metadata: Dict[str, Any] = {
            **(raw_figure_node.node.metadata or {}),
            **(metadata or {}),
            "file_id": raw_figure_node.node.file_id,
            "page_index": raw_figure_node.node.page_index,
            "figure_name": raw_figure_node.node.figure_name,
        }
        figure_node_with_score = NodeWithScore(
            node=ImageNode(image=figure_base64, metadata=figure_node_metadata),
            score=raw_figure_node.score,
        )
        figure_nodes.append(figure_node_with_score)

    return figure_nodes
