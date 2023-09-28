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
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "data_type",
            "openminds.v3_0.controlled_terms.DataType",
            "vocab:dataType",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all data types that may be represented via this content type.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of the content type specification. Leave blank if an official and public specification is linked under 'specification' for this content type.",
        ),
        Property(
            "display_label",
            str,
            "vocab:displayLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a display label for this content type.",
        ),
        Property(
            "file_extension",
            str,
            "vocab:fileExtension",
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
            "vocab:name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this content type following a IANA.org inspired convention.",
        ),
        Property(
            "related_media_type",
            IRI,
            "vocab:relatedMediaType",
            description="Reference to an official two-part identifier for file formats and format contents.",
            instructions="Enter the internationalized resource identifier (IRI) to the official registered media type (e.g., provided on IANA.org) matching this content type.",
        ),
        Property(
            "specification",
            IRI,
            "vocab:specification",
            description="Detailed and precise presentation of, or proposal for something.",
            instructions="Enter the internationalized resource identifier (IRI) to the offical specification of this content type. If no offical and public specification is available, leave blank and enter the specification under 'description'.",
        ),
        Property(
            "synonym",
            str,
            "vocab:synonym",
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
        data_type=None,
        description=None,
        display_label=None,
        file_extension=None,
        name=None,
        related_media_type=None,
        specification=None,
        synonym=None,
    ):
        return super().__init__(
            id=id,
            data_type=data_type,
            description=description,
            display_label=display_label,
            file_extension=file_extension,
            name=name,
            related_media_type=related_media_type,
            specification=specification,
            synonym=synonym,
        )
