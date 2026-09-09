"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class RegularTimeSeries(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/RegularTimeSeries"
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
            instructions="Enter any additional remarks concerning this regular time series.",
        ),
        Property(
            "channels",
            "openminds.v5.core.Channel",
            "channel",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Enter all channels used for this regular time series.",
        ),
        Property(
            "data_location",
            ["openminds.v5.core.File", "openminds.v5.core.FileBundle"],
            "dataLocation",
            required=True,
            description="no description available",
            instructions="Add the location of the file or file bundle in which the recorded data is stored.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies the regular time series within a particular product.",
            instructions="Enter the identifier (or label) of this regular time series that is used within the corresponding data files to identify this regular time series.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of the regular time series.",
            instructions="Enter a descriptive name for this regular time series.",
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
            instructions="Add the used device for obtaining this regular time series.",
        ),
        Property(
            "previous_regular_time_series",
            "openminds.v5.core.RegularTimeSeries",
            "previousRegularTimeSeries",
            description="no description available",
            instructions="If this regular time series is part of a sequence of regular time seriess (e.g., multiple repetitions or sweeps), add the regular time series preceding this regular time series.",
        ),
        Property(
            "sampling_frequency",
            "openminds.v5.core.QuantitativeValue",
            "samplingFrequency",
            required=True,
            description="no description available",
            instructions="Enter the sampling frequency of this regular time series.",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        channels=None,
        data_location=None,
        internal_identifier=None,
        name=None,
        obtained_with=None,
        previous_regular_time_series=None,
        sampling_frequency=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            channels=channels,
            data_location=data_location,
            internal_identifier=internal_identifier,
            name=name,
            obtained_with=obtained_with,
            previous_regular_time_series=previous_regular_time_series,
            sampling_frequency=sampling_frequency,
        )
