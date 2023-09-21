"""
Structured information on a temporary state of a tissue sample.
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class TissueSampleState(LinkedMetadata):
    """
    Structured information on a temporary state of a tissue sample.
    """
    type_ = ["https://openminds.ebrains.eu/core/TissueSampleState"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "additional_remarks",
            str,
            "vocab:additionalRemarks",formatting="text/markdown",
            multiline=True,
            
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter additional remarks about the specimen (set) in this state."
        ),
        Property(
            "age",
            ['openminds.v2_0.core.QuantitativeValue', 'openminds.v2_0.core.QuantitativeValueRange'],
            "vocab:age",
            description="Time of life or existence at which some particular qualification, capacity or event arises.",
            instructions="Add the age of the specimen (set) in this state."
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",formatting="text/plain",
            
            
            description="no description available",
            instructions="Enter a lookup label for this specimen (set) state that may help you to more easily find it again."
        ),
        Property(
            "pathology",
            ['openminds.v2_0.controlled_terms.Disease', 'openminds.v2_0.controlled_terms.DiseaseModel'],
            "vocab:pathology",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Structural and functional deviation from the normal that constitutes a disease or characterizes a particular disease.",
            instructions="Add the pathology of the specimen (set) in this state."
        ),
        Property(
            "weight",
            ['openminds.v2_0.core.QuantitativeValue', 'openminds.v2_0.core.QuantitativeValueRange'],
            "vocab:weight",
            description="Amount that a thing or being weighs.",
            instructions="Add the weight of the specimen (set) in this state."
        ),
        
    ]

    def __init__(self, id=None, additional_remarks=None, age=None, lookup_label=None, pathology=None, weight=None):
        return super().__init__(id=id,additional_remarks=additional_remarks,age=age,lookup_label=lookup_label,pathology=pathology,weight=weight,)

