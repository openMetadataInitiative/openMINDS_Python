"""
Structured information on a computational model (concept level).
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Model(LinkedMetadata):
    """
    Structured information on a computational model (concept level).
    """

    type_ = ["https://openminds.ebrains.eu/core/Model"]
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "abstraction_level",
            "openminds.v3_0.controlled_terms.ModelAbstractionLevel",
            "vocab:abstractionLevel",
            required=True,
            description="Extent of simplification of physical, spatial, or temporal details or attributes in the study of objects or systems.",
            instructions="Add the abstraction level of this computational model.",
        ),
        Property(
            "custodian",
            ["openminds.v3_0.core.Consortium", "openminds.v3_0.core.Organization", "openminds.v3_0.core.Person"],
            "vocab:custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for this research product (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product. Unless specified differently, this custodian will be responsible for all attached research product versions.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description (or abstract) of this research product. Note that this should be a suitable description for all attached research product versions.",
        ),
        Property(
            "developer",
            ["openminds.v3_0.core.Consortium", "openminds.v3_0.core.Organization", "openminds.v3_0.core.Person"],
            "vocab:developer",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Legal person that creates or improves products or services (e.g., software, applications, etc.).",
            instructions="Add all parties that developed this computational model.",
        ),
        Property(
            "digital_identifier",
            ["openminds.v3_0.core.DOI", "openminds.v3_0.core.SWHID"],
            "vocab:digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.",
        ),
        Property(
            "full_name",
            str,
            "vocab:fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (or title) for this research product. Note that this should be a suitable full name for all attached research product versions.",
        ),
        Property(
            "has_version",
            "openminds.v3_0.core.ModelVersion",
            "vocab:hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to variants of an original.",
            instructions="Add all versions of this computational model.",
        ),
        Property(
            "homepage",
            IRI,
            "vocab:homepage",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product.",
        ),
        Property(
            "how_to_cite",
            str,
            "vocab:howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier.",
        ),
        Property(
            "scope",
            "openminds.v3_0.controlled_terms.ModelScope",
            "vocab:scope",
            required=True,
            description="Extent of something.",
            instructions="Add the scope of this computational model.",
        ),
        Property(
            "short_name",
            str,
            "vocab:shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
        Property(
            "study_target",
            [
                "openminds.v3_0.controlled_terms.AuditoryStimulusType",
                "openminds.v3_0.controlled_terms.BiologicalOrder",
                "openminds.v3_0.controlled_terms.BiologicalSex",
                "openminds.v3_0.controlled_terms.BreedingType",
                "openminds.v3_0.controlled_terms.CellCultureType",
                "openminds.v3_0.controlled_terms.CellType",
                "openminds.v3_0.controlled_terms.Disease",
                "openminds.v3_0.controlled_terms.DiseaseModel",
                "openminds.v3_0.controlled_terms.ElectricalStimulusType",
                "openminds.v3_0.controlled_terms.GeneticStrainType",
                "openminds.v3_0.controlled_terms.GustatoryStimulusType",
                "openminds.v3_0.controlled_terms.Handedness",
                "openminds.v3_0.controlled_terms.MolecularEntity",
                "openminds.v3_0.controlled_terms.OlfactoryStimulusType",
                "openminds.v3_0.controlled_terms.OpticalStimulusType",
                "openminds.v3_0.controlled_terms.Organ",
                "openminds.v3_0.controlled_terms.OrganismSubstance",
                "openminds.v3_0.controlled_terms.OrganismSystem",
                "openminds.v3_0.controlled_terms.Species",
                "openminds.v3_0.controlled_terms.SubcellularEntity",
                "openminds.v3_0.controlled_terms.TactileStimulusType",
                "openminds.v3_0.controlled_terms.TermSuggestion",
                "openminds.v3_0.controlled_terms.UBERONParcellation",
                "openminds.v3_0.controlled_terms.VisualStimulusType",
                "openminds.v3_0.sands.CustomAnatomicalEntity",
                "openminds.v3_0.sands.ParcellationEntity",
                "openminds.v3_0.sands.ParcellationEntityVersion",
            ],
            "vocab:studyTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Structure or function that was targeted within a study.",
            instructions="Add all study targets of this computational model.",
        ),
    ]

    def __init__(
        self,
        id=None,
        abstraction_level=None,
        custodian=None,
        description=None,
        developer=None,
        digital_identifier=None,
        full_name=None,
        has_version=None,
        homepage=None,
        how_to_cite=None,
        scope=None,
        short_name=None,
        study_target=None,
    ):
        return super().__init__(
            id=id,
            abstraction_level=abstraction_level,
            custodian=custodian,
            description=description,
            developer=developer,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_version=has_version,
            homepage=homepage,
            how_to_cite=how_to_cite,
            scope=scope,
            short_name=short_name,
            study_target=study_target,
        )
