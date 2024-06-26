# ********************************************************************************
# *         WARNING: This file is automatically generated by unasync.py.         *
# *                             DO NOT MANUALLY EDIT                             *
# *   Source File: patent_client/_async/uspto/public_search/model/__init__.py    *
# ********************************************************************************

from .biblio import PublicSearchBiblio, PublicSearchBiblioPage
from .document import PublicSearchDocument


class PatentBiblio(PublicSearchBiblio):
    pass


class Patent(PublicSearchDocument):
    pass


class PublishedApplicationBiblio(PublicSearchBiblio):
    pass


class PublishedApplication(PublicSearchDocument):
    pass


__all__ = [
    "PatentBiblio",
    "Patent",
    "PublishedApplicationBiblio",
    "PublishedApplication",
    "PublicSearchBiblio",
    "PublicSearchBiblioPage",
    "PublicSearchDocument",
    "PublicSearchDocument",
]
