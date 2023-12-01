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

    type_ = "https://openminds.ebrains.eu/sands/ParcellationTerminologyVersion"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "data_locations",
            "openminds.v3.core.File",
            "dataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the location of all files in which this parcellation terminology version is stored.",
        ),
        Property(
            "has_entities",
            "openminds.v3.sands.ParcellationEntityVersion",
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
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation terminology version.",
        ),
    ]

    def __init__(self, data_locations=None, has_entities=None, ontology_identifiers=None):
        return super().__init__(
            data_locations=data_locations,
            has_entities=has_entities,
            ontology_identifiers=ontology_identifiers,
        )
