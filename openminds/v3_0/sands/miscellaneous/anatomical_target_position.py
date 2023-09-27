"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class AnatomicalTargetPosition(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/sands/AnatomicalTargetPosition"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "additional_remarks",
            str,
            "vocab:additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concering this anatomical target position.",
        ),
        Property(
            "anatomical_target",
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
            "vocab:anatomicalTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all anatomical entities that describe the target position(s).",
        ),
        Property(
            "spatial_location",
            "openminds.v3_0.sands.CoordinatePoint",
            "vocab:spatialLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all coordinate points that describe the spatial location of the anatomical target structure(s).",
        ),
        Property(
            "target_identification_type",
            "openminds.v3_0.controlled_terms.AnatomicalIdentificationType",
            "vocab:targetIdentificationType",
            required=True,
            description="no description available",
            instructions="Add the target identification type that best describes how the this anatomical target position was identified.",
        ),
    ]

    def __init__(
        self, additional_remarks=None, anatomical_target=None, spatial_location=None, target_identification_type=None
    ):
        return super().__init__(
            additional_remarks=additional_remarks,
            anatomical_target=anatomical_target,
            spatial_location=spatial_location,
            target_identification_type=target_identification_type,
        )
