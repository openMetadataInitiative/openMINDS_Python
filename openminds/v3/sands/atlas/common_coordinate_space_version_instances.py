# this file was auto-generated!


from openminds.base import IRI

from openminds.v3.controlled_terms.anatomical_axes_orientation import AnatomicalAxesOrientation

from openminds.v3.controlled_terms.product_accessibility import ProductAccessibility

from openminds.v3.controlled_terms.unit_of_measurement import UnitOfMeasurement

from openminds.v3.core.data.license import License

from openminds.v3.sands.atlas.common_coordinate_space_version import CommonCoordinateSpaceVersion


CommonCoordinateSpaceVersion.amb_ccf_v1 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/AMB-CCF_v1",
    abbreviation="AMB CCF",
    accessibility=ProductAccessibility.free_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.pir,
    full_name="Allen Mouse Brain Common Coordinate Framework",
    homepage=IRI("https://portal.brain-map.org/"),
    how_to_cite="Lein E, Hawrylycz M, Ao N, et al.; 'Genome-wide atlas of gene expression in the adult mouse brain.'; Nature; Jan 2007; 445(7124):168–176. [doi: 10.1038/nature05453](https://doi.org/10.1038/nature05453)",
    native_unit=UnitOfMeasurement.micrometer,
    short_name="Allen Mouse Brain CCF",
    version_identifier="v1",
    version_innovation="The first version of the 'Allen Mouse Brain Common Coordinate Framework' (CCFv1) is a 3D reconstruction of one brain hemisphere at 200µm resolution.",
)

CommonCoordinateSpaceVersion.amb_ccf_v2 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/AMB-CCF_v2",
    abbreviation="AMB CCF",
    accessibility=ProductAccessibility.free_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.pir,
    full_name="Allen Mouse Brain Common Coordinate Framework",
    homepage=IRI("https://portal.brain-map.org/"),
    how_to_cite="Oh S, Harris J, Ng L, et al.; 'A mesoscale connectome of the mouse brain.'; Nature; Apr 2014; 508(7495):207–214. [doi: 10.1038/nature13186](https://doi.org/10.1038/nature13186)",
    native_unit=UnitOfMeasurement.micrometer,
    short_name="Allen Mouse Brain CCF",
    version_identifier="v2",
    version_innovation="The second version of the 'Allen Mouse Brain Common Coordinate Framework' (CCFv2) is a 3D reconstruction of a whole brain at 100µm resolution.",
)

CommonCoordinateSpaceVersion.amb_ccf_v3 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/AMB-CCF_v3",
    abbreviation="AMB CCF",
    accessibility=ProductAccessibility.free_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.pir,
    axes_origins=[
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 0.0},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 0.0},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 0.0},
    ],
    full_name="Allen Mouse Brain Common Coordinate Framework",
    homepage=IRI("https://portal.brain-map.org/"),
    how_to_cite="Wang Q, Ding S-L, Li Y, et al.; 'The Allen Mouse Brain Common Coordinate Framework: A 3D Reference Atlas.'; Cell; May 2020; 181(4):936-953.e20. [doi: 10.1016/j.cell.2020.04.007](https://doi.org/10.1016/j.cell.2020.04.007)",
    native_unit=UnitOfMeasurement.micrometer,
    release_date="2015-05-01",
    short_name="Allen Mouse Brain CCF",
    version_identifier="v3",
    version_innovation="The third version of the 'Allen Mouse Brain Common Coordinate Framework' (CCFv3) is a 3D reconstruction of a whole brain at 10µm resolution.",
)

