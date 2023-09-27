"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Setup(LinkedMetadata):
    """
    <description not available>
    """

    type_ = ["https://openminds.ebrains.eu/core/Setup"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "description",
            str,
            "vocab:description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a short text describing this setup.",
        ),
        Property(
            "has_part",
            [
                "openminds.v3_0.core.Setup",
                "openminds.v3_0.core.SoftwareVersion",
                "openminds.v3_0.ephys.Electrode",
                "openminds.v3_0.ephys.ElectrodeArray",
                "openminds.v3_0.ephys.Pipette",
                "openminds.v3_0.specimen_prep.SlicingDevice",
            ],
            "vocab:hasPart",
            multiple=True,
            unique_items=True,
            min_items=2,
            required=True,
            description="no description available",
            instructions="Add all components, including other setups, that are part of this setup. Note that a setup should not be only composed of software.",
        ),
        Property(
            "location",
            str,
            "vocab:location",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the geographic location of this setup. This may include room number, building, institution and/or city.",
        ),
        Property(
            "manufacturer",
            ["openminds.v3_0.core.Consortium", "openminds.v3_0.core.Organization", "openminds.v3_0.core.Person"],
            "vocab:manufacturer",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the manufacturer (private or industrial) that constructed this setup.",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this setup.",
        ),
        Property(
            "type",
            "openminds.v3_0.controlled_terms.SetupType",
            "vocab:type",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Distinct class to which a group of entities or concepts with similar characteristics or attributes belong to.",
            instructions="Add all types that describe this setup.",
        ),
    ]

    def __init__(
        self, id=None, description=None, has_part=None, location=None, manufacturer=None, name=None, type=None
    ):
        return super().__init__(
            id=id,
            description=description,
            has_part=has_part,
            location=location,
            manufacturer=manufacturer,
            name=name,
            type=type,
        )
