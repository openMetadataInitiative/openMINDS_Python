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

    type_ = "https://openminds.ebrains.eu/sands/AnatomicalTargetPosition"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this anatomical target position.",
        ),
        Property(
            "anatomical_target",
            [
                "openminds.latest.controlled_terms.CellType",
                "openminds.latest.controlled_terms.Organ",
                "openminds.latest.controlled_terms.OrganismSubstance",
                "openminds.latest.controlled_terms.SubcellularEntity",
                "openminds.latest.controlled_terms.UBERONParcellation",
                "openminds.latest.sands.CustomAnatomicalEntity",
                "openminds.latest.sands.ParcellationEntity",
                "openminds.latest.sands.ParcellationEntityVersion",
            ],
            "anatomicalTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all anatomical entities that describe the target position(s).",
        ),
        Property(
            "spatial_location",
            "openminds.latest.sands.CoordinatePoint",
            "spatialLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all coordinate points that describe the spatial location of the anatomical target structure(s).",
        ),
        Property(
            "target_identification_type",
            "openminds.latest.controlled_terms.AnatomicalIdentificationType",
            "targetIdentificationType",
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