CommonCoordinateSpaceVersion.amb_ccf_v3_ras = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/AMB-CCF_v3-RAS",
    abbreviation="AMB CCF",
    accessibility=ProductAccessibility.free_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.ras,
    axes_origins=[
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 0.0},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 0.0},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 0.0},
    ],
    full_name="Allen Mouse Brain Common Coordinate Framework",
    homepage=IRI("https://portal.brain-map.org/"),
    how_to_cite="Wang Q, Ding S-L, Li Y, et al.; 'The Allen Mouse Brain Common Coordinate Framework: A 3D Reference Atlas.'; Cell; May 2020; 181(4):936-953.e20. [doi: 10.1016/j.cell.2020.04.007](https://doi.org/10.1016/j.cell.2020.04.007)",
    native_unit=UnitOfMeasurement.micrometer,
    release_date="2015-05-01",
    short_name="Allen Mouse Brain CCF",
    version_identifier="v3-RAS",
    version_innovation="The third version of the 'Allen Mouse Brain Common Coordinate Framework' (CCFv3-RAS) is a 3D reconstruction of a whole brain at 10µm resolution. This alternative CCFv3 version was transformed to RAS axes orientation.",
)

CommonCoordinateSpaceVersion.big_brain_2015 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/BigBrain_2015",
    abbreviation="BigBrain",
    accessibility=ProductAccessibility.free_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.ras,
    axes_origins=[
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 3338.5795590551184},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 3500.0},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 2776.899244094488},
    ],
    custodians=[
        {"@id": "https://openminds.ebrains.eu/instances/person/evansAlanC"},
        {"@id": "https://openminds.ebrains.eu/instances/person/amuntsKatrin"},
    ],
    full_name="BigBrain Whole-Brain Model",
    homepage=IRI("https://bigbrainproject.org/"),
    native_unit=UnitOfMeasurement.micrometer,
    release_date="2013-06-21",
    short_name="BigBrain Model",
    version_identifier="2015",
    version_innovation="The 'BigBrain Whole-Brain Model' (2015) is an ultrahigh-resolution three-dimensional (3D) model of a brain from a male human subject, deceased at the age of 65 years, at nearly cellular resolution of 20 micrometers. The model is based on a full 3D reconstruction from digital scans of 7404 histological coronal sections, which were stained for cell bodies.",
)

CommonCoordinateSpaceVersion.fs_lr_164k = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/fsLR_164k",
    abbreviation="fsLR",
    full_name="Unbiased FsAverage Left–Right Hybrid Surface Space",
    native_unit=UnitOfMeasurement.millimeter,
    short_name="fsLR Surface Space",
    version_identifier="164k",
    version_innovation="This fsLR Surface Space version has about 163842 (164k) vertices per hemisphere.",
)

CommonCoordinateSpaceVersion.fs_lr_32k = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/fsLR_32k",
    abbreviation="fsLR",
    full_name="Unbiased FsAverage Left–Right Hybrid Surface Space",
    native_unit=UnitOfMeasurement.millimeter,
    short_name="fsLR Surface Space",
    version_identifier="32k",
    version_innovation="This fsLR Surface Space version has about 32492 (32k) vertices per hemisphere.",
)

CommonCoordinateSpaceVersion.fsaverage_3 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/fsaverage_3",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    native_unit=UnitOfMeasurement.millimeter,
    short_name="FsAverage Surface Space",
    version_identifier="3",
    version_innovation="This FsAverage Surface Space version has about 1k vertices per hemisphere.",
)

CommonCoordinateSpaceVersion.fsaverage_4 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/fsaverage_4",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    native_unit=UnitOfMeasurement.millimeter,
    short_name="FsAverage Surface Space",
    version_identifier="4",
    version_innovation="This FsAverage Surface Space version has about 3k vertices per hemisphere.",
)

CommonCoordinateSpaceVersion.fsaverage_5 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/fsaverage_5",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    native_unit=UnitOfMeasurement.millimeter,
    short_name="FsAverage Surface Space",
    version_identifier="5",
    version_innovation="This FsAverage Surface Space version has about 10k vertices per hemisphere.",
)

CommonCoordinateSpaceVersion.fsaverage_6 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/fsaverage_6",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    native_unit=UnitOfMeasurement.millimeter,
    short_name="FsAverage Surface Space",
    version_identifier="6",
    version_innovation="This FsAverage Surface Space version has about 41k vertices per hemisphere.",
)

