"""
Structured information on a person.
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class Person(LinkedMetadata):
    """
    Structured information on a person.
    """
    type_ = ["https://openminds.ebrains.eu/core/Person"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "digital_identifier",
            "openminds.v1_0.core.DigitalIdentifier",
            "vocab:digitalIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Digital handle to identify objects or legal persons.",
            instructions="Add one or several globally unique and persistent digital identifier for this person."
        ),
        Property(
            "email",
            str,
            "vocab:email",formatting="text/plain",
            
            required=True,
            description="Address to which or from which an electronic mail can be sent.",
            instructions="Enter the email address of this person."
        ),
        Property(
            "family_name",
            str,
            "vocab:familyName",formatting="text/plain",
            
            
            description="Name borne in common by members of a family.",
            instructions="Enter the family name of this person."
        ),
        Property(
            "given_name",
            str,
            "vocab:givenName",formatting="text/plain",
            
            required=True,
            description="Name given to a person, including all potential middle names, but excluding the family name.",
            instructions="Enter the given name of this person."
        ),
        
    ]

    def __init__(self, id=None, digital_identifier=None, email=None, family_name=None, given_name=None):
        return super().__init__(id=id,digital_identifier=digital_identifier,email=email,family_name=family_name,given_name=given_name,)

