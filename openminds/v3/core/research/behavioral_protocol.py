"""
Structured information about a protocol used in an experiment studying human or animal behavior.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class BehavioralProtocol(LinkedMetadata):
    """
    Structured information about a protocol used in an experiment studying human or animal behavior.
    """

    type_ = "https://openminds.ebrains.eu/core/BehavioralProtocol"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "described_in",
            ["openminds.v3.core.DOI", "openminds.v3.core.File", "openminds.v3.core.WebResource"],
            "describedIn",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all sources in which this behavioral protocol is described in detail.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of this behavioral protocol.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this behavioral protocol that is used within the corresponding data files to identify this behavioral protocol.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this behavioral protocol.",
        ),
        Property(
            "stimulations",
            [
                "openminds.v3.controlled_terms.StimulationApproach",
                "openminds.v3.controlled_terms.StimulationTechnique",
            ],
            "stimulation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all stimulation approaches and/or techniques used within this behavioral protocol.",
        ),
        Property(
            "stimulus_types",
            [
                "openminds.v3.controlled_terms.AuditoryStimulusType",
                "openminds.v3.controlled_terms.ElectricalStimulusType",
                "openminds.v3.controlled_terms.GustatoryStimulusType",
                "openminds.v3.controlled_terms.OlfactoryStimulusType",
                "openminds.v3.controlled_terms.OpticalStimulusType",
                "openminds.v3.controlled_terms.TactileStimulusType",
                "openminds.v3.controlled_terms.VisualStimulusType",
            ],
            "stimulusType",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all stimulus types used within this behavioral protocol.",
        ),
    ]

    def __init__(
        self,
        id=None,
        described_in=None,
        description=None,
        internal_identifier=None,
        name=None,
        stimulations=None,
        stimulus_types=None,
    ):
        return super().__init__(
            id=id,
            described_in=described_in,
            description=description,
            internal_identifier=internal_identifier,
            name=name,
            stimulations=stimulations,
            stimulus_types=stimulus_types,
        )
