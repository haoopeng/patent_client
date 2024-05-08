# ********************************************************************************
# *         WARNING: This file is automatically generated by unasync.py.         *
# *                             DO NOT MANUALLY EDIT                             *
# *         Source File: patent_client/_async/uspto/odp/manager_test.py          *
# ********************************************************************************

from .model import USApplication, USApplicationBiblio


def test_all_apps():
    assert USApplication.objects.filter(query=dict()).count() > 1000


def test_get_one_app():
    app = USApplication.objects.get(q="applicationNumberText:16123456")
    assert app is not None
    assert app.appl_id == "16123456"


def test_get_app_from_search_result():
    application = USApplication.objects.get(q="applicationNumberText:16123456")
    assert application.appl_id == "16123456"


def test_get_app_biblio_from_search_result():
    result = USApplicationBiblio.objects.get(q="applicationNumberText:16123456")
    biblio = result.biblio
    assert biblio.appl_id == "16123456"


def test_get_continuity_from_search_result():
    result = USApplicationBiblio.objects.get(q="applicationNumberText:16123456")
    continuity = result.continuity
    assert len(continuity.child_continuity) > 0


def test_get_documents_from_search_result():
    result = USApplicationBiblio.objects.get(q="applicationNumberText:16123456")
    documents = result.documents
    assert documents.count() > 0


def test_simple_keyword_searches():
    result = USApplication.objects.get("16123456")
    assert result.appl_id == "16123456"


def test_combination_search():
    result = USApplication.objects.filter(
        invention_title="Hair Dryer", filing_date_gte="2020-01-01"
    )
    assert result.count() > 5


def test_can_get_old_applications():
    result = USApplication.objects.get("14230558")
    assert result.appl_id == "14230558"
    result = USApplicationBiblio.objects.get("14230558")
    assert result.appl_id == "14230558"


def test_can_get_pct_application():
    result = USApplication.objects.get("PCT/US07/19317")
    assert result.appl_id == "PCT/US07/19317"
