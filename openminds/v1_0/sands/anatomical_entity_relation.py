"""
Structured information on the relation between one anatomical entity and another.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class AnatomicalEntityRelation(LinkedMetadata):
    """
    Structured information on the relation between one anatomical entity and another.
    """

    type_ = ["https://openminds.ebrains.eu/sands/AnatomicalEntityRelation"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "criteria",
            "openminds.v1_0.core.ProtocolExecution",
            "vocab:criteria",
            description="Aspects or standards on which a judgement or decision is based.",
            instructions="Add the protocol execution defining the criteria that were applied to determine this relation.",
        ),
        Property(
            "criteria_quality_type",
            "openminds.v1_0.controlled_terms.CriteriaQualityType",
            "vocab:criteriaQualityType",
            required=True,
            description="Distinct class that defines how the judgement or decision was made for a particular criteria.",
            instructions="Add the quality type of the stated criteria used to determine this relation.",
        ),
        Property(
            "in_relation_to",
            "openminds.v1_0.sands.AnatomicalEntity",
            "vocab:inRelationTo",
            required=True,
            description="Reference to a related element.",
            instructions="Add the anatomical entity to which the relation is described.",
        ),
        Property(
            "qualitative_overlap",
            "openminds.v1_0.controlled_terms.QualitativeOverlap",
            "vocab:qualitativeOverlap",
            required=True,
            description="Semantic characterization of how much two things occupy the same space.",
            instructions="Add the qualitative overlap that best describes the relation between the two anatomical entities.",
        ),
        Property(
            "quantitative_overlap",
            ["openminds.v1_0.core.QuantitativeValue", "openminds.v1_0.core.QuantitativeValueRange"],
            "vocab:quantitativeOverlap",
            description="Numerical characterization of how much two things occupy the same space.",
            instructions="Add the quantitative overlap between the two anatomical entities preferably expressed in percentage.",
        ),
    ]

    def __init__(
        self,
        id=None,
        criteria=None,
        criteria_quality_type=None,
        in_relation_to=None,
        qualitative_overlap=None,
        quantitative_overlap=None,
    ):
        return super().__init__(
            id=id,
            criteria=criteria,
            criteria_quality_type=criteria_quality_type,
            in_relation_to=in_relation_to,
            qualitative_overlap=qualitative_overlap,
            quantitative_overlap=quantitative_overlap,
        )