CommonCoordinateSpaceVersion.fsaverage_7 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/fsaverage_7",
    abbreviation="fsaverage",
    full_name="FsAverage Surface Space",
    native_unit=UnitOfMeasurement.millimeter,
    short_name="FsAverage Surface Space",
    version_identifier="7",
    version_innovation="This FsAverage Surface Space version has about 164k vertices per hemisphere.",
)

CommonCoordinateSpaceVersion.marmoset_nmt_v1 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MarmosetNMT_v1",
    abbreviation="MarmosetNMT",
    accessibility=ProductAccessibility.free_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.lpi,
    description="The Nencki-Monash (NM) template v1.0 (2020) represents a computational morphological average of selected gender-balanced young adult brains of the Common Marmoset monkey (Callithrix jacchus), derived from 3D reconstructions based on Nissl-stained serial sections.",
    full_documentation={"@id": "https://www.marmosetbrain.org/nencki_monash_template/"},
    full_name="The Marmoset Nencki-Monash Template in Stereotaxic Coordinates",
    homepage=IRI("https://www.marmosetbrain.org/nencki_monash_template"),
    how_to_cite="Majka, P., Bednarek, S., Chan, J. M., Jermakow, N., Liu, C., Saworska, G., Worthy, K. H., Silva, A. C., Wójcik, D. K., & Rosa, M. G. P. (2021). Histology-Based Average Template of the Marmoset Cortex With Probabilistic Localization of Cytoarchitectural Areas. NeuroImage, 226, 117625. https://doi.org/10.1016/j.neuroimage.2020.117625.",
    license=License.cc_by_4_0,
    native_unit=UnitOfMeasurement.millimeter,
    related_publications=[{"@id": "https://doi.org/10.1016/j.neuroimage.2020.117625"}],
    release_date="2021-02-01",
    short_name="Marmoset Nencki-Monash Template",
    version_identifier="v1",
    version_innovation="This is the first version of average histology.",
)

CommonCoordinateSpaceVersion.mebrain_stemplate_v1_0 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MEBRAINStemplate_v1.0",
    abbreviation="MEBRAINStemplate",
    accessibility=ProductAccessibility.free_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.ras,
    axes_origins=[
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 108.0},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 128.0},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 70.0},
    ],
    full_name="MEBRAINS population-based monkey brain template",
    native_unit=UnitOfMeasurement.micrometer,
    short_name="MEBRAINS brain template",
    version_identifier="v1.0",
    version_innovation="The first version of the 'MEBRAINS population-based monkey brain template' (v1.0) is a population average brain of T1- and T2-weighted MRI scans from 10 macaque brains. In addition, 9 CT scans of the same monkeys (one missing) are registered to the T1 modality and co-registered to the population average.",
)

CommonCoordinateSpaceVersion.mni__colin27_1998 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-Colin27_1998",
    abbreviation="MNI-Colin27",
    anatomical_axes_orientation=AnatomicalAxesOrientation.ras,
    axes_origins=[
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 75.0},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 111.0},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 67.0},
    ],
    full_name="MNI Colin27 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases"),
    native_unit=UnitOfMeasurement.millimeter,
    release_date="1998-06-01",
    short_name="MNI Colin27 Average Brain",
    version_identifier="1998",
)

CommonCoordinateSpaceVersion.mni__colin27_2008 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-Colin27_2008",
    abbreviation="MNI-Colin27",
    full_name="MNI Colin27 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases"),
    is_alternative_version_of=[
        {"@id": "https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNIColin27_1998"}
    ],
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2006-08-01",
    short_name="MNI Colin27 Average Brain",
    version_identifier="2008",
)

CommonCoordinateSpaceVersion.mni_icbm152_linear_2001_sym = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-ICBM152_linear-2001-sym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152lin"),
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2001 linear symmetric",
)

CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009a_asym = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009a-asym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009a nonlinear asymmetric",
)

CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009a_sym = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009a-sym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009a nonlinear symmetric",
)

CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009b_asym = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009b-asym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009b nonlinear asymmetric",
)

CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009b_sym = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009b-sym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009b nonlinear symmetric",
)

CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009c_asym = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009c-asym",
    abbreviation="ICBM152",
    anatomical_axes_orientation=AnatomicalAxesOrientation.ras,
    axes_origins=[
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 96.0},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 132.0},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 78.0},
    ],
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009c nonlinear asymmetric",
)

CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_2009c_sym = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-2009c-sym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI(
        "https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear-2009"
    ),
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="2009c nonlinear symmetric",
)

CommonCoordinateSpaceVersion.mni_icbm152_nonlinear_6_g_sym = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/MNI-ICBM152_nonlinear-6G-sym",
    abbreviation="ICBM152",
    full_name="MNI ICBM152 Average Brain Stereotaxic Registration Model",
    homepage=IRI("https://www.mcgill.ca/bic/software/tools-data-analysis/anatomical-mri/atlases/icbm152-non-linear"),
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2009-07-01",
    short_name="MNI ICBM152",
    version_identifier="nonlinear 6th generation symmetric",
)

CommonCoordinateSpaceVersion.p__marmoset_bsc_cor_t_v2012__interaural_lsa = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/P-MarmosetBSC-corT_v2012-Interaural-LSA",
    abbreviation="P-MarmosetBSC-corT",
    accessibility=ProductAccessibility.free_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.lsa,
    description="This coordinate space of the coronal plates from Paxinos et al. 'Marmoset Brain in Stereotaxic Coordinates' uses the midpoint of the interaural line as its origin. The coordinates of the origin in the physical coordinate system of the marmoset brain could not be determined from the information provided in the atlas publication. This coordinate space has LSA orientation (X, Y, Z axes are oriented towards left, superior and anterior, respectively). This was obtained by combining information provided in the pdf version of the 1st edition: (1) 'In the common marmoset, the horizontal zero plane is defined as the plane passing thorough the lower margin of the orbit and the center of the external auditory meatus (Figure B). The anteroposterior zero plane is defined as the plane perpendicular to the horizontal zero plane which passes the centers of the external auditory meati. The left-right zero plane is the midsagittal plane [...].' (quoted from chapter 'Introduction', subsection 'Histology', page IX). (2) Based on Figure C (chapter 'Introduction', subsection 'Histology', page X), the fiducial marks were made on the right hemisphere of the marmoset brain. These are visible in some of the photographic plates (e.g., Figure 187a) identifying the left hemisphere as delineated one. Thus, the coordinate system is oriented towards the left since the marmoset's left hemisphere has been used to draw the atlas. A pdf version of the atlas can be accessed from https://r.marmosetbrain.org/Atlas+Small.pdf or https://www.researchgate.net/publication/335871101_PDF_of_The_Marmoset_Brain_in_Stereotaxic_Coordinates.",
    full_documentation={"@id": "https://openminds.ebrains.eu/instances/ISBN/978-0-12-415818-4"},
    full_name="Paxinos et al. Coronal Template of the Marmoset Brain in Stereotaxic Coordinates",
    homepage=IRI("http://www.neura.edu.au/research/themes/paxinos-group"),
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2011-10-11",
    short_name="Paxinos et al. Stereotaxic Coronal Template (Marmoset Brain)",
    version_identifier="v2012 (Interaural, LSA)",
    version_innovation="This is the first version of this stereotaxic coordinate system.",
)

CommonCoordinateSpaceVersion.pw_rbsc_cor_t_v2004__bregma_lia = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Bregma-LIA",
    abbreviation="PW-RBSC-corT",
    accessibility=ProductAccessibility.paid_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.lia,
    description="This coordinate space of the coronal plates from Paxinos and Watson's 'Rat Brain in Stereotaxic Coordinates' uses Bregma as its origin. The coordinates of the origin in the physical coordinate system of the rat brain could not be determined from the information provided in the atlas publication. Since the mediolateral axis of the coordinate system has positive values in either directions, two different coordinate systems were used - one left oriented and one right oriented. The X, Y and Z axes of this coordinate system are oriented towards the left, inferior, anterior (positive mediolateral values describe the rat's left hemisphere), respectively.",
    full_documentation={"@id": "https://openminds.ebrains.eu/instances/ISBN/0-12-547612-4"},
    full_name="Paxinos and Watson's Coronal Template of the Rat Brain in Stereotaxic Coordinates",
    how_to_cite="Paxinos, G. and Watson, C. (2004) The Rat Brain in Stereotaxic Coordinates. 5th Edition, Academic Press, San Diego.",
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2004-11-10",
    short_name="Paxinos and Watson's Stereotaxic Coronal Template (Rat Brain)",
    version_identifier="v2004 (Bregma, LIA)",
    version_innovation="This is the second version of the common coordinate space for the coronal plane atlas. From the 4th to the 5th edition of the Paxinos and Watson's The Rat Brain in Stereotaxic Coordinates, the reference data (template) was changed (new adult male Wistar rat with a more complete coronal series) which resulted in a new common coordinate space version.",
)

