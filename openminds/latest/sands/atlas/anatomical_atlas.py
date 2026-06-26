"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class AnatomicalAtlas(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/AnatomicalAtlas"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this anatomical atlas.",
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
            instructions="Add all individual, organisational, or consortial contributions to this research product. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "contributor_affiliations",
            "openminds.latest.core.Affiliation",
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
            description="Longer statement or account giving the characteristics of the anatomical atlas.",
            instructions="Enter a description (or abstract) of this research product. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "digital_identifier",
            ["openminds.latest.core.DOI", "openminds.latest.core.ISBN", "openminds.latest.core.RRID"],
            "digitalIdentifier",
            description="Digital handle to identify objects or legal persons.",
            instructions="Add the globally unique and persistent digital identifier of this research product. Note that this digital identifier will be used to reference all attached research product versions.",
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
            description="no description available",
            instructions="Add the publication or file that acts as the documentation of this research product. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "full_name",
            str,
            "fullName",
            formatting="text/plain",
            required=True,
            description="Whole, non-abbreviated name of the anatomical atlas.",
            instructions="Enter a descriptive full name (or title) for this research product. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "has_terminology",
            "openminds.latest.sands.ParcellationTerminology",
            "hasTerminology",
            required=True,
            description="no description available",
            instructions="Enter the parcellation terminology of this anatomical atlas.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of the anatomical atlas.",
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
            description="Significant word or concept that are representative of the anatomical atlas.",
            instructions="Add all relevant keywords to this research product either by adding controlled terms or by suggesting new terms. Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "ontology_identifier",
            IRI,
            "ontologyIdentifier",
            description="Term or code used to identify the anatomical atlas registered within a particular ontology.",
            instructions="Enter the internationalized resource identifier (IRI) to the related ontological term matching this anatomical atlas.",
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
            instructions="Add all further publications besides the documentation that provide the original context for the production of this research product (e.g., an original research article that used or produced the data of this research product). Inherited by all product versions unless overridden at the version level.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of the anatomical atlas.",
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
            ["openminds.latest.controlled_terms.BiologicalOrder", "openminds.latest.controlled_terms.Species"],
            "usedTaxon",
            required=True,
            description="no description available",
            instructions="Add the taxon (e.g., species) that was used for the creation of this anatomical atlas.",
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
        has_terminology=None,
        homepage=None,
        how_to_cite=None,
        keywords=None,
        ontology_identifier=None,
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
            has_terminology=has_terminology,
            homepage=homepage,
            how_to_cite=how_to_cite,
            keywords=keywords,
            ontology_identifier=ontology_identifier,
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


from . import anatomical_atlas_instances as _  # noqa: F401
