"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class SlicingDeviceUsage(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SlicingDeviceUsage"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "device",
            "openminds.v4.specimen_prep.SlicingDevice",
            "device",
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add the slicing device used.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this device usage that may help you to find this instance more easily.",
        ),
        Property(
            "metadata_locations",
            ["openminds.v4.core.File", "openminds.v4.core.FileBundle"],
            "metadataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all files or file bundles containing additional information about the usage of this device.",
        ),
        Property(
            "oscillation_amplitude",
            "openminds.v4.core.QuantitativeValue",
            "oscillationAmplitude",
            description="no description available",
            instructions="Enter the oscillation amplitude of the blade from the slicing device during its use.",
        ),
        Property(
            "slice_thickness",
            ["openminds.v4.core.QuantitativeValue", "openminds.v4.core.QuantitativeValueRange"],
            "sliceThickness",
            required=True,
            description="no description available",
            instructions="Enter the defined slice thickness during the use of this slicing device.",
        ),
        Property(
            "slicing_angles",
            ["openminds.v4.core.QuantitativeValue", "openminds.v4.core.NumericalProperty"],
            "slicingAngle",
            multiple=True,
            unique_items=False,
            min_items=1,
            max_items=2,
            description="no description available",
            instructions="Enter all slicing angles (intentional or unintentional) in relation to the slicing plane used during this activity.",
        ),
        Property(
            "slicing_plane",
            "openminds.v4.controlled_terms.AnatomicalPlane",
            "slicingPlane",
            required=True,
            description="no description available",
            instructions="Add the anatomical plane that best describes the slicing direction of the tissue sample(s) during the use of this slicing device.",
        ),
        Property(
            "slicing_speed",
            "openminds.v4.core.QuantitativeValue",
            "slicingSpeed",
            description="no description available",
            instructions="Enter the defined slicing speed during the use of this slicing device.",
        ),
        Property(
            "used_specimen",
            ["openminds.v4.core.SubjectState", "openminds.v4.core.TissueSampleState"],
            "usedSpecimen",
            description="no description available",
            instructions="Add the state of the tissue sample or subject that this device was used on.",
        ),
        Property(
            "vibration_frequency",
            "openminds.v4.core.QuantitativeValue",
            "vibrationFrequency",
            description="no description available",
            instructions="Enter the defined vibration frequency during the use of this slicing device.",
        ),
    ]

    def __init__(
        self,
        id=None,
        device=None,
        lookup_label=None,
        metadata_locations=None,
        oscillation_amplitude=None,
        slice_thickness=None,
        slicing_angles=None,
        slicing_plane=None,
        slicing_speed=None,
        used_specimen=None,
        vibration_frequency=None,
    ):
        return super().__init__(
            id=id,
            device=device,
            lookup_label=lookup_label,
            metadata_locations=metadata_locations,
            oscillation_amplitude=oscillation_amplitude,
            slice_thickness=slice_thickness,
            slicing_angles=slicing_angles,
            slicing_plane=slicing_plane,
            slicing_speed=slicing_speed,
            used_specimen=used_specimen,
            vibration_frequency=vibration_frequency,
        )
