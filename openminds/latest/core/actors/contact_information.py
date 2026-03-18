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

    type_ = "https://openminds.om-i.org/types/ContactInformation"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "emails",
            str,
            "email",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            required=True,
            description="Address to which or from which an electronic mail can be sent.",
            instructions="Enter all relevant contact email addresses.",
        ),
    ]

    def __init__(self, id=None, emails=None):
        return super().__init__(
            id=id,
            emails=emails,
        )
