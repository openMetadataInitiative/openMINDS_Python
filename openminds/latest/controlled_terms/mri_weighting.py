"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class MRIWeighting(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/MRIWeighting"
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
            description="Longer statement or account giving the characteristics of the m r i weighting.",
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
            description="Word or phrase that constitutes the distinctive designation of the m r i weighting.",
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


MRIWeighting.pd_weighting = MRIWeighting(
    id="https://openminds.om-i.org/instances/MRIWeighting/PDWeighting",
    definition="Image processing technique that specifically enhances the signal-to-noise ratio of density of protons (hydrogen atoms).",
    name="PD weighting",
    synonyms=[
        "PD weighted image processing",
        "PD weighted imaging",
        "PD weighted magnetic resonance imaging",
        "PD weighted MRI",
        "PDw image processing",
        "PDw imaging",
        "PDw magnetic resonance imaging",
        "PDw MRI",
        "proton density weighted image processing",
        "proton density weighted imaging",
        "proton density weighted magnetic resonance imaging",
        "proton density weighted MRI",
        "proton density weighting",
    ],
)
MRIWeighting.r2_star_weighting = MRIWeighting(
    id="https://openminds.om-i.org/instances/MRIWeighting/R2-starWeighting",
    definition="Image processing technique that creates the image contrast from the reciprocal of the T2-star relaxation time.",
    name="R2-star weighting",
    synonyms=[
        "R2-star weighted image processing",
        "R2-star weighted imaging",
        "R2-star weighted magnetic resonance imaging",
        "R2-star weighted MRI",
        "R2* weighted image processing",
        "R2* weighted imaging",
        "R2* weighted magnetic resonance imaging",
        "R2* weighted MRI",
        "R2* weighting",
        "R2*w image processing",
        "R2*w imaging",
        "R2*w magnetic resonance imaging",
        "R2*w MRI",
    ],
)
MRIWeighting.r2_weighting = MRIWeighting(
    id="https://openminds.om-i.org/instances/MRIWeighting/R2Weighting",
    definition="Image processing technique that creates the image contrast from the reciprocal of the T2 relaxation time.",
    name="R2 weighting",
    synonyms=[
        "R2 weighted image processing",
        "R2 weighted imaging",
        "R2 weighted magnetic resonance imaging",
        "R2 weighted MRI",
        "R2w image processing",
        "R2w imaging",
        "R2w magnetic resonance imaging",
        "R2w MRI",
    ],
)
MRIWeighting.t1_rho_weighting = MRIWeighting(
    id="https://openminds.om-i.org/instances/MRIWeighting/T1RhoWeighting",
    definition="Image processing technique that specifically enhances the signal-to-noise ratio of the spin-lattice relaxation in the rotation frame at the presence of an external RF pulse in the transverse plane (T1 rho relaxation time).",
    name="T1 rho weighting",
    synonyms=[
        "T1 rho weighted image processing",
        "T1 rho weighted imaging",
        "T1 rho weighted magnetic resonance imaging",
        "T1 rho weighted MRI",
        "T1ρ weighted image processing",
        "T1ρ weighted imaging",
        "T1ρ weighted magnetic resonance imaging",
        "T1ρ weighted MRI",
    ],
)
MRIWeighting.t1_weighting = MRIWeighting(
    id="https://openminds.om-i.org/instances/MRIWeighting/T1Weighting",
    definition="Image processing technique that specifically enhances the signal-to-noise ratio of the spin-lattice relaxation (T1 relaxation time).",
    name="T1 weighting",
    synonyms=[
        "T1 weighted image processing",
        "T1 weighted imaging",
        "T1 weighted magnetic resonance imaging",
        "T1 weighted MRI",
        "T1w image processing",
        "T1w imaging",
        "T1w magnetic resonance imaging",
        "T1w MRI",
    ],
)
MRIWeighting.t2_star_weighting = MRIWeighting(
    id="https://openminds.om-i.org/instances/MRIWeighting/T2-starWeighting",
    definition="Image processing technique that specifically enhances the signal-to-noise ratio of the observed spin-spin relaxation (T2-star relaxation time) which includes field inhomogeneities.",
    name="T2-star weighting",
    synonyms=[
        "T2-star weighted image processing",
        "T2-star weighted imaging",
        "T2-star weighted magnetic resonance imaging",
        "T2-star weighted MRI",
        "T2* weighted image processing",
        "T2* weighted imaging",
        "T2* weighted magnetic resonance imaging",
        "T2* weighted MRI",
        "T2* weighting",
        "T2*w image processing",
        "T2*w imaging",
        "T2*w magnetic resonance imaging",
        "T2*w MRI",
    ],
)
MRIWeighting.t2_weighting = MRIWeighting(
    id="https://openminds.om-i.org/instances/MRIWeighting/T2Weighting",
    definition="Image processing technique that specifically enhances the signal-to-noise ratio of the true spin-spin relaxation (T2 relaxation time) excluding field inhomogeneities.",
    name="T2 weighting",
    synonyms=[
        "T2 weighted image processing",
        "T2 weighted imaging",
        "T2 weighted magnetic resonance imaging",
        "T2 weighted MRI",
        "T2w image processing",
        "T2w imaging",
        "T2w magnetic resonance imaging",
        "T2w MRI",
    ],
)
