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
    type_ = ["https://openminds.ebrains.eu/core/File"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "iri",
            IRI,
            "vocab:IRI",required=True,
            description="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
            instructions="Enter the internationalized resource identifier of this single file."
        ),
        Property(
            "content",
            str,
            "vocab:content",formatting="text/plain",
            
            
            description="Something that is contained.",
            instructions="Enter a short content description for this file instance."
        ),
        Property(
            "file_repository",
            "openminds.v2_0.core.FileRepository",
            "vocab:fileRepository",
            description="no description available",
            instructions="Add the over all repository to which this single file belongs."
        ),
        Property(
            "format",
            "openminds.v2_0.core.ContentType",
            "vocab:format",
            description="Method of digitally organizing and structuring data or information.",
            instructions="Add the content type of this file instance."
        ),
        Property(
            "hash",
            "openminds.v2_0.core.Hash",
            "vocab:hash",
            description="Term used for the process of converting any data into a single value. Often also directly refers to the resulting single value.",
            instructions="Add the hash that was generated for this file instance."
        ),
        Property(
            "is_part_of",
            "openminds.v2_0.core.FileBundle",
            "vocab:isPartOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add one or several bundles in which this single file can be grouped."
        ),
        Property(
            "name",
            str,
            "vocab:name",formatting="text/plain",
            
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this single file."
        ),
        Property(
            "special_usage_role",
            "openminds.v2_0.controlled_terms.FileUsageRole",
            "vocab:specialUsageRole",
            description="Particular function of something when it is used.",
            instructions="Add a special usage role for this single file."
        ),
        Property(
            "storage_size",
            "openminds.v2_0.core.QuantitativeValue",
            "vocab:storageSize",
            description="Quantitative value defining how much disk space is used by an object on a computer system.",
            instructions="Enter the storage size this file instance allocates."
        ),
        
    ]

    def __init__(self, id=None, iri=None, content=None, file_repository=None, format=None, hash=None, is_part_of=None, name=None, special_usage_role=None, storage_size=None):
        return super().__init__(id=id,iri=iri,content=content,file_repository=file_repository,format=format,hash=hash,is_part_of=is_part_of,name=name,special_usage_role=special_usage_role,storage_size=storage_size,)

