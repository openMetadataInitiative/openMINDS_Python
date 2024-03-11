"""
Structured information on the content type of a file instance, bundle or repository.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ContentType(LinkedMetadata):
    """
    Structured information on the content type of a file instance, bundle or repository.
    """

    type_ = "https://openminds.ebrains.eu/core/ContentType"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "data_types",
            "openminds.latest.controlled_terms.DataType",
            "dataType",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="no description available",
            instructions="Add all data types that may be represented via this content type.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a description of the content type specification. Leave blank if an official and public specification is linked under 'specification' for this content type.",
        ),
        Property(
            "display_label",
            str,
            "displayLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a display label for this content type.",
        ),
        Property(
            "file_extensions",
            str,
            "fileExtension",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="String of characters attached as suffix to the names of files of a particular format.",
            instructions="Enter all file extensions associated with this content type.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this content type following a IANA.org inspired convention.",
        ),
        Property(
            "related_media_type",
            IRI,
            "relatedMediaType",
            description="Reference to an official two-part identifier for file formats and format contents.",
            instructions="Enter the internationalized resource identifier (IRI) to the official registered media type (e.g., provided on IANA.org) matching this content type.",
        ),
        Property(
            "specification",
            IRI,
            "specification",
            description="Detailed and precise presentation of, or proposal for something.",
            instructions="Enter the internationalized resource identifier (IRI) to the official specification of this content type. If no official and public specification is available, leave blank and enter the specification under 'description'.",
        ),
        Property(
            "synonyms",
            str,
            "synonym",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
            instructions="Enter any synonyms of this content type.",
        ),
    ]

    def __init__(
        self,
        id=None,
        data_types=None,
        description=None,
        display_label=None,
        file_extensions=None,
        name=None,
        related_media_type=None,
        specification=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            data_types=data_types,
            description=description,
            display_label=display_label,
            file_extensions=file_extensions,
            name=name,
            related_media_type=related_media_type,
            specification=specification,
            synonyms=synonyms,
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


ContentType.application_4_mat = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_4-mat",
    file_extensions=[".mat"],
    name="application/4-mat",
    synonyms=["Level 4 MAT-file format", "MAT"],
)
ContentType.application_5_mat = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_5-mat",
    file_extensions=[".mat"],
    name="application/5-mat",
    synonyms=["Level 5 MAT-file format", "MAT"],
)
ContentType.application_dicom = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_dicom",
    file_extensions=[".dcm"],
    name="application/dicom",
    related_media_type="https://www.iana.org/assignments/media-types/application/dicom",
    synonyms=["Digital Imaging and Communications in Medicine", "DICOM"],
)
ContentType.application_json = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_json",
    file_extensions=[".json"],
    name="application/json",
    related_media_type="https://www.iana.org/assignments/media-types/application/json",
    synonyms=["JavaScript Object Notation", "JSON"],
)
ContentType.application_ldplusjson = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_ld+json",
    file_extensions=[".jsonld"],
    name="application/ld+json",
    related_media_type="https://www.iana.org/assignments/media-types/application/ld+json",
    synonyms=["JSON-LD"],
)
ContentType.application_octet_stream = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_octet-stream",
    file_extensions=[".bin"],
    name="application/octet-stream",
    related_media_type="https://www.iana.org/assignments/media-types/application/octet-stream",
    synonyms=["binary format", "BIN"],
)
ContentType.application_pdf = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_pdf",
    file_extensions=[".pdf"],
    name="application/pdf",
    related_media_type="https://www.iana.org/assignments/media-types/application/pdf",
    specification="https://www.pdfa.org/resource/iso-32000-2-pdf-2-0/",
    synonyms=["Adobe Portable Document Format", "PDF"],
)
ContentType.application_sbmlplusxml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_sbml+xml",
    file_extensions=[".sbml"],
    name="application/sbml+xml",
    related_media_type="https://www.iana.org/assignments/media-types/application/sbml+xml",
    synonyms=["System Biology Markup Language"],
)
ContentType.application_schemaplusjson = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_schema+json",
    file_extensions=[".schema.json", ".json", ".jschema", ".jsd", ".jsonsd"],
    name="application/schema+json",
    related_media_type="https://www.iana.org/assignments/media-types/application/schema+json",
    synonyms=["JSON Schema"],
)
ContentType.application_vnd_3i_slidebook = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.3i.slidebook",
    file_extensions=[".sld"],
    name="application/vnd.3i.slidebook",
    synonyms=["SlideBook"],
)
ContentType.application_vnd_abberior_imspector = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.abberior.imspector",
    file_extensions=[".msr", ".obf"],
    name="application/vnd.abberior.imspector",
    specification="https://imspectordocs.readthedocs.io/en/latest/fileformat.html#the-imspector-msr-file-format",
    synonyms=["Imspector OBF"],
)
ContentType.application_vnd_afni = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.afni",
    file_extensions=[".brik", ".head"],
    name="application/vnd.afni",
    synonyms=["AFNI medical imaging data"],
)
ContentType.application_vnd_alicona = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.alicona",
    file_extensions=[".al3d"],
    name="application/vnd.alicona",
)
ContentType.application_vnd_alphaomega_eng = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.alphaomega-eng",
    file_extensions=[".map"],
    name="application/vnd.alphaomega-eng",
    synonyms=["AlphaMap"],
)
ContentType.application_vnd_amiramesh = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.amiramesh",
    file_extensions=[".labels", ".hx", ".grey", ".amiramesh", ".am"],
    name="application/vnd.amiramesh",
)
ContentType.application_vnd_amnis_flowsight = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.amnis-flowsight",
    file_extensions=[".cif"],
    name="application/vnd.amnis-flowsight",
    synonyms=["Amnis FlowSight"],
)
ContentType.application_vnd_analysisservices = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.analysisservices",
    file_extensions=[".abf"],
    name="application/vnd.analysisservices",
    synonyms=["Analysis Services Backup File"],
)
ContentType.application_vnd_analyze_analyze75 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.analyze.analyze75",
    file_extensions=[".img", ".hdr"],
    name="application/vnd.analyze.analyze75",
    synonyms=["Analyze 7.5"],
)
ContentType.application_vnd_analyze_analyzeavw = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.analyze.analyzeavw",
    file_extensions=[".avw"],
    name="application/vnd.analyze.analyzeavw",
    synonyms=["Analyze AVW"],
)
ContentType.application_vnd_andor_andorsif = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.andor.andorsif",
    file_extensions=[".sif"],
    name="application/vnd.andor.andorsif",
    synonyms=["Andor SIF"],
)
ContentType.application_vnd_ansysfluent = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ansysfluent",
    file_extensions=[".dat", ".cas"],
    name="application/vnd.ansysfluent",
    synonyms=["ANSYS Fluent"],
)
ContentType.application_vnd_ant_eeprobe = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ant.eeprobe",
    file_extensions=[".cnt"],
    name="application/vnd.ant.eeprobe",
)
ContentType.application_vnd_antee_probe = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ANTEEProbe",
    file_extensions=[".cnt"],
    name="application/vnd.ANTEEProbe",
)
ContentType.application_vnd_ants_linear_transformplusmat = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ants.linearTransform+mat",
    file_extensions=[".mat"],
    name="application/vnd.ants.linearTransform+mat",
    synonyms=["ANTs Linear Transformation"],
)
ContentType.application_vnd_ants_nonlinear_transformplushdf5 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ants.nonlinearTransform+hdf5",
    file_extensions=[".h5", ".hdf5"],
    name="application/vnd.ants.nonlinearTransform+hdf5",
    synonyms=["ANTs Nonlinear Transformation"],
)
ContentType.application_vnd_anywave = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.anywave",
    file_extensions=[".ades"],
    name="application/vnd.anywave",
    synonyms=["AnyWave Descriptive Format"],
)
ContentType.application_vnd_applied_precision_cellworx = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.applied-precision.cellworx",
    file_extensions=[".pnl", ".htd"],
    name="application/vnd.applied-precision.cellworx",
)
ContentType.application_vnd_arbor_simulatorpluspython = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.arbor-simulator+python",
    file_extensions=[".py"],
    name="application/vnd.arbor-simulator+python",
    synonyms=["Python:Arbor"],
)
ContentType.application_vnd_asciidoc = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.asciidoc",
    file_extensions=[".asciidoc", ".adoc"],
    name="application/vnd.asciidoc",
    synonyms=["AsciiDoc"],
)
ContentType.application_vnd_autodesk_3ds_max_3d_studio_mesh = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.autodesk.3ds-max.3d-studio-mesh",
    file_extensions=[".3ds"],
    name="application/vnd.autodesk.3ds-max.3d-studio-mesh",
)
ContentType.application_vnd_avs_ucd = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.avs.ucd",
    file_extensions=[".inp"],
    name="application/vnd.avs.ucd",
    synonyms=["Unstructured Cell Data"],
)
ContentType.application_vnd_axograph = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.axograph",
    file_extensions=[".axgd", ".axgx"],
    name="application/vnd.axograph",
    synonyms=["AxoGraph"],
)
ContentType.application_vnd_bbp_bluron = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bbp.bluron",
    file_extensions=[".dat"],
    name="application/vnd.bbp.bluron",
)
ContentType.application_vnd_bbp_simulation_blueconfig = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bbp.simulation.blueconfig",
    file_extensions=[".cfg"],
    name="application/vnd.bbp.simulation.blueconfig",
)
ContentType.application_vnd_bci2000 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bci2000",
    file_extensions=[".dat"],
    name="application/vnd.bci2000",
    synonyms=["BCI2000 File Format"],
)
ContentType.application_vnd_bd_biosciences_bdpathway = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bd-biosciences.bdpathway",
    file_extensions=[".tiff", ".exp"],
    name="application/vnd.bd-biosciences.bdpathway",
    synonyms=["BD Pathway"],
)
ContentType.application_vnd_becker_hickl_spcfifo = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.becker-hickl.spcfifo",
    file_extensions=[".spc"],
    name="application/vnd.becker-hickl.spcfifo",
    synonyms=["Becker & Hickl SPC FIFO"],
)
ContentType.application_vnd_becker_hickl_spcimage = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.becker-hickl.spcimage",
    file_extensions=[".sdt"],
    name="application/vnd.becker-hickl.spcimage",
    synonyms=["Becker & Hickl SPCImage"],
)
ContentType.application_vnd_bids = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bids",
    name="application/vnd.bids",
    synonyms=["BIDS"],
)
ContentType.application_vnd_bids_electrodesformat = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bids.electrodesformat",
    file_extensions=[".tsv"],
    name="application/vnd.bids.electrodesformat",
    synonyms=["BIDS electrodes format"],
)
ContentType.application_vnd_bigdataviewer = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bigdataviewer",
    file_extensions=[".xml"],
    name="application/vnd.bigdataviewer",
    synonyms=["Big Data Viewer"],
)
ContentType.application_vnd_bigdataviewerplush5 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bigdataviewer+h5",
    file_extensions=[".h5"],
    name="application/vnd.bigdataviewer+h5",
    synonyms=["Big Data Viewer"],
)
ContentType.application_vnd_bio_rad_gel = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bio-rad.gel",
    file_extensions=[".1sc"],
    name="application/vnd.bio-rad.gel",
    synonyms=["Bio-Rad Gel"],
)
ContentType.application_vnd_bio_rad_pic = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bio-rad.pic",
    file_extensions=[".xml", ".raw", ".pic"],
    name="application/vnd.bio-rad.pic",
    synonyms=["Bio-Rad PIC"],
)
ContentType.application_vnd_bio_rad_scn = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bio-rad.scn",
    file_extensions=[".scn"],
    name="application/vnd.bio-rad.scn",
    synonyms=["Bio-Rad SCN"],
)
ContentType.application_vnd_bionetgen = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bionetgen",
    file_extensions=[".ebngl", ".bngl"],
    name="application/vnd.bionetgen",
    synonyms=["BioNetGen Language"],
)
ContentType.application_vnd_blackrockmicrosystems_neuralevents = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blackrockmicrosystems.neuralevents",
    file_extensions=[".nev"],
    name="application/vnd.blackrockmicrosystems.neuralevents",
    specification="https://blackrockneurotech.com/research/wp-content/ifu/LB-0023-7.00_NEV_File_Format.pdf",
    synonyms=["Blackrock Neural Events"],
)
ContentType.application_vnd_blackrockmicrosystems_neuralsignals_1 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blackrockmicrosystems.neuralsignals.1",
    file_extensions=[".ns1"],
    name="application/vnd.blackrockmicrosystems.neuralsignals.1",
    specification="https://blackrockneurotech.com/research/wp-content/ifu/LB-0023-7.00_NEV_File_Format.pdf",
    synonyms=["Blackrock Neural Signals 1"],
)
ContentType.application_vnd_blackrockmicrosystems_neuralsignals_2 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blackrockmicrosystems.neuralsignals.2",
    file_extensions=[".ns2"],
    name="application/vnd.blackrockmicrosystems.neuralsignals.2",
    specification="https://blackrockneurotech.com/research/wp-content/ifu/LB-0023-7.00_NEV_File_Format.pdf",
    synonyms=["Blackrock Neural Signals 2"],
)
ContentType.application_vnd_blackrockmicrosystems_neuralsignals_3 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blackrockmicrosystems.neuralsignals.3",
    file_extensions=[".ns3"],
    name="application/vnd.blackrockmicrosystems.neuralsignals.3",
    specification="https://blackrockneurotech.com/research/wp-content/ifu/LB-0023-7.00_NEV_File_Format.pdf",
    synonyms=["Blackrock Neural Signals 3"],
)
ContentType.application_vnd_blackrockmicrosystems_neuralsignals_4 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blackrockmicrosystems.neuralsignals.4",
    file_extensions=[".ns4"],
    name="application/vnd.blackrockmicrosystems.neuralsignals.4",
    specification="https://blackrockneurotech.com/research/wp-content/ifu/LB-0023-7.00_NEV_File_Format.pdf",
    synonyms=["Blackrock Neural Signals 4"],
)
ContentType.application_vnd_blackrockmicrosystems_neuralsignals_5 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blackrockmicrosystems.neuralsignals.5",
    file_extensions=[".ns5"],
    name="application/vnd.blackrockmicrosystems.neuralsignals.5",
    specification="https://blackrockneurotech.com/research/wp-content/ifu/LB-0023-7.00_NEV_File_Format.pdf",
    synonyms=["Blackrock Neural Signals 5"],
)
ContentType.application_vnd_blackrockmicrosystems_neuralsignals_6 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blackrockmicrosystems.neuralsignals.6",
    file_extensions=[".ns6"],
    name="application/vnd.blackrockmicrosystems.neuralsignals.6",
    specification="https://blackrockneurotech.com/research/wp-content/ifu/LB-0023-7.00_NEV_File_Format.pdf",
    synonyms=["Blackrock Neural Signals 6"],
)
ContentType.application_vnd_blackrockmicrosystems_neuralsignals_7 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blackrockmicrosystems.neuralsignals.7",
    file_extensions=[".ns7"],
    name="application/vnd.blackrockmicrosystems.neuralsignals.7",
    specification="https://blackrockneurotech.com/research/wp-content/ifu/LB-0023-7.00_NEV_File_Format.pdf",
    synonyms=["Blackrock Neural Signals 7"],
)
ContentType.application_vnd_blackrockmicrosystems_neuralsignals_8 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blackrockmicrosystems.neuralsignals.8",
    file_extensions=[".ns8"],
    name="application/vnd.blackrockmicrosystems.neuralsignals.8",
    specification="https://blackrockneurotech.com/research/wp-content/ifu/LB-0023-7.00_NEV_File_Format.pdf",
    synonyms=["Blackrock Neural Signals 8"],
)
ContentType.application_vnd_blackrockmicrosystems_neuralsignals_9 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blackrockmicrosystems.neuralsignals.9",
    file_extensions=[".ns9"],
    name="application/vnd.blackrockmicrosystems.neuralsignals.9",
    specification="https://blackrockneurotech.com/research/wp-content/ifu/LB-0023-7.00_NEV_File_Format.pdf",
    synonyms=["Blackrock Neural Signals 9"],
)
ContentType.application_vnd_blackrockmicrosystems_parallelrecordings = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blackrockmicrosystems.parallelrecordings",
    file_extensions=[".ns1", ".ns2", ".ns3", ".ns4", ".ns5", ".ns6", ".ns7", ".ns8", ".ns9", ".nev"],
    name="application/vnd.blackrockmicrosystems.parallelrecordings",
    synonyms=["Blackrock Parallel Recordings"],
)
ContentType.application_vnd_blk = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.blk",
    file_extensions=[".blk"],
    name="application/vnd.blk",
    synonyms=["BLK File"],
)
ContentType.application_vnd_bluebrainproject_bluepyopt = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bluebrainproject.bluepyopt",
    file_extensions=[".zip"],
    name="application/vnd.bluebrainproject.bluepyopt",
    synonyms=["BluePyOpt"],
)
ContentType.application_vnd_brain_innovation_brainvoyager = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.brain-innovation.brainvoyager",
    file_extensions=[".v16", ".vmr"],
    name="application/vnd.brain-innovation.brainvoyager",
)
ContentType.application_vnd_brainnetviewer = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.brainnetviewer",
    file_extensions=[".nv"],
    name="application/vnd.brainnetviewer",
)
ContentType.application_vnd_brainproducts = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.brainproducts",
    file_extensions=[".vhdr"],
    name="application/vnd.brainproducts",
)
ContentType.application_vnd_brains2 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.brains2",
    file_extensions=[".mask"],
    name="application/vnd.brains2",
)
ContentType.application_vnd_brainvision_binary = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.brainvision.binary",
    file_extensions=[".eeg"],
    name="application/vnd.brainvision.binary",
    synonyms=["BrainVision Data Exchange Binary Data File", "BrainVision Binary Data"],
)
ContentType.application_vnd_brainvision_header = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.brainvision.header",
    file_extensions=[".vhdr"],
    name="application/vnd.brainvision.header",
    synonyms=["BrainVision Data Exchange Header File", "BrainVision Header"],
)
ContentType.application_vnd_brainvision_marker = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.brainvision.marker",
    file_extensions=[".vmrk"],
    name="application/vnd.brainvision.marker",
    synonyms=["BrainVision Data Exchange Marker File", "BrainVision Marker"],
)
ContentType.application_vnd_bsc = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bsc",
    file_extensions=[".row"],
    name="application/vnd.bsc",
)
ContentType.application_vnd_bsc_paraver_configurationfile = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.bsc.paraver.configurationfile",
    file_extensions=[".txt"],
    name="application/vnd.bsc.paraver.configurationfile",
    synonyms=["Paraver Configuration File"],
)
ContentType.application_vnd_burleigh_instruments_burleigh = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.burleigh-instruments.burleigh",
    file_extensions=[".img"],
    name="application/vnd.burleigh-instruments.burleigh",
)
ContentType.application_vnd_byu = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.byu",
    file_extensions=[".g", ".byu"],
    name="application/vnd.byu",
    synonyms=["BYU"],
)
ContentType.application_vnd_canon_canondng = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.canon.canondng",
    file_extensions=[".crw", ".c2r"],
    name="application/vnd.canon.canondng",
)
ContentType.application_vnd_cell_sens_vsi = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.cell-sens-vsi",
    file_extensions=[".vsi"],
    name="application/vnd.cell-sens-vsi",
)
ContentType.application_vnd_cellh5plushdf5 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.cellh5+hdf5",
    file_extensions=[".ch5"],
    name="application/vnd.cellh5+hdf5",
)
ContentType.application_vnd_commonworkflowlanguage_cmdline = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.commonworkflowlanguage.cmdline",
    file_extensions=[".cwl"],
    name="application/vnd.commonworkflowlanguage.cmdline",
    synonyms=["CWL command line tool", "CWL command-line wrapper description"],
)
ContentType.application_vnd_commonworkflowlanguage_workflow = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.commonworkflowlanguage.workflow",
    file_extensions=[".cwl"],
    name="application/vnd.commonworkflowlanguage.workflow",
    synonyms=["CWL workflow description"],
)
ContentType.application_vnd_connectomics_lab_connectome = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.connectomics-lab.connectome",
    file_extensions=[".cff"],
    name="application/vnd.connectomics-lab.connectome",
)
ContentType.application_vnd_ctf = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ctf",
    file_extensions=[".ds"],
    name="application/vnd.ctf",
)
ContentType.application_vnd_cytiva_deltavision = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.cytiva.deltavision",
    file_extensions=[".rcpnl", ".r3d", ".dv"],
    name="application/vnd.cytiva.deltavision",
)
ContentType.application_vnd_ebrains_image_service_deepzoom = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ebrains.image-service.deepzoom",
    description="This content type defines a file repository produced by the EBRAINS image-service holding a collection of files that is conform with the Microsoft Deep Zoom specifications.",
    name="application/vnd.ebrains.image-service.deepzoom",
    synonyms=["EBRAINS image-service with Deep Zoom specifications", "EBRAINS image-service Deep Zoom specs"],
)
ContentType.application_vnd_ebrains_image_service_neuroglancer_precomputed = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ebrains.image-service.neuroglancer.precomputed",
    description="This content type defines a file repository produced by the EBRAINS image-service holding a collection of files that is conform with the Neuroglancer precomputed specifications.",
    name="application/vnd.ebrains.image-service.neuroglancer.precomputed",
    synonyms=[
        "EBRAINS image-service with Neuroglancer precomputed specifications",
        "EBRAINS image-service Neuroglancer precomputed specs",
    ],
)
ContentType.application_vnd_edf = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.edf",
    file_extensions=[".edf"],
    name="application/vnd.edf",
    synonyms=["European Data Format"],
)
ContentType.application_vnd_edfplus = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.edf+",
    file_extensions=[".edf"],
    name="application/vnd.edf+",
)
ContentType.application_vnd_eeglab = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.eeglab",
    file_extensions=[".sat"],
    name="application/vnd.eeglab",
)
ContentType.application_vnd_egi = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.egi",
    file_extensions=[".mff"],
    name="application/vnd.egi",
)
ContentType.application_vnd_egi_mff = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.egi.mff",
    file_extensions=[".xml"],
    name="application/vnd.egi.mff",
)
ContentType.application_vnd_elan_continuous_data = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.elan.continuous-data",
    file_extensions=[".eeg", ".eeg.ent"],
    name="application/vnd.elan.continuous-data",
    synonyms=["ELAN continuous data file"],
)
ContentType.application_vnd_elan_event = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.elan.event",
    file_extensions=[".pos"],
    name="application/vnd.elan.event",
    synonyms=["ELAN event file"],
)
ContentType.application_vnd_elekta = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.elekta",
    file_extensions=[".fif"],
    name="application/vnd.elekta",
    synonyms=["FIFF"],
)
ContentType.application_vnd_elphy = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.elphy",
    file_extensions=[".dat"],
    name="application/vnd.elphy",
    synonyms=["Data Files"],
)
ContentType.application_vnd_enhancedswc = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.enhancedswc",
    file_extensions=[".eswc"],
    name="application/vnd.enhancedswc",
    synonyms=["Enhanced SWC"],
)
ContentType.application_vnd_ensight = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ensight",
    file_extensions=[".sos", ".case"],
    name="application/vnd.ensight",
    synonyms=["Engineering inSight"],
)
ContentType.application_vnd_enzo_amrplushdf5 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.enzo.amr+hdf5",
    file_extensions=[".hdf5"],
    name="application/vnd.enzo.amr+hdf5",
)
ContentType.application_vnd_espina_segpluszip = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.espina.seg+zip",
    file_extensions=[".seg"],
    name="application/vnd.espina.seg+zip",
)
ContentType.application_vnd_exodus_ii = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.exodusII",
    file_extensions=[".gen", ".g", ".exoii", ".exo", ".exii", ".ex2v2", ".ex2", ".e", ".0000", ".000", ".00", ".0"],
    name="application/vnd.exodusII",
)
ContentType.application_vnd_faconstructor_3d_pli = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.faconstructor.3d-pli",
    file_extensions=[".txt"],
    name="application/vnd.faconstructor.3d-pli",
)
ContentType.application_vnd_faconstructor_3d_pliplushdf5 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.faconstructor.3d-pli+hdf5",
    file_extensions=[".hdf5"],
    name="application/vnd.faconstructor.3d-pli+hdf5",
)
ContentType.application_vnd_fei = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.fei",
    file_extensions=[".img"],
    name="application/vnd.fei",
)
ContentType.application_vnd_fmri_cifti_2 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.fmri.cifti.2",
    file_extensions=[".nii.gz", ".dtseries.nii"],
    name="application/vnd.fmri.cifti.2",
)
ContentType.application_vnd_freesurfer = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.freesurfer",
    file_extensions=[".white", ".sphere", ".smoothwm", ".pial", ".orig", ".inflated", ".mgz", ".mgh"],
    name="application/vnd.freesurfer",
)
ContentType.application_vnd_freesurfer_annotation = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.freesurfer.annotation",
    file_extensions=[".annot"],
    name="application/vnd.freesurfer.annotation",
    specification="https://surfer.nmr.mgh.harvard.edu/fswiki/LabelsClutsAnnotationFiles#Annotation",
    synonyms=["FreeSurfer Annotation File"],
)
ContentType.application_vnd_g_node_nix_neo = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.g-node.nix.neo",
    file_extensions=[".nix", ".h5"],
    name="application/vnd.g-node.nix.neo",
    synonyms=["NIX:Neo"],
)
ContentType.application_vnd_g_node_nixplushdf5 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.g-node.nix+hdf5",
    file_extensions=[".hdf5"],
    name="application/vnd.g-node.nix+hdf5",
    synonyms=["Neuroscience information exchange format"],
)
ContentType.application_vnd_g_node_odml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.g-node.odml",
    file_extensions=[".odml"],
    name="application/vnd.g-node.odml",
    specification="https://g-node.github.io/python-odml/",
    synonyms=["odML", "open metadata Markup Language"],
)
ContentType.application_vnd_gatan_digitalmicrograph2 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.gatan.digitalmicrograph2",
    name="application/vnd.gatan.digitalmicrograph2",
    synonyms=["Gatan Digital Micrograph 2"],
)
ContentType.application_vnd_ge_healthcare_incell_1000_2000 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ge-healthcare.incell.1000-2000",
    file_extensions=[".tiff", ".xdce"],
    name="application/vnd.ge-healthcare.incell.1000-2000",
    synonyms=["InCell 1000/2000"],
)
ContentType.application_vnd_ge_healthcare_incell_3000 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ge-healthcare.incell.3000",
    file_extensions=[".frm"],
    name="application/vnd.ge-healthcare.incell.3000",
    synonyms=["InCell 3000"],
)
ContentType.application_vnd_ge_healthcare_life_sciences_amersham_biosciences_gel = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ge-healthcare-life-sciences.amersham-biosciences-gel",
    file_extensions=[".gel"],
    name="application/vnd.ge-healthcare-life-sciences.amersham-biosciences-gel",
    synonyms="GEL",
)
ContentType.application_vnd_ge_healthcare_microct = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ge-healthcare.microct",
    file_extensions=[".vff"],
    name="application/vnd.ge-healthcare.microct",
    synonyms=["GE MicroCT"],
)
ContentType.application_vnd_geomview_oogl = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.geomview.oogl",
    file_extensions=[".off"],
    name="application/vnd.geomview.oogl",
    synonyms=["Object Oriented Graphics Library"],
)
ContentType.application_vnd_gifti = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.gifti",
    file_extensions=[".gii"],
    name="application/vnd.gifti",
)
ContentType.application_vnd_hamamatsu_aquacosmos = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.hamamatsu.aquacosmos",
    file_extensions=[".naf"],
    name="application/vnd.hamamatsu.aquacosmos",
    synonyms=["Hamamatsu Aquacosmos NAF"],
)
ContentType.application_vnd_hamamatsu_his = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.hamamatsu.his",
    file_extensions=[".his"],
    name="application/vnd.hamamatsu.his",
    synonyms=["Hamamatsu HIS"],
)
ContentType.application_vnd_hamamatsu_ndpi = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.hamamatsu.ndpi",
    file_extensions=[".ndpis", ".ndpi"],
    name="application/vnd.hamamatsu.ndpi",
    synonyms=["Hamamatsu ndpi"],
)
ContentType.application_vnd_hamamatsu_vms = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.hamamatsu.vms",
    file_extensions=[".vms"],
    name="application/vnd.hamamatsu.vms",
    synonyms=["Hamamatsu VMS"],
)
ContentType.application_vnd_hitachi_s_4800 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.hitachi.s-4800",
    file_extensions=[".jpg", ".bmp", ".tif", ".txt"],
    name="application/vnd.hitachi.s-4800",
    synonyms=["Hitachi S-4800"],
)
ContentType.application_vnd_hyland_brainwaredam = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.hyland.brainwaredam",
    file_extensions=[".dam"],
    name="application/vnd.hyland.brainwaredam",
    synonyms=["Brainware DAM files"],
)
ContentType.application_vnd_hyland_brainwaref32 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.hyland.brainwaref32",
    file_extensions=[".f32"],
    name="application/vnd.hyland.brainwaref32",
    synonyms=["Brainware F32 files"],
)
ContentType.application_vnd_hyland_brainwaresrc = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.hyland.brainwaresrc",
    file_extensions=[".src"],
    name="application/vnd.hyland.brainwaresrc",
    synonyms=["Brainware SRC files"],
)
ContentType.application_vnd_ics = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ics",
    file_extensions=[".ids", ".ics"],
    name="application/vnd.ics",
    synonyms=["Image Cytometry Standard"],
)
ContentType.application_vnd_igorpro = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.igorpro",
    file_extensions=[".ibw", ".pxp"],
    name="application/vnd.igorpro",
    synonyms=["Igor Binary Waves, Packed Experiment files"],
)
ContentType.application_vnd_imacon = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.imacon",
    file_extensions=[".fff"],
    name="application/vnd.imacon",
    synonyms=["Imacon"],
)
ContentType.application_vnd_imagepro_sequence = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.imagepro.sequence",
    file_extensions=[".seq"],
    name="application/vnd.imagepro.sequence",
    synonyms=["ImagePro Sequence"],
)
ContentType.application_vnd_imagepro_workspace = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.imagepro.workspace",
    file_extensions=[".ipw"],
    name="application/vnd.imagepro.workspace",
    synonyms=["ImagePro Workspace"],
)
ContentType.application_vnd_imagic = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.imagic",
    file_extensions=[".img", ".hed"],
    name="application/vnd.imagic",
)
ContentType.application_vnd_imod = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.imod",
    file_extensions=[".mod"],
    name="application/vnd.imod",
    synonyms=["IMOD"],
)
ContentType.application_vnd_improvision_openlab = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.improvision.openlab",
    file_extensions=[".raw", ".liff"],
    name="application/vnd.improvision.openlab",
    synonyms=["Improvision Openlab"],
)
ContentType.application_vnd_indec_biosystems_axonrawformat = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.indec-biosystems.axonrawformat",
    file_extensions=[".arf"],
    name="application/vnd.indec-biosystems.axonrawformat",
    synonyms=["Axon Raw Format"],
)
ContentType.application_vnd_intan_technology = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.intan.technology",
    file_extensions=[".rhd", ".rhs"],
    name="application/vnd.intan.technology",
    synonyms=["Intan tech rhd and rhs files", "RHD RHS"],
)
ContentType.application_vnd_intranatpluscsv = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.intranat+csv",
    file_extensions=[".csv"],
    name="application/vnd.intranat+csv",
    synonyms=["IntrAnat CSV"],
)
ContentType.application_vnd_intranatplustxt = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.intranat+txt",
    file_extensions=[".pts", ".txt"],
    name="application/vnd.intranat+txt",
    synonyms=["IntrAnat PTS"],
)
ContentType.application_vnd_inveon = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.inveon",
    file_extensions=[".hdr"],
    name="application/vnd.inveon",
    synonyms=["Inveon"],
)
ContentType.application_vnd_iplab = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.iplab",
    file_extensions=[".ipl"],
    name="application/vnd.iplab",
    synonyms=["IPLab"],
)
ContentType.application_vnd_itk = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.itk",
    file_extensions=[".mhd", ".mha"],
    name="application/vnd.itk",
)
ContentType.application_vnd_ivision = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ivision",
    file_extensions=[".ipm"],
    name="application/vnd.ivision",
    synonyms=["IVision"],
)
ContentType.application_vnd_jeol = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.jeol",
    file_extensions=[".par", ".img", ".dat"],
    name="application/vnd.jeol",
    synonyms=["JEOL"],
)
ContentType.application_vnd_keller_lab_block = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.keller-lab.block",
    file_extensions=[".klb"],
    name="application/vnd.keller-lab.block",
    synonyms=["Keller Lab Block"],
)
ContentType.application_vnd_khoros_viff_bitmap = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.khoros.viff.bitmap",
    file_extensions=[".xv"],
    name="application/vnd.khoros.viff.bitmap",
    synonyms=["Khoros Visualization Image File Format Bitmap"],
)
ContentType.application_vnd_kitware_paraview_pvt = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.kitware.paraview.pvt",
    file_extensions=[".pvtu", ".pvts", ".pvtr", ".pvtp", ".ptvi", ".pvtb"],
    name="application/vnd.kitware.paraview.pvt",
)
ContentType.application_vnd_klustakwik = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.klustakwik",
    name="application/vnd.klustakwik",
    synonyms=["KlustaKwik Format"],
)
ContentType.application_vnd_kodak_bip = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.kodak.bip",
    file_extensions=[".bip"],
    name="application/vnd.kodak.bip",
    synonyms=["Kodak BIP"],
)
ContentType.application_vnd_kwik = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.kwik",
    file_extensions=[".kwik"],
    name="application/vnd.kwik",
    synonyms=["Kwik Format"],
)
ContentType.application_vnd_laboratory_imaging_nikon = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.laboratory-imaging.nikon",
    file_extensions=[".lim"],
    name="application/vnd.laboratory-imaging.nikon",
    synonyms=["LIM (Laboratory Imaging/Nikon)"],
)
ContentType.application_vnd_lambert_instruments_flim = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.lambert-instruments.flim",
    file_extensions=[".fli"],
    name="application/vnd.lambert-instruments.flim",
    synonyms=["Lambert Instruments FLIM"],
)
ContentType.application_vnd_lavision_imspector = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.lavision.imspector",
    file_extensions=[".msr"],
    name="application/vnd.lavision.imspector",
    synonyms=["LaVision Imspector"],
)
ContentType.application_vnd_leica_biosystems_aperio = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.leica-biosystems.aperio",
    file_extensions=[".svs", ".afi"],
    name="application/vnd.leica-biosystems.aperio",
)
ContentType.application_vnd_leica_biosystems_aperiosvstiff = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.leica-biosystems.aperiosvstiff",
    file_extensions=[".tiff", ".svs"],
    name="application/vnd.leica-biosystems.aperiosvstiff",
)
ContentType.application_vnd_leica_las_af_lif = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.leica.las.af.lif",
    file_extensions=[".lif"],
    name="application/vnd.leica.las.af.lif",
    synonyms=["Leica LAS AF LIF (Leica Image File Format)"],
)
ContentType.application_vnd_leica_lcs_lei = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.leica.lcs.lei",
    file_extensions=[".tiff", ".lei"],
    name="application/vnd.leica.lcs.lei",
    synonyms=["Leica LCS LEI"],
)
ContentType.application_vnd_leica_scn = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.leica.scn",
    file_extensions=[".scn"],
    name="application/vnd.leica.scn",
    synonyms=["Leica SCN"],
)
ContentType.application_vnd_li_cor_l2d = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.li-cor.l2d",
    file_extensions=[".scn", ".tiff", ".l2d"],
    name="application/vnd.li-cor.l2d",
    synonyms=["Li-Cor L2D"],
)
ContentType.application_vnd_libreoffice = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.libreoffice",
    file_extensions=[".ods"],
    name="application/vnd.libreoffice",
    synonyms=["Open Document Spreadsheet"],
)
ContentType.application_vnd_ls_dyna = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ls-dyna",
    file_extensions=[".d3plot"],
    name="application/vnd.ls-dyna",
    synonyms=["LS-DYNA D3PLOT"],
)
ContentType.application_vnd_mathworks_live_scriptpluszip = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.mathworks.live-script+zip",
    file_extensions=[".mlx"],
    name="application/vnd.mathworks.live-script+zip",
    specification="https://de.mathworks.com/help/matlab/matlab_prog/live-script-file-format.html",
    synonyms=["MATLAB MLX", "MATLAB Live", "MATLAB Live Script", "MATLAB Live-Script"],
)
ContentType.application_vnd_mbf_neurolucida = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.mbf.neurolucida",
    file_extensions=[".nrx", ".dat", ".asc"],
    name="application/vnd.mbf.neurolucida",
)
ContentType.application_vnd_mcid = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.mcid",
    file_extensions=[".im"],
    name="application/vnd.mcid",
    synonyms=["MCID"],
)
ContentType.application_vnd_mearec = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.mearec",
    file_extensions=[".h5"],
    name="application/vnd.mearec",
    synonyms=["Multi-Electrode-Arrays", "MEA"],
)
ContentType.application_vnd_metamorph_stack = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.metamorph.stack",
    file_extensions=[".nd", ".stk"],
    name="application/vnd.metamorph.stack",
    synonyms=["MetaMorph Stack"],
)
ContentType.application_vnd_metaxpress = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.metaxpress",
    file_extensions=[".tiff", ".htd"],
    name="application/vnd.metaxpress",
    synonyms=["MetaXpress"],
)
ContentType.application_vnd_micro_manager = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.micro-manager",
    file_extensions=[".xml", ".txt", ".tiff"],
    name="application/vnd.micro-manager",
    synonyms=["Micro-Manager"],
)
ContentType.application_vnd_micromed = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.micromed",
    file_extensions=[".trc"],
    name="application/vnd.micromed",
)
ContentType.application_vnd_micromedgroup = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.micromedgroup",
    file_extensions=[".trc"],
    name="application/vnd.micromedgroup",
    synonyms=["Micromed files"],
)
ContentType.application_vnd_microsoft_deepzoom_collectionplusxml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.microsoft.deepzoom.collection+xml",
    file_extensions=[".dzc", ".xml"],
    name="application/vnd.microsoft.deepzoom.collection+xml",
    specification="https://docs.microsoft.com/en-us/previous-versions/windows/silverlight/dotnet-windows-silverlight/cc645077(v=vs.95)",
    synonyms=["Deep Zoom Collection", "DZC"],
)
ContentType.application_vnd_microsoft_deepzoom_imageplusxml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.microsoft.deepzoom.image+xml",
    file_extensions=[".dzi", ".xml"],
    name="application/vnd.microsoft.deepzoom.image+xml",
    specification="https://docs.microsoft.com/en-us/previous-versions/windows/silverlight/dotnet-windows-silverlight/cc645077(v=vs.95)",
    synonyms=["Deep Zoom Image", "DZI"],
)
ContentType.application_vnd_minc = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.minc",
    file_extensions=[".mnc"],
    name="application/vnd.minc",
    synonyms=["MINC MRI"],
)
ContentType.application_vnd_mindsplusjson = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.minds+json",
    file_extensions=[".json"],
    name="application/vnd.minds+json",
)
ContentType.application_vnd_minolta = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.minolta",
    file_extensions=[".mrw"],
    name="application/vnd.minolta",
    synonyms=["Minolta MRW"],
)
ContentType.application_vnd_mitk_fiber = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.mitk.fiber",
    file_extensions=[".fib"],
    name="application/vnd.mitk.fiber",
    synonyms=["Fiber bundle"],
)
ContentType.application_vnd_molecular_imaging = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.molecular-imaging",
    file_extensions=[".stp"],
    name="application/vnd.molecular-imaging",
    synonyms=["Molecular Imaging"],
)
ContentType.application_vnd_moleculardevices_axon = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.moleculardevices.axon",
    file_extensions=[".abf"],
    name="application/vnd.moleculardevices.axon",
    synonyms=["Axon™ Binary File format"],
)
ContentType.application_vnd_mrc = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.mrc",
    file_extensions=[".mrcs", ".rec", ".map", ".ali", ".st", ".mrc"],
    name="application/vnd.mrc",
    synonyms=["MRC (Medical Research Council)"],
)
ContentType.application_vnd_mrtrix_imageformat = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.mrtrix.imageformat",
    file_extensions=[".mih", ".mif.gz", ".mif"],
    name="application/vnd.mrtrix.imageformat",
    synonyms=["MRTrix Image Format"],
)
ContentType.application_vnd_mrtrix_legacysparseformat = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.mrtrix.legacysparseformat",
    file_extensions=[".msf", ".msh"],
    name="application/vnd.mrtrix.legacysparseformat",
    synonyms=["Legacy MRtrix Sparse Format"],
)
ContentType.application_vnd_ms_excel = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ms-excel",
    file_extensions=[".xls"],
    name="application/vnd.ms-excel",
    related_media_type="https://www.iana.org/assignments/media-types/application/vnd.ms-excel",
    synonyms=["Microsoft Excel", "XLS"],
)
ContentType.application_vnd_neo_ascii_image = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neo.ascii.image",
    file_extensions=[".txt"],
    name="application/vnd.neo.ascii.image",
    synonyms=["Ascii Image"],
)
ContentType.application_vnd_neo_ascii_signal = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neo.ascii.signal",
    file_extensions=[".tsv", ".csv", ".asc", ".txt"],
    name="application/vnd.neo.ascii.signal",
    synonyms=["NEO AnalogSignals"],
)
ContentType.application_vnd_neo_ascii_spiketrain = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neo.ascii.spiketrain",
    file_extensions=[".txt"],
    name="application/vnd.neo.ascii.spiketrain",
    synonyms=["NEO SpikeTrains"],
)
ContentType.application_vnd_nest = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nest",
    file_extensions=[".gdf", ".dat"],
    name="application/vnd.nest",
)
ContentType.application_vnd_nest_simulatorpluspython = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nest-simulator+python",
    file_extensions=[".py"],
    name="application/vnd.nest-simulator+python",
    synonyms=["Python:NEST"],
)
ContentType.application_vnd_netpbm_portableanymap = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.netpbm.portableanymap",
    file_extensions=[".ppm", ".pgm", ".pbm"],
    name="application/vnd.netpbm.portableanymap",
    synonyms=["Portable Anymap"],
)
ContentType.application_vnd_neuralensemble = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuralensemble",
    file_extensions=[".neo"],
    name="application/vnd.neuralensemble",
)
ContentType.application_vnd_neuralensemble_pynn = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuralensemble.pynn",
    file_extensions=[".py"],
    name="application/vnd.neuralensemble.pynn",
    synonyms=["Python:PyNN"],
)
ContentType.application_vnd_neuralynx = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuralynx",
    file_extensions=[".ncs", ".nev", ".nse", ".ntt"],
    name="application/vnd.neuralynx",
    synonyms=["Neuralynx files"],
)
ContentType.application_vnd_neuroglancer_precomputed = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuroglancer.precomputed",
    name="application/vnd.neuroglancer.precomputed",
    specification="https://github.com/google/neuroglancer/blob/33d5206cf16c60530e9d0d517dc8bb9b968e2e18/src/neuroglancer/datasource/precomputed/README.md",
    synonyms=["Neuroglancer precomputed"],
)
ContentType.application_vnd_neuroglancer_precomputed_infoplusjson = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuroglancer.precomputed.info+json",
    name="application/vnd.neuroglancer.precomputed.info+json",
    specification="https://github.com/google/neuroglancer/blob/33d5206cf16c60530e9d0d517dc8bb9b968e2e18/src/neuroglancer/datasource/precomputed/README.md",
    synonyms=["Neuroglancer precomputed info", "Neuroglancer precomputed metadata"],
)
ContentType.application_vnd_neuroglancer_precomputed_raw = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuroglancer.precomputed.raw",
    name="application/vnd.neuroglancer.precomputed.raw",
    specification="https://github.com/google/neuroglancer/blob/33d5206cf16c60530e9d0d517dc8bb9b968e2e18/src/neuroglancer/datasource/precomputed/README.md",
    synonyms=["Neuroglancer precomputed raw"],
)
ContentType.application_vnd_neuroml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuroml",
    file_extensions=[".xml"],
    name="application/vnd.neuroml",
    synonyms=["NeuroML"],
)
ContentType.application_vnd_neuron_mod = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuron.mod",
    file_extensions=[".mod"],
    name="application/vnd.neuron.mod",
)
ContentType.application_vnd_neuron_simulatorplushoc = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuron-simulator+hoc",
    file_extensions=[".hoc"],
    name="application/vnd.neuron-simulator+hoc",
    synonyms=["Hoc:NEURON"],
)
ContentType.application_vnd_neuron_simulatorpluspython = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuron-simulator+python",
    file_extensions=[".py"],
    name="application/vnd.neuron-simulator+python",
    synonyms=["Python:NEURON"],
)
ContentType.application_vnd_neuroscope = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuroscope",
    name="application/vnd.neuroscope",
    synonyms=["NeuroScope format files"],
)
ContentType.application_vnd_neuroshareapi = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.neuroshareapi",
    name="application/vnd.neuroshareapi",
    synonyms=["Neuroshare compatible files"],
)
ContentType.application_vnd_nexstim_nbs_system_data = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nexstim.nbs-system.data",
    file_extensions=[".nxe"],
    name="application/vnd.nexstim.nbs-system.data",
)
ContentType.application_vnd_nfsim = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nfsim",
    file_extensions=[".rnf"],
    name="application/vnd.nfsim",
    synonyms=["Run NF"],
)
ContentType.application_vnd_nifti_1 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nifti.1",
    file_extensions=[".hdr", ".img", ".nii.gz", ".nii"],
    name="application/vnd.nifti.1",
    synonyms=["NIfTI"],
)
ContentType.application_vnd_nifti_2 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nifti.2",
    file_extensions=[".nii", ".hdr", ".img", ".nii.gz"],
    name="application/vnd.nifti.2",
    synonyms=["NIfTI-2"],
)
ContentType.application_vnd_nikon = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nikon",
    file_extensions=[".ids", ".ics"],
    name="application/vnd.nikon",
)
ContentType.application_vnd_nikon_nef = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nikon.nef",
    file_extensions=[".tiff", ".nef"],
    name="application/vnd.nikon.nef",
    synonyms=["Nikon Electronic Format"],
)
ContentType.application_vnd_nikon_nis_elements = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nikon.nis-elements",
    file_extensions=[".nd2"],
    name="application/vnd.nikon.nis-elements",
    synonyms=["Nikon NIS-Elements"],
)
ContentType.application_vnd_nineml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nineml",
    file_extensions=[".xml"],
    name="application/vnd.nineml",
    synonyms=["NineML"],
)
ContentType.application_vnd_nrrd = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nrrd",
    file_extensions=[".txt", ".raw", ".nhdr", ".nrrd"],
    name="application/vnd.nrrd",
    synonyms=["Nearly Raw Raster Data"],
)
ContentType.application_vnd_nsdf = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nsdf",
    file_extensions=[".nsdf"],
    name="application/vnd.nsdf",
    synonyms=["NSDF files"],
)
ContentType.application_vnd_nutil_parameters = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nutil.parameters",
    file_extensions=[".nut"],
    name="application/vnd.nutil.parameters",
    synonyms=["Nutil Analysis Parameters"],
)
ContentType.application_vnd_nutil_quantifierplusjson = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nutil.quantifier+json",
    file_extensions=[".json"],
    name="application/vnd.nutil.quantifier+json",
    related_media_type="https://www.iana.org/assignments/media-types/application/json",
    synonyms=["Nutil Quantifier JavaScript Object Notation", "Nutil Quantifier JSON"],
)
ContentType.application_vnd_nutil_resultspluscsv = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nutil.results+csv",
    file_extensions=[".csv"],
    name="application/vnd.nutil.results+csv",
    synonyms=["Nutil Results CSV"],
)
ContentType.application_vnd_nwb_nwbnplushdf = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.nwb.nwbn+hdf",
    file_extensions=[".nwb", ".h5"],
    name="application/vnd.nwb.nwbn+hdf",
    synonyms=["NWB:N"],
)
ContentType.application_vnd_olympus = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.olympus",
    file_extensions=[".oib"],
    name="application/vnd.olympus",
    synonyms=["Olympus Image Binary"],
)
ContentType.application_vnd_olympus_cellr_apl = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.olympus.cellr-apl",
    file_extensions=[".obsep", ".tiff", ".tnb", ".mtb", ".apl"],
    name="application/vnd.olympus.cellr-apl",
    synonyms=["Olympus CellR/APL"],
)
ContentType.application_vnd_olympus_fluoview_fv1000 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.olympus.fluoview.fv1000",
    file_extensions=[".oif", ".oib"],
    name="application/vnd.olympus.fluoview.fv1000",
    synonyms=["Olympus FluoView FV1000"],
)
ContentType.application_vnd_olympus_scanr = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.olympus.scanr",
    file_extensions=[".tiff", ".dat", ".xml"],
    name="application/vnd.olympus.scanr",
    synonyms=["Olympus ScanR"],
)
ContentType.application_vnd_ome_tiff = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ome.tiff",
    file_extensions=[".ome.btf", ".ome.tf8", ".ome.tf2", ".ome.tiff"],
    name="application/vnd.ome.tiff",
    synonyms=["OME-TIFF"],
)
ContentType.application_vnd_ome_xml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ome.xml",
    file_extensions=[".ome.xml", ".ome"],
    name="application/vnd.ome.xml",
    synonyms=["OME-XML"],
)
ContentType.application_vnd_opendx = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.opendx",
    file_extensions=[".dx"],
    name="application/vnd.opendx",
)
ContentType.application_vnd_openephys = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.openephys",
    name="application/vnd.openephys",
    synonyms=["Open Ephys Format"],
)
ContentType.application_vnd_openxmlformats_officedocument_spreadsheetml_sheet = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    file_extensions=[".xlsx"],
    name="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    related_media_type="https://www.iana.org/assignments/media-types/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    synonyms=["Microsoft Excel (Open XML)", "XLSX"],
)
ContentType.application_vnd_openxmlformats_officedocument_wordprocessingml_document = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.openxmlformats-officedocument.wordprocessingml.document",
    file_extensions=[".docx"],
    name="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    related_media_type="https://www.iana.org/assignments/media-types/application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    synonyms=["Microsoft Word (OpenXML)", "DOCX"],
)
ContentType.application_vnd_oxford_instruments = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.oxford-instruments",
    file_extensions=[".top"],
    name="application/vnd.oxford-instruments",
    synonyms=["Oxford Instruments"],
)
ContentType.application_vnd_oxford_instruments_bitplaneimaris = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.oxford-instruments.bitplaneimaris",
    file_extensions=[".ims"],
    name="application/vnd.oxford-instruments.bitplaneimaris",
    synonyms=["Bitplane Imaris"],
)
ContentType.application_vnd_pco_pcoraw = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.pco.pcoraw",
    file_extensions=[".rec", ".pcoraw"],
    name="application/vnd.pco.pcoraw",
    synonyms=["PCORAW"],
)
ContentType.application_vnd_perkinelmer_columbus = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.perkinelmer.columbus",
    file_extensions=[".tiff", ".csv", ".xml"],
    name="application/vnd.perkinelmer.columbus",
    synonyms=["PerkinElmer Columbus"],
)
ContentType.application_vnd_perkinelmer_densitometer = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.perkinelmer.densitometer",
    file_extensions=[".pds"],
    name="application/vnd.perkinelmer.densitometer",
    synonyms=["PerkinElmer Densitometer"],
)
ContentType.application_vnd_perkinelmer_evotec = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.perkinelmer.evotec",
    file_extensions=[".res", ".mea", ".flex"],
    name="application/vnd.perkinelmer.evotec",
    synonyms=["Evotec/PerkinElmer Opera Flex"],
)
ContentType.application_vnd_perkinelmer_nuance = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.perkinelmer.nuance",
    file_extensions=[".im3"],
    name="application/vnd.perkinelmer.nuance",
    synonyms=["PerkinElmer Nuance"],
)
ContentType.application_vnd_perkinelmer_operetta = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.perkinelmer.operetta",
    file_extensions=[".xml", ".tiff"],
    name="application/vnd.perkinelmer.operetta",
    synonyms=["PerkinElmer Operetta"],
)
ContentType.application_vnd_perkinelmer_ultraview = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.perkinelmer.ultraview",
    file_extensions=[".4", ".3", ".2", ".tiff"],
    name="application/vnd.perkinelmer.ultraview",
    synonyms=["PerkinElmer UltraVIEW"],
)
ContentType.application_vnd_perkinelmer_vectra = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.perkinelmer.vectra",
    file_extensions=[".qptiff", ".tiff"],
    name="application/vnd.perkinelmer.vectra",
    synonyms=["PerkinElmer Vectra QPTIFF"],
)
ContentType.application_vnd_perkinelmer_volocity = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.perkinelmer.volocity",
    file_extensions=[".mvd2"],
    name="application/vnd.perkinelmer.volocity",
)
ContentType.application_vnd_perkinelmer_volocitylibraryclipping = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.perkinelmer.volocitylibraryclipping",
    file_extensions=[".acff"],
    name="application/vnd.perkinelmer.volocitylibraryclipping",
)
ContentType.application_vnd_pickle = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.pickle",
    file_extensions=[".pkl", ".pickle"],
    name="application/vnd.pickle",
    synonyms=["Python pickle files"],
)
ContentType.application_vnd_picoquant = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.picoquant",
    file_extensions=[".bin"],
    name="application/vnd.picoquant",
    synonyms=["PicoQuant Bin"],
)
ContentType.application_vnd_pixar_renderman_interface_bytestream = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.pixar.renderman.interface-bytestream",
    file_extensions=[".rib"],
    name="application/vnd.pixar.renderman.interface-bytestream",
    synonyms=["RenderMan Interface Bytestream"],
)
ContentType.application_vnd_plexon = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.plexon",
    file_extensions=[".plx"],
    name="application/vnd.plexon",
    synonyms=["Plexon acquisition system"],
)
ContentType.application_vnd_plexon_neuroexplorer = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.plexon.neuroexplorer",
    file_extensions=[".nex"],
    name="application/vnd.plexon.neuroexplorer",
    synonyms=["NeuroExplorer files"],
)
ContentType.application_vnd_plot3d = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.plot3d",
    file_extensions=[".xyz", ".q"],
    name="application/vnd.plot3d",
    synonyms=["PLOT3D"],
)
ContentType.application_vnd_pov_ray_densityfile = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.pov-ray.densityfile",
    file_extensions=[".df3"],
    name="application/vnd.pov-ray.densityfile",
    synonyms=["POV-Ray density file"],
)
ContentType.application_vnd_prairie_technologies = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.prairie-technologies",
    file_extensions=[".cfg", ".xml", ".tiff"],
    name="application/vnd.prairie-technologies",
    synonyms=["Prairie Technologies TIFF"],
)
ContentType.application_vnd_princeton_instruments = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.princeton-instruments",
    file_extensions=[".spe"],
    name="application/vnd.princeton-instruments",
    synonyms=["Princeton Instruments SPE"],
)
ContentType.application_vnd_quesant = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.quesant",
    file_extensions=[".afm"],
    name="application/vnd.quesant",
    synonyms=["Quesant"],
)
ContentType.application_vnd_quicknii_flat = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.quicknii.flat",
    file_extensions=[".flat"],
    name="application/vnd.quicknii.flat",
    synonyms=["QuickNII flat file"],
)
ContentType.application_vnd_quickniiplusjson = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.quicknii+json",
    file_extensions=[".json"],
    name="application/vnd.quicknii+json",
    related_media_type="https://www.iana.org/assignments/media-types/application/json",
    synonyms=["QuickNII JavaScript Object Notation", "QuickNII JSON"],
)
ContentType.application_vnd_quickniiplusxml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.quicknii+xml",
    file_extensions=[".xml"],
    name="application/vnd.quicknii+xml",
    related_media_type="https://www.iana.org/assignments/media-types/application/xml",
    synonyms=["QuickNII Extensible Markup Language", "QuickNII XML"],
)
ContentType.application_vnd_raw_binarysignal = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.raw.binarysignal",
    file_extensions=[".raw"],
    name="application/vnd.raw.binarysignal",
    synonyms=["RawBinarySignal"],
)
ContentType.application_vnd_raw_mcs = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.raw.mcs",
    file_extensions=[".raw"],
    name="application/vnd.raw.mcs",
    synonyms=["RawMCS", "Raw Multi Channel System", "MCS"],
)
ContentType.application_vnd_rawbinarysignal = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.rawbinarysignal",
    file_extensions=[".raw"],
    name="application/vnd.rawbinarysignal",
    synonyms=["Raw binary interleaved compact files"],
)
ContentType.application_vnd_rhk = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.rhk",
    file_extensions=[".sm3", ".sm2"],
    name="application/vnd.rhk",
    synonyms=["RHK"],
)
ContentType.application_vnd_rochedigitaldiagnostics_ventana = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.rochedigitaldiagnostics.ventana",
    file_extensions=[".tiff", ".bif"],
    name="application/vnd.rochedigitaldiagnostics.ventana",
    synonyms=["Ventana BIF, Ventana TIFF"],
)
ContentType.application_vnd_sbtab = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.sbtab",
    file_extensions=[".sbtab"],
    name="application/vnd.sbtab",
    synonyms=["Sbtab"],
)
ContentType.application_vnd_scalasca_cube3 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.scalasca.cube3",
    file_extensions=[".cube"],
    name="application/vnd.scalasca.cube3",
)
ContentType.application_vnd_scalasca_cube4 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.scalasca.cube4",
    file_extensions=[".cubex"],
    name="application/vnd.scalasca.cube4",
)
ContentType.application_vnd_sciunit_model = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.sciunit.model",
    file_extensions=[".py"],
    name="application/vnd.sciunit.model",
)
ContentType.application_vnd_sciunit_test = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.sciunit.test",
    file_extensions=[".py"],
    name="application/vnd.sciunit.test",
)
ContentType.application_vnd_score_p_filter = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.score-p.filter",
    file_extensions=[".txt"],
    name="application/vnd.score-p.filter",
)
ContentType.application_vnd_score_p_log = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.score-p.log",
    file_extensions=[".txt"],
    name="application/vnd.score-p.log",
    synonyms=["LOG"],
)
ContentType.application_vnd_score_p_score = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.score-p.score",
    file_extensions=[".txt"],
    name="application/vnd.score-p.score",
    synonyms=["SCORE"],
)
ContentType.application_vnd_seiko = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.seiko",
    file_extensions=[".xqd", ".xqf"],
    name="application/vnd.seiko",
    synonyms=["Seiko"],
)
ContentType.application_vnd_siemens_ecat7 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.siemens.ecat7",
    file_extensions=[".v"],
    name="application/vnd.siemens.ecat7",
)
ContentType.application_vnd_sivic = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.sivic",
    name="application/vnd.sivic",
)
ContentType.application_vnd_snakemake_snakefile = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.snakemake.snakefile",
    file_extensions=[],
    name="application/vnd.snakemake.snakefile",
    synonyms=["Snakefile"],
)
ContentType.application_vnd_sonata = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.sonata",
    file_extensions=[".csv", ".h5", ".json"],
    name="application/vnd.sonata",
)
ContentType.application_vnd_sonata_nest = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.sonata.nest",
    name="application/vnd.sonata.nest",
    synonyms=["SONATA:NEST"],
)
ContentType.application_vnd_sonata_neuron = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.sonata.neuron",
    name="application/vnd.sonata.neuron",
    synonyms=["SONATA:NEURON"],
)
ContentType.application_vnd_sonata_pynn = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.sonata.pynn",
    name="application/vnd.sonata.pynn",
    synonyms=["SONATA:PyNN"],
)
ContentType.application_vnd_spike2_sonpy_son = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.spike2.sonpy.son",
    file_extensions=[".smr"],
    name="application/vnd.spike2.sonpy.son",
    synonyms=["CED spike2 files"],
)
ContentType.application_vnd_spikeglx_system = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.spikeglx.system",
    name="application/vnd.spikeglx.system",
    synonyms=["SpikeGLX system"],
)
ContentType.application_vnd_spm = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.spm",
    file_extensions=[".mat"],
    name="application/vnd.spm",
)
ContentType.application_vnd_spmfile = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.spmfile",
    file_extensions=[".mat"],
    name="application/vnd.spmfile",
    synonyms=["SPM File "],
)
ContentType.application_vnd_stimfit = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.stimfit",
    file_extensions=[".abf", ".abf2", ".atf", ".axgx", ".axgd", ".cfs", ".heka", ".hdf5"],
    name="application/vnd.stimfit",
    synonyms=["Python stfio"],
)
ContentType.application_vnd_stimulate = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.stimulate",
    file_extensions=[".spr", ".sdt"],
    name="application/vnd.stimulate",
)
ContentType.application_vnd_structuredatafile = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.structuredatafile",
    file_extensions=[".sdf"],
    name="application/vnd.structuredatafile",
    synonyms=["Structure Data File"],
)
ContentType.application_vnd_tdt = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.tdt",
    name="application/vnd.tdt",
    synonyms=["Tucker David TTank format"],
)
ContentType.application_vnd_tecplot = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.tecplot",
    file_extensions=[".txt"],
    name="application/vnd.tecplot",
)
ContentType.application_vnd_thermo_fisher_scientific_cellomics = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.thermo-fisher-scientific.cellomics",
    file_extensions=[".dib", ".c01"],
    name="application/vnd.thermo-fisher-scientific.cellomics",
)
ContentType.application_vnd_thevirtualbrain = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.thevirtualbrain",
    file_extensions=[".hdf5", ".zip"],
    name="application/vnd.thevirtualbrain",
    synonyms=["TVB"],
)
ContentType.application_vnd_thevirtualbrain_metadataplustsv = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.thevirtualbrain.metadata+tsv",
    file_extensions=[".tsv"],
    name="application/vnd.thevirtualbrain.metadata+tsv",
)
ContentType.application_vnd_tillphotonics_tillvision = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.tillphotonics.tillvision",
    file_extensions=[".vws"],
    name="application/vnd.tillphotonics.tillvision",
)
ContentType.application_vnd_tracesplusxml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.traces+xml",
    file_extensions=[".xml"],
    name="application/vnd.traces+xml",
)
ContentType.application_vnd_trackscalarfile = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.trackscalarfile",
    file_extensions=[".tsf"],
    name="application/vnd.trackscalarfile",
    synonyms=["Track Scalar File Format"],
)
ContentType.application_vnd_tracksfileformat = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.tracksfileformat",
    file_extensions=[".tck"],
    name="application/vnd.tracksfileformat",
    synonyms=["Tracks File Format"],
)
ContentType.application_vnd_trackvis_trackfile = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.trackvis.trackfile",
    file_extensions=[".trk"],
    name="application/vnd.trackvis.trackfile",
)
ContentType.application_vnd_treslte = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.treslte",
    file_extensions=[".tiff", ".sld", ".jpg"],
    name="application/vnd.treslte",
    synonyms=["Trestle"],
)
ContentType.application_vnd_ubm = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.ubm",
    file_extensions=[".pr3"],
    name="application/vnd.ubm",
    synonyms=["UBM"],
)
ContentType.application_vnd_unicore_workflowplusjson = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.unicore.workflow+json",
    file_extensions=[".json"],
    name="application/vnd.unicore.workflow+json",
    synonyms=["UNICORE workflow description language"],
)
ContentType.application_vnd_unisoku = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.unisoku",
    file_extensions=[".dat", ".hdr"],
    name="application/vnd.unisoku",
    synonyms=["Unisoku"],
)
ContentType.application_vnd_vaa3d_apo = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vaa3d.apo",
    file_extensions=[".csv", ".apo"],
    name="application/vnd.vaa3d.apo",
)
ContentType.application_vnd_vaa3d_marker = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vaa3d.marker",
    file_extensions=[".csv", ".marker"],
    name="application/vnd.vaa3d.marker",
)
ContentType.application_vnd_vaa3d_rawfile = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vaa3d.rawfile",
    file_extensions=[".v3draw", ".raw", ".v3dpbd"],
    name="application/vnd.vaa3d.rawfile",
)
ContentType.application_vnd_vaa3d_surfaceformat = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vaa3d.surfaceformat",
    file_extensions=[".v3ds"],
    name="application/vnd.vaa3d.surfaceformat",
    synonyms=["Vaa3d Surface Format"],
)
ContentType.application_vnd_varianfdf = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.varianfdf",
    file_extensions=[".fdf"],
    name="application/vnd.varianfdf",
    synonyms=["Varian FDF"],
)
ContentType.application_vnd_veeco = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.veeco",
    file_extensions=[".tfr", ".ffr", ".zfr", ".zfp", ".2fl"],
    name="application/vnd.veeco",
    synonyms=["TopoMetrix"],
)
ContentType.application_vnd_veecoafm = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.veecoafm",
    file_extensions=[".hdf"],
    name="application/vnd.veecoafm",
    synonyms=["Veeco AFM"],
)
ContentType.application_vnd_vfgen = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vfgen",
    file_extensions=[".vf"],
    name="application/vnd.vfgen",
    synonyms=["Vector Field File"],
)
ContentType.application_vnd_vgsam = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vgsam",
    file_extensions=[".dti"],
    name="application/vnd.vgsam",
)
ContentType.application_vnd_visitechinternational_xys = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.visitechinternational.xys",
    file_extensions=[".html", ".xys"],
    name="application/vnd.visitechinternational.xys",
)
ContentType.application_vnd_visualignplusjson = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.visualign+json",
    file_extensions=[".json"],
    name="application/vnd.visualign+json",
    related_media_type="https://www.iana.org/assignments/media-types/application/json",
    synonyms=["VisuAlign JavaScript Object Notation", "VisuAlign JSON"],
)
ContentType.application_vnd_voluba_v1_landmark_pairsplusjson = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.voluba.v1.landmarkPairs+json",
    file_extensions=[".json"],
    name="application/vnd.voluba.v1.landmarkPairs+json",
    synonyms=["VoluBA (v1) Landmark Pairs"],
)
ContentType.application_vnd_voluba_v1_linear_transformplusjson = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.voluba.v1.linearTransform+json",
    file_extensions=[".json"],
    name="application/vnd.voluba.v1.linearTransform+json",
    synonyms=["VoluBA (v1) Linear Transformation"],
)
ContentType.application_vnd_volumeproperty = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.volumeproperty",
    file_extensions=[".vp"],
    name="application/vnd.volumeproperty",
    synonyms=["Volume Property"],
)
ContentType.application_vnd_vtb = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vtb",
    file_extensions=[".xml"],
    name="application/vnd.vtb",
)
ContentType.application_vnd_vth = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vth",
    file_extensions=[".xml"],
    name="application/vnd.vth",
)
ContentType.application_vnd_vthb = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vthb",
    file_extensions=[".xml"],
    name="application/vnd.vthb",
)
ContentType.application_vnd_vti = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vti",
    file_extensions=[".xml"],
    name="application/vnd.vti",
)
ContentType.application_vnd_vtm = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vtm",
    file_extensions=[".xml"],
    name="application/vnd.vtm",
)
ContentType.application_vnd_vtmb = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vtmb",
    file_extensions=[".xml"],
    name="application/vnd.vtmb",
)
ContentType.application_vnd_vtp = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vtp",
    file_extensions=[".xml"],
    name="application/vnd.vtp",
)
ContentType.application_vnd_vtr = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vtr",
    file_extensions=[".xml"],
    name="application/vnd.vtr",
)
ContentType.application_vnd_vts = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vts",
    file_extensions=[".xml"],
    name="application/vnd.vts",
)
ContentType.application_vnd_vtu = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.vtu",
    file_extensions=[".xml"],
    name="application/vnd.vtu",
)
ContentType.application_vnd_wadsworthcenter_spider = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.wadsworthcenter.spider",
    file_extensions=[".spi", ".stk"],
    name="application/vnd.wadsworthcenter.spider",
    synonyms=["SPIDER"],
)
ContentType.application_vnd_watechnology_wa_top = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.watechnology.wa-top",
    file_extensions=[".wat"],
    name="application/vnd.watechnology.wa-top",
    synonyms=["WA-TOP"],
)
ContentType.application_vnd_wavefronttechnologies = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.wavefronttechnologies",
    file_extensions=[".obj"],
    name="application/vnd.wavefronttechnologies",
    related_media_type="https://www.iana.org/assignments/media-types/model/obj",
    synonyms=["Wavefront OBJ"],
)
ContentType.application_vnd_wavefronttechnologies_mtl = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.wavefronttechnologies.mtl",
    file_extensions=[".mtl"],
    name="application/vnd.wavefronttechnologies.mtl",
    related_media_type="https://www.iana.org/assignments/media-types/model/mtl",
    synonyms=["Wavefront MTL"],
)
ContentType.application_vnd_wavemetrics_igorpro = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.wavemetrics.igorpro",
    file_extensions=[".igor"],
    name="application/vnd.wavemetrics.igorpro",
)
ContentType.application_vnd_winedr = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.winedr",
    file_extensions=[".edr"],
    name="application/vnd.winedr",
    synonyms=["WinEdr files", "EDR"],
)
ContentType.application_vnd_winwcp = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.winwcp",
    file_extensions=[".wcp"],
    name="application/vnd.winwcp",
    synonyms=["WinWCP files"],
)
ContentType.application_vnd_woolz = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.woolz",
    file_extensions=[".wlz"],
    name="application/vnd.woolz",
)
ContentType.application_vnd_x_matlab_data = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.x-matlab-data",
    file_extensions=[".mat"],
    name="application/vnd.x-matlab-data",
)
ContentType.application_vnd_xdmf = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.xdmf",
    file_extensions=[".xdmf", ".xmf"],
    name="application/vnd.xdmf",
    synonyms=["eXtensible Data Model and Format"],
)
ContentType.application_vnd_yokogawa_cv7000 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.yokogawa.cv7000",
    file_extensions=[".tiff", ".wpi"],
    name="application/vnd.yokogawa.cv7000",
)
ContentType.application_vnd_zarr = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.zarr",
    file_extensions=[".zarray", ".zarr"],
    name="application/vnd.zarr",
    synonyms=["Zarr format array "],
)
ContentType.application_vnd_zeiss = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.zeiss",
    file_extensions=[".czi"],
    name="application/vnd.zeiss",
)
ContentType.application_vnd_zeiss_axio_csm = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.zeiss.axio-csm",
    file_extensions=[".lsm  "],
    name="application/vnd.zeiss.axio-csm",
)
ContentType.application_vnd_zeiss_axio_vision = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.zeiss.axio-vision",
    file_extensions=[".xml", ".tiff", ".zvl"],
    name="application/vnd.zeiss.axio-vision",
)
ContentType.application_vnd_zeiss_leo = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.zeiss.leo",
    file_extensions=[".tiff", ".sxm"],
    name="application/vnd.zeiss.leo",
    synonyms=["LEO"],
)
ContentType.application_vnd_zeiss_lsm_510 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_vnd.zeiss.lsm-510",
    file_extensions=[".mdb", ".lsm"],
    name="application/vnd.zeiss.lsm-510",
)
ContentType.application_x_blender = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_x-blender",
    file_extensions=[".blend"],
    name="application/x-blender",
    synonyms=["Blender scene description format"],
)
ContentType.application_x_font_speedo = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_x-font-speedo",
    file_extensions=[".spd"],
    name="application/x-font-speedo",
    synonyms=["Speedo fonts"],
)
ContentType.application_x_hdf = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_x-hdf",
    file_extensions=[".hdf5"],
    name="application/x-hdf",
    synonyms=["Hierarchical Data Format version 5", "HDF5"],
)
ContentType.application_x_ipynbplusjson = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_x-ipynb+json",
    file_extensions=[".ipynb"],
    name="application/x-ipynb+json",
    specification="https://nbformat.readthedocs.io/en/latest/format_description.html",
    synonyms=["Jupyter Notebook", "IPYNB"],
)
ContentType.application_x_kseg = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_x-kseg",
    file_extensions=[".seg"],
    name="application/x-kseg",
    synonyms=["KSEG file format"],
)
ContentType.application_x_latex = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_x-latex",
    file_extensions=[".latex"],
    name="application/x-latex",
)
ContentType.application_x_netcdf = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_x-netcdf",
    file_extensions=[".cdf", ".nc"],
    name="application/x-netcdf",
    synonyms=["Network Common Data Form"],
)
ContentType.application_x_tgif = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_x-tgif",
    file_extensions=[".obj"],
    name="application/x-tgif",
    synonyms=["Tgif file format"],
)
ContentType.application_xml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_xml",
    file_extensions=[".xml"],
    name="application/xml",
    related_media_type="https://www.iana.org/assignments/media-types/application/xml",
    synonyms=["Extensible Markup Language", "XML"],
)
ContentType.application_yaml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_yaml",
    file_extensions=[".yml", ".yaml"],
    name="application/yaml",
    synonyms=["application/yml", "application/vnd.yaml", "application/vnd.yml", "YAML", "Yet Another Markup Language"],
)
ContentType.application_zip = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/application_zip",
    file_extensions=[".zip", ".zipx"],
    name="application/zip",
    related_media_type="https://www.iana.org/assignments/media-types/application/zip",
    specification="https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT",
    synonyms=["ZIP", "ZIP file", "zipfile"],
)
ContentType.image_bmp = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_bmp",
    file_extensions=[".bmp"],
    name="image/bmp",
    related_media_type="https://www.iana.org/assignments/media-types/image/bmp",
    synonyms=["Bitmap image"],
)
ContentType.image_jp2 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_jp2",
    file_extensions=[".jpc", ".j2c", ".j2k"],
    name="image/jp2",
    synonyms=["JPEG 2000"],
)
ContentType.image_jpeg = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_jpeg",
    file_extensions=[".jpg", ".jpeg", ".jif", ".jfif", ".pjp", ".pjpeg"],
    name="image/jpeg",
    synonyms=["Joint Photographic Expert Group", "JPG JPEG"],
)
ContentType.image_png = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_png",
    file_extensions=[".png"],
    name="image/png",
    related_media_type="https://www.iana.org/assignments/media-types/image/png",
    synonyms=["Portable Network Graphics", "PNG"],
)
ContentType.image_tiff = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff",
    file_extensions=[".tiff", ".tif"],
    name="image/tiff",
    related_media_type="https://www.iana.org/assignments/media-types/image/tiff",
    synonyms=["Tagged Image File (Tiled)"],
)
ContentType.image_tiff_andor_abd = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.andor.abd",
    file_extensions=[".tiff"],
    name="image/tiff.andor.abd",
    synonyms=["Andor Bio-Imaging Division (ABD) TIFF"],
)
ContentType.image_tiff_improvision = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.improvision",
    file_extensions=[".tiff"],
    name="image/tiff.improvision",
    synonyms=["Improvision TIFF"],
)
ContentType.image_tiff_ionpath_mibi = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.ionpath.mibi",
    file_extensions=[".tiff"],
    name="image/tiff.ionpath.mibi",
    synonyms=["Ionpath MIBI"],
)
ContentType.image_tiff_metamorph_75 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.metamorph.75",
    file_extensions=[".tiff"],
    name="image/tiff.metamorph.75",
    synonyms=["MetaMorph 7.5 TIFF"],
)
ContentType.image_tiff_mias = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.mias",
    file_extensions=[".tiff"],
    name="image/tiff.mias",
    synonyms=["MIAS (Maia Scientific)"],
)
ContentType.image_tiff_mikroscan = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.mikroscan",
    file_extensions=[".tiff"],
    name="image/tiff.mikroscan",
    synonyms=["Mikroscan TIFF"],
)
ContentType.image_tiff_multichannel = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.multichannel",
    file_extensions=[".tiff", ".tif"],
    name="image/tiff.multichannel",
    synonyms=["Tagged Image File (Multi channel)"],
)
ContentType.image_tiff_multipage = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.multipage",
    file_extensions=[".tiff", ".tif"],
    name="image/tiff.multipage",
    synonyms=["Tagged Image File (Multi-page)"],
)
ContentType.image_tiff_nikon_elements = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.nikon.elements",
    file_extensions=[".tiff"],
    name="image/tiff.nikon.elements",
    synonyms=["Nikon Elements"],
)
ContentType.image_tiff_nikon_ez_c1 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.nikon.ez-c1",
    file_extensions=[".tiff"],
    name="image/tiff.nikon.ez-c1",
    synonyms=["Nikon EZ-C1"],
)
ContentType.image_tiff_olympus_fluoview = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.olympus.fluoview",
    file_extensions=[".tiff"],
    name="image/tiff.olympus.fluoview",
    synonyms=["Olympus FluoView TIFF"],
)
ContentType.image_tiff_olympus_sis = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.olympus.sis",
    file_extensions=[".tiff"],
    name="image/tiff.olympus.sis",
    synonyms=["Olympus SIS TIFF"],
)
ContentType.image_tiff_photoshop = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.photoshop",
    file_extensions=[".tiff"],
    name="image/tiff.photoshop",
    synonyms=["Photoshop TIFF"],
)
ContentType.image_tiff_yokogawa_cellvoyager = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_tiff.yokogawa.cellvoyager",
    file_extensions=[".tiff"],
    name="image/tiff.yokogawa.cellvoyager",
)
ContentType.image_vnd_adobe_photoshop = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_vnd.adobe.photoshop",
    file_extensions=[".psd"],
    name="image/vnd.adobe.photoshop",
)
ContentType.image_vnd_compix_simplepcihcimage = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_vnd.compix.simplepcihcimage",
    file_extensions=[".cxd "],
    name="image/vnd.compix.simplepcihcimage",
    synonyms=["SimplePCI, HCImage"],
)
ContentType.image_vnd_silicongraphicsimage = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_vnd.silicongraphicsimage",
    file_extensions=[".bw", ".rgb", ".rgba"],
    name="image/vnd.silicongraphicsimage",
    synonyms=["Silicon Graphics Image"],
)
ContentType.image_x_eps = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_x-eps",
    file_extensions=[".epsf", ".ps", ".epsi", ".eps"],
    name="image/x-eps",
    synonyms=["Encapsulated PostScript", "EPS"],
)
ContentType.image_x_panasonic_rw = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_x-panasonic-rw",
    file_extensions=[".raw"],
    name="image/x-panasonic-rw",
    synonyms=["Panasonic RAW file format"],
)
ContentType.image_x_targa = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/image_x-targa",
    file_extensions=[".tga"],
    name="image/x-targa",
)
ContentType.text_cfg = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_cfg",
    file_extensions=[".cfg"],
    name="text/cfg",
)
ContentType.text_csv = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_csv",
    file_extensions=[".csv"],
    name="text/csv",
    related_media_type="https://www.iana.org/assignments/media-types/text/csv",
    synonyms=["Comma-Separated Value", "CSV"],
)
ContentType.text_html = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_html",
    file_extensions=[".html", ".htm"],
    name="text/html",
    related_media_type="https://www.iana.org/assignments/media-types/text/html",
    synonyms=["Hypertext Markup Language", "HTML"],
)
ContentType.text_markdown = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_markdown",
    file_extensions=[".md", ".markdown"],
    name="text/markdown",
    related_media_type="https://www.iana.org/assignments/media-types/text/markdown",
    synonyms=["Markdown"],
)
ContentType.text_plain = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_plain",
    file_extensions=[".txt"],
    name="text/plain",
    synonyms=["plain text file format"],
)
ContentType.text_prs_fallenstein_rst = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_prs.fallenstein.rst",
    file_extensions=[".txt", ".rst"],
    name="text/prs.fallenstein.rst",
)
ContentType.text_semicolon_separated_values = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_semicolon-separated-values",
    file_extensions=[".csv"],
    name="text/semicolon-separated-values",
    synonyms=["semi-colon separated value"],
)
ContentType.text_tab_separated_values = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_tab-separated-values",
    file_extensions=[".tsv", ".csv"],
    name="text/tab-separated-values",
    related_media_type="https://www.iana.org/assignments/media-types/text/tab-separated-values",
    synonyms=["Tab-Separated Value", "TSV"],
)
ContentType.text_x_cmlplusxml = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-cml+xml",
    file_extensions=[".cml"],
    name="text/x-cml+xml",
    specification="http://www.xml-cml.org/schema/schema3/schema.xsd",
)
ContentType.text_x_matlab = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-matlab",
    file_extensions=[".m"],
    name="text/x-matlab",
    synonyms=["MATLAB Plain", "MATLAB Plain Script"],
)
ContentType.text_x_objcsrc = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-objcsrc",
    file_extensions=[".m"],
    name="text/x-objcsrc",
    synonyms=["Objective C source file"],
)
ContentType.text_x_python = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-python",
    file_extensions=[".py"],
    name="text/x-python",
)
ContentType.text_x_python_2 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-python.2",
    file_extensions=[".py"],
    name="text/x-python.2",
)
ContentType.text_x_python_2_7 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-python.2.7",
    file_extensions=[".py"],
    name="text/x-python.2.7",
)
ContentType.text_x_python_3 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-python.3",
    file_extensions=[".py"],
    name="text/x-python.3",
)
ContentType.text_x_python_3_6 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-python.3.6",
    file_extensions=[".py"],
    name="text/x-python.3.6",
)
ContentType.text_x_python_3_6_5 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-python.3.6.5",
    file_extensions=[".py"],
    name="text/x-python.3.6.5",
)
ContentType.text_x_python_3_7 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-python.3.7",
    file_extensions=[".py"],
    name="text/x-python.3.7",
)
ContentType.text_x_python_3_8 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-python.3.8",
    file_extensions=[".py"],
    name="text/x-python.3.8",
)
ContentType.text_x_python_3_9 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/text_x-python.3.9",
    file_extensions=[".py"],
    name="text/x-python.3.9",
)
ContentType.video_mp4 = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/video_mp4",
    file_extensions=[".mp4"],
    name="video/mp4",
    related_media_type="https://www.iana.org/assignments/media-types/video/mp4",
    synonyms=["Moving Picture Experts Group 4 video file", "MPEG-4"],
)
ContentType.video_quicktime = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/video_quicktime",
    file_extensions=[".mov"],
    name="video/quicktime",
    synonyms=["QuickTime Movie"],
)
ContentType.video_x_msvideo = ContentType(
    id="https://openminds.ebrains.eu/instances/contentTypes/video_x-msvideo",
    file_extensions=[".avi"],
    name="video/x-msvideo",
    synonyms=["Audio Video Interleave", "AVI"],
)
