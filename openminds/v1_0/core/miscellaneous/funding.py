"""
Structured information on used funding.
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class Funding(LinkedMetadata):
    """
    Structured information on used funding.
    """
    type_ = ["https://openminds.ebrains.eu/core/Funding"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "acknowledgement",
            str,
            "vocab:acknowledgement",formatting="text/plain",
            
            
            description="Offical declaration or avowal of appreciation of an act or achievement.",
            instructions="Enter the acknowledgement that should be used with this funding."
        ),
        Property(
            "award_number",
            str,
            "vocab:awardNumber",formatting="text/plain",
            
            
            description="Machine-readable identifier for a benefit that is conferred or bestowed on the basis of merit or need.",
            instructions="Enter the associated award number of this funding."
        ),
        Property(
            "award_title",
            str,
            "vocab:awardTitle",formatting="text/plain",
            
            
            description="Human-readable identifier for a benefit that is conferred or bestowed on the basis of merit or need.",
            instructions="Enter the award title of this funding."
        ),
        Property(
            "funder",
            "openminds.v1_0.core.Organization",
            "vocab:funder",required=True,
            description="Legal person that provides money for a particular purpose.",
            instructions="Add the organization that provided this funding."
        ),
        
    ]

    def __init__(self, id=None, acknowledgement=None, award_number=None, award_title=None, funder=None):
        return super().__init__(id=id,acknowledgement=acknowledgement,award_number=award_number,award_title=award_title,funder=funder,)

