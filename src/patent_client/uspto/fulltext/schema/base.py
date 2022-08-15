import lxml.html as ETH
from yankee.xml import fields as f
from patent_client.util.xml import Schema as BaseSchema, RegexSchema, ZipSchema

class Schema(BaseSchema):
    def pre_load(self, obj):
        if isinstance(obj, str):
            obj = obj.encode("utf-8")
        
        if isinstance(obj, bytes):
            return ETH.fromstring(obj)
        else:
            return obj
