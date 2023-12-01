"""
Structured information on a research project.
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Protocol(LinkedMetadata):
    """
    Structured information on a research project.
    """

    type_ = "https://openminds.ebrains.eu/core/Protocol"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "described_in",
            ["openminds.v3.core.DOI", "openminds.v3.core.File", "openminds.v3.core.WebResource"],
            "describedIn",
            description="no description available",
            instructions="Add a publication or file in which this behavioral protocol is (originally) described in detail.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of this protocol.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter a descriptive name for this protocol.",
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
            instructions="Add all stimulus types used with this protocol.",
        ),
        Property(
            "techniques",
            [
                "openminds.v3.controlled_terms.AnalysisTechnique",
                "openminds.v3.controlled_terms.StimulationApproach",
                "openminds.v3.controlled_terms.StimulationTechnique",
                "openminds.v3.controlled_terms.Technique",
            ],
            "technique",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Method of accomplishing a desired aim.",
            instructions="Add all techniques (including stimulation approaches and/or techniques) that were used in this protocol.",
        ),
    ]

    def __init__(self, id=None, described_in=None, description=None, name=None, stimulus_types=None, techniques=None):
        return super().__init__(
            id=id,
            described_in=described_in,
            description=description,
            name=name,
            stimulus_types=stimulus_types,
            techniques=techniques,
        )
