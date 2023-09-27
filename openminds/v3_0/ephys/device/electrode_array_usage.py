"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ElectrodeArrayUsage(LinkedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/ephys/ElectrodeArrayUsage"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "anatomical_location_of_array",
            [
                "openminds.v3_0.controlled_terms.CellType",
                "openminds.v3_0.controlled_terms.Organ",
                "openminds.v3_0.controlled_terms.OrganismSubstance",
                "openminds.v3_0.controlled_terms.SubcellularEntity",
                "openminds.v3_0.controlled_terms.UBERONParcellation",
                "openminds.v3_0.sands.CustomAnatomicalEntity",
                "openminds.v3_0.sands.ParcellationEntity",
                "openminds.v3_0.sands.ParcellationEntityVersion",
            ],
            "vocab:anatomicalLocationOfArray",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all anatomical entities that semantically best describe the overall anatomical location of the electrode array.",
        ),
        Property(
            "anatomical_location_of_electrodes",
            [
                "openminds.v3_0.controlled_terms.CellType",
                "openminds.v3_0.controlled_terms.Organ",
                "openminds.v3_0.controlled_terms.OrganismSubstance",
                "openminds.v3_0.controlled_terms.SubcellularEntity",
                "openminds.v3_0.controlled_terms.UBERONParcellation",
                "openminds.v3_0.sands.CustomAnatomicalEntity",
                "openminds.v3_0.sands.ParcellationEntity",
                "openminds.v3_0.sands.ParcellationEntityVersion",
            ],
            "vocab:anatomicalLocationOfElectrodes",
            multiple=True,
            unique_items=True,
            min_items=2,
            description="no description available",
            instructions="Add all anatomical entities that semantically best describe the anatomical location of each electrode contact of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.",
        ),
        Property(
            "contact_resistances",
            ["openminds.v3_0.core.QuantitativeValue", "openminds.v3_0.core.QuantitativeValueRange"],
            "vocab:contactResistances",
            multiple=True,
            unique_items=True,
            min_items=2,
            description="no description available",
            instructions="Enter the contact resistance for each electrode of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.",
        ),
        Property(
            "device",
            "openminds.v3_0.ephys.ElectrodeArray",
            "vocab:device",
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add the electrode array used.",
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this device usage that may help you to find this instance more easily.",
        ),
        Property(
            "metadata_location",
            ["openminds.v3_0.core.File", "openminds.v3_0.core.FileBundle"],
            "vocab:metadataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all files or file bundles containing additional information about the usage of this device.",
        ),
        Property(
            "spatial_location_of_electrodes",
            "openminds.v3_0.sands.CoordinatePoint",
            "vocab:spatialLocationOfElectrodes",
            multiple=True,
            unique_items=True,
            min_items=2,
            description="no description available",
            instructions="Add all coordinate points that best describe the spatial location of each electrode contact of this array during its use, in the same order that the electrode identifiers for this electrode array have been specified.",
        ),
        Property(
            "used_electrode",
            str,
            "vocab:usedElectrode",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter the identifiers of all electrodes that are actually in use for this array.",
        ),
        Property(
            "used_specimen",
            ["openminds.v3_0.core.SubjectState", "openminds.v3_0.core.TissueSampleState"],
            "vocab:usedSpecimen",
            description="no description available",
            instructions="Add the state of the tissue sample or subject that this device was used on.",
        ),
    ]

    def __init__(
        self,
        id=None,
        anatomical_location_of_array=None,
        anatomical_location_of_electrodes=None,
        contact_resistances=None,
        device=None,
        lookup_label=None,
        metadata_location=None,
        spatial_location_of_electrodes=None,
        used_electrode=None,
        used_specimen=None,
    ):
        return super().__init__(
            id=id,
            anatomical_location_of_array=anatomical_location_of_array,
            anatomical_location_of_electrodes=anatomical_location_of_electrodes,
            contact_resistances=contact_resistances,
            device=device,
            lookup_label=lookup_label,
            metadata_location=metadata_location,
            spatial_location_of_electrodes=spatial_location_of_electrodes,
            used_electrode=used_electrode,
            used_specimen=used_specimen,
        )
