"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class OrganismSystem(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/OrganismSystem"
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
            description="Longer statement or account giving the characteristics of the organism system.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the organism system.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "other_cross_references",
            str,
            "otherCrossReference",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all internationalized resource identifiers (IRIs) pointing to cross-references to external databases or registries that are equivalent to this term (e.g., Wikidata). Do not repeat the preferred cross-reference.",
        ),
        Property(
            "other_ontology_identifiers",
            str,
            "otherOntologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all internationalized resource identifiers (IRIs) pointing to ontology entries that are equivalent to this term (e.g., UBERON). Do not repeat the preferred ontology identifier.",
        ),
        Property(
            "preferred_cross_reference",
            IRI,
            "preferredCrossReference",
            description="no description available",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred cross-reference to an external database or registry (e.g., KnowledgeSpace).",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term (e.g., InterLex).",
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
        name=None,
        other_cross_references=None,
        other_ontology_identifiers=None,
        preferred_cross_reference=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            name=name,
            other_cross_references=other_cross_references,
            other_ontology_identifiers=other_ontology_identifiers,
            preferred_cross_reference=preferred_cross_reference,
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


OrganismSystem.autonomic_nervous_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/autonomicNervousSystem",
    definition="Is an anatomical entity. Is part of the peripheral nervous system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0002410) ('is_a' and 'relationship')]",
    description="The autonomic nervous system is composed of neurons that are not under conscious control, and is comprised of two antagonistic components, the sympathetic and parasympathetic nervous systems. The autonomic nervous system regulates key functions including the activity of the cardiac (heart) muscle, smooth muscles (e.g. of the gut), and glands. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0002410)]",
    name="autonomic nervous system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0002410#autonomic-nervous-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0002410"),
    synonyms=[
        "autonomic division of peripheral nervous system",
        "autonomic part of peripheral nervous system",
        "divisio autonomica systematis nervosi peripherici",
        "pars autonomica systematis nervosi peripherici",
        "peripheral autonomic nervous system",
        "visceral nervous system",
    ],
)
OrganismSystem.cardiovascular_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/cardiovascularSystem",
    definition="'The 'cardiovascular system' is an anatomical organ system where the heart pumps blood through blood vessels to and from all parts of the body.",
    name="cardiovascular system",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0101670"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0004535#cardiovascular-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0004535"),
)
OrganismSystem.central_nervous_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/centralNervousSystem",
    definition="Is part of the nervous system. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001017)]",
    description="The central nervous system is the core nervous system that serves an integrating and coordinating function. In vertebrates it consists of the neural tube derivatives: the brain and spinal cord. In invertebrates it includes central ganglia plus nerve cord. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001017)]",
    name="central nervous system",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0101901"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0001017#central-nervous-system-1"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001017"),
    synonyms=["CNS", "systema nervosum centrale"],
)
OrganismSystem.cholinergic_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/cholinergicSystem",
    definition="The cholinergic system is composed of any molecule, protein, cell, tissue or organ that is related to acetylcholine.",
    name="cholinergic system",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0102133"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0025595#cholinergic-system-1"),
    preferred_ontology_identifier=IRI(
        "http://purl.obolibrary.org/obo/UBERON_0002204http://purl.obolibrary.org/obo/UBERON_0025595"
    ),
    synonyms=["acetylcholine system", "ach system", "ACh system"],
)
OrganismSystem.digestive_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/digestiveSystem",
    definition="The 'digestive system' is an anatomical organ system composed of organs devoted to the ingestion, digestion, the assimilation of food and the discharge of residual wastes.",
    name="digestive system",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0729362"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0001007#digestive-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001007"),
)
OrganismSystem.enteric_nervous_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/entericNervousSystem",
    definition="Is part of the autonomic nervous system. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0002005)]",
    description="The enteric nervous system is composed of two ganglionated neural plexuses in the gut wall which form one of the three major divisions of the autonomic nervous system. The enteric nervous system innervates the gastrointestinal tract, the pancreas, and the gall bladder. It contains sensory neurons, interneurons, and motor neurons. Thus the circuitry can autonomously sense the tension and the chemical environment in the gut and regulate blood vessel tone, motility, secretions, and fluid transport. The system is itself governed by the central nervous system and receives both parasympathetic and sympathetic innervation. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0002005)]",
    name="enteric nervous system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0002005#enteric-nervous-system-1"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0002005"),
    synonyms=["enteric PNS", "PNS - enteric"],
)
OrganismSystem.extrapyramidal_tract_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/extrapyramidalTractSystem",
    definition="Is a regional part of brain. Is part of the motor system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035803) ('is_a' and 'relationship')]",
    description="A neural network located in the brain that is part of the motor system involved in the coordination of movement that is distinct from the pyramidal tract. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035803)]",
    name="extrapyramidal tract system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0035803#extrapyramidal-tract-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0035803"),
)
OrganismSystem.gabaergic_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/gabaergicSystem",
    definition="The gabaergic system is composed of any molecule, protein, cell, tissue or organ that is related to GABA.",
    name="gabaergic system",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0104506"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/NLXANAT:1005024#gabaergic-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0025591"),
    synonyms=["GABAergic system"],
)
OrganismSystem.glutamatergic_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/glutamatergicSystem",
    definition="The glutamatergic system is composed of any molecule, protein, cell, tissue or organ that is related to glutamate (when in the role of a neurotransmitter).",
    name="glutamatergic system",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0104682"],
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0025592"),
)
OrganismSystem.glymphatic_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/glymphaticSystem",
    definition="Is an anatomical entity and anatomical system. Is part of the nervous system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0036145) ('is_a' and 'relationship')]",
    description="Macroscopic waste clearance system that utilizes a unique system of perivascular tunnels, formed by astroglial cells, to promote efficient elimination of soluble proteins and metabolites from the central nervous system. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0036145)]",
    name="glymphatic system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0036145#glymphatic-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0036145"),
)
OrganismSystem.limbic_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/limbicSystem",
    definition="Is part of the forebrain. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000349)]",
    description="A set of midline structures surrounding the brainstem of the mammalian brain, originally described anatomically, e.g., hippocampal formation, amygdala, hypothalamus, cingulate cortex. Although the original designation was anatomical, the limbic system has come to be associated with the system in the brain subserving emotional functions. As such, it is very poorly defined and doesn't correspond closely to the anatomical meaning any longer. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000349)]",
    name="limbic system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0000349#limbic-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000349"),
)
OrganismSystem.motor_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/motorSystem",
    definition="Is a neural system. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0025525)]",
    description="The part of the central nervous system that is involved with movement. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0025525)]",
    name="motor system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0025525#motor-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0025525"),
)
OrganismSystem.musculoskeletal_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/musculoskeletalSystem",
    definition="The 'musculoskeletal system' is an anatomical organ system composed of organs providing the body with movement, stability, shape and support.",
    description="The musculoskeletal system (sometimes also called locomotor system) is subdivided into two broader systems, the skeletal system and the muscular system. The skeletal system includes bones and joints. The muscular system includes all muscles in the body.",
    name="musculoskeletal system",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0728294"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0002204#musculoskeletal-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0002204"),
    synonyms=["musculo-skeletal system"],
)
OrganismSystem.nervous_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/nervousSystem",
    definition="Is an anatomical entity and anatomical system. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001016)]",
    description="The nervous system is an organ system containing predominantly neuron and glial cells. In bilaterally symmetrical organism, it is arranged in a network of tree-like structures connected to a central body. The main functions of the nervous system are to regulate and control body functions, and to receive sensory input, process this information, and generate behavior. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001016)]",
    name="nervous system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0001016#nervous-system-1"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001016"),
    synonyms=["neurological system"],
)
OrganismSystem.neural_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/neuralSystem",
    definition="Is an anatomical entity. Is part of the nervous system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0023879) ('is_a' and 'relationship')]",
    description="A set of neural structures that subserve a specific function, e.g., visual system. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0023879)]",
    name="neural system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0023879#neural-system-1"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0023879"),
)
OrganismSystem.noradrenergic_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/noradrenergicSystem",
    definition="The noradrenergic system is composed of any molecule, protein, cell, tissue or organ that is related to norepinephrine (also known as noradrenaline).",
    name="noradrenergic system",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0107679"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/NLXANAT:1005027#noradrenergic-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0027225"),
)
OrganismSystem.parasympathetic_nervous_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/parasympatheticNervousSystem",
    definition="Is part of the autonomic nervous system. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000011)]",
    description="The parasympathetic nervous system is one of the two divisions of the vertebrate autonomic nervous system. Parasympathetic nerves emerge cranially as pre ganglionic fibers from oculomotor, facial, glossopharyngeal and vagus and from the sacral region of the spinal cord. Most neurons are cholinergic and responses are mediated by muscarinic receptors. The parasympathetic system innervates, for example: salivary glands, thoracic and abdominal viscera, bladder and genitalia. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000011)]",
    name="parasympathetic nervous system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0000011#parasympathetic-nervous-system-1"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000011"),
    synonyms=[
        "parasympathetic part of autonomic division of nervous system",
        "pars parasympathica divisionis autonomici systematis nervosi",
        "PNS - parasympathetic",
    ],
)
OrganismSystem.peripheral_nervous_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/peripheralNervousSystem",
    definition="Is an anatomical entity. Is part of the nervous system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000010) ('is_a' and 'relationship')]",
    description="A major division of the nervous system that contains nerves which connect the central nervous system (CNS) with sensory organs, other organs, muscles, blood vessels and glands. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000010)]",
    name="peripheral nervous system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0000010#peripheral-nervous-system-1"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000010"),
    synonyms=["pars peripherica", "systema nervosum periphericum"],
)
OrganismSystem.proprioceptive_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/proprioceptiveSystem",
    definition="Is a neural system. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0025533)]",
    description="The sensory system for the sense of proprioception. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0025533)]",
    name="proprioceptive system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0025533#proprioceptive-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0025533"),
)
OrganismSystem.sensorimotor_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/sensorimotorSystem",
    definition="Is a neural system. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0025534)]",
    name="sensorimotor system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0025534#sensorimotor-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0025534"),
)
OrganismSystem.serotonergic_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/serotonergicSystem",
    definition="The serotonergic system is composed of any molecule, protein, cell, tissue or organ that is related to serotonin.",
    name="serotonergic system",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0110555"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0025593#serotonergic-system-1"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0025593"),
    synonyms=["serotonin system", "5HT system", "5-HT system", "5-ht system", "5ht system"],
)
OrganismSystem.somatic_motor_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/somaticMotorSystem",
    definition="Is an anatomical entity. Is part of the somatic nervous system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0003945) ('is_a' and 'relationship')]",
    description="The neural tissue involved in the transmission of motor signals. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0003945)]",
    name="somatic motor system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0003945#somatic-motor-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0003945"),
)
OrganismSystem.somatic_nervous_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/somaticNervousSystem",
    definition="Is an anatomical entity. Is part of the peripheral nervous system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000012) ('is_a' and 'relationship')]",
    description="Part of peripheral nervous system that includes the somatic parts of the cranial and spinal nerves and their ganglia and the peripheral sensory receptors. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000012)]",
    name="somatic nervous system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0000012#somatic-nervous-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000012"),
    synonyms=[
        "PNS - somatic",
        "somatic nervous system, somatic division",
        "somatic part of peripheral nervous system",
        "somatic peripheral nervous system",
    ],
)
OrganismSystem.somatic_sensory_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/somaticSensorySystem",
    definition="Is part of the somatic nervous system. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0003942)]",
    description="The sensory system for the sense of touch and pain. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0003942)]",
    name="somatic sensory system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0003942#somatosensory-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0003942"),
    synonyms=["somatosensory system", "system for detection of somatic senses"],
)
OrganismSystem.sympathetic_nervous_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/sympatheticNervousSystem",
    definition="Is an anatomical entity. Is part of the autonomic nervous system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000013) ('is_a' and 'relationship')]",
    description="The sympathetic nervous system is one of the two divisions of the vertebrate autonomic nervous system (the other being the parasympathetic nervous system). The sympathetic preganglionic neurons have their cell bodies in the thoracic and lumbar regions of the spinal cord and connect to the paravertebral chain of sympathetic ganglia. Innervate heart and blood vessels, sweat glands, viscera and the adrenal medulla. Most sympathetic neurons, but not all, use noradrenaline as a post-ganglionic neurotransmitter. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0000013)]",
    name="sympathetic nervous system",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0000013#sympathetic-nervous-system-1"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000013"),
    synonyms=[
        "pars sympathica divisionis autonomici systematis nervosi",
        "sympathetic part of autonomic division of nervous system",
    ],
)
OrganismSystem.vascular_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/vascularSystem",
    definition="The 'vascular system' is an anatomical system that consists of all vessels in the body, and carries blood and lymph through all parts of the body.",
    name="vascular system",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0726589"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0007798#vascular-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0007798"),
)
OrganismSystem.ventricular_system_of_brain = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/ventricularSystemOfBrain",
    definition="Is an anatomical system. Is part of the brain and the ventricular system of central nervous system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0005282) ('is_a' and 'relationship')]",
    name="ventricular system of brain",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0731568"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0005282#ventricular-system-of-brain"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0005282"),
    synonyms=["brain ventricular system"],
)
OrganismSystem.ventricular_system_of_central_nervous_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/ventricularSystemOfCentralNervousSystem",
    definition="Is an anatomical system. Is part of the central nervous system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0005281) ('is_a' and 'relationship')]",
    description="A set of structures containing cerebrospinal fluid in the brain. It is continuous with the central canal of the spinal cord. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0005281)]",
    name="ventricular system of central nervous system",
    preferred_cross_reference=IRI(
        "https://knowledge-space.org/wiki/UBERON:0005281#ventricular-system-of-central-nervous-system"
    ),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0005281"),
    synonyms=["CNS ventricular system", "ventricular system", "ventricular system of neuraxis"],
)
OrganismSystem.visual_processing_part_of_nervous_system = OrganismSystem(
    id="https://openminds.om-i.org/instances/organismSystem/visualProcessingPartOfNervousSystem",
    definition="Is an anatomical entity. Is part of the nervous system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0006794) ('is_a' and 'relationship')]",
    name="visual processing part of nervous system",
    preferred_cross_reference=IRI(
        "https://knowledge-space.org/wiki/UBERON:0006794#visual-processing-part-of-nervous-system"
    ),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0006794"),
)
