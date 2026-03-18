"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class GridImage(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/GridImage"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this grid image.",
        ),
        Property(
            "coordinate_framework",
            ["openminds.v5.sands.CommonCoordinateFrameworkVersion", "openminds.v5.sands.CustomCoordinateFramework"],
            "coordinateFramework",
            description="no description available",
            instructions="Add the coordinate space in which this grid image exists.",
        ),
        Property(
            "data_location",
            ["openminds.v5.core.File", "openminds.v5.core.FileBundle"],
            "dataLocation",
            required=True,
            description="no description available",
            instructions="Add a reference to the file to which this grid image information applies. If the information applies uniformly to a grid image file series, a reference to the corresponding file bundle may be provided instead.",
        ),
        Property(
            "dimensions",
            int,
            "dimension",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=2,
            required=True,
            description="no description available",
            instructions="Enter the dimension of this grid image in pixels.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of the grid image.",
            instructions="Enter a descriptive name of this grid image preferably matching the filename.",
        ),
        Property(
            "obtained_with",
            [
                "openminds.v5.ephys.ElectrodeArrayUsage",
                "openminds.v5.ephys.ElectrodeUsage",
                "openminds.v5.ephys.PipetteUsage",
                "openminds.v5.neuroimaging.MRICoilUsage",
                "openminds.v5.neuroimaging.MRIScannerUsage",
                "openminds.v5.specimen_prep.SlicingDeviceUsage",
            ],
            "obtainedWith",
            description="no description available",
            instructions="Add the used device for obtaining this grid image.",
        ),
        Property(
            "pixel_sizes",
            "openminds.v5.core.QuantitativeValue",
            "pixelSize",
            multiple=True,
            unique_items=False,
            min_items=2,
            max_items=2,
            required=True,
            description="no description available",
            instructions="Enter the physical pixel size for this grid image (in x,y order).",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        coordinate_framework=None,
        data_location=None,
        dimensions=None,
        name=None,
        obtained_with=None,
        pixel_sizes=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            coordinate_framework=coordinate_framework,
            data_location=data_location,
            dimensions=dimensions,
            name=name,
            obtained_with=obtained_with,
            pixel_sizes=pixel_sizes,
        )
