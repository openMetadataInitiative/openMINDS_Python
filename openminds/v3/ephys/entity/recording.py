"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Recording(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/ephys/Recording"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this recording.",
        ),
        Property(
            "channels",
            "openminds.v3.ephys.Channel",
            "channel",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Enter all channels used for this recording.",
        ),
        Property(
            "data_location",
            ["openminds.v3.core.File", "openminds.v3.core.FileBundle"],
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
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this recording that is used within the corresponding data files to identify this recording.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this recording.",
        ),
        Property(
            "previous_recording",
            "openminds.v3.ephys.Recording",
            "previousRecording",
            description="no description available",
            instructions="If this recording is part of a sequence of recordings (e.g., multiple repetitions or sweeps), add the recording preceding this recording.",
        ),
        Property(
            "recorded_with",
            [
                "openminds.v3.ephys.ElectrodeArrayUsage",
                "openminds.v3.ephys.ElectrodeUsage",
                "openminds.v3.ephys.PipetteUsage",
                "openminds.v3.specimen_prep.SlicingDeviceUsage",
            ],
            "recordedWith",
            required=True,
            description="no description available",
            instructions="Add the device used to generate this recording.",
        ),
        Property(
            "sampling_frequency",
            "openminds.v3.core.QuantitativeValue",
            "samplingFrequency",
            required=True,
            description="no description available",
            instructions="Enter the sampling frequency of this recording.",
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
        previous_recording=None,
        recorded_with=None,
        sampling_frequency=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            channels=channels,
            data_location=data_location,
            internal_identifier=internal_identifier,
            name=name,
            previous_recording=previous_recording,
            recorded_with=recorded_with,
            sampling_frequency=sampling_frequency,
        )
