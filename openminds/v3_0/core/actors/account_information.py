"""
Structured information about a user account for a web service.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class AccountInformation(LinkedMetadata):
    """
    Structured information about a user account for a web service.
    """

    type_ = "https://openminds.ebrains.eu/core/AccountInformation"
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "service",
            "openminds.v3_0.core.WebService",
            "vocab:service",
            required=True,
            description="no description available",
            instructions="Add the web service of this account.",
        ),
        Property(
            "user_name",
            str,
            "vocab:userName",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the user name for this account.",
        ),
    ]

    def __init__(self, id=None, service=None, user_name=None):
        return super().__init__(
            id=id,
            service=service,
            user_name=user_name,
        )
