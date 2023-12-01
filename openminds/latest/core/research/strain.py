"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Strain(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/Strain"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "alternate_identifiers",
            str,
            "alternateIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all identifiers for this strain, excluding its ontological identifiers or RRID (e.g., identifiers from the Mouse Genome Informatics (MGI) database or Rat Genome Database (RGD)).",
        ),
        Property(
            "background_strains",
            "openminds.latest.core.Strain",
            "backgroundStrain",
            multiple=True,
            unique_items=True,
            min_items=1,
            max_items=2,
            description="no description available",
            instructions="Add the background strain that explains the majority of the genetic background and/or causes the majority of the prominent traits. If two strains contributed equally, state both.",
        ),
        Property(
            "breeding_type",
            "openminds.latest.controlled_terms.BreedingType",
            "breedingType",
            description="no description available",
            instructions="Add the breeding type for this strain.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a short text describing this strain.",
        ),
        Property(
            "digital_identifier",
            "openminds.latest.core.RRID",
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the 'Research Resource Identifier' (RRID) of this strain.",
        ),
        Property(
            "disease_models",
            ["openminds.latest.controlled_terms.Disease", "openminds.latest.controlled_terms.DiseaseModel"],
            "diseaseModel",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all (human) diseases and/or conditions that this strain is a model for.",
        ),
        Property(
            "genetic_strain_type",
            "openminds.latest.controlled_terms.GeneticStrainType",
            "geneticStrainType",
            required=True,
            description="no description available",
            instructions="Add the genetic background type of this strain.",
        ),
        Property(
            "laboratory_code",
            str,
            "laboratoryCode",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the laboratory code assigned by the Institute of Laboratory Animal Research (ILAR) for the investigator or organization that has created this strain following the defined pattern (e.g., Aaa).",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this strain.",
        ),
        Property(
            "ontology_identifiers",
            str,
            "ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this strain.",
        ),
        Property(
            "phenotype",
            str,
            "phenotype",
            formatting="text/plain",
            description="Physical expression of one or more genes of an organism.",
            instructions="Enter a short description for the phenotype of this strain.",
        ),
        Property(
            "species",
            "openminds.latest.controlled_terms.Species",
            "species",
            required=True,
            description="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.",
            instructions="Add the species of this strain.",
        ),
        Property(
            "stock_number",
            "openminds.latest.core.StockNumber",
            "stockNumber",
            description="no description available",
            instructions="Add the stock number from the vendor the strain was supplied from/is in stock at.",
        ),
        Property(
            "synonyms",
            str,
            "synonym",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
            instructions="Enter any synonyms (including abbreviations) of this strain.",
        ),
    ]

    def __init__(
        self,
        id=None,
        alternate_identifiers=None,
        background_strains=None,
        breeding_type=None,
        description=None,
        digital_identifier=None,
        disease_models=None,
        genetic_strain_type=None,
        laboratory_code=None,
        name=None,
        ontology_identifiers=None,
        phenotype=None,
        species=None,
        stock_number=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            alternate_identifiers=alternate_identifiers,
            background_strains=background_strains,
            breeding_type=breeding_type,
            description=description,
            digital_identifier=digital_identifier,
            disease_models=disease_models,
            genetic_strain_type=genetic_strain_type,
            laboratory_code=laboratory_code,
            name=name,
            ontology_identifiers=ontology_identifiers,
            phenotype=phenotype,
            species=species,
            stock_number=stock_number,
            synonyms=synonyms,
        )
