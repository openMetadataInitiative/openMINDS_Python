"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class DeployedInterface(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/DeployedInterface"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "accessibility",
            "openminds.latest.core.Accessibility",
            "accessibility",
            required=True,
            description="Level to which something is accessible to the deployed interface.",
            instructions="Add the accessibility of this deployed interface.",
        ),
        Property(
            "entry_point",
            "openminds.latest.core.WebResource",
            "entryPoint",
            required=True,
            description="no description available",
            instructions="Add the URL that serves as the entry point to this deployed interface.",
        ),
        Property(
            "interface",
            "openminds.latest.core.InterfaceVersion",
            "interface",
            required=True,
            description="no description available",
            instructions="Enter the interface version that is deployed.",
        ),
    ]

    def __init__(self, accessibility=None, entry_point=None, interface=None):
        return super().__init__(
            accessibility=accessibility,
            entry_point=entry_point,
            interface=interface,
        )
