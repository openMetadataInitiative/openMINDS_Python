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

    type_ = "https://openminds.ebrains.eu/ephys/ElectrodeUsage"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "anatomical_location",
            [
                "openminds.v3.controlled_terms.CellType",
                "openminds.v3.controlled_terms.Organ",
                "openminds.v3.controlled_terms.OrganismSubstance",
                "openminds.v3.controlled_terms.SubcellularEntity",
                "openminds.v3.controlled_terms.UBERONParcellation",
                "openminds.v3.sands.CustomAnatomicalEntity",
                "openminds.v3.sands.ParcellationEntity",
                "openminds.v3.sands.ParcellationEntityVersion",
            ],
            "anatomicalLocation",
            description="no description available",
            instructions="Add the anatomical entity that semantically best describes the anatomical location of the electrode contact.",
        ),
        Property(
            "contact_resistance",
            ["openminds.v3.core.QuantitativeValue", "openminds.v3.core.QuantitativeValueRange"],
            "contactResistance",
            description="no description available",
            instructions="Enter the contact resistance of this electrode during its use.",
        ),
        Property(
            "device",
            "openminds.v3.ephys.Electrode",
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
            ["openminds.v3.core.File", "openminds.v3.core.FileBundle"],
            "metadataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all files or file bundles containing additional information about the usage of this device.",
        ),
        Property(
            "spatial_location",
            "openminds.v3.sands.CoordinatePoint",
            "spatialLocation",
            description="no description available",
            instructions="Add the coordinate point that best describes the spatial location of the electrode contact during its use.",
        ),
        Property(
            "used_specimen",
            ["openminds.v3.core.SubjectState", "openminds.v3.core.TissueSampleState"],
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
