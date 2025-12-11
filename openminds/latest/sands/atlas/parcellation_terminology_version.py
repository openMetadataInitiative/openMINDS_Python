"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class ParcellationTerminologyVersion(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/ParcellationTerminologyVersion"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "data_locations",
            ["openminds.latest.core.File", "openminds.latest.core.WebResource"],
            "dataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the location of all files in which this parcellation terminology version is stored.",
        ),
        Property(
            "digital_identifier",
            ["openminds.latest.core.DOI", "openminds.latest.core.ISBN", "openminds.latest.core.RRID"],
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this parcellation terminology version.",
        ),
        Property(
            "has_entities",
            "openminds.latest.sands.ParcellationEntityVersion",
            "hasEntity",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all parcellation entity versions which belong to this parcellation terminology version.",
        ),
        Property(
            "ontology_identifiers",
            str,
            "ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify the parcellation terminology version registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation terminology version.",
        ),
    ]

    def __init__(self, data_locations=None, digital_identifier=None, has_entities=None, ontology_identifiers=None):
        return super().__init__(
            data_locations=data_locations,
            digital_identifier=digital_identifier,
            has_entities=has_entities,
            ontology_identifiers=ontology_identifiers,
        )
