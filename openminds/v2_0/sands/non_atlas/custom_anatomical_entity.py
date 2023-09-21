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
    type_ = ["https://openminds.ebrains.eu/sands/CustomAnatomicalEntity"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "has_annotation",
            "openminds.v2_0.sands.CustomAnnotation",
            "vocab:hasAnnotation",
            description="no description available",
            instructions="Add the custom annotation which this custom anatomical entity defines."
        ),
        Property(
            "name",
            str,
            "vocab:name",formatting="text/plain",
            
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this custom anatomical entity."
        ),
        Property(
            "relation_assessment",
            ['openminds.v2_0.sands.QualitativeRelationAssessment', 'openminds.v2_0.sands.QuantitativeRelationAssessment'],
            "vocab:relationAssessment",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add one or several relations of this custom anatomical entity to parcellation entities used in defined parcellation terminologies."
        ),
        
    ]

    def __init__(self, id=None, has_annotation=None, name=None, relation_assessment=None):
        return super().__init__(id=id,has_annotation=has_annotation,name=name,relation_assessment=relation_assessment,)

