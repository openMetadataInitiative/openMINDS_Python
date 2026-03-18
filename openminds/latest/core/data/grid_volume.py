"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class GridVolume(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/GridVolume"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this grid volume.",
        ),
        Property(
            "coordinate_framework",
            [
                "openminds.latest.sands.CommonCoordinateFrameworkVersion",
                "openminds.latest.sands.CustomCoordinateFramework",
            ],
            "coordinateFramework",
            description="no description available",
            instructions="Add the coordinate space in which this grid volume exists.",
        ),
        Property(
            "data_location",
            ["openminds.latest.core.File", "openminds.latest.core.FileBundle"],
            "dataLocation",
            required=True,
            description="no description available",
            instructions="Add a reference to the file to which this grid volume information applies. If the information applies uniformly to a grid volume file series, a reference to the corresponding file bundle may be provided instead.",
        ),
        Property(
            "dimensions",
            int,
            "dimension",
            multiple=True,
            unique_items=False,
            min_items=3,
            max_items=3,
            required=True,
            description="no description available",
            instructions="Enter the dimension of this grid volume.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of the grid volume.",
            instructions="Enter a descriptive name of this grid volume preferably matching the filename.",
        ),
        Property(
            "number_of_planes",
            int,
            "numberOfPlanes",
            description="no description available",
            instructions="Enter number of planes in this grid volume.",
        ),
        Property(
            "obtained_with",
            [
                "openminds.latest.ephys.ElectrodeArrayUsage",
                "openminds.latest.ephys.ElectrodeUsage",
                "openminds.latest.ephys.PipetteUsage",
                "openminds.latest.neuroimaging.MRICoilUsage",
                "openminds.latest.neuroimaging.MRIScannerUsage",
                "openminds.latest.specimen_prep.SlicingDeviceUsage",
            ],
            "obtainedWith",
            description="no description available",
            instructions="Add the used device for obtaining this grid volume.",
        ),
        Property(
            "voxel_sizes",
            "openminds.latest.core.QuantitativeValue",
            "voxelSize",
            multiple=True,
            unique_items=False,
            min_items=3,
            max_items=3,
            required=True,
            description="Extent of the discrete elements comprising a three-dimensional entity.",
            instructions="Enter the physical voxel size for this grid volume (in x,y,z order).",
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
        number_of_planes=None,
        obtained_with=None,
        voxel_sizes=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            coordinate_framework=coordinate_framework,
            data_location=data_location,
            dimensions=dimensions,
            name=name,
            number_of_planes=number_of_planes,
            obtained_with=obtained_with,
            voxel_sizes=voxel_sizes,
        )
