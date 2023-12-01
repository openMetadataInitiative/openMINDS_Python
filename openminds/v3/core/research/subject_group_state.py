"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class SubjectGroupState(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/SubjectGroupState"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concering the specimen (set) in this state.",
        ),
        Property(
            "age",
            ["openminds.v3.core.QuantitativeValue", "openminds.v3.core.QuantitativeValueRange"],
            "age",
            description="Time of life or existence at which some particular qualification, capacity or event arises.",
            instructions="Enter the age of the specimen (set) in this state.",
        ),
        Property(
            "age_categories",
            "openminds.v3.controlled_terms.AgeCategory",
            "ageCategory",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Distinct life cycle class that is defined by a similar age or age range (developmental stage) within a group of individual beings.",
            instructions="Add the age category of the subject in this state.",
        ),
        Property(
            "attributes",
            "openminds.v3.controlled_terms.SubjectAttribute",
            "attribute",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all attributes that can be ascribed to this subject group state.",
        ),
        Property(
            "descended_from",
            "openminds.v3.core.SubjectGroupState",
            "descendedFrom",
            description="no description available",
            instructions="Add the previous subject group state.",
        ),
        Property(
            "handedness",
            "openminds.v3.controlled_terms.Handedness",
            "handedness",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Degree to which an organism prefers one hand or foot over the other hand or foot during the performance of a task.",
            instructions="Add all preferred types of handedness of the subject group in this state.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this specimen (set) state that is used within the corresponding data files to identify this specimen (set) state.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this specimen (set) state that may help you to find this instance more easily.",
        ),
        Property(
            "pathologies",
            ["openminds.v3.controlled_terms.Disease", "openminds.v3.controlled_terms.DiseaseModel"],
            "pathology",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease.",
            instructions="Add all (human) diseases and/or conditions that the specimen (set) in this state has and/or is a model for.",
        ),
        Property(
            "relative_time_indication",
            ["openminds.v3.core.QuantitativeValue", "openminds.v3.core.QuantitativeValueRange"],
            "relativeTimeIndication",
            description="no description available",
            instructions="If there is a temporal relation between the states of a specimen (set), enter the relative time that has passed between this and the preceding specimen (set) state referenced under 'descendedFrom'.",
        ),
        Property(
            "weight",
            ["openminds.v3.core.QuantitativeValue", "openminds.v3.core.QuantitativeValueRange"],
            "weight",
            description="Amount that a thing or being weighs.",
            instructions="Enter the weight of the specimen (set) in this state.",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        age=None,
        age_categories=None,
        attributes=None,
        descended_from=None,
        handedness=None,
        internal_identifier=None,
        lookup_label=None,
        pathologies=None,
        relative_time_indication=None,
        weight=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            age=age,
            age_categories=age_categories,
            attributes=attributes,
            descended_from=descended_from,
            handedness=handedness,
            internal_identifier=internal_identifier,
            lookup_label=lookup_label,
            pathologies=pathologies,
            relative_time_indication=relative_time_indication,
            weight=weight,
        )
