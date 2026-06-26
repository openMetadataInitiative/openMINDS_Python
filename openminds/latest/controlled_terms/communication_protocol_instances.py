# this file was auto-generated!


from openminds.base import IRI

from openminds.latest.controlled_terms.communication_protocol import CommunicationProtocol


CommunicationProtocol.http = CommunicationProtocol(
    id="https://openminds.om-i.org/instances/communicationProtocol/HTTP",
    definition="A network communication protocol used for exchanging hypermedia documents, primarily between web servers and browsers.",
    description="For more information please go to the [HTTP Documentation](https://httpwg.org/specs/).",
    name="HTTP",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q8777"),
    synonyms=["Hypertext Transfer Protocol"],
)

CommunicationProtocol.https = CommunicationProtocol(
    id="https://openminds.om-i.org/instances/communicationProtocol/HTTPS",
    definition="A network communication protocol that secures HTTP traffic by encrypting it using SSL/TLS.",
    name="HTTPS",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q44484"),
    synonyms=["Hypertext Transfer Protocol Secure"],
)

CommunicationProtocol.ssh = CommunicationProtocol(
    id="https://openminds.om-i.org/instances/communicationProtocol/SSH",
    definition="A network communication protocol that enables secure remote login and command execution over unsecured networks.",
    name="SSH",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q170460"),
    synonyms=["Secure Shell"],
)

CommunicationProtocol.tcp_ip = CommunicationProtocol(
    id="https://openminds.om-i.org/instances/communicationProtocol/TCP_IP",
    definition="A network communication protocol suite that defines how data is transmitted across interconnected networks.",
    name="TCP/IP",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q81414"),
    synonyms=["Internet Protocol suite", "IP suite", "TCP-IP", "Transmission Control Protocol / Internet Protocol"],
)

CommunicationProtocol.web_socket = CommunicationProtocol(
    id="https://openminds.om-i.org/instances/communicationProtocol/WebSocket",
    definition="A computer communications protocol, providing a bidirectional communication channel over a single Transmission Control Protocol (TCP) connection.",
    description="For more information please go to the [WebSocket documentation](https://www.rfc-editor.org/rfc/rfc6455) provided by the Internet Engineering Task Force (IETF).",
    name="WebSocket",
    preferred_cross_reference=IRI("https://www.wikidata.org/entity/Q859938"),
    synonyms=["WebSocket protocol"],
)
