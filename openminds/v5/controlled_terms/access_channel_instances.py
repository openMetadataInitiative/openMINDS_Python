# this file was auto-generated!


from openminds.v5.controlled_terms.access_channel import AccessChannel


AccessChannel.hybrid_access = AccessChannel(
    id="https://openminds.om-i.org/instances/accessChannel/hybridAccess",
    definition="Access is provided both remotely through digital means and at a specific physical location.",
    name="hybrid access",
)

AccessChannel.physical_access = AccessChannel(
    id="https://openminds.om-i.org/instances/accessChannel/physicalAccess",
    definition="Access requires physical presence at a specific location.",
    name="physical access",
    synonyms=["in-person access", "on-premises access", "on-site access"],
)

AccessChannel.virtual_access = AccessChannel(
    id="https://openminds.om-i.org/instances/accessChannel/virtualAccess",
    definition="Refers to the ability of users to connect to, interact with, and utilize resources, systems, or other individuals remotely via digital interfaces.",
    name="virtual access",
    synonyms=["digital access", "online access"],
)
