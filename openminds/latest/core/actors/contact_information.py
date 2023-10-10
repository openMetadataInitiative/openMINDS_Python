"""
Structured information about how to contact a given person or consortium.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ContactInformation(LinkedMetadata):
    """
    Structured information about how to contact a given person or consortium.
    """

    type_ = "https://openminds.ebrains.eu/core/ContactInformation"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "email",
            str,
            "email",
            formatting="text/plain",
            required=True,
            description="Address to which or from which an electronic mail can be sent.",
            instructions="Enter the email address of the party (e.g., of the person).",
        ),
    ]

    def __init__(self, id=None, email=None):
        return super().__init__(
            id=id,
            email=email,
        )
