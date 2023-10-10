"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class LivePaperSection(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/publications/LivePaperSection"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of this live paper section.",
        ),
        Property(
            "is_part_of",
            "openminds.v3.publications.LivePaperVersion",
            "isPartOf",
            required=True,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add the live paper version this live paper section is part of.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name (or title) of this live paper section.",
        ),
        Property(
            "order",
            int,
            "order",
            required=True,
            description="no description available",
            instructions="Enter an integer that is used to sort this live paper section in ascending order with other live paper sections of the overarching live paper version.",
        ),
        Property(
            "type",
            str,
            "type",
            formatting="text/plain",
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type of this live paper section (e.g., 'custom', 'generic', 'models', 'morphology', or 'traces').",
        ),
    ]

    def __init__(self, id=None, description=None, is_part_of=None, name=None, order=None, type=None):
        return super().__init__(
            id=id,
            description=description,
            is_part_of=is_part_of,
            name=name,
            order=order,
            type=type,
        )
