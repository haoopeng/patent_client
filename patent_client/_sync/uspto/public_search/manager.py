# ********************************************************************************
# *         WARNING: This file is automatically generated by unasync.py.         *
# *                             DO NOT MANUALLY EDIT                             *
# *       Source File: patent_client/_async/uspto/public_search/manager.py       *
# ********************************************************************************

from typing import Generic, Iterator, TypeVar

from patent_client.util.manager import Manager
from patent_client.util.request_util import get_start_and_row_count

from .api import PublicSearchApi
from .model import (
    Patent,
    PatentBiblio,
    PublicSearchBiblio,
    PublicSearchDocument,
    PublishedApplication,
    PublishedApplicationBiblio,
)
from .query import QueryBuilder


class CapacityException(Exception):
    pass


class FinishedException(Exception):
    pass


T = TypeVar("T")
public_search_api = PublicSearchApi()


class GenericPublicSearchManager(Manager, Generic[T]):
    page_size = 500
    default_filter = "patent_number"
    query_builder = QueryBuilder()

    @property
    def _query(self):
        return self.query_builder.build_query(self.config)

    @property
    def _order_by(self):
        return self.query_builder.build_order_by(self.config)

    @property
    def query_fields(self):
        return self.query_builder.search_keywords

    @property
    def order_by_fields(self):
        return self.query_builder.order_by_keywords

    def count(self):
        query = self._query
        order_by = self._order_by
        sources = self.config.options.get("sources", ["US-PGPUB", "USPAT", "USOCR"])
        page = public_search_api.run_query(
            query=query, start=0, limit=self.page_size, sort=order_by, sources=sources
        )
        max_len = page.num_found - self.config.offset
        return min(self.config.limit, max_len) if self.config.limit else max_len


class GenericPublicSearchBiblioManager(GenericPublicSearchManager, Generic[T]):
    def _get_results(self) -> Iterator[T]:
        query = self._query
        order_by = self._order_by
        sources = self.config.options.get("sources", ["US-PGPUB", "USPAT", "USOCR"])
        for start, rows in get_start_and_row_count(
            self.config.limit, self.config.offset, self.page_size
        ):
            page = public_search_api.run_query(
                query=query,
                start=start,
                limit=rows,
                sort=order_by,
                sources=sources,
            )
            for obj in page.docs:
                yield obj
            if len(page.docs) < rows:
                break


capacity_limit = 501


class GenericPublicSearchDocumentManager(GenericPublicSearchBiblioManager, Generic[T]):
    def _get_results(self) -> Iterator["PublicSearchDocument"]:
        result_count = super().count()
        if result_count > capacity_limit:
            raise CapacityException(
                f"Query would result in more than 501 results! ({result_count} > 20).\nPlease use the associated Biblio method to reduce load on the API (PublicSearch / PatentBiblio / PublishedApplicationBiblio"
            )
        for obj in super()._get_results():
            doc = public_search_api.get_document(obj)
            yield doc


class PublicSearchBiblioManager(GenericPublicSearchBiblioManager[PublicSearchBiblio]):
    pass


class PublicSearchDocumentManager(GenericPublicSearchDocumentManager[PublicSearchDocument]):
    pass


class PatentBiblioManager(GenericPublicSearchBiblioManager[PatentBiblio]):
    def __init__(self, config=None):
        super().__init__(config=config)
        self.config.options["sources"] = [
            "USPAT",
        ]


class PatentManager(GenericPublicSearchDocumentManager[Patent]):
    def __init__(self, config=None):
        super().__init__(config=config)
        self.config.options["sources"] = [
            "USPAT",
        ]


class PublishedApplicationBiblioManager(
    GenericPublicSearchBiblioManager[PublishedApplicationBiblio]
):
    def __init__(self, config=None):
        super().__init__(config=config)
        self.config.options["sources"] = [
            "US-PGPUB",
        ]


class PublishedApplicationManager(GenericPublicSearchDocumentManager[PublishedApplication]):
    def __init__(self, config=None):
        super().__init__(config=config)
        self.config.options["sources"] = [
            "US-PGPUB",
        ]
