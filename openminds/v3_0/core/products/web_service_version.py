"""
<description not available>
"""

# this file was auto-generated!

from datetime import date
from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class WebServiceVersion(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/WebServiceVersion"
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "accessibility",
            "openminds.v3_0.controlled_terms.ProductAccessibility",
            "vocab:accessibility",
            required=True,
            description="Level to which something is accessible to someone or something.",
            instructions="Add the accessibility of the data for this research product version.",
        ),
        Property(
            "copyright",
            "openminds.v3_0.core.Copyright",
            "vocab:copyright",
            description="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
            instructions="Enter the copyright information of this research product version.",
        ),
        Property(
            "custodian",
            ["openminds.v3_0.core.Consortium", "openminds.v3_0.core.Organization", "openminds.v3_0.core.Person"],
            "vocab:custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for the research product version (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product version.",
        ),
        Property(
            "description",
            str,
            "vocab:description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description (or abstract) of this research product version. Note that this version specific description will overwrite the description for the overarching dataset.",
        ),
        Property(
            "developer",
            ["openminds.v3_0.core.Consortium", "openminds.v3_0.core.Organization", "openminds.v3_0.core.Person"],
            "vocab:developer",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Legal person that creates or improves products or services (e.g., software, applications, etc.).",
            instructions="Add all parties that developed this web service version. Note that these developers will overwrite the developer list provided for the overarching web service.",
        ),
        Property(
            "full_documentation",
            ["openminds.v3_0.core.DOI", "openminds.v3_0.core.File", "openminds.v3_0.core.WebResource"],
            "vocab:fullDocumentation",
            required=True,
            description="Non-abridged instructions, comments, and information for using a particular product.",
            instructions="Add the publication or file that acts as the full documentation of this research product version.",
        ),
        Property(
            "full_name",
            str,
            "vocab:fullName",
            formatting="text/plain",
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (or title) for this research product version. Note that this version specific full name will overwrite the full name for the overarching dataset.",
        ),
        Property(
            "funding",
            "openminds.v3_0.core.Funding",
            "vocab:funding",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Money provided by a legal person for a particular purpose.",
            instructions="Add all funding information of this research product version.",
        ),
        Property(
            "has_part",
            "openminds.v3_0.core.SoftwareVersion",
            "vocab:hasPart",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all software versions that are components of this web service version.",
        ),
        Property(
            "homepage",
            IRI,
            "vocab:homepage",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product version.",
        ),
        Property(
            "how_to_cite",
            str,
            "vocab:howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier.",
        ),
        Property(
            "input_format",
            "openminds.v3_0.core.ContentType",
            "vocab:inputFormat",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Format of data that is put into a process or machine.",
            instructions="Add all content types that can be used as input by this web service version.",
        ),
        Property(
            "is_alternative_version_of",
            "openminds.v3_0.core.WebServiceVersion",
            "vocab:isAlternativeVersionOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an original form where the essence was preserved, but presented in an alternative form.",
            instructions="Add all web service versions that can be used alternatively to this web service version.",
        ),
        Property(
            "is_new_version_of",
            "openminds.v3_0.core.WebServiceVersion",
            "vocab:isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the web service version preceding this web service version.",
        ),
        Property(
            "keyword",
            [
                "openminds.v3_0.controlled_terms.ActionStatusType",
                "openminds.v3_0.controlled_terms.AgeCategory",
                "openminds.v3_0.controlled_terms.AnalysisTechnique",
                "openminds.v3_0.controlled_terms.AnatomicalAxesOrientation",
                "openminds.v3_0.controlled_terms.AnatomicalIdentificationType",
                "openminds.v3_0.controlled_terms.AnatomicalPlane",
                "openminds.v3_0.controlled_terms.AnnotationCriteriaType",
                "openminds.v3_0.controlled_terms.AnnotationType",
                "openminds.v3_0.controlled_terms.AtlasType",
                "openminds.v3_0.controlled_terms.AuditoryStimulusType",
                "openminds.v3_0.controlled_terms.BiologicalOrder",
                "openminds.v3_0.controlled_terms.BiologicalProcess",
                "openminds.v3_0.controlled_terms.BiologicalSex",
                "openminds.v3_0.controlled_terms.BreedingType",
                "openminds.v3_0.controlled_terms.CellCultureType",
                "openminds.v3_0.controlled_terms.CellType",
                "openminds.v3_0.controlled_terms.ChemicalMixtureType",
                "openminds.v3_0.controlled_terms.Colormap",
                "openminds.v3_0.controlled_terms.ContributionType",
                "openminds.v3_0.controlled_terms.CranialWindowConstructionType",
                "openminds.v3_0.controlled_terms.CranialWindowReinforcementType",
                "openminds.v3_0.controlled_terms.CriteriaQualityType",
                "openminds.v3_0.controlled_terms.DataType",
                "openminds.v3_0.controlled_terms.DeviceType",
                "openminds.v3_0.controlled_terms.DifferenceMeasure",
                "openminds.v3_0.controlled_terms.Disease",
                "openminds.v3_0.controlled_terms.DiseaseModel",
                "openminds.v3_0.controlled_terms.EducationalLevel",
                "openminds.v3_0.controlled_terms.ElectricalStimulusType",
                "openminds.v3_0.controlled_terms.EthicsAssessment",
                "openminds.v3_0.controlled_terms.ExperimentalApproach",
                "openminds.v3_0.controlled_terms.FileBundleGrouping",
                "openminds.v3_0.controlled_terms.FileRepositoryType",
                "openminds.v3_0.controlled_terms.FileUsageRole",
                "openminds.v3_0.controlled_terms.GeneticStrainType",
                "openminds.v3_0.controlled_terms.GustatoryStimulusType",
                "openminds.v3_0.controlled_terms.Handedness",
                "openminds.v3_0.controlled_terms.Language",
                "openminds.v3_0.controlled_terms.Laterality",
                "openminds.v3_0.controlled_terms.LearningResourceType",
                "openminds.v3_0.controlled_terms.MeasuredQuantity",
                "openminds.v3_0.controlled_terms.MeasuredSignalType",
                "openminds.v3_0.controlled_terms.MetaDataModelType",
                "openminds.v3_0.controlled_terms.ModelAbstractionLevel",
                "openminds.v3_0.controlled_terms.ModelScope",
                "openminds.v3_0.controlled_terms.MolecularEntity",
                "openminds.v3_0.controlled_terms.OlfactoryStimulusType",
                "openminds.v3_0.controlled_terms.OperatingDevice",
                "openminds.v3_0.controlled_terms.OperatingSystem",
                "openminds.v3_0.controlled_terms.OpticalStimulusType",
                "openminds.v3_0.controlled_terms.Organ",
                "openminds.v3_0.controlled_terms.OrganismSubstance",
                "openminds.v3_0.controlled_terms.OrganismSystem",
                "openminds.v3_0.controlled_terms.PatchClampVariation",
                "openminds.v3_0.controlled_terms.PreparationType",
                "openminds.v3_0.controlled_terms.ProductAccessibility",
                "openminds.v3_0.controlled_terms.ProgrammingLanguage",
                "openminds.v3_0.controlled_terms.QualitativeOverlap",
                "openminds.v3_0.controlled_terms.SemanticDataType",
                "openminds.v3_0.controlled_terms.Service",
                "openminds.v3_0.controlled_terms.SetupType",
                "openminds.v3_0.controlled_terms.SoftwareApplicationCategory",
                "openminds.v3_0.controlled_terms.SoftwareFeature",
                "openminds.v3_0.controlled_terms.Species",
                "openminds.v3_0.controlled_terms.StimulationApproach",
                "openminds.v3_0.controlled_terms.StimulationTechnique",
                "openminds.v3_0.controlled_terms.SubcellularEntity",
                "openminds.v3_0.controlled_terms.SubjectAttribute",
                "openminds.v3_0.controlled_terms.TactileStimulusType",
                "openminds.v3_0.controlled_terms.Technique",
                "openminds.v3_0.controlled_terms.TermSuggestion",
                "openminds.v3_0.controlled_terms.Terminology",
                "openminds.v3_0.controlled_terms.TissueSampleAttribute",
                "openminds.v3_0.controlled_terms.TissueSampleType",
                "openminds.v3_0.controlled_terms.TypeOfUncertainty",
                "openminds.v3_0.controlled_terms.UBERONParcellation",
                "openminds.v3_0.controlled_terms.UnitOfMeasurement",
                "openminds.v3_0.controlled_terms.VisualStimulusType",
            ],
            "vocab:keyword",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Significant word or concept that are representative of something or someone.",
            instructions="Add all relevant keywords to this research product version either by adding controlled terms or by suggesting new terms.",
        ),
        Property(
            "other_contribution",
            "openminds.v3_0.core.Contribution",
            "vocab:otherContribution",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.",
            instructions="Add any other contributions to this research product version that are not covered under 'author'/'developer' or 'custodian'.",
        ),
        Property(
            "output_format",
            "openminds.v3_0.core.ContentType",
            "vocab:outputFormat",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Format of data that comes out of, is delivered or produced by a process or machine.",
            instructions="Add all content types that can be generated as output by this web service version.",
        ),
        Property(
            "related_publication",
            [
                "openminds.v3_0.core.DOI",
                "openminds.v3_0.core.HANDLE",
                "openminds.v3_0.core.ISBN",
                "openminds.v3_0.core.ISSN",
                "openminds.v3_0.publications.Book",
                "openminds.v3_0.publications.Chapter",
                "openminds.v3_0.publications.ScholarlyArticle",
            ],
            "vocab:relatedPublication",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to something that was made available for the general public to see or buy.",
            instructions="Add all further publications besides the full documentation that provide the original context for the production of this research product version (e.g., an original research article that used or produced the data of this research product version).",
        ),
        Property(
            "release_date",
            date,
            "vocab:releaseDate",
            required=True,
            description="Fixed date on which a product is due to become or was made available for the general public to see or buy",
            instructions="Enter the date (actual or intended) on which this research product version was first release, formatted as 'YYYY-MM-DD'.",
        ),
        Property(
            "repository",
            "openminds.v3_0.core.FileRepository",
            "vocab:repository",
            description="Place, room, or container where something is deposited or stored.",
            instructions="Add the file repository of this research product version.",
        ),
        Property(
            "short_name",
            str,
            "vocab:shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
        Property(
            "support_channel",
            str,
            "vocab:supportChannel",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Way of communication used to interact with users or customers.",
            instructions="Enter all channels through which a user can receive support for handling this research product version.",
        ),
        Property(
            "version_identifier",
            str,
            "vocab:versionIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this research product version.",
        ),
        Property(
            "version_innovation",
            str,
            "vocab:versionInnovation",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Documentation on what changed in comparison to a previously published form of something.",
            instructions="Enter a short description (or summary) of the novelties/peculiarities of this research product version in comparison to its preceding versions. If this research product version is the first version, you can enter the following disclaimer 'This is the first version of this research product'.",
        ),
    ]

    def __init__(
        self,
        id=None,
        accessibility=None,
        copyright=None,
        custodian=None,
        description=None,
        developer=None,
        full_documentation=None,
        full_name=None,
        funding=None,
        has_part=None,
        homepage=None,
        how_to_cite=None,
        input_format=None,
        is_alternative_version_of=None,
        is_new_version_of=None,
        keyword=None,
        other_contribution=None,
        output_format=None,
        related_publication=None,
        release_date=None,
        repository=None,
        short_name=None,
        support_channel=None,
        version_identifier=None,
        version_innovation=None,
    ):
        return super().__init__(
            id=id,
            accessibility=accessibility,
            copyright=copyright,
            custodian=custodian,
            description=description,
            developer=developer,
            full_documentation=full_documentation,
            full_name=full_name,
            funding=funding,
            has_part=has_part,
            homepage=homepage,
            how_to_cite=how_to_cite,
            input_format=input_format,
            is_alternative_version_of=is_alternative_version_of,
            is_new_version_of=is_new_version_of,
            keyword=keyword,
            other_contribution=other_contribution,
            output_format=output_format,
            related_publication=related_publication,
            release_date=release_date,
            repository=repository,
            short_name=short_name,
            support_channel=support_channel,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )