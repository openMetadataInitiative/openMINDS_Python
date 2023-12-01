"""
Structured information on a coordinate space.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class CoordinateSpace(LinkedMetadata):
    """
    Structured information on a coordinate space.
    """

    type_ = "https://openminds.ebrains.eu/sands/CoordinateSpace"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "anatomical_axes_orientation",
            "openminds.v1.controlled_terms.AnatomicalAxesOrientation",
            "anatomicalAxesOrientation",
            required=True,
            description="Relation between reference planes used in anatomy and mathematics.",
            instructions="Add the axes orientation denoted in standard anatomical terms of direction (stated as XYZ).",
        ),
        Property(
            "axes_origins",
            "openminds.v1.core.QuantitativeValue",
            "axesOrigin",
            multiple=True,
            unique_items=True,
            min_items=2,
            max_items=3,
            required=True,
            description="Special point in a coordinate system used as a fixed point of reference for the geometry of the surrounding space.",
            instructions="Enter the origin of the coordinate system (central point where axes intersect; 2D: [x, y] or 3D:[x, y, z]).",
        ),
        Property(
            "default_images",
            "openminds.v1.sands.Image",
            "defaultImage",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Two or three dimensional image that particluarly represents a specific coordinate space.",
            instructions="Add one or several images used as visual representation of this coordinate space.",
        ),
        Property(
            "digital_identifier",
            "openminds.v1.core.DigitalIdentifier",
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this coordinate space.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name for this coordinate space.",
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
            "native_unit",
            "openminds.v1.controlled_terms.UnitOfMeasurement",
            "nativeUnit",
            required=True,
            description="Determinate quantity used in the original measurement.",
            instructions="Add the native unit that is used for this coordinate space.",
        ),
        Property(
            "ontology_identifier",
            str,
            "ontologyIdentifier",
            formatting="text/plain",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the identifier (IRI) of the related ontological term matching this coordinate space.",
        ),
        Property(
            "release_date",
            str,
            "releaseDate",
            formatting="text/plain",
            required=True,
            description="Fixed date on which a product is due to become or was made available for the general public to see or buy",
            instructions="Enter the date of first publication of this coordinate space.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a descriptive short name for this coordinate space.",
        ),
        Property(
            "version_identifier",
            str,
            "versionIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this coordinate space.",
        ),
    ]

    def __init__(
        self,
        id=None,
        anatomical_axes_orientation=None,
        axes_origins=None,
        default_images=None,
        digital_identifier=None,
        full_name=None,
        homepage=None,
        native_unit=None,
        ontology_identifier=None,
        release_date=None,
        short_name=None,
        version_identifier=None,
    ):
        return super().__init__(
            id=id,
            anatomical_axes_orientation=anatomical_axes_orientation,
            axes_origins=axes_origins,
            default_images=default_images,
            digital_identifier=digital_identifier,
            full_name=full_name,
            homepage=homepage,
            native_unit=native_unit,
            ontology_identifier=ontology_identifier,
            release_date=release_date,
            short_name=short_name,
            version_identifier=version_identifier,
        )
