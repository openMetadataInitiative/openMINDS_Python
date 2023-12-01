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

    type_ = "https://openminds.ebrains.eu/sands/CustomAnatomicalEntity"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "has_annotations",
            "openminds.v3.sands.CustomAnnotation",
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
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this custom anatomical entity.",
        ),
        Property(
            "related_uberon_term",
            ["openminds.v3.controlled_terms.Organ", "openminds.v3.controlled_terms.UBERONParcellation"],
            "relatedUBERONTerm",
            description="no description available",
            instructions="Add the related anatomical entity as defined by the UBERON ontology.",
        ),
        Property(
            "relation_assessments",
            ["openminds.v3.sands.QualitativeRelationAssessment", "openminds.v3.sands.QuantitativeRelationAssessment"],
            "relationAssessment",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all relations (qualitative or quantitative) of this custom anatomical entity to other anatomical entities.",
        ),
    ]

    def __init__(self, id=None, has_annotations=None, name=None, related_uberon_term=None, relation_assessments=None):
        return super().__init__(
            id=id,
            has_annotations=has_annotations,
            name=name,
            related_uberon_term=related_uberon_term,
            relation_assessments=relation_assessments,
        )
