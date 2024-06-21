"""
Structured information on a brain atlas (concept level).
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class BrainAtlas(LinkedMetadata):
    """
    Structured information on a brain atlas (concept level).
    """

    type_ = "https://openminds.ebrains.eu/sands/BrainAtlas"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this brain atlas.",
        ),
        Property(
            "authors",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "author",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this brain atlas as authors.",
        ),
        Property(
            "custodians",
            ["openminds.latest.core.Consortium", "openminds.latest.core.Organization", "openminds.latest.core.Person"],
            "custodian",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="The 'custodian' is a legal person who is responsible for the content and quality of the data, metadata, and/or code of a research product.",
            instructions="Add all parties that fulfill the role of a custodian for this research product (e.g., a research group leader or principle investigator). Custodians are typically the main contact in case of misconduct, obtain permission from the contributors to publish personal information, and maintain the content and quality of the data, metadata, and/or code of the research product. Unless specified differently, this custodian will be responsible for all attached research product versions.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            required=True,
            description="Longer statement or account giving the characteristics of the brain atlas.",
            instructions="Enter a description (or abstract) of this research product. Note that this should be a suitable description for all attached research product versions.",
        ),
        Property(
            "digital_identifier",
            ["openminds.latest.core.DOI", "openminds.latest.core.ISBN", "openminds.latest.core.RRID"],
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
            description="Whole, non-abbreviated name of the brain atlas.",
            instructions="Enter a descriptive full name (or title) for this research product. Note that this should be a suitable full name for all attached research product versions.",
        ),
        Property(
            "has_terminology",
            "openminds.latest.sands.ParcellationTerminology",
            "hasTerminology",
            required=True,
            description="no description available",
            instructions="Enter the parcellation terminology of this brain atlas.",
        ),
        Property(
            "has_versions",
            "openminds.latest.sands.BrainAtlasVersion",
            "hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to variants of an original.",
            instructions="Add versions of this brain atlas.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of the brain atlas.",
            instructions="Enter the internationalized resource identifier (IRI) to the homepage of this research product.",
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
            "ontology_identifier",
            IRI,
            "ontologyIdentifier",
            description="Term or code used to identify the brain atlas registered within a particular ontology.",
            instructions="Enter the internationalized resource identifier (IRI) to the related ontological term matching this brain atlas.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of the brain atlas.",
            instructions="Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
        Property(
            "used_species",
            "openminds.latest.controlled_terms.Species",
            "usedSpecies",
            description="no description available",
            instructions="Add the species that was used for the creation of this brain atlas.",
        ),
    ]

    def __init__(
        self,
        id=None,
        abbreviation=None,
        authors=None,
        custodians=None,
        description=None,
        digital_identifier=None,
        full_name=None,
        has_terminology=None,
        has_versions=None,
        homepage=None,
        how_to_cite=None,
        ontology_identifier=None,
        short_name=None,
        used_species=None,
    ):
        return super().__init__(
            id=id,
            abbreviation=abbreviation,
            authors=authors,
            custodians=custodians,
            description=description,
            digital_identifier=digital_identifier,
            full_name=full_name,
            has_terminology=has_terminology,
            has_versions=has_versions,
            homepage=homepage,
            how_to_cite=how_to_cite,
            ontology_identifier=ontology_identifier,
            short_name=short_name,
            used_species=used_species,
        )

    @classmethod
    def instances(cls):
        return [value for value in cls.__dict__.values() if isinstance(value, cls)]

    @classmethod
    def by_name(cls, name):
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                cls._instance_lookup[instance.name] = instance
                if instance.synonyms:
                    for synonym in instance.synonyms:
                        cls._instance_lookup[synonym] = instance
        return cls._instance_lookup[name]


BrainAtlas.aal1 = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/AAL1",
    abbreviation="AAL1",
    full_name="Automated Anatomical Labeling Atlas 1",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": [
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_centralRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PRE"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_POST"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_RO"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F3OP"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F3T"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F1M"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_SMA"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PCL"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F1O"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F1MO"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F2O"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F3O"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_GR"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_OC"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_temporalLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_T1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_HES"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_T2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_T3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_parietalLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_P1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_P2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_AG"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_SMG"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PQ"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_occipitalLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_O1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_O2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_O3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_Q"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_V1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_LING"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_FUSI"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_limbicLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_T1P"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_T2P"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_ACIN"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_MCIN"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PCIN"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_HIP"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PHIP"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_IN"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_subcorticalGrayNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_AMYG"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_CAU"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PUT"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PAL"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_THA"},
        ],
        "ontologyIdentifier": None,
    },
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/AAL1_SPM12-v4"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/AAL1_SPM8-v1"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/AAL1_SPM5-vbeta2"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/AAL1_SPM2-vbeta1"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/AAL1_SPM99-vbeta2"},
    ],
    homepage=IRI("https://www.gin.cnrs.fr/en/tools/aal/"),
    short_name="AAL Atlas 1",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/homoSapiens"},
)
BrainAtlas.amba = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/AMBA",
    abbreviation="AMBA",
    full_name="Allen Mouse Brain Atlas",
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/AMBA_CCFv3-2015"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/AMBA_CCFv3-2017"},
    ],
    homepage=IRI("https://portal.brain-map.org/"),
    short_name="Allen Mouse Brain Atlas",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/musMusculus"},
)
BrainAtlas.aseg_atlas = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/AsegAtlas",
    abbreviation="Aseg Atlas",
    description="The Automated Segmentation Atlas of the Human Brain is an automated whole brain segmentation that is based on probabilistic information on the location of structures of a manual labeled training set (cf., [Fischl et al., 2002](https://doi.org/10.1016/S0896-6273(02)00569-X)).",
    full_name="Automated Segmentation Atlas of the Human Brain",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": [
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_cerebralWhiteMatter"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_cerebralCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_lateralVentricle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_inferiorLateralVentricle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_cerebellumWhiteMatter"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_cerebellumCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_thalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_caudate"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_putamen"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_pallidum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_hippocampus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_amygdala"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_lesion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_accumbensArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_ventralDiencephalon"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_vessel"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_thirdVentricle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_fourthVentricle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_brainStem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_cerebrospinalFluid"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_unknown"},
        ],
        "ontologyIdentifier": None,
    },
    short_name="Automated Segmentation Atlas",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/homoSapiens"},
)
BrainAtlas.ba_human = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/BA-human",
    abbreviation="BA-human",
    full_name="Brodmann Cortical Parcellation Scheme (human)",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": [
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA4"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA5"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA6"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA7"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA8"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA8a"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA9"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA10"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA11"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA12"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA13"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA14"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA15"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA16"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA17"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA18"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA19"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA20"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA21"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA22"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA23"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA24"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA25"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA26"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA27"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA28"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA29"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA30"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA31"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA32"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA33"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA34"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA35"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA36"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA37"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA38"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA39"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA40"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA41"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA42"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA43"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA44"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA45"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA46"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA47"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA48"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA52"},
        ],
        "ontologyIdentifier": None,
    },
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/BA-human_1909"}],
    short_name="Brodmann Areas (human)",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/homoSapiens"},
)
BrainAtlas.dka = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/DKA",
    abbreviation="DKA",
    full_name="Desikan-Killiany Atlas",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": [
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_anteriorCingulateCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_banksOfSuperiorTemporalSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_caudalAnteriorCingulateCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_caudalMiddleFrontalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cerebralCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cingulateCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_corpusCallosum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cuneusCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_entorhinalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_frontalLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_frontalPole"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_fusiformGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_inferiorFrontalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_inferiorParietalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_inferiorTemporalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_insula"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_isthmusOfCingulateCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_lateralOccipitalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_lateralOrbitalFrontalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_lingualGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_medialOrbitalFrontalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_middleFrontalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_middleTemporalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_occipitalLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_orbitofrontalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parahippocampalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_paracentralLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parietalLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parsOpercularis"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parsOrbitalis"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parsTriangularis"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_pericalcarineCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_postcentralGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_posteriorCingulateCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_precentralGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_precuneusCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_rostralAnteriorCingulateCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_rostralMiddleFrontalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_superiorFrontalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_superiorParietalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_superiorTemporalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_supramarginalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_medialAspect"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_lateralAspect"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalPole"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_transverseTemporalCortex"},
        ],
        "ontologyIdentifier": None,
    },
    short_name="DK Atlas",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/homoSapiens"},
)
BrainAtlas.dwma = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/DWMA",
    abbreviation="DWMA",
    full_name="Atlas of Deep White Matter Fibre Bundles",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": [
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_anteriorSegementOfArcuateFasciculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_arcuateFasciculus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_cingulum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_corticospinalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_deepWhiteMatter"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_directSegementOfArcuateFasciculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_fornix"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_inferiorFronto-occipitalFasciculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_inferiorLongitudinalFasciculus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_longCingulateFibres"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_posteriorSegementOfArcuateFasciculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_shortCingulateFibres"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_temporalCingulateFibres"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_uncinateFasciculus"},
        ],
        "ontologyIdentifier": None,
    },
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/DWMA_2018"}],
    short_name="Deep White Matter Atlas",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/homoSapiens"},
)
BrainAtlas.julich__brain_atlas = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/Julich-BrainAtlas",
    abbreviation="JBA",
    description="The Julich-Brain Atlas is a three-dimensional atlas of the human brain. It integrates high-resolution cytoarchitectonic maps with microstructural and connectivity data as well as neurotransmitter receptor expression profiles and functional data. It is available in the common reference spaces MNI ICBM 152 (2009c Nonlinear Asymmetric), Colin 27 and FreeSurfer fsaverage surface space.  Furthermore, many maps are also available in the BigBrain high-resolution reference space. It is continuously expanded and openly accessible for researchers to systematically integrate multi-level data. It is interoperable in a way that it can be linked with other brain parcellations, databases and mapping projects. The Julich Brain Atlas offers a powerful tool for neuroscience and medicine alike and has been adopted as central element of the multilevel human brain atlas for the EBRAINS infrastructure, see [EBRAINS Human Brain Atlas](https://www.ebrains.eu/tools/human-brain-atlas).",
    digital_identifier={"@id": "https://scicrunch.org/resolver/RRID:SCR_023277"},
    full_name="Julich-Brain Cytoarchitectonic Atlas",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": [
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_AcbL"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_AcbM"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-25"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-25.25a"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-25.25p"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-33"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-3a"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-3b"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-44"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-45"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-4a"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-4p"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-5Ci"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-5L"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-5M"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-6d1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-6d2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-6d3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-6ma"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-6mp"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-7A"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-7M"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-7P"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-7PC"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-8d1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-8d2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-8v1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-8v2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-CoS1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-FG1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-FG2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-FG3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-FG4"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo4"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo5"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo6"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo7"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fp1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fp2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFJ1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFJ2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFS1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFS2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFS3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFS4"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ia"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ia1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ia2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ia3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id10"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id4"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id5"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id6"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id7"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id8"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id9"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ig1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ig2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ig3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-MFG1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-MFG2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP4"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP5"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP6"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP7"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP8"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP9"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PF"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PFcm"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PFm"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PFop"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PFt"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PGa"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PGp"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ph1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ph2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ph3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-SFS1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-SFS2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-STS1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-STS2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-1.0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-1.1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-1.2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-2.1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-2.2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TI"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TPJ"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TeI"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-a29"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-a30"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP4"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP5"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP6"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP7"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP8"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc3d"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc3v"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc4d"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc4la"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc4lp"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc4v"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc5"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc6"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hPO1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-i29"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-i30"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24ab"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24ab.p24a"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24ab.p24b"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24c"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24c.pd24cd"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24c.pd24cv"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24c.pv24c"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p29"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p30"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p32"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-s24"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-s24.s24a"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-s24.s24b"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-s32"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_BST"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CA"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CA1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CA2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CA3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam4"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam5"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam6"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGM"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGM.CGMd"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGM.CGMm"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGM.CGMv"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CM"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CM.AAA"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CM.Ce"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CM.Me"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Ch-123"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Ch-4"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_DG"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Dorsal-Dentate-Nucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Entorhinal-Cortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Fastigial-Nucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-I"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-II"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-to-Occipital"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-to-Temporal"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-to-Temporal-I"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-to-Temporal-II"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_FuCd"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_FuP"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_HATA"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_HC-Transsubiculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_HeschlsGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_IF"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_IF.ice"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_IF.iol"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_IF.ld"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Interposed-Nucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB.Bl"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB.Bm"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB.La"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB.Pl"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_MF"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_MF.icm"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_MF.lm"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_SF"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_SF.AHi"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_SF.APir"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_SF.VCo"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_STN"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum.PaS"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum.PreS"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum.ProS"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum.Sub"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Temporal-to-Parietal"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Terminal-islands"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Tuberculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_VP"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_VTM"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Ventral-Dentate-Nucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_agranularInsula"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_amygdala"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_amygdaloidGroups"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_basalForebrain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_basalGanglia"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_brain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebellarNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebellum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cingulateGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_collateralSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dentateNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_diencephalon"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dorsalOccipitalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dorsalPrecentralGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fiberMasses"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalCingulateGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalOperculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalPole"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fronto-marginalSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fusiformGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_granularInsula"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_hippocampalFormation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorParietalLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_insula"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_intraparietalSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_lateralOccipitalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_lateralOrbitofrontalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_limbicLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_magnocellularGroup"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_medialOrbitofrontalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_mesialPrecentralGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_metathalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_metencephalon"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_middleFrontalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_occipitalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_occipitalLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_olfactoryCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parahippocampalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalOperculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parieto-occipitalSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_postcentralGyrus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_posteriorMedialSuperiorFrontalGyrus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_precentralGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_retrosplenialPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_sublenticularPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_subthalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorFrontalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorFrontalSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorParietalLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorTemporalGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorTemporalSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_telencephalon"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalInsula"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporo-parietalJunction"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_thalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_ventralOccipitalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_ventralStriatum"},
        ],
        "ontologyIdentifier": None,
    },
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v1.13-Colin27"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v1.18-Colin27"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v1.18-MNI152"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v2.2-Colin27"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v2.2-MNI152"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v2.4-Colin27"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v2.4-MNI152"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v2.5-Colin27"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v2.5-MNI152"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v2.6-MNI152"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v2.9-BigBrain"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v2.9-Colin27"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v2.9-fsaverage"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v2.9-MNI152"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0-BigBrain"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0-Colin27"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0-fsaverage"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0-MNI152"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.1-BigBrain"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.1-Colin27"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.1-fsaverage"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.1-MNI152"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.2-BigBrain"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.2-Colin27"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.2-fsaverage"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.2-MNI152"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.3-BigBrain"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.3-Colin27"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.3-fsaverage"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/JBA_v3.0.3-MNI152"},
    ],
    homepage=IRI("https://julich-brain-atlas.de/"),
    how_to_cite="Please refer to the atlas by its [RRID:SCR_023277](https://scicrunch.org/resolver/SCR_023277), and cite the two main publications [Amunts and Zilles (2015)](https://doi.org/10.1016/j.neuron.2015.12.001) AND [Amunts et al. (2020)](https://doi.org/10.1126/science.abb4588) along with the atlas version(s) you have used.",
    short_name="Julich-Brain Atlas",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/homoSapiens"},
)
BrainAtlas.pw_rbsc_cor = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/PW-RBSC-cor",
    abbreviation="PW-RBSC-cor",
    description="Paxinos and Watson's stereotaxic rat brain atlases are based on the study of 130 adult male Wistar rats. The atlases have a stereotactic reference system, in a flat-skull position with bregma and lambda as reference points, photographs of rat brain sections in the coronal plane, and contain diagrams showing delineated brain structures based on the previously mentioned photographs.",
    full_name="Paxinos and Watson's The Rat Brain in Stereotaxic Coordinates - Coronal Plates",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": [
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_10thCerebellarLobuleNodule"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_1stCerebellarLobuleLingula"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_2bCerebellarLobule"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_2ndAnd3rdCerebellarLobules"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_2ndCerebellarLobule"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_3rdAnd4thCerebellarLobules"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_3rdCerebellarLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_3rdVentricle"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_4thAnd5thCerebellarLobules"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_4thCerebellarLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_4thVentricle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_5thCerebellarLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_6aCerebellarLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_6bCerebellarLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_6cCerebellarLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_6thCerebellarLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_7thCerebellarLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_8thCerebellarLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_9thCerebellarLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_9thCerebellarLobuleA"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_9thCerebellarLobuleAAndB"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_9thCerebellarLobuleB"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_9thCerebellarLobuleC"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_A11dopamineCells"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_A13DopamineCells"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_A1NoradrenalineCells"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_A1NoradrenalineCellsC1AdrenalineCells"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_A2NoradrenalineCells"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_A5NoradrenalineCells"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_A7NoradrenalineCells"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_B9SerotoninCells"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_BarringtonsNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_BotzingerComplex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_C1AdrenalineCells"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_C1AdrenalineCellsAndA1NoradrenalineCells"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_C2AdrenalineCells"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_C3AdrenalineCells"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_EdingerWestphalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_FCellGroupOfTheVestibularComplex"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_KillikerFuseNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_PurkinjeCellLayerOfTheCerebellum"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_abducensNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_abducensNucleusRetractorBulbiPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_accessoryAbducensFacialNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_accessoryNerveNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_accessoryNeurosecretoryNuclei"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_accessoryOlfactoryBulb"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_accessoryOlfactoryTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_accumbensNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_accumbensNucleusCore"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_accumbensNucleusShell"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_agranularInsularCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_agranularInsularCortexDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_agranularInsularCortexPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_agranularInsularCortexVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_alarNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_alveusOfTheHippocampus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ambiguusNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ambiguusNucleusCompactPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ambiguusNucleusLoosePart"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ambiguusNucleusSubcompactPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_amygdalohippocampalArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_amygdalohippocampalAreaAnterolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_amygdalohippocampalAreaPosterolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_amygdalohippocampalAreaPosteromedialPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_amygdaloidFissure"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_amygdaloidIntramedullaryGray"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_amygdalopiriformTransitionArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_amygdalostriatalTransitionArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_angularThalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ansoparamedianFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorAmygdaloidArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorCerebralArtery"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorCommissuralNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorCommissure"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorCommissureAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorCommissureIntrabulbarPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorCommissurePosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorCorticalAmygdaloidNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorHypothalamicArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorHypothalamicAreaAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorHypothalamicAreaCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorHypothalamicAreaPosteriorPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorLobeOfPituitary"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorOlfactoryNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorOlfactoryNucleusExternalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorOlfactoryNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorOlfactoryNucleusMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorOlfactoryNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorOlfactoryNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorOlfactoryNucleusVentroposteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorPerifornicalNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorPretectalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorPretectalNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorPretectalNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorSpinalArtery"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteriorTegmentalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anterodorsalThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteromedialThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteromedialThalamicNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteroventThalamicNucleusDorsomedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteroventralPeriventricularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteroventralThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_anteroventralThalamicNucleusVentrolateralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_aqueduct"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_arcuateHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_arcuateHypothalamicNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_arcuateHypothalamicNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_arcuateHypothalamicNucleusLateroposteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_arcuateHypothalamicNucleusMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_arcuateHypothalamicNucleusMedialPosteriorPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_areaPostrema"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_artery"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ascendingFibersOfTheFacialNerve"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_azygousAnteriorCerebralArtery"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_azygousPericallosalArtery"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_basalNucleusCompactPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_basalNucleusMeynert"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_basilarArtery"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_basolateralAmygdaloidNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_basolateralAmygdaloidNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_basolateralAmygdaloidNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_basolateralAmygdaloidNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_basomedialAmygdaloidNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_basomedialAmygdaloidNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfStriaTerminalisFusiformPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfStriaTerminalisSupracapsularDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfStriaTerminalisSupracapsularDivisionLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfStriaTerminalisSupracapsularDivisionMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheAccessoryOlfactoryTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheAnteriorCommissure"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisIntermediateDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisIntraamygdaloidDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisLateralDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisLateralDivisionDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisLateralDivisionIntermediatePart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisLateralDivisionJuxtacapsularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisLateralDivisionPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisLateralDivisionVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisMedialDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisMedialDivisionAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisMedialDivisionAnterolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisMedialDivisionAnteromedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisMedialDivisionPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisMedialDivisionPosterointermediatePart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisMedialDivisionPosterolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisMedialDivisionPosteromedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_bedNucleusOfTheStriaTerminalisMedialDivisionVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_brachiumOfTheInferiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_brachiumOfTheSuperiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_caudalInterstitialNucleusOfTheMedialLongitudinalFasciculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_caudalLinearNucleusOfTheRaphe"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_caudalPeriolivaryNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_caudatePutamenStriatum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_caudomedialEntothinalCortex"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_caudoventrolateralReticularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cellBridgesOfTheVentralStriatum"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralAmygdaloidNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralAmygdaloidNucleusCapsularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralAmygdaloidNucleusLateralDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralAmygdaloidNucleusMedialDivision"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralCanal"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralCervicalNucleusOfTheSpinalCord"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralGray"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralGrayAlphaPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralGrayBetaPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralGrayGammaPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralGrayNucleusO"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralGrayOfThePons"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralMedialThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centralNucleusOfTheInferiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_centrolateralThalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cerebellarCommissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cerebellarWhiteMatter"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cerebellum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cerebralCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cerebralPeduncle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_choroidPlexus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cingulateCortexArea1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cingulateCortexArea2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cingulum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_circularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_claustrum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cochlearRootOfTheVestibulocochlearNerve"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_commissuralNucleusOfTheInferiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_commissuralStriaTerminalis"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_commissureOfTheInferiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_commissureOfTheLateralLemniscus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_commissureOfTheSuperiorColliculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_conterminalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_copulaOfThePyramis"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_corpusCallosum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cortexAmygdalaTransitionZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cortexAmygdalaTransitionZoneLayer1"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_crus1OfTheAnsiformLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_crus2OfTheAnsiformLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cuneateFasciculus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cuneateNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cuneateNucleusRotundusPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cuneiformNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cuneiformNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cuneiformNucleusIntermediatePart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_cuneiformNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_decussationOfTheSuperiorCerebellarPeduncle"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_decussationOfTheTrapezoidBody"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_deepCerebralWhiteMatter"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_deepGrayLayerOfTheSuperiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_deepWhiteLayerOfTheSuperiorColliculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dentateGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsal3rdVentricle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalAcousticStria"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalCochlearNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalCochlearNucleusDeepCore"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalCochlearNucleusFusiformLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalCochlearNucleusGranularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalCochlearNucleusMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalCortexOfTheInferiorColliculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalCorticospinalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalEndopiriformNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalFornix"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalHippocampalCommissure"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalHypothalamicArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalIntermediateEntorhinalCortex"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalLateralGeniculateNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalLateralOlfactoryTract"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalMotorNucleusOfVagus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalNucleusOfTheLateralLemniscus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalNucleusOfTheSpinalCord"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalParagigantocellularNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalPartOfClaustrum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalPeduncularCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalPeduncularPontineNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalPeriolivaryRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalRapheNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalRapheNucleusCaudalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalRapheNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalRapheNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalRapheNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalSpinocerebellarTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalSpinocerebellarTractAndOlivocerebellarTract"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalSubiculum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalTegmentalDecussation"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalTegmentalNucleusCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalTegmentalNucleusPericentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalTeniaTecta"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalTeniaTectaLayer1"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalTerminalNucleusOfTheAccessoryOpticTract"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalTransitionZone"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsalTuberomammillaryNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsolateralEntorhinalCortex"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsolateralOrbitalCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsolateralPeriaqueductalGray"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsomedialHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsomedialHypothalamicNucleusCompactPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsomedialHypothalamicNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsomedialHypothalamicNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsomedialPeriaqueductalGray"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsomedialSpinalTrigeminalNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dorsomedialTegmentalArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_dysgranularInsularCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ectorhinalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ectotrigeminalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_entopeduncularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_entorhinalCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ependymaAndSubependymalLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ependymalAndSubendymalLayerOlfactoryVentricle"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_epifascicularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_epilemniscalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_epipeduncularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_epirubrospinalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_episupraopticNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ethmoidThalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_externalCapsule"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_externalCortexOfTheInferiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_externalCortexOfTheInferiorColliculusLayer1"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_externalCuneateNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_externalMedullaryLamina"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_externalPlexiformLayerOfTheAccessoryOlfactoryBulb"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_externalPlexiformLayerOfTheOlfactoryBulb"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_facialNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_facialNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_facialNucleusDorsalIntermediateSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_facialNucleusDorsolateralSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_facialNucleusDorsomedialSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_facialNucleusLateralSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_facialNucleusStylohyoidPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_facialNucleusVentralIntermediateSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_facialNucleusVentromedialSubnucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_fasciculusRetroflexus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_fasciolaCinereum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_fieldCA1OfTheHippocampus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_fieldCA2OfTheHippocampus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_fieldCA3OfTheHippocampus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_fimbriaOfTheHippocampus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_flocculus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_forcepsMajorOfTheCorpusCallosum"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_forcepsMinorOfTheCorpusCallosum"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_fornix"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_frontalAssociationCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_frontalCortexArea3"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_gelatinousLayerOfTheCaudalSpinalTrigeminalNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_geminiHypothalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_genuOfTheCorpusCallosum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_genuOfTheFacialNerve"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_gigantocellularReticularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_gigantocellularReticularNucleusAlphaPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_gigantocellularReticularNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_globusPallidus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_glomerularLayerOfTheAccessoryOlfactoryBulb"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_glomerularLayerOfTheOlfactoryBulb"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_glossopharyngealNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_gracileFasciculus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_gracileNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_granularCellLayerOfTheOlfactoryBulb"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_granularInsularCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_granularLayerOfTheDentateGyrus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_granuleCellLayerOfCochlearNuclei"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_granuleCellLayerOfTheAccessoryOlfactoryBulb"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_granuleCellLayerOfTheCerebellum"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_habenularCommissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_hilusOfTheDentateGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_hippocampalFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_hypoglossalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_hypoglossalNucleusGeniohyoidPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_indusiumGriseum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorCerebellarPeduncleDecussation"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorCerebellarPeduncleRestiformBody"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorColliculus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorOliveBetaSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorOliveCapOfKooyOfTheMedialNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorOliveDorsalNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorOliveDorsomedialCellGroup"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorOliveMedialNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorOlivePrincipalNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorOliveSubnucleusAOfMedialNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorOliveSubnucleusBOfMedialNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorOliveSubnucleusCOfMedialNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorOliveVentrolateralProtrusion"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_inferiorSalivatoryNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_infralimbicCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_infundibularRecess"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_infundibularStem"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interanterodorsalThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interanteromedialThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intercalatedAmygdaloidNucleusMainPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intercalatedNucleiOfTheAmygdala"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intercalatedNucleusOfTheMedulla"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intercruralFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interfascicularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intergeniculateLeaf"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermediateEndopiriformNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermediateGrayLayerOfTheSuperiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermediateInterstitialNucleusOfTheMedialLongitudinalFasciculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermediateLobeOfPituitary"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermediateNucleusOfTheLateralLemniscus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermediateReticularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermediateReticularNucleusAlphaPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermediateWhiteLayerOfTheSuperiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermediodorsalThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermediolateralCellColumnOfTheSpinalCord"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermedioventralThalamicCommissure"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intermediusNucleusOfTheMedulla"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_internalArcuateFibers"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_internalCapsule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_internalCarotidArtery"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_internalMedullaryLamina"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_internalPlexiformLayerOfTheOlfactoryBulb"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interpeduncularFossa"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interpeduncularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interpeduncularNucleusApicalSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interpeduncularNucleusCaudalSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interpeduncularNucleusDorsolateralSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interpeduncularNucleusDorsomedialSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interpeduncularNucleusIntermediateSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interpeduncularNucleusLateralSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interpeduncularNucleusRostralSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interposedCerebellarNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interposedCerebellarNucleusDorsolateralHump"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interposedCerebellarNucleusDorsomedialCrest"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interposedCerebellarNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interposedCerebellarNucleusPosteriorParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interstitialNucleusOfCajal"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interstitialNucleusOfCajalShellRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interstitialNucleusOfTheDecussationOfTheSuperiorCerebellarPeduncle"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interstitialNucleusOfTheMedulla"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interstitialNucleusOfThePosteriorLimbOfTheAnteriorCommissure"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interstitialNucleusOfThePosteriorLimbOfTheAnteriorCommissureLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interstitialNucleusOfThePosteriorLimbOfTheAnteriorCommissureMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interstitialNucleusOfTheVestibulocochlearNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_interventricularForamen"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_intramedullaryThalamicArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_islandsOfCalleja"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_islandsOfCallejaMajorIsland"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_isthmicPeriaqueductalGray"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_isthmicReticularFormation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_juxtaolivaryNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_juxtaparaventricularPartOfLateralHypothalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lacunosumMoleculareLayerOfTheHippocampus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lambdoidSeptalZone"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralAccumbensShell"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralAmygdaloidNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralAmygdaloidNucleusDorsolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralAmygdaloidNucleusVentrolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralAmygdaloidNucleusVentromedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralCerebellarNucleusParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralCervicalNucleusOfTheSpinalCord"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralDentateCerebellarNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralEntorhinalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralHabenularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralHabenularNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralHabenularNucleusMedialPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralHypothalamicArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralLemniscus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralMammillaryNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralOlfactoryTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralOrbitalCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralOrbitofrontalArtery"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParabrachialNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParabrachialNucleusCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParabrachialNucleusCrescentPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParabrachialNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParabrachialNucleusExternalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParabrachialNucleusInternalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParabrachialNucleusMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParabrachialNucleusSuperiorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParabrachialNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParagigantocellularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParagigantocellularNucleusAlphaPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParagigantocellularNucleusExternalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralParietalAssociationCortex"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralPeriaqueductalGray"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralPosteriorThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralPosteriorThalamicNucleusLaterocaudalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralPosteriorThalamicNucleusLaterorostralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralPosteriorThalamicNucleusMediocaudalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralPosteriorThalamicNucleusMediorostralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralPreopticArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralRecessOfThe4thVentricle"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralReticularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralReticularNucleusParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralReticularNucleusSubtrigeminalPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralSeptalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralSeptalNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralSeptalNucleusIntermediatePart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralSeptalNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralSpinalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralStripeOfTheStriatum"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralSuperiorOlive"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralTerminalNucleusOfTheAccessoryOpticTract"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralVentricle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateralVestibularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateroanteriorHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_laterodorsalTegmentalNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_laterodorsalTegmentalNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_laterodorsalThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_laterodorsalThalamicNucleusDorsomedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_laterodorsalThalamicNucleusVentrolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lateroventralPeriolivaryNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_layer1OfCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_layer1bOfCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_layer2OfCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_layer3OfCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_layer4OfCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_layer5OfCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_layer5aOfCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_layer5bOfCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_layer6OfCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_layer6aOfCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_layer6bOfCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_leminaTerminalis"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_linearNucleusOfTheMedulla"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_lithoidNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_locusCoeruleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_longitudinalFasciculusOfThePons"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_magnocellularNucleusOfTheLateralHypothalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_magnocellularNucleusOfThePosteriorCommissure"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_magnocellularPreopticNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mammillaryPeduncle"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mammillaryRecessOfThe3rdVentricle"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mammillotegmentalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mammillothalamicTract"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_marginalZoneOfTheMedialGeniculate"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_matrixRegionOfTheMedulla"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialAccessoryOculomotorNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialAmygdaloidNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialAmygdaloidNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialAmygdaloidNucleusAnterodorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialAmygdaloidNucleusAnteroventralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialAmygdaloidNucleusPosterodorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialAmygdaloidNucleusPosteroventralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialCerebellarNucleusCaudomedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialCerebellarNucleusDorsolateralProtuberance"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialCerebellarNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialCorticohypothalamicTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialEminenceExternalLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialEminenceInternalLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialEntorhinalCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialEntorhinalCortexVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialFastigialCerebellarNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialForebrainBundle"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialForebrainBundleAComponent"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialForebrainBundleBComponent"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialGeniculateNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialGeniculateNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialGeniculateNucleusMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialGeniculateNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialHabenularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialLemniscus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialLemniscusDecussation"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialLongitudinalFasciculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialMammillaryNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialMammillaryNucleusMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialMammillaryNucleusMedianPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialOrbitalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialOrbitofrontalArtery"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialParabrachialNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialParabrachialNucleusExternalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialParalemniscialNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialParietalAssociationCortex"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialPreopticArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialPreopticNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialPreopticNucleusCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialPreopticNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialPreopticNucleusMedialPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialPretectalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialSeptalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialSuperiorOlive"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialTerminalNucleusOfTheAccessoryOpticTract"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialTuberalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialVestibularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialVestibularNucleusMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medialVestibularNucleusParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medianAccessoryNucleusOfTheMedulla"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medianEminence"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medianPreopticNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medianRapheNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mediodorsalThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mediodorsalThalamicNucleusCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mediodorsalThalamicNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mediodorsalThalamicNucleusMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medioventralPeriolivaryNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medullaryReticularNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_medullaryReticularNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mesencephalicReticularFormation"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mesencephalicTrigeminalNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mesencephalicTrigeminalTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_microcellularTegmentalNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_middleCerebellarPeduncle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_middleCerebralArtery"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mitralCellLayerOfTheAccessoryOlfactoryBulb"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_mitralCellLayerOfTheOlfactoryBulb"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_molecularLayerOfTheCerebellum"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_molecularLayerOfTheDentateGyrus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_molecularLayerOfTheSubiculum"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_motorRootOfTheTrigeminalNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_motorTrigeminalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_motorTrigeminalNucleusAnteriorDigastricPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_motorTrigeminalNucleusMasseterPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_motorTrigeminalNucleusMylohyoidPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_motorTrigeminalNucleusTemporalisPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_motorTrigeminalNucleusTensorTympaniPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_navicularNucleusOfTheBasalForebrain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nervusIntermediusComponentOfTheFacialNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nigrostriatalBundle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfDarkschewitsch"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfOriginOfEfferentsOfTheVestibularNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfRoller"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheAnsaLenticularis"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheBrachiumOfTheInferiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheCentralAcousticTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheCommissuralStriaTerminalis"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheFieldsOfForel"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheHorizontalLimbOfTheDiagonalBand"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheLateralOlfactoryTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheLateralOlfactoryTractLayer1"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheOpticTract"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfThePosteriorCommissure"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheSolitaryTractCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheSolitaryTractCommissuralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheSolitaryTractDorsomedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheSolitaryTractGelatinousPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheSolitaryTractIntermediatePart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheSolitaryTractInterstitialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheSolitaryTractLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheSolitaryTractMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheSolitaryTractRostrolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheSolitaryTractVentrolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheStriaMedullaris"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheTrapezoidBody"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusOfTheVerticalLimbOfTheDiagonalBand"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusX"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusY"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_nucleusZ"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_obex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_oculomotorNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_oculomotorNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_oculomotorNucleusParvicellularPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_olfactoryBulb"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_olfactoryNerveLayer"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_olfactoryTubercle"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_olfactoryVentricleOlfactoryPartOfLateralVentricle"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_olivaryPretectalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_olivocerebellarTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_olivocochlearBundle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_opticChiasm"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_opticNerve"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_opticNerveLayerOfTheSuperiorColliculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_opticTract"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_oriensLayerOfTheHippocampus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ovalParacentralThalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_p1PeriaqueductalGray"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraabducensNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parabigeminalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parabrachialPigmentedNucleusOfTheVTA"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paracentralThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paracochlearGlialSubstance"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paracommissuralNucleusOfThePosteriorCommissure"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parafascicularThalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parafloccularSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraflocculus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parainterfascicularNucleusOfTheVTA"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paralambdoidSeptalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paralemniscalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paramedianLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paramedianRapheNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paramedianReticularNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paramedianSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paranigralNucleusOfTheVTA"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parapyramidalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pararubralNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parasolitaryNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parastrialNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parasubiculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parasubthalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paratenialThalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paratereteNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paratrigeminalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paratrochlearNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraventricularHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraventricularHypothalamicNucleusAnteriorParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraventricularHypothalamicNucleusDorsalCap"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraventricularHypothalamicNucleusLateralMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraventricularHypothalamicNucleusMedialMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraventricularHypothalamicNucleusMedialParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraventricularHypothalamicNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraventricularHypothalamicNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraventricularThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraventricularThalamicNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraventricularThalamicNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_paraxiphoidNucleusOfThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parietalCortexPosteriorAreaCaudalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parietalCortexPosteriorAreaDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parietalCortexPosteriorAreaRostralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parvicellularReticularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_parvicellularReticularNucleusAlphaPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_peduncularPartOfLateralHypothalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pedunculopontineTegmentalNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_periaqueductalGray"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_perifacialZone"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_perifornicalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_perifornicalPartOfLateralHypothalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_perilemniscalNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_periolivaryHorn"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_peripeduncularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_perirhinalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_peritrigeminalZone"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_periventricularGray"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_periventricularHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_periventricularHypothalamicNucleusAnteriorParvicellularPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pinealGland"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pinealStalk"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_piriformCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_piriformCortexLayer1"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pleomorphicPartOfPeriaqueductaiGray"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_polymorphLayerOfTheDentateGyrus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pontineNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pontineRapheNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pontineReticularNucleusCaudalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pontineReticularNucleusOralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pontineReticularNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorCerebralArtery"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorCommissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorHypothalamicArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorHypothalamicAreaDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorIntralaminarThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorLimitansThalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorLobeOfPituitary"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorPretectalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorSuperiorFissure"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorThalamicNuclearGroup"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteriorThalamicNuclearGroupTriangularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posterodorsalPreopticNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posterodorsalRapheNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posterodorsalTegmentalNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posterolateralCorticalAmygdaloidNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posterolateralCorticalAmygdaloidNucleusLayer1"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posterolateralFissure"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteromedialCorticalAmygdaloidNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_posteromedianThalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_postsubiculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_preBotzingerComplex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_preEdingerWestphalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_precommissuralNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_preculminateFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_precuneiformArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_prelimbicCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_premammillaryNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_premammillaryNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_preopticRecessOfThe3rdVentricle"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_prepositusNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_prepyramidalFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_prerubralField"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_presubiculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primaryAuditoryCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primaryFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primaryMotorCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primarySomatosensoryCortex"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primarySomatosensoryCortexBarrelField"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primarySomatosensoryCortexDysgranularZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primarySomatosensoryCortexForelimbRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primarySomatosensoryCortexHindlimbRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primarySomatosensoryCortexJawRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primarySomatosensoryCortexOralDysgranularZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primarySomatosensoryCortexShoulderRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primarySomatosensoryCortexTrunkRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primarySomatosensoryCortexUpperLipRegion"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primaryVisualCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primaryVisualCortexBinocularArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_primaryVisualCortexMonocularArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_principalMammillaryTract"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_principalSensoryTrigeminalNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_principalSensoryTrigeminalNucleusDorsomedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_principalSensoryTrigeminalNucleusVentrolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pyramidalCellLayerOfTheHippocampus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pyramidalDecussation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_pyramidalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_r1ReticularFormation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_r2ReticularFormation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_r3ReticularFormation"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_radiatumLayerOfTheHippocampus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rapheInterpositusNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rapheMagnusNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rapheObscurusNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_raphePallidusNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_recessOfTheInferiorColliculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_redNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_redNucleusMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_redNucleusParvicellularPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_regionWhereVAAndVLOverlap"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_reticluostrialNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_reticularThalamicNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_reticulotegmentalNucleusOfThePons"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_reticulotegmentalNucleusOfThePonsLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_reticulotegmentalNucleusOfThePonsPericentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retroambiguusNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retrochiasmaticArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retrochiasmaticAreaLateralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retroendopiriformNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retroethmoidNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retrolemniscalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retroparafascicularNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retrorubralField"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retrorubralNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retrosplenialDysgranularCortex"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retrosplenialGranularCortex"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retrosplenialGranularCortexARegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retrosplenialGranularCortexBRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retrosplenialGranularCortexCRegion"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_retrouniensArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_reuniensThalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rhabdoidNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rhinalFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rhinalIncisure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rhomboidThalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rootOfAbducensNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rootOfAccessoryNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rootOfHypoglossalNerve"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rostralAmygdalopiriformArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rostralInterstitialNucleusOfMedialLongitudinalFasciculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rostralLinearNucleusOfTheRaphe"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rostralVentralRespiratoryGroup"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rostroventrolateralReticularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rostrumOfTheCorpusCallosum"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_rubrospinalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_sagulumNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_scaphoidThalamicNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_secondaryAuditoryCortexDorsalArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_secondaryAuditoryCortexVentralArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_secondaryFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_secondaryMotorCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_secondarySomatosensoryCortex"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_secondaryVisualCortexLateralArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_secondaryVisualCortexMediolateralArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_secondaryVisualCortexMediomedialArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_sensoryRootOfTheTrigeminalNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_septofimbrialNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_septohippocampalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_septohypothalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_simpleLobule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_simpleLobuleA"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_simpleLobuleB"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_simplexFissure"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_solitaryNucleusDorsolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_solitaryNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_solitaryTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_sphenoidNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_spinalTrigeminalNucleusCaudalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_spinalTrigeminalNucleusInterpolarPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_spinalTrigeminalNucleusOralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_spinalTrigeminalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_spinalVestibularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_spleniumOfTheCorpusCallosum"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_stigmoidHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_stratumLucidumOfTheHippocampus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_striaMedullarisOfTheThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_striaTerminalis"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_strialPartOfThePreopticArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_striohypothalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subbrachialNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subcoeruleusNucleusAlphaPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subcoeruleusNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subcoeruleusNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subcommissuralOrgan"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subfornicalOrgan"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subgeniculateNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subiculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subiculumTransitionArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subincertalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_sublenticularExtendedAmygdala"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_sublenticularExtendedAmygdalaCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_sublenticularExtendedAmygdalaMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_submammillothalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_submediusThalamicNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_submediusThalamicNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_submediusThalamicNucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subparafascicularThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subparafascicularThalamicNucleusParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subparaventricularZoneOfTheHypothalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subpeduncularTegmentalNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subpostremaArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_substantiaInnominata"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_substantiaInnominataBasalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_substantiaNigraCompactPartDorsalTier"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_substantiaNigraCompactPartMedialTier"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_substantiaNigraCompactaPartVentralTier"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_substantiaNigraLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_substantiaNigraReticularPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_subthalamicNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_superficialGrayLayerOfTheSuperiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_superiorCerebellarPeduncleBrachiumConjunctivum"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_superiorCerebellarPeduncleDescendingLimb"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_superiorMedullaryVelum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_superiorParaolivaryNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_superiorSalivatoryNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_superiorThalamicRadiation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_superiorVestibularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_suprachiasmaticNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_suprachiasmaticNucleusDorsolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_suprachiasmaticNucleusVentromedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_suprageniculateThalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_supragenualNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_supramammillaryDecussation"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_supramammillaryNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_supramammillaryNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_supramammillaryNucleusMedialPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_supraoculomotorCap"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_supraoculomotorPeriaqueductalGray"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_supraopticDecussation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_supraopticNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_supraopticNucleusRetrochiasmaticPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_supratrigeminalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_tectospinalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_temporalAssociationCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_tereteHypothalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_transverseFibersOfThePons"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_trapezoidBody"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_triangularNucleusLateralLemniscus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_triangularSeptalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_trigeminalGanglion"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_trigeminalSolitaryTransitionZone"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_trigeminalTransitionZone"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_trigeminothalamicTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_trochlearNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_trochlearNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_trochlearNucluesShellRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_tuberalRegionOfLateralHypothalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_uncinateFasciculusDecussation"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_uncinateFasciculusOfTheCerebellum"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vagusNerve"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vascularOrganOfTheLaminaTerminalis"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vein"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralAnteriorThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralCochlearNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralCochlearNucleusCapsularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralCochlearNucleusGranuleCellLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralCochlearNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralCochlearNucleusPosteriorPartOctopusCellArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralEndopiriformNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralGeniculateNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralGeniculateNucleusLayer1"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralHippocampalCommissure"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralIntermediateEntorhinalCortex"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralLinearNucleusOfTheThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralNucleusOfTheLatLemniscus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralOrbitalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralPallidum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralPartOfClaustrum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralPosteriorNucleusOfTheThalamusParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralPosterolateralThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralPosteromedialThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralReuniensThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralSpinocerebellarTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralSpinocerebellarTractDecussation"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralSubiculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralTegmentalArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralTegmentalAreaRostralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralTegmentalDecussation"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralTegmentalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralTeniaTecta"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralTeniaTectaLayer1"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventralTuberomammillaryNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventrolateralHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventrolateralHypothalamicTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventrolateralPeriaqueductalGray"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventrolateralPreopticNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventrolateralThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventromedialHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventromedialHypothalamicNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventromedialHypothalamicNucleusCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventromedialHypothalamicNucleusDorsomedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventromedialHypothalamicNucleusVentrolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventromedialNucleusOfTheHypothalamusShell"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventromedialPreopticNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_ventromedialThalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vertebralArtery"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vestibularRootOfTheVestibulocochlearNerve"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vestibulocerebellarNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vestibulocochlearGanglion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vestibulocochlearNerve"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vestibulomesencephalicTract"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vestibulospinalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vomeronasalNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_vomeronasalNerveLayer"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_xiphoidThalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_zonaIncerta"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_zonaIncertaCaudalPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_zonaIncertaDorsalPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_zonaIncertaRostralPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_zonaIncertaVentralPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_zonaLimitans"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/PW-RBSC-cor_zonalLayerOfTheSuperiorColliculus"
            },
        ],
        "ontologyIdentifier": None,
    },
    has_versions=[
        {"@type": "https://openminds.ebrains.eu/instances/brainAtlasVersion/PW-RBSC-cor_6th-ed-Bregma-LIA"},
        {"@type": "https://openminds.ebrains.eu/instances/brainAtlasVersion/PW-RBSC-cor_6th-ed-Bregma-RIA"},
        {"@type": "https://openminds.ebrains.eu/instances/brainAtlasVersion/PW-RBSC-cor_6th-ed-Interaural-LSA"},
        {"@type": "https://openminds.ebrains.eu/instances/brainAtlasVersion/PW-RBSC-cor_6th-ed-Interaural-RSA"},
    ],
    short_name="Paxinos and Watson's Stereotaxic Rat Brain Atlas (Coronal)",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/rattusNorvegicus"},
)
BrainAtlas.schaefer_400p = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/Schaefer-400p",
    abbreviation="Schaefer-400p",
    full_name="Schaefer Atlas with 400 Parcellation",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": None,
        "ontologyIdentifier": None,
    },
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/Schaefer-400p_2018-FSL-MNI152-yeo7n"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/Schaefer-400p_2018-FSL-MNI152-yeo17n"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/Schaefer-400p_2018-FSL-MNI152-kong17n"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/Schaefer-400p_2018-fsLR32k-yeo7n"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/Schaefer-400p_2018-fsLR32k-yeo17n"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/Schaefer-400p_2018-fsLR32k-kong17n"},
    ],
    homepage=IRI(
        "https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal"
    ),
    short_name="Schaefer Atlas (400p)",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/homoSapiens"},
)
BrainAtlas.swanson_bm = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/SwansonBM",
    abbreviation="SwansonBM",
    description="Swanson's Brain Maps atlases are open access, stereotaxic rat brain atlases of an adult Sprague Dawley rat. These atlases contain spatially aligned maps for 3D reconstruction, hierarchical nomenclature and flatmaps.",
    full_name="Swanson's Brain Maps: Structure of the Rat Brain",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": [
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_AmmonsHornNoguez"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_BarringtonsNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_EdingerWestphalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_KollikerFuseSubnucleusOfPB"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_OnufsNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_abducensNerveEustachius"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_abducensNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_accessoryAbducensNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_accessoryFacialNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_accessoryOlfactoryBulbBalogh"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_accessoryOlfactoryBulbGlomerularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_accessoryOlfactoryBulbGranuleCellLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_accessoryOlfactoryBulbMitralLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_accessoryOlfactoryNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_accessoryOlfactoryTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_accessoryOpticTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_accessorySpinalNerveWillis"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_accessorySupraopticGroup"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_agranularInsularArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_agranularInsularAreaDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_agranularInsularAreaPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_agranularInsularAreaVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_alveusBurdach"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_amygdalaBurdach"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_amygdalarCapsule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_angularBundle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ansaPeduncularisGratiolet"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ansiformLobule"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ansiformLobuleCrus1SublobulesAd"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ansiformLobuleCrus2SublobulesAb"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ansoparamedianFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorAmygdalarArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorCingulateArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorCingulateAreaDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorCingulateAreaVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorCommissureOlfactoryLimb"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorCommissureRiolan"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorCommissureTemporalLimb"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorHypothalamicArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorHypothalamicNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorHypothalamicNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorHypothalamicNucleusCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorHypothalamicNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorHypothalamicNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorLaterolateralVisualArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorLevelHypothalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorLobeCerebellum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorNucleiDorsalThalamusNissl"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusDorsalPartMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusDorsalPartPyramidalLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusExternalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusExternalPartMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusExternalPartPyramidalLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusKolliker"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusLateralPartMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusLateralPartPyramidalLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusMedialPartMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusMedialPartPyramidalLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusPosteroventralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusPosteroventralPartMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorOlfactoryNucleusPosteroventralPartPyramidalLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorPretectalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteriorTegmentalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anterodorsalNucleusThalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anterodorsalPreopticNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anterolateralVisualArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteromedialNucleusThalamus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteromedialNucleusThalamusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteromedialNucleusThalamusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteromedialVisualArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteroventralNucleusThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteroventralPeriventricularNucleusHypothalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_anteroventralPreopticNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_arachnoid"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_arborVitae"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_arcuateHypothalamicNucleusClark"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_areaPostrema"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_auditoryAreas"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_autonomicGanglia"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_autonomicNervousSystemLangley"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_basalNucleusOfTheDorsalHorn"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_basalNucleusOfTheDorsalHornGeneral"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_basolateralAmygdalarNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_basolateralAmygdalarNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_basolateralAmygdalarNucleusPosteriorPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_basomedialAmygdalarNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_basomedialAmygdalarNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_basomedialAmygdalarNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisAnteriorDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisAnteriorDivisionAnterolateralArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisAnteriorDivisionAnteromedialArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisAnteriorDivisionDorsomedialNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisAnteriorDivisionFusiformNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisAnteriorDivisionJuxtacapsularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisAnteriorDivisionMagnocellularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisAnteriorDivisionOvalNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisAnteriorDivisionRhomboidNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisAnteriorDivisionSubcommissuralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisAnteriorDivisionVentralNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisJohnston"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisPosteriorDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisPosteriorDivisionCellsparseZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisPosteriorDivisionDorsalNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisPosteriorDivisionInterfascicularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisPosteriorDivisionPremedullaryNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisPosteriorDivisionPrincipalNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisPosteriorDivisionStrialExtension"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleiStriaTerminalisPosteriorDivisionTransverseNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleusAccessoryOlfactoryTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleusAnteriorCommissureGurdjian"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bedNucleusOfTheStriaMedullarisCajal"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_behaviorControlColumn"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_behavioralStateSystem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_brachialPlexus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_brachiumOfTheInferiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_brachiumOfTheSuperiorColliculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_brain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_brainstem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_bulbocerebellarTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_caudalIntracentralFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_caudoputamen"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_celiacGanglion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralAmygdalarNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralAmygdalarNucleusCapsularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralAmygdalarNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralAmygdalarNucleusMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralCanalSpinalCordmedulla"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralCervicalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralGray"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralGrayBrain"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralLateralNucleusThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralLinearNucleusRaphe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralLobule"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralLobuleLobuleIIISublobulesAb"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralLobuleLobuleIISublobulesAb"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralMedialNucleusThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralNervousSystem"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralNervousSystemGrayMatter"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralNervousSystemWhiteMatter"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_centralTegmentalBundleBechterew"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebellarCommissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebellarCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebellarCortexGranuleCellLayerInner"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebellarCortexGrooves"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebellarCortexMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebellarCortexPurkinjeLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebellarNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebellarPeduncles"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebellumHerophilusErasistratus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebellumRelatedFiberTracts"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebralAqueductCollicularRecess"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebralAqueductGeneral"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebralAqueductProperSylvius"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebralCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebralCortexCorticalPlate"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebralCortexGrooves"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebralCortexPolymodalAssociationCortex"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebralCortexSensorymotorCortex"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebralCortexSubplateRegion"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebralNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebralPeduncle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebrospinalFluid"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebrospinalTrunk"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cerebrumCerebralHemispheresEndbrainTelencephalon"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cervicalPlexus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cervicalSpinalGanglia18"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cervicothalamicTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_choroidFissure"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_choroidFissureFourthVentricle"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_choroidFissureLateralVentricle"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_choroidFissureThirdVentricle"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_choroidPlexus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_choroidPlexusFourthVentricle"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_choroidPlexusLateralVentricle"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_choroidPlexusThirdVentricle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_choroidalFissureEye"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ciliaryGanglion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ciliaryNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cingulateRegionBurdach"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cingulumBundleReil"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_claustrumBurdach"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_coccygealSpinalGanglia13"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_coccygealSympatheticGanglion"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cochlearNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cochlearNuclei"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cochlearNucleiGranularLamina"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cochlearNucleiSubpeduncularGranularRegion"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_columnsOfTheFornix"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_commissuralNucleusPeriaqueductalGrayPaxinosWatson"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_copulaPyramidisSublobulesAb"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corpusCallosumAnteriorForcepsArnold"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corpusCallosumBody"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corpusCallosumGalen"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corpusCallosumGenu"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corpusCallosumPosteriorForcepsArnold"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corpusCallosumRostrum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corpusCallosumSpleniumBurdach"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corticalAmygdalarNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corticalAmygdalarNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corticalAmygdalarNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corticalAmygdalarNucleusPosteriorPartLateralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corticalAmygdalarNucleusPosteriorPartMedialZone"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corticobulbarTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corticopontineTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corticorubralTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corticospinalTract"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corticospinalTractUncrossedBurdachTurck"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_corticotectalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cranialNerves"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cranialParasympatheticGanglia"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cranialPlexuses"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cranialSensoryGanglia"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_crus1Fissures13"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_crus2Fissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_culmen"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_culmenLobulesIVV"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cuneateFascicleBurdach"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cuneateNucleusBurdach"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cuneiformNucleusCastaldi"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_cuneocerebellarTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_declivalFissure2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_decliveVISublobulesAd"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_decussationOfTheTrochlearNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_deepCerebellarNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusCrest"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusCrestgranuleCellLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusCrestmolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusCrestpolymorphLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusLateralBlade"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusLateralBladegranuleCellLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusLateralBlademolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusLateralBladepolymorphLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusMedialBlade"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusMedialBladegranuleCellLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusMedialBlademolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusMedialBladepolymorphLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateGyrusTarin"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateNucleusMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateNucleusParvicellularPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dentateNucleusVicqDAzyr"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_diagonalBandBroca"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_diagonalBandNucleusBroca"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_diencephalon"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_distalGlossopharyngealGanglionAndersch"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_distalGlossopharyngeovagalPlacode"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_distalVagalGanglion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalAcousticStriaMonakow"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalAuditoryAreas"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalCochlearNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalColumnNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalColumns"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalCommissuralNucleusOfTheSpinalCord"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalCommissureSpinalCord"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalFornix"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalHippocampalCommissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalHornSpinalCord"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalLongitudinalFascicleSchutz"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalMedianSeptum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalMotorNucleusVagusNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalNucleusRaphe"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalNucleusSpinalCordCaudalPartStilling"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalNucleusSpinalCordGeneral"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalNucleusSpinalCordStillingClarke"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalPremammillaryNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalPropriohypothalamicPathways"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalRootsCoiter"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalSpinocerebellarTractFlechsig"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalTegmentalDecussationMeynert"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalTegmentalNucleusGudden"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalTegmentalTractLindvallBjorklund"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalTerminalNucleusAccessoryOpticTract"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalThalamus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalThalamusPolymodalAssociationCortexRelate"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsalThalamusSensorymotorCortexRelated"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsolateralFascicleLissauer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsomedialHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsomedialHypothalamicNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsomedialHypothalamicNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dorsomedialHypothalamicNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_dura"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ectorhinalArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_efferentCochlearGroup"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_efferentCochleovestibularBundle"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_efferentVestibularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_endopiriformNucleusDorsalPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_endopiriformNucleusLoo"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_endopiriformNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_endorhinalGroove"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_entericNervousSystemLangley"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_entorhinalArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_entorhinalAreaLateralPartLayers16"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_entorhinalAreaMedialPartDorsalZoneLayers16"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_entorhinalAreaMedialPartVentralZoneHaug"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_epithalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_externalCapsuleBurdach"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_externalCuneateNucleusMonakowBlumenau"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_externalMedullaryLaminaThalamusBurdach"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_extrapyramidalFiberSystems"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_extrapyramidalFiberSystemsCerebralNucleiRelated"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_extremeCapsule"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_facialNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_facialNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fasciculusProprius"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fasciculusRetroflexusMeynert"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fasciolaCinereaReilArnold"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fastigialNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA1AmmonsHornLorenteDeNo"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA1PyramidalLayer"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA1PyramidalLayerDeep"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA1PyramidalLayerSuperficial"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA1StratumLacunosummoleculareMeynert"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA1StratumOriensSala"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA1StratumRadiatumMeynert"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA2AmmonsHornLorenteDeNo"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA2PyramidalLayer"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA2StratumLacunosummoleculare"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA2StratumOriens"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA2StratumRadiatum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA3AmmonsHornLorenteDeNo"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA3PyramidalLayer"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA3StratumLacunosummoleculare"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA3StratumLucidumHonegger"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA3StratumOriens"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldCA3StratumRadiatum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fieldsOfForel"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_filumTerminale"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fimbriaVieussens"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_flocculonodularLobeCerebellum"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_flocculus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_foliumtuberVermisVII"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_forebrain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fornixSystemGalen"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fourthVentricleGeneral"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fourthVentricleLateralRecess"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_fourthVentricleProper"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_frontalPoleCerebralCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_frontalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ganglia"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_geniculateGanglion"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_geniculateGroupOfTheDorsalThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_geniculateGroupOfTheVentralThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_genuOfTheFacialNerve"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_gigantocellularReticularNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_globusPallidusBurdach"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_globusPallidusExternalSegment"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_globusPallidusInternalSegment"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_glossopharyngealNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_gracileFascicleGoll"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_gracileNucleusGeneralGoll"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_gracileNucleusMedianPartBischoff"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_gracileNucleusPrincipalPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_grooves"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_gustatoryArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_habenularCommissureHaller"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hemisphericRegionCerebellum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hindbrain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hippocampalCommissuresDavid"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hippocampalFissureGratiolet"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hippocampalFormation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hippocampalRegionAranzi"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hypoglossalNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hypoglossalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hypothalamicLateralZone"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hypothalamicLateralZoneMotorRelated"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hypothalamicLateralZoneStateRelated"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hypothalamicPeriventricularRegion"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hypothalamohypophysialTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_hypothalamusHis"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_induseumGriseumValentin"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorCerebellarPeduncleRidley"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorColliculus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorColliculusCentralNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorColliculusCommissure"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorColliculusDorsalNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorColliculusExternalNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorMesentericGanglia"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorOlivaryComplexDorsalAccessoryOlive"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorOlivaryComplexMedialAccessoryOlive"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorOlivaryComplexPrincipalOlive"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorOlivaryComplexVieussens"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_inferiorSalivatoryNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_infracerebellarNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_infralimbicArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_infundibulumExternalLamina"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_infundibulumGalen"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_infundibulumInternalLamina"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_insularRegion"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interanterodorsalNucleusThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interanteromedialNucleusThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interbrain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intercalatedAmygdalarNuclei"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intercalatedNucleusOfTheSpinalCord"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intercruralFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interfascicularNucleusRaphe"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intermediateAcousticStriaHeld"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intermediateGraySpinalCordGeneral"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intermediateGraySpinalCordProper"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intermediateNerveWrisberg"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intermediodorsalNucleusThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intermediolateralSpinalColumn"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intermediolateralSpinalColumnSacralDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intermediolateralSpinalColumnThoracolumbarDivision"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intermediolateralVisualArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intermediomedialSpinalColumn"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_internalArcuateFibers"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_internalCapsuleBurdach"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_internalMedullaryLaminaThalamusBurdach"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_internuclearAreaHypothalamicPeriventricularRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interpeduncularNucleusApicalSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interpeduncularNucleusCentralSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interpeduncularNucleusDorsomedialSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interpeduncularNucleusGudden"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interpeduncularNucleusIntermediateSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interpeduncularNucleusLateralSubnucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interpeduncularNucleusLateralSubnucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interpeduncularNucleusLateralSubnucleusIntermediatePart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interpeduncularNucleusLateralSubnucleusRostralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interpeduncularNucleusLateralSubnucleusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interpeduncularNucleusRostralSubnucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interposedNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interposedNucleusMainPart"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interposedNucleusParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interstitialNucleusAuditoryNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interstitialNucleusOfCajal"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interstitialNucleusVestibularNerve"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_interventricularForamenMonro"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intracentralFissure2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intraculminateFissure1"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intralaminarNucleiDorsalThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_intraparafloccularFissure"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_islandsOfCallejaOlfactoryTubercle"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_isocortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_isocortexDeepSupragranularPyramidalLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_isocortexGranularLayer"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_isocortexInfragranularPyramidalLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_isocortexMolecularLayer"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_isocortexPolymorphLayer"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_isocortexSuperficialSupragranularPyramidalLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_juxtarestiformBody"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralAmygdalarNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralApertureFourthVentricleLuschka"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralCervicalNucleusRexedBrodal"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralDorsalNucleusThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralForebrainBundle"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralForebrainBundleSystem"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralForebrainBundleSystemThalamusRelated"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralFuniculus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralGeniculateComplexDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralGeniculateComplexIntergeniculateLeaflet"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralGeniculateComplexSantorini"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralGeniculateComplexVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralGeniculateComplexVentralPartLateralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralGeniculateComplexVentralPartMedialZone"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHabenulaNissl"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaAnteriorRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaAnteriorRegionDorsalZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaAnteriorRegionIntermediateZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaAnteriorRegionVentralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaDorsalRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaJuxtadorsomedialRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaJuxtaparaventricularRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaJuxtaventromedialRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaJuxtaventromedialRegionDorsalZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaJuxtaventromedialRegionVentralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaMagnocellularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaMotorRelated"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaNissl"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaParvicellularRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaPosteriorRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaSubfornicalRegionAnteriorZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaSubfornicalRegionPosteriorZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaSubfornicalRegionPremammillaryZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaSuprafornicalRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaVentralRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaVentralRegionLateralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralHypothalamicAreaVentralRegionMedialZone"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralLemniscusReil"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralMammillaryNucleusGudden"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralNucleiDorsalThalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralOlfactoryTractBody"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralOlfactoryTractDorsalLimb"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralOlfactoryTractGeneral"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralPosteriorNucleusThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralPreopticArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralPropriohypothalamicPathways"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralReticularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralReticularNucleusMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralReticularNucleusParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalComplexRisoldSwanson"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCajal"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalCaudodorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartDorsalZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartDorsalZoneDorsalRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartDorsalZoneLateralRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartDorsalZoneRostralRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartDorsalZoneVentralRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartVentralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartVentralZoneIntermediateRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartVentralZoneLateralRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartVentralZoneLateralRegionDorsalDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartVentralZoneLateralRegionVentralDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartVentralZoneMedialRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartVentralZoneMedialRegionDorsalDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusCaudalPartVentralZoneMedialRegionVentralDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartDorsolateralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartDorsolateralZoneLateralRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartDorsolateralZoneLateralRegionDorsalDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartDorsolateralZoneLateralRegionVentralDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartDorsolateralZoneMedialRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartDorsolateralZoneMedialRegionDorsalDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartDorsolateralZoneMedialRegionVentralDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartMedialZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartMedialZoneDorsalRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartMedialZoneVentralRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartMedialZoneVentralRegionCaudalDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartMedialZoneVentralRegionRostralDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartVentrolateralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartVentrolateralZoneDorsalRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartVentrolateralZoneDorsalRegionLateralDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartVentrolateralZoneDorsalRegionMedialDomain"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralPartVentrolateralZoneVentralRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusRostralRostroventralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSeptalNucleusVentralPartRisoldSwanson"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSpinalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralSpinothalamicTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralTegmentalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralTerminalNucleusAccessoryOpticTract"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralVentricle"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lateralVestibularNucleusDeiters"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_laterodorsalTegmentalNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_laterolateralVisualArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_linearNucleusMedulla"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lingulaI"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_locusCeruleusVicqDAzyr"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_longitudinalAssociationBundle"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lumbarSpinalGanglia16"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lumbarSympatheticGanglia16"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_lumbosacralPlexus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_magnocellularNucleusLoo"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_magnocellularReticularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mainOlfactoryBulbGlomerularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mainOlfactoryBulbGranuleCellLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mainOlfactoryBulbInnerPlexiformLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mainOlfactoryBulbMitralLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mainOlfactoryBulbOuterPlexiformLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mainOlfactoryBulbSoemmerring"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_majorIslandOfCallejaOlfactoryTubercle"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mammillaryBodyGallSpurzheim"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mammillaryPeduncleMeynert"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mammillotegmentalTractGudden"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mammillothalamicTractVicqDAzyr"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_marginalZoneSpinalCordWaldeyer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialAccessoryOculomotorNucleusBechterew"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialAmygdalarNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialAmygdalarNucleusAnterodorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialAmygdalarNucleusAnteroventralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialAmygdalarNucleusPosterodorsalPartSublayersAc"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialAmygdalarNucleusPosteroventralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialCorticohypothalamicTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialForebrainBundleEdinger"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialForebrainBundleSystem"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialForebrainBundleSystemCerebrumRelated"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialForebrainBundleSystemEpithalamusRelated"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialForebrainBundleSystemHypothalamusRelated"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialForebrainBundleSystemMammillaryRelated"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialForebrainBundleSystemMidbrainRelated"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialForebrainBundleSystemThalamusRelated"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialGeniculateComplex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialGeniculateComplexDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialGeniculateComplexMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialGeniculateComplexVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialHabenulaDorsalPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialHabenulaNissl"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialHabenulaVentralPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialLemniscusReil"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialLongitudinalFascicle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialMammillaryNucleusBody"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialMammillaryNucleusGeneralGudden"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialMammillaryNucleusMedianPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialNucleiDorsalThalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialPreopticArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialPreopticNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialPreopticNucleusCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialPreopticNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialPreopticNucleusMedialPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialPretectalArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialPropriohypothalamicPathways"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialSeptalComplex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialSeptalNucleusCajal"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialTerminalNucleusAccessoryOpticTractEdinger"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medialVestibularNucleusSchwalbe"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medianApertureFourthVentricleMagendie"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medianEminence"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medianEminenceExternalLamina"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medianEminenceInternalLamina"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medianPreopticNucleusLoo"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mediodorsalNucleusThalamus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mediodorsalNucleusThalamusCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mediodorsalNucleusThalamusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mediodorsalNucleusThalamusMedialPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_mediolateralVisualArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medulla"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medullaryReticularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medullaryReticularNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_medullaryReticularNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_meninges"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_midbrain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_midbrainReticularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_midbrainReticularNucleusMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_midbrainReticularNucleusMagnocellularPartGeneral"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_midbrainReticularNucleusParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_midbrainReticularNucleusRetrorubralArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_midbrainTractOfTheTrigeminalNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_midbrainTrigeminalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_middleCerebellarPeduncle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_middleCervicalGanglion"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_middleCommissureOfTheThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_midlineGroupDorsalThalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_midlineNucleiDorsalThalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_motoneuronGroups"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_motorNucleusOfTheTrigeminalMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_motorNucleusOfTheTrigeminalNerve"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_motorNucleusOfTheTrigeminalNerveParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_motorRootOfTheTrigeminalNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_motorSystem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_myentericPlexusAuerbach"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nerveFibers"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nervePlexuses"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nerves"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nervousSystem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_neuroendocrineMotorZone"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_neuroendocrineMotorZoneMagnocellular"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_neuroendocrineMotorZoneParvicellular"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nigrostriatalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nigrothalamicFibers"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nodularFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nodulusXSublobulesAb"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusAccumbens"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusAmbiguusDorsalDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusAmbiguusVentralDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusBrachiumInferiorColliculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusCircularis"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusIncertusCompactPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusIncertusDiffusePart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusIncertusStreeter"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusIntercalatusStaderini"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfDarkschewitsch"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfRoller"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheBulbocavernosus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheLateralLemniscusBechterew"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheLateralLemniscusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheLateralLemniscusHorizontalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheLateralLemniscusVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheLateralOlfactoryTractDorsalCap"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheLateralOlfactoryTractGanser"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheLateralOlfactoryTractMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheLateralOlfactoryTractPyramidalLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheOpticTract"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfThePosteriorCommissure"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheSolitaryTract"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheSolitaryTractCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheSolitaryTractCommissuralPartCajal"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheSolitaryTractGelatinousPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheSolitaryTractLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheSolitaryTractMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheSpinalAccessoryNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusOfTheTrapezoidBody"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusPrepositusMarburg"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusPropriusOfTheSpinalCord"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusRapheMagnus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusRapheObscurus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusRaphePallidus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusRaphePontis"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusReuniensCaudalDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusReuniensCaudalDivisionDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusReuniensCaudalDivisionMedianPartGurdjian"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusReuniensCaudalDivisionPosteriorPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusReuniensMalone"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusReuniensRostralDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusReuniensRostralDivisionAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusReuniensRostralDivisionDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusReuniensRostralDivisionLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusReuniensRostralDivisionMedianPartGurdjian"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusReuniensRostralDivisionVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusSagulum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusXBrodalPompeiano"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusYBrodalPompeiano"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_nucleusZBrodalPompeiano"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_occipitalPoleCerebralCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_occipitalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_oculomotorNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_oculomotorNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_olfactoryCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_olfactoryNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_olfactoryTubercleGanser"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_olfactoryTubercleMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_olfactoryTuberclePolymorphLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_olfactoryTuberclePyramidalLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_olivaryPretectalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_olivocerebellarTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_opticChiasm"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_opticNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_opticTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_orbitalArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_orbitalAreaLateralPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_orbitalAreaMedialPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_orbitalAreaVentralPart"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_orbitalAreaVentrolateralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_oticGanglionArnold"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pallidotegmentalFascicle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pallidothalamicPathway"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pallidum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabigeminalNucleusBechterew"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusCentralLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusDorsalLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusExternalLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusExternalMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusExtremeLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusInternalLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusLateralDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusMedialDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusMedialMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusSuperiorLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusVentralLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parabrachialNucleusVentralMedialPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paracentralNucleusThalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parafascicularNucleusVogt"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parafloccularSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraflocculus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paragigantocellularReticularNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paragigantocellularReticularNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paragigantocellularReticularNucleusLateralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paramedianLobule"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paramedianReticularNucleusMislawsky"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paramedianSulcus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parapyramidalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parapyramidalNucleusDeepPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parapyramidalNucleusSuperficialPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parasolitaryNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parastrialNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parasubiculumLayers16"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parasubthalamicNucleusZhangWang"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parasympatheticGanglia"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parasympatheticPlexuses"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parasympatheticSystem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paratenialNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paratrigeminalNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusAnteriorMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusAnteriorParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusDescendingDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusDorsalParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusFornicealPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusLateralParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusMagnocellularDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusMalone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusMedialMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusMedialParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusMedialParvicellularPartDorsalZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusMedialParvicellularPartVentralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusNeuroendocrineComponent"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusParvicellularDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusPeriventricularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusPosteriorMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusPosteriorMagnocellularPartLateralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularHypothalamicNucleusPosteriorMagnocellularPartMedialZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paraventricularThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_paravertebralSympatheticGanglia"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parietalRegion"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parietalRegionPosteriorAssociationAreas"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_parvicellularReticularNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pedunculopontineNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pelvicGanglion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_perforantPath"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periaqueductalGray"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periaqueductalGrayDorsalDivisionBeitz"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periaqueductalGrayDorsolateralDivisionBeitz"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periaqueductalGrayMedialDivisionBeitz"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periaqueductalGrayRostrolateralDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periaqueductalGrayRostromedialDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periaqueductalGrayVentrolateralDivisionBeitz"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_perihypoglossalNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periolivaryRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_peripeduncularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_peripheralNervousSystem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_perireuniensNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_perirhinalArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periventricularBundleHypothalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periventricularBundleThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periventricularHypothalamicNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periventricularHypothalamicNucleusIntermediatePart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periventricularHypothalamicNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_periventricularRegionHypothalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_phrenicNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_phrenicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pia"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pinealGlandGalen"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pinealStalk"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_piriformArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_piriformAreaMolecularLayer"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_piriformAreaPolymorphLayer"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_piriformAreaPyramidalLayer"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_piriformamygdalarArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pituitaryGlandAnteriorLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pituitaryGlandGalen"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pituitaryGlandIntermediateLobe"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pituitaryGlandNeuralLobe"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ponsVarolio"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pontineCentralGray"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pontineCentralGrayGeneral"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pontineGray"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pontineGrayGeneral"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pontineReticularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pontineReticularNucleusCaudalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pontineReticularNucleusRostralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_postAndPrecerebellarNuclei"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_postcommissuralFornixElliotSmith"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posteriorAmygdalarNucleusCanterasSwanson"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posteriorAuditoryArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posteriorCommissureLieutaud"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posteriorComplexThalamus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posteriorHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posteriorLimitingNucleusThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posteriorLobeCerebellum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posteriorPretectalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posteriorSeptalComplex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posteriorSuperiorFissure"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posterodorsalIntraculminateFissure"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posterodorsalPreopticNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posterolateralFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posterolateralVisualArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_posteromedialVisualArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_postpiriformTransitionArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_postsubiculumLayers16"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_precentralFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_precentralFissureA"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_precentralFissureB"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_precommissuralFornixElliotSmith"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_precommissuralFornixGeneral"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_precommissuralNucleusPeriaqueductalGrayPaxinosWatson"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_preculminateFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_prefrontalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_preganglionicAutonomicPools"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_preganglionicAutonomicPoolsParasympathetic"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_preganglionicAutonomicPoolsSympathetic"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_prelimbicArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_premammillaryCommissureRisoldEtAl"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_preopticCommissureRisoldEtAl"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_preopticLevelHypothalamusEdinger"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_preopticPeriventricularNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_preparasubthalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_prepyramidalFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_presubiculumLayers16Cajal"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pretectalRegionEdinger"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_prevertebralSympatheticGanglia"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_primaryAuditoryArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_primaryFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_primarySomatomotorArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_primarySomatosensoryArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_primarySomatosensoryAreaBarrelField"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_primarySomatosensoryAreaLowerLimbRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_primarySomatosensoryAreaMouthRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_primarySomatosensoryAreaNoseRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_primarySomatosensoryAreaTrunkRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_primarySomatosensoryAreaUpperLimbRegion"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_primaryVisualArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_principalMammillaryTractKolliker"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_principalSensoryNucleusOfTheTrigeminal"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_propriohypothalamicPathways"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_proximalGlossopharyngealGanglion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_proximalGlossopharyngeovagalPlacode"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_proximalVagalGanglionEhrenritter"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pterygopalatineGanglionMeckel"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pudentalPlexus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pyramidWillis"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pyramidalDecussationPourfourDuPetit"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pyramidalFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_pyramusVIIISublobulesAb"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rapheNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_redNucleusBurdach"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_reticularFormationJLenhossek"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_reticularNucleusSpinalCord"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_reticularNucleusThalamusArnold"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_reticulocerebellarTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_reticulospinalTract"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_reticulospinalTractLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_reticulospinalTractMedialPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retina"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retinaGanglionCellLayer"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retinaInnerNuclearLayer"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retinaInnerPlexiformLayer"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retinaOuterNuclearLayer"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retinaOuterPlexiformLayer"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retrochiasmaticAreaLateralHypothalamicArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retrohippocampalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retrosplenialArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retrosplenialAreaDorsalPart"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retrosplenialAreaLateralAgranularPartRisoldSwanson"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retrosplenialAreaVentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retrosplenialAreaVentralPartZoneA"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_retrosplenialAreaVentralPartZoneBc"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rhinalFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rhinalIncisure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rhinalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rhinocele"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rhomboidNucleusCajal"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rostralLinearNucleusRaphe"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rostralMedullaryVelumVieussens"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rostralNeuropore"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rostrolateralVisualArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rubroreticularTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_rubrospinalTractMonakow"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sacralParasympatheticGanglia"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sacralSpinalGanglia14"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sacralSympatheticGanglia14"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_secondaryFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_secondarySomatomotorAreas"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sensoryGanglia"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sensoryRootOfTheTrigeminalNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sensorySystem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sensorySystemAuditory"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sensorySystemGustatory"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sensorySystemHumorosensory"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sensorySystemSomatosensory"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sensorySystemVisceral"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sensorySystemVisual"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_septalRegionMeynert"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_septofimbrialNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_septohippocampalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_simpleFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_simpleLobuleSublobulesAb"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_solitaryTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_somaticNervousSystem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_somatomotorAreas"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_somatomotorMotoneuronPools"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_somatosensoryAreas"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalCentralGray"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalCord"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalCordCervicalLevelSegments18"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalCordCoccygealLevelSegments13"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalCordGrooves"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalCordLumbarLevelSegments16"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalCordSacralLevelSegments14"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalCordThoracicLevelSegments113"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalNerves"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalNucleusOfTheTrigeminal"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalNucleusOfTheTrigeminalCaudalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalNucleusOfTheTrigeminalInterpolarPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalNucleusOfTheTrigeminalOralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalNucleusOfTheTrigeminalOralPartCaudalDorsomedialRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalNucleusOfTheTrigeminalOralPartMiddleDorsomedialRegionDorsalZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalNucleusOfTheTrigeminalOralPartMiddleDorsomedialRegionVentralZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalNucleusOfTheTrigeminalOralPartRostralDorsomedialRegion"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalNucleusOfTheTrigeminalOralPartVentrolateralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalPlexuses"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalSensoryGanglia"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalTractOfTheTrigeminalNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinalVestibularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinocerebellarTracts"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinocervicalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinohypothalamicPathway"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinoolivaryPathway"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinoreticularPathway"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinotectalPathway"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinotelencephalicPathway"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinothalamicTractThieleHorsley"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spinovestibularPathway"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_spiralGanglionCorti"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_splanchnicNerves"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_stellateGanglion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_stratumZonaleThalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_striaMedullaris"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_striaTerminalisWenzelWenzel"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_striatalFundus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_striatonigralPathway"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_striatum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subceruleusNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subcommissuralOrgan"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subependymalZone"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subfornicalOrganPines"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subiculumBurdach"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subiculumDorsalPart"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subiculumDorsalPartMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subiculumDorsalPartPyramidalLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subiculumDorsalPartStratumRadiatum"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subiculumVentralPart"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subiculumVentralPartMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subiculumVentralPartPyramidalLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subiculumVentralPartStratumRadiatum"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sublaterodorsalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_submandibularGanglion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_submedialNucleusThalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_submucosalPlexusMeissner"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subparafascicularNucleusThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subparafascicularNucleusThalamusMagnocellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subparafascicularNucleusThalamusParvicellularPartLateralDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subparafascicularNucleusThalamusParvicellularPartMedialDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subparaventricularZoneHypothalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_substantiaGelatinosaSpinalCordRolando"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_substantiaInnominataReilReichert"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_substantiaNigraCompactPart"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_substantiaNigraReticularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_substantiaNigraSoemmerringVicqDAzyr"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subthalamicFascicle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_subthalamicNucleusLuys"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorCentralNucleusRapheBechterew"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorCentralNucleusRapheLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorCentralNucleusRapheMedialPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorCerebellarPeduncle"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorCerebellarPeduncleWernekinck"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorCervicalGanglion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusCommissure"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusDeepGrayLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusDeepWhiteLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusIntermediateGrayLayerSublayerA"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusIntermediateGrayLayerSublayerB"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusIntermediateGrayLayerSublayerC"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusIntermediateWhiteLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusMotorRelated"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusOpticLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusSensoryRelated"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusSuperficialGrayLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorColliculusZonalLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorMesentericGanglion"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorOlivaryComplexLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorOlivaryComplexMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorOlivaryComplexSchroederVanDerKolk"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorSalivatoryNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_superiorVestibularNucleusBechterew"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supplementalSomatosensoryArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_suprachiasmaticNucleusDorsomedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_suprachiasmaticNucleusSpiegelZwieg"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_suprachiasmaticNucleusVentrolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_suprachiasmaticPreopticNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_suprageniculateNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supragenualNucleusMeessenOlszewski"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supramammillaryDecussation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supramammillaryNucleusCajal"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supramammillaryNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supramammillaryNucleusMedialPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supraopticCommissures"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supraopticCommissuresAnteriorGanser"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supraopticCommissuresDorsalMeynert"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supraopticCommissuresVentralGudden"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supraopticNucleusGeneralLenhossek"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supraopticNucleusProper"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supraopticNucleusRetrochiasmaticPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_supratrigeminalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sympatheticChain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sympatheticGanglia"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sympatheticPlexuses"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_sympatheticSystem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tectospinalPathway"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tectospinalPathwayCrossedEdinger"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tectospinalPathwayDirect"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tectothalamicPathway"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tectum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tegmentalReticularNucleusPontineGrayBechterew"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tegmentum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_telencephalicRoofPlate"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_telencephalon"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_temporalAssociationAreas"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_temporalPoleCerebralCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_temporalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_teniaTecta"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_teniaTectaDorsalPartLayers14"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_teniaTectaVentralPartLayers13"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_terminalGanglion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_terminalNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thalamicPeduncles"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thirdVentricle"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thirdVentricleHypothalamicPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thirdVentricleInfundibularRecess"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thirdVentricleMammillaryRecess"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thirdVentriclePeriventricularRecess"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thirdVentriclePinealRecess"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thirdVentriclePreopticRecessEdinger"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thirdVentricleThalamicPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thoracicSpinalGanglia113"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_thoracicSympatheticGanglia313"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_trapezoidBodyTreviranus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_triangularNucleusSeptumCajal"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_trigeminalGanglionVieussensGasser"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_trigeminalNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_trigeminocerebellarTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_trochlearNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_trochlearNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tuberalNucleusIntermediatePart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tuberalNucleusLateralPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tuberalNucleusMalone"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tuberalNucleusSubventricularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tuberalNucleusTereteSubnucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tuberomammillaryNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tuberomammillaryNucleusDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_tuberomammillaryNucleusVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_uncinateFascicleRussell"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_uvulaIXSublobulesAbc"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_uvularFissure1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_vagalCommissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_vagusNerve"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_vascularOrganOfTheLaminaTerminalis"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralAnteriorlateralComplexThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralAuditoryAreas"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralCochlearNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralCochlearNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralCochlearNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralCommissureOfTheSpinalCord"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralCommissureSpinalCord"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralFuniculus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralHippocampalCommissure"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralHornSpinalCord"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralHornSpinalCordGeneral"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralMedialNucleusThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralMedianFissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralNucleiDorsalThalamus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralPosteriorComplexThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralPosterolateralNucleusThalamusGeneral"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralPosterolateralNucleusThalamusParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralPosterolateralNucleusThalamusPrincipalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralPosteromedialNucleusThalamusGeneral"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralPosteromedialNucleusThalamusParvicellularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralPosteromedialNucleusThalamusPrincipalPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralPremammillaryNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralPropriohypothalamicPathways"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralRootsCoiter"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralSpinocerebellarTractGowers"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralSpinothalamicTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralTegmentalAreaTsai"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralTegmentalDecussationForel"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralTegmentalNucleusGudden"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventralThalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventricularSystem"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventrolateralHypothalamicTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventrolateralPreopticNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventromedialHypothalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventromedialNucleusHypothalamusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventromedialNucleusHypothalamusCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventromedialNucleusHypothalamusDorsomedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_ventromedialNucleusHypothalamusVentrolateralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_vermalRegionsCerebellum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_vestibularGanglionScarpa"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_vestibularNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_vestibularNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_vestibulocochlearNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_vestibulomotorRegions"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_vestibulospinalPathway"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_visceralArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_visceralSensorymotorAreas"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_visualAreas"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_vomeronasalNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_zonaIncerta"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_zonaIncertaDopaminergicGroup"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_zonaIncertaGeneral"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SwansonBM_zonaLimitans"},
        ],
        "ontologyIdentifier": None,
    },
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/SwansonBM_3rd-ed"}],
    homepage=IRI("https://larrywswanson.com/"),
    short_name="Swanson's Brain Maps",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/rattusNorvegicus"},
)
BrainAtlas.swma = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/SWMA",
    abbreviation="SWMA",
    full_name="Atlas of Superficial White Matter Fibre Bundles",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": [
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_CAC-PoCi_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_CAC-PrCu_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_CMF-Op_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_CMF-PoC_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_CMF-PrC_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_CMF-PrC_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_CMF-RMF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_CMF-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_CMF-SF_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_Cu-Li_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_Fu-LO_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_Fu-LO_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_IC-PrCu_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_IP-IT_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_IP-LO_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_IP-LO_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_IP-MT_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_IP-SM_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_IP-SP_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_IP-SP_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_IT-MT_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_IT-MT_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_IT-MT_2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_LO-SP_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_LOF-MOF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_LOF-Or_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_LOF-RMF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_LOF-RMF_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_LOF-ST_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_MOF-ST_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_MT-SM_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_MT-ST_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_Op-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_Op-PrC_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_Op-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_Op-Tr_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_Or-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoC-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoC-PrC_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoC-PrC_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoC-PrC_2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoC-PrC_3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoC-SM_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoC-SM_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoC-SP_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoC-SP_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoCi-PrCu_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoCi-PrCu_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoCi-PrCu_2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoCi-RAC_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PoCi-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PrC-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PrC-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PrC-SM_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_PrC-SP_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_RAC-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_RAC-SF_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_RMF-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_RMF-SF_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_SM-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_SP-SM_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_ST-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_ST-TT_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_Tr-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_Tr-SF_0"},
        ],
        "ontologyIdentifier": None,
    },
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/SWMA_2018"}],
    short_name="Superficial White Matter Atlas",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/homoSapiens"},
)
BrainAtlas.whss_datlas = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/WHSSDatlas",
    abbreviation="WHSSDatlas",
    description="The Waxholm Space Atlas of the Sprague Dawley Rat Brain is an open access volumetric atlas. The delineations are defined in isotropic magnetic resonance (39 micrometre) and diffusion tensor (78 micrometre) images acquired ex vivo from an 80 day old male rat at the Duke Center for In Vivo Microscopy. Coordinates for navigating the volume are provided by the Waxholm Space coordinate system. The location of bregma and lambda are also identified as anchors towards stereotaxic space. The atlas (with MRI/DTI anatomical volumes, delineation- and label files) is hosted at [NITRC](https://www.nitrc.org/projects/whs-sd-atlas/) along with configuration files for ITK-SNAP, the Mouse BIRN Atlasing Toolkit, and PMOD. The atlas has been adopted as the standard rat brain atlas for the EBRAINS infrastructure, see [EBRAINS Rat Brain Atlas](https://ebrains.eu/service/rat-brain-atlas/). Note that the licence was changed to from CC BY-SA-NC to CC BY-SA on October 1, 2021.",
    digital_identifier={"@id": "https://scicrunch.org/resolver/SCR_001592"},
    full_name="Waxholm Space Atlas of the Sprague Dawley Rat Brain",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": [
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_brain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_whiteMatter"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_olfactoryWhiteMatter"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralOlfactoryTract"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_corpusCallosumAndAssociatedSubcorticalWhiteMatter"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteriorCommissure"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteriorCommissureAnteriorLimb"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteriorCommissurePosteriorLimb"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteriorCommissureIntrabulbarPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hippocampalWhiteMatter"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_alveusOfTheHippocampus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralHippocampalCommissure"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_fornix"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_fimbriaOfTheHippocampus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_corticofugalPathways"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_corticofugalTractAndCoronaRadiata"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pyramidalDecussation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialLemniscus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialLemniscusUnspecified"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialLemniscusDecussation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_thalamicTracts"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_externalMedullaryLamina"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_externalMedullaryLaminaUnspecified"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_externalMedullaryLaminaAuditoryRadiation"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_internalMedullaryLamina"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_intramedullaryThalamicArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superiorCerebellarPeduncleAndPrerubralField"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pretectothalamicLamina"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mammillotegmentalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_commissuralStriaTerminalis"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_fasciculusRetroflexus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_striaMedullarisThalami"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_striaTerminalis"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_habenularCommissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorCommissure"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_facialNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_facialNerveUnspecified"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ascendingFibersOfTheFacialNerve"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_genuOfTheFacialNerve"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_opticFiberSystemAndSupraopticDecussation"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_opticNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_opticTractAndOpticChiasm"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_supraopticDecussation"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_whiteMatterOfTheTectum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_commissureOfTheSuperiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_brachiumOfTheSuperiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculusCommissure"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculusBrachium"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebellarAndPrecerebellarWhiteMatter"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorCerebellarPeduncle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_middleCerebellarPeduncle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_transverseFibersOfThePons"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_whiteMatterOfTheBrainstem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscusCommissure"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscusUnspecified"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_acousticStriae"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_trapezoidBody"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_spinalTrigeminalTract"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_grayMatter"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebrum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebralCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_corticalPlate"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_isocortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_neocortexUnspecified"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_telencephalon"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_laminatedPallium"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_olfactoryBulb"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_glomerularLayerOfTheAccessoryOlfactoryBulb"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_glomerularLayerOfTheOlfactoryBulb"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_olfactoryBulbUnspecified"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusOfTheLateralOlfactoryTract"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebralCortexIncludingTheNeocortexAndTheHippocampus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebralCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hippocampalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hippocampalFormation"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hippocampalFormationUnspecified"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_fasciolaCinereum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_subiculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cornuAmmonis"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cornuAmmonis1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cornuAmmonis2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cornuAmmonis3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dentateGyrus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parahippocampalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_postrhinalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_presubiculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parasubiculum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_perirhinalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_perirhinalArea35"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_perirhinalArea36"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_entorhinalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialEntorhinalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralEntorhinalCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralintermediateEntorhinalArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialEntorhinalField"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_caudalEntorhinalField"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsallateralEntorhinalArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalintermediateEntorhinalArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_piriformCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_piriformCortexLayer1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_piriformCortexLayer2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_piriformCortexLayer3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cingulateRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cingulateCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cingulateArea1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cingulateArea2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_retrosplenialCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_retrosplenialDysgranularArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_retrosplenialGranularArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_insularRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_agranularInsularCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_agranularInsularCortexVentralArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_agranularInsularCortexDorsalArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_agranularInsularCortexPosteriorArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dysgranularInsularCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_granularInsularCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_frontalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_frontalAssociationCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_orbitofrontalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialOrbitalArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralOrbitalArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventrolateralOrbitalArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralOrbitalArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsolateralOrbitalArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mediofrontalCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_prelimbicArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_infralimbicArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_motorCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primaryMotorArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryMotorArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_frontalAssociationArea3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parietalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_somatosensoryCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaFaceRepresentation"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaBarrelField"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaDysgranularZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaForelimbRepresentation"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaHindlimbRepresentation"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaTrunkRepresentation"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondarySomatosensoryArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorParietalCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parietalAssociationCortexMedialArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parietalAssociationCortexLateralArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parietalAssociationCortexPosteriorArea"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_occipitalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_visualCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primaryVisualArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryVisualCortex"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryVisualAreaMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryVisualAreaLateralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_temporalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_temporalAssociationCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_auditoryCortex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primaryAuditoryArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryAuditoryArea"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryAuditoryAreaDorsalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryAuditoryAreaVentralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_corticalSubplate"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebralNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nonlaminatedPallium"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_claustrum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_endopiriformNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_amygdaloidAreaUnspecified"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_subpallium"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_striatum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_caudatePutamen"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusAccumbens"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusAccumbensCore"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusAccumbensShell"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralStriatalRegionUnspecified"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pallidum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_globusPallidusExternal"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_globusPallidusExternalMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_globusPallidusExternalLateralPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_entopeduncularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPallidum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_basalForebrainRegion"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_basalForebrainRegionUnspecified"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_bedNucleusOfTheStriaTerminalis"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_septalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_subthalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_interbrain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_thalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_thalamusUnspecified"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_diencephalon"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_prethalamus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_reticularPrethalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_reticularPrethalamicNucleusUnspecified"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_reticularPrethalamicNucleusAuditorySegment"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncerta"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaDorsalPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaVentralPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaRostralPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaCaudalPart"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaA13DopamineCells"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaA11DopamineCells"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_fieldsOfForel"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pregeniculateNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_subgeniculateNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_intergeniculateLeaflet"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_epithalamus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralHabenularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialHabenularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusOfTheStriaMedullaris"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pinealGland"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalThalamus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteriorNucleiOfTheDorsalThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anterodorsalThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteroventralThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteroventralThalamicNucleusDorsomedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteroventralThalamicNucleusVentrolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteromedialThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_interanteromedialThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalcaudalMidlineGroupOfTheDorsalThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_paraventricularThalamicNucleiAnteriorAndPosterior"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_intermediodorsalThalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parataenialThalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_subparafascicularNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorIntralaminarNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralMidlineGroupOfTheDorsalThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_rhomboidThalamicNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_reuniensThalamicNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_retroreuniensThalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_xiphoidThalamicNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mediodorsalNucleusOfTheDorsalThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mediodorsalThalamicNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mediodorsalThalamicNucleusCentralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mediodorsalThalamicNucleusMedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralNucleiOfTheDorsalThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralAnteriorThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventromedialThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventrolateralThalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_angularThalamicNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPosteriorThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPosteromedialThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPosterolateralThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPosteriorNucleusOfTheThalamusParvicellularPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_submediusThalamicNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_intralaminarNucleiOfTheDorsalThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_paracentralThalamicNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_centralMedialThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_centralLateralThalamicNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parafascicularThalamicNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ethmoidLimitansNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorComplexOfTheDorsalThalamus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorThalamicNucleus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorThalamicNuclearGroupTriangularPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralPosteriorPulvinarComplexOfTheDorsalThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralPosteriorThalamicNucleusMediorostralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralPosteriorThalamicNucleusMediocaudalPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralPosteriorThalamicNucleusLateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_laterodorsalThalamicNucleiOfTheDorsalThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_laterodorsalThalamicNucleusDorsomedialPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_laterodorsalThalamicNucleusVentrolateralPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalLateralGeniculateNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateComplexOfTheDorsalThalamus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateBodyVentralDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateBodyDorsalDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateBodyMarginalZone"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateBodyMedialDivision"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateBodySuprageniculateNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hypothalamus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hypothalamicRegionUnspecified"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pretectum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pretectalRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusSagulum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mesencephalon"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_midbrain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_tectum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculusDorsalCortex"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculusCentralNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculusExternalCortex"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superiorColliculus"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superficialGrayLayerOfTheSuperiorColliculus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_deeperLayersOfTheSuperiorColliculus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_tegmentum"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_substantiaNigra"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_substantiaNigraReticularPart"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_substantiaNigraCompactPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_substantiaNigraLateralPart"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralTegmentalArea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_peripeduncularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_periaqueductalGray"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_interpeduncularNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_brainstem"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_brainstemUnspecified"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hindbrain"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pons"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_rhombencephalon"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_metencephalon"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pontineNuclei"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebellum"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_molecularCellLayerOfTheCerebellum"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebellumUnspecified"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medullaOblongata"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_myelencephalon"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cochlearNucleusVentralPart"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralCochlearNucleusAnteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralCochlearNucleusPosteriorPart"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralCochlearNucleusCapArea"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralCochlearNucleusGranuleCellLayer"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cochlearNucleusDorsalPart"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalCochlearNucleusMolecularLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalCochlearNucleusFusiformAndGranuleLayer"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalCochlearNucleusDeepCore"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_spinalTrigeminalNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_periventricularGray"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superiorOlivaryComplex"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusOfTheTrapezoidBody"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superiorParaolivaryNucleus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialSuperiorOlive"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralSuperiorOlive"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superiorPeriolivaryRegion"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPeriolivaryNuclei"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleiOfTheLateralLemniscus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscusVentralNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscusIntermediateNucleus"
            },
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscusDorsalNucleus"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorOlive"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventricularSystem"},
            {
                "@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventricularSystemUnspecified"
            },
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_4thVentricle"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_centralCanal"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_spinalCord"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_innerEar"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_vestibularApparatus"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cochlea"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cochlearNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_vestibularNerve"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_spiralGanglion"},
        ],
        "ontologyIdentifier": None,
    },
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/WHSSDatlas_v1.01"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/WHSSDatlas_v2"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/WHSSDatlas_v3"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/WHSSDatlas_v3.01"},
        {"@id": "https://openminds.ebrains.eu/instances/brainAtlasVersion/WHSSDatlas_v4"},
    ],
    homepage=IRI("https://www.nitrc.org/projects/whs-sd-atlas/"),
    how_to_cite="Please refer to the atlas by its [RRID:SCR_001592](https://scicrunch.org/resolver/SCR_001592), and cite the first publication [Papp et al. (2014)](https://doi.org/10.1016/j.neuroimage.2014.04.001) along with the atlas version(s) you have used.",
    short_name="Waxholm Space Rat Brain Atlas",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/rattusNorvegicus"},
)
