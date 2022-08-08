from yankee.xml import Schema, RegexSchema, fields as f
from ..schema.image_schema import ImageSchema
from ..schema.new_schema import PublicationSchema
from .model import PublishedApplication
from .model import PublishedApplicationImage


class PublishedApplicationSchema(PublicationSchema):
    __model__ = PublishedApplication


class PublishedApplicationImageSchema(ImageSchema):
    __model__ = PublishedApplicationImage

class PublishedApplicationResultSchema(Schema):
    seq = f.Int(".//td[1]")
    publication_number = f.Str('.//td[2]', formatter=lambda s: s.replace(",", ""))
    title = f.Str(".//td[3]")

class ResultMetaSchema(RegexSchema):
    __regex__ = r"Hits (?P<start>\d+) through (?P<end>\d+) out of (?P<num_results>\d+)"
    start = f.Int(".//start")
    end = f.Int(".//end")
    num_results = f.Int(".//num_results")

class PublishedApplicationResultPageSchema(Schema):
    query = f.Str('.//input[@title="query"]/@value')
    result = ResultMetaSchema(
        '(.//i)[2]', 
        flatten=True)
    results = f.List(PublishedApplicationResultSchema, "(.//table//tr)[position()>1]")
    
