"""
Structured information on a tissue sample.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class TissueSample(LinkedMetadata):
    """
    Structured information on a tissue sample.
    """

    type_ = "https://openminds.ebrains.eu/core/TissueSample"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "biological_sex",
            "openminds.v1.controlled_terms.BiologicalSex",
            "biologicalSex",
            required=True,
            description="Differentiation of individuals of most species (animals and plants) based on the type of gametes they produce.",
            instructions="Add the biological sex of this specimen.",
        ),
        Property(
            "genotype",
            "openminds.v1.controlled_terms.Genotype",
            "genotype",
            description="Genetic constitution of an individual or group.",
            instructions="Add the genotype of this specimen.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier of this specimen that is used within the corresponding data.",
        ),
        Property(
            "lateralities",
            "openminds.v1.controlled_terms.Laterality",
            "laterality",
            multiple=True,
            unique_items=True,
            min_items=1,
            max_items=2,
            description="Differentiation between a pair of lateral homologous parts of the body.",
            instructions="Add one or both hemisphere sides from which this tissue sample originates from.",
        ),
        Property(
            "origin",
            ["openminds.v1.controlled_terms.CellType", "openminds.v1.controlled_terms.Organ"],
            "origin",
            required=True,
            description="Source at which something begins or rises, or from which something derives.",
            instructions="Add the biogical origin (organ or cell type) of this tissue sample.",
        ),
        Property(
            "phenotype",
            "openminds.v1.controlled_terms.Phenotype",
            "phenotype",
            description="Physical expression of one or more genes of an organism.",
            instructions="Add the phenotype of this specimen.",
        ),
        Property(
            "species",
            "openminds.v1.controlled_terms.Species",
            "species",
            required=True,
            description="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.",
            instructions="Add the species of this specimen.",
        ),
        Property(
            "strain",
            "openminds.v1.controlled_terms.Strain",
            "strain",
            description="Group of presumed common ancestry with physiological but usually not morphological distinctions.",
            instructions="Add the strain of this specimen.",
        ),
        Property(
            "studied_states",
            "openminds.v1.core.TissueSampleState",
            "studiedState",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to a point in time at which something or someone was studied in a particular mode or condition.",
            instructions="Add all states in which this tissue sample was studied.",
        ),
        Property(
            "type",
            "openminds.v1.controlled_terms.TissueSampleType",
            "type",
            required=True,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type of this tissue sample.",
        ),
    ]

    def __init__(
        self,
        id=None,
        biological_sex=None,
        genotype=None,
        internal_identifier=None,
        lateralities=None,
        origin=None,
        phenotype=None,
        species=None,
        strain=None,
        studied_states=None,
        type=None,
    ):
        return super().__init__(
            id=id,
            biological_sex=biological_sex,
            genotype=genotype,
            internal_identifier=internal_identifier,
            lateralities=lateralities,
            origin=origin,
            phenotype=phenotype,
            species=species,
            strain=strain,
            studied_states=studied_states,
            type=type,
        )
