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
            description="Longer statement or account giving the characteristics of someone or something.",
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
            description="Whole, non-abbreviated name of something or somebody.",
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
            description="Main website of something or someone.",
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
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifier (IRI) to the related ontological term matching this brain atlas.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of something or somebody.",
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
    homepage="https://www.gin.cnrs.fr/en/tools/aal/",
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
    homepage="https://portal.brain-map.org/",
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
    homepage="https://julich-brain-atlas.de/",
    how_to_cite="Please refer to the atlas by its [RRID:SCR_023277](https://scicrunch.org/resolver/SCR_023277), and cite the two main publications [Amunts and Zilles (2015)](https://doi.org/10.1016/j.neuron.2015.12.001) AND [Amunts et al. (2020)](https://doi.org/10.1126/science.abb4588) along with the atlas version(s) you have used.",
    short_name="Julich-Brain Atlas",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/homoSapiens"},
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
    homepage="https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal",
    short_name="Schaefer Atlas (400p)",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/homoSapiens"},
)
BrainAtlas.swma = BrainAtlas(
    id="https://openminds.ebrains.eu/instances/brainAtlas/SWMA",
    abbreviation="SWMA",
    full_name="Atlas of Superficial White Matter Fibre Bundles",
    has_terminology={
        "@type": "https://openminds.ebrains.eu/sands/ParcellationTerminology",
        "dataLocation": None,
        "hasEntity": [
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CAC-PoCi_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CAC-PrCu_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-Op_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-PoC_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-PrC_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-PrC_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-RMF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-SF_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Cu-Li_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Fu-LO_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Fu-LO_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IC-PrCu_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-IT_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-LO_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-LO_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-MT_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-SM_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-SP_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-SP_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IT-MT_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IT-MT_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IT-MT_2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LO-SP_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LOF-MOF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LOF-Or_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LOF-RMF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LOF-RMF_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LOF-ST_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_MOF-ST_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_MT-SM_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_MT-ST_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Op-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Op-PrC_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Op-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Op-Tr_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Or-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-PrC_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-PrC_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-PrC_2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-PrC_3"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-SM_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-SM_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-SP_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-SP_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoCi-PrCu_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoCi-PrCu_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoCi-PrCu_2"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoCi-RAC_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoCi-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PrC-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PrC-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PrC-SM_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PrC-SP_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_RAC-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_RAC-SF_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_RMF-SF_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_RMF-SF_1"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_SM-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_SP-SM_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_ST-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_ST-TT_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_superficialWhiteMatter"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Tr-Ins_0"},
            {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Tr-SF_0"},
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
    homepage="https://www.nitrc.org/projects/whs-sd-atlas/",
    how_to_cite="Please refer to the atlas by its [RRID:SCR_001592](https://scicrunch.org/resolver/SCR_001592), and cite the first publication [Papp et al. (2014)](https://doi.org/10.1016/j.neuroimage.2014.04.001) along with the atlas version(s) you have used.",
    short_name="Waxholm Space Rat Brain Atlas",
    used_species={"@id": "https://openminds.ebrains.eu/instances/species/rattusNorvegicus"},
)
