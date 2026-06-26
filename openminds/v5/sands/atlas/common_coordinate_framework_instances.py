# this file was auto-generated!


from openminds.base import IRI

from openminds.v5.controlled_terms.species import Species

from openminds.v5.sands.atlas.common_coordinate_framework import CommonCoordinateFramework


CommonCoordinateFramework.amb_ccf = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/AMB-CCF",
    abbreviation="AMB CCF",
    description="The 'Allen Mouse Brain Common Coordinate Framework' is a 3D reconstruction of an averaged adult mouse brain.",
    full_name="Allen Mouse Brain Common Coordinate Framework",
    homepage=IRI("https://portal.brain-map.org/"),
    short_name="Allen Mouse Brain CCF",
    used_taxon=Species.mus_musculus,
)

CommonCoordinateFramework.big_brain = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/BigBrain",
    abbreviation="BigBrain",
    description="The 'BigBrain Whole-Brain Model' is a 3D reconstruction of a human brain in extremely high resolution.",
    full_name="BigBrain Whole-Brain Model",
    homepage=IRI("https://bigbrainproject.org/"),
    short_name="BigBrain Model",
    used_taxon=Species.homo_sapiens,
)

CommonCoordinateFramework.fs_lr = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/fsLR",
    abbreviation="fsLR",
    description="The 'Unbiased FsAverage Left–Right Hybrid Surface Space' (fsLR) brings the left and right fsaverage surfaces into geographic correspondence using Landmark-SBR ([Van Essen et al. 2011](https://doi.org/10.1093/cercor/bhr291)).",
    full_name="Unbiased FsAverage Left–Right Hybrid Surface Space",
    short_name="fsLR Surface Space",
    used_taxon=Species.homo_sapiens,
)

CommonCoordinateFramework.fsaverage = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/fsaverage",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    short_name="FsAverage Surface Space",
    used_taxon=Species.homo_sapiens,
)

CommonCoordinateFramework.marmoset_nmt = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/MarmosetNMT",
    abbreviation="MarmosetNMT",
    description="Stereotactic coordinate space of the coronal plane generated using computational average of histology sections.",
    full_name="The Marmoset Nencki-Monash Template in Stereotaxic Coordinates",
    homepage=IRI("https://www.marmosetbrain.org/nencki_monash_template"),
    how_to_cite="Please refer to the template by its RRID:SCR_018367, and cite the publication of the version of the template you have used.",
    short_name="Marmoset Nencki-Monash Template",
    used_taxon=Species.callithrix_jacchus,
)

CommonCoordinateFramework.mebrain_stemplate = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/MEBRAINStemplate",
    abbreviation="MEBRAINStemplate",
    description="The 'MEBRAINS population-based monkey brain template' is a multi-subject based, multi-modal, volume and surface brain template for macaque monkeys.",
    full_name="MEBRAINS population-based monkey brain template",
    short_name="MEBRAINS brain template",
    used_taxon=Species.macaca_mulatta,
)

CommonCoordinateFramework.mni__colin27 = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/MNI-Colin27",
    abbreviation="MNI-Colin27",
    description="The 'MNI Colin 27 Average Brain Stereotaxic Registration Model' is a stereotaxic average of 27 T1-weighted MRI scans of the same individual. It was created at the Montreal Neurological Institute (MNI) in a two step process: (1) each of the 27 T1-weighted scans were registered to stereotaxic space using MRITOTAL (an automated volumetric registration procedure) and resampled onto a 1mm grid. All 27 scans were averaged together to create an initial average. (2) The initial average volume was used as a target for a second phase of registration where each original T1-weighted MRI was re-registered in stereotaxic space. This two-step procedure has the advantage of removing the small variance in intra-subject mapping in stereotaxic space associated with the use of a multi-subject average resulting in an average brain stereotaxic registration model with high signal-to-noise ratio and structure definition.",
    full_name="MNI Colin27 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases"),
    how_to_cite="Holmes CJ, Hoge R, Collins L, Woods R, Toga AW, and Evans AC; 'Enhancement of MR images using registration for signal averaging.'; J Comput Assist Tomogr; 1998 Mar-Apr; 22(2):324–333. [doi: 10.1097/00004728-199803000-00032](http://dx.doi.org/10.1097/00004728-199803000-00032) Aubert-Broche B, Evans AC, and Collins DL; 'A new improved version of the realistic digital brain phantom'; NeuroImage; 2006 Aug;32(1):138–145. [doi: 10.1016/j.neuroimage.2006.03.052](https://doi.org/10.1016/j.neuroimage.2006.03.052)",
    short_name="MNI Colin27 Average Brain",
    used_taxon=Species.homo_sapiens,
)

CommonCoordinateFramework.mni_icbm152 = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/MNI-ICBM152",
    abbreviation="ICBM152",
    description="The 'MNI ICBM152 Average Brain Stereotaxic Registration Model' is an average of T1-weighted magnetic resonance imaging (MRI) scans from 152 normative young adults.",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases"),
    short_name="MNI ICBM152",
    used_taxon=Species.homo_sapiens,
)

CommonCoordinateFramework.p__marmoset_bsc_cor_t = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/P-MarmosetBSC-corT",
    abbreviation="P-MarmosetBSC-corT",
    description="Stereotactic coordinate space of the coronal plane.",
    full_name="Paxinos et al. Coronal Template of the Marmoset Brain in Stereotaxic Coordinates",
    homepage=IRI("http://www.neura.edu.au/research/themes/paxinos-group"),
    short_name="Paxinos et al. Stereotaxic Coronal Template (Marmoset Brain)",
    used_taxon=Species.callithrix_jacchus,
)

CommonCoordinateFramework.pw_rbsc_cor_t = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/PW-RBSC-corT",
    abbreviation="PW-RBSC-corT",
    description="Stereotactic coordinate space of the coronal plane.",
    full_name="Paxinos and Watson's Coronal Template of the Rat Brain in Stereotaxic Coordinates",
    short_name="Paxinos and Watson's Stereotaxic Coronal Template (Rat Brain)",
    used_taxon=Species.rattus_norvegicus,
)

CommonCoordinateFramework.swanson_srb = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/SwansonSRB",
    abbreviation="SwansonSRB",
    description="Stereotactic coordinate system derived from the atlas by Paxinos and Watson (1986; ISBN: 0-12-547621-3).",
    full_name="Swanson's Stereotactic Brain of the Sprague Dawley Rat",
    short_name="Swanson's Stereotactic Rat Brain",
    used_taxon=Species.rattus_norvegicus,
)

CommonCoordinateFramework.whssd = CommonCoordinateFramework(
    id="https://openminds.om-i.org/instances/commonCoordinateFramework/WHSSD",
    abbreviation="WHSSD",
    description="The 'Waxholm Space of the Sprague Dawley Rat Brain (coordinate space)' employs a continuous three- dimensional Cartesian coordinate system, with its origin set at the decussation of the anterior commissure.",
    full_name="Waxholm Space of the Sprague Dawley Rat Brain (coordinate space)",
    homepage=IRI("https://www.nitrc.org/projects/whs-sd-atlas"),
    short_name="WHS of the SD Rat Brain",
    used_taxon=Species.rattus_norvegicus,
)