CommonCoordinateSpaceVersion.pw_rbsc_cor_t_v2004__bregma_ria = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Bregma-RIA",
    abbreviation="PW-RBSC-corT",
    accessibility=ProductAccessibility.paid_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.ria,
    description="This coordinate space of the coronal plates from Paxinos and Watson's 'Rat Brain in Stereotaxic Coordinates' uses Bregma as its origin. The coordinates of the origin in the physical coordinate system of the rat brain could not be determined from the information provided in the atlas publication. Since the mediolateral axis of the coordinate system has positive values in either directions, two different coordinate systems were used - one left oriented and one right oriented. The X, Y and Z axes of this coordinate system are oriented towards the right, anterior, inferior (positive mediolateral values describe the rat's right hemisphere), respectively.",
    full_documentation={"@id": "https://openminds.ebrains.eu/instances/ISBN/0-12-547612-4"},
    full_name="Paxinos and Watson's Coronal Template of the Rat Brain in Stereotaxic Coordinates",
    how_to_cite="Paxinos, G. and Watson, C. (2004) The Rat Brain in Stereotaxic Coordinates. 5th Edition, Academic Press, San Diego.",
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2004-11-10",
    short_name="Paxinos and Watson's Stereotaxic Coronal Template (Rat Brain)",
    version_identifier="v2004 (Bregma, RIA)",
    version_innovation="This is the second version of the common coordinate space for the coronal plane atlas. From the 4th to the 5th edition of the Paxinos and Watson's The Rat Brain in Stereotaxic Coordinates, the reference data (template) was changed (new adult male Wistar rat with a more complete coronal series) which resulted in a new common coordinate space version.",
)

CommonCoordinateSpaceVersion.pw_rbsc_cor_t_v2004__interaural_lsa = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Interaural-LSA",
    abbreviation="PW-RBSC-corT",
    accessibility=ProductAccessibility.paid_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.lsa,
    description="This coordinate space of the coronal plates from Paxinos and Watson's 'Rat Brain in Stereotaxic Coordinates' uses the midpoint of the interaural line as its origin. The coordinates of the origin in the physical coordinate system of the rat brain could not be determined from the information provided in the atlas publication. Since the mediolateral axis of the coordinate system has positive values in either directions, two different coordinate systems were used - one left oriented and one right oriented. The X, Y and Z axes of this coordinate system are oriented towards the left, superior, anterior (positive mediolateral values describe the rat's left hemisphere), respectively.",
    full_documentation={"@id": "https://openminds.ebrains.eu/instances/ISBN/0-12-547612-4"},
    full_name="Paxinos and Watson's Coronal Template of the Rat Brain in Stereotaxic Coordinates",
    how_to_cite="Paxinos, G. and Watson, C. (2004) The Rat Brain in Stereotaxic Coordinates. 5th Edition, Academic Press, San Diego.",
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2004-11-10",
    short_name="Paxinos and Watson's Stereotaxic Coronal Template (Rat Brain)",
    version_identifier="v2004 (Interaural, LSA)",
    version_innovation="This is the second version of the common coordinate space for the coronal plane atlas. From the 4th to the 5th edition of the Paxinos and Watson's The Rat Brain in Stereotaxic Coordinates, the reference data (template) was changed (new adult male Wistar rat with a more complete coronal series) which resulted in a new common coordinate space version.",
)

CommonCoordinateSpaceVersion.pw_rbsc_cor_t_v2004__interaural_rsa = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/PW-RBSC-corT_v2004-Interaural-RSA",
    abbreviation="PW-RBSC-corT",
    accessibility=ProductAccessibility.paid_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.rsa,
    description="This coordinate space of the coronal plates from Paxinos and Watson's 'Rat Brain in Stereotaxic Coordinates' uses the midpoint of the interaural line as its origin. The coordinates of the origin in the physical coordinate system of the rat brain could not be determined from the information provided in the atlas publication. Since the mediolateral axis of the coordinate system has positive values in either directions, two different coordinate systems were used - one left oriented and one right oriented. The X, Y and Z axes of this coordinate system are oriented towards the right, superior, anterior (positive mediolateral values describe the rat's right hemisphere), respectively.",
    full_documentation={"@id": "https://openminds.ebrains.eu/instances/ISBN/0-12-547612-4"},
    full_name="Paxinos and Watson's Coronal Template of the Rat Brain in Stereotaxic Coordinates",
    how_to_cite="Paxinos, G. and Watson, C. (2004) The Rat Brain in Stereotaxic Coordinates. 5th Edition, Academic Press, San Diego.",
    native_unit=UnitOfMeasurement.millimeter,
    release_date="2004-11-10",
    short_name="Paxinos and Watson's Stereotaxic Coronal Template (Rat Brain)",
    version_identifier="v2004 (Interaural, RSA)",
    version_innovation="This is the second version of the common coordinate space for the coronal plane atlas. From the 4th to the 5th edition of the Paxinos and Watson's The Rat Brain in Stereotaxic Coordinates, the reference data (template) was changed (new adult male Wistar rat with a more complete coronal series) which resulted in a new common coordinate space version.",
)

CommonCoordinateSpaceVersion.swanson_srb_v1992 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/SwansonSRB_v1992",
    abbreviation="SwansonSRB",
    accessibility=ProductAccessibility.free_access,
    anatomical_axes_orientation=AnatomicalAxesOrientation.ria,
    axes_origins=[
        {
            "@type": "https://openminds.ebrains.eu/core/QuantitativeValue",
            "typeOfUncertainty": None,
            "uncertainty": None,
            "unit": {"@id": "https://openminds.ebrains.eu/instances/unitOfMeasurement/millimeter"},
            "value": 0,
        },
        {
            "@type": "https://openminds.ebrains.eu/core/QuantitativeValue",
            "typeOfUncertainty": None,
            "uncertainty": None,
            "unit": {"@id": "https://openminds.ebrains.eu/instances/unitOfMeasurement/millimeter"},
            "value": 12,
        },
        {
            "@type": "https://openminds.ebrains.eu/core/QuantitativeValue",
            "typeOfUncertainty": None,
            "uncertainty": None,
            "unit": {"@id": "https://openminds.ebrains.eu/instances/unitOfMeasurement/millimeter"},
            "value": 8.11,
        },
    ],
    description="The coordinate space of Swanson’s ‘Brain Maps: Structure of the Rat Brain’ uses Bregma as its origin. The coordinates stated under ‘axesOrigin’ are the coordinates of the origin in the physical coordinate system of the rat brain. The coordinates, AP = 8.11 mm, DV = 12 mm and ML = 0 mm, were obtained by combining the information provided in the physical book and the pdf version of the 3rd edition of Brain Maps: (1) 'In the physical coordinate system, the z axis begins (= 0) at the rostral tip of the olfactory bulb, the y axis begins along an imaginary line that corresponds approximately to a surface that the extracted brain is lying upon, and the x axis begins at the midline.' (quoted from chapter [‘B. Coordinate Systems: Stereotaxic Surgery and Databases’ of the 3rd edition of Brain Maps (pdf version from Swanson’s homepage)](http://larrywswanson.com/wp-content/uploads/2015/03/2-Atlas-prep-BrainMaps3-20041.pdf)). (2) 'The rostrocaudal coordinate is given in parentheses after the corresponding physical coordinates, and the other two (dorsoventral and mediolateral) can be obtained with the transparent overlay provided in Appendix B.' (quoted from chapter ‘D. How to Use this Atlas’ of the 3rd edition of Brain Maps, p. 15; ISBN: 0-126-10582-0). Based on Figure 4 from chapter [‘A. Histology and Map Production’ of the 3rd edition of Brain Maps (pdf version from Swanson’s homepage)](http://larrywswanson.com/wp-content/uploads/2015/03/2-Atlas-prep-BrainMaps3-20041.pdf)), the coordinate system is oriented towards the right since the rat’s right hemisphere has been used to draw the atlas. Thus, giving Swanson’s coordinate system RIA orientation (X, Y, Z axes are oriented towards right, inferior and anterior, respectively). Note: More detailed descriptions were provided in the 3rd edition of the atlas (digital and book combined) compared to the 1st edition, but both describe the exact same coordinate system.",
    full_documentation={"@id": "https://larrywswanson.com/?page_id=164"},
    full_name="Swanson's Stereotactic Brain of the Sprague Dawley Rat",
    how_to_cite="Swanson, L.W. (1992) 'Coordinate Systems' Brain maps: structure of the rat brain, 1st edition.",
    license=License.cc_by_nc_4_0,
    native_unit=UnitOfMeasurement.millimeter,
    release_date="1992-12-24",
    short_name="Swanson's Stereotactic Rat Brain",
    version_identifier="v1992",
    version_innovation="This is the first version of this common coordinate space.",
)

