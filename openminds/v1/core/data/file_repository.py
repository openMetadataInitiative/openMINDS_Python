"""
Structured information on a file repository.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class FileRepository(LinkedMetadata):
    """
    Structured information on a file repository.
    """

    type_ = "https://openminds.ebrains.eu/core/FileRepository"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "iri",
            IRI,
            "IRI",
            required=True,
            description="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
            instructions="Enter the internationalized resource identifier (IRI) of this file repository.",
        ),
        Property(
            "content_type_patterns",
            "openminds.v1.core.ContentTypePattern",
            "contentTypePattern",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all content type patterns that would identify matching content types for files within this file repository.",
        ),
        Property(
            "format",
            "openminds.v1.core.ContentType",
            "format",
            description="Method of digitally organizing and structuring data or information.",
            instructions="If file instances and bundles within the repository are organized and formatted according to a formal data structure use the appropriate contentType. Leave blank otherwise.",
        ),
        Property(
            "hash",
            "openminds.v1.core.Hash",
            "hash",
            description="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.",
            instructions="Add the hash that was generated for this file repository.",
        ),
        Property(
            "hosted_by",
            "openminds.v1.core.Organization",
            "hostedBy",
            required=True,
            description="Reference to an organization that provides facilities and services for something.",
            instructions="Add the host of this file repository.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the file repository.",
            instructions="Enter the name of this file repository.",
        ),
        Property(
            "repository_type",
            "openminds.v1.controlled_terms.FileRepositoryType",
            "repositoryType",
            description="no description available",
            instructions="Add the type of this file repository.",
        ),
        Property(
            "storage_size",
            "openminds.v1.core.QuantitativeValue",
            "storageSize",
            description="Quantitative value defining how much disk space is used by an object on a computer system.",
            instructions="Enter the storage size this file repository allocates.",
        ),
        Property(
            "structure_pattern",
            "openminds.v1.core.FileRepositoryStructure",
            "structurePattern",
            description="no description available",
            instructions="Add a file repository structure which identifies the file path patterns used in this file repository.",
        ),
    ]

    def __init__(
        self,
        id=None,
        iri=None,
        content_type_patterns=None,
        format=None,
        hash=None,
        hosted_by=None,
        name=None,
        repository_type=None,
        storage_size=None,
        structure_pattern=None,
    ):
        return super().__init__(
            id=id,
            iri=iri,
            content_type_patterns=content_type_patterns,
            format=format,
            hash=hash,
            hosted_by=hosted_by,
            name=name,
            repository_type=repository_type,
            storage_size=storage_size,
            structure_pattern=structure_pattern,
        )
