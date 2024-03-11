"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class PatchClampVariation(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/PatchClampVariation"
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


PatchClampVariation.cell_attached_patch = PatchClampVariation(
    id="https://openminds.ebrains.eu/instances/patchClampVariation/cellAttachedPatch",
    definition="A variation of the patch-clamp technique in which the cell membrane remains intact.",
    description="For this method, the pipette is sealed onto the cell membrane to obtain a gigaseal (a seal with electrical resistance on the order of a gigaohm), while ensuring that the cell membrane remains intact. This allows the recording of currents through single, or a few, ion channels contained in the patch of membrane captured by the pipette. By only attaching to the exterior of the cell membrane, there is very little disturbance of the cell structure. Also, by not disrupting the interior of the cell, any intracellular mechanisms normally influencing the channel will still be able to function as they would physiologically. [Wikipedia]",
    name="cell-attached patch",
)
PatchClampVariation.inside_out_patch = PatchClampVariation(
    id="https://openminds.ebrains.eu/instances/patchClampVariation/insideOutPatch",
    definition="A variation of the patch-clamp technique in which a patch of membrane is excised and the cytosolic surface exposed.",
    description="In the inside-out method, a patch of the membrane is attached to the patch pipette, detached from the rest of the cell, and the cytosolic surface of the membrane is exposed to the external media, or bath. One advantage of this method is that the experimenter has access to the intracellular surface of the membrane via the bath and can change the chemical composition of what the inside surface of the membrane is exposed to. This is useful when an experimenter wishes to manipulate the environment at the intracellular surface of single ion channels. [Wikipedia]",
    name="inside-out patch",
)
PatchClampVariation.loose_patch = PatchClampVariation(
    id="https://openminds.ebrains.eu/instances/patchClampVariation/loosePatch",
    definition="A variation of the patch-clamp technique involving a seal with low electrical resistance.",
    description="This technique employs a loose seal (low electrical resistance) rather than the tight gigaseal used in the conventional technique. A significant advantage of the loose seal is that the pipette can be repeatedly removed from the membrane after recording, and the membrane will remain intact. This allows repeated measurements in a variety of locations on the same cell without destroying the integrity of the membrane. [Wikipedia]",
    name="loose patch",
)
PatchClampVariation.outside_out_patch = PatchClampVariation(
    id="https://openminds.ebrains.eu/instances/patchClampVariation/outsideOutPatch",
    definition="A variation of the patch-clamp technique in which a patch of membrane is excised and the external surface exposed.",
    description="The name 'outside-out' emphasizes both this technique's complementar­ity to the inside-out technique, and the fact that it places the external rather than intracellular surface of the cell membrane on the outside of the patch of membrane, in relation to the patch electrode. Outside-out patching gives the experimenter the opportunity to examine the properties of an ion channel when it is isolated from the cell and exposed successively to different solutions on the extracellular surface of the membrane. [Wikipedia]",
    name="outside-out patch",
)
PatchClampVariation.perforated_patch = PatchClampVariation(
    id="https://openminds.ebrains.eu/instances/patchClampVariation/perforatedPatch",
    definition="A variation of the patch-clamp technique in which the cell membrane is perforated.",
    description="This variation of the patch clamp method is very similar to the whole-cell configuration. The main difference lies in the fact that when the experimenter forms the gigaohm seal, suction is not used to rupture the patch membrane. Instead, the electrode solution contains small amounts of an antifungal or antibiotic agent which diffuses into the membrane patch and forms small pores in the membrane, providing electrical access to the cell interior. [Wikipedia]",
    name="perforated patch",
)
PatchClampVariation.whole_cell_patch = PatchClampVariation(
    id="https://openminds.ebrains.eu/instances/patchClampVariation/wholeCellPatch",
    definition="A variation of the patch-clamp technique in which the patch is ruptured, giving access to the intracellular space.",
    description="Whole-cell recordings involve recording currents through multiple channels simultaneously, over a large region of the cell membrane. The electrode is left in place on the cell, as in cell-attached recordings, but more suction is applied to rupture the membrane patch, thus providing access from the interior of the pipette to the intracellular space of the cell. This provides a means to administer and study how treatments (e.g. drugs) can affect cells in real time. [Wikipedia]",
    name="whole-cell patch",
    synonyms=["whole-cell recording"],
)