CommonCoordinateSpaceVersion.whssd_v1 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/WHSSD_v1",
    abbreviation="WHSSD",
    anatomical_axes_orientation=AnatomicalAxesOrientation.als,
    full_name="Waxholm Space of the Sprague Dawley Rat Brain (coordinate space)",
    homepage=IRI("https://www.nitrc.org/projects/whs-sd-atlas"),
    native_unit=UnitOfMeasurement.micrometer,
    release_date="2014-07-16",
    short_name="WHS of the SD Rat Brain",
    version_identifier="v1",
)

CommonCoordinateSpaceVersion.whssd_v1_01 = CommonCoordinateSpaceVersion(
    id="https://openminds.ebrains.eu/instances/commonCoordinateSpaceVersion/WHSSD_v1.01",
    abbreviation="WHSSD",
    anatomical_axes_orientation=AnatomicalAxesOrientation.ras,
    axes_origins=[
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 243.9999936},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 622.9999808},
        {"@type": "https://openminds.ebrains.eu/core/QuantitativeValue", "value": 247.9999936},
    ],
    full_name="Waxholm Space of the Sprague Dawley Rat Brain (coordinate space)",
    homepage=IRI("https://www.nitrc.org/projects/whs-sd-atlas"),
    native_unit=UnitOfMeasurement.micrometer,
    release_date="2014-07-16",
    short_name="WHS of the SD Rat Brain",
    version_identifier="v1.01",
)


CommonCoordinateSpaceVersion.amb_ccf_v2.is_new_version_of = CommonCoordinateSpaceVersion.amb_ccf_v1

CommonCoordinateSpaceVersion.amb_ccf_v3.is_alternative_version_of = [CommonCoordinateSpaceVersion.amb_ccf_v3_ras]

CommonCoordinateSpaceVersion.amb_ccf_v3.is_new_version_of = CommonCoordinateSpaceVersion.amb_ccf_v2

CommonCoordinateSpaceVersion.amb_ccf_v3_ras.is_alternative_version_of = [CommonCoordinateSpaceVersion.amb_ccf_v3]

CommonCoordinateSpaceVersion.amb_ccf_v3_ras.is_new_version_of = CommonCoordinateSpaceVersion.amb_ccf_v2

CommonCoordinateSpaceVersion.mni__colin27_1998.is_alternative_version_of = [
    CommonCoordinateSpaceVersion.mni__colin27_2008
]

CommonCoordinateSpaceVersion.whssd_v1_01.is_new_version_of = CommonCoordinateSpaceVersion.whssd_v1
