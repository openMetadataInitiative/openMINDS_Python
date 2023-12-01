"""
Structured information on an image.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Image(LinkedMetadata):
    """
    Structured information on an image.
    """

    type_ = "https://openminds.ebrains.eu/sands/Image"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "coordinate_space",
            "openminds.v1.sands.CoordinateSpace",
            "coordinateSpace",
            required=True,
            description="Two or three dimensional geometric setting.",
            instructions="Add the coordinate space this image exists in.",
        ),
        Property(
            "defined_in",
            "openminds.v1.core.FileInstance",
            "definedIn",
            required=True,
            description="Reference to a file instance in which something is stored.",
            instructions="Add the file in which this image is stored in.",
        ),
        Property(
            "voxel_sizes",
            "openminds.v1.core.QuantitativeValue",
            "voxelSize",
            multiple=True,
            unique_items=True,
            min_items=2,
            max_items=3,
            required=True,
            description="Extent of the discrete elements comprising a three-dimensional entity.",
            instructions="Add two or three values with units defined that describe the size of one pixel (2D: [x, y]) or voxel (3D: [x, y, z]) in the physical space.",
        ),
    ]

    def __init__(self, id=None, coordinate_space=None, defined_in=None, voxel_sizes=None):
        return super().__init__(
            id=id,
            coordinate_space=coordinate_space,
            defined_in=defined_in,
            voxel_sizes=voxel_sizes,
        )
