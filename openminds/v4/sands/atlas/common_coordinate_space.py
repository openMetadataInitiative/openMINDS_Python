"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class CommonCoordinateSpace(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CommonCoordinateSpace"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this common coordinate space.",
        ),
        Property(
            "authors",
            ["openminds.v4.core.Consortium", "openminds.v4.core.Organization", "openminds.v4.core.Person"],
            "author",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Creator of a literary or creative work, as well as a dataset publication.",
            instructions="Add all parties that contributed to this common coordinate space as authors.",
        ),
        Property(
            "custodians",
            ["openminds.v4.core.Consortium", "openminds.v4.core.Organization", "openminds.v4.core.Person"],
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
            description="Longer statement or account giving the characteristics of the common coordinate space.",
            instructions="Enter a description (or abstract) of this research product. Note that this should be a suitable description for all attached research product versions.",
        ),
        Property(
            "digital_identifier",
            ["openminds.v4.core.DOI", "openminds.v4.core.ISBN", "openminds.v4.core.RRID"],
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
            description="Whole, non-abbreviated name of the common coordinate space.",
            instructions="Enter a descriptive full name (or title) for this research product. Note that this should be a suitable full name for all attached research product versions.",
        ),
        Property(
            "has_versions",
            "openminds.v4.sands.CommonCoordinateSpaceVersion",
            "hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="Reference to variants of an original.",
            instructions="Add all versions of this common coordinate space.",
        ),
        Property(
            "homepage",
            IRI,
            "homepage",
            description="Main website of the common coordinate space.",
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
            "ontology_identifiers",
            str,
            "ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify the common coordinate space registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this common coordinate space.",
        ),
        Property(
            "short_name",
            str,
            "shortName",
            formatting="text/plain",
            required=True,
            description="Shortened or fully abbreviated name of the common coordinate space.",
            instructions="Enter a short name (or alias) for this research product that could be used as a shortened display title (e.g., for web services with too little space to display the full name).",
        ),
        Property(
            "used_species",
            "openminds.v4.controlled_terms.Species",
            "usedSpecies",
            required=True,
            description="no description available",
            instructions="Add the species that was used for the creation of this common coordinate space.",
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
        has_versions=None,
        homepage=None,
        how_to_cite=None,
        ontology_identifiers=None,
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
            has_versions=has_versions,
            homepage=homepage,
            how_to_cite=how_to_cite,
            ontology_identifiers=ontology_identifiers,
            short_name=short_name,
            used_species=used_species,
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
            matches = cls._instance_lookup.get(name, None)
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if all:
            return matches
        elif len(matches) > 0:
            return matches[0]
        else:
            return None


CommonCoordinateSpace.amb_ccf = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/AMB-CCF",
    abbreviation="AMB CCF",
    description="The 'Allen Mouse Brain Common Coordinate Framework' is a 3D reconstruction of an averaged adult mouse brain.",
    full_name="Allen Mouse Brain Common Coordinate Framework",
    has_versions=[
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v3-RAS"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v3"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v2"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/AMB-CCF_v1"},
    ],
    homepage=IRI("https://portal.brain-map.org/"),
    short_name="Allen Mouse Brain CCF",
    used_species={"@id": "https://openminds.om-i.org/instances/species/musMusculus"},
)
CommonCoordinateSpace.big_brain = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/BigBrain",
    abbreviation="BigBrain",
    description="The 'BigBrain Whole-Brain Model' is a 3D reconstruction of a human brain in extremely high resolution.",
    full_name="BigBrain Whole-Brain Model",
    has_versions=[{"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/BigBrain_2015"}],
    homepage=IRI("https://bigbrainproject.org/"),
    short_name="BigBrain Model",
    used_species={"@id": "https://openminds.om-i.org/instances/species/homoSapiens"},
)
CommonCoordinateSpace.fs_lr = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/fsLR",
    abbreviation="fsLR",
    description="The 'Unbiased FsAverage Left–Right Hybrid Surface Space' (fsLR) brings the left and right fsaverage surfaces into geographic correspondence using Landmark-SBR ([Van Essen et al. 2011](https://doi.org/10.1093/cercor/bhr291)).",
    full_name="Unbiased FsAverage Left–Right Hybrid Surface Space",
    has_versions=[
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsLR_32k"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsLR_164k"},
    ],
    short_name="fsLR Surface Space",
    used_species={"@id": "https://openminds.om-i.org/instances/species/homoSapiens"},
)
CommonCoordinateSpace.fsaverage = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/fsaverage",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    has_versions=[
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsaverage_3"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsaverage_4"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsaverage_5"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsaverage_6"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/fsaverage_7"},
    ],
    short_name="FsAverage Surface Space",
    used_species={"@id": "https://openminds.om-i.org/instances/species/homoSapiens"},
)
CommonCoordinateSpace.marmoset_nmt = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/MarmosetNMT",
    abbreviation="MarmosetNMT",
    description="Stereotactic coordinate space of the coronal plane generated using computational average of histology sections.",
    full_name="The Marmoset Nencki-Monash Template in Stereotaxic Coordinates",
    has_versions=[{"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MarmosetNMT_v1"}],
    homepage=IRI("https://www.marmosetbrain.org/nencki_monash_template"),
    how_to_cite="Please refer to the template by its RRID:SCR_018367, and cite the publication of the version of the template you have used.",
    short_name="Marmoset Nencki-Monash Template",
    used_species={"@id": "https://openminds.om-i.org/instances/species/callithrixJacchus"},
)
CommonCoordinateSpace.mebrain_stemplate = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/MEBRAINStemplate",
    abbreviation="MEBRAINStemplate",
    description="The 'MEBRAINS population-based monkey brain template' is a multi-subject based, multi-modal, volume and surface brain template for macaque monkeys.",
    full_name="MEBRAINS population-based monkey brain template",
    has_versions=[{"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MEBRAINStemplate_v1.0"}],
    short_name="MEBRAINS brain template",
    used_species={"@id": "https://openminds.om-i.org/instances/species/macacaMulatta"},
)
CommonCoordinateSpace.mni__colin27 = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/MNI-Colin27",
    abbreviation="MNI-Colin27",
    description="The 'MNI Colin 27 Average Brain Stereotaxic Registration Model' is a stereotaxic average of 27 T1-weighted MRI scans of the same individual. It was created at the Montreal Neurological Institute (MNI) in a two step process: (1) each of the 27 T1-weighted scans were registered to stereotaxic space using MRITOTAL (an automated volumetric registration procedure) and resampled onto a 1mm grid. All 27 scans were averaged together to create an initial average. (2) The initial average volume was used as a target for a second phase of registration where each original T1-weighted MRI was re-registered in stereotaxic space. This two-step procedure has the advantage of removing the small variance in intra-subject mapping in stereotaxic space associated with the use of a multi-subject average resulting in an average brain stereotaxic registration model with high signal-to-noise ratio and structure definition.",
    full_name="MNI Colin27 Average Brain Stereotaxic Registration Model",
    has_versions=[
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-Colin27_1998"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-Colin27_2008"},
    ],
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases"),
    how_to_cite="Holmes CJ, Hoge R, Collins L, Woods R, Toga AW, and Evans AC; 'Enhancement of MR images using registration for signal averaging.'; J Comput Assist Tomogr; 1998 Mar-Apr; 22(2):324–33. [doi: 10.1097/00004728-199803000-00032](http://dx.doi.org/10.1097/00004728-199803000-00032) Aubert-Broche B, Evans AC, and Collins DL; 'A new improved version of the realistic digital brain phantom'; NeuroImage; 2006 Aug;32(1):138–45. [doi: 10.1016/j.neuroimage.2006.03.052](https://doi.org/10.1016/j.neuroimage.2006.03.052)",
    short_name="MNI Colin27 Average Brain",
    used_species={"@id": "https://openminds.om-i.org/instances/species/homoSapiens"},
)
CommonCoordinateSpace.mni_icbm152 = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/MNI-ICBM152",
    abbreviation="ICBM152",
    description="The 'MNI ICBM152 Average Brain Stereotaxic Registration Model' is an average of T1-weighted magnetic resonance imaging (MRI) scans from 152 normative young adults.",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    has_versions=[
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_linear-2001-sym"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-6G-sym"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009a-asym"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009a-sym"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009b-asym"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009b-sym"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009c-asym"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009c-sym"},
    ],
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases"),
    short_name="MNI ICBM152",
    used_species={"@id": "https://openminds.om-i.org/instances/species/homoSapiens"},
)
CommonCoordinateSpace.p__marmoset_bsc_cor_t = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/P-MarmosetBSC-corT",
    abbreviation="P-MarmosetBSC-corT",
    description="Stereotactic coordinate space of the coronal plane.",
    full_name="Paxinos et al. Coronal Template of the Marmoset Brain in Stereotaxic Coordinates",
    has_versions=[
        {
            "@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/P-MarmosetBSC-corT_v2012-Interaural-LSA"
        }
    ],
    homepage=IRI("http://www.neura.edu.au/research/themes/paxinos-group"),
    short_name="Paxinos et al. Stereotaxic Coronal Template (Marmoset Brain)",
    used_species={"@id": "https://openminds.om-i.org/instances/species/callithrixJacchus"},
)
CommonCoordinateSpace.pw_rbsc_cor_t = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/PW-RBSC-corT",
    abbreviation="PW-RBSC-corT",
    description="Stereotactic coordinate space of the coronal plane.",
    full_name="Paxinos and Watson's Coronal Template of the Rat Brain in Stereotaxic Coordinates",
    has_versions=[
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Bregma-LIA"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Bregma-RIA"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Interaural-LSA"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Interaural-RSA"},
    ],
    short_name="Paxinos and Watson's Stereotaxic Coronal Template (Rat Brain)",
    used_species={"@id": "https://openminds.om-i.org/instances/species/rattusNorvegicus"},
)
CommonCoordinateSpace.swanson_srb = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/SwansonSRB",
    abbreviation="SwansonSRB",
    description="Stereotactic coordinate system derived from the atlas by Paxinos and Watson (1986; ISBN: 0-12-547621-3).",
    full_name="Swanson's Stereotactic Brain of the Sprague Dawley Rat",
    has_versions=[{"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/SwansonSRB_v1992"}],
    short_name="Swanson's Stereotactic Rat Brain",
    used_species={"@id": "https://openminds.om-i.org/instances/species/rattusNorvegicus"},
)
CommonCoordinateSpace.whssd = CommonCoordinateSpace(
    id="https://openminds.om-i.org/instances/commonCoordinateSpace/WHSSD",
    abbreviation="WHSSD",
    description="The 'Waxholm Space of the Sprague Dawley Rat Brain (coordinate space)' employs a continuous three- dimensional Cartesian coordinate system, with its origin set at the decussation of the anterior commissure.",
    full_name="Waxholm Space of the Sprague Dawley Rat Brain (coordinate space)",
    has_versions=[
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/WHSSD_v1.01"},
        {"@id": "https://openminds.om-i.org/instances/commonCoordinateSpaceVersion/WHSSD_v1"},
    ],
    homepage=IRI("https://www.nitrc.org/projects/whs-sd-atlas"),
    short_name="WHS of the SD Rat Brain",
    used_species={"@id": "https://openminds.om-i.org/instances/species/rattusNorvegicus"},
)
