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
    schema_version = "v2.0"

    properties = [
        Property(
            "electrodes",
            "openminds.v2.sands.Electrode",
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
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this electrode array that may help you to more easily find it again.",
        ),
    ]

    def __init__(self, id=None, electrodes=None, internal_identifier=None, lookup_label=None):
        return super().__init__(
            id=id,
            electrodes=electrodes,
            internal_identifier=internal_identifier,
            lookup_label=lookup_label,
        )
