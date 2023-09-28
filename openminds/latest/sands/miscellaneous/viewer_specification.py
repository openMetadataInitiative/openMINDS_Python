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

    type_ = "https://openminds.ebrains.eu/sands/ViewerSpecification"
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "additional_remarks",
            str,
            "vocab:additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this viewer specification.",
        ),
        Property(
            "anchor_point",
            "openminds.latest.core.QuantitativeValue",
            "vocab:anchorPoint",
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
            "openminds.latest.sands.CoordinatePoint",
            "vocab:cameraPosition",
            description="no description available",
            instructions="Enter the camera position that a viewer should use.",
        ),
        Property(
            "preferred_display_color",
            ["openminds.latest.controlled_terms.Colormap", "openminds.latest.sands.SingleColor"],
            "vocab:preferredDisplayColor",
            description="no description available",
            instructions="Add the preferred color that a viewer should display.",
        ),
    ]

    def __init__(self, additional_remarks=None, anchor_point=None, camera_position=None, preferred_display_color=None):
        return super().__init__(
            additional_remarks=additional_remarks,
            anchor_point=anchor_point,
            camera_position=camera_position,
            preferred_display_color=preferred_display_color,
        )
