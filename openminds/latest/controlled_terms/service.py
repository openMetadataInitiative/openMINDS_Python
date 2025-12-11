"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Service(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Service"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "definition",
            str,
            "definition",
            formatting="text/markdown",
            multiline=True,
            description="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
            instructions="Enter one sentence for defining this term.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of the service.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "interlex_identifier",
            IRI,
            "interlexIdentifier",
            description="Persistent identifier for a term registered in the InterLex project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the integrated ontology entry in the InterLex project.",
        ),
        Property(
            "knowledge_space_link",
            IRI,
            "knowledgeSpaceLink",
            description="Persistent link to an encyclopedia entry in the Knowledge Space project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the wiki page of the corresponding term in the KnowledgeSpace.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the service.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term.",
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
            instructions="Enter one or several synonyms (including abbreviations) for this controlled term.",
        ),
    ]

    def __init__(
        self,
        id=None,
        definition=None,
        description=None,
        interlex_identifier=None,
        knowledge_space_link=None,
        name=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            name=name,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
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


Service.allen_institute_cell_types_data_portal = Service(
    id="https://openminds.om-i.org/instances/service/AllenInstituteCellTypesDataPortal",
    definition="Web application for visualizing and browsing the Allen Cell Types Database.",
    description="The Allen Cell Types Database contains a multimodal characterization of single brain cells by electrophysiology and morphology, as well as single-cell transcriptional data from nuclei or whole cells, with search and visualization tools for exploring the single cell transcriptomics for LGd, and single cell electrophysiology, morphology, and modeling data.",
    name="Allen Institute Cell Types Data Portal",
)
Service.ebrains_collaboratory_lab = Service(
    id="https://openminds.om-i.org/instances/service/EBRAINSCollaboratoryLab",
    definition="The Collaboratory Lab is a web-based JupyterLab service provided by the EBRAINS research infrastructure.",
    description="The Lab gives EBRAINS users the ability to develop and run programs in the cloud from their web browser, without needing to install anything on their local machine. The Lab offers a readily installed programming environment and all of the EBRAINS tools and libraries which can be run from it.",
    name="EBRAINS Collaboratory Lab",
)
Service.ebrains_knowledge_graph_search_ui = Service(
    id="https://openminds.om-i.org/instances/service/EBRAINSKnowledgeGraphSearchUI",
    definition="The EBRAINS Knowledge Graph Search User Interface is a web application for searching the EBRAINS Knowledge Graph.",
    description="The Knowledge Graph Search User Interface makes data, models and software discoverable and easy to use. The user interface allows for free text searches and provides filters to narrow searches based on metadata that classifies data according to experimental method, data modality and species among other options. The query results are displayed as Dataset cards containing key information about the dataset, e.g. its metadata, terms of use, and how to cite and reuse the data. Datasets that have undergone spatial registration to an atlas contain links to 3D or 2D viewers for navigating the data in atlas space.",
    name="EBRAINS Knowledge Graph Search UI",
    synonyms=[
        "EBRAINS KG Search UI",
        "EBRAINS KGS UI",
        "EBRAINS Knowledge Graph Search User Interface",
        "KG Search UI",
        "KGS UI",
        "Knowledge Graph Search User Interface",
    ],
)
Service.ebrains_model_catalog = Service(
    id="https://openminds.om-i.org/instances/service/EBRAINSModelCatalog",
    definition="The EBRAINS Model Catalog contains information about models developed and/or used within the EBRAINS research infrastructure.",
    description="The Model Catalog app provides a more in-depth view of computational models than is available in the KG Search UI, including tools for visualizing model structure, exploring how models have been validated against experimental data, and comparing different models.",
    name="EBRAINS Model Catalog",
)
Service.erbains_collaboratory_wiki = Service(
    id="https://openminds.om-i.org/instances/service/ERBAINSCollaboratoryWiki",
    definition="The Collaboratory Wiki is the main interface to access all other Collaboratory service provided by the EBRAINS research infrastructure.",
    description="The Wiki service of the Collaboratory hosts the main interface to access all the other Collaboratory services. As such, it embodies the full concept of collab workspaces and most users consider it to be the collab service. Wiki pages are a convenient way of publishing content on the web, either addressing the Team of the collab or making the content completely public, that is, also accessible to visitors who do not have an EBRAINS account.",
    name="EBRAINS Collaboratory Wiki",
)
Service.locali_zoom = Service(
    id="https://openminds.om-i.org/instances/service/LocaliZoom",
    definition="Web application for viewing of series of high-resolution 2D images that have been anchored to reference atlases.",
    description="LocaliZoom allows the viewing and exploring of high-resolution images with superimposed atlas overlays. For more information see: https://localizoom.readthedocs.io/en/latest/index.html.",
    name="LocaliZoom",
)
Service.mesh_view = Service(
    id="https://openminds.om-i.org/instances/service/MeshView",
    definition="Web application for viewing atlas surface meshes and data point clouds.",
    description="MeshView is a web application for real-time 3D display of surface mesh data representing structural parcellations from volumetric atlases, such as the Waxholm Space Atlas of the Sprague Dawley Rat Brain.",
    name="MeshView",
)
Service.model_db = Service(
    id="https://openminds.om-i.org/instances/service/ModelDB",
    definition="ModelDB is a curated database of published models in the broad domain of computational neuroscience.",
    description="ModelDB provides an accessible location for storing and efficiently retrieving computational neuroscience models. A ModelDB entry contains a model's source code, concise description, and a citation of the article that published it. The source code can be in any language for any environment, can be viewed before downloading, and optionally can be auto-launched on download.",
    name="ModelDB",
)
Service.multi__image_o_sd = Service(
    id="https://openminds.om-i.org/instances/service/Multi-Image-OSd",
    definition="Web application for viewing of series of high-resolution 2D images.",
    description="Multi-Image-OSd allows the viewing and exploring of high-resolution images. For more information see: https://github.com/Neural-Systems-at-UIO/Multi-Image-OSd. This service is not supported anymore and has been replaced by 'SeriesZoom'. [edited 2025-09-11]",
    name="Multi-Image-OSd",
    synonyms=["Multi-Image OpenSeadragon viewer"],
)
Service.neuro_morpho_dot_org = Service(
    id="https://openminds.om-i.org/instances/service/NeuroMorphoDotOrg",
    definition="A web-based inventory dedicated to densely archive and organize all publicly shared digital reconstructions of neuronal morphology.",
    description="Digital reconstructions are a parsimonious and efficient representation of neuronal morphology. They allow extensive analysis and implementation of biophysical models of electrophysiology. However, reconstructing cells is a very labor-intensive and time-consuming process. A collection of such data is an invaluable resource for the neuroscience community. This inventory is meant to encourage data sharing among neuroscientists, enabling further use of this data and to prevent data loss.",
    name="NeuroMorpho.Org",
)
Service.neuroglancer = Service(
    id="https://openminds.om-i.org/instances/service/Neuroglancer",
    definition="'Neuroglancer' is a WebGL-based viewer for volumetric data.",
    description="'Neuroglancer' is capable of displaying arbitrary (non axis-aligned) cross-sectional views of volumetric data, as well as 3-D meshes and line-segment based models (skeletons). A live demo without any preloaded datasets is hosted at https://neuroglancer-demo.appspot.com.",
    name="Neuroglancer",
)
Service.neurosift = Service(
    id="https://openminds.om-i.org/instances/service/Neurosift",
    definition="Neurosift is a browser-based tool designed for the visualization of neuroscience data with a focus on NWB (Neurodata Without Borders) files.",
    name="Neurosift",
)
Service.series_zoom = Service(
    id="https://openminds.om-i.org/instances/service/SeriesZoom",
    definition="Web application for viewing of series of high-resolution 2D images.",
    description="SeriesZoom allows the viewing and exploring of high-resolution images. For more information see: https://github.com/Neural-Systems-at-UIO/SeriesZoom.",
    name="SeriesZoom",
    synonyms=["SeriesZoom"],
)
Service.siibra_explorer = Service(
    id="https://openminds.om-i.org/instances/service/siibraExplorer",
    definition="'siibra-explorer' is an interactive viewer for multilevel brain atlases",
    description="siibra-explorer is an frontend module wrapping around nehuba for visualizing volumetric brain volumes at possible high resolutions, and connecting to siibra-api for offering access to brain atlases of different species, including to navigate their brain region hierarchies, maps in different coordinate spaces, and linked regional data features. It provides metadata integration with the EBRAINS knowledge graph, different forms of data visualisation, and a structured plugin system for implementing custom extensions. For more information see: https://github.com/FZJ-INM1-BDA/siibra-explorer",
    name="siibra-explorer",
)
Service.zenodo = Service(
    id="https://openminds.om-i.org/instances/service/Zenodo",
    definition="Zenodo is a general-purpose open repository developed under the European OpenAIRE program and operated by CERN.",
    description="Zenodo allows researchers to deposit research papers, data sets, research software, reports, and any other research related digital artefacts.",
    name="Zenodo",
)
