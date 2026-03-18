"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ElectrodeUsage(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ElectrodeUsage"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "anatomical_location",
            [
                "openminds.v5.controlled_terms.AnatomicalCavity",
                "openminds.v5.controlled_terms.CellType",
                "openminds.v5.controlled_terms.ExternalBodyRegion",
                "openminds.v5.controlled_terms.MuscularStructure",
                "openminds.v5.controlled_terms.NervousSystemStructure",
                "openminds.v5.controlled_terms.Organ",
                "openminds.v5.controlled_terms.OrganSystemStructure",
                "openminds.v5.controlled_terms.OrganismSubstance",
                "openminds.v5.controlled_terms.OrganismSystem",
                "openminds.v5.controlled_terms.SkeletalStructure",
                "openminds.v5.controlled_terms.SubcellularEntity",
                "openminds.v5.controlled_terms.TissueStructure",
                "openminds.v5.controlled_terms.VascularStructure",
                "openminds.v5.sands.CustomAnatomicalEntity",
                "openminds.v5.sands.ParcellationEntity",
                "openminds.v5.sands.ParcellationEntityVersion",
            ],
            "anatomicalLocation",
            description="no description available",
            instructions="Add the anatomical entity that semantically best describes the anatomical location of the electrode contact.",
        ),
        Property(
            "contact_resistance",
            ["openminds.v5.core.QuantitativeValue", "openminds.v5.core.QuantitativeValueRange"],
            "contactResistance",
            description="no description available",
            instructions="Enter the contact resistance of this electrode during its use.",
        ),
        Property(
            "device",
            "openminds.v5.ephys.Electrode",
            "device",
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add the electrode used.",
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
            ["openminds.v5.core.File", "openminds.v5.core.FileBundle"],
            "metadataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all files or file bundles containing additional information about the usage of this device.",
        ),
        Property(
            "spatial_location",
            "openminds.v5.sands.CoordinatePoint",
            "spatialLocation",
            description="no description available",
            instructions="Add the coordinate point that best describes the spatial location of the electrode contact during its use.",
        ),
        Property(
            "used_specimen",
            ["openminds.v5.core.SubjectState", "openminds.v5.core.TissueSampleState"],
            "usedSpecimen",
            description="no description available",
            instructions="Add the state of the tissue sample or subject that this device was used on.",
        ),
    ]

    def __init__(
        self,
        id=None,
        anatomical_location=None,
        contact_resistance=None,
        device=None,
        lookup_label=None,
        metadata_locations=None,
        spatial_location=None,
        used_specimen=None,
    ):
        return super().__init__(
            id=id,
            anatomical_location=anatomical_location,
            contact_resistance=contact_resistance,
            device=device,
            lookup_label=lookup_label,
            metadata_locations=metadata_locations,
            spatial_location=spatial_location,
            used_specimen=used_specimen,
        )
