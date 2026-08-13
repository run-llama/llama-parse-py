# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = [
    "SyncPaginatedJobsHistory",
    "AsyncPaginatedJobsHistory",
    "SyncPaginatedPipelineFiles",
    "AsyncPaginatedPipelineFiles",
    "SyncPaginatedBatchItems",
    "AsyncPaginatedBatchItems",
    "SyncPaginatedCloudDocuments",
    "AsyncPaginatedCloudDocuments",
    "SyncPaginatedQuotaConfigurations",
    "AsyncPaginatedQuotaConfigurations",
    "SyncPaginatedCursor",
    "AsyncPaginatedCursor",
    "SyncPaginatedCursorPost",
    "AsyncPaginatedCursorPost",
]

_T = TypeVar("_T")


class SyncPaginatedJobsHistory(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    jobs: List[_T]
    total_count: Optional[int] = None
    offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        jobs = self.jobs
        if not jobs:
            return []
        return jobs

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncPaginatedJobsHistory(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    jobs: List[_T]
    total_count: Optional[int] = None
    offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        jobs = self.jobs
        if not jobs:
            return []
        return jobs

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncPaginatedPipelineFiles(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    files: List[_T]
    total_count: Optional[int] = None
    offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        files = self.files
        if not files:
            return []
        return files

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncPaginatedPipelineFiles(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    files: List[_T]
    total_count: Optional[int] = None
    offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        files = self.files
        if not files:
            return []
        return files

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"offset": current_count})

        return None


class SyncPaginatedBatchItems(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    total_size: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_size = self.total_size
        if total_size is None:
            return None

        if current_count < total_size:
            return PageInfo(params={"offset": current_count})

        return None


class AsyncPaginatedBatchItems(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    total_size: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self._options.params.get("offset") or 0
        if not isinstance(offset, int):
            raise ValueError(f'Expected "offset" param to be an integer but got {offset}')

        length = len(self._get_page_items())
        current_count = offset + length

        total_size = self.total_size
        if total_size is None:
            return None

        if current_count < total_size:
            return PageInfo(params={"offset": current_count})

        return None


class SyncPaginatedCloudDocuments(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    documents: List[_T]
    total_count: Optional[int] = None
    offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        documents = self.documents
        if not documents:
            return []
        return documents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"skip": current_count})

        return None


class AsyncPaginatedCloudDocuments(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    documents: List[_T]
    total_count: Optional[int] = None
    offset: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        documents = self.documents
        if not documents:
            return []
        return documents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        offset = self.offset
        if offset is None:
            return None  # type: ignore[unreachable]

        length = len(self._get_page_items())
        current_count = offset + length

        total_count = self.total_count
        if total_count is None:
            return None

        if current_count < total_count:
            return PageInfo(params={"skip": current_count})

        return None


class SyncPaginatedQuotaConfigurations(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    page: Optional[int] = None
    pages: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        total_pages = self.pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class AsyncPaginatedQuotaConfigurations(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    page: Optional[int] = None
    pages: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if current_page is None:
            current_page = 1

        total_pages = self.pages
        if total_pages is not None and current_page >= total_pages:
            return None

        return PageInfo(params={"page": current_page + 1})


class SyncPaginatedCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_page_token: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page_token = self.next_page_token
        if not next_page_token:
            return None

        return PageInfo(params={"page_token": next_page_token})


class AsyncPaginatedCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_page_token: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page_token = self.next_page_token
        if not next_page_token:
            return None

        return PageInfo(params={"page_token": next_page_token})


class SyncPaginatedCursorPost(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_page_token: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page_token = self.next_page_token
        if not next_page_token:
            return None

        return PageInfo(json={"page_token": next_page_token})


class AsyncPaginatedCursorPost(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    items: List[_T]
    next_page_token: Optional[str] = None

    @override
    def _get_page_items(self) -> List[_T]:
        items = self.items
        if not items:
            return []
        return items

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_page_token = self.next_page_token
        if not next_page_token:
            return None

        return PageInfo(json={"page_token": next_page_token})
