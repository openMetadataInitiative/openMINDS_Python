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


CommonCoordinateFramework.amb_ccf = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/AMB-CCF",
    abbreviation="AMB CCF",
    description="The 'Allen Mouse Brain Common Coordinate Framework' is a 3D reconstruction of an averaged adult mouse brain.",
    full_name="Allen Mouse Brain Common Coordinate Framework",
    homepage=IRI("https://portal.brain-map.org/"),
    short_name="Allen Mouse Brain CCF",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/musMusculus"},
)
CommonCoordinateFramework.big_brain = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/BigBrain",
    abbreviation="BigBrain",
    description="The 'BigBrain Whole-Brain Model' is a 3D reconstruction of a human brain in extremely high resolution.",
    full_name="BigBrain Whole-Brain Model",
    homepage=IRI("https://bigbrainproject.org/"),
    short_name="BigBrain Model",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/homoSapiens"},
)
CommonCoordinateFramework.fs_lr = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/fsLR",
    abbreviation="fsLR",
    description="The 'Unbiased FsAverage Left–Right Hybrid Surface Space' (fsLR) brings the left and right fsaverage surfaces into geographic correspondence using Landmark-SBR ([Van Essen et al. 2011](https://doi.org/10.1093/cercor/bhr291)).",
    full_name="Unbiased FsAverage Left–Right Hybrid Surface Space",
    short_name="fsLR Surface Space",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/homoSapiens"},
)
CommonCoordinateFramework.fsaverage = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/fsaverage",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    short_name="FsAverage Surface Space",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/homoSapiens"},
)
CommonCoordinateFramework.marmoset_nmt = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/MarmosetNMT",
    abbreviation="MarmosetNMT",
    description="Stereotactic coordinate space of the coronal plane generated using computational average of histology sections.",
    full_name="The Marmoset Nencki-Monash Template in Stereotaxic Coordinates",
    homepage=IRI("https://www.marmosetbrain.org/nencki_monash_template"),
    how_to_cite="Please refer to the template by its RRID:SCR_018367, and cite the publication of the version of the template you have used.",
    short_name="Marmoset Nencki-Monash Template",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/callithrixJacchus"},
)
CommonCoordinateFramework.mebrain_stemplate = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/MEBRAINStemplate",
    abbreviation="MEBRAINStemplate",
    description="The 'MEBRAINS population-based monkey brain template' is a multi-subject based, multi-modal, volume and surface brain template for macaque monkeys.",
    full_name="MEBRAINS population-based monkey brain template",
    short_name="MEBRAINS brain template",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/macacaMulatta"},
)
CommonCoordinateFramework.mni__colin27 = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/MNI-Colin27",
    abbreviation="MNI-Colin27",
    description="The 'MNI Colin 27 Average Brain Stereotaxic Registration Model' is a stereotaxic average of 27 T1-weighted MRI scans of the same individual. It was created at the Montreal Neurological Institute (MNI) in a two step process: (1) each of the 27 T1-weighted scans were registered to stereotaxic space using MRITOTAL (an automated volumetric registration procedure) and resampled onto a 1mm grid. All 27 scans were averaged together to create an initial average. (2) The initial average volume was used as a target for a second phase of registration where each original T1-weighted MRI was re-registered in stereotaxic space. This two-step procedure has the advantage of removing the small variance in intra-subject mapping in stereotaxic space associated with the use of a multi-subject average resulting in an average brain stereotaxic registration model with high signal-to-noise ratio and structure definition.",
    full_name="MNI Colin27 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases"),
    how_to_cite="Holmes CJ, Hoge R, Collins L, Woods R, Toga AW, and Evans AC; 'Enhancement of MR images using registration for signal averaging.'; J Comput Assist Tomogr; 1998 Mar-Apr; 22(2):324–333. [doi: 10.1097/00004728-199803000-00032](http://dx.doi.org/10.1097/00004728-199803000-00032) Aubert-Broche B, Evans AC, and Collins DL; 'A new improved version of the realistic digital brain phantom'; NeuroImage; 2006 Aug;32(1):138–145. [doi: 10.1016/j.neuroimage.2006.03.052](https://doi.org/10.1016/j.neuroimage.2006.03.052)",
    short_name="MNI Colin27 Average Brain",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/homoSapiens"},
)
CommonCoordinateFramework.mni_icbm152 = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/MNI-ICBM152",
    abbreviation="ICBM152",
    description="The 'MNI ICBM152 Average Brain Stereotaxic Registration Model' is an average of T1-weighted magnetic resonance imaging (MRI) scans from 152 normative young adults.",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases"),
    short_name="MNI ICBM152",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/homoSapiens"},
)
CommonCoordinateFramework.p__marmoset_bsc_cor_t = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/P-MarmosetBSC-corT",
    abbreviation="P-MarmosetBSC-corT",
    description="Stereotactic coordinate space of the coronal plane.",
    full_name="Paxinos et al. Coronal Template of the Marmoset Brain in Stereotaxic Coordinates",
    homepage=IRI("http://www.neura.edu.au/research/themes/paxinos-group"),
    short_name="Paxinos et al. Stereotaxic Coronal Template (Marmoset Brain)",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/callithrixJacchus"},
)
CommonCoordinateFramework.pw_rbsc_cor_t = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/PW-RBSC-corT",
    abbreviation="PW-RBSC-corT",
    description="Stereotactic coordinate space of the coronal plane.",
    full_name="Paxinos and Watson's Coronal Template of the Rat Brain in Stereotaxic Coordinates",
    short_name="Paxinos and Watson's Stereotaxic Coronal Template (Rat Brain)",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/rattusNorvegicus"},
)
CommonCoordinateFramework.swanson_srb = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/SwansonSRB",
    abbreviation="SwansonSRB",
    description="Stereotactic coordinate system derived from the atlas by Paxinos and Watson (1986; ISBN: 0-12-547621-3).",
    full_name="Swanson's Stereotactic Brain of the Sprague Dawley Rat",
    short_name="Swanson's Stereotactic Rat Brain",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/rattusNorvegicus"},
)
CommonCoordinateFramework.whssd = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/WHSSD",
    abbreviation="WHSSD",
    description="The 'Waxholm Space of the Sprague Dawley Rat Brain (coordinate space)' employs a continuous three- dimensional Cartesian coordinate system, with its origin set at the decussation of the anterior commissure.",
    full_name="Waxholm Space of the Sprague Dawley Rat Brain (coordinate space)",
    homepage=IRI("https://www.nitrc.org/projects/whs-sd-atlas"),
    short_name="WHS of the SD Rat Brain",
    used_taxon={"@id": "https://openminds.om-i.org/instances/species/rattusNorvegicus"},
)
