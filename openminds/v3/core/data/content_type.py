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
    schema_version = "v3.0"

    properties = [
        Property(
            "data_types",
            "openminds.v3.controlled_terms.DataType",
            "dataType",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all data types that may be represented via this content type.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of the content type specification. Leave blank if an official and public specification is linked under 'specification' for this content type.",
        ),
        Property(
            "display_label",
            str,
            "displayLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a display label for this content type.",
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
            instructions="Enter all file extensions associated with this content type.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this content type following a IANA.org inspired convention.",
        ),
        Property(
            "related_media_type",
            IRI,
            "relatedMediaType",
            description="Reference to an official two-part identifier for file formats and format contents.",
            instructions="Enter the internationalized resource identifier (IRI) to the official registered media type (e.g., provided on IANA.org) matching this content type.",
        ),
        Property(
            "specification",
            IRI,
            "specification",
            description="Detailed and precise presentation of, or proposal for something.",
            instructions="Enter the internationalized resource identifier (IRI) to the offical specification of this content type. If no offical and public specification is available, leave blank and enter the specification under 'description'.",
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
            instructions="Enter any synonyms of this content type.",
        ),
    ]

    def __init__(
        self,
        id=None,
        data_types=None,
        description=None,
        display_label=None,
        file_extensions=None,
        name=None,
        related_media_type=None,
        specification=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            data_types=data_types,
            description=description,
            display_label=display_label,
            file_extensions=file_extensions,
            name=name,
            related_media_type=related_media_type,
            specification=specification,
            synonyms=synonyms,
        )
