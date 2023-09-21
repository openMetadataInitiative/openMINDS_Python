"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI
from datetime import date

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
            "anatomical_axes_orientation",
            "openminds.v2_0.controlled_terms.AnatomicalAxesOrientation",
            "vocab:anatomicalAxesOrientation",required=True,
            description="Relation between reference planes used in anatomy and mathematics.",
            instructions="Add the axes orientation denoted in standard anatomical terms of direction (stated as XYZ) for this common coordinate space."
        ),
        Property(
            "axes_origin",
            "openminds.v2_0.core.QuantitativeValue",
            "vocab:axesOrigin",
            multiple=True,
            unique_items=True,
            min_items=2,
            max_items=3,
            required=True,
            description="Special point in a coordinate system used as a fixed point of reference for the geometry of the surrounding space.",
            instructions="Enter the origin of this common coordinate space (central point where axes intersect; 2D: [x, y] or 3D:[x, y, z])."
        ),
        Property(
            "default_image",
            "openminds.v2_0.core.File",
            "vocab:defaultImage",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            
            description="Two or three dimensional image that particluarly represents a specific coordinate space.",
            instructions="Add one or several image files used as visual representation of this common coordinate space."
        ),
        Property(
            "digital_identifier",
            "openminds.v2_0.core.DOI",
            "vocab:digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this common coordinate space."
        ),
        Property(
            "full_name",
            str,
            "vocab:fullName",formatting="text/plain",
            
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name for this common coordinate space."
        ),
        Property(
            "homepage",
            "openminds.v2_0.core.URL",
            "vocab:homepage",
            description="Main website of something or someone.",
            instructions="Add the uniform resource locator (URL) to the homepage of this common coordinate space."
        ),
        Property(
            "how_to_cite",
            str,
            "vocab:howToCite",formatting="text/markdown",
            multiline=True,
            
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this common coordinate space. Leave blank if citation text can be extracted from the assigned digital identifier."
        ),
        Property(
            "native_unit",
            "openminds.v2_0.controlled_terms.UnitOfMeasurement",
            "vocab:nativeUnit",required=True,
            description="Determinate quantity used in the original measurement.",
            instructions="Add the native unit that is used for this common coordinate space."
        ),
        Property(
            "ontology_identifier",
            IRI,
            "vocab:ontologyIdentifier",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the identifier (IRI) of the related ontological term matching this common coordinate space."
        ),
        Property(
            "release_date",
            date,
            "vocab:releaseDate",required=True,
            description="Fixed date on which a product is due to become or was made available for the general public to see or buy",
            instructions="Enter the date of first publication of this common coordinate space."
        ),
        Property(
            "short_name",
            str,
            "vocab:shortName",formatting="text/plain",
            
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a descriptive short name for this common coordinate space."
        ),
        Property(
            "version_identifier",
            str,
            "vocab:versionIdentifier",formatting="text/plain",
            
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this common coordinate space."
        ),
        
    ]

    def __init__(self, id=None, anatomical_axes_orientation=None, axes_origin=None, default_image=None, digital_identifier=None, full_name=None, homepage=None, how_to_cite=None, native_unit=None, ontology_identifier=None, release_date=None, short_name=None, version_identifier=None):
        return super().__init__(id=id,anatomical_axes_orientation=anatomical_axes_orientation,axes_origin=axes_origin,default_image=default_image,digital_identifier=digital_identifier,full_name=full_name,homepage=homepage,how_to_cite=how_to_cite,native_unit=native_unit,ontology_identifier=ontology_identifier,release_date=release_date,short_name=short_name,version_identifier=version_identifier,)

