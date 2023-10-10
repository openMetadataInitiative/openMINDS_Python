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
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "service",
            "openminds.latest.core.WebService",
            "service",
            required=True,
            description="no description available",
            instructions="Add the web service of this account.",
        ),
        Property(
            "user_name",
            str,
            "userName",
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
