"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class GridImageSequence(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/GridImageSequence"
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
            instructions="Enter any additional remarks concerning this grid image sequence.",
        ),
        Property(
            "coordinate_framework",
            ["openminds.v5.sands.CommonCoordinateFrameworkVersion", "openminds.v5.sands.CustomCoordinateFramework"],
            "coordinateFramework",
            description="no description available",
            instructions="Add the coordinate space in which this grid image sequence exists.",
        ),
        Property(
            "data_location",
            ["openminds.v5.core.File", "openminds.v5.core.FileBundle"],
            "dataLocation",
            required=True,
            description="no description available",
            instructions="Add a reference to the file to which this grid image sequence information applies. If the information applies uniformly to a grid image sequence file series, a reference to the corresponding file bundle may be provided instead.",
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
            instructions="Enter the common dimension of the consecutive grid images (frames) in pixels.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of the grid image sequence.",
            instructions="Enter a descriptive name of this grid image sequence preferably matching the filename.",
        ),
        Property(
            "number_of_images",
            int,
            "numberOfImages",
            description="no description available",
            instructions="Enter the total number of grid images in this sequence (at least two).",
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
            instructions="Add the used device for obtaining this grid image sequence.",
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
            instructions="Enter the common physical pixel size for the consecutive grid images (frames) (in x,y order).",
        ),
        Property(
            "temporal_sampling_frequency",
            "openminds.v5.core.QuantitativeValue",
            "temporalSamplingFrequency",
            required=True,
            description="no description available",
            instructions="Enter the rate at which consecutive grid images (frames) are captured in a sequence, preferably measured in Hertz (Hz).",
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
        number_of_images=None,
        obtained_with=None,
        pixel_sizes=None,
        temporal_sampling_frequency=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            coordinate_framework=coordinate_framework,
            data_location=data_location,
            dimensions=dimensions,
            name=name,
            number_of_images=number_of_images,
            obtained_with=obtained_with,
            pixel_sizes=pixel_sizes,
            temporal_sampling_frequency=temporal_sampling_frequency,
        )
