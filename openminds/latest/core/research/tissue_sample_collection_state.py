"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class TissueSampleCollectionState(LinkedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/core/TissueSampleCollectionState"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "additional_remarks",
            str,
            "vocab:additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concering the specimen (set) in this state.",
        ),
        Property(
            "age",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "vocab:age",
            description="Time of life or existence at which some particular qualification, capacity or event arises.",
            instructions="Enter the age of the specimen (set) in this state.",
        ),
        Property(
            "attribute",
            "openminds.latest.controlled_terms.TissueSampleAttribute",
            "vocab:attribute",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all attributes that can be ascribed to this tissue sample collection state.",
        ),
        Property(
            "descended_from",
            [
                "openminds.latest.core.SubjectGroupState",
                "openminds.latest.core.SubjectState",
                "openminds.latest.core.TissueSampleCollectionState",
                "openminds.latest.core.TissueSampleState",
            ],
            "vocab:descendedFrom",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all specimen states used to produce or obtain this tissue sample collection state.",
        ),
        Property(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this specimen (set) state that is used within the corresponding data files to identify this specimen (set) state.",
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this specimen (set) state that may help you to find this instance more easily.",
        ),
        Property(
            "pathology",
            ["openminds.latest.controlled_terms.Disease", "openminds.latest.controlled_terms.DiseaseModel"],
            "vocab:pathology",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease.",
            instructions="Add all (human) diseases and/or conditions that the specimen (set) in this state has and/or is a model for.",
        ),
        Property(
            "relative_time_indication",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "vocab:relativeTimeIndication",
            description="no description available",
            instructions="If there is a temporal relation between the states of a specimen (set), enter the relative time that has passed between this and the preceding specimen (set) state referenced under 'descendedFrom'.",
        ),
        Property(
            "weight",
            ["openminds.latest.core.QuantitativeValue", "openminds.latest.core.QuantitativeValueRange"],
            "vocab:weight",
            description="Amount that a thing or being weighs.",
            instructions="Enter the weight of the specimen (set) in this state.",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        age=None,
        attribute=None,
        descended_from=None,
        internal_identifier=None,
        lookup_label=None,
        pathology=None,
        relative_time_indication=None,
        weight=None,
    ):
        return super().__init__(
            id=id,
            additional_remarks=additional_remarks,
            age=age,
            attribute=attribute,
            descended_from=descended_from,
            internal_identifier=internal_identifier,
            lookup_label=lookup_label,
            pathology=pathology,
            relative_time_indication=relative_time_indication,
            weight=weight,
        )
