"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class DiseaseModel(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/DiseaseModel"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
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
            description="Longer statement or account giving the characteristics of someone or something.",
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
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
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
    def by_name(cls, name):
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                cls._instance_lookup[instance.name] = instance
                if instance.synonyms:
                    for synonym in instance.synonyms:
                        cls._instance_lookup[synonym] = instance
        return cls._instance_lookup[name]


DiseaseModel.alzheimers_disease_model = DiseaseModel(
    id="https://openminds.ebrains.eu/instances/diseaseModel/alzheimersDiseaseModel",
    definition="An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Alzheimer's disease.",
    description="An animal or cell type model for Alzheimer's disease display all or some pathological processes that are observed in the actual disease in humans or animals, such as the formation of neurofibrillary tangles or amyloid-beta plaques.",
    name="Alzheimer's disease model",
)
DiseaseModel.autism_spectrum_disorder_model = DiseaseModel(
    id="https://openminds.ebrains.eu/instances/diseaseModel/autismSpectrumDisorderModel",
    definition="An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal autism sprectrum disorder.",
    name="autism spectrum disorder model",
)
DiseaseModel.epilepsy_model = DiseaseModel(
    id="https://openminds.ebrains.eu/instances/diseaseModel/epilepsyModel",
    definition="An animal or cell displaying all or some of the pathological processes that are observed for epilepsy in humans or animals.",
    description="Epilepsy describes a group of central nervous system disorders characterized by recurrent unprovoked seizures. A model of epilepsy displays all or some of the pathological processes that are observed for epilespy in humans or animals.",
    name="epilepsy model",
)
DiseaseModel.fragile_xsyndrome_model = DiseaseModel(
    id="https://openminds.ebrains.eu/instances/diseaseModel/fragileXsyndromeModel",
    definition="An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal fragile X syndrome.",
    description="An animal or cell type model for fragile X syndrome display all or some pathological processes that are observed in the actual disease in humans or animals, such as the general loss of FMR1 gene function.",
    name="fragile X syndrome model",
)
DiseaseModel.huntingtons_disease_model = DiseaseModel(
    id="https://openminds.ebrains.eu/instances/diseaseModel/huntingtonsDiseaseModel",
    definition="An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Huntington's disease.",
    name="Huntington's disease model",
)
DiseaseModel.parkinsons_disease_model = DiseaseModel(
    id="https://openminds.ebrains.eu/instances/diseaseModel/parkinsonsDiseaseModel",
    definition="An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Parkinson's disease.",
    name="Parkinson's disease model",
)
DiseaseModel.stroke_model = DiseaseModel(
    id="https://openminds.ebrains.eu/instances/diseaseModel/strokeModel",
    definition="An animal or cell displaying all or some of the pathological processes that are observed during stroke in humans or animals.",
    description="A sudden loss of neurological function secondary to hemorrhage or ischemia in the brain parenchyma due to a vascular event. A model of stroke displays some or all of the pathological processes that are observed during stroke in humans or animals.",
    name="stroke model",
    synonyms=[
        "cerebral infaction model",
        "cerebrovascular accident model",
        "cerebrovascular disease model",
        "CVA model",
        "stroke disorder model",
    ],
)
DiseaseModel.williams_beuren_syndrome_model = DiseaseModel(
    id="https://openminds.ebrains.eu/instances/diseaseModel/williamsBeurenSyndromeModel",
    definition="An animal or cell displaying all or some of the pathological processes that are observed in the actual human or animal Williams-Beuren syndrome.",
    name="Williams-Beuren syndrome model",
)
