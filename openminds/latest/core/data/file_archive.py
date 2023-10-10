"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class FileArchive(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/FileArchive"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "iri",
            IRI,
            "IRI",
            required=True,
            description="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
            instructions="Enter the internationalized resource identifier (IRI) to this file archive.",
        ),
        Property(
            "format",
            "openminds.latest.core.ContentType",
            "format",
            required=True,
            description="Method of digitally organizing and structuring data or information.",
            instructions="Add the content type of this file archive.",
        ),
        Property(
            "source_data",
            "openminds.latest.core.File",
            "sourceData",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the data that were ingested and modified to create this file archive.",
        ),
    ]

    def __init__(self, id=None, iri=None, format=None, source_data=None):
        return super().__init__(
            id=id,
            iri=iri,
            format=format,
            source_data=source_data,
        )
