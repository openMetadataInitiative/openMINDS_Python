"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class OrganismSubstance(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/OrganismSubstance"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "v4.0"

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
            description="Longer statement or account giving the characteristics of the organism substance.",
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
            description="Word or phrase that constitutes the distinctive designation of the organism substance.",
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


OrganismSubstance.arterial_blood = OrganismSubstance(
    id="https://openminds.om-i.org/instances/organismSubstance/arterialBlood",
    definition="'Arterial blood' is the oxygenated portion of blood which occupies the pulmonary vein, the left chambers of the heart, and the arteries of the circulatory system.",
    description="Blood that flows through an artery.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0725460"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/UBERON:0013755#arterial-blood"),
    name="arterial blood",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0013755"),
    synonyms=["arterial blood", "blood in artery", "portion of arterial blood"],
)
OrganismSubstance.blood = OrganismSubstance(
    id="https://openminds.om-i.org/instances/organismSubstance/blood",
    definition="''Blood' is a body fluid in the circulatory system of vertebrates that transports substances to and from cells (e.g. nutrients, oxygen or metabolic waste products). [[adapted from Wikipedia](https://en.wikipedia.org/wiki/Blood)]",
    description="A bodily fluid that is composed of blood plasma and erythrocytes (blood cells).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0101354"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/UBERON:0000178#blood"),
    name="blood",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0000178"),
    synonyms=["portion of blood", "vertebrate blood"],
)
OrganismSubstance.cerebrospinal_fluid = OrganismSubstance(
    id="https://openminds.om-i.org/instances/organismSubstance/cerebrospinalFluid",
    definition="'cerebrospinal fluid' is a clear, colorless, bodily fluid, that occupies the subarachnoid space and the ventricular system around and inside the brain and spinal cord [WP, modified]. [http://en.wikipedia.org/wiki/Cerebrospinal_fluid]",
    description="The fluid that is contained within the brain ventricles, the subarachnoid space and the central canal of the spinal cord (NCI). Transudate contained in the subarachnoid space (UWDA). Clear colorless liquid secreted by the choroid plexus of the lateral, third, and fourth ventricles, and contained within the ventricular system of the brain and spinal cord and within the subarachnoid space (CSP).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0101997"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/#cerebral-spinal-fluid"),
    name="cerebrospinal fluid",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001359"),
    synonyms=["CSF", "cerebral spinal fluid", "liquor cerebrospinalis", "spinal fluid"],
)
OrganismSubstance.venous_blood = OrganismSubstance(
    id="https://openminds.om-i.org/instances/organismSubstance/venousBlood",
    definition="'Venous blood' is deoxygenated blood which travels from the peripheral vessels, through the venous system into the right atrium of the heart.",
    description="Blood that flows through a vein.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0734397"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/UBERON:0013756#venous-blood"),
    name="venous blood",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0013756"),
    synonyms=["blood in vein", "portion of venous blood", "venous blood"],
)
