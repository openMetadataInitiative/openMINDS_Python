"""
Structured information on a brain atlas (version level).
"""

# this file was auto-generated!

from datetime import date
from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class BrainAtlasVersion(LinkedMetadata):
    """
    Structured information on a brain atlas (version level).
    """

    type_ = "https://openminds.ebrains.eu/sands/BrainAtlasVersion"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "coordinate_space",
            "openminds.v2.sands.CommonCoordinateSpace",
            "coordinateSpace",
            required=True,
            description="Two or three dimensional geometric setting.",
            instructions="Add the common coordinate space in which this brain atlas version exists in.",
        ),
        Property(
            "digital_identifier",
            "openminds.v2.core.DOI",
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this brain atlas version.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name for this brain atlas version.",
        ),
        Property(
            "has_terminology",
            "openminds.v2.sands.parcellationTerminology",
            "hasTerminology",
            required=True,
            description="no description available",
            instructions="Add the parcellation terminology for this brain atlas version.",
        ),
        Property(
            "homepage",
            "openminds.v2.core.URL",
            "homepage",
            description="Main website of something or someone.",
            instructions="Add the uniform resource locator (URL) to the homepage of this brain atlas version.",
        ),
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this brain atlas version. Leave blank if citation text can be extracted from the assigned digital identifier.",
        ),
        Property(
            "is_alternative_version_of",
            "openminds.v2.sands.BrainAtlasVersion",
            "isAlternativeVersionOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an original form where the essence was preserved, but presented in an alternative form.",
            instructions="Add one or several alternative versions to this brain atlas version.",
        ),
        Property(
            "is_new_version_of",
            "openminds.v2.sands.BrainAtlasVersion",
            "isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the earlier version of this brain atlas version.",
        ),
        Property(
            "ontology_identifier",
            IRI,
            "ontologyIdentifier",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the identifier (IRI) of the related ontological term matching this brain atlas version.",
        ),
        Property(
            "release_date",
            date,
            "releaseDate",
            required=True,
            description="Fixed date on which a product is due to become or was made available for the general public to see or buy",
            instructions="Enter the date of first publication of this brain atlas version.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a descriptive short name for this brain atlas version.",
        ),
        Property(
            "version_identifier",
            str,
            "versionIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this brain atlas version.",
        ),
        Property(
            "version_innovation",
            str,
            "versionInnovation",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Documentation on what changed in comparison to a previously published form of something.",
            instructions="Enter a short description of the novelties/peculiarities of this brain atlas version.",
        ),
    ]

    def __init__(
        self,
        id=None,
        coordinate_space=None,
        digital_identifier=None,
        full_name=None,
        has_terminology=None,
        homepage=None,
        how_to_cite=None,
        is_alternative_version_of=None,
        is_new_version_of=None,
        ontology_identifier=None,
        release_date=None,
        short_name=None,
        version_identifier=None,
        version_innovation=None,
    ):
        return super().__init__(
            id=id,
            coordinate_space=coordinate_space,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_terminology=has_terminology,
            homepage=homepage,
            how_to_cite=how_to_cite,
            is_alternative_version_of=is_alternative_version_of,
            is_new_version_of=is_new_version_of,
            ontology_identifier=ontology_identifier,
            release_date=release_date,
            short_name=short_name,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )
