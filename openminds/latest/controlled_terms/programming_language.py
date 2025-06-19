"""
Structured information on the programming language.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ProgrammingLanguage(LinkedMetadata):
    """
    Structured information on the programming language.
    """

    type_ = "https://openminds.om-i.org/types/ProgrammingLanguage"
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
            description="Longer statement or account giving the characteristics of the programming language.",
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
            description="Word or phrase that constitutes the distinctive designation of the programming language.",
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


ProgrammingLanguage.ampl = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/AMPL",
    name="AMPL",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q295250"),
    synonyms=["A Mathematical Programming Language"],
)
ProgrammingLanguage.bash = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/Bash",
    name="Bash",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q189248"),
)
ProgrammingLanguage.c = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/C",
    name="C",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q15777"),
)
ProgrammingLanguage.cplusplus = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/C++",
    name="C++",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q2407"),
)
ProgrammingLanguage.csharp = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/C#",
    name="C#",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q2370"),
)
ProgrammingLanguage.fortran = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/Fortran",
    name="Fortran",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q83303"),
)
ProgrammingLanguage.glsl = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/GLSL",
    name="GLSL",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q779819"),
)
ProgrammingLanguage.html = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/HTML",
    name="HTML",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q8811"),
)
ProgrammingLanguage.igor_pro = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/IGORPro",
    definition="C-like programming language of the correspondent scientific data analysis software and numerical computing environment IGOR Pro available for Windows or Mac operating systems.",
    name="IGOR Pro",
    synonyms=["IGOR Pro programming language"],
)
ProgrammingLanguage.java = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/Java",
    name="Java",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q251"),
)
ProgrammingLanguage.java_script = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/JavaScript",
    name="JavaScript",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q2005"),
)
ProgrammingLanguage.matlab = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/MATLAB",
    name="MATLAB",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q37805571"),
)
ProgrammingLanguage.pascal = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/Pascal",
    name="Pascal",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q81571"),
)
ProgrammingLanguage.php = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/PHP",
    name="PHP",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q59"),
)
ProgrammingLanguage.python = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/Python",
    name="Python",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q28865"),
)
ProgrammingLanguage.r = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/R",
    name="R",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q206904"),
)
ProgrammingLanguage.ruby = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/Ruby",
    name="Ruby",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q161053"),
)
ProgrammingLanguage.scala = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/Scala",
    name="Scala",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q460584"),
)
ProgrammingLanguage.shell = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/shell",
    name="Shell",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q14663"),
)
ProgrammingLanguage.t_sql = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/T-SQL",
    name="T-SQL",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q1411245"),
)
ProgrammingLanguage.type_script = ProgrammingLanguage(
    id="https://openminds.om-i.org/instances/programmingLanguage/TypeScript",
    name="TypeScript",
    preferred_ontology_identifier=IRI("https://www.wikidata.org/entity/Q978185"),
)
