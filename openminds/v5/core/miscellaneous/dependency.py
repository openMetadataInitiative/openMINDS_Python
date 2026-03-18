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
    schema_version = "v5.0"

    properties = [
        Property(
            "failure_impacts",
            "openminds.v5.controlled_terms.DependencyImpact",
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
                "openminds.v5.core.Configuration",
                "openminds.v5.core.File",
                "openminds.v5.core.InterfaceVersion",
                "openminds.v5.core.SoftwareVersion",
                "openminds.v5.core.WebResource",
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
