"""
Structured information on the content type of a file instance, bundle or repository.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ContentType(LinkedMetadata):
    """
    Structured information on the content type of a file instance, bundle or repository.
    """

    type_ = "https://openminds.ebrains.eu/core/ContentType"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "associated_file_extension",
            str,
            "associatedFileExtension",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter one or several file extensions associated with this content type.",
        ),
        Property(
            "category",
            str,
            "category",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the category to which this content type belongs to.",
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
            str,
            "relatedMediaType",
            formatting="text/plain",
            description="Reference to an official two-part identifier for file formats and format contents.",
            instructions="Enter the iternationalized resource identifier (IRI) to a registered media type (e.g. on IANA.org) matching this content type.",
        ),
        Property(
            "synonym",
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
        self, id=None, associated_file_extension=None, category=None, name=None, related_media_type=None, synonym=None
    ):
        return super().__init__(
            id=id,
            associated_file_extension=associated_file_extension,
            category=category,
            name=name,
            related_media_type=related_media_type,
            synonym=synonym,
        )