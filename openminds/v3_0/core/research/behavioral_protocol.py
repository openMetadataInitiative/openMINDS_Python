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
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "described_in",
            ["openminds.v3_0.core.DOI", "openminds.v3_0.core.File", "openminds.v3_0.core.WebResource"],
            "vocab:describedIn",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all sources in which this behavioral protocol is described in detail.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of this behavioral protocol.",
        ),
        Property(
            "internal_identifier",
            str,
            "vocab:internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies someone or something within a particular product.",
            instructions="Enter the identifier (or label) of this behavioral protocol that is used within the corresponding data files to identify this behavioral protocol.",
        ),
        Property(
            "name",
            str,
            "vocab:name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this behavioral protocol.",
        ),
        Property(
            "stimulation",
            [
                "openminds.v3_0.controlled_terms.StimulationApproach",
                "openminds.v3_0.controlled_terms.StimulationTechnique",
            ],
            "vocab:stimulation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all stimulation approaches and/or techniques used within this behavioral protocol.",
        ),
        Property(
            "stimulus_type",
            [
                "openminds.v3_0.controlled_terms.AuditoryStimulusType",
                "openminds.v3_0.controlled_terms.ElectricalStimulusType",
                "openminds.v3_0.controlled_terms.GustatoryStimulusType",
                "openminds.v3_0.controlled_terms.OlfactoryStimulusType",
                "openminds.v3_0.controlled_terms.OpticalStimulusType",
                "openminds.v3_0.controlled_terms.TactileStimulusType",
                "openminds.v3_0.controlled_terms.VisualStimulusType",
            ],
            "vocab:stimulusType",
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
        stimulation=None,
        stimulus_type=None,
    ):
        return super().__init__(
            id=id,
            described_in=described_in,
            description=description,
            internal_identifier=internal_identifier,
            name=name,
            stimulation=stimulation,
            stimulus_type=stimulus_type,
        )
