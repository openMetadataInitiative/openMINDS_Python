"""
Structured information on an electrode array.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ElectrodeArray(LinkedMetadata):
    """
    Structured information on an electrode array.
    """

    type_ = "https://openminds.ebrains.eu/sands/ElectrodeArray"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "electrodes",
            "openminds.v1.sands.Electrode",
            "electrodes",
            multiple=True,
            unique_items=True,
            min_items=2,
            required=True,
            description="Elements in a semiconductor device that emits or collects electrons or holes or controls their movements.",
            instructions="Add two or more electrodes which build this array.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier used for this electrode array within the file it is stored in.",
        ),
    ]

    def __init__(self, id=None, electrodes=None, internal_identifier=None):
        return super().__init__(
            id=id,
            electrodes=electrodes,
            internal_identifier=internal_identifier,
        )
