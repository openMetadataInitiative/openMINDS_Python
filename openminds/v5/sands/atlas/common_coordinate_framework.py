"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class CommonCoordinateFramework(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CommonCoordinateFramework"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v5.0"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this common coordinate framework.",
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
            instructions="Add all individual, organisational, or consortial contributions to this research product. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "contributor_affiliations",
            "openminds.v5.core.Affiliation",
            "contributorAffiliation",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all affiliations for the individual contributors to this research product. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of the common coordinate framework.",
            instructions="Enter a description (or abstract) of this research product. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "digital_identifier",
            ["openminds.v5.core.DOI", "openminds.v5.core.ISBN", "openminds.v5.core.RRID"],
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.",
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
            description="no description available",
            instructions="Add the publication or file that acts as the documentation of this research product. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of the common coordinate framework.",
            instructions="Enter a descriptive full name (or title) for this research product. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of the common coordinate framework.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "how_to_cite",
            str,
            "howToCite",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Preferred format for citing a particular object or legal person.",
            instructions="Enter the preferred citation text for this research product. Leave blank if citation text can be extracted from the assigned digital identifier.",
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
            description="Significant word or concept that are representative of the common coordinate framework.",
            instructions="Add all relevant keywords to this research product either by adding controlled terms or by suggesting new terms. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "ontology_identifiers",
            str,
            "ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify the common coordinate framework registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this common coordinate framework.",
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
            instructions="Add all further publications besides the documentation that provide the original context for the production of this research product (e.g., an original research article that used or produced the data of this research product). Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of the common coordinate framework.",
            instructions="Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name). Inherited by all product versions unless overridden at the version level.",
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
            instructions="Enter all channels through which a user can receive support for handling this research product. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "used_taxon",
            ["openminds.v5.controlled_terms.BiologicalOrder", "openminds.v5.controlled_terms.Species"],
            "usedTaxon",
            required=True,
            description="no description available",
            instructions="Add the taxon (e.g., species) that was used for the creation of this common coordinate framework.",
        ),
    ]

    def __init__(
        self,
        id=None,
        abbreviation=None,
        contributions=None,
        contributor_affiliations=None,
        description=None,
        digital_identifier=None,
        documentation=None,
        full_name=None,
        homepage=None,
        how_to_cite=None,
        keywords=None,
        ontology_identifiers=None,
        related_publications=None,
        short_name=None,
        support_channels=None,
        used_taxon=None,
    ):
        return super().__init__(
            id=id,
            abbreviation=abbreviation,
            contributions=contributions,
            contributor_affiliations=contributor_affiliations,
            description=description,
            digital_identifier=digital_identifier,
            documentation=documentation,
            full_name=full_name,
            homepage=homepage,
            how_to_cite=how_to_cite,
            keywords=keywords,
            ontology_identifiers=ontology_identifiers,
            related_publications=related_publications,
            short_name=short_name,
            support_channels=support_channels,
            used_taxon=used_taxon,
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


from . import common_coordinate_framework_instances as _  # noqa: F401
