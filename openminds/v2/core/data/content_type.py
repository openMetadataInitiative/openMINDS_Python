"""
Structured information on the content type of a file instance, bundle or repository.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ContentType(LinkedMetadata):
    """
    Structured information on the content type of a file instance, bundle or repository.
    """

    type_ = "https://openminds.ebrains.eu/core/ContentType"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of the content type specification. May be left blank if a public specification can be linked in 'specification'.",
        ),
        Property(
            "file_extensions",
            str,
            "fileExtension",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="String of characters attached as suffix to the names of files of a particular format.",
            instructions="Enter one or several file extensions associated with this content type.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name (iana-inspired convention) of this content type.",
        ),
        Property(
            "related_media_type",
            IRI,
            "relatedMediaType",
            description="Reference to an official two-part identifier for file formats and format contents.",
            instructions="Enter the iternationalized resource identifier (IRI) of the official registered media type (e.g. on IANA.org) matching this content type.",
        ),
        Property(
            "specification",
            IRI,
            "specification",
            description="Detailed and precise presentation of, or proposal for something.",
            instructions="Enter the iternationalized resource identifier (IRI) of the official specification of this content type. Leave blank and use 'description' to provide some specification if an official specification is not available.",
        ),
        Property(
            "synonyms",
            str,
            "synonym",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
            instructions="Enter one or several synonyms of this content type.",
        ),
    ]

    def __init__(
        self,
        id=None,
        description=None,
        file_extensions=None,
        name=None,
        related_media_type=None,
        specification=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            description=description,
            file_extensions=file_extensions,
            name=name,
            related_media_type=related_media_type,
            specification=specification,
            synonyms=synonyms,
        )
