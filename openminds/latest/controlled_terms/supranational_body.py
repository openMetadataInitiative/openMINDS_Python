"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class SupranationalBody(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SupranationalBody"
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
            description="Longer statement or account giving the characteristics of the supranational body.",
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
            description="Word or phrase that constitutes the distinctive designation of the supranational body.",
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


SupranationalBody.arab_maghreb_union = SupranationalBody(
    id="https://openminds.om-i.org/instances/SupranationalBody/ArabMaghrebUnion",
    definition="Trade agreement among Arab countries. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q370862)]",
    name="Arab Maghreb Union",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q370862"),
    synonyms=["AMU"],
)
SupranationalBody.covax = SupranationalBody(
    id="https://openminds.om-i.org/instances/SupranationalBody/COVAX",
    definition="Global vaccine alliance regarding the COVID-19 pandemic. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q99360983)]",
    name="COVAX",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q99360983"),
    synonyms=[
        "COVAX Facility",
        "COVAX Global Vaccines Facility",
        "COVAX initiative",
        "COVID-19 Vaccines Global Access",
        "Covid-19 vaccine allocation plan",
        "COVAX programma",
    ],
)
SupranationalBody.european_economic_area = SupranationalBody(
    id="https://openminds.om-i.org/instances/SupranationalBody/EuropeanEconomicArea",
    definition="Area of the European Union's internal market and some of EFTA states established in 1994. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q8932)]",
    name="European Economic Area",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q8932"),
    synonyms=["EEA"],
)
SupranationalBody.european_union = SupranationalBody(
    id="https://openminds.om-i.org/instances/SupranationalBody/EuropeanUnion",
    definition="Political and economic union of 27 European states. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q458)]",
    name="European Union",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q458"),
    synonyms=[
        "An tAontas Eorpach",
        "Den Europæiske Union",
        "E.U.",
        "Eiropas Savienība",
        "EU",
        "eu",
        "Euroopa Liit",
        "Euroopan unioni",
        "Europeiska unionen",
        "Europese Unie",
        "Europos Sąjunga",
        "Europska unija",
        "Europäische Union",
        "Európai Unió",
        "Európska únia",
        "Evropska unija",
        "Evropská unie",
        "Unia Europejska",
        "Union européenne",
        "Unione Europea",
        "Uniunea Europeană",
        "União Europeia",
        "Unión Europea",
        "Unjoni Ewropea",
    ],
)
SupranationalBody.nordic_council = SupranationalBody(
    id="https://openminds.om-i.org/instances/SupranationalBody/NordicCouncil",
    definition="Geo-political inter-parliamentary forum for co-operation between the Nordic countries. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q146165)]",
    name="Nordic Council",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q146165"),
    synonyms=["Nordic cooperation", "The Nordic Council"],
)
SupranationalBody.provisional_world_government = SupranationalBody(
    id="https://openminds.om-i.org/instances/SupranationalBody/ProvisionalWorldGovernment",
    definition="World Government in Provisional stage. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q119439372)]",
    name="Provisional World Government",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q119439372"),
    synonyms=[
        "Provisional World Government for the Federation of Earth",
        "Transitional World Government",
        "World Government for the Federation of Earth",
    ],
)
SupranationalBody.the_mahdi_servants_union = SupranationalBody(
    id="https://openminds.om-i.org/instances/SupranationalBody/TheMahdiServantsUnion",
    definition="International non-governmental organization. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q96979217)]",
    name="The Mahdi Servants Union",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q96979217"),
    synonyms=["Khoddam Al-Mahdi", "MSU"],
)
SupranationalBody.union_state = SupranationalBody(
    id="https://openminds.om-i.org/instances/SupranationalBody/UnionState",
    definition="Supranational entity consisting of the Russian Federation and the Republic of Belarus. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q166110)]",
    name="Union State",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q166110"),
    synonyms=["Union State of Russia and Belarus"],
)
SupranationalBody.west_african_examinations_council = SupranationalBody(
    id="https://openminds.om-i.org/instances/SupranationalBody/WestAfricanExaminationsCouncil",
    definition="Is an examination board established in the public interest to conduct exams and award certificates in English-speaking West African countries. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/West_African_Examinations_Council)]",
    name="West African Examinations Council",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q2993835"),
    synonyms=["WAEC", "West African Examination Council", "West African Exams Council"],
)
