"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class MolecularEntity(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/MolecularEntity"
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


MolecularEntity.a1_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/A1Receptor",
    definition="The adenosine A1 receptor is a subtype of the adenosine receptor group that bind adenosine as endogenous ligand.",
    interlex_identifier="http://uri.interlex.org/ilx_0100146",
    name="A1 receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5717",
    synonyms=["A1", "adenosine A1 receptor"],
)
MolecularEntity.a2_a_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/A2AReceptor",
    definition="The adenosine A2A receptor is a subtype of the adenosine receptor group that bind adenosine as endogenous ligand.",
    interlex_identifier="http://uri.interlex.org/ilx_0100148",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:7728#a2a-receptor",
    name="A2A receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_7727",
    synonyms=["A2A", "adenosine A2A receptor", "adenosine A2a receptor"],
)
MolecularEntity.acetylcholine = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/acetylcholine",
    definition="Acetylcholine in vertebrates is the major neurotransmitter at neuromuscular junctions, autonomic ganglia, parasympathetic effector junctions, a subset of sympathetic effector junctions, and at many sites in the central nervous system.",
    interlex_identifier="http://uri.interlex.org/ilx_0100240",
    name="acetylcholine",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao185580330",
    synonyms=["ACh"],
)
MolecularEntity.alexa_fluor594 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/AlexaFluor594",
    definition="Alexa Fluor 594' is a fluorochrome/fluorescent dye used to stain biological specimens.",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:51248#alexa-fluor-594",
    name="Alexa Fluor 594",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_51248",
    synonyms=["Alexa 594"],
)
MolecularEntity.alpha_1_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/alpha-1Receptor",
    definition="The alpha-1 receptor is a subclass of the adrenoceptor group that bind epinephrine or norepinephrine as endogenous ligands.",
    name="alpha-1 receptor",
    synonyms=["alpha1", "alpha-1 adrenergic receptor", "alpha 1", "α1 receptor", "α1 adrenergic receptor"],
)
MolecularEntity.alpha_2_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/alpha-2Receptor",
    definition="The alpha-2 receptor is a subclass of the adrenoceptor group that bind epinephrine or norepinephrine as endogenous ligands.",
    name="alpha-2 receptor",
    synonyms=["alpha2", "alpha-2 adrenergic receptor", "alpha 2", "α2 receptor", "α2 adrenergic receptor"],
)
MolecularEntity.alpha_4_beta_2_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/alpha-4Beta-2Receptor",
    definition="The alpha-4 beta-2 receptor belongs to the family of nicotinic acetylcholine receptors that respond to the neurotransmitter acetylcholine as endogenous ligand. This subtype is located in the brain, where activation yields post- and presynaptic excitation.",
    interlex_identifier="http://uri.interlex.org/ilx_0597802",
    name="alpha-4 beta-2 receptor",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0356600",
    synonyms=[
        "nicotinic acetylcholine alpha4beta2 receptor",
        "alpha-4 beta-2 nicotinic receptor",
        "alpha-4 beta-2 receptor",
        "nicotinic receptor alpha4beta2",
        "α4β2 receptor",
    ],
)
MolecularEntity.ampa_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/AMPAReceptor",
    definition="The AMPA receptors belong to the class of ionotropic glutamate receptors and mediate fast synaptic transmission in the central nervous system (CNS).",
    interlex_identifier="http://uri.interlex.org/ilx_0100559",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:5251#ampa-type-glutamate-gated-cationic-channel",
    name="AMPA receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5251",
    synonyms=[
        "AMPA-type glutamate-gated cationic channel",
        "AMPAR",
        "ionotropic alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid receptor",
        "ionotropic AMPA receptor",
        "ionotropic glutamate AMPA receptor",
        "quisqualate receptor",
    ],
)
MolecularEntity.anterograde_tracer = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/anterogradeTracer",
    definition="An anterograde tracer is a molecule that is taken up by neurons (e.g., by viral transfection mechanisms, by other cell internalization mechanisms or passive diffusion) and transported towards the axon terminals. It is used for anterograde tract tracing studies in the nervous system.",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXMOL:1012002#anterograde-tracer",
    name="anterograde tracer",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/NLXMOL_1012002",
)
MolecularEntity.beta__amyloid40 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/Beta-Amyloid40",
    definition="Amyloid beta peptide with carboxyterminal variant ending at residual Val40.",
    interlex_identifier="http://uri.interlex.org/ilx_0101246",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXMOL:20090708#beta-amyloid-40",
    name="Beta-Amyloid 40",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_13181",
    synonyms=["Abeta40", "AbetaX-40", "Amyloid-Beta 40"],
)
MolecularEntity.biomarker = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/biomarker",
    definition="A substance used as an indicator of a biological state, most commonly disease.",
    interlex_identifier="http://uri.interlex.org/ilx_0101294",
    name="biomarker",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_mol_20090517",
)
MolecularEntity.biotinylated_dextran_amine = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/biotinylatedDextranAmine",
    definition="A 'biotinylated dextran amine' is an organic compound which is used as an anterograde and retrograde neuroanatomical tracer.",
    interlex_identifier="http://uri.interlex.org/ilx_0450726",
    name="biotinylated dextran amine",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0205506",
    synonyms=["B-DA", "BDA", "biotin dextran amine", "biotinylated dextranamine"],
)
MolecularEntity.brain_derived_neurotrophic_factor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/brainDerivedNeurotrophicFactor",
    definition="The 'brain-derived neurotrophic factor' is a protein that, in humans, is encoded by the BDNF gene. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Brain-derived_neurotrophic_factor)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101140",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXMOL:20090401#bdnf",
    name="brain-derived neurotrophic factor",
    synonyms=["BDNF", "abrineurin"],
)
MolecularEntity.bz = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/GABA-A/BZ",
    definition="The GABA-A/BZ is a distinct binding site for benzodiazepines that is situated at the interface between the α- and γ-subunits of α- and γ-subunit containing GABA-A receptors.",
    name="GABA-A/BZ",
    synonyms=[
        "GABA-A/benzodiazepine site",
        "GABAA/benzodiazepine site",
        "GABA A receptor/benzodiazepine site",
        "GABA_A/benzodiazepine site",
        "GABAA/BZ\r",
        "GABA A receptor/BZ\r",
        "GABA_A/BZ",
    ],
)
MolecularEntity.c_fos = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/c-FOS",
    definition="c-FOS is a proto-oncogene that is the human homolog of the retroviral oncogene v-fos.",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000007597#proto-oncogene-c-fos",
    name="c-FOS",
    preferred_ontology_identifier="https://ncimeta.nci.nih.gov/ncimbrowser/ConceptReport.jsp?dictionary=NCI%20Metathesaurus&code=C0314702",
    synonyms=["c-f", "c-fos", "cF", "cFos", "D12Rfj", "D12Rfj1", "FBJ osteosarcoma oncogene", "Fos"],
)
MolecularEntity.calbindin = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/calbindin",
    definition="Calbindin is a calcium-binding protein.",
    interlex_identifier="http://uri.interlex.org/ilx_0101551",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXMOL:1006006#calbindin-28k",
    name="calbindin",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_mol_1006006",
    synonyms=["28kDa", "CALB1", "calbindin 1", "calbindin D28K", "calbindin-D(28k)"],
)
MolecularEntity.calcium_calmodulin_protein_kinase_ii = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/calciumCalmodulinProteinKinaseII",
    definition="The 'calcium calmodulin protein kinase II' is a protein with a core domain architecture consisting of a Protein kinase domain and a C-terminal Calcium/calmodulin dependent protein kinase II Association domain.",
    interlex_identifier="http://uri.interlex.org/ilx_0101561",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000003197#calcium-calmodulin-dependent-protein-kinase-ii-chain",
    name="calcium calmodulin protein kinase II",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000003197",
    synonyms=[
        "Ca2+/calmodulin-dependent protein kinase II",
        "calcium/calmodulin-dependent protein kinase type II",
        "CaMKII",
    ],
)
MolecularEntity.calcium_calmodulin_protein_kinase_ii_alpha_chain = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/calciumCalmodulinProteinKinaseIIAlphaChain",
    definition="The 'calcium calmodulin protein kinase II alpha chain' is a calcium/calmodulin-dependent protein kinase type II chain that is a translation product of the human CAMK2A gene or a 1:1 ortholog thereof.",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000003199#calcium-calmodulin-dependent-protein-kinase-type-ii-alpha-chain",
    name="calcium calmodulin protein kinase II alpha chain",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000003199",
    synonyms=[
        "Ca2+/calmodulin-dependent protein kinase 2 alpha chain",
        "Ca2+/calmodulin-dependent protein kinase II alpha chain",
        "calcium/calmodulin-dependent protein kinase type 2 alpha chain",
        "calcium/calmodulin-dependent protein kinase type II alpha chain",
        "CaM kinase 2 subunit alpha",
        "CaM kinase II subunit alpha",
        "CaMK2 subunit alpha",
        "CaMK2a",
        "CaMKII subunit alpha",
        "CaMKIIa",
    ],
)
MolecularEntity.calcium_chloride = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/calciumChloride",
    definition="Calcium chloride is an inorganic compound, a salt with the chemical formula CaCl2. [adapted from wikipedia (https://en.wikipedia.org/wiki/Calcium_chloride)]",
    description="CaCl2 is a white crystalline solid at room temperature, and it is highly soluble in water. It can be created by neutralising hydrochloric acid with calcium hydroxide. Calcium chloride is commonly encountered as a hydrated solid with generic formula CaCl2·nH2O, where n = 0, 1, 2, 4, and 6. These compounds are mainly used for de-icing and dust control. Because the anhydrous salt is hygroscopic and deliquescent, it is used as a desiccant. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Calcium_chloride)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0101566",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:3312#calcium-dichloride",
    name="calcium chloride",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_3312",
    synonyms=["CaCl2", "calcium(II) chloride", "calcium dichloride (1:2)", "E509"],
)
MolecularEntity.calretinin = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/calretinin",
    definition="Calretinin is an intracellular calcium-binding protein belonging to the troponin C superfamily. Members of this protein family have six EF-hand domains which bind calcium.",
    interlex_identifier="http://uri.interlex.org/ilx_0101602",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:5#calretinin",
    name="calretinin",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5717",
    synonyms=["29kDa calbindin", "CAB29", "CALB2", "calbindin 2", "CR"],
)
MolecularEntity.carbon_dioxide = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/carbonDioxide",
    definition="A one-carbon compound with formula CO2 in which the carbon is attached to each oxygen atom by a double bond. A colourless, odourless gas under normal conditions, it is produced during respiration by all animals, fungi and microorganisms that depend directly or indirectly on living or decaying plants for food. [adapted from ChEBI (https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:16526)]",
    description="Carbon dioxide is a chemical compound with the chemical formula CO2. It is made up of molecules that each have one carbon atom covalently double bonded to two oxygen atoms. It is found in the gas state at room temperature, and as the source of available carbon in the carbon cycle, atmospheric CO2 is the primary carbon source for life on Earth. In the air, carbon dioxide is transparent to visible light but absorbs infrared radiation, acting as a greenhouse gas. Carbon dioxide is soluble in water and is found in groundwater, lakes, ice caps, and seawater. [adapted from ChEBI (https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:16526)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0780969",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:16526#carbon-dioxide",
    name="carbon dioxide",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_16526",
    synonyms=[
        "CO2",
        "carbonic acid gas",
        "carbonic anhydride",
        "carbonic dioxide",
        "dry ice",
        "carbonic oxide",
        "E290",
    ],
)
MolecularEntity.cholecystokinin = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/cholecystokinin",
    definition="Cholecystokinin is a peptide hormone of the gastrointestinal system responsible for stimulating the digestion of fat and protein.",
    interlex_identifier="http://uri.interlex.org/ilx_0102124",
    name="cholecystokinin",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5068",
    synonyms=["CCK"],
)
MolecularEntity.choline = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/choline",
    definition="Choline is a cation with the chemical formula [(CH3)3NCH2CH2OH]+. Choline forms various salts, for example choline chloride and choline bitartrate. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Choline)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0102128",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:15354#choline",
    name="choline",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_15354",
    synonyms=[
        "(2-hydroxyethyl)trimethylammonium",
        "2-hydroxy-N,N,N-trimethylethanaminium",
        "bilineurine",
        "choline cation",
        "choline ion",
    ],
)
MolecularEntity.choline_acetyltransferase = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/cholineAcetyltransferase",
    definition="Choline acetyltransferase is a synthetic enzyme that catalyzes the formation of acetylcholine from acetyl-CoA and choline",
    interlex_identifier="http://uri.interlex.org/base/ilx_0102129",
    name="choline acetyltransferase",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao722953401",
    synonyms=["ChAT", "choline acetylase"],
)
MolecularEntity.cyclic_adenosine_monophosphate = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/cyclicAdenosineMonophosphate",
    definition="Cyclic adenosine monophosphate is a second messenger important in many biological processes.",
    interlex_identifier="http://uri.interlex.org/ilx_0100318",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:17489#3-5-cyclic-amp",
    name="cyclic adenosine monophosphate",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_17489",
    synonyms=[
        "3',5'-cyclic AMP",
        "3',5'-cylic adenosine monophosphate",
        "adenosine 3',5'-cyclic monophosphate",
        "cAMP",
        "cyclic AMP",
    ],
)
MolecularEntity.d1_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/D1Receptor",
    definition="The D1 receptor is a subtype of the dopamine receptor group that primarily binds the neurotransmitter dopamine as endogenous ligand. The D1 receptor is the most abundant kind of dopamine receptor in the central nervous system.",
    interlex_identifier="http://uri.interlex.org/ilx_0102774",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:5845#d1-receptor-1",
    name="D1 receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5845",
    synonyms=["D(1A) dopamine receptor", "D1", "D1 dopamine receptor", "D1R", "dopamine receptor D1", "DRD1"],
)
MolecularEntity.d2_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/D2Receptor",
    definition="The D2 receptor is a subtype of the dopamine receptor group that primarily binds the neurotransmitter dopamine as endogenous ligand.",
    interlex_identifier="http://uri.interlex.org/ilx_0102775",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:5833#d2-receptor-3",
    name="D2 receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5833",
    synonyms=["D(2) dopamine receptor", "D2", "D2 dopamine receptor", "D2R", "dopamine receptor D2", "DRD2"],
)
MolecularEntity.dab = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/DAB",
    definition="DAB is a chemically and thermodynamically stable derivative of benzidine.",
    interlex_identifier="http://uri.interlex.org/ilx_0482636",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:90994#3-3-diaminobenzidine",
    name="DAB",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_90994",
    synonyms=["3,3'-diaminobenzidine"],
)
MolecularEntity.diboron_trioxide = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/diboronTrioxide",
    definition="Diboron trioxide or boron trioxide is the oxide of boron with the formula B2O3. [adapted from wikipedia (https://en.wikipedia.org/wiki/Boron_trioxide)]",
    description=" Diboron trioxide is a colorless transparent solid, almost always glassy (amorphous), which can be crystallized only with great difficulty. It is also called boric oxide or boria. It has many important industrial applications, chiefly in ceramics as a flux for glazes and enamels and in the production of glasses. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Boron_trioxide)]",
    name="diboron trioxide",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_30163",
    synonyms=["boron trioxide", "boron oxide", "boron sesquioxide", "boric oxide", "boria", "boric anhydride"],
)
MolecularEntity.dimethyl_sulfoxide = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/dimethylSulfoxide",
    definition="Dimethyl sulfoxide (DMSO) is an organosulfur compound with the formula (CH3)2SO. [adapted from wikipedia (https://en.wikipedia.org/wiki/Dimethyl_sulfoxide)]",
    description="A highly polar organic liquid, that is used widely as a chemical solvent. Because of its ability to penetrate biological membranes, it is used as a vehicle for topical application of pharmaceuticals. It is also used to protect tissue during cryopreservation. Dimethyl sulfoxide shows a range of pharmacological activity including analgesia and anti-inflammation. (PubChem) Pharmacology: Dimethyl Sulfoxide may have anti-inflammatory, antioxidant and analgesic activities. Dimethyl Sulfoxide also readily penetrates cellular membranes. The membrane-penetrating ability of dimethyl sulfoxide may enhance diffusion of other substances through the skin. For this reason, mixtures of idoxuridine and dimethyl sulfoxide have been used for topical treatment of herpes zoster in the United Kingdom. Mechanism of action: The mechanism of dimethyl sulfoxide's actions is not well understood. Dimethyl sulfoxide has demonstrated antioxidant activity in certain biological settings. For example, the cardiovascular protective effect of dimethyl sulfoxide in copper-deficient rats is thought to occur by an antioxidant mechanism. It is also thought that dimethyl sulfoxide's possible anti-inflammatory activity is due to antioxidant action. [adapted from wikipedia (https://en.wikipedia.org/wiki/Dimethyl_sulfoxide)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103278",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:28262#dimethyl-sulfoxide",
    name="dimethyl sulfoxide",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_28262",
    synonyms=[
        "DMSO",
        "dimethyl sulfoxide BP",
        "dimethyl sulfur oxide",
        "dimethyl sulphoxide",
        "dimethyl sulpoxide",
        "Dimexidum",
        "methyl sulfoxide",
        "methylsulfinylmethane",
        "sulfinylbis-methane",
        "sulfinylbismethane",
        "sulfinyldimethane",
        "Decap",
        "Deltan",
        "Demasorb",
        "Demavet",
        "Demeso",
        "Demsodrox",
        "Dermasorb",
        "Dimexide",
        "Dipirartril-tropico",
        "Dolicur",
        "Doligur",
        "Domoso",
        "Dromisol",
        "Durasorb",
        "Gamasol 90",
        "Hyadur",
        "Infiltrina",
        "Kemsol",
        "Rimso 50",
        "Sclerosol",
        "Somipront",
        "Syntexan",
    ],
)
MolecularEntity.dinitrogen = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/dinitrogen",
    definition="An elemental molecule consisting of two trivalently-bonded nitrogen atoms. [adapted from ChEBI (https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:17997)]",
    description="At standard temperature and pressure, two atoms of the element nitrogen bond to form N2, a colorless and odorless diatomic gas. N2 forms about 78% of Earth's atmosphere, making it the most abundant uncombined element in air. Because of the volatility of nitrogen compounds, nitrogen is relatively rare in the solid parts of the Earth. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Nitrogen)]",
    name="dinitrogen",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_17997",
    synonyms=["N2", "nitrogen", "N≡N"],
)
MolecularEntity.dioxygen = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/dioxygen",
    definition="The common allotrope of elemental oxygen on Earth, O2, is generally known as oxygen. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Allotropes_of_oxygen)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0398707",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:15379#dioxygen",
    name="dioxygen",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_15379",
    synonyms=["oxygen", "O2", "diatomic oxygen", "molecular oxygen", "dioxidene", "oxygen gas"],
)
MolecularEntity.dopamine = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/dopamine",
    definition="Dopamine is one of the catecholamine neurotransmitters in the brain. It is derived from tyrosine and is the precursor to norepinephrine and epinephrine.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103384",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:18243#dopamine",
    name="dopamine",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_18243",
    synonyms=["DA", "deoxyepinephrine", "dopamin", "dopamine HCl", "hydroxyltyramine"],
)
MolecularEntity.dopamine_transporter = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/dopamineTransporter",
    definition="A 'dopamine transporter' is a membrane-spanning protein that pumps the neurotransmitter dopamine out of the synaptic cleft back into cytosol.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103388",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXMOL:20090512#dopamine-transporter",
    name="dopamine transporter",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000015188",
    synonyms=["DAT", "dopamine active transporter"],
)
MolecularEntity.dynorphin = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/dynorphin",
    definition="Dynorphin belongs to a class of opioid peptides that arise from the precursor protein prodynorphin. Dynorphins bind to the kappa opioid receptor.",
    interlex_identifier="http://uri.interlex.org/ilx_0103624",
    name="dynorphin",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5097",
    synonyms=["Dyn"],
)
MolecularEntity.edetic_acid = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/edeticAcid",
    definition="Edetic Acid (Ethylenediaminetetraacetic acid, EDTA), also called edetic acid after its own abbreviation, is an aminopolycarboxylic acid with the formula [CH2N(CH2CO2H)2]2. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Ethylenediaminetetraacetic_acid)]",
    description="This white, water-soluble solid is widely used to bind to iron (Fe2+/Fe3+) and calcium ions (Ca2+), forming water-soluble complexes even at neutral pH. It is thus used to dissolve Fe- and Ca-containing scale as well as to deliver iron ions under conditions where its oxides are insoluble. EDTA is available as several salts, notably disodium EDTA, sodium calcium edetate, and tetrasodium EDTA, but these all function similarly. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Ethylenediaminetetraacetic_acid)]",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:4735#ethylene-glycol-bis-2-aminoethyl-tetraacetic-acid",
    name="edetic acid",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_4735",
    synonyms=[
        "EGTA",
        "edetic acid",
        "(ethylenedinitrilo)tetraacetic acid",
        "2,2',2'',2'''-(ethane-1,2-diylbis(azanetriyl))tetraacetic acid",
        "2,2',2'',2'''-(ethane-1,2-diyldinitrilo)tetraacetic acid",
        "2-([2-[bis(carboxymethyl)amino]ethyl](carboxymethyl)amino)acetic acid",
        "edathamil",
        "EDTA (chelating agent)",
        "ethylene-N,N'-biscarboxymethyl-N,N'-diglycine",
        "ethylenediamine-N,N,N',N'-tetraacetic acid",
        "ethylenediaminetetraacetic acid",
        "ethylenedinitrilotetraacetic acid",
        "H4edta",
        "N,N'-1,2-Ethane diylbis-(N-(carboxymethyl)glycine)",
        "N,N'-1,2-ethanediylbis[N-(carboxymethyl)glycine]",
        "{[-(BIS-CARBOXYMETHYL-AMINO)-ETHYL]-CARBOXYMETHYL-AMINO}-ACETIC",
    ],
)
MolecularEntity.egtazic_acid = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/EgtazicAcid",
    definition="EGTA (ethylene glycol-bis(β-aminoethyl ether)-N,N,N',N'-tetraacetic acid), also known as egtazic acid (INN, USAN), is an aminopolycarboxylic acid, a chelating agent. [adapted from Wikipedia (https://en.wikipedia.org/wiki/EGTA_(chemical))]",
    description="EGTA is a white solid that is related to the better known EDTA. Compared to EDTA, it has a lower affinity for magnesium, making it more selective for calcium ions. It is useful in buffer solutions that resemble the environment in living cells where calcium ions are usually at least a thousandfold less concentrated than magnesium. [adapted from Wikipedia (https://en.wikipedia.org/wiki/EGTA_(chemical))]",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:30740#ethylene-glycol-bis-2-aminoethyl-tetraacetic-acid",
    name="egtazic acid",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_30740",
    synonyms=[
        "3,12-bis(carboxymethyl)-6,9-dioxa-3,12-diazatetradecanedioic acid",
        "[ethylenebis(oxyethylenenitrilo)]tetraacetic acid",
        "EGTA",
        "ethylene glycol bis(β-aminoethyl ether)-N,N,N',N'-tetraacetic acid",
        "ethylene glycol-O,O'-bis(2-aminoethyl)-N,N,N',N'-tetraacetic acid",
        "H4egta",
    ],
)
MolecularEntity.enkephalin = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/enkephalin",
    definition="Enkephalin is a pentapeptide involved in regulating nociception in the body.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103826",
    name="enkephalin",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5096",
    synonyms=["Enk"],
)
MolecularEntity.epibatidine = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/epibatidine",
    definition="Epibatidine is a chlorinated alkaloid that binds to nicotinic and muscarinic acetylcholine receptors with high affinity.",
    interlex_identifier="http://uri.interlex.org/ilx_0103884",
    name="epibatidine",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_chem_20090204",
)
MolecularEntity.ethanol = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/ethanol",
    definition="Ethanol (also called ethyl alcohol, grain alcohol, drinking alcohol, or simply alcohol) is an organic compound with the chemical formula CH3CH2OH. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Ethanol)]",
    description="Ethanol is an alcohol, with its formula also written as C2H5OH, C2H6O or EtOH, where Et stands for ethyl. Ethanol is a volatile, flammable, colorless liquid with a characteristic wine-like odor and pungent taste. It is a psychoactive recreational drug, and the active ingredient in alcoholic drinks. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Ethanol)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103948",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:16236#ethanol",
    name="ethanol",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_16236",
    synonyms=[
        "absolute alcohol",
        "alcohol",
        "Cologne spirit",
        "drinking alcohol",
        "ethylic alcohol",
        "EtOH",
        "ethyl alcohol",
        "ethyl hydroxide",
        "ethylene hydrate",
        "ethylol",
        "grain alcohol",
        "hydroxyethane",
        "methylcarbinol",
    ],
)
MolecularEntity.excitatory_amino_acid_transporter = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/excitatoryAminoAcidTransporter",
    definition="The excitatory amino acid transporters are a subclass of glutamate transporters that remove glutamate from the synaptic cleft and extrasynaptic sites via glutamate reuptake into glial cells and neurons.",
    name="excitatory amino acid transporter",
    synonyms=["EAAT"],
)
MolecularEntity.excitatory_amino_acid_transporter1 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/excitatoryAminoAcidTransporter1",
    definition="The excitatory amino acid transporter 1 belongs to the EAAT family. It is predominantly expressed in the plasma membrane removing glutamate from the extracellular space, but was also localized in the inner mitochondrial membrane as part of the malate-aspartate shuttle.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103639",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000014974#excitatory-amino-acid-transporter-1",
    name="excitatory amino acid transporter 1",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_0000149744",
    synonyms=["EAAT1", "GLAST-1", "glutamate aspartate transporter 1"],
)
MolecularEntity.excitatory_amino_acid_transporter2 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/excitatoryAminoAcidTransporter2",
    definition="The excitatory amino acid transporter 2 belongs to the EAAT family. It clears the excitatory neurotransmitter glutamate from the extracellular space at synapses in the central nervous system and is responsible for over 90% of glutamate reuptake within the brain.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103640",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000014973#excitatory-amino-acid-transporter-2",
    name="excitatory amino acid transporter 2",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000014973",
    synonyms=["EAAT2", "GLT-1", "glutamate transporter 1", "SLC1A2", "solute carrier family 1 member 2"],
)
MolecularEntity.excitatory_amino_acid_transporter3 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/excitatoryAminoAcidTransporter3",
    definition="The excitatory amino acid transporter 3 belongs to the EAAT family transporting glutamate across plasma membranes in neurons. It can also transport aspartate and plays a role in the neuronal cysteine uptake.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103641",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000014972#excitatory-amino-acid-transporter-3",
    name="excitatory amino acid transporter 3",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000014972",
    synonyms=["EAAT3"],
)
MolecularEntity.excitatory_amino_acid_transporter4 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/excitatoryAminoAcidTransporter4",
    definition="The excitatory amino acid transporter 4 belongs to the EAAT family. It is expressed predominantly in the cerebellum, has high affinity for the excitatory amino acids L-aspartate and L-glutamate.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103642",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000014977#excitatory-amino-acid-transporter-4",
    name="excitatory amino acid transporter 4",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000014977",
    synonyms=["EAAT4"],
)
MolecularEntity.excitatory_amino_acid_transporter5 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/excitatoryAminoAcidTransporter5",
    definition="The excitatory amino acid transporter 5 belongs to the EAAT family. It is expressed predominantly in the retina, has high affinity for the excitatory amino acid L-glutamate.",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000014978#excitatory-amino-acid-transporter-5",
    name="excitatory amino acid transporter 5",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000014978",
    synonyms=["EAAT5"],
)
MolecularEntity.five_ht1_a_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/5-HT1AReceptor",
    definition="The 5-HT1A receptor is a subtype of serotonin receptor group (5-HT receptors) that bind the neurotransmitter serotonin (5-hydroxytryptamine, 5-HT).",
    interlex_identifier="http://uri.interlex.org/ilx_0100033",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:5891#5-ht1a-receptor-2",
    name="5-HT1A receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5890",
    synonyms=["1A receptor", "5-HT1A", "5-HT1A serotonin receptor", "serotonin 1A receptor"],
)
MolecularEntity.five_ht1_b_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/5-HT1BReceptor",
    definition="The 5-HT1B receptor is a subtype of serotonin receptor group (5-HT receptors) that bind the neurotransmitter serotonin (5-hydroxytryptamine, 5-HT).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0100034",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:6386#5-ht1b-receptor-3",
    name="5-HT1B receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_6386",
    synonyms=["1B receptor", "5-HT1B", "5-HT1B serotonin receptor", "serotonin 1B receptor"],
)
MolecularEntity.five_ht2_a_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/5-HT2AReceptor",
    definition="The 5-HT2A receptor is a subtype of serotonin receptor group (5-HT receptors) that bind the neurotransmitter serotonin (5-hydroxytryptamine, 5-HT).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0100038",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:6742#5-ht2a-receptor-1",
    name="5-HT2A receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_6741",
    synonyms=["2A receptor", "5-HT2A", "5-HT2A serotonin receptor", "serotonin 2A receptor"],
)
MolecularEntity.five_ht2_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/5-HT2Receptor",
    definition="The 5-HT2 receptor is a subtype of serotonin receptor group (5-HT receptors) that bind the neurotransmitter serotonin (5-hydroxytryptamine, 5-HT).",
    interlex_identifier="http://uri.interlex.org/ilx_0492260",
    name="5-HT2 receptor",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0018621",
    synonyms=["5-HT2", "5-HT2 serotonin receptor"],
)
MolecularEntity.five_ht4_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/5-HT4Receptor",
    definition="The 5-HT4 receptor is a subtype of serotonin receptor group (5-HT receptors) that bind the neurotransmitter serotonin (5-hydroxytryptamine, 5-HT).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0100041",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:6151#5-ht4-receptor-1",
    name="5-HT4 receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_6151",
    synonyms=["5-HT4", "5-HT4 serotonin receptor", "5-hydroxytryptamine 4 receptor", "serotonin receptor 4"],
)
MolecularEntity.five_ht_transporter = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/5-HTTransporter",
    definition="The 5-HT transporter is a type of monoamine transporter protein that transports the neurotransmitter serotonin (5-hydroxytryptamine, 5-HT) from the synaptic cleft back to the presynaptic neuron.",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000015189#sodium-dependent-serotonin-transporter",
    name="5-HT transporter",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000015189",
    synonyms=["5-HTT", "SERT", "sodium-dependent serotonin transporter"],
)
MolecularEntity.flumazenil = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/flumazenil",
    definition="Flumazenil is a selective GABAA receptor antagonist that binds to the benzodiazepine recognition site on the GABAA/benzodiazepine receptor complex.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0104307",
    name="flumazenil",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_5103",
)
MolecularEntity.fluorescent_microspheres = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/fluorescentMicrospheres",
    definition="Fluorescent microspheres are non-toxic, non-biologically reactive small polymers embedded with fluorescent dye which are used in medical imaging, as markers for fluorescent microscopy and as standards for flow cytometry fluorescent cell sorting.",
    name="fluorescent microspheres",
)
MolecularEntity.fluoro__emerald = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/Fluoro-Emerald",
    definition="Fluoro-Emerald is a fluorescent dextran derivative (dextran, fluorescein, 10,000 MW) used for tracing studies in the nervous system.",
    name="Fluoro-Emerald",
    synonyms=["Fluoro Emerald", "FluoroEmerald"],
)
MolecularEntity.fluoro__gold = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/Fluoro-Gold",
    definition="Fluoro-Gold is a fluorescent dye that is used as a retrograde tracer in tract tracing studies.",
    interlex_identifier="http://uri.interlex.org/ilx_0104323",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXMOL:1012018#fluorogold",
    name="Fluoro-Gold",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_30125",
    synonyms=["Fluoro Gold", "FluoroGold"],
)
MolecularEntity.fluoro__ruby = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/Fluoro-Ruby",
    definition="Fluoro-Ruby is a fluorescent dextran derivative (dextran, tetramethylrhodamine, 10,000 MW) used for retrograde tracing studies in the nervous system.",
    interlex_identifier="http://uri.interlex.org/ilx_0104322",
    knowledge_space_link="https://knowledge-space.org/wiki/NLX:65982#fluoro-ruby",
    name="Fluoro-Ruby",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_65982",
    synonyms=["Fluoro Ruby", "FluoroRuby"],
)
MolecularEntity.formaldehyde = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/formaldehyde",
    definition="Formaldehyde is an organic compound with the formula CH2O and structure H-CHO. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Formaldehyde)]",
    description="Formaldehyde is a pungent, colourless gas that polymerises spontaneously into paraformaldehyde . It is stored as aqueous solutions (formalin), which consists mainly of the hydrate CH2(OH)2. It is the simplest of the aldehydes (R-CHO). It is produced commercially as a precursor to many other materials and chemical compounds. In 2006, the global production rate of formaldehyde was estimated at 12 million tons per year. It is mainly used in the production of industrial resins, e.g., for particle board and coatings. Small amounts also occur naturally. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Formaldehyde)]",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:16842#formaldehyde",
    name="formaldehyde",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_16842",
    synonyms=[
        "methyl aldehyde",
        "methylene glycol",
        "methylene oxide",
        "formalin (aqueous solution)",
        "Formol",
        "carbonyl hydride",
        "methanone",
        "oxomethane",
        "methanal",
    ],
)
MolecularEntity.four_2_hydroxyethyl_1_piperazine_ethanesulfonic_acid = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/4-(2-hydroxyethyl)-1-piperazineEthanesulfonicAcid",
    definition="HEPES (4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid) is a zwitterionic sulfonic acid buffering agent; one of the twenty Good's buffers. [adapted from W  ikipedia (https://en.wikipedia.org/wiki/HEPES)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0484759",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:42334#2-4-2-hydroxyethyl-piperazin-1-yl-ethanesulfonic-acid",
    name="4-(2-hydroxyethyl)-1-piperazine ethanesulfonic acid",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_42334",
    synonyms=["HEPES", "2-[4-(2-hydroxyethyl)piperazin-1-yl]ethane-1-sulfonic acid"],
)
MolecularEntity.gaba_a_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/GABA-AReceptor",
    definition="The GABA-A receptor is an ionotropic subtype of the GABA receptor class that respond to the neurotransmitter gamma-aminobutyric acid (GABA) as endogenous ligand.",
    knowledge_space_link="https://knowledge-space.org/wiki/GO:1902711#gaba-a-receptor-complex",
    name="GABA-A receptor",
    synonyms=["GABA A receptor", "GABA_A", "GABAA"],
)
MolecularEntity.gaba_b_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/GABA-BReceptor",
    definition="The GABA-B receptor is a metabotropic subtype of the GABA receptor class that respond to the neurotransmitter gamma-aminobutyric acid (GABA) as endogenous ligand.",
    interlex_identifier="http://uri.interlex.org/ilx_0104503",
    name="GABA-B receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_mol_090801",
    synonyms=["GABA B receptor", "GABA_B", "GABAB"],
)
MolecularEntity.gaba_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/GABAReceptor",
    definition="The GABA receptors are a group of receptors that respond to the neurotransmitter gamma-aminobutyric acid (GABA) as endogenous ligand.",
    interlex_identifier="http://uri.interlex.org/ilx_0104502",
    knowledge_space_link="https://knowledge-space.org/wiki/GO:1902710#gaba-receptor-complex",
    name="GABA receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_mol_1006001",
    synonyms=["GABAR", "gamma-aminobutyric acid receptor"],
)
MolecularEntity.gabazine = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/gabazine",
    definition="Gabazine is a competitive and selective GABAA antagonist.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0572043",
    name="gabazine",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0142643",
    synonyms=["SR-95531"],
)
MolecularEntity.galanin = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/galanin",
    definition="Galanin is a biologically active neuropeptide, encoded by the GAL gene, that is widely distributed in the central and peripheral nervous systems and the endocrine system.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0104529",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:5074#galanin",
    name="galanin",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5074",
    synonyms=["GAL"],
)
MolecularEntity.gluconic_acid = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/gluconicAcid",
    definition="Gluconic acid is an organic compound with molecular formula C6H12O7 and condensed structural formula HOCH2(CHOH)4CO2H. [adapted from wikipedia (https://en.wikipedia.org/wiki/Gluconic_acid)]",
    description="A white solid, it is forms the gluconate anion in neutral aqueous solution. The salts of gluconic acid are known as 'gluconates'. Gluconic acid, gluconate salts, and gluconate esters occur widely in nature because such species arise from the oxidation of glucose. Some drugs are injected in the form of gluconates. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Gluconic_acid)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0402003",
    name="gluconic acid",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_33198",
    synonyms=["dextronic acid", "(2R,3S,4R,5R)-2,3,4,5,6-Pentahydroxyhexanoic acid", "HOCH2(CHOH)4CO2H"],
)
MolecularEntity.glucose = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/glucose",
    definition="Glucose is a sugar with the molecular formula C6H12O6. Glucose is overall the most abundant monosaccharide, a subcategory of carbohydrates. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Glucose)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0104670",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:17234#glucose",
    name="glucose",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_17234",
    synonyms=["D-glucopyranose", "D-glucose", "glukose", "D-gluco-hexose"],
)
MolecularEntity.glutamate = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/glutamate",
    definition="Glutamate is the carboxylate anion of glutamic acid; and the major excitatory neurotransmitter in the central nervous system of vertebrates, the peripheral nervous system of invertebrates.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0104676",
    knowledge_space_link="https://knowledge-space.org/wiki/SAO:1744435799#glutamate",
    name="glutamate",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1744435799",
    synonyms=["GLU", "Glu", "Glut", "GLUT"],
)
MolecularEntity.glutamate_transporter = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/glutamateTransporter",
    definition="The glutamate transporters are a class of transporter proteins that can move the neurotransmitter glutamate across membranes.",
    interlex_identifier="http://uri.interlex.org/ilx_0104678",
    knowledge_space_link="https://knowledge-space.org/wiki/SAO:1399894198#glutamate-transporter",
    name="glutamate transporter",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1399894198",
    synonyms=["GLT"],
)
MolecularEntity.glycerol = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/glycerol",
    definition="Glycerol is a triol with a structure of propane substituted at positions 1, 2 and 3 by hydroxy groups. [adapted from ChEBI (https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:17754)]",
    description="Glycerol, also called glycerine or glycerin, is a simple triol compound. It is a colorless, odorless, viscous liquid that is sweet-tasting and non-toxic. The glycerol backbone is found in lipids known as glycerides. Because it has antimicrobial and antiviral properties, it is widely used in wound and burn treatments approved by the U.S. Food and Drug Administration. Conversely, it is also used as a bacterial culture medium. Its presence in blood can be used as an effective marker to measure liver disease. It is also widely used as a sweetener in the food industry and as a humectant in pharmaceutical formulations. Because of its three hydroxyl groups, glycerol is miscible with water and is hygroscopic in nature. [adapted from wikipedia (https://en.wikipedia.org/wiki/Glycerol)]",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:17754#glycerol",
    name="glycerol",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_17754",
    synonyms=["glycerin", "glycerine", "1,2,3-trioxypropane", "1,2,3-trihydroxypropane", "1,2,3-propanetriol"],
)
MolecularEntity.glycine_transporter2 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/glycineTransporter2",
    definition="The glycine transporter 2 is a member of the Na+ and Cl−-coupled transporter family SLC6 that recaptures the inhibitory transmitter glycine in the spinal cord and brainstem.",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000015190#sodium-and-chloride-dependent-glycine-transporter-2",
    name="glycine transporter 2",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000015190",
    synonyms=["glycine transporter type 2", "GlyT2", "sodium- and chloride-dependent glycine transporter 2"],
)
MolecularEntity.growth_factor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/growthFactor",
    definition="The 'growth factor' comprises signal molecules that are involved in the control of cell growth and differentiation.",
    interlex_identifier="http://uri.interlex.org/ilx_0104801",
    name="growth factor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/sao1671627152",
    synonyms=["GF"],
)
MolecularEntity.halothane = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/Halothane",
    definition="Halothane is a haloalkane comprising ethane having three fluoro substituents at the 1-position as well as bromo- and chloro substituents at the 2-position. It has a role as an inhalation anaesthetic. It is a haloalkane, an organofluorine compound, an organochlorine compound and an organobromine compound.[adapted from ChEBI (https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:5615)]",
    name="halothane",
    preferred_ontology_identifier="https://pubchem.ncbi.nlm.nih.gov/compound/3562",
    synonyms=[
        "1,1,1-trifluoro-2-bromo-2-chloroethane",
        "1,1,1-trifluoro-2-chloro-2-bromoethane",
        "1-bromo-1-chloro-2,2,2-trifluoroethane",
        "2,2,2-trifluoro-1-chloro-1-bromoethane",
        "2-bromo-2-chloro-1,1,1-trifluoroethane",
        "bromochlorotrifluoroethane",
        "fluothane",
        "Narcotane",
        "Phthorothanum",
        "Rhodialothan",
    ],
)
MolecularEntity.histamine = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/histamine",
    definition="Histamine is produced by basophils and mast cells (in connective tissues). It is involved in local immune responses and regulating physiological function in the gut and acts as a neurotransmitter (adapted from Wikipedia).",
    interlex_identifier="http://uri.interlex.org/base/ilx_0105065",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:5016#histamine",
    name="histamine",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5016",
)
MolecularEntity.insulin_like_growth_factor1 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/insulinLikeGrowthFactor1",
    definition="The term 'insulin-like growth factor' names a set of proteins with high sequence similarity to insulin that are part of a complex system that cells use to communicate with their physiologic environment. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Insulin-like_growth_factor)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0105523",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000009182#insulin-like-growth-factor-i",
    name="insulin-like growth factor 1",
    synonyms=["IGF-1", "Igf-1", "IGF-I", "Igf-I", "IGF1", "Igf1", "insulin-like growth factor I"],
)
MolecularEntity.intrabody = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/intrabody",
    definition="An 'intrabody' is an antibody that works within the cell to bind an intracellular protein.",
    name="intrabody",
)
MolecularEntity.ionotropic_glutamate_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/ionotropicGlutamateReceptor",
    definition="Ionotropic glutamate receptors are a class of ligand-gated ion channels that are activated by the neurotransmitter glutamate as endogenous ligand.",
    interlex_identifier="http://uri.interlex.org/ilx_0105706",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXMOL:20090501#ionotropic-glutamate-receptor",
    name="ionotropic glutamate receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_mol_20090501",
    synonyms=["iGluR"],
)
MolecularEntity.iperoxo = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/iperoxo",
    definition="Iperoxo is an organic chemical molecule that is used as a muscarinic M2 receptor agonist.",
    interlex_identifier="http://uri.interlex.org/ilx_0630403",
    name="iperoxo",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M000598130",
    synonyms=["4-[(4,5-Dihydro-3-isoxazolyl)oxy]-N,N,N-trimethyl-2-butyn-1-aminium iodide"],
)
MolecularEntity.iron = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/iron",
    definition="Iron is a chemical element; it has symbol Fe (from Latin ferrum 'iron') and atomic number 26. [adapted from wikipedia (https://en.wikipedia.org/wiki/Iron)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0105721",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:24873#iron-molecular-entity",
    name="iron",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_24873",
    synonyms=["Fe", "Ferrum"],
)
MolecularEntity.isoflurane = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/isoflurane",
    definition="Isoflurane is a stable, non-explosive inhalation anesthetic, relatively free from significant side effects.",
    interlex_identifier="http://uri.interlex.org/ilx_0105740",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:6015#isoflurane",
    name="isoflurane",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_6015",
    synonyms=["Aerrane", "Ethane", "Forane", "Forene"],
)
MolecularEntity.jnk_map_kinase_scaffold_protein2 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/JNKMapKinaseScaffoldProtein2",
    definition="The JNK MAP kinase scaffold protein 2 is a protein that is a translation product of the human MAPK8IP2 gene or a 1:1 ortholog thereof.",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000010161#c-jun-amino-terminal-kinase-interacting-protein-2",
    name="JNK MAP kinase scaffold protein 2",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000010161",
    synonyms=[
        "C-Jun-amino-terminal kinase-interacting protein 2",
        "IB-2 ",
        "JIP-2",
        "JNK-interacting protein 2",
        "islet-brain-2",
        "mitogen-activated protein kinase 8-interacting protein 2",
    ],
)
MolecularEntity.kainate_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/kainateReceptor",
    definition="The kainate receptors belong to the class of ionotropic glutamate receptors that can be involved in excitatory neurotransmission (postsynaptic) as well as inhibitory neurotransmission (presynaptic).",
    interlex_identifier="http://uri.interlex.org/ilx_0105822",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:5252#kainate-glutamate-gated-cationic-channel",
    name="kainate receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5252",
    synonyms=[
        "ionotropic glutamate kainate receptor",
        "ionotropic kainate receptor",
        "kainate glutamate-gated cationic channel",
        "kainic acid receptor",
        "KAR",
    ],
)
MolecularEntity.kallikrein_related_peptidase8 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/kallikrein-relatedPeptidase8",
    definition="The kallikrein-related peptidase 8 is a protein that is a translation product of the mouse Klk1b8 gene or a 1:1 ortholog thereof.",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000009614#kallikrein-1-related-peptidase-b8",
    name="kallikrein-related peptidase 8",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000009614",
    synonyms=["KLK8", "neuropsin", "Nop"],
)
MolecularEntity.ketamine = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/ketamine",
    definition="Ketamine is a cyclohexanone derivative used for induction of anesthesia.",
    interlex_identifier="http://uri.interlex.org/ilx_0105850",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFSTD:DB01221#ketamine",
    name="ketamine",
    preferred_ontology_identifier="https://www.drugbank.ca/drugs/DB01221",
    synonyms=[
        "(-)-ketamine",
        "(S)-(-)-ketamine",
        "(S)-ketamine",
        "Cl 581 base",
        "esketamine",
        "I-ketamine",
        "ketaject",
        "ketalar",
        "ketalor",
        "ketanest",
    ],
)
MolecularEntity.lucifer_yellow = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/luciferYellow",
    definition="Lucifer yellow is a fluorescent dye used that it can be readily visualized in both living and fixed cells using a fluorescence microscope.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0439021",
    name="lucifer yellow",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0068243",
    synonyms=["LY"],
)
MolecularEntity.m1_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/M1Receptor",
    definition="The M1 receptor belongs to the family of muscarinic receptors which are activated by acetylcholine as endegenous ligand. It mediates slow excitatory postsynaptic potential in the postganglionic nerve and is also expressed in exocrine glands and in the central nervous system.",
    interlex_identifier="http://uri.interlex.org/ilx_0106429",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:7352#m1-receptor-1",
    name="M1 receptor",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000001613",
    synonyms=[
        "cholinergic receptor, muscarinic 1",
        "M1",
        "M1 acetylcholine receptor",
        "M1 AChR",
        "muscarinic acetylcholine receptor 1",
        "muscarinic acetylcholine receptor M1",
        "muscarinic acetylcholine receptor type 1",
    ],
)
MolecularEntity.m2_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/M2Receptor",
    definition="The M2 receptor belongs to the family of muscarinic receptors which are activated by acetylcholine as endegenous ligand. It is expressed in cardiac tissues and acts to slow the heart rate to normal after sympathetic nervous system stimulation.",
    interlex_identifier="http://uri.interlex.org/ilx_0106430",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:7953#m2-receptor-2",
    name="M2 receptor",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000001614",
    synonyms=[
        "M2",
        "M2 acetylcholine receptor",
        "M2 AChR",
        "muscarinic acetylcholine receptor 2",
        "muscarinic acetylcholine receptor M2",
        "muscarinic acetylcholine receptor type 2",
    ],
)
MolecularEntity.m3_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/M3Receptor",
    definition="The M3 receptor belongs to the family of muscarinic receptors which are activated by acetylcholine as endegenous ligand. It is expressed in many glands, in lungs, and in the smooth muscles of blood vessels.",
    interlex_identifier="http://uri.interlex.org/ilx_0106431",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:6135#m3-receptor",
    name="M3 receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_6131",
    synonyms=[
        "M3",
        "M3 acetylcholine receptor",
        "M3 AChR",
        "muscarinic acetylcholine receptor 3",
        "muscarinic acetylcholine receptor M3",
        "muscarinic acetylcholine receptor type 3",
    ],
)
MolecularEntity.magnesium_atp = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/magnesiumATP",
    definition="An ATP binded to magnesium ion (Mg2+) to compose biologically functional form, and most of intracellular ATP and Mg2+ assumed to form Mg-ATP complexes. [adapted from Yamanaka et al. Mitochondrial Mg(2+) homeostasis decides cellular energy metabolism and vulnerability to stress. Sci Rep. 2016 Jul 26;6:30027. doi: 10.1038/srep30027]",
    name="magnesium ATP",
    preferred_ontology_identifier="https://pubchem.ncbi.nlm.nih.gov/compound/15126",
    synonyms=["MgATP"],
)
MolecularEntity.magnesium_chloride = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/magnesiumChloride",
    definition="A magnesium salt comprising of two chlorine atoms bound to a magnesium atom. [adapted from ChEBI (https://www.ebi.ac.uk/chebi/searchId.do?chebiId=CHEBI:6636)]",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:6636#magnesium-dichloride",
    name="magnesium chloride",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_6636",
    synonyms=["MgCl2", "E511"],
)
MolecularEntity.magnesium_sulfate = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/magnesiumSulfate",
    definition="A magnesium salt with the formula MgSO4, consisting of magnesium cations Mg2+ (20.19% by mass) and sulfate anions (SO4)2-. [adapted from wikipedia (https://en.wikipedia.org/wiki/Magnesium_sulfate)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0106452",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:32599#magnesium-sulfate",
    name="magnesium sulfate",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_32599",
    synonyms=[
        "MgSO4",
        "bitter salt",
        "bath salt",
        "magnesium sulphate hydrate",
        "magnesium sulfate anhydrous",
        "magnesium sulfate dried",
        "magnesium sulfate heptahydrate",
        "Elliotts B Solution",
        "Epsom salts",
        "English salt",
        "hair salt",
        "Kieserite (as monohydrate)",
        "Sal amarum",
        "Sal anglicum",
        "Sal catharticum",
        "Sal seidlitense",
        "Salts of England",
    ],
)
MolecularEntity.medetomidine = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/medetomidine",
    definition="Medetomidine is a synthetic drug used as both a surgical anesthetic and analgesic.",
    interlex_identifier="http://uri.interlex.org/ilx_0488544",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:48552#medetomidine",
    name="medetomidine",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_48552",
)
MolecularEntity.metabotropic_glutamate_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/metabotropicGlutamateReceptor",
    definition="Metabotropic glutamate receptors are active through an indirect metabotropic process and respond to glutamate as endogenous ligand.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0106829",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXMOL:20090503#metabotropic-glutamate-receptor",
    name="metabotropic glutamate receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_mol_20090503",
    synonyms=["glutamate metabotropic", "GRM", "mGluR", "mGluRs"],
)
MolecularEntity.metabotropic_glutamate_receptor1 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/metabotropicGlutamateReceptor1",
    definition="The metabotropic glutamate receptor 1 belongs to group I of the MGluR family.",
    interlex_identifier="http://uri.interlex.org/ilx_0106891",
    name="metabotropic glutamate receptor 1",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_mol_20090504",
    synonyms=["glutamate metabotropic 1", "glutamate metabotropic receptor 1", "GRM1", "MGluR1"],
)
MolecularEntity.metabotropic_glutamate_receptor2 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/metabotropicGlutamateReceptor2",
    definition="The metabotropic glutamate receptor 2 belongs to group II of the MGluR family. When activated by its endogenous ligand glutamate, it inhibits the emptying of vesicular contents at the presynaptic terminal of glutamatergic neurons.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0106892",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000008264#metabotropic-glutamate-receptor-2",
    name="metabotropic glutamate receptor 2",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_mol_20090505",
    synonyms=["glutamate metabotropic 2", "glutamate metabotropic receptor 2", "GRM2", "MGluR2"],
)
MolecularEntity.metabotropic_glutamate_receptor3 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/metabotropicGlutamateReceptor3",
    definition="The metabotropic glutamate receptor 3 belongs to group II of the MGluR family. When activated by its endogenous ligand glutamate, it inhibits the emptying of vesicular contents at the presynaptic terminal of glutamatergic neurons.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0106893",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000008265#metabotropic-glutamate-receptor-3",
    name="metabotropic glutamate receptor 3",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_mol_20090506",
    synonyms=["glutamate metabotropic 3", "glutamate metabotropic receptor 3", "GRM3", "MGluR3"],
)
MolecularEntity.metabotropic_glutamate_receptor5 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/metabotropicGlutamateReceptor5",
    definition="The metabotropic glutamate receptor 5 belongs to group I of the MGluR family.",
    interlex_identifier="http://uri.interlex.org/ilx_0106895",
    name="metabotropic glutamate receptor 5",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_mol_20090508",
    synonyms=["glutamate metabotropic 5", "glutamate metabotropic receptor 5", "GRM5", "MGluR5"],
)
MolecularEntity.methanol = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/methanol",
    definition="Methanol is an organic chemical and the simplest aliphatic alcohol, with the formula CH3OH (a methyl group linked to a hydroxyl group, often abbreviated as MeOH). [adapted from Wikipedia (https://en.wikipedia.org/wiki/Methanol)]",
    description="Methanol is a light, volatile, colorless and flammable liquid with a distinctive alcoholic odour similar to that of ethanol (potable alcohol). Methanol acquired the name wood alcohol because it was once produced chiefly by the destructive distillation of wood. Today, methanol is mainly produced industrially by hydrogenation of carbon monoxide. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Methanol)]",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:17790#methanol",
    name="methanol",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_17790",
    synonyms=[
        "Carbinol",
        "Columbian spirits",
        "hydroxymethane",
        "MeOH",
        "methyl alcohol",
        "methyl hydroxide",
        "methylic alcohol",
        "methylol",
        "methylene hydrate, primary alcohol",
        "pyroligneous spirit",
        "wood alcohol",
        "wood naphtha",
        "wood spirit",
    ],
)
MolecularEntity.monosodium_phosphate = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/monosodiumPhosphate",
    definition="Monosodium phosphate (MSP), is an inorganic compound of sodium with a dihydrogen phosphate (H2PO4) anion. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Monosodium_phosphate)]",
    description="Monosodium phosphate, one of many sodium phosphates, it is a common industrial chemical. The salt exists in an anhydrous form, as well as mono- and dihydrates. [adapted from Wikipedia (https://en.wikipedia.org/wiki/Monosodium_phosphate)]",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:37585#sodium-dihydrogenphosphate",
    name="monosodium phosphate",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_37585",
    synonyms=[
        "sodium dihydrogen phosphate",
        "MSP",
        "monobasic sodium phosphate",
        "sodium dihydrogen phosphate",
        "sodium biphosphate",
        "NaH2PO4",
        "phosphoric acid, monosodium salt",
        "E339",
    ],
)
MolecularEntity.muscimol = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/muscimol",
    definition="Muscimol is a potent and selective orthosteric agonist for the GABAA receptors and displays sedative-hypnotic, depressant and hallucinogenic psychoactivity",
    interlex_identifier="http://uri.interlex.org/base/ilx_0485557",
    name="muscimol",
    preferred_ontology_identifier="http://id.nlm.nih.gov/mesh/2018/M0014231",
    synonyms=["agarin", "pantherine"],
)
MolecularEntity.neurobiotin = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/neurobiotin",
    definition="Neurobiotin is a biotin derivative with moleular weight 286 kDa that can be used as an anterograde and retrograde tracer in the nervous system.",
    interlex_identifier="http://uri.interlex.org/ilx_0107453",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXMOL:1012015#neurobiotin",
    name="neurobiotin",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_157299",
)
MolecularEntity.neuroligin_3 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/neuroligin-3",
    definition="Neuroligin-3 is a protein that is a translation product of the NLGN3 gene or a 1:1 ortholog thereof.",
    interlex_identifier="http://uri.interlex.org/ilx_0107485",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000011256#neuroligin-3",
    name="neuroligin-3",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000011256",
    synonyms=["gliotactin homolog", "KIAA1480", "NL3", "NLGN3"],
)
MolecularEntity.neuronal_nuclear_antigen = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/neuronalNuclearAntigen",
    definition="Neuronal nuclear antigen is a 46/48KD DNA-binding, neuron-specific protein found in nuclei which is present in most vertebrate CNS and PNS neuronal cell types.",
    interlex_identifier="http://uri.interlex.org/ilx_0107517",
    name="neuronal nuclear antigen",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nlx_152221",
    synonyms=["NeuN"],
)
MolecularEntity.neurotrophic_factor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/neurotrophicFactor",
    definition="The 'neurotrophic factor' is a family of biomolecules that support growth, survival, and differentiation of both developing and mature neurons.",
    name="neurotrophic factor",
    synonyms=["NTF"],
)
MolecularEntity.nickel = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/nickel",
    definition="Nickel is a chemical element; it has symbol Ni and atomic number 28.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0107575",
    name="nickel",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_28112",
    synonyms=["Ni", "niccolum"],
)
MolecularEntity.nmda_receptor = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/NMDAReceptor",
    definition="The NMDA receptors belong to the class of ionotropic glutamate receptors which can be activated with glutamate and glycine with a voltage-dependent current flow. The blockage of the activated channel through extracellular magnesium (Mg2+) and zinc (Zn2+) ions can only be removed when the neuron is sufficiently depolarized.",
    interlex_identifier="http://uri.interlex.org/ilx_0107622",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:5250#nmda-type-glutamate-gated-cationic-channel",
    name="NMDA receptor",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_5250",
    synonyms=[
        "ionotropic glutamate N-methyl-D-aspartate receptor",
        "ionotropic glutamate NMDA receptor",
        "ionotropic NMDA receptor",
        "NMDA-type glutamate-gated cationic channel",
        "NMDAR",
    ],
)
MolecularEntity.parvalbumin = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/parvalbumin",
    definition="Parvalbumin is a calcium-binding albumin protein with low molecular weight (typically 9-11 kDa).",
    interlex_identifier="http://uri.interlex.org/ilx_0108558",
    knowledge_space_link="https://knowledge-space.org/wiki/NIFEXT:6#parvalbumin",
    name="parvalbumin",
    preferred_ontology_identifier="http://uri.neuinfo.org/nif/nifstd/nifext_6",
    synonyms=["PV", "Pvalb"],
)
MolecularEntity.pentobarbital = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/pentobarbital",
    definition="A member of the class of barbiturates, the structure of which is that of barbituric acid substituted at C-5 by ethyl and sec-pentyl groups.",
    description="A short-acting barbiturate that is effective as a sedative and hypnotic (but not as an anti-anxiety) agent and is usually given orally. It is prescribed more frequently for sleep induction than for sedation but, like similar agents, may lose its effectiveness by the second week of continued administration. (From AMA Drug Evaluations Annual,1994, p236) Pharmacology: Pentobarbital, a barbiturate, is used for the treatment of short term insomnia. It belongs to a group of medicines called central nervous system (CNS) depressants that induce drowsiness and relieve tension or nervousness. Little analgesia is conferred by barbiturates; their use in the presence of pain may result in excitation. Mechanism of action: Pentobarbital binds at a distinct binding site associated with a Cl- ionopore at the GABAA receptor, increasing the duration of time for which the Cl- ionopore is open. The post-synaptic inhibitory effect of GABA in the thalamus is, therefore, prolonged. All of these effects are associated with marked decreases in GABA-sensitive neuronal calcium conductance (gCa). The net result of barbiturate action is acute potentiation of inhibitory GABAergic tone. Barbiturates also act through potent (if less well characterized) and direct inhibition of excitatory AMPA-type glutamate receptors, resulting in a profound suppression of glutamatergic neurotransmission. Drug type: Approved. Small Molecule. Drug category: Adjuvants, Anesthesia. Barbiturates. GABA Modulators. Hypnotics and Sedatives",
    interlex_identifier="http://uri.interlex.org/base/ilx_0108667",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:7983#pentobarbital",
    name="pentobarbital",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_7983",
    synonyms=[
        "pentabarbital",
        "pentabarbitone",
        "pentobarbital Sodium",
        "pentobarbitone",
        "pentobarbiturate",
        "pentobarbituric acid",
        "sodium pentobarbital",
        "Dorxssital",
        "Ethaminal",
        "Mebubarbital",
        "Mebumal",
        "Nebralin",
        "Nembutal",
        "Nembutal Sodium",
        "Neodorm",
    ],
)
MolecularEntity.pentobarbital_sodium = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/pentobarbitalSodium",
    definition="Sodium salt of pentobarbital, which is most common form of pentobarbital.",
    name="pentobarbital sodium",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_7984",
    synonyms=["Nembutal"],
)
MolecularEntity.potassium_chloride = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/potassiumChloride",
    definition="A metal chloride salt with a K(+) counterion.",
    description="Potassium chloride (KCl, or potassium salt) is a metal halide salt composed of potassium and chlorine. It is odorless and has a white or colorless vitreous crystal appearance.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0109170",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:32588#potassium-chloride",
    name="potassium chloride",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_32588",
    synonyms=["KCl", "Sylvite", "muriate of potash", "E508"],
)
MolecularEntity.potassium_gluconate = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/potassiumGluconate",
    definition="Potassium gluconate is the potassium salt of the conjugate base of gluconic acid.",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:32032#potassium-gluconate",
    name="potassium gluconate",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_32032",
    synonyms=[],
)
MolecularEntity.propofol = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/propofol",
    definition="An intravenous anesthetic agent which has the advantage of a very rapid onset after infusion or bolus injection plus a very short recovery period of a couple of minutes. (From Smith and Reynard, Textbook of Pharmacology, 1992, 1st ed, p206)",
    description="Pharmacology: Propofol a sedative-hypnotic agent for use in the induction and maintenance of anesthesia or sedation. Intravenous injection of a therapeutic dose of propofol produces hypnosis rapidly with minimal excitation, usually within 40 seconds from the start of an injection (the time for one arm-brain circulation). Mechanism of action: The action of propofol involves a positive modulation of the inhibitory function of the neurotransmitter gama-aminobutyric acid(GABA) through GABA-A receptors. Drug type: Approved. Investigational. Small Molecule. Drug category: Anesthetics, Intravenous. Anticonvulsants. Antiemetics. Free Radical Scavengers. Hypnotics and Sedatives",
    interlex_identifier="http://uri.interlex.org/ilx_0109431",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:44915#propofol",
    name="propofol",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_44915",
    synonyms=["2,6-Diisopropylphenol", "Diisopropylphenol", "propofol", "Diprivan", "Disoprivan", "Disoprofol"],
)
MolecularEntity.silicon_dioxide = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/siliconDioxide",
    definition="Silicon dioxide, also known as silica, is an oxide of silicon with the chemical formula SiO2, commonly found in nature as quartz.",
    description="In many parts of the world, silica is the major constituent of sand. Silica is abundant as it comprises several minerals and as a synthetic products. All forms are white or colorless, although impure samples can be colored.  Silicon dioxide is a common fundamental constituent of glass.",
    name="silicon dioxide",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_30563",
    synonyms=[
        "quartz",
        "silica",
        "silicic oxide",
        "silicon(IV) oxide",
        "crystalline silica",
        "pure Silica",
        "silicea",
        "silica sand",
    ],
)
MolecularEntity.silver_ammonium = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/silverAmmonium",
    definition="Silver ammonium is an inorganic compound with chemical formula AgNH4.",
    name="Silver ammonium",
    preferred_ontology_identifier="https://pubchem.ncbi.nlm.nih.gov/compound/57440423",
    synonyms=[],
)
MolecularEntity.silver_nitrate = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/silverNitrate",
    definition="Silver nitrate is an inorganic compound with chemical formula AgNO3.",
    description="Silver nitrate is a versatile precursor to many other silver compounds, such as those used in photography. It is far less sensitive to light than the halides. It was once called lunar caustic because silver was called luna by ancient alchemists who associated silver with the moon. In solid silver nitrate, the silver ions are three-coordinated in a trigonal planar arrangement.",
    name="Silver nitrate",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_32130",
    synonyms=["Silver(I) nitrate", "Nitric acid silver(1+) salt", "Lapis infernalis", "Argentous nitrate"],
)
MolecularEntity.sixcomma7_dinitro_1comma4_dihydroquinoxaline_2comma3_dione = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/6,7-dinitro-1,4-dihydroquinoxaline-2,3-dione",
    definition="DNQX (6,7-dinitroquinoxaline-2,3-dione) is a competitive antagonist at AMPA and kainate receptors, two ionotropic glutamate receptor (iGluR) subfamilies. [adapted from Wikipedia (https://en.wikipedia.org/wiki/DNQX)]",
    description="DNQX (6,7-dinitroquinoxaline-2,3-dione) is used in a variety of molecular biology subfields, notably neurophysiology, to assist researchers in determining the properties of various types of ion channels and their potential applications in medicine. [adapted from Wikipedia (https://en.wikipedia.org/wiki/DNQX)]",
    interlex_identifier="http://uri.interlex.org/base/ilx_0103368",
    name="6,7-dinitro-1,4-dihydroquinoxaline-2,3-dione",
    preferred_ontology_identifier="https://pubchem.ncbi.nlm.nih.gov/compound/3899541",
    synonyms=["DNQX", "6,7-dinitroquinoxaline-2,3-dione"],
)
MolecularEntity.sodium_bicarbonate = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/sodiumBicarbonate",
    definition="A white, crystalline powder that is commonly used as a pH buffering agent, an electrolyte replenisher, systemic alkalizer and in topical cleansing solutions.",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:32139#sodium-hydrogencarbonate",
    name="sodium bicarbonate",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_32139",
    synonyms=[
        "bicarbonate, sodium",
        "carbonic acid monosodium salt",
        "sodium hydrogen carbonate",
        "hydrogen carbonate, sodium",
        "sodium hydrogencarbonate",
        "bicarbonate of soda",
        "baking soda",
        "soda, baking",
        "NaHCO3",
        "E500",
    ],
)
MolecularEntity.sodium_chloride = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/sodiumChloride",
    definition="Sodium chloride commonly known as table salt, is an ionic compound with the chemical formula NaCl, representing a 1:1 ratio of sodium and chloride ions.",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:26710#sodium-chloride",
    name="sodium chloride",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_26710",
    synonyms=["NaCl", "common salt", "regular salt", "halite", "rock salt", "table salt", "sea salt", "saline"],
)
MolecularEntity.sucrose = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/sucrose",
    definition="A nonreducing disaccharide composed of GLUCOSE and FRUCTOSE linked via their anomeric carbons. It is obtained commercially from SUGARCANE, sugar beet (BETA VULGARIS), and other plants and used extensively as a food and a sweetener.",
    description="It is produced naturally in plants and is the main constituent of white sugar. It has the molecular formula C12H22O11. For human consumption, sucrose is extracted and refined from either sugarcane or sugar beet. Sugar mills – typically located in tropical regions near where sugarcane is grown – crush the cane and produce raw sugar which is shipped to other factories for refining into pure sucrose. Sugar beet factories are located in temperate climates where the beet is grown, and process the beets directly into refined sugar. The sugar-refining process involves washing the raw sugar crystals before dissolving them into a sugar syrup which is filtered and then passed over carbon to remove any residual colour. The sugar syrup is then concentrated by boiling under a vacuum and crystallized as the final purification process to produce crystals of pure sucrose that are clear, odorless, and sweet.",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:17992#sucrose",
    name="sucrose",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_17992",
    synonyms=[
        "Sugar",
        "1-alpha-D-Glucopyranosyl-2-beta-D-fructofuranoside",
        "β-D-Fruf-(2↔1)-α-D-Glcp",
        "Saccharose",
        "White sugar",
        "Cane sugar",
    ],
)
MolecularEntity.tungsten = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/tungsten",
    definition="Tungsten (also called wolfram) is a chemical element; it has symbol W and atomic number 74.",
    description="Tungsten is a rare metal found naturally on Earth almost exclusively as compounds with other elements. It was identified as a new element in 1781 and first isolated as a metal in 1783. Its important ores include scheelite and wolframite, the latter lending the element its alternate name. The free element is remarkable for its robustness, especially the fact that it has the highest melting point of all known elements, melting at 3,422 °C (6,192 °F; 3,695 K). It also has the highest boiling point, at 5,930 °C (10,706 °F; 6,203 K). Its density is 19.30 grams per cubic centimetre (0.697 lb/cu in), comparable with that of uranium and gold, and much higher (about 1.7 times) than that of lead. Polycrystalline tungsten is an intrinsically brittle and hard material (under standard conditions, when uncombined), making it difficult to work into metal. However, pure single-crystalline tungsten is more ductile and can be cut with a hard-steel hacksaw.",
    name="tungsten",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_27998",
    synonyms=["wolfram"],
)
MolecularEntity.vesicular_glutamate_transporter = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/vesicularGlutamateTransporter",
    definition="The vesicular glutamate transporters are a subclass of glutamate transporters that move glutamate from the cell cytoplasm into synaptic vesicles.",
    name="vesicular glutamate transporter",
    synonyms=["VGLUT"],
)
MolecularEntity.vesicular_glutamate_transporter1 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/vesicularGlutamateTransporter1",
    definition="The vesicular glutamate transporter 1 belongs to the VGLUT family. It is preferentially associated with the membranes of synaptic vesicles and functions in glutamate transport.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0112442",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXMOL:1006007#vesicular-glutamate-transporter-1",
    name="vesicular glutamate transporter 1",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000014963",
    synonyms=["VGLUT1"],
)
MolecularEntity.vesicular_glutamate_transporter2 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/vesicularGlutamateTransporter2",
    definition="The vesicular glutamate transporter 2 belongs to the VGLUT family. It mediates the uptake of glutamate into synaptic vesicles at presynaptic nerve terminals of excitatory neural cells.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0112443",
    knowledge_space_link="https://knowledge-space.org/wiki/NLXMOL:1006009#vesicular-glutamate-transporter-2",
    name="vesicular glutamate transporter 2",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000014962",
    synonyms=["VGLUT2"],
)
MolecularEntity.vesicular_glutamate_transporter3 = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/vesicularGlutamateTransporter3",
    definition="The vesicular glutamate transporter 3 belongs to the VGLUT family. It transports the neurotransmitter glutamate into synaptic vesicles before it is released into the synaptic cleft.",
    knowledge_space_link="https://knowledge-space.org/wiki/PR:000014964#vesicular-glutamate-transporter-3",
    name="vesicular glutamate transporter 3",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/PR_000014964",
    synonyms=["SLC17A8", "solute carrier family 17 member 8", "VGLUT3"],
)
MolecularEntity.water = MolecularEntity(
    id="https://openminds.ebrains.eu/instances/molecularEntity/water",
    definition="An oxygen hydride consisting of an oxygen atom that is covalently bonded to two hydrogen atoms.",
    description="Water is an inorganic compound with the chemical formula H2O. It is a transparent, tasteless, odorless, and nearly colorless chemical substance, and it is the main constituent of Earth's hydrosphere and the fluids of all known living organisms (in which it acts as a solvent). It is vital for all known forms of life, despite not providing food energy or organic micronutrients. Its chemical formula, H2O, indicates that each of its molecules contains one oxygen and two hydrogen atoms, connected by covalent bonds. The hydrogen atoms are attached to the oxygen atom at an angle of 104.45°. 'Water' is also the name of the liquid state of H2O at standard temperature and pressure. Because Earth's environment is relatively close to water's triple point, water exists on Earth as a solid, liquid, and gas.",
    interlex_identifier="http://uri.interlex.org/base/ilx_0782172",
    knowledge_space_link="https://knowledge-space.org/wiki/CHEBI:15377#water",
    name="water",
    preferred_ontology_identifier="http://purl.obolibrary.org/obo/CHEBI_15377",
    synonyms=[
        "H2O",
        "hydrogen oxide",
        "hydrogen hydroxide (HH or HOH)",
        "hydroxylic acid",
        "dihydrogen monoxide (DHMO) (parody name)",
        "dihydrogen oxide",
        "hydric acid",
        "hydrohydroxic acid",
        "hydroxic acid",
        "hydroxoic acid",
        "hydrol[2]",
        "μ-Oxidodihydrogen",
        "κ1-hydroxylhydrogen(0)",
        "neutral liquid",
    ],
)
