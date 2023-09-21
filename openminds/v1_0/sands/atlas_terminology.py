"""
<description not available>
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class AtlasTerminology(LinkedMetadata):
    """
    <description not available>
    """
    type_ = ["https://openminds.ebrains.eu/sands/AtlasTerminology"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "anatomical_entity",
            "openminds.v1_0.sands.AnatomicalEntity",
            "vocab:anatomicalEntity",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Physical component of a body, organ, or tissue.",
            instructions="Add all anatomical entities that belong to this atlas terminology."
        ),
        Property(
            "defined_in",
            "openminds.v1_0.core.FileInstance",
            "vocab:definedIn",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Reference to a file instance in which something is stored.",
            instructions="Add one or several files in which this atlas terminology is stored in."
        ),
        Property(
            "full_name",
            str,
            "vocab:fullName",formatting="text/plain",
            
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name for this atlas terminology."
        ),
        Property(
            "ontology_identifier",
            str,
            "vocab:ontologyIdentifier",formatting="text/plain",
            
            
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the identifier (IRI) of the related ontological term matching this atlas terminology."
        ),
        Property(
            "short_name",
            str,
            "vocab:shortName",formatting="text/plain",
            
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a descriptive short name for this atlas terminology."
        ),
        
    ]

    def __init__(self, id=None, anatomical_entity=None, defined_in=None, full_name=None, ontology_identifier=None, short_name=None):
        return super().__init__(id=id,anatomical_entity=anatomical_entity,defined_in=defined_in,full_name=full_name,ontology_identifier=ontology_identifier,short_name=short_name,)

