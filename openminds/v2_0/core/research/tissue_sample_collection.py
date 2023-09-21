"""
<description not available>
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class TissueSampleCollection(LinkedMetadata):
    """
    <description not available>
    """
    type_ = ["https://openminds.ebrains.eu/core/TissueSampleCollection"]
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
            instructions="Enter additional remarks about the specimen set."
        ),
        Property(
            "biological_sex",
            "openminds.v2_0.controlled_terms.BiologicalSex",
            "vocab:biologicalSex",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.",
            instructions="Add the biological sex of all specimen in this set."
        ),
        Property(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",formatting="text/plain",
            
            
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier of this specimen set that is used within the corresponding data."
        ),
        Property(
            "laterality",
            "openminds.v2_0.controlled_terms.Laterality",
            "vocab:laterality",
            multiple=True,
            unique_items=True,
            min_items=1,
            max_items=2,
            
            description="Differentiation between a pair of lateral homologous parts of the body.",
            instructions="Add one or both hemisphere sides from which the tissue samples in this collection originate from."
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",formatting="text/plain",
            
            
            description="no description available",
            instructions="Enter a lookup label for this specimen set that may help you to more easily find it again."
        ),
        Property(
            "origin",
            ['openminds.v2_0.controlled_terms.CellType', 'openminds.v2_0.controlled_terms.Organ'],
            "vocab:origin",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Source at which something begins or rises, or from which something derives.",
            instructions="Add the biogical origin (organ or cell type) of all tissue samples in this collection."
        ),
        Property(
            "phenotype",
            "openminds.v2_0.controlled_terms.Phenotype",
            "vocab:phenotype",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Physical expression of one or more genes of an organism.",
            instructions="Add the phenotype of all specimen in this set."
        ),
        Property(
            "quantity",
            int,
            "vocab:quantity",
            description="Total amount or number of things or beings.",
            instructions="Enter the number of specimen that belong to this set."
        ),
        Property(
            "species",
            "openminds.v2_0.controlled_terms.Species",
            "vocab:species",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.",
            instructions="Add the species of all specimen in this set."
        ),
        Property(
            "strain",
            "openminds.v2_0.controlled_terms.Strain",
            "vocab:strain",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Group of presumed common ancestry with physiological but usually not morphological distinctions.",
            instructions="Add the strain of all specimen in this set."
        ),
        Property(
            "studied_state",
            "openminds.v2_0.core.TissueSampleCollectionState",
            "vocab:studiedState",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Reference to a point in time at which something or someone was studied in a particular mode or condition.",
            instructions="Add all states in which this tissue sample collection was studied."
        ),
        Property(
            "type",
            "openminds.v2_0.controlled_terms.TissueSampleType",
            "vocab:type",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type of all tissue samples in this collection."
        ),
        
    ]

    def __init__(self, id=None, additional_remarks=None, biological_sex=None, internal_identifier=None, laterality=None, lookup_label=None, origin=None, phenotype=None, quantity=None, species=None, strain=None, studied_state=None, type=None):
        return super().__init__(id=id,additional_remarks=additional_remarks,biological_sex=biological_sex,internal_identifier=internal_identifier,laterality=laterality,lookup_label=lookup_label,origin=origin,phenotype=phenotype,quantity=quantity,species=species,strain=strain,studied_state=studied_state,type=type,)

