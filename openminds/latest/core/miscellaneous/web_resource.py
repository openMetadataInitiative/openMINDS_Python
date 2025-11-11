"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class WebResource(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/WebResource"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "content_description",
            str,
            "contentDescription",
            formatting="text/plain",
            multiline=True,
            description="no description available",
            instructions="Enter a short content description for this web resource.",
        ),
        Property(
            "format",
            "openminds.latest.core.ContentType",
            "format",
            description="Method of digitally organizing and structuring data or information.",
            instructions="Add the expected content type of the document at this web resource.",
        ),
        Property(
            "iri",
            IRI,
            "IRI",
            required=True,
            description="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
            instructions="Enter the internationalized resource identifier (IRI) to this web resource.",
        ),
    ]

    def __init__(self, id=None, content_description=None, format=None, iri=None):
        return super().__init__(
            id=id,
            content_description=content_description,
            format=format,
            iri=iri,
        )
