"""
Structured information on a computational model (concept level).
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class Model(LinkedMetadata):
    """
    Structured information on a computational model (concept level).
    """

    type_ = "https://openminds.ebrains.eu/core/Model"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v2.0"

    properties = [
        Property(
            "abstraction_level",
            "openminds.v2.controlled_terms.ModelAbstractionLevel",
            "abstractionLevel",
            required=True,
            description="Extent of simplification of physical, spatial, or temporal details or attributes in the study of objects or systems.",
            instructions="Add the abstraction level of this model version.",
        ),
        Property(
            "custodians",
            ["openminds.v2.core.Organization", "openminds.v2.core.Person"],
            "custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add one or several custodians (person or organization) that are responsible for this research product. Note that this custodian will be responsible for all attached research product versions.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description (abstract) for this research product (max. 2000 characters, incl. spaces; no references). Note that this description should be fitting for all attached research product versions.",
        ),
        Property(
            "developers",
            ["openminds.v2.core.Organization", "openminds.v2.core.Person"],
            "developer",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Legal person that creates or improves products or services (e.g., software, applications, etc.).",
            instructions="Add one or several developers (person or organization) that contributed to the code implementation of this model.",
        ),
        Property(
            "digital_identifier",
            ["openminds.v2.core.DOI", "openminds.v2.core.SWHID"],
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (title) for this research product.  Note that this full name should be fitting for all attached research product versions.",
        ),
        Property(
            "has_versions",
            "openminds.v2.core.ModelVersion",
            "hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to variants of an original.",
            instructions="Add one or several versions of this computational model.",
        ),
        Property(
            "homepage",
            "openminds.v2.core.URL",
            "homepage",
            description="Main website of something or someone.",
            instructions="Add the uniform resource locator (URL) to the homepage of this research product.",
        ),
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier.",
        ),
        Property(
            "scope",
            "openminds.v2.controlled_terms.ModelScope",
            "scope",
            required=True,
            description="Extent of something.",
            instructions="Add the scope of this model version.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (alias) for this research product (max. 30 characters; no space).",
        ),
        Property(
            "study_targets",
            [
                "openminds.v2.controlled_terms.BiologicalSex",
                "openminds.v2.controlled_terms.CellType",
                "openminds.v2.controlled_terms.Disease",
                "openminds.v2.controlled_terms.DiseaseModel",
                "openminds.v2.controlled_terms.Handedness",
                "openminds.v2.controlled_terms.Organ",
                "openminds.v2.controlled_terms.Phenotype",
                "openminds.v2.controlled_terms.Species",
                "openminds.v2.controlled_terms.Strain",
                "openminds.v2.controlled_terms.TermSuggestion",
                "openminds.v2.sands.CustomAnatomicalEntity",
                "openminds.v2.sands.ParcellationEntity",
            ],
            "studyTarget",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Structure or function that was targeted within a study.",
            instructions="Add all study targets of this model version.",
        ),
    ]

    def __init__(
        self,
        id=None,
        abstraction_level=None,
        custodians=None,
        description=None,
        developers=None,
        digital_identifier=None,
        full_name=None,
        has_versions=None,
        homepage=None,
        how_to_cite=None,
        scope=None,
        short_name=None,
        study_targets=None,
    ):
        return super().__init__(
            id=id,
            abstraction_level=abstraction_level,
            custodians=custodians,
            description=description,
            developers=developers,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_versions=has_versions,
            homepage=homepage,
            how_to_cite=how_to_cite,
            scope=scope,
            short_name=short_name,
            study_targets=study_targets,
        )
