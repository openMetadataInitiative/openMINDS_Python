"""
Structured information on an electrode.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Electrode(LinkedMetadata):
    """
    Structured information on an electrode.
    """

    type_ = ["https://openminds.ebrains.eu/sands/Electrode"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "electrode_contact",
            "openminds.v2_0.sands.ElectrodeContact",
            "vocab:electrodeContact",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Not shielded part of a conductor that is used to establish electrical contact with a nonmetallic part of a circuit.",
            instructions="Add one or several electrical contacts of this electrode.",
        ),
        Property(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier used for this electrode within the file it is stored in.",
        ),
        Property(
            "lookup_label",
            str,
            "vocab:lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this electrode that may help you to more easily find it again.",
        ),
    ]

    def __init__(self, id=None, electrode_contact=None, internal_identifier=None, lookup_label=None):
        return super().__init__(
            id=id,
            electrode_contact=electrode_contact,
            internal_identifier=internal_identifier,
            lookup_label=lookup_label,
        )
