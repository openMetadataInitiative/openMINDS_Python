"""
Structured information on a file instance that is accessible via a URL.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class File(LinkedMetadata):
    """
    Structured information on a file instance that is accessible via a URL.
    """

    type_ = "https://openminds.ebrains.eu/core/File"
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "iri",
            IRI,
            "vocab:IRI",
            required=True,
            description="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
            instructions="Enter the internationalized resource identifier (IRI) to this file instance.",
        ),
        Property(
            "content_description",
            str,
            "vocab:contentDescription",
            formatting="text/plain",
            multiline=True,
            description="no description available",
            instructions="Enter a short content description for this file instance.",
        ),
        Property(
            "data_type",
            "openminds.latest.controlled_terms.DataType",
            "vocab:dataType",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all data types that are specifically represented in this file instance.",
        ),
        Property(
            "file_repository",
            "openminds.latest.core.FileRepository",
            "vocab:fileRepository",
            description="no description available",
            instructions="Add the overarching repository to which this file instance belongs.",
        ),
        Property(
            "format",
            "openminds.latest.core.ContentType",
            "vocab:format",
            description="Method of digitally organizing and structuring data or information.",
            instructions="Add the content type of this file instance.",
        ),
        Property(
            "hash",
            "openminds.latest.core.Hash",
            "vocab:hash",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.",
            instructions="Add all hashes that were generated for this file instance.",
        ),
        Property(
            "is_part_of",
            "openminds.latest.core.FileBundle",
            "vocab:isPartOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add all file bundles in which this file instance is grouped into.",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this file instance.",
        ),
        Property(
            "special_usage_role",
            "openminds.latest.controlled_terms.FileUsageRole",
            "vocab:specialUsageRole",
            description="Particular function of something when it is used.",
            instructions="Add the special usage role of this file instance.",
        ),
        Property(
            "storage_size",
            "openminds.latest.core.QuantitativeValue",
            "vocab:storageSize",
            description="Quantitative value defining how much disk space is used by an object on a computer system.",
            instructions="Enter the storage size of this file instance.",
        ),
    ]

    def __init__(
        self,
        id=None,
        iri=None,
        content_description=None,
        data_type=None,
        file_repository=None,
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
            content_description=content_description,
            data_type=data_type,
            file_repository=file_repository,
            format=format,
            hash=hash,
            is_part_of=is_part_of,
            name=name,
            special_usage_role=special_usage_role,
            storage_size=storage_size,
        )
