"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class CustomAnatomicalEntity(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CustomAnatomicalEntity"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "has_annotations",
            "openminds.v5.sands.CustomAnnotation",
            "hasAnnotation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all custom annotations which define this custom anatomical entity.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the custom anatomical entity.",
            instructions="Enter a descriptive name for this custom anatomical entity.",
        ),
        Property(
            "related_interspecies_anatomy",
            [
                "openminds.v5.controlled_terms.AnatomicalCavity",
                "openminds.v5.controlled_terms.ExternalBodyRegion",
                "openminds.v5.controlled_terms.MuscularStructure",
                "openminds.v5.controlled_terms.NervousSystemStructure",
                "openminds.v5.controlled_terms.Organ",
                "openminds.v5.controlled_terms.OrganSystemStructure",
                "openminds.v5.controlled_terms.OrganismSubstance",
                "openminds.v5.controlled_terms.OrganismSystem",
                "openminds.v5.controlled_terms.SkeletalStructure",
                "openminds.v5.controlled_terms.TissueStructure",
                "openminds.v5.controlled_terms.VascularStructure",
            ],
            "relatedInterspeciesAnatomy",
            description="no description available",
            instructions="Add the corresponding cross-species anatomical entity from the UBERON-derived terminologies that represents the generic anatomical concept underlying the custom anatomical entity.",
        ),
        Property(
            "relation_assessments",
            ["openminds.v5.sands.QualitativeRelationAssessment", "openminds.v5.sands.QuantitativeRelationAssessment"],
            "relationAssessment",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all relations (qualitative or quantitative) of this custom anatomical entity to other anatomical entities.",
        ),
    ]

    def __init__(
        self, id=None, has_annotations=None, name=None, related_interspecies_anatomy=None, relation_assessments=None
    ):
        return super().__init__(
            id=id,
            has_annotations=has_annotations,
            name=name,
            related_interspecies_anatomy=related_interspecies_anatomy,
            relation_assessments=relation_assessments,
        )
