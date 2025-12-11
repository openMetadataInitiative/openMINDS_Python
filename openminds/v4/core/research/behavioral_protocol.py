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

    type_ = "https://openminds.om-i.org/types/BehavioralProtocol"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "described_in",
            ["openminds.v4.core.DOI", "openminds.v4.core.File", "openminds.v4.core.WebResource"],
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
            description="Longer statement or account giving the characteristics of the behavioral protocol.",
            instructions="Enter a description of this behavioral protocol.",
        ),
        Property(
            "internal_identifier",
            str,
            "internalIdentifier",
            formatting="text/plain",
            description="Term or code that identifies the behavioral protocol within a particular product.",
            instructions="Enter the identifier (or label) of this behavioral protocol that is used within the corresponding data files to identify this behavioral protocol.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the behavioral protocol.",
            instructions="Enter a descriptive name for this behavioral protocol.",
        ),
        Property(
            "stimulations",
            [
                "openminds.v4.controlled_terms.StimulationApproach",
                "openminds.v4.controlled_terms.StimulationTechnique",
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
                "openminds.v4.controlled_terms.AuditoryStimulusType",
                "openminds.v4.controlled_terms.ElectricalStimulusType",
                "openminds.v4.controlled_terms.GustatoryStimulusType",
                "openminds.v4.controlled_terms.OlfactoryStimulusType",
                "openminds.v4.controlled_terms.OpticalStimulusType",
                "openminds.v4.controlled_terms.TactileStimulusType",
                "openminds.v4.controlled_terms.VisualStimulusType",
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
