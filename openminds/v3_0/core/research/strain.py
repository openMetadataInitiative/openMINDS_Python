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

    type_ = ["https://openminds.ebrains.eu/core/Strain"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "alternate_identifier",
            str,
            "vocab:alternateIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all identifiers for this strain, excluding its ontological identifers or RRID (e.g., identifiers from the Mouse Genome Informatics (MGI) database or Rat Genome Database (RGD)).",
        ),
        Property(
            "background_strain",
            "openminds.v3_0.core.Strain",
            "vocab:backgroundStrain",
            multiple=True,
            unique_items=True,
            min_items=1,
            max_items=2,
            description="no description available",
            instructions="Add the background strain that explains the majority of the genetic background and/or causes the majority of the prominent traits. If two strains contributed equally, state both.",
        ),
        Property(
            "breeding_type",
            "openminds.v3_0.controlled_terms.BreedingType",
            "vocab:breedingType",
            description="no description available",
            instructions="Add the breeding type for this strain.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a short text describing this strain.",
        ),
        Property(
            "digital_identifier",
            "openminds.v3_0.core.RRID",
            "vocab:digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the 'Research Resource Identifier' (RRID) of this strain.",
        ),
        Property(
            "disease_model",
            ["openminds.v3_0.controlled_terms.Disease", "openminds.v3_0.controlled_terms.DiseaseModel"],
            "vocab:diseaseModel",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all (human) diseases and/or conditions that this strain is a model for.",
        ),
        Property(
            "genetic_strain_type",
            "openminds.v3_0.controlled_terms.GeneticStrainType",
            "vocab:geneticStrainType",
            required=True,
            description="no description available",
            instructions="Add the genetic background type of this strain.",
        ),
        Property(
            "laboratory_code",
            str,
            "vocab:laboratoryCode",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the laboratory code assigned by the Institute of Laboratory Animal Research (ILAR) for the investigator or organization that has created this strain following the defined pattern (e.g., Aaa).",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this strain.",
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
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this strain.",
        ),
        Property(
            "phenotype",
            str,
            "vocab:phenotype",
            formatting="text/plain",
            description="Physical expression of one or more genes of an organism.",
            instructions="Enter a short description for the phenotype of this strain.",
        ),
        Property(
            "species",
            "openminds.v3_0.controlled_terms.Species",
            "vocab:species",
            required=True,
            description="Category of biological classification comprising related organisms or populations potentially capable of interbreeding, and being designated by a binomial that consists of the name of a genus followed by a Latin or latinized uncapitalized noun or adjective.",
            instructions="Add the species of this strain.",
        ),
        Property(
            "stock_number",
            "openminds.v3_0.core.StockNumber",
            "vocab:stockNumber",
            description="no description available",
            instructions="Add the stock number from the vendor the strain was supplied from/is in stock at.",
        ),
        Property(
            "synonym",
            str,
            "vocab:synonym",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
            instructions="Enter any synonyms (inlcuding abbreviations) of this strain.",
        ),
    ]

    def __init__(
        self,
        id=None,
        alternate_identifier=None,
        background_strain=None,
        breeding_type=None,
        description=None,
        digital_identifier=None,
        disease_model=None,
        genetic_strain_type=None,
        laboratory_code=None,
        name=None,
        ontology_identifier=None,
        phenotype=None,
        species=None,
        stock_number=None,
        synonym=None,
    ):
        return super().__init__(
            id=id,
            alternate_identifier=alternate_identifier,
            background_strain=background_strain,
            breeding_type=breeding_type,
            description=description,
            digital_identifier=digital_identifier,
            disease_model=disease_model,
            genetic_strain_type=genetic_strain_type,
            laboratory_code=laboratory_code,
            name=name,
            ontology_identifier=ontology_identifier,
            phenotype=phenotype,
            species=species,
            stock_number=stock_number,
            synonym=synonym,
        )
