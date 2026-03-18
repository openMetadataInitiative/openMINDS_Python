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

    type_ = "https://openminds.om-i.org/types/TissueSampleCollectionState"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "additional_remarks",
            str,
            "additionalRemarks",
            formatting="text/markdown",
            multiline=True,
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning the specimen (set) in this state.",
        ),
        Property(
            "age",
            "openminds.v5.core.SpecimenAge",
            "age",
            description="Time of life or existence at which some particular qualification, capacity or event arises.",
            instructions="Enter the age and age reference of the specimen (set) in this state.",
        ),
        Property(
            "associated_protocols",
            ["openminds.v5.core.Protocol", "openminds.v5.core.BehavioralProtocol"],
            "associatedProtocol",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all technical and/or behavioral protocols associated with this specimen state.",
        ),
        Property(
            "attributes",
            "openminds.v5.controlled_terms.TissueSampleAttribute",
            "attribute",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all attributes that can be ascribed to this tissue sample collection state.",
        ),
        Property(
            "descended_from",
            [
                "openminds.v5.core.SubjectGroupState",
                "openminds.v5.core.SubjectState",
                "openminds.v5.core.TissueSampleCollectionState",
                "openminds.v5.core.TissueSampleState",
            ],
            "descendedFrom",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all specimen states used to produce or obtain this tissue sample collection state.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies the tissue sample collection state within a particular product.",
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
            ["openminds.v5.controlled_terms.Disease", "openminds.v5.controlled_terms.DiseaseModel"],
            "pathology",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease.",
            instructions="Add all (human) diseases and/or conditions that the specimen (set) in this state has and/or is a model for.",
        ),
        Property(
            "relative_time_indication",
            ["openminds.v5.core.QuantitativeValue", "openminds.v5.core.QuantitativeValueRange"],
            "relativeTimeIndication",
            description="no description available",
            instructions="If there is a temporal relation between the states of a specimen (set), enter the relative time that has passed between this and the preceding specimen (set) state referenced under 'descendedFrom'.",
        ),
        Property(
            "weight",
            "openminds.v5.core.SpecimenWeight",
            "weight",
            description="Amount that a thing or being weighs.",
            instructions="Enter the weight and weight type of the specimen (set) in this state.",
        ),
    ]

    def __init__(
        self,
        id=None,
        additional_remarks=None,
        age=None,
        associated_protocols=None,
        attributes=None,
        descended_from=None,
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
            associated_protocols=associated_protocols,
            attributes=attributes,
            descended_from=descended_from,
            internal_identifier=internal_identifier,
            lookup_label=lookup_label,
            pathologies=pathologies,
            relative_time_indication=relative_time_indication,
            weight=weight,
        )
