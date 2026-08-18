"""
<description not available>
"""

# this file was auto-generated!

from datetime import date
from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class CommonCoordinateFrameworkVersion(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CommonCoordinateFrameworkVersion"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this common coordinate framework version.",
        ),
        Property(
            "accessibility",
            "openminds.latest.core.Accessibility",
            "accessibility",
            required=True,
            description="Level to which something is accessible to the common coordinate framework version.",
            instructions="Add the accessibility of the data for this research product version.",
        ),
        Property(
            "anatomical_axes_orientation",
            "openminds.latest.controlled_terms.AnatomicalAxesOrientation",
            "anatomicalAxesOrientation",
            required=True,
            description="Relation between reference planes used in anatomy and mathematics.",
            instructions="Add the axes orientation denoted in standard anatomical terms of direction (stated as XYZ) for the anatomical space of this common coordinate framework version.",
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
            instructions="Enter the coordinate point in the native anatomical space of the template as [x, y] or [x, y, z] for two- or three-dimensional spaces, respectively, that has been defined as the origin of the anatomical space of this common coordinate framework version (i.e., as the central point where all axes intersect).",
        ),
        Property(
            "contributions",
            "openminds.latest.core.Contribution",
            "contribution",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all individual, organisational, or consortial contributions to this research product version. These values override the inherited values from the version-independent product.",
        ),
        Property(
            "contributor_affiliations",
            "openminds.latest.core.Affiliation",
            "contributorAffiliation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all affiliations for the individual contributors to this research product version.",
        ),
        Property(
            "copyright",
            "openminds.latest.core.Copyright",
            "copyright",
            description="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
            instructions="Enter the copyright information of this research product version.",
        ),
        Property(
            "default_images",
            "openminds.latest.core.File",
            "defaultImage",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Two or three dimensional image that particluarly represents a specific coordinate space.",
            instructions="Add all image files used as visual representation of this common coordinate framework version.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of the common coordinate framework version.",
            instructions="Enter a description (or abstract) of this research product version. This value overrides the inherited value from the version-independent product.",
        ),
        Property(
            "digital_identifier",
            ["openminds.latest.core.DOI", "openminds.latest.core.ISBN", "openminds.latest.core.RRID"],
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product version.",
        ),
        Property(
            "documentation",
            [
                "openminds.latest.core.DOI",
                "openminds.latest.core.File",
                "openminds.latest.core.ISBN",
                "openminds.latest.core.WebResource",
            ],
            "documentation",
            required=True,
            description="no description available",
            instructions="Add the publication or file that acts as the documentation of this research product version. This value overrides the inherited value from the version-independent product.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of the common coordinate framework version.",
            instructions="Enter a descriptive full name (or title) for this research product version. This value overrides the inherited value from the version-independent product.",
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
            description="Main website of the common coordinate framework version.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product version. This value overrides the inherited value from the version-independent product.",
        ),
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product version. Leave blank if citation text can be extracted from the assigned digital identifier.",
        ),
        Property(
            "is_preceded_by",
            "openminds.latest.sands.CommonCoordinateFrameworkVersion",
            "isPrecededBy",
            description="no description available",
            instructions="Add the common coordinate framework version preceding this common coordinate framework version.",
        ),
        Property(
            "is_variant_of",
            "openminds.latest.sands.CommonCoordinateFrameworkVersion",
            "isVariantOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all common coordinate framework versions that can be used alternatively to this common coordinate framework version.",
        ),
        Property(
            "is_version_of",
            "openminds.latest.sands.CommonCoordinateFramework",
            "isVersionOf",
            required=True,
            description="no description available",
            instructions="Add the version-independent information about this common coordinate framework.",
        ),
        Property(
            "keywords",
            [
                "openminds.latest.controlled_terms.AccessChannel",
                "openminds.latest.controlled_terms.AccessEligibilityType",
                "openminds.latest.controlled_terms.AccessForm",
                "openminds.latest.controlled_terms.AccessProcessType",
                "openminds.latest.controlled_terms.ActionStatusType",
                "openminds.latest.controlled_terms.AgeCategory",
                "openminds.latest.controlled_terms.AgeReference",
                "openminds.latest.controlled_terms.AnalysisTechnique",
                "openminds.latest.controlled_terms.AnatomicalAxesOrientation",
                "openminds.latest.controlled_terms.AnatomicalCavity",
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
                "openminds.latest.controlled_terms.CommunicationInterfaceType",
                "openminds.latest.controlled_terms.CommunicationProtocol",
                "openminds.latest.controlled_terms.ContributionType",
                "openminds.latest.controlled_terms.CranialWindowConstructionType",
                "openminds.latest.controlled_terms.CranialWindowReinforcementType",
                "openminds.latest.controlled_terms.CriteriaQualityType",
                "openminds.latest.controlled_terms.DataType",
                "openminds.latest.controlled_terms.DependencyImpact",
                "openminds.latest.controlled_terms.DeploymentEnvironmentType",
                "openminds.latest.controlled_terms.DeviceMountingType",
                "openminds.latest.controlled_terms.DeviceType",
                "openminds.latest.controlled_terms.DifferenceMeasure",
                "openminds.latest.controlled_terms.Disease",
                "openminds.latest.controlled_terms.DiseaseModel",
                "openminds.latest.controlled_terms.EducationalLevel",
                "openminds.latest.controlled_terms.ElectricalStimulusType",
                "openminds.latest.controlled_terms.ExperimentalApproach",
                "openminds.latest.controlled_terms.ExternalBodyRegion",
                "openminds.latest.controlled_terms.FileBundleGrouping",
                "openminds.latest.controlled_terms.FileRepositoryType",
                "openminds.latest.controlled_terms.FileUsageRole",
                "openminds.latest.controlled_terms.GeneticStrainType",
                "openminds.latest.controlled_terms.GustatoryStimulusType",
                "openminds.latest.controlled_terms.Handedness",
                "openminds.latest.controlled_terms.Language",
                "openminds.latest.controlled_terms.Laterality",
                "openminds.latest.controlled_terms.LearningResourceType",
                "openminds.latest.controlled_terms.MRIFatSuppressionTechnique",
                "openminds.latest.controlled_terms.MRIParallelAcquisitionTechnique",
                "openminds.latest.controlled_terms.MRIPulseSequence",
                "openminds.latest.controlled_terms.MRISpoilingTechnique",
                "openminds.latest.controlled_terms.MRIWeighting",
                "openminds.latest.controlled_terms.MeasuredQuantity",
                "openminds.latest.controlled_terms.MeasuredSignalType",
                "openminds.latest.controlled_terms.MetaDataModelType",
                "openminds.latest.controlled_terms.ModelAbstractionLevel",
                "openminds.latest.controlled_terms.ModelScope",
                "openminds.latest.controlled_terms.ModificationConsentRequirement",
                "openminds.latest.controlled_terms.ModificationConstraint",
                "openminds.latest.controlled_terms.ModificationForm",
                "openminds.latest.controlled_terms.ModificationScope",
                "openminds.latest.controlled_terms.MolecularEntity",
                "openminds.latest.controlled_terms.MuscularStructure",
                "openminds.latest.controlled_terms.NervousSystemStructure",
                "openminds.latest.controlled_terms.OlfactoryStimulusType",
                "openminds.latest.controlled_terms.OperatingDevice",
                "openminds.latest.controlled_terms.OperatingSystem",
                "openminds.latest.controlled_terms.OperationalApproach",
                "openminds.latest.controlled_terms.OpticalStimulusType",
                "openminds.latest.controlled_terms.Organ",
                "openminds.latest.controlled_terms.OrganSystemStructure",
                "openminds.latest.controlled_terms.OrganismSubstance",
                "openminds.latest.controlled_terms.OrganismSystem",
                "openminds.latest.controlled_terms.OrganizationType",
                "openminds.latest.controlled_terms.PatchClampVariation",
                "openminds.latest.controlled_terms.PaymentModelType",
                "openminds.latest.controlled_terms.PreparationType",
                "openminds.latest.controlled_terms.ProgrammingLanguage",
                "openminds.latest.controlled_terms.ProjectType",
                "openminds.latest.controlled_terms.PublicationStatus",
                "openminds.latest.controlled_terms.PulseShape",
                "openminds.latest.controlled_terms.QualitativeOverlap",
                "openminds.latest.controlled_terms.SemanticDataType",
                "openminds.latest.controlled_terms.SetupType",
                "openminds.latest.controlled_terms.SignalDirectionality",
                "openminds.latest.controlled_terms.SkeletalStructure",
                "openminds.latest.controlled_terms.SoftwareApplicationCategory",
                "openminds.latest.controlled_terms.SoftwareFeature",
                "openminds.latest.controlled_terms.SovereignState",
                "openminds.latest.controlled_terms.SpatialEncoding",
                "openminds.latest.controlled_terms.Species",
                "openminds.latest.controlled_terms.StimulationApproach",
                "openminds.latest.controlled_terms.StimulationTechnique",
                "openminds.latest.controlled_terms.SubcellularEntity",
                "openminds.latest.controlled_terms.SubjectAttribute",
                "openminds.latest.controlled_terms.SupranationalBody",
                "openminds.latest.controlled_terms.TactileStimulusType",
                "openminds.latest.controlled_terms.Technique",
                "openminds.latest.controlled_terms.TermSuggestion",
                "openminds.latest.controlled_terms.Terminology",
                "openminds.latest.controlled_terms.TissueSampleAttribute",
                "openminds.latest.controlled_terms.TissueSampleType",
                "openminds.latest.controlled_terms.TissueStructure",
                "openminds.latest.controlled_terms.TypeOfUncertainty",
                "openminds.latest.controlled_terms.UnitOfMeasurement",
                "openminds.latest.controlled_terms.VascularStructure",
                "openminds.latest.controlled_terms.VisualStimulusType",
                "openminds.latest.controlled_terms.WeightType",
            ],
            "keyword",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Significant word or concept that are representative of the common coordinate framework version.",
            instructions="Add all relevant keywords to this research product version either by adding controlled terms or by suggesting new terms. This value overrides the inherited value from the version-independent product.",
        ),
        Property(
            "native_unit",
            "openminds.latest.controlled_terms.UnitOfMeasurement",
            "nativeUnit",
            required=True,
            description="Determinate quantity used in the original measurement.",
            instructions="Add the native unit that is used for this common coordinate framework version.",
        ),
        Property(
            "ontology_identifiers",
            str,
            "ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify the common coordinate framework version registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this common coordinate framework version.",
        ),
        Property(
            "publication_status",
            "openminds.latest.controlled_terms.PublicationStatus",
            "publicationStatus",
            description="no description available",
            instructions="Add the relevant publication status indicating the current lifecycle state of the resource (published, embargoed, disposed, retracted, etc.).",
        ),
        Property(
            "related_publications",
            [
                "openminds.latest.core.DOI",
                "openminds.latest.core.GenericIdentifier",
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
            instructions="Add all further publications besides the documentation that provide the original context for the production of this research product version (e.g., an original research article that used or produced the data of this research product version). This value overrides the inherited value from the version-independent product.",
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
            description="Shortened or fully abbreviated name of the common coordinate framework version.",
            instructions="Enter a short name (or alias) for this research product version that could be used as a shortened display title (e.g., for web services with too little space to display the full name). This value overrides the inherited value from the version-independent product.",
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
            instructions="Enter all channels through which a user can receive support for handling this research product version. This value overrides the inherited value from the version-independent product.",
        ),
        Property(
            "usage_conditions",
            ["openminds.latest.core.License", "openminds.latest.core.UsageAgreement"],
            "usageCondition",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all licenses and available data usage agreements applicable to this product version.",
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
            instructions="Add the specimen(s) that were used in the creation of this common coordinate framework version.",
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
            "version_specification",
            str,
            "versionSpecification",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter a short description (or summary) of the novelties/peculiarities of this research product version in comparison to its preceding versions. If this research product version is the first version, you can enter the following disclaimer 'This is the first version of this research product'.",
        ),
    ]

    def __init__(
        self,
        id=None,
        abbreviation=None,
        accessibility=None,
        anatomical_axes_orientation=None,
        axes_origins=None,
        contributions=None,
        contributor_affiliations=None,
        copyright=None,
        default_images=None,
        description=None,
        digital_identifier=None,
        documentation=None,
        full_name=None,
        funding=None,
        homepage=None,
        how_to_cite=None,
        is_preceded_by=None,
        is_variant_of=None,
        is_version_of=None,
        keywords=None,
        native_unit=None,
        ontology_identifiers=None,
        publication_status=None,
        related_publications=None,
        release_date=None,
        repository=None,
        short_name=None,
        support_channels=None,
        usage_conditions=None,
        used_specimens=None,
        version_identifier=None,
        version_specification=None,
    ):
        return super().__init__(
            id=id,
            abbreviation=abbreviation,
            accessibility=accessibility,
            anatomical_axes_orientation=anatomical_axes_orientation,
            axes_origins=axes_origins,
            contributions=contributions,
            contributor_affiliations=contributor_affiliations,
            copyright=copyright,
            default_images=default_images,
            description=description,
            digital_identifier=digital_identifier,
            documentation=documentation,
            full_name=full_name,
            funding=funding,
            homepage=homepage,
            how_to_cite=how_to_cite,
            is_preceded_by=is_preceded_by,
            is_variant_of=is_variant_of,
            is_version_of=is_version_of,
            keywords=keywords,
            native_unit=native_unit,
            ontology_identifiers=ontology_identifiers,
            publication_status=publication_status,
            related_publications=related_publications,
            release_date=release_date,
            repository=repository,
            short_name=short_name,
            support_channels=support_channels,
            usage_conditions=usage_conditions,
            used_specimens=used_specimens,
            version_identifier=version_identifier,
            version_specification=version_specification,
        )

    @classmethod
    def instances(cls):
        return [value for value in cls.__dict__.values() if isinstance(value, cls)]

    @classmethod
    def by_name(
        cls,
        name: str,
        match: str = "equals",
        all: bool = False,
        case_sensitive: bool = True,
    ):
        """
        Search for instances in the openMINDS instance library based on their name.

        This includes properties "name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation", and "synonyms".

        Note that not all metadata classes have a name.

        Args:
            name (str): a string to search for.
            match (str, optional): either "equals" (exact match - default), "contains"
                (the name-like property contains the given string), or "within"
                (the given string contains the name-like property).
            all (bool, optional): Whether to return all objects that match the name, or only the first. Defaults to False.
            case_sensitive (bool, optional): Whether the search should be case-sensitive. Defaults to True.
        """
        namelike_properties = ("name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation")
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                keys = []
                for prop_name in namelike_properties:
                    value = getattr(instance, prop_name, None)
                    if value is not None:
                        keys.append(value)
                if hasattr(instance, "synonyms"):
                    for synonym in instance.synonyms or []:
                        keys.append(synonym)
                for key in keys:
                    if key in cls._instance_lookup:
                        cls._instance_lookup[key].append(instance)
                    else:
                        cls._instance_lookup[key] = [instance]

        def normalize(s):
            return s if case_sensitive else s.casefold()

        if match == "equals":
            if case_sensitive:
                matches = cls._instance_lookup.get(name, [])
            else:
                matches = []
                for key, instances in cls._instance_lookup.items():
                    if key.casefold() == name.casefold():
                        matches.extend(instances)
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if normalize(name) in normalize(key):
                    matches.extend(instances)
        elif match == "within":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if normalize(key) in normalize(name):
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals', 'contains', or 'within'")
        if not matches:
            return None
        elif all:
            return list(dict.fromkeys(matches))
        else:
            return matches[0]


from . import common_coordinate_framework_version_instances as _  # noqa: F401
