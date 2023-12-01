"""
Structured information on a brain atlas (version level).
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class BrainAtlasVersion(LinkedMetadata):
    """
    Structured information on a brain atlas (version level).
    """

    type_ = "https://openminds.ebrains.eu/sands/BrainAtlasVersion"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "annotation_sets",
            "openminds.v1.sands.Annotation",
            "annotationSet",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Collection of notes or markings, each added by way of comment or explanation.",
            instructions="Add all annotations that belong to this brain atlas version.",
        ),
        Property(
            "coordinate_space",
            "openminds.v1.sands.CoordinateSpace",
            "coordinateSpace",
            required=True,
            description="Two or three dimensional geometric setting.",
            instructions="Add the coordinate space in which this brain atlas version exists in.",
        ),
        Property(
            "digital_identifier",
            "openminds.v1.core.DigitalIdentifier",
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
            "has_alternative_versions",
            "openminds.v1.sands.BrainAtlasVersion",
            "hasAlternativeVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add one or several alternative versions to this brain atlas version.",
        ),
        Property(
            "homepage",
            str,
            "homepage",
            formatting="text/plain",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this brain atlas.",
        ),
        Property(
            "is_new_version_of",
            "openminds.v1.sands.BrainAtlasVersion",
            "isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the earlier version of this brain atlas version.",
        ),
        Property(
            "ontology_identifier",
            str,
            "ontologyIdentifier",
            formatting="text/plain",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the identifier (IRI) of the related ontological term matching this brain atlas version.",
        ),
        Property(
            "release_date",
            str,
            "releaseDate",
            formatting="text/plain",
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
            "terminology",
            "openminds.v1.sands.AtlasTerminology",
            "terminology",
            required=True,
            description="Nomenclature for a particular field of study.",
            instructions="Add the terminology used for this brain atlas version.",
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
        annotation_sets=None,
        coordinate_space=None,
        digital_identifier=None,
        full_name=None,
        has_alternative_versions=None,
        homepage=None,
        is_new_version_of=None,
        ontology_identifier=None,
        release_date=None,
        short_name=None,
        terminology=None,
        version_identifier=None,
        version_innovation=None,
    ):
        return super().__init__(
            id=id,
            annotation_sets=annotation_sets,
            coordinate_space=coordinate_space,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_alternative_versions=has_alternative_versions,
            homepage=homepage,
            is_new_version_of=is_new_version_of,
            ontology_identifier=ontology_identifier,
            release_date=release_date,
            short_name=short_name,
            terminology=terminology,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )
