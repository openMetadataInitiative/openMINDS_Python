"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class SubjectGroup(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/SubjectGroup"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "biological_sexes",
            "openminds.v1.controlled_terms.BiologicalSex",
            "biologicalSex",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.",
            instructions="Add the biological sex of all specimen in this set.",
        ),
        Property(
            "genotypes",
            "openminds.v1.controlled_terms.Genotype",
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
            "phenotypes",
            "openminds.v1.controlled_terms.Phenotype",
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
            "openminds.v1.controlled_terms.Species",
            "species",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.",
            instructions="Add the species of all specimen in this set.",
        ),
        Property(
            "strains",
            "openminds.v1.controlled_terms.Strain",
            "strain",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Group of presumed common ancestry with physiological but usually not morphological distinctions.",
            instructions="Add the strain of all specimen in this set.",
        ),
        Property(
            "studied_states",
            "openminds.v1.core.SubjectGroupState",
            "studiedState",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to a point in time at which something or someone was studied in a particular mode or condition.",
            instructions="Add all states in which this subject group was studied.",
        ),
    ]

    def __init__(
        self,
        id=None,
        biological_sexes=None,
        genotypes=None,
        internal_identifier=None,
        phenotypes=None,
        quantity=None,
        species=None,
        strains=None,
        studied_states=None,
    ):
        return super().__init__(
            id=id,
            biological_sexes=biological_sexes,
            genotypes=genotypes,
            internal_identifier=internal_identifier,
            phenotypes=phenotypes,
            quantity=quantity,
            species=species,
            strains=strains,
            studied_states=studied_states,
        )
