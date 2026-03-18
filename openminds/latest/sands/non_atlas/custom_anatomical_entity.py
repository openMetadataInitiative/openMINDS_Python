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
    schema_version = "latest"

    properties = [
        Property(
            "has_annotations",
            "openminds.latest.sands.CustomAnnotation",
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
                "openminds.latest.controlled_terms.AnatomicalCavity",
                "openminds.latest.controlled_terms.ExternalBodyRegion",
                "openminds.latest.controlled_terms.MuscularStructure",
                "openminds.latest.controlled_terms.NervousSystemStructure",
                "openminds.latest.controlled_terms.Organ",
                "openminds.latest.controlled_terms.OrganSystemStructure",
                "openminds.latest.controlled_terms.OrganismSubstance",
                "openminds.latest.controlled_terms.OrganismSystem",
                "openminds.latest.controlled_terms.SkeletalStructure",
                "openminds.latest.controlled_terms.TissueStructure",
                "openminds.latest.controlled_terms.VascularStructure",
            ],
            "relatedInterspeciesAnatomy",
            description="no description available",
            instructions="Add the corresponding cross-species anatomical entity from the UBERON-derived terminologies that represents the generic anatomical concept underlying the custom anatomical entity.",
        ),
        Property(
            "relation_assessments",
            [
                "openminds.latest.sands.QualitativeRelationAssessment",
                "openminds.latest.sands.QuantitativeRelationAssessment",
            ],
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
