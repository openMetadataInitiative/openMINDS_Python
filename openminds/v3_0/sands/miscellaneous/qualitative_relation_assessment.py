"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class QualitativeRelationAssessment(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/sands/QualitativeRelationAssessment"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "criteria",
            "openminds.v3_0.core.ProtocolExecution",
            "vocab:criteria",
            description="Aspects or standards on which a judgement or decision is based.",
            instructions="Add the protocol execution defining the criteria that were applied to determine this relation.",
        ),
        Property(
            "in_relation_to",
            [
                "openminds.v3_0.sands.CustomAnatomicalEntity",
                "openminds.v3_0.sands.ParcellationEntity",
                "openminds.v3_0.sands.ParcellationEntityVersion",
            ],
            "vocab:inRelationTo",
            required=True,
            description="Reference to a related element.",
            instructions="Add the anatomical entity to which the relation is described.",
        ),
        Property(
            "qualitative_overlap",
            "openminds.v3_0.controlled_terms.QualitativeOverlap",
            "vocab:qualitativeOverlap",
            required=True,
            description="Semantic characterization of how much two things occupy the same space.",
            instructions="Add the qualitative overlap that best describes the relation between the two anatomical entities.",
        ),
    ]

    def __init__(self, criteria=None, in_relation_to=None, qualitative_overlap=None):
        return super().__init__(
            criteria=criteria,
            in_relation_to=in_relation_to,
            qualitative_overlap=qualitative_overlap,
        )
