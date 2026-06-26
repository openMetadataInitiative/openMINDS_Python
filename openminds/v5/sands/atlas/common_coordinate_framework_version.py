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
    schema_version = "v5.0"

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
            "openminds.v5.core.Accessibility",
            "accessibility",
            required=True,
            description="Level to which something is accessible to the common coordinate framework version.",
            instructions="Add the accessibility of the data for this research product version.",
        ),
        Property(
            "anatomical_axes_orientation",
            "openminds.v5.controlled_terms.AnatomicalAxesOrientation",
            "anatomicalAxesOrientation",
            required=True,
            description="Relation between reference planes used in anatomy and mathematics.",
            instructions="Add the axes orientation denoted in standard anatomical terms of direction (stated as XYZ) for the anatomical space of this common coordinate framework version.",
        ),
        Property(
            "axes_origins",
            "openminds.v5.core.QuantitativeValue",
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
            "openminds.v5.core.Contribution",
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
            "openminds.v5.core.Affiliation",
            "contributorAffiliation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all affiliations for the individual contributors to this research product version.",
        ),
        Property(
            "copyright",
            "openminds.v5.core.Copyright",
            "copyright",
            description="Exclusive and assignable legal right of an originator to reproduce, publish, sell, or distribute the matter and form of a creative work for a defined time period.",
            instructions="Enter the copyright information of this research product version.",
        ),
        Property(
            "default_images",
            "openminds.v5.core.File",
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
            ["openminds.v5.core.DOI", "openminds.v5.core.ISBN", "openminds.v5.core.RRID"],
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product version.",
        ),
        Property(
            "documentation",
            [
                "openminds.v5.core.DOI",
                "openminds.v5.core.File",
                "openminds.v5.core.ISBN",
                "openminds.v5.core.WebResource",
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
            "openminds.v5.core.Funding",
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
            "openminds.v5.sands.CommonCoordinateFrameworkVersion",
            "isPrecededBy",
            description="no description available",
            instructions="Add the common coordinate framework version preceding this common coordinate framework version.",
        ),
        Property(
            "is_variant_of",
            "openminds.v5.sands.CommonCoordinateFrameworkVersion",
            "isVariantOf",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all common coordinate framework versions that can be used alternatively to this common coordinate framework version.",
        ),
        Property(
            "is_version_of",
            "openminds.v5.sands.CommonCoordinateFramework",
            "isVersionOf",
            required=True,
            description="no description available",
            instructions="Add the version-independent information about this common coordinate framework.",
        ),
        Property(
            "keywords",
            [
                "openminds.v5.controlled_terms.AccessChannel",
                "openminds.v5.controlled_terms.AccessEligibilityType",
                "openminds.v5.controlled_terms.AccessForm",
                "openminds.v5.controlled_terms.AccessProcessType",
                "openminds.v5.controlled_terms.ActionStatusType",
                "openminds.v5.controlled_terms.AgeCategory",
                "openminds.v5.controlled_terms.AgeReference",
                "openminds.v5.controlled_terms.AnalysisTechnique",
                "openminds.v5.controlled_terms.AnatomicalAxesOrientation",
                "openminds.v5.controlled_terms.AnatomicalCavity",
                "openminds.v5.controlled_terms.AnatomicalIdentificationType",
                "openminds.v5.controlled_terms.AnatomicalPlane",
                "openminds.v5.controlled_terms.AnnotationCriteriaType",
                "openminds.v5.controlled_terms.AnnotationType",
                "openminds.v5.controlled_terms.AtlasType",
                "openminds.v5.controlled_terms.AuditoryStimulusType",
                "openminds.v5.controlled_terms.BiologicalOrder",
                "openminds.v5.controlled_terms.BiologicalProcess",
                "openminds.v5.controlled_terms.BiologicalSex",
                "openminds.v5.controlled_terms.BreedingType",
                "openminds.v5.controlled_terms.CellCultureType",
                "openminds.v5.controlled_terms.CellType",
                "openminds.v5.controlled_terms.ChemicalMixtureType",
                "openminds.v5.controlled_terms.Colormap",
                "openminds.v5.controlled_terms.CommunicationInterfaceType",
                "openminds.v5.controlled_terms.CommunicationProtocol",
                "openminds.v5.controlled_terms.ContributionType",
                "openminds.v5.controlled_terms.CranialWindowConstructionType",
                "openminds.v5.controlled_terms.CranialWindowReinforcementType",
                "openminds.v5.controlled_terms.CriteriaQualityType",
                "openminds.v5.controlled_terms.DataType",
                "openminds.v5.controlled_terms.DependencyImpact",
                "openminds.v5.controlled_terms.DeploymentEnvironmentType",
                "openminds.v5.controlled_terms.DeviceMountingType",
                "openminds.v5.controlled_terms.DeviceType",
                "openminds.v5.controlled_terms.DifferenceMeasure",
                "openminds.v5.controlled_terms.Disease",
                "openminds.v5.controlled_terms.DiseaseModel",
                "openminds.v5.controlled_terms.EducationalLevel",
                "openminds.v5.controlled_terms.ElectricalStimulusType",
                "openminds.v5.controlled_terms.ExperimentalApproach",
                "openminds.v5.controlled_terms.ExternalBodyRegion",
                "openminds.v5.controlled_terms.FileBundleGrouping",
                "openminds.v5.controlled_terms.FileRepositoryType",
                "openminds.v5.controlled_terms.FileUsageRole",
                "openminds.v5.controlled_terms.GeneticStrainType",
                "openminds.v5.controlled_terms.GustatoryStimulusType",
                "openminds.v5.controlled_terms.Handedness",
                "openminds.v5.controlled_terms.Language",
                "openminds.v5.controlled_terms.Laterality",
                "openminds.v5.controlled_terms.LearningResourceType",
                "openminds.v5.controlled_terms.MRIFatSuppressionTechnique",
                "openminds.v5.controlled_terms.MRIParallelAcquisitionTechnique",
                "openminds.v5.controlled_terms.MRIPulseSequence",
                "openminds.v5.controlled_terms.MRISpoilingTechnique",
                "openminds.v5.controlled_terms.MRIWeighting",
                "openminds.v5.controlled_terms.MeasuredQuantity",
                "openminds.v5.controlled_terms.MeasuredSignalType",
                "openminds.v5.controlled_terms.MetaDataModelType",
                "openminds.v5.controlled_terms.ModelAbstractionLevel",
                "openminds.v5.controlled_terms.ModelScope",
                "openminds.v5.controlled_terms.ModificationConsentRequirement",
                "openminds.v5.controlled_terms.ModificationConstraint",
                "openminds.v5.controlled_terms.ModificationForm",
                "openminds.v5.controlled_terms.ModificationScope",
                "openminds.v5.controlled_terms.MolecularEntity",
                "openminds.v5.controlled_terms.MuscularStructure",
                "openminds.v5.controlled_terms.NervousSystemStructure",
                "openminds.v5.controlled_terms.OlfactoryStimulusType",
                "openminds.v5.controlled_terms.OperatingDevice",
                "openminds.v5.controlled_terms.OperatingSystem",
                "openminds.v5.controlled_terms.OperationalApproach",
                "openminds.v5.controlled_terms.OpticalStimulusType",
                "openminds.v5.controlled_terms.Organ",
                "openminds.v5.controlled_terms.OrganSystemStructure",
                "openminds.v5.controlled_terms.OrganismSubstance",
                "openminds.v5.controlled_terms.OrganismSystem",
                "openminds.v5.controlled_terms.OrganizationType",
                "openminds.v5.controlled_terms.PatchClampVariation",
                "openminds.v5.controlled_terms.PaymentModelType",
                "openminds.v5.controlled_terms.PreparationType",
                "openminds.v5.controlled_terms.ProgrammingLanguage",
                "openminds.v5.controlled_terms.ProjectType",
                "openminds.v5.controlled_terms.PublicationStatus",
                "openminds.v5.controlled_terms.PulseShape",
                "openminds.v5.controlled_terms.QualitativeOverlap",
                "openminds.v5.controlled_terms.SemanticDataType",
                "openminds.v5.controlled_terms.SetupType",
                "openminds.v5.controlled_terms.SignalDirectionality",
                "openminds.v5.controlled_terms.SkeletalStructure",
                "openminds.v5.controlled_terms.SoftwareApplicationCategory",
                "openminds.v5.controlled_terms.SoftwareFeature",
                "openminds.v5.controlled_terms.SovereignState",
                "openminds.v5.controlled_terms.SpatialEncoding",
                "openminds.v5.controlled_terms.Species",
                "openminds.v5.controlled_terms.StimulationApproach",
                "openminds.v5.controlled_terms.StimulationTechnique",
                "openminds.v5.controlled_terms.SubcellularEntity",
                "openminds.v5.controlled_terms.SubjectAttribute",
                "openminds.v5.controlled_terms.SupranationalBody",
                "openminds.v5.controlled_terms.TactileStimulusType",
                "openminds.v5.controlled_terms.Technique",
                "openminds.v5.controlled_terms.TermSuggestion",
                "openminds.v5.controlled_terms.Terminology",
                "openminds.v5.controlled_terms.TissueSampleAttribute",
                "openminds.v5.controlled_terms.TissueSampleType",
                "openminds.v5.controlled_terms.TissueStructure",
                "openminds.v5.controlled_terms.TypeOfUncertainty",
                "openminds.v5.controlled_terms.UnitOfMeasurement",
                "openminds.v5.controlled_terms.VascularStructure",
                "openminds.v5.controlled_terms.VisualStimulusType",
                "openminds.v5.controlled_terms.WeightType",
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
            "openminds.v5.controlled_terms.UnitOfMeasurement",
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
            "openminds.v5.controlled_terms.PublicationStatus",
            "publicationStatus",
            description="no description available",
            instructions="Add the relevant publication status indicating the current lifecycle state of the resource (published, embargoed, disposed, retracted, etc.).",
        ),
        Property(
            "related_publications",
            [
                "openminds.v5.core.DOI",
                "openminds.v5.core.GenericIdentifier",
                "openminds.v5.core.HANDLE",
                "openminds.v5.core.ISBN",
                "openminds.v5.core.ISSN",
                "openminds.v5.publications.Book",
                "openminds.v5.publications.Chapter",
                "openminds.v5.publications.ScholarlyArticle",
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
            "openminds.v5.core.FileRepository",
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
            ["openminds.v5.core.License", "openminds.v5.core.UsageAgreement"],
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
                "openminds.v5.core.Subject",
                "openminds.v5.core.SubjectGroup",
                "openminds.v5.core.TissueSample",
                "openminds.v5.core.TissueSampleCollection",
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
    ):
        """
        Search for instances in the openMINDS instance library based on their name.

        This includes properties "name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation", and "synonyms".

        Note that not all metadata classes have a name.

        Args:
            name (str): a string to search for.
            match (str, optional): either "equals" (exact match - default) or "contains".
            all (bool, optional): Whether to return all objects that match the name, or only the first. Defaults to False.
        """
        namelike_properties = ("name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation")
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                keys = []
                for prop_name in namelike_properties:
                    if hasattr(instance, prop_name):
                        keys.append(getattr(instance, prop_name))
                if hasattr(instance, "synonyms"):
                    for synonym in instance.synonyms or []:
                        keys.append(synonym)
                for key in keys:
                    if key in cls._instance_lookup:
                        cls._instance_lookup[key].append(instance)
                    else:
                        cls._instance_lookup[key] = [instance]
        if match == "equals":
            matches = cls._instance_lookup.get(name, [])
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if not matches:
            return None
        elif all:
            return matches
        else:
            return matches[0]


from . import common_coordinate_framework_version_instances as _  # noqa: F401
