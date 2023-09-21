"""
<description not available>
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class SoftwareVersion(LinkedMetadata):
    """
    <description not available>
    """
    type_ = ["https://openminds.ebrains.eu/core/SoftwareVersion"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "accessibility",
            "openminds.v1_0.controlled_terms.ProductAccessibility",
            "vocab:accessibility",required=True,
            description="Level to which something is accessible to someone or something.",
            instructions="Add the accessibility of the data for this research product version."
        ),
        Property(
            "application_category",
            "openminds.v1_0.controlled_terms.SoftwareApplicationCategory",
            "vocab:applicationCategory",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Distinct class that groups software programs which perform a similar task or set of tasks.",
            instructions="Add all categories to which this software version belongs."
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
            "device",
            "openminds.v1_0.controlled_terms.OperatingDevice",
            "vocab:device",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Piece of equipment or mechanism (hardware) designed to serve a special purpose or perform a special function.",
            instructions="Add all hardware devices compatible with this software version."
        ),
        Property(
            "digital_identifier",
            "openminds.v1_0.core.DigitalIdentifier",
            "vocab:digitalIdentifier",required=True,
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product version."
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
            "openminds.v1_0.core.SoftwareVersion",
            "vocab:hasAlternativeVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add all software versions that can be used alternatively to this software version."
        ),
        Property(
            "has_feature",
            "openminds.v1_0.controlled_terms.SoftwareFeature",
            "vocab:hasFeature",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="no description available",
            instructions="Add all features of this software version."
        ),
        Property(
            "has_requirement",
            str,
            "vocab:hasRequirement",formatting="text/plain",
            
            required=True,
            description="no description available",
            instructions="Enter all requirements of this software version."
        ),
        Property(
            "has_supplement_version",
            "openminds.v1_0.core.SoftwareVersion",
            "vocab:hasSupplementVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="no description available",
            instructions="Add all software versions that supplement this software version."
        ),
        Property(
            "homepage",
            str,
            "vocab:homepage",formatting="text/plain",
            
            
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product version."
        ),
        Property(
            "input_format",
            "openminds.v1_0.core.ContentType",
            "vocab:inputFormat",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Format of data that is put into a process or machine.",
            instructions="Add the content types of all possible input formats for this software version."
        ),
        Property(
            "is_new_version_of",
            "openminds.v1_0.core.SoftwareVersion",
            "vocab:isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the software version preceding this software version."
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
            "language",
            "openminds.v1_0.controlled_terms.Language",
            "vocab:language",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="System of communication (words, their pronunciation, and the methods of combining them) used and understood by a particular community.",
            instructions="Add all languages supported by this software version."
        ),
        Property(
            "license",
            "openminds.v1_0.core.License",
            "vocab:license",required=True,
            description="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
            instructions="Add the license of this research product version."
        ),
        Property(
            "operating_system",
            "openminds.v1_0.controlled_terms.OperatingSystem",
            "vocab:operatingSystem",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Software that controls the operation of a computer and directs the processing of programs.",
            instructions="Add all operating systems supported by this software version."
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
            "output_format",
            "openminds.v1_0.core.ContentType",
            "vocab:outputFormat",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Format of data that comes out of, is delivered or produced by a process or machine.",
            instructions="Add the content types of all possible input formats for this software version."
        ),
        Property(
            "programming_language",
            "openminds.v1_0.controlled_terms.ProgrammingLanguage",
            "vocab:programmingLanguage",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Distinct set of instructions for computer programs in order to produce various kinds of output.",
            instructions="Add all programming languages used for this software version."
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
            "short_name",
            str,
            "vocab:shortName",formatting="text/plain",
            
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (alias) for this research product version (max. 30 characters, no space)."
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

    def __init__(self, id=None, accessibility=None, application_category=None, author=None, copyright=None, custodian=None, description=None, developer=None, device=None, digital_identifier=None, full_documentation=None, full_name=None, funding=None, has_alternative_version=None, has_feature=None, has_requirement=None, has_supplement_version=None, homepage=None, input_format=None, is_new_version_of=None, keyword=None, language=None, license=None, operating_system=None, other_contribution=None, output_format=None, programming_language=None, related_publication=None, release_date=None, repository=None, short_name=None, version_identifier=None, version_innovation=None):
        return super().__init__(id=id,accessibility=accessibility,application_category=application_category,author=author,copyright=copyright,custodian=custodian,description=description,developer=developer,device=device,digital_identifier=digital_identifier,full_documentation=full_documentation,full_name=full_name,funding=funding,has_alternative_version=has_alternative_version,has_feature=has_feature,has_requirement=has_requirement,has_supplement_version=has_supplement_version,homepage=homepage,input_format=input_format,is_new_version_of=is_new_version_of,keyword=keyword,language=language,license=license,operating_system=operating_system,other_contribution=other_contribution,output_format=output_format,programming_language=programming_language,related_publication=related_publication,release_date=release_date,repository=repository,short_name=short_name,version_identifier=version_identifier,version_innovation=version_innovation,)

