"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class MRSpatialEncoding(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/MRSpatialEncoding"
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
            description="Longer statement or account giving the characteristics of the m r spatial encoding.",
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
            description="Word or phrase that constitutes the distinctive designation of the m r spatial encoding.",
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
            matches = cls._instance_lookup.get(name, None)
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if all:
            return matches
        elif len(matches) > 0:
            return matches[0]
        else:
            return None


MRSpatialEncoding.frequency_encoding = MRSpatialEncoding(
    id="https://openminds.om-i.org/instances/MRSpatialEncoding/frequencyEncoding",
    definition="Gradients establish a direct relationship between frequency and spatial position, a process referred to as frequency encoding.",
    description="In MRI, gradients generate a controlled variation in the magnetic field strength across the imaging volume. Each location along the gradient direction corresponds to a unique frequency in the received MR signal. This process, known as frequency encoding, allows spatial information to be extracted from the signal during image reconstruction. Primarily used in specialized applications like spectroscopy.",
    name="1D MR acquisition",
    synonyms=["frequency encoding", "1D MRI acquisition"],
)
MRSpatialEncoding.frequency_phase_encoding = MRSpatialEncoding(
    id="https://openminds.om-i.org/instances/MRSpatialEncoding/frequencyPhaseEncoding",
    definition="Using frequency encoding and phase encoding in conjunction together to acquire 2D magnetic resonance images.",
    description="In 2D frequency x phase MRI imaging, spatial localization is achieved through a combination of slice selection, frequency encoding, and phase encoding. Slice selection involves applying a gradient along one axis (typically the z-axis) during RF excitation, ensuring that only a specific tissue slice resonates based on its unique Larmor frequency. Once the slice is excited, frequency encoding is applied along another axis (usually the x-axis) during signal acquisition, creating a direct relationship between spatial position and resonance frequency. To encode the second spatial dimension (typically the y-axis), phase encoding is applied before signal acquisition, briefly altering the phase of spins based on their position. This phase shift remains embedded in the signal and is later decoded during image reconstruction, allowing for the creation of detailed 2D MR images.",
    name="Frequency x phase encoding",
    synonyms=["2D MRI acquisition", "2D frequency x phase encoding"],
)
MRSpatialEncoding.frequency_phase_phase_encoding = MRSpatialEncoding(
    id="https://openminds.om-i.org/instances/MRSpatialEncoding/frequencyPhasePhaseEncoding",
    definition="3D MRI imaging is a technique that acquires volumetric data by using frequency encoding and two phase encoding steps, eliminating the need for slice selection and enabling high-resolution, multi-plane image reconstruction.",
    description="In 3D frequency x phase x phase MRI imaging, spatial localization is achieved using frequency encoding, phase encoding, and a second phase encoding step instead of slice selection. Unlike 2D imaging, where individual slices are excited separately, 3D MRI excites the entire imaging volume at once. Frequency encoding is applied along one axis (typically the x-axis), while phase encoding is applied along the second (usually the y-axis). To resolve the third dimension, an additional phase encoding step is applied along the slice-select direction (typically the z-axis), replacing traditional slice selection. This results in a fully sampled 3D dataset, which can be reconstructed into thin slices or reformatted in multiple planes, providing higher signal-to-noise ratio (SNR) and improved spatial resolution compared to 2D imaging.",
    name="Frequency x phase x phase encoding",
    synonyms=["3D MRI acquisition", "frequency x phase x phase", "3D frequency x phase x phase"],
)
MRSpatialEncoding.phase_encoding = MRSpatialEncoding(
    id="https://openminds.om-i.org/instances/MRSpatialEncoding/phaseEncoding",
    definition="Gradients establish a direct relationship between phase and spatial position, a process referred to as phase encoding.",
    name="Phase encoding",
    synonyms=["phase encoding"],
)
