"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class QuantitativeRelationAssessment(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/QuantitativeRelationAssessment"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "criteria",
            "openminds.latest.core.ProtocolExecution",
            "criteria",
            description="Aspects or standards on which a judgement or decision is based.",
            instructions="Add the protocol execution defining the criteria that were applied to determine this relation.",
        ),
        Property(
            "in_relation_to",
            "openminds.latest.sands.ParcellationEntityVersion",
            "inRelationTo",
            required=True,
            description="Reference to a related element.",
            instructions="Add the parcellation entity version to which the relation is described.",
        ),
        Property(
            "quantitative_overlap",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "quantitativeOverlap",
            required=True,
            description="Numerical characterization of how much two things occupy the same space.",
            instructions="Enter the quantitative overlap between the two anatomical entities, preferably expressed in percentage.",
        ),
    ]

    def __init__(self, criteria=None, in_relation_to=None, quantitative_overlap=None):
        return super().__init__(
            criteria=criteria,
            in_relation_to=in_relation_to,
            quantitative_overlap=quantitative_overlap,
        )
