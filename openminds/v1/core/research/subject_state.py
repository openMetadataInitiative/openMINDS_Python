"""
Structured information on a temporary state of a subject.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class SubjectState(LinkedMetadata):
    """
    Structured information on a temporary state of a subject.
    """

    type_ = "https://openminds.ebrains.eu/core/SubjectState"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter additional remarks about the specimen (set) in this state.",
        ),
        Property(
            "age",
            ["openminds.v1.core.QuantitativeValue", "openminds.v1.core.QuantitativeValueRange"],
            "age",
            description="Time of life or existence at which some particular qualification, capacity or event arises.",
            instructions="Add the age of the specimen (set) in this state.",
        ),
        Property(
            "age_category",
            "openminds.v1.controlled_terms.AgeCategory",
            "ageCategory",
            required=True,
            description="Distinct life cycle class that is defined by a similar age or age range (developmental stage) within a group of individual beings.",
            instructions="Add the age category of the subject in this state.",
        ),
        Property(
            "handedness",
            "openminds.v1.controlled_terms.Laterality",
            "handedness",
            description="Degree to which an organism prefers one hand or foot over the other hand or foot during the performance of a task.",
            instructions="Add the preferred hand of the subject in this state.",
        ),
        Property(
            "pathologies",
            ["openminds.v1.controlled_terms.Disease", "openminds.v1.controlled_terms.DiseaseModel"],
            "pathology",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease.",
            instructions="Add the pathology of the specimen (set) in this state.",
        ),
        Property(
            "weight",
            ["openminds.v1.core.QuantitativeValue", "openminds.v1.core.QuantitativeValueRange"],
            "weight",
            description="Amount that a thing or being weighs.",
            instructions="Add the weight of the specimen (set) in this state.",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        age=None,
        age_category=None,
        handedness=None,
        pathologies=None,
        weight=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            age=age,
            age_category=age_category,
            handedness=handedness,
            pathologies=pathologies,
            weight=weight,
        )
