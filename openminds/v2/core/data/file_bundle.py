"""
Structured information on a bundle of file instances.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class FileBundle(LinkedMetadata):
    """
    Structured information on a bundle of file instances.
    """

    type_ = "https://openminds.ebrains.eu/core/FileBundle"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "format",
            "openminds.v2.core.ContentType",
            "format",
            description="Method of digitally organizing and structuring data or information.",
            instructions="If file instances within this bundle are organized and formatted according to a formal data structure use the appropriate contentType. Leave blank otherwise.",
        ),
        Property(
            "grouped_by",
            "openminds.v2.controlled_terms.FileBundleGrouping",
            "groupedBy",
            description="Reference to the aspect used to group something.",
            instructions="Add the concept which was used to group file instances into this file bundle.",
        ),
        Property(
            "hash",
            "openminds.v2.core.Hash",
            "hash",
            description="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.",
            instructions="Add the hash that was generated for this file bundle.",
        ),
        Property(
            "is_part_of",
            ["openminds.v2.core.FileBundle", "openminds.v2.core.FileRepository"],
            "isPartOf",
            required=True,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add the file bundle or file repository this file bundle is a part of.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this file bundle.",
        ),
        Property(
            "pattern_of_filenames",
            str,
            "patternOfFilenames",
            formatting="text/plain",
            description="Reliable sample / structure of characters valid for all names in a particular collection of files.",
            instructions="Enter a regular expression (syntax: ECMA 262) which is valid for all filenames of the file instances that should be grouped into this file bundle.",
        ),
        Property(
            "storage_size",
            "openminds.v2.core.QuantitativeValue",
            "storageSize",
            description="Quantitative value defining how much disk space is used by an object on a computer system.",
            instructions="Enter the storage size this file bundle allocates.",
        ),
    ]

    def __init__(
        self,
        id=None,
        format=None,
        grouped_by=None,
        hash=None,
        is_part_of=None,
        name=None,
        pattern_of_filenames=None,
        storage_size=None,
    ):
        return super().__init__(
            id=id,
            format=format,
            grouped_by=grouped_by,
            hash=hash,
            is_part_of=is_part_of,
            name=name,
            pattern_of_filenames=pattern_of_filenames,
            storage_size=storage_size,
        )
