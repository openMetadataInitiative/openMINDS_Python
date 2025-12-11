"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class ViewerSpecification(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ViewerSpecification"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this viewer specification.",
        ),
        Property(
            "anchor_points",
            "openminds.v4.core.QuantitativeValue",
            "anchorPoint",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=3,
            required=True,
            description="no description available",
            instructions="Enter the coordinates of the anchor point that a viewer should use. Either state the anchor point of the annotation again or state another coordinate point.",
        ),
        Property(
            "camera_position",
            "openminds.v4.sands.CoordinatePoint",
            "cameraPosition",
            description="no description available",
            instructions="Enter the camera position that a viewer should use.",
        ),
        Property(
            "preferred_display_color",
            ["openminds.v4.controlled_terms.Colormap", "openminds.v4.sands.SingleColor"],
            "preferredDisplayColor",
            description="no description available",
            instructions="Add the preferred color that a viewer should display.",
        ),
    ]

    def __init__(
        self, additional_remarks=None, anchor_points=None, camera_position=None, preferred_display_color=None
    ):
        return super().__init__(
            additional_remarks=additional_remarks,
            anchor_points=anchor_points,
            camera_position=camera_position,
            preferred_display_color=preferred_display_color,
        )
