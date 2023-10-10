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
            "iri",
            str,
            "IRI",
            formatting="text/plain",
            required=True,
            description="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
            instructions="Enter the internationalized resource identifier (IRI) of this file bundle.",
        ),
        Property(
            "format",
            "openminds.v1.core.ContentType",
            "format",
            description="Method of digitally organizing and structuring data or information.",
            instructions="Add the content type of this file bundle.",
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
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this file bundle.",
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
        self, id=None, iri=None, format=None, grouped_by=None, hash=None, is_part_of=None, name=None, storage_size=None
    ):
        return super().__init__(
            id=id,
            iri=iri,
            format=format,
            grouped_by=grouped_by,
            hash=hash,
            is_part_of=is_part_of,
            name=name,
            storage_size=storage_size,
        )
