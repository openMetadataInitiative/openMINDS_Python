"""
Structured information on a computational model (version level).
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class ModelVersion(LinkedMetadata):
    """
    Structured information on a computational model (version level).
    """
    type_ = ["https://openminds.ebrains.eu/core/ModelVersion"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "abstraction_level",
            "openminds.v1_0.controlled_terms.ModelAbstractionLevel",
            "vocab:abstractionLevel",required=True,
            description="Extent of simplification of physical, spatial, or temporal details or attributes in the study of objects or systems.",
            instructions="Add the abstraction level of this model version."
        ),
        Property(
            "accessibility",
            "openminds.v1_0.controlled_terms.ProductAccessibility",
            "vocab:accessibility",required=True,
            description="Level to which something is accessible to someone or something.",
            instructions="Add the accessibility of the data for this research product version."
        ),
        Property(
            "author",
            ['openminds.v1_0.core.Organization', 'openminds.v1_0.core.Person'],
            "vocab:author",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add one or several authors (person or organization) that contributed to the production and publication of this research product version."
        ),
        Property(
            "copyright",
            "openminds.v1_0.core.Copyright",
            "vocab:copyright",
            description="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
            instructions="Add the copyright information of this research product version."
        ),
        Property(
            "custodian",
            ['openminds.v1_0.core.Organization', 'openminds.v1_0.core.Person'],
            "vocab:custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add one or several custodians (person or organization) that are responsible for this research product version."
        ),
        Property(
            "description",
            str,
            "vocab:description",formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description (abstract) for this research product (max. 2000 characters, incl. spaces; no references)."
        ),
        Property(
            "developer",
            ['openminds.v1_0.core.Organization', 'openminds.v1_0.core.Person'],
            "vocab:developer",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Legal person that creates or improves products or services (e.g., software, applications, etc.).",
            instructions="Add one or several developers (person or organization) that contributed to the code implementation of this research product version."
        ),
        Property(
            "digital_identifier",
            "openminds.v1_0.core.DigitalIdentifier",
            "vocab:digitalIdentifier",required=True,
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product version."
        ),
        Property(
            "format",
            "openminds.v1_0.core.ContentType",
            "vocab:format",required=True,
            description="Method of digitally organizing and structuring data or information.",
            instructions="Add the used content type of this model version."
        ),
        Property(
            "full_documentation",
            "openminds.v1_0.core.DigitalIdentifier",
            "vocab:fullDocumentation",required=True,
            description="Non-abridged instructions, comments, and information for using a particular product.",
            instructions="Add the globally unique and persistent digital identifier of a full documentation of this research product version."
        ),
        Property(
            "full_name",
            str,
            "vocab:fullName",formatting="text/plain",
            
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (title) for this research product version."
        ),
        Property(
            "funding",
            "openminds.v1_0.core.Funding",
            "vocab:funding",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Money provided by a legal person for a particular purpose.",
            instructions="Add all funding information of this research product version."
        ),
        Property(
            "has_alternative_version",
            "openminds.v1_0.core.ModelVersion",
            "vocab:hasAlternativeVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add all model versions that can be used alternatively to this model version."
        ),
        Property(
            "has_supplement_version",
            "openminds.v1_0.core.ModelVersion",
            "vocab:hasSupplementVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add all model versions that supplement this model version."
        ),
        Property(
            "homepage",
            str,
            "vocab:homepage",formatting="text/plain",
            
            
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product version."
        ),
        Property(
            "input_data",
            "openminds.v1_0.core.DigitalIdentifier",
            "vocab:inputData",
            description="Data that is put into a process or machine.",
            instructions="Add the data that was used as input for this model version."
        ),
        Property(
            "is_new_version_of",
            "openminds.v1_0.core.ModelVersion",
            "vocab:isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the model version preceding this model version."
        ),
        Property(
            "keyword",
            str,
            "vocab:keyword",
            multiple=True,
            unique_items=True,
            min_items=1,
            max_items=5,
            formatting="text/plain",
            
            
            description="Significant word or concept that are representative of something or someone.",
            instructions="Enter custom keywords to this research product version."
        ),
        Property(
            "license",
            "openminds.v1_0.core.License",
            "vocab:license",required=True,
            description="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
            instructions="Add the license of this research product version."
        ),
        Property(
            "other_contribution",
            "openminds.v1_0.core.Contribution",
            "vocab:otherContribution",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.",
            instructions="Add the contributions for each involved person or organization going beyond being an author, custodian or developer of this research product version."
        ),
        Property(
            "output_data",
            "openminds.v1_0.core.DigitalIdentifier",
            "vocab:outputData",
            description="Data that comes out of, is delivered or produced by a process or machine.",
            instructions="Add the data that was generated as output of this model version."
        ),
        Property(
            "related_publication",
            "openminds.v1_0.core.DigitalIdentifier",
            "vocab:relatedPublication",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Reference to something that was made available for the general public to see or buy.",
            instructions="Add further publications besides the documentation (e.g. an original research article) providing the original context for the production of this research product version."
        ),
        Property(
            "release_date",
            str,
            "vocab:releaseDate",formatting="text/plain",
            
            required=True,
            description="Fixed date on which a product is due to become or was made available for the general public to see or buy",
            instructions="Enter the date (actual or intended) of the first broadcast/publication of this research product version."
        ),
        Property(
            "repository",
            "openminds.v1_0.core.FileRepository",
            "vocab:repository",required=True,
            description="Place, room, or container where something is deposited or stored.",
            instructions="Add the file repository of this research product version."
        ),
        Property(
            "scope",
            "openminds.v1_0.controlled_terms.ModelScope",
            "vocab:scope",required=True,
            description="Extent of something.",
            instructions="Add the scope of this model version."
        ),
        Property(
            "short_name",
            str,
            "vocab:shortName",formatting="text/plain",
            
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (alias) for this research product version (max. 30 characters, no space)."
        ),
        Property(
            "study_target",
            ['openminds.v1_0.controlled_terms.BiologicalSex', 'openminds.v1_0.controlled_terms.Disease', 'openminds.v1_0.controlled_terms.Genotype', 'openminds.v1_0.controlled_terms.Phenotype', 'openminds.v1_0.controlled_terms.Species', 'openminds.v1_0.controlled_terms.TermSuggestion', 'openminds.v1_0.sands.AnatomicalEntity'],
            "vocab:studyTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Structure or function that was targeted within a study.",
            instructions="Add all study targets of this model version."
        ),
        Property(
            "version_identifier",
            str,
            "vocab:versionIdentifier",formatting="text/plain",
            
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this research product version."
        ),
        Property(
            "version_innovation",
            str,
            "vocab:versionInnovation",formatting="text/markdown",
            multiline=True,
            
            description="Documentation on what changed in comparison to a previously published form of something.",
            instructions="Enter a short summary of the novelties/peculiarities of this research product version."
        ),
        
    ]

    def __init__(self, id=None, abstraction_level=None, accessibility=None, author=None, copyright=None, custodian=None, description=None, developer=None, digital_identifier=None, format=None, full_documentation=None, full_name=None, funding=None, has_alternative_version=None, has_supplement_version=None, homepage=None, input_data=None, is_new_version_of=None, keyword=None, license=None, other_contribution=None, output_data=None, related_publication=None, release_date=None, repository=None, scope=None, short_name=None, study_target=None, version_identifier=None, version_innovation=None):
        return super().__init__(id=id,abstraction_level=abstraction_level,accessibility=accessibility,author=author,copyright=copyright,custodian=custodian,description=description,developer=developer,digital_identifier=digital_identifier,format=format,full_documentation=full_documentation,full_name=full_name,funding=funding,has_alternative_version=has_alternative_version,has_supplement_version=has_supplement_version,homepage=homepage,input_data=input_data,is_new_version_of=is_new_version_of,keyword=keyword,license=license,other_contribution=other_contribution,output_data=output_data,related_publication=related_publication,release_date=release_date,repository=repository,scope=scope,short_name=short_name,study_target=study_target,version_identifier=version_identifier,version_innovation=version_innovation,)

