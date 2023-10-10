"""
Structured information on a file instances.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class FileInstance(LinkedMetadata):
    """
    Structured information on a file instances.
    """

    type_ = "https://openminds.ebrains.eu/core/FileInstance"
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
            instructions="Enter the internationalized resource identifier of this file instance.",
        ),
        Property(
            "content",
            str,
            "content",
            formatting="text/plain",
            description="Something that is contained.",
            instructions="Enter a short content description for this file instance.",
        ),
        Property(
            "format",
            "openminds.v1.core.ContentType",
            "format",
            description="Method of digitally organizing and structuring data or information.",
            instructions="Add the content type of this file instance.",
        ),
        Property(
            "hash",
            "openminds.v1.core.Hash",
            "hash",
            description="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.",
            instructions="Add the hash that was generated for this file instance.",
        ),
        Property(
            "is_part_of",
            "openminds.v1.core.FileBundle",
            "isPartOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add one or several file bundles in which this file instance can be grouped in.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this file instance.",
        ),
        Property(
            "special_usage_role",
            "openminds.v1.controlled_terms.fileUsageRole",
            "specialUsageRole",
            description="Particular function of something when it is used.",
            instructions="Add a special usage role for this file instance.",
        ),
        Property(
            "storage_size",
            "openminds.v1.core.QuantitativeValue",
            "storageSize",
            description="Quantitative value defining how much disk space is used by an object on a computer system.",
            instructions="Enter the storage size this file instance allocates.",
        ),
    ]

    def __init__(
        self,
        id=None,
        iri=None,
        content=None,
        format=None,
        hash=None,
        is_part_of=None,
        name=None,
        special_usage_role=None,
        storage_size=None,
    ):
        return super().__init__(
            id=id,
            iri=iri,
            content=content,
            format=format,
            hash=hash,
            is_part_of=is_part_of,
            name=name,
            special_usage_role=special_usage_role,
            storage_size=storage_size,
        )
