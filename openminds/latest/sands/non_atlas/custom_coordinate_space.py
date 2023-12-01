"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class CustomCoordinateSpace(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/CustomCoordinateSpace"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "anatomical_axes_orientation",
            "openminds.latest.controlled_terms.AnatomicalAxesOrientation",
            "anatomicalAxesOrientation",
            required=True,
            description="Relation between reference planes used in anatomy and mathematics.",
            instructions="Add the axes orientation denoted in standard anatomical terms of direction (stated as XYZ) for this custom coordinate space.",
        ),
        Property(
            "axes_origins",
            "openminds.latest.core.QuantitativeValue",
            "axesOrigin",
            multiple=True,
            unique_items=True,
            min_items=2,
            max_items=3,
            required=True,
            description="Special point in a coordinate system used as a fixed point of reference for the geometry of the surrounding space.",
            instructions="Enter the origin (central point where all axes intersect) of this custom coordinate space for two-dimensional spaces as [x, y] or for three-dimensional space as [x, y, z].",
        ),
        Property(
            "default_images",
            "openminds.latest.core.File",
            "defaultImage",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Two or three dimensional image that particluarly represents a specific coordinate space.",
            instructions="Add all image files used as visual representation of this custom coordinate space.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this custom coordinate space.",
        ),
        Property(
            "native_unit",
            "openminds.latest.controlled_terms.UnitOfMeasurement",
            "nativeUnit",
            required=True,
            description="Determinate quantity used in the original measurement.",
            instructions="Add the native unit that is used for this custom coordinate space.",
        ),
    ]

    def __init__(
        self,
        id=None,
        anatomical_axes_orientation=None,
        axes_origins=None,
        default_images=None,
        name=None,
        native_unit=None,
    ):
        return super().__init__(
            id=id,
            anatomical_axes_orientation=anatomical_axes_orientation,
            axes_origins=axes_origins,
            default_images=default_images,
            name=name,
            native_unit=native_unit,
        )
