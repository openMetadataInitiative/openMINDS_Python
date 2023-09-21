"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ParcellationEntity(LinkedMetadata):
    """
    <description not available>
    """
    type_ = ["https://openminds.ebrains.eu/sands/ParcellationEntity"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "has_annotation",
            "openminds.v2_0.sands.AtlasAnnotation",
            "vocab:hasAnnotation",
            description="no description available",
            instructions="Add the atlas annotation which this parcellation entity defines."
        ),
        Property(
            "has_parent",
            "openminds.v2_0.sands.ParcellationEntity",
            "vocab:hasParent",
            description="Reference to a parent object or legal person.",
            instructions="Add for this parcellation entity the defined anatomical parent structure."
        ),
        Property(
            "is_part_of",
            "openminds.v2_0.sands.ParcellationTerminology",
            "vocab:isPartOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add one or several parcellation terminologies to which this parcellation entity belongs."
        ),
        Property(
            "name",
            str,
            "vocab:name",formatting="text/plain",
            
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name for this parcellation entity."
        ),
        Property(
            "ontology_identifier",
            IRI,
            "vocab:ontologyIdentifier",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the ontological term matching this parcellation entity."
        ),
        Property(
            "related_uberon_term",
            "openminds.v2_0.controlled_terms.UBERONParcellation",
            "vocab:relatedUBERONTerm",required=True,
            description="no description available",
            instructions="Add the related UBERON parcellation term."
        ),
        Property(
            "relation_assessment",
            ['openminds.v2_0.sands.QualitativeRelationAssessment', 'openminds.v2_0.sands.QuantitativeRelationAssessment'],
            "vocab:relationAssessment",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add one or several relations of this parcellation entity to parcellation entities of other parcellation terminologies."
        ),
        Property(
            "version_identifier",
            str,
            "vocab:versionIdentifier",formatting="text/plain",
            
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this parcellation entity."
        ),
        Property(
            "version_innovation",
            str,
            "vocab:versionInnovation",formatting="text/markdown",
            multiline=True,
            required=True,
            description="Documentation on what changed in comparison to a previously published form of something.",
            instructions="Enter a short description of the novelties/peculiarities of this parcellation entity."
        ),
        
    ]

    def __init__(self, id=None, has_annotation=None, has_parent=None, is_part_of=None, name=None, ontology_identifier=None, related_uberon_term=None, relation_assessment=None, version_identifier=None, version_innovation=None):
        return super().__init__(id=id,has_annotation=has_annotation,has_parent=has_parent,is_part_of=is_part_of,name=name,ontology_identifier=ontology_identifier,related_uberon_term=related_uberon_term,relation_assessment=relation_assessment,version_identifier=version_identifier,version_innovation=version_innovation,)

