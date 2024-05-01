# ********************************************************************************
# *         WARNING: This file is automatically generated by unasync.py.         *
# *                             DO NOT MANUALLY EDIT                             *
# *            Source File: patent_client/_async/epo/ops/legal/api.py            *
# ********************************************************************************

from ..session import asession
from .model import Legal


class LegalApi:
    @classmethod
    def get_legal(cls, doc_number, doc_type="publication", format="docdb"):
        url = f"http://ops.epo.org/3.2/rest-services/legal/{doc_type}/{format}/{doc_number}"
        response = asession.get(url)

        return Legal.model_validate(response.text)