# ********************************************************************************
# *         WARNING: This file is automatically generated by unasync.py.         *
# *                             DO NOT MANUALLY EDIT                             *
# *     Source File: patent_client/_async/epo/ops/published/manager_test.py      *
# ********************************************************************************

import pytest

from .model.search import Inpadoc


class TestPublished:
    
    def test_inpadoc_manager(self):
        result = Inpadoc.objects.filter(applicant="Microsoft")
        assert result.count() > 20
        countries = [
            c for c in result.limit(20).values_list("country", flat=True)
        ]
        assert sum(1 for c in countries if c == "US") >= 1

    
    def test_get_biblio_from_result(self):
        doc = Inpadoc.objects.filter(applicant="Google").first()
        result = doc.biblio
        assert len(result.titles) > 0

    
    def test_get_claims_from_result(self):
        result = Inpadoc.objects.get("WO2009085664A2")
        claims = result.claims
        assert len(claims.claims) == 20
        assert len(claims.claim_text) == 4830

    
    def test_get_description_from_result(self):
        result = Inpadoc.objects.get("WO2009085664A2")
        description = result.description
        assert len(description) == 47955

    
    def test_get_family_from_result(self):
        result = Inpadoc.objects.get("WO2009085664A2")
        family = result.family
        assert len(family) >= 20

    
    def test_get_biblio_from_wo(self):
        result = Inpadoc.objects.get("WO2009085664A2")
        biblio = result.biblio
        assert biblio.abstract is not None

    
    def test_can_index_inpadoc_result(self):
        result = Inpadoc.objects.filter(applicant="Tesla")
        first = result.first()
        second = result.offset(1).first()
        assert first != second

    
    def test_can_handle_single_item_ipc_classes(self):
        result = Inpadoc.objects.get("WO2020081771")
        biblio = result.biblio
        assert biblio.intl_class is not None

    
    def test_issue_41(self):
        result = Inpadoc.objects.get("JP2005533465A")
        biblio = result.biblio
        assert biblio.title is None