"""
Structured information on a disease.
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Disease(LinkedMetadata):
    """
    Structured information on a disease.
    """

    type_ = "https://openminds.om-i.org/types/Disease"
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
            description="Longer statement or account giving the characteristics of the disease.",
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
            description="Word or phrase that constitutes the distinctive designation of the disease.",
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


Disease.acquired_blindness = Disease(
    id="https://openminds.om-i.org/instances/disease/acquiredBlindness",
    definition="Acquired blindness is caused by a group of diseases, disorders or injuries that led to permanent severely impaired vision or irreversible lack of vision during adulthood.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0499758"),
    name="acquired blindness",
    preferred_ontology_identifier=IRI("http://id.nlm.nih.gov/mesh/2018/M0336554"),
)
Disease.alzheimers_disease = Disease(
    id="https://openminds.om-i.org/instances/disease/alzheimersDisease",
    name="Alzheimer's disease",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/DOID_10652"),
)
Disease.autism_spectrum_disorder = Disease(
    id="https://openminds.om-i.org/instances/disease/autismSpectrumDisorder",
    name="autism sprectrum disorder",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/DOID_0060041"),
)
Disease.cerebral_atrophy = Disease(
    id="https://openminds.om-i.org/instances/disease/cerebralAtrophy",
    definition="Cerebral atrophy describes the pathological process of wasting or decrease in size of the cells or tissue of the cerebrum.",
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/HP:0012444#brain-atrophy"),
    name="cerebral atrophy",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/HP_0002059"),
    synonyms=["atrophy of cerebrum", "brain atrophy", "degeneration of cerebrum", "degeneration of brain"],
)
Disease.congenital_blindness = Disease(
    id="https://openminds.om-i.org/instances/disease/congenitalBlindness",
    definition="Congenital blindness is caused by a group of diseases, disorders or injuries that led to permanent severely impaired vision or irreversible lack of vision before/during birth or in early childhood.",
    name="congenital blindness",
)
Disease.covid_19 = Disease(
    id="https://openminds.om-i.org/instances/disease/COVID-19",
    definition="A coronavirus infectious disease that is characterized by fever, cough and shortness of breath and caused by the coronavirus strain SARS-CoV-2.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739370"),
    name="COVID-19",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/DOID_0080600"),
    synonyms=[
        "coronavirus disease 2019",
        "severe acute respiratory syndrome coronavirus 2",
        "2019 Novel Coronavirus (2019-nCoV)",
        "2019-nCoV infection",
        "COVID19",
        "SARS-CoV-2 infection",
        "Wuhan coronavirus infection",
        "Wuhan seafood market pneumonia virus infection",
    ],
)
Disease.disorder_of_consciousness = Disease(
    id="https://openminds.om-i.org/instances/disease/disorderOfConsciousness",
    definition="A 'disorder of consciousness' is a state where a subject's consciousness has been affected by damage to the brain.",
    name="disorder of consciousness",
    synonyms=["DOC", "impaired consciousness"],
)
Disease.epilepsy = Disease(
    id="https://openminds.om-i.org/instances/disease/epilepsy",
    definition="Epilepsy describes a group of central nervous system disorders characterized by recurrent unprovoked seizures.",
    name="epilepsy",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/DOID_1826"),
)
Disease.focal_cerebral_ischemia = Disease(
    id="https://openminds.om-i.org/instances/disease/focalCerebralIschemia",
    definition="A 'focal brain ischemia' occurs when a blood clot has occluded a cerebral vessel reducing the blood flow to a specific brain region which increases the risk of cell death in that particular area. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Brain_ischemia#Focal_brain_ischemia)]",
    name="focal cerebral ischemia",
    synonyms=["focal brain ischemia", "focal ischemic brain injury"],
)
Disease.fragile_xsyndrome = Disease(
    id="https://openminds.om-i.org/instances/disease/fragileXsyndrome",
    name="fragile X syndrome",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/DOID_14261"),
)
Disease.glioma = Disease(
    id="https://openminds.om-i.org/instances/disease/glioma",
    definition="A benign or malignant brain and spinal cord tumor that arises from glial cells (astrocytes, oligodendrocytes, ependymal cells).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0104647"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/BIRNLEX:12618#glioma"),
    name="glioma",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/birnlex_12618"),
    synonyms=[
        "glial neoplasm",
        "neoplasm of the neuroglia",
        "neuroglial neoplasm",
        "neuroglial tumor",
        "tumor of neuroglia",
        "tumor of the neuroglia",
    ],
)
Disease.long_covid = Disease(
    id="https://openminds.om-i.org/instances/disease/longCOVID",
    definition="A long-term disease originally caused by the severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) with symptoms persisting beyond three to four weeks.",
    description="A Coronavirus infectious disease that is characterized by long-term persistent and fluctuating symptoms, in individuals with COVID-19, persisting beyond three to four weeks, including the loss of the ability to smell and taste, breathlessness, fatigue, difficulty in breathing, difficulty concentrating, memory loss, confusion, headache, heart palpitations, chest pain, pain with deep breaths, dizziness, and tachycardia.",
    name="long COVID",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/DOID_0080848"),
    synonyms=["chronic COVID-19", "PASC", "post-acute sequelae of SARS-CoV-2 infection", "post-COVID syndrome"],
)
Disease.macular_degeneration = Disease(
    id="https://openminds.om-i.org/instances/disease/macularDegeneration",
    definition="A retinal degeneration characterized by gradual deterioration of light-sensing cells in the tissues at the back of the eye resulting in vision loss.[adapted from [Disease Ontology definition](http://purl.obolibrary.org/obo/DOID_4448)]",
    description="Deterioration of the macula lutea in the retina; may be inherited, drug induced, or due to aging; leads to a severe loss of central vision while peripheral vision is retained.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0106448"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/BIRNLEX:12811#macular-degeneration-1"),
    name="macular degeneration",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/DOID_4448"),
    synonyms=["macular degeneration of retina", "macular dystrophy", "maculopathy"],
)
Disease.malignant_neoplasm = Disease(
    id="https://openminds.om-i.org/instances/disease/malignantNeoplasm",
    definition="A 'malignant neoplasm' is composed of atypical, often pleomorphic cells that uncontrollably grow and multiply, spreading into surrounding tissue and even invading distant anatomic sites (metastasis). Many malignant neoplasm form solid tumors, but cancers of the blood generally do not. [(adapted from [NCI](https://www.cancer.gov/about-cancer/understanding/what-is-cancer)].",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0752652"),
    name="malignant neoplasm",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/NCIT_C9305"),
    synonyms=["cancer"],
)
Disease.meningioma = Disease(
    id="https://openminds.om-i.org/instances/disease/meningioma",
    definition="A generally slow growing tumor attached to the dura mater and composed of neoplastic meningothelial (arachnoidal) cells.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0106789"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/BIRNLEX:12601#meningioma"),
    name="meningioma",
    preferred_ontology_identifier=IRI("http://uri.neuinfo.org/nif/nifstd/birnlex_12601"),
    synonyms=[
        "meningeal neoplasm",
        "meningothelial cell tumor",
        "neoplasm of the meninges",
        "primary meningeal tumor",
        "supratentorial meningioma",
    ],
)
Disease.mental_disorder = Disease(
    id="https://openminds.om-i.org/instances/disease/mentalDisorder",
    definition="A 'mental disorder' is characterized by a clinically significant disturbance in an individual’s cognition, emotional regulation, or behaviour and is usually associated with distress or impairment in important areas of functioning. [adapted from [WHO fact-sheets](https://www.who.int/news-room/fact-sheets/detail/mental-disorders)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0106792"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/BIRNLEX:12669#mental-disorder"),
    name="mental disorder",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/base/ilx_0106792"),
    synonyms=["mental disease", "mental illness", "psychiatric disease", "psychiatric disorder"],
)
Disease.minimally_conscious_state = Disease(
    id="https://openminds.om-i.org/instances/disease/minimallyConsciousState",
    definition="A 'minimally conscious state' (MCS) is a disorder of consciousness with partial preservation of conscious awareness. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Minimally_conscious_state)]",
    name="minimally conscious state",
    synonyms=["MCS"],
)
Disease.multiple_sclerosis = Disease(
    id="https://openminds.om-i.org/instances/disease/multipleSclerosis",
    definition="'Multiple sclerosis' is a disorder in which the body's immune system attacks the protective meylin covering of the nerve cells in the brain, optic nerve and spinal cord (adapted from the [Mayo clinic](https://www.mayoclinic.org/diseases-conditions/multiple-sclerosis/symptoms-causes/syc-20350269#:~:text=Multiple%20sclerosis%20is%20a%20disorder,insulation%20on%20an%20electrical%20wire.))",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0756481"),
    knowledge_space_link=IRI("https://knowledge-space.org/wiki/BIRNLEX:12514#multiple-sclerosis-1"),
    name="multiple sclerosis",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/DOID_2377"),
    synonyms=["MS", "generalized multiple sclerosis"],
)
Disease.parkinsons_disease = Disease(
    id="https://openminds.om-i.org/instances/disease/parkinsonsDisease",
    definition="Parkinson's is a progressive central nervous system disorder that affects the motor system.",
    name="Parkinson's disease",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/DOID_14330"),
)
Disease.stroke = Disease(
    id="https://openminds.om-i.org/instances/disease/stroke",
    definition="A sudden loss of neurological function secondary to hemorrhage or ischemia in the brain parenchyma due to a vascular event.",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0738754"),
    name="stroke",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/DOID_6713"),
    synonyms=["cerebral infaction", "cerebrovascular accident", "cerebrovascular disease", "CVA", "stroke disorder"],
)
Disease.unresponsive_wakefulness_syndrome = Disease(
    id="https://openminds.om-i.org/instances/disease/unresponsiveWakefulnessSyndrome",
    definition="The 'unresponsive wakefulness syndrome' (UWS) is a disorder of consciousness, formerly known as vegetative state, with only reflexive behavior and no sign of conscious awareness [[Laureys et al. 2010](https://doi.org/10.1186/1741-7015-8-68)].",
    name="unresponsive wakefulness syndrome",
    synonyms=["UWS", "vegetative state", "VS"],
)
Disease.williams_beuren_syndrome = Disease(
    id="https://openminds.om-i.org/instances/disease/williamsBeurenSyndrome",
    name="Williams-Beuren syndrome",
    preferred_ontology_identifier=IRI("http://purl.obolibrary.org/obo/DOID_1928"),
)
