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
            "openminds.v1_0.core.SubjectGroupState",
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
        biological_sex=None,
        genotype=None,
        internal_identifier=None,
        phenotype=None,
        quantity=None,
        species=None,
        strain=None,
        studied_state=None,
    ):
        return super().__init__(
            id=id,
            biological_sex=biological_sex,
            genotype=genotype,
            internal_identifier=internal_identifier,
            phenotype=phenotype,
            quantity=quantity,
            species=species,
            strain=strain,
            studied_state=studied_state,
        )
