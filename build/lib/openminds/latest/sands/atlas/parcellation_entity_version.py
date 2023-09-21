"""
<description not available>
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class ParcellationEntityVersion(LinkedMetadata):
    """
    <description not available>
    """
    type_ = ["https://openminds.ebrains.eu/sands/ParcellationEntityVersion"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "abbreviation",
            str,
            "vocab:abbreviation",formatting="text/plain",
            
            
            description="no description available",
            instructions="Enter the official abbreviation of this parcellation entity version."
        ),
        Property(
            "additional_remarks",
            str,
            "vocab:additionalRemarks",formatting="text/markdown",
            multiline=True,
            
            description="Mention of what deserves additional attention or notice.",
            instructions="Enter any additional remarks concerning this parcellation entity version."
        ),
        Property(
            "alternate_name",
            str,
            "vocab:alternateName",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            formatting="text/plain",
            
            
            description="no description available",
            instructions="Enter any alternate names, including any alternative abbreviations, for this parcellation entity version."
        ),
        Property(
            "corrected_name",
            str,
            "vocab:correctedName",formatting="text/plain",
            
            
            description="no description available",
            instructions="Enter the refined or corrected name of this parcellation entity version."
        ),
        Property(
            "has_annotation",
            "openminds.latest.sands.AtlasAnnotation",
            "vocab:hasAnnotation",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add all atlas annotations which define this parcellation entity version."
        ),
        Property(
            "has_parent",
            ['openminds.latest.sands.ParcellationEntity', 'openminds.latest.sands.ParcellationEntityVersion'],
            "vocab:hasParent",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Reference to a parent object or legal person.",
            instructions="Add all anatomical parent structures (or version of the structures) for this parcellation entity as defined within corresponding brain atlas version."
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",formatting="text/plain",
            
            
            description="no description available",
            instructions="Enter a lookup label for this parcellation entity version that may help you to find this instance more easily."
        ),
        Property(
            "name",
            str,
            "vocab:name",formatting="text/plain",
            
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this parcellation entity version."
        ),
        Property(
            "ontology_identifier",
            str,
            "vocab:ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            formatting="text/plain",
            
            
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation entity version."
        ),
        Property(
            "relation_assessment",
            ['openminds.latest.sands.QualitativeRelationAssessment', 'openminds.latest.sands.QuantitativeRelationAssessment'],
            "vocab:relationAssessment",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add all relations (qualitative or quantitative) of this parcellation entity version to other anatomical entities."
        ),
        Property(
            "version_identifier",
            str,
            "vocab:versionIdentifier",formatting="text/plain",
            
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this parcellation entity version."
        ),
        Property(
            "version_innovation",
            str,
            "vocab:versionInnovation",formatting="text/markdown",
            multiline=True,
            
            description="Documentation on what changed in comparison to a previously published form of something.",
            instructions="Enter a short description (or summary) of the novelties/peculiarities of this parcellation entity version in comparison to its preceding versions. If this parcellation entity version is the first version, leave blank."
        ),
        
    ]

    def __init__(self, id=None, abbreviation=None, additional_remarks=None, alternate_name=None, corrected_name=None, has_annotation=None, has_parent=None, lookup_label=None, name=None, ontology_identifier=None, relation_assessment=None, version_identifier=None, version_innovation=None):
        return super().__init__(id=id,abbreviation=abbreviation,additional_remarks=additional_remarks,alternate_name=alternate_name,corrected_name=corrected_name,has_annotation=has_annotation,has_parent=has_parent,lookup_label=lookup_label,name=name,ontology_identifier=ontology_identifier,relation_assessment=relation_assessment,version_identifier=version_identifier,version_innovation=version_innovation,)

