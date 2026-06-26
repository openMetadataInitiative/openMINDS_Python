# this file was auto-generated!


from openminds.v5.controlled_terms.communication_interface_type import CommunicationInterfaceType


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
