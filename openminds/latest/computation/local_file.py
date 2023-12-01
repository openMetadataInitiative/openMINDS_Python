"""
Structured information about a file that is not accessible via a URL.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class LocalFile(LinkedMetadata):
    """
    Structured information about a file that is not accessible via a URL.
    """

    type_ = "https://openminds.ebrains.eu/computation/LocalFile"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "content_description",
            str,
            "contentDescription",
            formatting="text/plain",
            multiline=True,
            description="no description available",
            instructions="Enter a short content description for this local file instance.",
        ),
        Property(
            "copy_of",
            "openminds.latest.core.File",
            "copyOf",
            description="no description available",
            instructions="Add the file of which this is a copy.",
        ),
        Property(
            "data_types",
            "openminds.latest.controlled_terms.DataType",
            "dataType",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all data types that are specifically represented in this local file instance.",
        ),
        Property(
            "format",
            "openminds.latest.core.ContentType",
            "format",
            description="Method of digitally organizing and structuring data or information.",
            instructions="Add the content type of this local file instance.",
        ),
        Property(
            "hash",
            "openminds.latest.core.Hash",
            "hash",
            description="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.",
            instructions="Add the hash that was generated for this local file instance.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this local file instance.",
        ),
        Property(
            "path",
            str,
            "path",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the file system path (absolute path or relative to the working directory) to this local file instance.",
        ),
        Property(
            "special_usage_role",
            "openminds.latest.controlled_terms.FileUsageRole",
            "specialUsageRole",
            description="Particular function of something when it is used.",
            instructions="Add the special usage role of this local file instance.",
        ),
        Property(
            "storage_size",
            "openminds.latest.core.QuantitativeValue",
            "storageSize",
            description="Quantitative value defining how much disk space is used by an object on a computer system.",
            instructions="Enter the storage size of this local file instance.",
        ),
    ]

    def __init__(
        self,
        id=None,
        content_description=None,
        copy_of=None,
        data_types=None,
        format=None,
        hash=None,
        name=None,
        path=None,
        special_usage_role=None,
        storage_size=None,
    ):
        return super().__init__(
            id=id,
            content_description=content_description,
            copy_of=copy_of,
            data_types=data_types,
            format=format,
            hash=hash,
            name=name,
            path=path,
            special_usage_role=special_usage_role,
            storage_size=storage_size,
        )
