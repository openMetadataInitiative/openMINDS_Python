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

    type_ = "https://openminds.ebrains.eu/core/TissueSampleCollection"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "biological_sex",
            "openminds.v1_0.controlled_terms.BiologicalSex",
            "biologicalSex",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.",
            instructions="Add the biological sex of all specimen in this set.",
        ),
        Property(
            "genotype",
            "openminds.v1_0.controlled_terms.Genotype",
            "genotype",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Genetic constitution of an individual or group.",
            instructions="Add the genotype of all specimen in this set.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier of this specimen set that is used within the corresponding data.",
        ),
        Property(
            "laterality",
            "openminds.v1_0.controlled_terms.Laterality",
            "laterality",
            multiple=True,
            unique_items=True,
            min_items=1,
            max_items=2,
            description="Differentiation between a pair of lateral homologous parts of the body.",
            instructions="Add one or both hemisphere sides from which the tissue samples in this collection originate from.",
        ),
        Property(
            "origin",
            ["openminds.v1_0.controlled_terms.CellType", "openminds.v1_0.controlled_terms.Organ"],
            "origin",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Source at which something begins or rises, or from which something derives.",
            instructions="Add the biogical origin (organ or cell type) of all tissue samples in this collection.",
        ),
        Property(
            "phenotype",
            "openminds.v1_0.controlled_terms.Phenotype",
            "phenotype",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Physical expression of one or more genes of an organism.",
            instructions="Add the phenotype of all specimen in this set.",
        ),
        Property(
            "quantity",
            int,
            "quantity",
            description="Total amount or number of things or beings.",
            instructions="Enter the number of specimen that belong to this set.",
        ),
        Property(
            "species",
            "openminds.v1_0.controlled_terms.Species",
            "species",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.",
            instructions="Add the species of all specimen in this set.",
        ),
        Property(
            "strain",
            "openminds.v1_0.controlled_terms.Strain",
            "strain",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Group of presumed common ancestry with physiological but usually not morphological distinctions.",
            instructions="Add the strain of all specimen in this set.",
        ),
        Property(
            "studied_state",
            "openminds.v1_0.core.TissueSampleCollectionState",
            "studiedState",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to a point in time at which something or someone was studied in a particular mode or condition.",
            instructions="Add all states in which this tissue sample collection was studied.",
        ),
        Property(
            "type",
            "openminds.v1_0.controlled_terms.TissueSampleType",
            "type",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type of all tissue samples in this collection.",
        ),
    ]

    def __init__(
        self,
        id=None,
        biological_sex=None,
        genotype=None,
        internal_identifier=None,
        laterality=None,
        origin=None,
        phenotype=None,
        quantity=None,
        species=None,
        strain=None,
        studied_state=None,
        type=None,
    ):
        return super().__init__(
            id=id,
            biological_sex=biological_sex,
            genotype=genotype,
            internal_identifier=internal_identifier,
            laterality=laterality,
            origin=origin,
            phenotype=phenotype,
            quantity=quantity,
            species=species,
            strain=strain,
            studied_state=studied_state,
            type=type,
        )
