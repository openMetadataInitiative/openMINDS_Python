"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class MRICoilUsage(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/MRICoilUsage"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "active_elements",
            str,
            "activeElement",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Only applicable to radiofrequency (RF) coils! Enter the active coil element identifier(s) corresponding to the transmitting and/or receiving elements that were electrically active during this acquisition; the number of identifiers typically matches the number of physical elements in the selected RF coil and may be fewer if some elements were disabled.",
        ),
        Property(
            "device",
            "openminds.latest.neuroimaging.MRICoil",
            "device",
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add the MRI Coil used.",
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
            ["openminds.latest.core.File", "openminds.latest.core.FileBundle"],
            "metadataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all files or file bundles containing additional information about the usage of this device.",
        ),
        Property(
            "mounting_location",
            "openminds.latest.controlled_terms.ExternalBodyRegion",
            "mountingLocation",
            description="no description available",
            instructions="Add the anatomical mounting location of the coil, indicating where the coil was positioned on or around the subject (for example, head, neck, knee, or torso). This information is typically applicable to radiofrequency (RF) coils and may be omitted for gradient or shim systems.",
        ),
        Property(
            "signal_directionality",
            "openminds.latest.controlled_terms.SignalDirectionality",
            "signalDirectionality",
            required=True,
            description="no description available",
            instructions="Add the signal directionality of the coil, indicating whether it was used for signal transmission, reception, or both. This information is typically defined in the system configuration and can be retrieved from the DICOM header or scanner hardware metadata.",
        ),
        Property(
            "used_specimen",
            ["openminds.latest.core.SubjectState", "openminds.latest.core.TissueSampleState"],
            "usedSpecimen",
            description="no description available",
            instructions="Add the state of the tissue sample or subject that this device was used on.",
        ),
    ]

    def __init__(
        self,
        id=None,
        active_elements=None,
        device=None,
        lookup_label=None,
        metadata_locations=None,
        mounting_location=None,
        signal_directionality=None,
        used_specimen=None,
    ):
        return super().__init__(
            id=id,
            active_elements=active_elements,
            device=device,
            lookup_label=lookup_label,
            metadata_locations=metadata_locations,
            mounting_location=mounting_location,
            signal_directionality=signal_directionality,
            used_specimen=used_specimen,
        )
