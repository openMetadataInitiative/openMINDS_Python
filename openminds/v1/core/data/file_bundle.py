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
    schema_version = "v1.0"

    properties = [
        Property(
            "content",
            str,
            "content",
            formatting="text/plain",
            description="Something that is contained.",
            instructions="Enter a short content description for this file bundle.",
        ),
        Property(
            "descended_from",
            [
                "openminds.v1.controlled_terms.BehavioralTask",
                "openminds.v1.core.File",
                "openminds.v1.core.FileBundle",
                "openminds.v1.core.SubjectGroupState",
                "openminds.v1.core.SubjectState",
                "openminds.v1.core.TissueSampleCollectionState",
                "openminds.v1.core.TissueSampleState",
            ],
            "descendedFrom",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all entities that played a role in the production of this file bundle (must be true for all grouped files).",
        ),
        Property(
            "format",
            "openminds.v1.core.ContentType",
            "format",
            description="Method of digitally organizing and structuring data or information.",
            instructions="If file instances within this bundle are organized and formatted according to a formal data structure use the appropriate contentType. Leave blank otherwise.",
        ),
        Property(
            "grouped_by",
            "openminds.v1.controlled_terms.FileBundleGrouping",
            "groupedBy",
            description="Reference to the aspect used to group something.",
            instructions="Add the concept which was used to group file instances into this file bundle.",
        ),
        Property(
            "hash",
            "openminds.v1.core.Hash",
            "hash",
            description="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.",
            instructions="Add the hash that was generated for this file bundle.",
        ),
        Property(
            "is_part_of",
            ["openminds.v1.core.FileBundle", "openminds.v1.core.FileRepository"],
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
            description="Word or phrase that constitutes the distinctive designation of the file bundle.",
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
            "openminds.v1.core.QuantitativeValue",
            "storageSize",
            description="Quantitative value defining how much disk space is used by an object on a computer system.",
            instructions="Enter the storage size this file bundle allocates.",
        ),
    ]

    def __init__(
        self,
        id=None,
        content=None,
        descended_from=None,
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
            content=content,
            descended_from=descended_from,
            format=format,
            grouped_by=grouped_by,
            hash=hash,
            is_part_of=is_part_of,
            name=name,
            pattern_of_filenames=pattern_of_filenames,
            storage_size=storage_size,
        )
