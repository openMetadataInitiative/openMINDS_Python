"""
Structured information on a software tool (concept level).
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class Software(LinkedMetadata):
    """
    Structured information on a software tool (concept level).
    """
    type_ = ["https://openminds.ebrains.eu/core/Software"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "custodian",
            ['openminds.v2_0.core.Organization', 'openminds.v2_0.core.Person'],
            "vocab:custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add one or several custodians (person or organization) that are responsible for this research product. Note that this custodian will be responsible for all attached research product versions."
        ),
        Property(
            "description",
            str,
            "vocab:description",formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description (abstract) for this research product (max. 2000 characters, incl. spaces; no references). Note that this description should be fitting for all attached research product versions."
        ),
        Property(
            "developer",
            ['openminds.v2_0.core.Organization', 'openminds.v2_0.core.Person'],
            "vocab:developer",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Legal person that creates or improves products or services (e.g., software, applications, etc.).",
            instructions="Add one or several developers (person or organization) that contributed to the code implementation of this software."
        ),
        Property(
            "digital_identifier",
            ['openminds.v2_0.core.DOI', 'openminds.v2_0.core.SWHID'],
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
            instructions="Enter a descriptive full name (title) for this research product.  Note that this full name should be fitting for all attached research product versions."
        ),
        Property(
            "has_version",
            "openminds.v2_0.core.SoftwareVersion",
            "vocab:hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Reference to variants of an original.",
            instructions="Add one or several versions of this software tool."
        ),
        Property(
            "homepage",
            "openminds.v2_0.core.URL",
            "vocab:homepage",
            description="Main website of something or someone.",
            instructions="Add the uniform resource locator (URL) to the homepage of this research product."
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
            "short_name",
            str,
            "vocab:shortName",formatting="text/plain",
            
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (alias) for this research product (max. 30 characters; no space)."
        ),
        
    ]

    def __init__(self, id=None, custodian=None, description=None, developer=None, digital_identifier=None, full_name=None, has_version=None, homepage=None, how_to_cite=None, short_name=None):
        return super().__init__(id=id,custodian=custodian,description=description,developer=developer,digital_identifier=digital_identifier,full_name=full_name,has_version=has_version,homepage=homepage,how_to_cite=how_to_cite,short_name=short_name,)

