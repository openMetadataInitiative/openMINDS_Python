"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class ParcellationTerminology(EmbeddedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/sands/ParcellationTerminology"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "data_location",
            "openminds.v3_0.core.File",
            "vocab:dataLocation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the location of all files in which this parcellation terminology is stored.",
        ),
        Property(
            "has_entity",
            "openminds.v3_0.sands.ParcellationEntity",
            "vocab:hasEntity",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all parcellation entities which belong to this parcellation terminology.",
        ),
        Property(
            "ontology_identifier",
            str,
            "vocab:ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation terminology.",
        ),
    ]

    def __init__(self, data_location=None, has_entity=None, ontology_identifier=None):
        return super().__init__(
            data_location=data_location,
            has_entity=has_entity,
            ontology_identifier=ontology_identifier,
        )
