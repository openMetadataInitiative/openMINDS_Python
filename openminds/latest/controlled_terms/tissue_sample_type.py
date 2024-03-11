"""
Structured information on the general type of the tissue sample.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class TissueSampleType(LinkedMetadata):
    """
    Structured information on the general type of the tissue sample.
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/TissueSampleType"
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


TissueSampleType.biopsy_sample = TissueSampleType(
    id="https://openminds.ebrains.eu/instances/tissueSampleType/biopsySample",
    definition="Typically very small sample of tissue that was excised from a living or deceased multicellular organism body.",
    interlex_identifier="http://uri.interlex.org/ilx_0782394",
    name="biopsy sample",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/OBI_0002650",
)
TissueSampleType.fluid_specimen = TissueSampleType(
    id="https://openminds.ebrains.eu/instances/tissueSampleType/fluidSpecimen",
    definition="A fluid sample either taken directly from a living or deceased multicellular organism body (i.e. body fluids) or produced in a laboratory.",
    name="fluid specimen",
)
TissueSampleType.hemisphere = TissueSampleType(
    id="https://openminds.ebrains.eu/instances/tissueSampleType/hemisphere",
    definition="One of the symmetric halves excised from a bilateral organ tissue sample (e.g., a brain) from a living or deceased multicellular organism body.",
    name="hemisphere",
)
TissueSampleType.heterogeneous_cell_population = TissueSampleType(
    id="https://openminds.ebrains.eu/instances/tissueSampleType/heterogeneousCellPopulation",
    definition="A sample of multiple cells/a population of cells that are of two or more different cell types.",
    name="heterogeneous cell population",
)
TissueSampleType.homogeneous_cell_population = TissueSampleType(
    id="https://openminds.ebrains.eu/instances/tissueSampleType/homogeneousCellPopulation",
    definition="A sample of multiple cells/a population of cells that are of the same cell type.",
    name="homogeneous cell population",
)
TissueSampleType.nerve = TissueSampleType(
    id="https://openminds.ebrains.eu/instances/tissueSampleType/nerve",
    definition="A nerve sample (i.e. a whole nerve or a part of a nerve) from a living or deceased multicellular organism body.",
    name="nerve",
)
TissueSampleType.single_cell = TissueSampleType(
    id="https://openminds.ebrains.eu/instances/tissueSampleType/singleCell",
    definition="A single cell sample from a living or deceased multicellular organism body.",
    name="single cell",
)
TissueSampleType.tissue_block = TissueSampleType(
    id="https://openminds.ebrains.eu/instances/tissueSampleType/tissueBlock",
    definition="A cube-like sample of tissue that was excised from a larger tissue sample (e.g., a whole organ) from a living or deceased multicellular organism body.",
    name="tissue block",
)
TissueSampleType.tissue_slice = TissueSampleType(
    id="https://openminds.ebrains.eu/instances/tissueSampleType/tissueSlice",
    definition="A thin and often flat sample of tissue that was excised from a larger tissue sample (e.g., a tissue block or a whole organ) from a living or deceased multicellular organism body.",
    name="tissue slice",
)
TissueSampleType.whole_organ = TissueSampleType(
    id="https://openminds.ebrains.eu/instances/tissueSampleType/wholeOrgan",
    definition="A whole organ sample from a living or deceased multicellular organism body.",
    name="whole organ",
)
