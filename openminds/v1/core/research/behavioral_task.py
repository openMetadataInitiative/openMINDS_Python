"""
Structured information on the behavioral task that had to be performed by a subject.
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class BehavioralTask(LinkedMetadata):
    """
    Structured information on the behavioral task that had to be performed by a subject.
    """

    type_ = "https://openminds.ebrains.eu/core/BehavioralTask"
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
            description="Longer statement or account giving the characteristics of the behavioral task.",
            instructions="Enter a description of this behavioral task.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of the behavioral task.",
            instructions="Enter a descriptive full name for this behavioral task.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            description="Shortened or fully abbreviated name of the behavioral task.",
            instructions="Enter a short name (alias) for this behavioral task.",
        ),
    ]

    def __init__(self, id=None, description=None, full_name=None, short_name=None):
        return super().__init__(
            id=id,
            description=description,
            full_name=full_name,
            short_name=short_name,
        )
