"""
<description not available>
"""

# this file was auto-generated!

from datetime import date
from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class CommonCoordinateSpaceVersion(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/CommonCoordinateSpaceVersion"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this common coordinate space version.",
        ),
        Property(
            "accessibility",
            "openminds.latest.controlled_terms.ProductAccessibility",
            "accessibility",
            required=True,
            description="Level to which something is accessible to someone or something.",
            instructions="Add the accessibility of the data for this research product version.",
        ),
        Property(
            "anatomical_axes_orientation",
            "openminds.latest.controlled_terms.AnatomicalAxesOrientation",
            "anatomicalAxesOrientation",
            required=True,
            description="Relation between reference planes used in anatomy and mathematics.",
            instructions="Add the axes orientation denoted in standard anatomical terms of direction (stated as XYZ) for this common coordinate space version.",
        ),
        Property(
            "authors",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "author",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this common coordinate space version as authors. Note that these authors will overwrite the author list provided for the overarching common coordinate space.",
        ),
        Property(
            "axes_origins",
            "openminds.latest.core.QuantitativeValue",
            "axesOrigin",
            multiple=True,
            unique_items=True,
            min_items=2,
            max_items=3,
            required=True,
            description="Special point in a coordinate system used as a fixed point of reference for the geometry of the surrounding space.",
            instructions="Enter the origin (central point where all axes intersect) of this common coordinate space version for two-dimensional spaces as [x, y] or for three-dimensional space as [x, y, z].",
        ),
        Property(
            "copyright",
            "openminds.latest.core.Copyright",
            "copyright",
            description="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
            instructions="Enter the copyright information of this research product version.",
        ),
        Property(
            "custodians",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for the research product version (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product version.",
        ),
        Property(
            "default_images",
            "openminds.latest.core.File",
            "defaultImage",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Two or three dimensional image that particluarly represents a specific coordinate space.",
            instructions="Add all image files used as visual representation of this common coordinate space version.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description (or abstract) of this research product version. Note that this version specific description will overwrite the description for the overarching dataset.",
        ),
        Property(
            "digital_identifier",
            ["openminds.latest.core.DOI", "openminds.latest.core.ISBN", "openminds.latest.core.RRID"],
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product version.",
        ),
        Property(
            "full_documentation",
            ["openminds.latest.core.DOI", "openminds.latest.core.File", "openminds.latest.core.WebResource"],
            "fullDocumentation",
            required=True,
            description="Non-abridged instructions, comments, and information for using a particular product.",
            instructions="Add the publication or file that acts as the full documentation of this research product version.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            description="Whole, non-abbreviated name of something or somebody.",
            instructions="Enter a descriptive full name (or title) for this research product version. Note that this version specific full name will overwrite the full name for the overarching dataset.",
        ),
        Property(
            "funding",
            "openminds.latest.core.Funding",
            "funding",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Money provided by a legal person for a particular purpose.",
            instructions="Add all funding information of this research product version.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of something or someone.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product version.",
        ),
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier.",
        ),
        Property(
            "is_alternative_version_of",
            "openminds.latest.sands.CommonCoordinateSpaceVersion",
            "isAlternativeVersionOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to an original form where the essence was preserved, but presented in an alternative form.",
            instructions="Add all common coordinate space versions that can be used alternatively to this common coordinate space version.",
        ),
        Property(
            "is_new_version_of",
            "openminds.latest.sands.CommonCoordinateSpaceVersion",
            "isNewVersionOf",
            description="Reference to a previous (potentially outdated) particular form of something.",
            instructions="Add the common coordinate space version preceding this common coordinate space version.",
        ),
        Property(
            "keywords",
            [
                "openminds.latest.controlled_terms.ActionStatusType",
                "openminds.latest.controlled_terms.AgeCategory",
                "openminds.latest.controlled_terms.AnalysisTechnique",
                "openminds.latest.controlled_terms.AnatomicalAxesOrientation",
                "openminds.latest.controlled_terms.AnatomicalIdentificationType",
                "openminds.latest.controlled_terms.AnatomicalPlane",
                "openminds.latest.controlled_terms.AnnotationCriteriaType",
                "openminds.latest.controlled_terms.AnnotationType",
                "openminds.latest.controlled_terms.AtlasType",
                "openminds.latest.controlled_terms.AuditoryStimulusType",
                "openminds.latest.controlled_terms.BiologicalOrder",
                "openminds.latest.controlled_terms.BiologicalProcess",
                "openminds.latest.controlled_terms.BiologicalSex",
                "openminds.latest.controlled_terms.BreedingType",
                "openminds.latest.controlled_terms.CellCultureType",
                "openminds.latest.controlled_terms.CellType",
                "openminds.latest.controlled_terms.ChemicalMixtureType",
                "openminds.latest.controlled_terms.Colormap",
                "openminds.latest.controlled_terms.ContributionType",
                "openminds.latest.controlled_terms.CranialWindowConstructionType",
                "openminds.latest.controlled_terms.CranialWindowReinforcementType",
                "openminds.latest.controlled_terms.CriteriaQualityType",
                "openminds.latest.controlled_terms.DataType",
                "openminds.latest.controlled_terms.DeviceType",
                "openminds.latest.controlled_terms.DifferenceMeasure",
                "openminds.latest.controlled_terms.Disease",
                "openminds.latest.controlled_terms.DiseaseModel",
                "openminds.latest.controlled_terms.EducationalLevel",
                "openminds.latest.controlled_terms.ElectricalStimulusType",
                "openminds.latest.controlled_terms.EthicsAssessment",
                "openminds.latest.controlled_terms.ExperimentalApproach",
                "openminds.latest.controlled_terms.FileBundleGrouping",
                "openminds.latest.controlled_terms.FileRepositoryType",
                "openminds.latest.controlled_terms.FileUsageRole",
                "openminds.latest.controlled_terms.GeneticStrainType",
                "openminds.latest.controlled_terms.GustatoryStimulusType",
                "openminds.latest.controlled_terms.Handedness",
                "openminds.latest.controlled_terms.Language",
                "openminds.latest.controlled_terms.Laterality",
                "openminds.latest.controlled_terms.LearningResourceType",
                "openminds.latest.controlled_terms.MeasuredQuantity",
                "openminds.latest.controlled_terms.MeasuredSignalType",
                "openminds.latest.controlled_terms.MetaDataModelType",
                "openminds.latest.controlled_terms.ModelAbstractionLevel",
                "openminds.latest.controlled_terms.ModelScope",
                "openminds.latest.controlled_terms.MolecularEntity",
                "openminds.latest.controlled_terms.OlfactoryStimulusType",
                "openminds.latest.controlled_terms.OperatingDevice",
                "openminds.latest.controlled_terms.OperatingSystem",
                "openminds.latest.controlled_terms.OpticalStimulusType",
                "openminds.latest.controlled_terms.Organ",
                "openminds.latest.controlled_terms.OrganismSubstance",
                "openminds.latest.controlled_terms.OrganismSystem",
                "openminds.latest.controlled_terms.PatchClampVariation",
                "openminds.latest.controlled_terms.PreparationType",
                "openminds.latest.controlled_terms.ProductAccessibility",
                "openminds.latest.controlled_terms.ProgrammingLanguage",
                "openminds.latest.controlled_terms.QualitativeOverlap",
                "openminds.latest.controlled_terms.SemanticDataType",
                "openminds.latest.controlled_terms.Service",
                "openminds.latest.controlled_terms.SetupType",
                "openminds.latest.controlled_terms.SoftwareApplicationCategory",
                "openminds.latest.controlled_terms.SoftwareFeature",
                "openminds.latest.controlled_terms.Species",
                "openminds.latest.controlled_terms.StimulationApproach",
                "openminds.latest.controlled_terms.StimulationTechnique",
                "openminds.latest.controlled_terms.SubcellularEntity",
                "openminds.latest.controlled_terms.SubjectAttribute",
                "openminds.latest.controlled_terms.TactileStimulusType",
                "openminds.latest.controlled_terms.Technique",
                "openminds.latest.controlled_terms.TermSuggestion",
                "openminds.latest.controlled_terms.Terminology",
                "openminds.latest.controlled_terms.TissueSampleAttribute",
                "openminds.latest.controlled_terms.TissueSampleType",
                "openminds.latest.controlled_terms.TypeOfUncertainty",
                "openminds.latest.controlled_terms.UBERONParcellation",
                "openminds.latest.controlled_terms.UnitOfMeasurement",
                "openminds.latest.controlled_terms.VisualStimulusType",
            ],
            "keyword",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Significant word or concept that are representative of something or someone.",
            instructions="Add all relevant keywords to this research product version either by adding controlled terms or by suggesting new terms.",
        ),
        Property(
            "license",
            "openminds.latest.core.License",
            "license",
            description="Grant by a party to another party as an element of an agreement between those parties that permits to do, use, or own something.",
            instructions="Add the license of this common coordinate space version.",
        ),
        Property(
            "native_unit",
            "openminds.latest.controlled_terms.UnitOfMeasurement",
            "nativeUnit",
            required=True,
            description="Determinate quantity used in the original measurement.",
            instructions="Add the native unit that is used for this common coordinate space version.",
        ),
        Property(
            "ontology_identifiers",
            str,
            "ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this common coordinate space version.",
        ),
        Property(
            "other_contributions",
            "openminds.latest.core.Contribution",
            "otherContribution",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Giving or supplying of something (such as money or time) as a part or share other than what is covered elsewhere.",
            instructions="Add any other contributions to this research product version that are not covered under 'author'/'developer' or 'custodian'.",
        ),
        Property(
            "related_publications",
            [
                "openminds.latest.core.DOI",
                "openminds.latest.core.HANDLE",
                "openminds.latest.core.ISBN",
                "openminds.latest.core.ISSN",
                "openminds.latest.publications.Book",
                "openminds.latest.publications.Chapter",
                "openminds.latest.publications.ScholarlyArticle",
            ],
            "relatedPublication",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to something that was made available for the general public to see or buy.",
            instructions="Add all further publications besides the full documentation that provide the original context for the production of this research product version (e.g., an original research article that used or produced the data of this research product version).",
        ),
        Property(
            "release_date",
            date,
            "releaseDate",
            required=True,
            description="Fixed date on which a product is due to become or was made available for the general public to see or buy",
            instructions="Enter the date (actual or intended) on which this research product version was first release, formatted as 'YYYY-MM-DD'.",
        ),
        Property(
            "repository",
            "openminds.latest.core.FileRepository",
            "repository",
            description="Place, room, or container where something is deposited or stored.",
            instructions="Add the file repository of this research product version.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
            instructions="Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
        Property(
            "support_channels",
            str,
            "supportChannel",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Way of communication used to interact with users or customers.",
            instructions="Enter all channels through which a user can receive support for handling this research product version.",
        ),
        Property(
            "used_specimens",
            [
                "openminds.latest.core.Subject",
                "openminds.latest.core.SubjectGroup",
                "openminds.latest.core.TissueSample",
                "openminds.latest.core.TissueSampleCollection",
            ],
            "usedSpecimen",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add the specimen that was used for the creation of this common coordinate space version.",
        ),
        Property(
            "version_identifier",
            str,
            "versionIdentifier",
            formatting="text/plain",
            required=True,
            description="Term or code used to identify the version of something.",
            instructions="Enter the version identifier of this research product version.",
        ),
        Property(
            "version_innovation",
            str,
            "versionInnovation",
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
        abbreviation=None,
        accessibility=None,
        anatomical_axes_orientation=None,
        authors=None,
        axes_origins=None,
        copyright=None,
        custodians=None,
        default_images=None,
        description=None,
        digital_identifier=None,
        full_documentation=None,
        full_name=None,
        funding=None,
        homepage=None,
        how_to_cite=None,
        is_alternative_version_of=None,
        is_new_version_of=None,
        keywords=None,
        license=None,
        native_unit=None,
        ontology_identifiers=None,
        other_contributions=None,
        related_publications=None,
        release_date=None,
        repository=None,
        short_name=None,
        support_channels=None,
        used_specimens=None,
        version_identifier=None,
        version_innovation=None,
    ):
        return super().__init__(
            id=id,
            abbreviation=abbreviation,
            accessibility=accessibility,
            anatomical_axes_orientation=anatomical_axes_orientation,
            authors=authors,
            axes_origins=axes_origins,
            copyright=copyright,
            custodians=custodians,
            default_images=default_images,
            description=description,
            digital_identifier=digital_identifier,
            full_documentation=full_documentation,
            full_name=full_name,
            funding=funding,
            homepage=homepage,
            how_to_cite=how_to_cite,
            is_alternative_version_of=is_alternative_version_of,
            is_new_version_of=is_new_version_of,
            keywords=keywords,
            license=license,
            native_unit=native_unit,
            ontology_identifiers=ontology_identifiers,
            other_contributions=other_contributions,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            short_name=short_name,
            support_channels=support_channels,
            used_specimens=used_specimens,
            version_identifier=version_identifier,
            version_innovation=version_innovation,
        )
