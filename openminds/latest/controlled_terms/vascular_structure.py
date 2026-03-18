"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class VascularStructure(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/VascularStructure"
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
            description="Longer statement or account giving the characteristics of the vascular structure.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of the vascular structure.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "other_cross_references",
            str,
            "otherCrossReference",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all internationalized resource identifiers (IRIs) pointing to cross-references to external databases or registries that are equivalent to this term (e.g., Wikidata). Do not repeat the preferred cross-reference.",
        ),
        Property(
            "other_ontology_identifiers",
            str,
            "otherOntologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter all internationalized resource identifiers (IRIs) pointing to ontology entries that are equivalent to this term (e.g., UBERON). Do not repeat the preferred ontology identifier.",
        ),
        Property(
            "preferred_cross_reference",
            IRI,
            "preferredCrossReference",
            description="no description available",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred cross-reference to an external database or registry (e.g., KnowledgeSpace).",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term (e.g., InterLex).",
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
        name=None,
        other_cross_references=None,
        other_ontology_identifiers=None,
        preferred_cross_reference=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            name=name,
            other_cross_references=other_cross_references,
            other_ontology_identifiers=other_ontology_identifiers,
            preferred_cross_reference=preferred_cross_reference,
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


VascularStructure.anterior_cerebral_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/anteriorCerebralVein",
    definition="Is a cerebral vein. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001672)]",
    name="anterior cerebral vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0001672#anterior-cerebral-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001672"),
)
VascularStructure.anterior_mesencephalic_central_artery = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/anteriorMesencephalicCentralArtery",
    definition="Is a central artery. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_2005052)]",
    description="Arteries that irrigate rostral regions of the midbrain. They extend between the Basial communicating artery to the anterior cerebral vein. Isogai et al. 2001. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_2005052)]",
    name="anterior mesencephalic central artery",
    preferred_cross_reference=IRI(
        "https://knowledge-space.org/wiki/UBERON:2005052#anterior-mesencephalic-central-artery"
    ),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_2005052"),
    synonyms=["AMCtA", "rostral mesencephalic central artery"],
)
VascularStructure.basal_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/basalVein",
    definition="Is a deep cerebral vein. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035530)]",
    description="The basal vein is formed at the anterior perforated substance by the union of (a) a small anterior cerebral vein which accompanies the anterior cerebral artery and supplies the medial surface of the frontal lobe by the fronto-basal vein. (b) the deep middle cerebral vein (deep Sylvian vein), which receives tributaries from the insula and neighboring gyri, and runs in the lower part of the lateral cerebral fissure, and (c) the inferior striate veins, which leave the corpus striatum through the anterior perforated substance. The basal vein passes backward around the cerebral peduncle, and ends in the internal cerebral vein; it receives tributaries from the interpeduncular fossa, the inferior horn of the lateral ventricle, the hippocampal gyrus, and the mid-brain. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035530)]",
    name="basal vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0035530#basal-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0035530"),
    synonyms=["basal vein of rosenthal", "rosenthal's vein"],
)
VascularStructure.brain_blood_vessel = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/brainBloodVessel",
    definition="Is part of the vasculature of brain. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0003499)]",
    description="A blood vessel that is part of a brain. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0003499)]",
    name="brain blood vessel",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0726967"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0003499#brain-blood-vessel"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0003499"),
    synonyms=["blood vessel of brain"],
)
VascularStructure.cavernous_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/cavernousSinus",
    definition="Is a venous dural sinus. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0003712)]",
    description="The cavernous sinus (or lateral sellar compartment), within the human head, is a large collection of thin-walled veins creating a cavity bordered by the temporal bone of the skull and the sphenoid bone, lateral to the sella turcica. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0003712)]",
    name="cavernous sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0003712#cavernous-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0003712"),
)
VascularStructure.central_artery = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/centralArtery",
    definition="Is a brain blood vessel. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_2005020)]",
    description="Arteries that irrigate the forebrain and midbrain Isogai et al. 2001. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_2005020)]",
    name="central artery",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:2005020#central-artery"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_2005020"),
    synonyms=["CtA"],
)
VascularStructure.central_retinal_artery = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/centralRetinalArtery",
    definition="Is a retina blood vessel. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001620)]",
    description="The central retinal artery (retinal artery) branches off the ophthalmic artery, running inferior to the optic nerve within its dural sheath to the eyeball. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001620)]",
    name="central retinal artery",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0001620#central-retinal-artery"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001620"),
    synonyms=["central artery of retina", "retinal artery", "Zinn's artery"],
)
VascularStructure.central_retinal_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/centralRetinalVein",
    definition="Is part of the cavernous sinus. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001673)]",
    description="The central retinal vein (retinal vein) is a short vein that runs through the optic nerve and drains blood from the capillaries of the retina into the larger veins outside the eye. The anatomy of the veins of the orbit of the eye varies between individuals, and in some the central retinal vein drains into the superior ophthalmic vein, and in some it drains directly into the cavernous sinus. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001673)]",
    name="central retinal vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0001673#central-retinal-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001673"),
    synonyms=["retinal vein"],
)
VascularStructure.cerebellar_central_artery = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/cerebellarCentralArtery",
    definition="Is a central artery. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_2005021)]",
    description="Extend upward from the PCS, branch to provide an arterial feed to the hindbrain, then drain back down into the PHBC Isogai et al. 2001. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_2005021)]",
    name="cerebellar central artery",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:2005021#cerebellar-central-artery"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_2005021"),
    synonyms=["CCtA"],
)
VascularStructure.cerebellum_vasculature = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/cerebellumVasculature",
    definition="Is a vasculature of central nervous system. Is part of the cerebellum. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0006694) ('is_a' and 'relationship')]",
    description="A vasculature that is part of a cerebellum. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0006694)]",
    name="cerebellum vasculature",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0729550"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0006694#cerebellum-vasculature"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0006694"),
)
VascularStructure.cerebral_blood_vessel = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/cerebralBloodVessel",
    definition="Is a brain blood vessel. Is part of the cerebellum. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0016565) ('is_a' and 'relationship')]",
    description="A blood vessel that is part of a cerebellum. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0016565)]",
    name="cerebral blood vessel",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0732836"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0016565#cerebral-blood-vessel"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0016565"),
)
VascularStructure.cerebral_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/cerebralVein",
    definition="Is a brain blood vessel. Is part of the telencephalon. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001663) ('is_a' and 'relationship')]",
    description="The cerebral veins are divisible into external and internal groups according to the outer surfaces or the inner parts of the hemispheres they drain into. The external veins are the superior cerebral veins, inferior cerebral veins, and middle cerebral vein. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001663)]",
    name="cerebral vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0001663#cerebral-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001663"),
)
VascularStructure.deep_cerebral_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/deepCerebralVein",
    definition="Is a cerebral vein. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0016564)]",
    description="The deep cerebral veins are a group of veins in the head. This group includes the superior thalamostriate vein. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0016564)]",
    name="deep cerebral vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0016564#deep-cerebral-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0016564"),
)
VascularStructure.deep_middle_cerebral_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/deepMiddleCerebralVein",
    definition="Is a cerebral vein. Is part of the basal vein. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035532) ('is_a' and 'relationship')]",
    description="The blood vessel that receives deoxygenated blood from the insula and gyri and drains into the basal vein of Rosenthal deep in the lateral sulcus. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035532)]",
    name="deep middle cerebral vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0035532#deep-middle-cerebral-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0035532"),
)
VascularStructure.dorsal_cerebral_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/dorsalCerebralVein",
    definition="Is a cerebral vein. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035151)]",
    name="dorsal cerebral vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0035151#dorsal-cerebral-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0035151"),
)
VascularStructure.dorsal_longitudinal_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/dorsalLongitudinalVein",
    definition="Is a brain blood vessel. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_2005031)]",
    description="Vessel that connects to the primitive hindbrain channel and the basilar artery at the caudal end of the medulla oblongata. Isogai et al. 2001. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_2005031)]",
    name="dorsal longitudinal vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:2005031#dorsal-longitudinal-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_2005031"),
    synonyms=["DLV"],
)
VascularStructure.dura_mater_lymph_vessel = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/duraMaterLymphVessel",
    definition="Is part of the meningeal cluster. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035608)]",
    description="Any lymph vessel that is located in the dura mater of the brain. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035608)]",
    name="dura mater lymph vessel",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0035608#dura-mater-lymph-vessel"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0035608"),
    synonyms=["dural lymph vessel"],
)
VascularStructure.great_cerebral_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/greatCerebralVein",
    definition="Is a cerebral vein. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0006666)]",
    description="The great cerebral vein is one of the large blood vessels in the skull draining the cerebrum (brain) [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0006666)]",
    name="great cerebral vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0006666#great-cerebral-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0006666"),
    synonyms=["great cerebral vein of Galen", "vein of Galen"],
)
VascularStructure.hindbrain_venous_system = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/hindbrainVenousSystem",
    definition="Is part of the hindbrain. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0005720)]",
    description="A venous system that is part of a hindbrain. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0005720)]",
    name="hindbrain venous system",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0735731"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0005720#hindbrain-venous-system"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0005720"),
)
VascularStructure.hyaloid_artery = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/hyaloidArtery",
    definition="Is a brain blood vessel. Is part of the optic stalk. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0002270) ('is_a' and 'relationship')]",
    description="An artery that is part of the optic stalk of the eye and extends from the optic disc through the vitreous humor to the lens. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0002270)]",
    name="hyaloid artery",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0002270#hyaloid-artery"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0002270"),
    synonyms=["arteria hyaloidea"],
)
VascularStructure.inferior_petrosal_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/inferiorPetrosalSinus",
    definition="Is a paired venous dural sinus. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0007160)]",
    description="The inferior petrosal sinus, within the human head, is an area beneath the brain, which allows blood veins to span the area, from the center of the head downward. It drains from the cavernous sinus (beneath the brain) to the sigmoid sinuses above the internal jugular vein. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0007160)]",
    name="inferior petrosal sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0007160#inferior-petrosal-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0007160"),
    synonyms=["sinus petrosal inferior"],
)
VascularStructure.inferior_sagittal_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/inferiorSagittalSinus",
    definition="Is a sagittal sinus. Is part of the tentorial sinus. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0007152) ('is_a' and 'relationship')]",
    description="An intracranial venous sinus that lies in a midline location along the lower free border of the falx cerebri of the brain. The sinus receives blood from the great cerebral vein and joins the superior sagittal sinus posteriorly. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0007152)]",
    name="inferior sagittal sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0007152#inferior-sagittal-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0007152"),
)
VascularStructure.internal_cerebral_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/internalCerebralVein",
    definition="Is a cerebral vein. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035152)]",
    description="The internal cerebral veins (veins of Galen; deep cerebral veins) drain the deep parts of the hemisphere and are two in number; each is formed near the interventricular foramen by the union of the terminal and choroid veins. They run backward parallel with one another, between the layers of the tela chorioidea of the third ventricle, and beneath the splenium of the corpus callosum, where they unite to form a short trunk, the great cerebral vein; just before their union each receives the corresponding basal vein. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035152)]",
    name="internal cerebral vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0035152#internal-cerebral-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0035152"),
)
VascularStructure.marginal_venous_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/marginalVenousSinus",
    definition="Is a paired venous dural sinus. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0017637)]",
    description="A paired dural venous sinus at the rim of the foramen magnum. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0017637)]",
    name="marginal venous sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0017637#marginal-venous-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0017637"),
    synonyms=["intracranial marginal sinus"],
)
VascularStructure.middle_mesencephalic_central_artery = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/middleMesencephalicCentralArtery",
    definition="Is a central artery. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_2005078)]",
    description="Project rostrally and dorsally from the AMCtA to to irrigate the midportion of the midbrain Isogai et al. 2001. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_2005078)]",
    name="middle mesencephalic central artery",
    preferred_cross_reference=IRI(
        "https://knowledge-space.org/wiki/UBERON:2005078#middle-mesencephalic-central-artery"
    ),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_2005078"),
    synonyms=["MMCtA"],
)
VascularStructure.naso_frontal_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/nasoFrontalVein",
    definition="Is part of the cavernous sinus. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0004689)]",
    description="The nasofrontal vein is a vein in the eye which drains to the superior ophthalmic vein. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0004689)]",
    name="naso-frontal vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0004689#naso-frontal-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0004689"),
    synonyms=["nasofrontal vein"],
)
VascularStructure.paired_venous_dural_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/pairedVenousDuralSinus",
    definition="Is a venous dural sinus. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0017635)]",
    name="paired venous dural sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0017635#paired-venous-dural-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0017635"),
    synonyms=["paired dural venous sinus"],
)
VascularStructure.perineural_vascular_plexus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/perineuralVascularPlexus",
    definition="Is part of the nervous system. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0015189)]",
    description="The capillary bed that initially surrounds the relative avascular brain and spinal cord; the perineural vascular plexus (PNVP) is the precursor to the blood brain barrier formed by angioblasts which migrate away from somites and is recruited to surround the neural tube in response to VEGF; vascularization of the brain and spinal cord occurs via angiogenesis as sprouting vessels from the PNVP invade the neuroepithelium and grow inward toward the ventricular lumen. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0015189)]",
    name="perineural vascular plexus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0015189#perineural-vascular-plexus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0015189"),
    synonyms=["PNVP"],
)
VascularStructure.primitive_marginal_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/primitiveMarginalSinus",
    definition="Is a paired venous dural sinus. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0017638)]",
    description="The primitive marginal sinuses (PMS) are embryonic sinuses forming the later superior sagittal sinus. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0017638)]",
    name="primitive marginal sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0017638#primitive-marginal-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0017638"),
)
VascularStructure.primitive_superior_sagittal_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/primitiveSuperiorSagittalSinus",
    definition="Is part of the venous dural sinus. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0009968)]",
    name="primitive superior sagittal sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0009968#primitive-superior-sagittal-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0009968"),
)
VascularStructure.retina_blood_vessel = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/retinaBloodVessel",
    definition="Is part of the vasculature of retina. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0003501)]",
    description="A blood vessel that is part of a retina. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0003501)]",
    name="retina blood vessel",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0003501#retina-blood-vessel"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0003501"),
    synonyms=[
        "blood vessel of inner layer of eyeball",
        "blood vessel of retina",
        "blood vessel of tunica interna of eyeball",
        "inner layer of eyeball blood vessel",
        "retinal blood vessel",
        "tunica interna of eyeball blood vessel",
    ],
)
VascularStructure.sagittal_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/sagittalSinus",
    definition="Is an unpaired venous dural sinus. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0015704)]",
    description="Either the inferior or superior sagittal sinus. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0015704)]",
    name="sagittal sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0015704#sagittal-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0015704"),
)
VascularStructure.sigmoid_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/sigmoidSinus",
    definition="Is a paired venous dural sinus. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0005475)]",
    description="A portion of the lateral venous sinus, bulging prominently into the mastoid cavity, that serves as a principal conduit by which blood leaves the cranium. The sigmoid is drained by the internal jugular vein. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0005475)]",
    name="sigmoid sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0005475#sigmoid-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0005475"),
)
VascularStructure.sphenoparietal_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/sphenoparietalSinus",
    definition="Is a paired venous dural sinus. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035338)]",
    description="The cavernous sinus receives the superior ophthalmic vein through the superior orbital fissure, some of the cerebral veins, and also the small sphenoparietal sinus, which courses along the under surface of the small wing of the sphenoid. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035338)]",
    name="sphenoparietal sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0035338#sphenoparietal-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0035338"),
)
VascularStructure.superficial_cerebral_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/superficialCerebralVein",
    definition="Is a cerebral vein. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0016559)]",
    description="The superficial cerebral veins are a group of veins in the head. This group includes the superior cerebral veins. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0016559)]",
    name="superficial cerebral vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0016559#superficial-cerebral-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0016559"),
    synonyms=["cortical cerebral vein"],
)
VascularStructure.superficial_middle_cerebral_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/superficialMiddleCerebralVein",
    definition="Is a cerebral vein. Is part of the cavernous sinus. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035231) ('is_a' and 'relationship')]",
    description="A vein that runs along the fissure of Sylvius to the cavernous sinus on the lateral surface of the brain and connects to the superior sagittal and transverse sinuses. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035231)]",
    name="superficial middle cerebral vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0035231#superficial-middle-cerebral-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0035231"),
    synonyms=["Sylvian vein", "vein of Labbe"],
)
VascularStructure.superior_cerebral_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/superiorCerebralVein",
    definition="Is a superficial cerebral vein. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035150)]",
    description="The Superior Cerebral Veins, eight to twelve in number, drain the superior, lateral, and medial surfaces of the hemispheres, and are mainly lodged in the sulci between the gyri, but some run across the gyri. They open into the superior sagittal sinus; the anterior veins runs nearly at right angles to the sinus; the posterior and larger veins are directed obliquely forward and open into the sinus in a direction more or less opposed to the current of the blood contained within it. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0035150)]",
    name="superior cerebral vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0035150#superior-cerebral-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0035150"),
)
VascularStructure.superior_sagittal_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/superiorSagittalSinus",
    definition="Is a sagittal sinus. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001642)]",
    description="The superior sagittal sinus (also known as the superior longitudinal sinus), within a human cranium, is an area above/behind the brain, which allows blood veins to span the area, from the top of the head towards the back. It is believed that the cerebrospinal fluid drains through the arachnoid granulations into the dural venous sinuses of the superior sagittal sinus. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001642)]",
    name="superior sagittal sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0001642#superior-sagittal-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001642"),
)
VascularStructure.tentorial_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/tentorialSinus",
    definition="Is an unpaired venous dural sinus. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0005481)]",
    description="An unpaired venous dural sinus that receives blood from the superior cerebellar veins and inferior sagittal sinus and drains into the confluence of sinuses. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0005481)]",
    name="tentorial sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0005481#tentorial-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0005481"),
)
VascularStructure.transverse_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/transverseSinus",
    definition="Is a paired venous dural sinus. Is part of the sigmoid sinus. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001641) ('is_a' and 'relationship')]",
    description="One of the dural venous sinuses and drains the superior sagittal sinus the occipital sinus and the straight sinus, and empties into the sigmoid sinus which in turn reaches the jugular bulb. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0001641)]",
    name="transverse sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0001641#transverse-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0001641"),
    synonyms=["sinus transversus durae matris"],
)
VascularStructure.tributary_of_central_retinal_vein = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/tributaryOfCentralRetinalVein",
    definition="Is part of the central retinal vein. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0036300)]",
    name="tributary of central retinal vein",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0036300#tributary-of-central-retinal-vein"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0036300"),
    synonyms=["central retinal venous tributary"],
)
VascularStructure.unpaired_venous_dural_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/unpairedVenousDuralSinus",
    definition="Is a venous dural sinus. [auto-generated from 'is_a' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0017640)]",
    name="unpaired venous dural sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0017640#unpaired-venous-dural-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0017640"),
    synonyms=["unpaired dural venous sinus"],
)
VascularStructure.vasculature_of_brain = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/vasculatureOfBrain",
    definition="Is a vasculature of central nervous system. Is part of the brain. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0008998) ('is_a' and 'relationship')]",
    description="System pertaining to blood vessels in the brain. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0008998)]",
    name="vasculature of brain",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0735625"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0008998#vasculature-of-brain"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0008998"),
    synonyms=["brain vasculature", "cerebrovascular system", "intracerebral vasculature"],
)
VascularStructure.vasculature_of_central_nervous_system = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/vasculatureOfCentralNervousSystem",
    definition="Is an anatomical entity. Is part of the central nervous system. [auto-generated from properties of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0036303) ('is_a' and 'relationship')]",
    name="vasculature of central nervous system",
    preferred_cross_reference=IRI(
        "https://knowledge-space.org/wiki/UBERON:0036303#vasculature-of-central-nervous-system"
    ),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0036303"),
)
VascularStructure.vasculature_of_retina = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/vasculatureOfRetina",
    definition="Is part of the retina. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0004864)]",
    description="A vasculature that is part of a retina. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0004864)]",
    name="vasculature of retina",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0004864#vasculature-of-retina"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0004864"),
    synonyms=[
        "retina vasculature",
        "retina vasculature of camera-type eye",
        "retinal blood vessels",
        "retinal blood vessels set",
        "retinal vasculature",
        "set of blood vessels of retina",
        "set of retinal blood vessels",
        "vasa sanguinea retinae",
    ],
)
VascularStructure.venous_dural_sinus = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/venousDuralSinus",
    definition="Is part of the meningeal cluster. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0005486)]",
    description="A venous channel found between layers of dura mater in the brain. Receives blood from internal and external veins of the brain, receive cerebrospinal fluid (CSF) from the subarachnoid space, and ultimately empty into the internal jugular vein. [definition of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0005486)]",
    name="venous dural sinus",
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0005486#venous-dural-sinus"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0005486"),
    synonyms=["cranial dural venous sinus", "dural sinus", "dural vein", "dural venous sinus", "venous dural"],
)
VascularStructure.venous_system_of_brain = VascularStructure(
    id="https://openminds.om-i.org/instances/vascularStructure/venousSystemOfBrain",
    definition="Is part of the brain. [auto-generated from 'relationship' property of the [UBERON ontology term](http://purl.obolibrary.org/obo/UBERON_0013146)]",
    name="venous system of brain",
    other_ontology_identifiers=["http://uri.interlex.org/base/ilx_0733246"],
    preferred_cross_reference=IRI("https://knowledge-space.org/wiki/UBERON:0013146#venous-system-of-brain"),
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/UBERON_0013146"),
    synonyms=["brain venous system"],
)
