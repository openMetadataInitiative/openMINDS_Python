"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class EphysStimulus(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/stimulation/EphysStimulus"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "type",
            "openminds.v3.controlled_terms.ElectricalStimulusType",
            "type",
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add the type that describe this electrical stimulus.",
        ),
    ]

    def __init__(self, id=None, type=None):
        return super().__init__(
            id=id,
            type=type,
        )
