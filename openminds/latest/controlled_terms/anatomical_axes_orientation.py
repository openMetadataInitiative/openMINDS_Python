"""
Structured information on the anatomical directions of the X, Y, and Z axis.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class AnatomicalAxesOrientation(LinkedMetadata):
    """
    Structured information on the anatomical directions of the X, Y, and Z axis.
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/AnatomicalAxesOrientation"
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


AnatomicalAxesOrientation.ail = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/AIL",
    definition="X, Y, Z axes are oriented towards anterior, inferior and left, respectively.",
    name="AIL",
)
AnatomicalAxesOrientation.air = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/AIR",
    definition="X, Y, Z axes are oriented towards anterior, inferior and right, respectively.",
    name="AIR",
)
AnatomicalAxesOrientation.ali = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/ALI",
    definition="X, Y, Z axes are oriented towards anterior, left and inferior, respectively.",
    name="ALI",
)
AnatomicalAxesOrientation.als = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/ALS",
    definition="X, Y, Z axes are oriented towards anterior, left and superior, respectively.",
    name="ALS",
)
AnatomicalAxesOrientation.ari = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/ARI",
    definition="X, Y, Z axes are oriented towards anterior, right and inferior, respectively.",
    name="ARI",
)
AnatomicalAxesOrientation.ars = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/ARS",
    definition="X, Y, Z axes are oriented towards anterior, right and superior, respectively.",
    name="ARS",
)
AnatomicalAxesOrientation.asl = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/ASL",
    definition="X, Y, Z axes are oriented towards anterior, superior and left, respectively.",
    name="ASL",
)
AnatomicalAxesOrientation.asr = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/ASR",
    definition="X, Y, Z axes are oriented towards anterior, superior and right, respectively.",
    name="ASR",
)
AnatomicalAxesOrientation.ial = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/IAL",
    definition="X, Y, Z axes are oriented towards inferior, anterior and left, respectively.",
    name="IAL",
)
AnatomicalAxesOrientation.iar = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/IAR",
    definition="X, Y, Z axes are oriented towards inferior, anterior and right, respectively.",
    name="IAR",
)
AnatomicalAxesOrientation.ila = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/ILA",
    definition="X, Y, Z axes are oriented towards inferior, left and anterior, respectively.",
    name="ILA",
)
AnatomicalAxesOrientation.ilp = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/ILP",
    definition="X, Y, Z axes are oriented towards inferior, left and posterior, respectively.",
    name="ILP",
)
AnatomicalAxesOrientation.ipl = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/IPL",
    definition="X, Y, Z axes are oriented towards inferior, posterior and left, respectively.",
    name="IPL",
)
AnatomicalAxesOrientation.ipr = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/IPR",
    definition="X, Y, Z axes are oriented towards inferior, posterior and right, respectively.",
    name="IPR",
)
AnatomicalAxesOrientation.ira = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/IRA",
    definition="X, Y, Z axes are oriented towards inferior, right and anterior, respectively.",
    name="IRA",
)
AnatomicalAxesOrientation.irp = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/IRP",
    definition="X, Y, Z axes are oriented towards inferior, right and posterior, respectively.",
    name="IRP",
)
AnatomicalAxesOrientation.lai = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/LAI",
    definition="X, Y, Z axes are oriented towards left, anterior and inferior, respectively.",
    name="LAI",
)
AnatomicalAxesOrientation.las = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/LAS",
    definition="X, Y, Z axes are oriented towards left, anterior and superior, respectively.",
    name="LAS",
)
AnatomicalAxesOrientation.lia = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/LIA",
    definition="X, Y, Z axes are oriented towards left, inferior and anterior, respectively.",
    name="LIA",
)
AnatomicalAxesOrientation.lip = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/LIP",
    definition="X, Y, Z axes are oriented towards left, inferior and posterior, respectively.",
    name="LIP",
)
AnatomicalAxesOrientation.lpi = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/LPI",
    definition="X, Y, Z axes are oriented towards left, posterior and inferior, respectively.",
    name="LPI",
)
AnatomicalAxesOrientation.lps = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/LPS",
    definition="X, Y, Z axes are oriented towards left, posterior and superior, respectively.",
    name="LPS",
)
AnatomicalAxesOrientation.lsa = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/LSA",
    definition="X, Y, Z axes are oriented towards left, superior and anterior, respectively.",
    name="LSA",
)
AnatomicalAxesOrientation.lsp = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/LSP",
    definition="X, Y, Z axes are oriented towards left, superior and posterior, respectively.",
    name="LSP",
)
AnatomicalAxesOrientation.pil = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/PIL",
    definition="X, Y, Z axes are oriented towards posterior, inferior and left, respectively.",
    name="PIL",
)
AnatomicalAxesOrientation.pir = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/PIR",
    definition="X, Y, Z axes are oriented towards posterior, inferior and right, respectively.",
    name="PIR",
)
AnatomicalAxesOrientation.pli = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/PLI",
    definition="X, Y, Z axes are oriented towards posterior, left and inferior, respectively.",
    name="PLI",
)
AnatomicalAxesOrientation.pls = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/PLS",
    definition="X, Y, Z axes are oriented towards posterior, left and superior, respectively.",
    name="PLS",
)
AnatomicalAxesOrientation.pri = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/PRI",
    definition="X, Y, Z axes are oriented towards posterior, right and inferior, respectively.",
    name="PRI",
)
AnatomicalAxesOrientation.prs = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/PRS",
    definition="X, Y, Z axes are oriented towards posterior, right and superior, respectively.",
    name="PRS",
)
AnatomicalAxesOrientation.psl = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/PSL",
    definition="X, Y, Z axes are oriented towards posterior, superior and left, respectively.",
    name="PSL",
)
AnatomicalAxesOrientation.psr = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/PSR",
    definition="X, Y, Z axes are oriented towards posterior, superior and right, respectively.",
    name="PSR",
)
AnatomicalAxesOrientation.rai = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/RAI",
    definition="X, Y, Z axes are oriented towards right, anterior and inferior, respectively.",
    name="RAI",
)
AnatomicalAxesOrientation.ras = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/RAS",
    definition="X, Y, Z axes are oriented towards right, anterior and superior, respectively.",
    name="RAS",
)
AnatomicalAxesOrientation.ria = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/RIA",
    definition="X, Y, Z axes are oriented towards right, inferior and anterior, respectively.",
    name="RIA",
)
AnatomicalAxesOrientation.rip = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/RIP",
    definition="X, Y, Z axes are oriented towards right, inferior and posterior, respectively.",
    name="RIP",
)
AnatomicalAxesOrientation.rpi = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/RPI",
    definition="X, Y, Z axes are oriented towards right, posterior and inferior, respectively.",
    name="RPI",
)
AnatomicalAxesOrientation.rps = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/RPS",
    definition="X, Y, Z axes are oriented towards right, posterior and superior, respectively.",
    name="RPS",
)
AnatomicalAxesOrientation.rsa = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/RSA",
    definition="X, Y, Z axes are oriented towards right, superior and anterior, respectively.",
    name="RSA",
)
AnatomicalAxesOrientation.rsp = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/RSP",
    definition="X, Y, Z axes are oriented towards right, superior and posterior, respectively.",
    name="RSP",
)
AnatomicalAxesOrientation.sal = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/SAL",
    definition="X, Y, Z axes are oriented towards superior, anterior and left, respectively.",
    name="SAL",
)
AnatomicalAxesOrientation.sar = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/SAR",
    definition="X, Y, Z axes are oriented towards superior, anterior and right, respectively.",
    name="SAR",
)
AnatomicalAxesOrientation.sla = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/SLA",
    definition="X, Y, Z axes are oriented towards superior, left and anterior, respectively.",
    name="SLA",
)
AnatomicalAxesOrientation.slp = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/SLP",
    definition="X, Y, Z axes are oriented towards superior, left and posterior, respectively.",
    name="SLP",
)
AnatomicalAxesOrientation.spl = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/SPL",
    definition="X, Y, Z axes are oriented towards superior, posterior and left, respectively.",
    name="SPL",
)
AnatomicalAxesOrientation.spr = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/SPR",
    definition="X, Y, Z axes are oriented towards superior, posterior and right, respectively.",
    name="SPR",
)
AnatomicalAxesOrientation.sra = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/SRA",
    definition="X, Y, Z axes are oriented towards superior, right and anterior, respectively.",
    name="SRA",
)
AnatomicalAxesOrientation.srp = AnatomicalAxesOrientation(
    id="https://openminds.ebrains.eu/instances/anatomicalAxesOrientation/SRP",
    definition="X, Y, Z axes are oriented towards superior, right and posterior, respectively.",
    name="SRP",
)
