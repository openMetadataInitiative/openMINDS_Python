"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class CommonCoordinateSpace(LinkedMetadata):
    """
    <description not available>
    """
    type_ = ["https://openminds.ebrains.eu/sands/CommonCoordinateSpace"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "abbreviation",
            str,
            "vocab:abbreviation",formatting="text/plain",
            
            
            description="no description available",
            instructions="Enter the official abbreviation of this common coordinate space."
        ),
        Property(
            "author",
            ['openminds.latest.core.Consortium', 'openminds.latest.core.Organization', 'openminds.latest.core.Person'],
            "vocab:author",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this common coordinate space as authors."
        ),
        Property(
            "custodian",
            ['openminds.latest.core.Consortium', 'openminds.latest.core.Organization', 'openminds.latest.core.Person'],
            "vocab:custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for this research product (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product. Unless specified differently, this custodian will be responsible for all attached research product versions."
        ),
        Property(
            "description",
            str,
            "vocab:description",formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description (or abstract) of this research product. Note that this should be a suitable description for all attached research product versions."
        ),
        Property(
            "digital_identifier",
            ['openminds.latest.core.DOI', 'openminds.latest.core.ISBN', 'openminds.latest.core.RRID'],
            "vocab:digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions."
        ),
        Property(
            "full_name",
            str,
            "vocab:fullName",formatting="text/plain",
            
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (or title) for this research product. Note that this should be a suitable full name for all attached research product versions."
        ),
        Property(
            "has_version",
            "openminds.latest.sands.CommonCoordinateSpaceVersion",
            "vocab:hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Reference to variants of an original.",
            instructions="Add all versions of this common coordinate space."
        ),
        Property(
            "homepage",
            IRI,
            "vocab:homepage",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product."
        ),
        Property(
            "how_to_cite",
            str,
            "vocab:howToCite",formatting="text/markdown",
            multiline=True,
            
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier."
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
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this common coordinate space."
        ),
        Property(
            "short_name",
            str,
            "vocab:shortName",formatting="text/plain",
            
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name)."
        ),
        Property(
            "used_species",
            "openminds.latest.controlled_terms.Species",
            "vocab:usedSpecies",required=True,
            description="no description available",
            instructions="Add the species that was used for the creation of this common coordinate space."
        ),
        
    ]

    def __init__(self, id=None, abbreviation=None, author=None, custodian=None, description=None, digital_identifier=None, full_name=None, has_version=None, homepage=None, how_to_cite=None, ontology_identifier=None, short_name=None, used_species=None):
        return super().__init__(id=id,abbreviation=abbreviation,author=author,custodian=custodian,description=description,digital_identifier=digital_identifier,full_name=full_name,has_version=has_version,homepage=homepage,how_to_cite=how_to_cite,ontology_identifier=ontology_identifier,short_name=short_name,used_species=used_species,)

