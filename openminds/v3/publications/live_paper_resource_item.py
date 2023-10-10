"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class LivePaperResourceItem(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/publications/LivePaperResourceItem"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "iri",
            IRI,
            "IRI",
            required=True,
            description="Stands for Internationalized Resource Identifier which is an internet protocol standard that builds on the URI protocol, extending the set of permitted characters to include Unicode/ISO 10646.",
            instructions="Enter the internationalized resource identifier (IRI) to this live paper resource item.",
        ),
        Property(
            "hosted_by",
            "openminds.v3.core.Organization",
            "hostedBy",
            required=True,
            description="Reference to an organization that provides facilities and services for something.",
            instructions="Add the host organization of this live paper resource item.",
        ),
        Property(
            "is_part_of",
            "openminds.v3.publications.LivePaperSection",
            "isPartOf",
            required=True,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add the live paper section this live paper resource item is part of.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this live paper resource item.",
        ),
    ]

    def __init__(self, id=None, iri=None, hosted_by=None, is_part_of=None, name=None):
        return super().__init__(
            id=id,
            iri=iri,
            hosted_by=hosted_by,
            is_part_of=is_part_of,
            name=name,
        )
