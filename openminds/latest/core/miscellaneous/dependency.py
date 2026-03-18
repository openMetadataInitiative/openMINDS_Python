"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Dependency(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Dependency"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "failure_impacts",
            "openminds.latest.controlled_terms.DependencyImpact",
            "failureImpact",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the impacts that failure of this dependency would have.",
        ),
        Property(
            "fulfilled_by",
            [
                "openminds.latest.core.Configuration",
                "openminds.latest.core.File",
                "openminds.latest.core.InterfaceVersion",
                "openminds.latest.core.SoftwareVersion",
                "openminds.latest.core.WebResource",
            ],
            "fulfilledBy",
            required=True,
            description="no description available",
            instructions="Enter the resource that fulfils this dependency.",
        ),
    ]

    def __init__(self, failure_impacts=None, fulfilled_by=None):
        return super().__init__(
            failure_impacts=failure_impacts,
            fulfilled_by=fulfilled_by,
        )
