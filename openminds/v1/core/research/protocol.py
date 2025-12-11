"""
Structured information on a research project.
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Protocol(LinkedMetadata):
    """
    Structured information on a research project.
    """

    type_ = "https://openminds.ebrains.eu/core/Protocol"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of the protocol.",
            instructions="Enter a description of this protocol.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the protocol.",
            instructions="Enter a descriptive name for this protocol.",
        ),
        Property(
            "study_options",
            [],
            "studyOption",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all study options this protocol offers.",
        ),
        Property(
            "techniques",
            "openminds.v1.controlled_terms.Technique",
            "technique",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Method of accomplishing a desired aim.",
            instructions="Add all techniques that were used in this protocol.",
        ),
    ]

    def __init__(self, id=None, description=None, name=None, study_options=None, techniques=None):
        return super().__init__(
            id=id,
            description=description,
            name=name,
            study_options=study_options,
            techniques=techniques,
        )
