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

    type_ = "https://openminds.om-i.org/types/AnatomicalTargetPosition"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

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
            "anatomical_targets",
            [
                "openminds.v4.controlled_terms.CellType",
                "openminds.v4.controlled_terms.Organ",
                "openminds.v4.controlled_terms.OrganismSubstance",
                "openminds.v4.controlled_terms.SubcellularEntity",
                "openminds.v4.controlled_terms.UBERONParcellation",
                "openminds.v4.sands.CustomAnatomicalEntity",
                "openminds.v4.sands.ParcellationEntity",
                "openminds.v4.sands.ParcellationEntityVersion",
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
            "spatial_locations",
            "openminds.v4.sands.CoordinatePoint",
            "spatialLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all coordinate points that describe the spatial location of the anatomical target structure(s).",
        ),
        Property(
            "target_identification_type",
            "openminds.v4.controlled_terms.AnatomicalIdentificationType",
            "targetIdentificationType",
            required=True,
            description="no description available",
            instructions="Add the target identification type that best describes how the this anatomical target position was identified.",
        ),
    ]

    def __init__(
        self, additional_remarks=None, anatomical_targets=None, spatial_locations=None, target_identification_type=None
    ):
        return super().__init__(
            additional_remarks=additional_remarks,
            anatomical_targets=anatomical_targets,
            spatial_locations=spatial_locations,
            target_identification_type=target_identification_type,
        )
