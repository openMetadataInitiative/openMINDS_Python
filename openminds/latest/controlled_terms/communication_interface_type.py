"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class CommunicationInterfaceType(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/CommunicationInterfaceType"
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
            description="Longer statement or account giving the characteristics of the communication interface type.",
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
            description="Word or phrase that constitutes the distinctive designation of the communication interface type.",
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


CommunicationInterfaceType.command_line_interface = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/commandLineInterface",
    definition="A means of interacting with software through text-based commands entered in a terminal or shell.",
    name="command line interface",
    synonyms=["CLI"],
)
CommunicationInterfaceType.desktop_gui = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/desktopGUI",
    definition="A graphical user interface that runs as a native application on a desktop computer.",
    name="desktop GUI",
    synonyms=["desktop graphical user interface", "desktop application"],
)
CommunicationInterfaceType.email_communication = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/emailCommunication",
    definition="A means of interacting with a service through sending and receiving e-mail.",
    name="email communication",
    synonyms=["e-mail communication", "email interface", "e-mail interface"],
)
CommunicationInterfaceType.library_api = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/libraryAPI",
    definition="An application programming interface implemented as a library for a specific programming language.",
    name="library API",
    synonyms=["programming language API"],
)
CommunicationInterfaceType.message_queue = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/messageQueue",
    definition="A means of interacting with a software system by sending messages to a buffer from which they may be retrieved at a later time.",
    name="message queue",
)
CommunicationInterfaceType.mobile_gui = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/mobileGUI",
    definition="A graphical user interface that runs as a native app on a mobile phone.",
    name="mobile GUI",
    synonyms=["mobile graphical user interface"],
)
CommunicationInterfaceType.osapi = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/OSAPI",
    definition="An application programming interface that allows applications to interact with the underlying operating system.",
    name="OS API",
    synonyms=["operating system API"],
)
CommunicationInterfaceType.restapi = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/RESTAPI",
    definition="An application programming interface that conforms to the representational state transfer (REST) architectural style, typically using the HTTP(S) protocol with JSON or XML documents.",
    name="REST API",
    synonyms=["RESTful API", "Representational State Transfer API"],
)
CommunicationInterfaceType.rpcapi = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/RPCAPI",
    definition="An application programming interface that allows remote functions in external servers to be called as if they were local functions.",
    name="RPC API",
    synonyms=["Remote Procedure Call API"],
)
CommunicationInterfaceType.soapapi = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/SOAPAPI",
    definition="An application programming interface that uses the Simple Object Access Protocol (SOAP).",
    name="SOAP API",
    synonyms=["Simple Object Access Protocol API"],
)
CommunicationInterfaceType.web_gui = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/webGUI",
    definition="A graphical user interface that runs in a web browser, typically implemented in HTML, Javascript and CSS.",
    name="web GUI",
    synonyms=["web-browser interface", "web-based graphical user interface"],
)
CommunicationInterfaceType.web_socket_api = CommunicationInterfaceType(
    id="https://openminds.om-i.org/instances/communicationInterfaceType/webSocketAPI",
    definition="An application programming interface based on exchanging messages between a client application and a server using web sockets.",
    name="web socket API",
)
