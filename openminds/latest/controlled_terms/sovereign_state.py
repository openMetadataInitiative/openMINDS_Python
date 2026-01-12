"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class SovereignState(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/SovereignState"
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
            description="Longer statement or account giving the characteristics of the sovereign state.",
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
            description="Word or phrase that constitutes the distinctive designation of the sovereign state.",
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


SovereignState.afghanistan = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Afghanistan",
    definition="Country in Central and South Asia. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q889)]",
    name="Afghanistan",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q889"),
    synonyms=[
        "AF",
        "Affghanistan",
        "Affghanisthan",
        "Affghaunistan",
        "AFG",
        "Afghania",
        "Afghaunistan",
        "Afghaunistaun",
    ],
)
SovereignState.albania = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Albania",
    definition="Country in southeastern Europe. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q222)]",
    name="Albania",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q222"),
    synonyms=[
        "AL",
        "ALB",
        "People's Republic of Albania",
        "People's Socialist Republic of Albania",
        "Republic of Albania",
        "Republika e Shqipërisë",
        "Republika Popullore e Shqiperise",
        "Republika Popullore Socialiste e Shqiperise",
        "Shqipërisë",
    ],
)
SovereignState.algeria = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Algeria",
    definition="Country in North Africa. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q262)]",
    name="Algeria",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q262"),
    synonyms=["ALG", "Djazaïr", "dz", "DZ", "DZA", "Dzayer", "People's Democratic Republic of Algeria"],
)
SovereignState.andorra = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Andorra",
    definition="Sovereign microstate between France and Spain, in Western Europe. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q228)]",
    name="Andorra",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q228"),
    synonyms=["AD", "AND", "Andorra", "Principality of Andorra", "Principality of the Valleys of Andorra"],
)
SovereignState.angola = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Angola",
    definition="Country on the west coast of Southern Africa. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q916)]",
    name="Angola",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q916"),
    synonyms=["AGO", "ANG", "Angola", "AO", "ao", "Ngola", "Republic of Angola", "República de Angola"],
)
SovereignState.antigua_and_barbuda = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/AntiguaAndBarbuda",
    definition="Island sovereign state in the Caribbean Sea. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q781)]",
    name="Antigua and Barbuda",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q781"),
    synonyms=["A&B", "Aanteega an' Baabyuuda", "AG", "ag", "ANT", "Antigua and Barbuda", "ATG"],
)
SovereignState.argentina = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Argentina",
    definition="Country in South America. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q414)]",
    name="Argentina",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q414"),
    synonyms=[
        "AR",
        "ARG",
        "Argentine Republic",
        "Republic of Argentina",
        "Republica Argentina",
        "República Argentina",
    ],
)
SovereignState.armenia = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Armenia",
    definition="Sovereign state in the South Caucasus region of Eurasia. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q399)]",
    name="Armenia",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q399"),
    synonyms=["AM", "ARM", "Hayastan", "Hayastani Hanrapetut’yun", "Republic of Armenia"],
)
SovereignState.australia = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Australia",
    definition="Country in Oceania. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q408)]",
    name="Australia",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q408"),
    synonyms=[
        "AU",
        "AUS",
        "Aussieland",
        "Commonwealth of Australia",
        "Down Under",
        "New Holland",
        "New Hollandia",
        "Nova Hollandia",
        "Oz",
        "Stralia",
        "Straya",
        "Stria",
        "The Commonwealth of Australia",
    ],
)
SovereignState.austria = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Austria",
    definition="Country in Central Europe. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q40)]",
    name="Austria",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q40"),
    synonyms=["AT", "AUT", "Republic of Austria", "Republik Österreich", "Österreich"],
)
SovereignState.azerbaijan = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Azerbaijan",
    definition="Country in the Caucasus in Eastern Europe and Western Asia. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q227)]",
    name="Azerbaijan",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q227"),
    synonyms=["AZ", "az", "AZE", "Azərbaycan", "Azərbaycan Respublikası", "Republic of Azerbaijan"],
)
SovereignState.bahrain = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Bahrain",
    definition="Country in the Persian Gulf. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q398)]",
    name="Bahrain",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q398"),
    synonyms=[
        "BAH",
        "Bahrein Islands",
        "bh",
        "BH",
        "BHR",
        "Dawlat al-Bahrain",
        "Kingdom of Bahrain",
        "Mamlakat al-Baḥrayn",
    ],
)
SovereignState.bangladesh = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Bangladesh",
    definition="Country in South Asia. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q902)]",
    name="Bangladesh",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q902"),
    synonyms=[
        "BAN",
        "Bangla Desh",
        "BD",
        "bd",
        "BGD",
        "Country of Bengal",
        "Land of Bengal",
        "People's Republic of Bangladesh",
    ],
)
SovereignState.barbados = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Barbados",
    definition="Island nation in the Caribbean. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q244)]",
    name="Barbados",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q244"),
    synonyms=["BAR", "Barbadoes", "bb", "BB", "BRB"],
)
SovereignState.belarus = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Belarus",
    definition="Country in Eastern Europe. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q184)]",
    name="Belarus",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q184"),
    synonyms=[
        "Belorussia",
        "Bielaruś",
        "Bielorussia",
        "BLR",
        "BY",
        "by",
        "Byeloruss",
        "Byelorussia",
        "Republic of Belarus",
        "Respublika Belarus'",
        "Respublika Bielaruś",
        "White Russia",
        "White Ruthenia",
    ],
)
SovereignState.belgium = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Belgium",
    definition="Country in western Europe. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q31)]",
    name="Belgium",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q31"),
    synonyms=[
        "be",
        "BE",
        "BEL",
        "Kingdom of Belgium",
        "Koninkrijk België",
        "Königreich Belgien",
        "Royaume de Belgique",
    ],
)
SovereignState.belize = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Belize",
    definition="Sovereign state in Central America. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q242)]",
    name="Belize",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q242"),
    synonyms=["Belize", "BLZ", "bz", "BZ"],
)
SovereignState.benin = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Benin",
    definition="Sovereign state in West Africa. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q962)]",
    name="Benin",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q962"),
    synonyms=["BEN", "BJ", "Dahomey", "Republic of Benin"],
)
SovereignState.bhutan = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Bhutan",
    definition="Sovereign state in South Asia. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q917)]",
    name="Bhutan",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q917"),
    synonyms=["BHU", "bt", "BT", "BTN", "Kingdom of Bhutan"],
)
SovereignState.bolivia = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Bolivia",
    definition="Sovereign state in South America. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q750)]",
    name="Bolivia",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q750"),
    synonyms=[
        "BO",
        "bo",
        "bol",
        "BOL",
        "Buliwya Achka nasyunkunap Mama llaqta",
        "Estado Plurinacional de Bolivia",
        "Plurinational State of Bolivia",
        "Republic of Bolivia",
        "Tetã Volívia",
        "Wuliwya Suyu",
    ],
)
SovereignState.bosnia_and_herzegovina = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/BosniaAndHerzegovina",
    definition="Country in Southeast Europe. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q225)]",
    name="Bosnia and Herzegovina",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q225"),
    synonyms=[
        "B&H",
        "BA",
        "ba",
        "BIH",
        "BiH",
        "Bosna i Hercegovina",
        "Bosnia",
        "Bosnia & Herzegovina",
        "Bosnia and Hercegovina",
        "Bosnia-Herzegovina",
    ],
)
SovereignState.botswana = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Botswana",
    definition="Sovereign state in Southern Africa. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q963)]",
    name="Botswana",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q963"),
    synonyms=["BOT", "Botswana", "bw", "BW", "BWA", "Lefatshe la Botswana", "Republic of Botswana"],
)
SovereignState.brazil = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Brazil",
    definition="Country in South America. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q155)]",
    name="Brazil",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q155"),
    synonyms=["br", "BR", "BRA", "Brasil", "Federative Republic of Brazil", "República Federativa do Brasil"],
)
SovereignState.brunei = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Brunei",
    definition="Sovereign country and sultanate on the island of Borneo in south-east Asia, member of the Commonwealth of Nations. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q921)]",
    name="Brunei",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q921"),
    synonyms=[
        "bn",
        "BN",
        "BRN",
        "BRU",
        "Brunei Darussalam",
        "Nation of Brunei, the Abode of Peace",
        "Negara Brunei Darussalam",
    ],
)
SovereignState.bulgaria = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Bulgaria",
    definition="Country in Southeast Europe. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q219)]",
    name="Bulgaria",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q219"),
    synonyms=["BG", "bg", "BGR", "BUL", "Republic of Bulgaria"],
)
SovereignState.burkina_faso = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/BurkinaFaso",
    definition="Sovereign state in Africa. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q965)]",
    name="Burkina Faso",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q965"),
    synonyms=["BF", "bf", "BFA", "Burkina Faso", "Republic of Burkina Faso", "Republic of Upper Volta (-1984)"],
)
SovereignState.burundi = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Burundi",
    definition="Sovereign state in Africa. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q967)]",
    name="Burundi",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q967"),
    synonyms=["BDI", "BI", "bi", "Gouvernement du Burundi", "Republic of Burundi", "Republika y'Uburundi", "Uburundi"],
)
SovereignState.cambodia = SovereignState(
    id="https://openminds.om-i.org/instances/SovereignState/Cambodia",
    definition="Country in Southeast Asia. [auto-generated from 'schema:description' property of the [Wikidata entity](http://www.wikidata.org/entity/Q424)]",
    name="Cambodia",
    preferred_ontology_identifier=IRI("http://www.wikidata.org/entity/Q424"),
    synonyms=[
        "Camboya",
        "Campuchia",
        "Kambodzha",
        "Kamboja",
        "Kampuchea",
        "KH",
        "kh",
        "KHM",
        "Kingdom of Cambodia",
        "KKH",
    ],
)
