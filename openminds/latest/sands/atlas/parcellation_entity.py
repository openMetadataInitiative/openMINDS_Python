"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class ParcellationEntity(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/sands/ParcellationEntity"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "abbreviation",
            str,
            "abbreviation",
            formatting="text/plain",
            description="no description available",
            instructions="Enter the official abbreviation of this parcellation entity.",
        ),
        Property(
            "alternate_names",
            str,
            "alternateName",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="no description available",
            instructions="Enter any alternate names, including any alternative abbreviations, for this parcellation entity.",
        ),
        Property(
            "definition",
            str,
            "definition",
            formatting="text/markdown",
            multiline=True,
            description="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
            instructions="Enter the definition for this parcellation entity.",
        ),
        Property(
            "has_parents",
            "openminds.latest.sands.ParcellationEntity",
            "hasParent",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to a parent object or legal person.",
            instructions="Add all anatomical parent structures for this parcellation entity as defined within the corresponding brain atlas.",
        ),
        Property(
            "has_versions",
            "openminds.latest.sands.ParcellationEntityVersion",
            "hasVersion",
            multiple=True,
            unique_items=True,
            min_items=1,
            description="Reference to variants of an original.",
            instructions="Add all versions of this parcellation entity.",
        ),
        Property(
            "lookup_label",
            str,
            "lookupLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a lookup label for this parcellation entity that may help you to find this instance more easily.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Enter the name of this parcellation entity.",
        ),
        Property(
            "ontology_identifiers",
            str,
            "ontologyIdentifier",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Term or code used to identify something or someone registered within a particular ontology.",
            instructions="Enter the internationalized resource identifiers (IRIs) to the related ontological terms matching this parcellation entity.",
        ),
        Property(
            "related_uberon_term",
            ["openminds.latest.controlled_terms.Organ", "openminds.latest.controlled_terms.UBERONParcellation"],
            "relatedUBERONTerm",
            description="no description available",
            instructions="Add the related anatomical entity as defined by the UBERON ontology.",
        ),
    ]

    def __init__(
        self,
        id=None,
        abbreviation=None,
        alternate_names=None,
        definition=None,
        has_parents=None,
        has_versions=None,
        lookup_label=None,
        name=None,
        ontology_identifiers=None,
        related_uberon_term=None,
    ):
        return super().__init__(
            id=id,
            abbreviation=abbreviation,
            alternate_names=alternate_names,
            definition=definition,
            has_parents=has_parents,
            has_versions=has_versions,
            lookup_label=lookup_label,
            name=name,
            ontology_identifiers=ontology_identifiers,
            related_uberon_term=related_uberon_term,
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


ParcellationEntity.aal1_acin = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_ACIN",
    abbreviation="ACIN",
    alternate_names=["CIA", "Cingulum_Ant"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_limbicLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_ACIN"}],
    lookup_label="AAL1_ACIN",
    name="anterior cingulate and paracingulate gyri",
)
ParcellationEntity.aal1_ag = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_AG",
    abbreviation="AG",
    alternate_names=["GA", "Angular"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_parietalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_AG"}],
    lookup_label="AAL1_AG",
    name="angular gyrus",
)
ParcellationEntity.aal1_amyg = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_AMYG",
    abbreviation="AMYG",
    alternate_names=["AMYGD", "Amygdala"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_subcorticalGrayNuclei"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_AMYG"}],
    lookup_label="AAL1_AMYG",
    name="amygdala",
)
ParcellationEntity.aal1_brain = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_brain",
    lookup_label="AAL1_brain",
    name="brain",
)
ParcellationEntity.aal1_cau = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_CAU",
    abbreviation="CAU",
    alternate_names=["NC", "Caudate"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_subcorticalGrayNuclei"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_CAU"}],
    lookup_label="AAL1_CAU",
    name="caudate nucleus",
)
ParcellationEntity.aal1_central_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_centralRegion",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_brain"}],
    lookup_label="AAL1_centralRegion",
    name="central region",
)
ParcellationEntity.aal1_f1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F1",
    abbreviation="F1",
    alternate_names=["F1", "Frontal_Sup"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_F1"}],
    lookup_label="AAL1_F1",
    name="superior frontal gyrus, dorsolateral",
)
ParcellationEntity.aal1_f1_m = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F1M",
    abbreviation="F1M",
    alternate_names=["FM", "Frontal_Sup_Medial"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_F1M"}],
    lookup_label="AAL1_F1M",
    name="superior frontal gyrus, medial",
)
ParcellationEntity.aal1_f1_mo = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F1MO",
    abbreviation="F1MO",
    alternate_names=["FMO", "Frontal_Med_Orb"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_F1MO"}],
    lookup_label="AAL1_F1MO",
    name="superior frontal gyrus, medial orbital",
)
ParcellationEntity.aal1_f1_o = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F1O",
    abbreviation="F1O",
    alternate_names=["F1O", "Frontal_Sup_Orb"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_F1O"}],
    lookup_label="AAL1_F1O",
    name="superior frontal gyrus, orbital part",
)
ParcellationEntity.aal1_f2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F2",
    abbreviation="F2",
    alternate_names=["F2", "Frontal_Mid"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_F2"}],
    lookup_label="AAL1_F2",
    name="middle frontal gyrus",
)
ParcellationEntity.aal1_f2_o = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F2O",
    abbreviation="F2O",
    alternate_names=["F2O", "Frontal_Mid_Orb"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_F2O"}],
    lookup_label="AAL1_F2O",
    name="middle frontal gyrus, orbital part",
)
ParcellationEntity.aal1_f3_o = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F3O",
    abbreviation="F3O",
    alternate_names=["F3O", "Frontal_Inf_Orb"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_F3O"}],
    lookup_label="AAL1_F3O",
    name="inferior frontal gyrus, orbital part",
)
ParcellationEntity.aal1_f3_op = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F3OP",
    abbreviation="F3OP",
    alternate_names=["F3OP", "Frontal_Inf_Oper"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_F3OP"}],
    lookup_label="AAL1_F3OP",
    name="inferior frontal gyrus, opercular part",
)
ParcellationEntity.aal1_f3_t = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_F3T",
    abbreviation="F3T",
    alternate_names=["F3T", "Frontal_Inf_Tri"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_F3T"}],
    lookup_label="AAL1_F3T",
    name="inferior frontal gyrus, triangular part",
)
ParcellationEntity.aal1_frontal_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_brain"}],
    lookup_label="AAL1_frontalLobe",
    name="frontal lobe",
)
ParcellationEntity.aal1_fusi = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_FUSI",
    abbreviation="FUSI",
    alternate_names=["FUSI", "Fusiform"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_occipitalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_FUSI"}],
    lookup_label="AAL1_FUSI",
    name="fusiform gyrus",
)
ParcellationEntity.aal1_gr = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_GR",
    abbreviation="GR",
    alternate_names=["GR", "Rectus"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_GR"}],
    lookup_label="AAL1_GR",
    name="gyrus rectus",
)
ParcellationEntity.aal1_hes = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_HES",
    abbreviation="HES",
    alternate_names=["HESCHL", "Heschl"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_temporalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_HES"}],
    lookup_label="AAL1_HES",
    name="Heschl gyrus",
)
ParcellationEntity.aal1_hip = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_HIP",
    abbreviation="HIP",
    alternate_names=["HIPPO", "Hippocampus"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_limbicLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_HIP"}],
    lookup_label="AAL1_HIP",
    name="hippocampus",
)
ParcellationEntity.aal1_in = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_IN",
    abbreviation="IN",
    alternate_names=["IN", "Insula"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_brain"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_IN"}],
    lookup_label="AAL1_IN",
    name="insula",
)
ParcellationEntity.aal1_limbic_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_limbicLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_brain"}],
    lookup_label="AAL1_limbicLobe",
    name="limbic lobe",
)
ParcellationEntity.aal1_ling = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_LING",
    abbreviation="LING",
    alternate_names=["LING", "Lingual"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_occipitalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_LING"}],
    lookup_label="AAL1_LING",
    name="lingual gyrus",
)
ParcellationEntity.aal1_mcin = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_MCIN",
    abbreviation="MCIN",
    alternate_names=["CINM", "Cingulum_Mid"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_limbicLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_MCIN"}],
    lookup_label="AAL1_MCIN",
    name="median cingulate and paracingulate gyri",
)
ParcellationEntity.aal1_o1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_O1",
    abbreviation="O1",
    alternate_names=["O1", "Occipital_Sup"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_occipitalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_O1"}],
    lookup_label="AAL1_O1",
    name="superior occipital gyrus",
)
ParcellationEntity.aal1_o2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_O2",
    abbreviation="O2",
    alternate_names=["O2", "Occipital_Mid"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_occipitalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_O2"}],
    lookup_label="AAL1_O2",
    name="middle occipital gyrus",
)
ParcellationEntity.aal1_o3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_O3",
    abbreviation="O3",
    alternate_names=["O3", "Occipital_Inf"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_occipitalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_O3"}],
    lookup_label="AAL1_O3",
    name="inferior occipital gyrus",
)
ParcellationEntity.aal1_oc = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_OC",
    abbreviation="OC",
    alternate_names=["COB", "Olfactory"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_OC"}],
    lookup_label="AAL1_OC",
    name="olfactory cortex",
)
ParcellationEntity.aal1_occipital_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_occipitalLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_brain"}],
    lookup_label="AAL1_occipitalLobe",
    name="occipital lobe",
)
ParcellationEntity.aal1_p1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_P1",
    abbreviation="P1",
    alternate_names=["P1", "Parietal_Sup"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_parietalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_P1"}],
    lookup_label="AAL1_P1",
    name="superior parietal gyrus",
)
ParcellationEntity.aal1_p2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_P2",
    abbreviation="P2",
    alternate_names=["P2", "Parietal_Inf"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_parietalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_P2"}],
    lookup_label="AAL1_P2",
    name="inferior parietal, but supramarginal and angular gyri",
)
ParcellationEntity.aal1_pal = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PAL",
    abbreviation="PAL",
    alternate_names=["PALL", "Pallidum"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_subcorticalGrayNuclei"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_PAL"}],
    lookup_label="AAL1_PAL",
    name="lenticular nucleus, pallidum",
)
ParcellationEntity.aal1_parietal_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_parietalLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_brain"}],
    lookup_label="AAL1_parietalLobe",
    name="parietal lobe",
)
ParcellationEntity.aal1_pcin = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PCIN",
    abbreviation="PCIN",
    alternate_names=["CIP", "Cingulum_Post"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_limbicLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_PCIN"}],
    lookup_label="AAL1_PCIN",
    name="posterior cingulate gyrus",
)
ParcellationEntity.aal1_pcl = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PCL",
    abbreviation="PCL",
    alternate_names=["LPC", "Paracentralobule"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_PCL"}],
    lookup_label="AAL1_PCL",
    name="paracentral lobule",
)
ParcellationEntity.aal1_phip = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PHIP",
    abbreviation="PHIP",
    alternate_names=["PARA_HIPPO", "ParaHippocampal"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_limbicLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_PHIP"}],
    lookup_label="AAL1_PHIP",
    name="parahippocampal gyrus",
)
ParcellationEntity.aal1_post = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_POST",
    abbreviation="POST",
    alternate_names=["PA", "Postcentral"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_centralRegion"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_POST"}],
    lookup_label="AAL1_POST",
    name="postcentral gyrus",
)
ParcellationEntity.aal1_pq = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PQ",
    abbreviation="PQ",
    alternate_names=["PQ", "Precuneus"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_parietalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_PQ"}],
    lookup_label="AAL1_PQ",
    name="precuneus",
)
ParcellationEntity.aal1_pre = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PRE",
    abbreviation="PRE",
    alternate_names=["FA", "Precentral"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_centralRegion"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_PRE"}],
    lookup_label="AAL1_PRE",
    name="precentral gyrus",
)
ParcellationEntity.aal1_put = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_PUT",
    abbreviation="PUT",
    alternate_names=["NL", "Putamen"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_subcorticalGrayNuclei"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_PUT"}],
    lookup_label="AAL1_PUT",
    name="lenticular nucleus, putamen",
)
ParcellationEntity.aal1_q = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_Q",
    abbreviation="Q",
    alternate_names=["Q", "Cuneus"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_occipitalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_Q"}],
    lookup_label="AAL1_Q",
    name="cuneus",
)
ParcellationEntity.aal1_ro = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_RO",
    abbreviation="RO",
    alternate_names=["OR", "Rolandic_Oper"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_centralRegion"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_RO"}],
    lookup_label="AAL1_RO",
    name="rolandic operculum",
)
ParcellationEntity.aal1_sma = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_SMA",
    abbreviation="SMA",
    alternate_names=["SMA", "Supp_Motor_Area"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_frontalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_SMA"}],
    lookup_label="AAL1_SMA",
    name="supplementary motor area",
)
ParcellationEntity.aal1_smg = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_SMG",
    abbreviation="SMG",
    alternate_names=["GSM", "SupraMarginal"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_parietalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_SMG"}],
    lookup_label="AAL1_SMG",
    name="supramarginal gyrus",
)
ParcellationEntity.aal1_subcortical_gray_nuclei = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_subcorticalGrayNuclei",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_brain"}],
    lookup_label="AAL1_subcorticalGrayNuclei",
    name="subcortical gray nuclei",
)
ParcellationEntity.aal1_t1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_T1",
    abbreviation="T1",
    alternate_names=["T1", "Temporal_Sup"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_temporalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_T1"}],
    lookup_label="AAL1_T1",
    name="superior temporal gyrus",
)
ParcellationEntity.aal1_t1_p = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_T1P",
    abbreviation="T1P",
    alternate_names=["T1A", "Temporal_Pole_Sup"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_limbicLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_T1P"}],
    lookup_label="AAL1_T1P",
    name="temporal pole: superior temporal gyrus",
)
ParcellationEntity.aal1_t2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_T2",
    abbreviation="T2",
    alternate_names=["T2", "Temporal_Mid"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_temporalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_T2"}],
    lookup_label="AAL1_T2",
    name="middle temporal gyrus",
)
ParcellationEntity.aal1_t2_p = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_T2P",
    abbreviation="T2P",
    alternate_names=["T2A", "Temporal_Pole_Mid"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_limbicLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_T2P"}],
    lookup_label="AAL1_T2P",
    name="temporal pole: middle temporal gyrus",
)
ParcellationEntity.aal1_t3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_T3",
    abbreviation="T3",
    alternate_names=["T3", "Temporal_Inf"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_temporalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_T3"}],
    lookup_label="AAL1_T3",
    name="inferior temporal gyrus",
)
ParcellationEntity.aal1_temporal_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_temporalLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_brain"}],
    lookup_label="AAL1_temporalLobe",
    name="temporal lobe",
)
ParcellationEntity.aal1_tha = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_THA",
    abbreviation="THA",
    alternate_names=["THA", "Thalamus"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_subcorticalGrayNuclei"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_THA"}],
    lookup_label="AAL1_THA",
    name="thalamus",
)
ParcellationEntity.aal1_v1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_V1",
    abbreviation="V1",
    alternate_names=["V1", "Calcarine"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/AAL1_occipitalLobe"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/AAL1_SPM12-v4_V1"}],
    lookup_label="AAL1_V1",
    name="calcarine fissure and surrounding cortex",
)
ParcellationEntity.aseg_atlas_accumbens_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_accumbensArea",
    lookup_label="AsegAtlas_accumbensArea",
    name="accumbens area",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/nucleusAccumbens"},
)
ParcellationEntity.aseg_atlas_amygdala = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_amygdala",
    lookup_label="AsegAtlas_amygdala",
    name="amygdala",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/amygdala"},
)
ParcellationEntity.aseg_atlas_brain_stem = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_brainStem",
    lookup_label="AsegAtlas_brainStem",
    name="brain stem",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/brainstem"},
)
ParcellationEntity.aseg_atlas_caudate = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_caudate",
    lookup_label="AsegAtlas_caudate",
    name="caudate",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/caudateNucleus"},
)
ParcellationEntity.aseg_atlas_cerebellum_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_cerebellumCortex",
    lookup_label="AsegAtlas_cerebellumCortex",
    name="cerebellum cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/cerebellarCortex"},
)
ParcellationEntity.aseg_atlas_cerebellum_white_matter = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_cerebellumWhiteMatter",
    lookup_label="AsegAtlas_cerebellumWhiteMatter",
    name="cerebellum white matter",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/whiteMatterOfCerebellum"},
)
ParcellationEntity.aseg_atlas_cerebral_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_cerebralCortex",
    lookup_label="AsegAtlas_cerebralCortex",
    name="cerebral cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/cerebralCortex"},
)
ParcellationEntity.aseg_atlas_cerebral_white_matter = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_cerebralWhiteMatter",
    lookup_label="AsegAtlas_cerebralWhiteMatter",
    name="cerebral white matter",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/cerebralHemisphereWhiteMatter"
    },
)
ParcellationEntity.aseg_atlas_cerebrospinal_fluid = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_cerebrospinalFluid",
    lookup_label="AsegAtlas_cerebrospinalFluid",
    name="cerebrospinal fluid",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/cerebrospinalFluid"},
)
ParcellationEntity.aseg_atlas_fourth_ventricle = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_fourthVentricle",
    lookup_label="AsegAtlas_fourthVentricle",
    name="fourth ventricle",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/fourthVentricle"},
)
ParcellationEntity.aseg_atlas_hippocampus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_hippocampus",
    lookup_label="AsegAtlas_hippocampus",
    name="hippocampus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/hippocampalFormation"},
)
ParcellationEntity.aseg_atlas_inferior_lateral_ventricle = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_inferiorLateralVentricle",
    lookup_label="AsegAtlas_inferiorLateralVentricle",
    name="inferior lateral ventricle",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/inferiorHornOfTheLateralVentricle"
    },
)
ParcellationEntity.aseg_atlas_lateral_ventricle = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_lateralVentricle",
    lookup_label="AsegAtlas_lateralVentricle",
    name="lateral ventricle",
)
ParcellationEntity.aseg_atlas_lesion = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_lesion",
    lookup_label="AsegAtlas_lesion",
    name="lesion",
)
ParcellationEntity.aseg_atlas_pallidum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_pallidum",
    lookup_label="AsegAtlas_pallidum",
    name="pallidum",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/pallidum"},
)
ParcellationEntity.aseg_atlas_putamen = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_putamen",
    lookup_label="AsegAtlas_putamen",
    name="putamen",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/putamen"},
)
ParcellationEntity.aseg_atlas_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_thalamus",
    lookup_label="AsegAtlas_thalamus",
    name="thalamus",
)
ParcellationEntity.aseg_atlas_third_ventricle = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_thirdVentricle",
    lookup_label="AsegAtlas_thirdVentricle",
    name="third ventricle",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/thirdVentricle"},
)
ParcellationEntity.aseg_atlas_unknown = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_unknown",
    lookup_label="AsegAtlas_unknown",
    name="unknown",
)
ParcellationEntity.aseg_atlas_ventral_diencephalon = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_ventralDiencephalon",
    lookup_label="AsegAtlas_ventralDiencephalon",
    name="ventral diencephalon",
)
ParcellationEntity.aseg_atlas_vessel = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/AsegAtlas_vessel",
    lookup_label="AsegAtlas_vessel",
    name="vessel",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/vessel"},
)
ParcellationEntity.ba_human_ba1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA1",
    abbreviation="BA1",
    alternate_names=["Brodmann's area 1", "human BA1", "human Brodmann area 1", "human Brodmann's area 1"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA1"}],
    lookup_label="BA-human_BA1",
    name="Brodmann area 1",
)
ParcellationEntity.ba_human_ba10 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA10",
    abbreviation="BA10",
    alternate_names=["Brodmann's area 10", "human BA10", "human Brodmann area 10", "human Brodmann's area 10"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA10"}],
    lookup_label="BA-human_BA10",
    name="Brodmann area 10",
)
ParcellationEntity.ba_human_ba11 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA11",
    abbreviation="BA11",
    alternate_names=["Brodmann's area 11", "human BA11", "human Brodmann area 11", "human Brodmann's area 11"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA11"}],
    lookup_label="BA-human_BA11",
    name="Brodmann area 11",
)
ParcellationEntity.ba_human_ba12 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA12",
    abbreviation="BA12",
    alternate_names=["Brodmann's area 12", "human BA12", "human Brodmann area 12", "human Brodmann's area 12"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA12"}],
    lookup_label="BA-human_BA12",
    name="Brodmann area 12",
)
ParcellationEntity.ba_human_ba13 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA13",
    abbreviation="BA13",
    alternate_names=["Brodmann's area 13", "human BA13", "human Brodmann area 13", "human Brodmann's area 13"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA13"}],
    lookup_label="BA-human_BA13",
    name="Brodmann area 13",
)
ParcellationEntity.ba_human_ba14 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA14",
    abbreviation="BA14",
    alternate_names=["Brodmann's area 14", "human BA14", "human Brodmann area 14", "human Brodmann's area 14"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA14"}],
    lookup_label="BA-human_BA14",
    name="Brodmann area 14",
)
ParcellationEntity.ba_human_ba15 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA15",
    abbreviation="BA15",
    alternate_names=["Brodmann's area 15", "human BA15", "human Brodmann area 15", "human Brodmann's area 15"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA15"}],
    lookup_label="BA-human_BA15",
    name="Brodmann area 15",
)
ParcellationEntity.ba_human_ba16 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA16",
    abbreviation="BA16",
    alternate_names=["Brodmann's area 16", "human BA16", "human Brodmann area 16", "human Brodmann's area 16"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA16"}],
    lookup_label="BA-human_BA16",
    name="Brodmann area 16",
)
ParcellationEntity.ba_human_ba17 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA17",
    abbreviation="BA17",
    alternate_names=["Brodmann's area 17", "human BA17", "human Brodmann area 17", "human Brodmann's area 17"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA17"}],
    lookup_label="BA-human_BA17",
    name="Brodmann area 17",
)
ParcellationEntity.ba_human_ba18 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA18",
    abbreviation="BA18",
    alternate_names=["Brodmann's area 18", "human BA18", "human Brodmann area 18", "human Brodmann's area 18"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA18"}],
    lookup_label="BA-human_BA18",
    name="Brodmann area 18",
)
ParcellationEntity.ba_human_ba19 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA19",
    abbreviation="BA19",
    alternate_names=["Brodmann's area 19", "human BA19", "human Brodmann area 19", "human Brodmann's area 19"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA19"}],
    lookup_label="BA-human_BA19",
    name="Brodmann area 19",
)
ParcellationEntity.ba_human_ba2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA2",
    abbreviation="BA2",
    alternate_names=["Brodmann's area 2", "human BA2", "human Brodmann area 2", "human Brodmann's area 2"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA2"}],
    lookup_label="BA-human_BA2",
    name="Brodmann area 2",
)
ParcellationEntity.ba_human_ba20 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA20",
    abbreviation="BA20",
    alternate_names=["Brodmann's area 20", "human BA20", "human Brodmann area 20", "human Brodmann's area 20"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA20"}],
    lookup_label="BA-human_BA20",
    name="Brodmann area 20",
)
ParcellationEntity.ba_human_ba21 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA21",
    abbreviation="BA21",
    alternate_names=["Brodmann's area 21", "human BA21", "human Brodmann area 21", "human Brodmann's area 21"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA21"}],
    lookup_label="BA-human_BA21",
    name="Brodmann area 21",
)
ParcellationEntity.ba_human_ba22 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA22",
    abbreviation="BA22",
    alternate_names=["Brodmann's area 22", "human BA22", "human Brodmann area 22", "human Brodmann's area 22"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA22"}],
    lookup_label="BA-human_BA22",
    name="Brodmann area 22",
)
ParcellationEntity.ba_human_ba23 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA23",
    abbreviation="BA23",
    alternate_names=["Brodmann's area 23", "human BA23", "human Brodmann area 23", "human Brodmann's area 23"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA23"}],
    lookup_label="BA-human_BA23",
    name="Brodmann area 23",
)
ParcellationEntity.ba_human_ba24 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA24",
    abbreviation="BA24",
    alternate_names=["Brodmann's area 24", "human BA24", "human Brodmann area 24", "human Brodmann's area 24"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA24"}],
    lookup_label="BA-human_BA24",
    name="Brodmann area 24",
)
ParcellationEntity.ba_human_ba25 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA25",
    abbreviation="BA25",
    alternate_names=["Brodmann's area 25", "human BA25", "human Brodmann area 25", "human Brodmann's area 25"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA25"}],
    lookup_label="BA-human_BA25",
    name="Brodmann area 25",
)
ParcellationEntity.ba_human_ba26 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA26",
    abbreviation="BA26",
    alternate_names=["Brodmann's area 26", "human BA26", "human Brodmann area 26", "human Brodmann's area 26"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA26"}],
    lookup_label="BA-human_BA26",
    name="Brodmann area 26",
)
ParcellationEntity.ba_human_ba27 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA27",
    abbreviation="BA27",
    alternate_names=["Brodmann's area 27", "human BA27", "human Brodmann area 27", "human Brodmann's area 27"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA27"}],
    lookup_label="BA-human_BA27",
    name="Brodmann area 27",
)
ParcellationEntity.ba_human_ba28 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA28",
    abbreviation="BA28",
    alternate_names=["Brodmann's area 28", "human BA28", "human Brodmann area 28", "human Brodmann's area 28"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA28"}],
    lookup_label="BA-human_BA28",
    name="Brodmann area 28",
)
ParcellationEntity.ba_human_ba29 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA29",
    abbreviation="BA29",
    alternate_names=["Brodmann's area 29", "human BA29", "human Brodmann area 29", "human Brodmann's area 29"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA29"}],
    lookup_label="BA-human_BA29",
    name="Brodmann area 29",
)
ParcellationEntity.ba_human_ba3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA3",
    abbreviation="BA3",
    alternate_names=["Brodmann's area 3", "human BA3", "human Brodmann area 3", "human Brodmann's area 3"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA3"}],
    lookup_label="BA-human_BA3",
    name="Brodmann area 3",
)
ParcellationEntity.ba_human_ba30 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA30",
    abbreviation="BA30",
    alternate_names=["Brodmann's area 30", "human BA30", "human Brodmann area 30", "human Brodmann's area 30"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA30"}],
    lookup_label="BA-human_BA30",
    name="Brodmann area 30",
)
ParcellationEntity.ba_human_ba31 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA31",
    abbreviation="BA31",
    alternate_names=["Brodmann's area 31", "human BA31", "human Brodmann area 31", "human Brodmann's area 31"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA31"}],
    lookup_label="BA-human_BA31",
    name="Brodmann area 31",
)
ParcellationEntity.ba_human_ba32 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA32",
    abbreviation="BA32",
    alternate_names=["Brodmann's area 32", "human BA32", "human Brodmann area 32", "human Brodmann's area 32"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA32"}],
    lookup_label="BA-human_BA32",
    name="Brodmann area 32",
)
ParcellationEntity.ba_human_ba33 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA33",
    abbreviation="BA33",
    alternate_names=["Brodmann's area 33", "human BA33", "human Brodmann area 33", "human Brodmann's area 33"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA33"}],
    lookup_label="BA-human_BA33",
    name="Brodmann area 33",
)
ParcellationEntity.ba_human_ba34 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA34",
    abbreviation="BA34",
    alternate_names=["Brodmann's area 34", "human BA34", "human Brodmann area 34", "human Brodmann's area 34"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA34"}],
    lookup_label="BA-human_BA34",
    name="Brodmann area 34",
)
ParcellationEntity.ba_human_ba35 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA35",
    abbreviation="BA35",
    alternate_names=["Brodmann's area 35", "human BA35", "human Brodmann area 35", "human Brodmann's area 35"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA35"}],
    lookup_label="BA-human_BA35",
    name="Brodmann area 35",
)
ParcellationEntity.ba_human_ba36 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA36",
    abbreviation="BA36",
    alternate_names=["Brodmann's area 36", "human BA36", "human Brodmann area 36", "human Brodmann's area 36"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA36"}],
    lookup_label="BA-human_BA36",
    name="Brodmann area 36",
)
ParcellationEntity.ba_human_ba37 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA37",
    abbreviation="BA37",
    alternate_names=["Brodmann's area 37", "human BA37", "human Brodmann area 37", "human Brodmann's area 37"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA37"}],
    lookup_label="BA-human_BA37",
    name="Brodmann area 37",
)
ParcellationEntity.ba_human_ba38 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA38",
    abbreviation="BA38",
    alternate_names=["Brodmann's area 38", "human BA38", "human Brodmann area 38", "human Brodmann's area 38"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA38"}],
    lookup_label="BA-human_BA38",
    name="Brodmann area 38",
)
ParcellationEntity.ba_human_ba39 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA39",
    abbreviation="BA39",
    alternate_names=["Brodmann's area 39", "human BA39", "human Brodmann area 39", "human Brodmann's area 39"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA39"}],
    lookup_label="BA-human_BA39",
    name="Brodmann area 39",
)
ParcellationEntity.ba_human_ba4 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA4",
    abbreviation="BA4",
    alternate_names=["Brodmann's area 4", "human BA4", "human Brodmann area 4", "human Brodmann's area 4"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA4"}],
    lookup_label="BA-human_BA4",
    name="Brodmann area 4",
)
ParcellationEntity.ba_human_ba40 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA40",
    abbreviation="BA40",
    alternate_names=["Brodmann's area 40", "human BA40", "human Brodmann area 40", "human Brodmann's area 40"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA40"}],
    lookup_label="BA-human_BA40",
    name="Brodmann area 40",
)
ParcellationEntity.ba_human_ba41 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA41",
    abbreviation="BA41",
    alternate_names=["Brodmann's area 41", "human BA41", "human Brodmann area 41", "human Brodmann's area 41"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA41"}],
    lookup_label="BA-human_BA41",
    name="Brodmann area 41",
)
ParcellationEntity.ba_human_ba42 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA42",
    abbreviation="BA42",
    alternate_names=["Brodmann's area 42", "human BA42", "human Brodmann area 42", "human Brodmann's area 42"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA42"}],
    lookup_label="BA-human_BA42",
    name="Brodmann area 42",
)
ParcellationEntity.ba_human_ba43 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA43",
    abbreviation="BA43",
    alternate_names=["Brodmann's area 43", "human BA43", "human Brodmann area 43", "human Brodmann's area 43"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA43"}],
    lookup_label="BA-human_BA43",
    name="Brodmann area 43",
)
ParcellationEntity.ba_human_ba44 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA44",
    abbreviation="BA44",
    alternate_names=["Brodmann's area 44", "human BA44", "human Brodmann area 44", "human Brodmann's area 44"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA44"}],
    lookup_label="BA-human_BA44",
    name="Brodmann area 44",
)
ParcellationEntity.ba_human_ba45 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA45",
    abbreviation="BA45",
    alternate_names=["Brodmann's area 45", "human BA45", "human Brodmann area 45", "human Brodmann's area 45"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA45"}],
    lookup_label="BA-human_BA45",
    name="Brodmann area 45",
)
ParcellationEntity.ba_human_ba46 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA46",
    abbreviation="BA46",
    alternate_names=["Brodmann's area 46", "human BA46", "human Brodmann area 46", "human Brodmann's area 46"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA46"}],
    lookup_label="BA-human_BA46",
    name="Brodmann area 46",
)
ParcellationEntity.ba_human_ba47 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA47",
    abbreviation="BA47",
    alternate_names=["Brodmann's area 47", "human BA47", "human Brodmann area 47", "human Brodmann's area 47"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA47"}],
    lookup_label="BA-human_BA47",
    name="Brodmann area 47",
)
ParcellationEntity.ba_human_ba48 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA48",
    abbreviation="BA48",
    alternate_names=["Brodmann's area 48", "human BA48", "human Brodmann area 48", "human Brodmann's area 48"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA48"}],
    lookup_label="BA-human_BA48",
    name="Brodmann area 48",
)
ParcellationEntity.ba_human_ba5 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA5",
    abbreviation="BA5",
    alternate_names=["Brodmann's area 5", "human BA5", "human Brodmann area 5", "human Brodmann's area 5"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA5"}],
    lookup_label="BA-human_BA5",
    name="Brodmann area 5",
)
ParcellationEntity.ba_human_ba52 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA52",
    abbreviation="BA52",
    alternate_names=["Brodmann's area 52", "human BA52", "human Brodmann area 52", "human Brodmann's area 52"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA52"}],
    lookup_label="BA-human_BA52",
    name="Brodmann area 52",
)
ParcellationEntity.ba_human_ba6 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA6",
    abbreviation="BA6",
    alternate_names=["Brodmann's area 6", "human BA6", "human Brodmann area 6", "human Brodmann's area 6"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA6"}],
    lookup_label="BA-human_BA6",
    name="Brodmann area 6",
)
ParcellationEntity.ba_human_ba7 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA7",
    abbreviation="BA7",
    alternate_names=["Brodmann's area 7", "human BA7", "human Brodmann area 7", "human Brodmann's area 7"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA7"}],
    lookup_label="BA-human_BA7",
    name="Brodmann area 7",
)
ParcellationEntity.ba_human_ba8 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA8",
    abbreviation="BA8",
    alternate_names=["Brodmann's area 8", "human BA8", "human Brodmann area 8", "human Brodmann's area 8"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA8"}],
    lookup_label="BA-human_BA8",
    name="Brodmann area 8",
)
ParcellationEntity.ba_human_ba8a = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA8a",
    abbreviation="BA8a",
    alternate_names=["Brodmann's area 8a", "human BA8a", "human Brodmann area 8a", "human Brodmann's area 8a"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA8a"}],
    lookup_label="BA-human_BA8a",
    name="Brodmann area 8a",
)
ParcellationEntity.ba_human_ba9 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_BA9",
    abbreviation="BA9",
    alternate_names=["Brodmann's area 9", "human BA9", "human Brodmann area 9", "human Brodmann's area 9"],
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/BA-human_1909_BA9"}],
    lookup_label="BA-human_BA9",
    name="Brodmann area 9",
)
ParcellationEntity.ba_human_cerebral_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/BA-human_cerebralCortex",
    abbreviation="cortex",
    alternate_names=[
        "Brodmann's cerebral cortex",
        "human cortex",
        "human Brodmann cerebral cortex",
        "human Brodmann's cerebral cortex",
    ],
    lookup_label="BA-human_cerebralCortex",
    name="Brodmann cerebral cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/cerebralCortex"},
)
ParcellationEntity.dka_anterior_cingulate_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_anteriorCingulateCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cingulateCortex"}],
    lookup_label="DKA_anteriorCingulateCortex",
    name="anterior cingulate cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/anteriorCingulateCortex"},
)
ParcellationEntity.dka_banks_of_superior_temporal_sulcus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_banksOfSuperiorTemporalSulcus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_lateralAspect"}],
    lookup_label="DKA_banksOfSuperiorTemporalSulcus",
    name="banks of superior temporal sulcus",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/banksOfSuperiorTemporalSulcus"
    },
)
ParcellationEntity.dka_banks_superior_temporal_sulcus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_banksSuperiorTemporalSulcus",
    lookup_label="DKA_banksSuperiorTemporalSulcus",
    name="banks superior temporal sulcus",
)
ParcellationEntity.dka_caudal_anterior_cingulate_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_caudalAnteriorCingulateCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_anteriorCingulateCortex"}],
    lookup_label="DKA_caudalAnteriorCingulateCortex",
    name="caudal anterior cingulate cortex",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/caudalAnteriorCingulateCortex"
    },
)
ParcellationEntity.dka_caudal_middle_frontal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_caudalMiddleFrontalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_middleFrontalGyrus"}],
    lookup_label="DKA_caudalMiddleFrontalGyrus",
    name="caudal middle frontal gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/caudalMiddleFrontalGyrus"},
)
ParcellationEntity.dka_cerebral_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cerebralCortex",
    lookup_label="DKA_cerebralCortex",
    name="cerebral cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/cerebralCortex"},
)
ParcellationEntity.dka_cingulate_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cingulateCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cerebralCortex"}],
    lookup_label="DKA_cingulateCortex",
    name="cingulate cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/cingulateCortex"},
)
ParcellationEntity.dka_corpus_callosum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_corpusCallosum",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_occipitalLobe"}],
    lookup_label="DKA_corpusCallosum",
    name="corpus callosum",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/corpusCallosum"},
)
ParcellationEntity.dka_cuneus_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cuneusCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_occipitalLobe"}],
    lookup_label="DKA_cuneusCortex",
    name="cuneus cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/cuneusCortex"},
)
ParcellationEntity.dka_entorhinal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_entorhinalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_medialAspect"}],
    lookup_label="DKA_entorhinalCortex",
    name="entorhinal cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/entorhinalCortex"},
)
ParcellationEntity.dka_frontal_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_frontalLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cerebralCortex"}],
    lookup_label="DKA_frontalLobe",
    name="frontal lobe",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/frontalLobe"},
)
ParcellationEntity.dka_frontal_pole = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_frontalPole",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_frontalLobe"}],
    lookup_label="DKA_frontalPole",
    name="frontal pole",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/frontalPole"},
)
ParcellationEntity.dka_fusiform_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_fusiformGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_medialAspect"}],
    lookup_label="DKA_fusiformGyrus",
    name="fusiform gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/fusiformGyrus"},
)
ParcellationEntity.dka_inferior_frontal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_inferiorFrontalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_frontalLobe"}],
    lookup_label="DKA_inferiorFrontalGyrus",
    name="inferior frontal gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/inferiorFrontalGyrus"},
)
ParcellationEntity.dka_inferior_parietal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_inferiorParietalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parietalLobe"}],
    lookup_label="DKA_inferiorParietalCortex",
    name="inferior parietal cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/inferiorParietalCortex"},
)
ParcellationEntity.dka_inferior_temporal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_inferiorTemporalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_lateralAspect"}],
    lookup_label="DKA_inferiorTemporalGyrus",
    name="inferior temporal gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/inferiorTemporalGyrus"},
)
ParcellationEntity.dka_insula = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_insula",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cerebralCortex"}],
    lookup_label="DKA_insula",
    name="insula",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/insula"},
)
ParcellationEntity.dka_isthmus_of_cingulate_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_isthmusOfCingulateCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_occipitalLobe"}],
    lookup_label="DKA_isthmusOfCingulateCortex",
    name="isthmus of cingulate cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/isthmusOfCingulateGyrus"},
)
ParcellationEntity.dka_lateral_occipital_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_lateralOccipitalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_occipitalLobe"}],
    lookup_label="DKA_lateralOccipitalCortex",
    name="lateral occipital cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/lateralOccipitalCortex"},
)
ParcellationEntity.dka_lateral_orbital_frontal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_lateralOrbitalFrontalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_orbitofrontalCortex"}],
    lookup_label="DKA_lateralOrbitalFrontalCortex",
    name="lateral orbitofrontal cortex",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/lateralOrbitalFrontalCortex"
    },
)
ParcellationEntity.dka_lingual_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_lingualGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_occipitalLobe"}],
    lookup_label="DKA_lingualGyrus",
    name="lingual gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/lingualGyrus"},
)
ParcellationEntity.dka_medial_orbital_frontal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_medialOrbitalFrontalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_orbitofrontalCortex"}],
    lookup_label="DKA_medialOrbitalFrontalCortex",
    name="medial orbitofrontal cortex",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/medialOrbitalFrontalCortex"
    },
)
ParcellationEntity.dka_middle_frontal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_middleFrontalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_frontalLobe"}],
    lookup_label="DKA_middleFrontalGyrus",
    name="middle frontal gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/middleFrontalGyrus"},
)
ParcellationEntity.dka_middle_temporal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_middleTemporalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_lateralAspect"}],
    lookup_label="DKA_middleTemporalGyrus",
    name="middle temporal gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/middleTemporalGyrus"},
)
ParcellationEntity.dka_occipital_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_occipitalLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cerebralCortex"}],
    lookup_label="DKA_occipitalLobe",
    name="occipital lobe",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/occipitalLobe"},
)
ParcellationEntity.dka_orbitofrontal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_orbitofrontalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_frontalLobe"}],
    lookup_label="DKA_orbitofrontalCortex",
    name="orbitofrontal cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/orbitofrontalCortex"},
)
ParcellationEntity.dka_paracentral_lobule = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_paracentralLobule",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_frontalLobe"}],
    lookup_label="DKA_paracentralLobule",
    name="paracentral lobule",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/paracentralLobule"},
)
ParcellationEntity.dka_parahippocampal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parahippocampalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_medialAspect"}],
    lookup_label="DKA_parahippocampalGyrus",
    name="parahippocampal gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/parahippocampalGyrus"},
)
ParcellationEntity.dka_parietal_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parietalLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cerebralCortex"}],
    lookup_label="DKA_parietalLobe",
    name="parietal lobe",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/parietalLobe"},
)
ParcellationEntity.dka_pars_opercularis = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parsOpercularis",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_inferiorFrontalGyrus"}],
    lookup_label="DKA_parsOpercularis",
    name="pars opercularis",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/opercularPartOfInferiorFrontalGyrus"
    },
)
ParcellationEntity.dka_pars_orbitalis = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parsOrbitalis",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_inferiorFrontalGyrus"}],
    lookup_label="DKA_parsOrbitalis",
    name="pars orbitalis",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/orbitalPartOfInferiorFrontalGyrus"
    },
)
ParcellationEntity.dka_pars_triangularis = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parsTriangularis",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_inferiorFrontalGyrus"}],
    lookup_label="DKA_parsTriangularis",
    name="pars triangularis",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/triangularPartOfInferiorFrontalGyrus"
    },
)
ParcellationEntity.dka_pericalcarine_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_pericalcarineCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_occipitalLobe"}],
    lookup_label="DKA_pericalcarineCortex",
    name="pericalcarine cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/pericalcarineCortex"},
)
ParcellationEntity.dka_postcentral_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_postcentralGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parietalLobe"}],
    lookup_label="DKA_postcentralGyrus",
    name="postcentral gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/postcentralGyrus"},
)
ParcellationEntity.dka_posterior_cingulate_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_posteriorCingulateCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_occipitalLobe"}],
    lookup_label="DKA_posteriorCingulateCortex",
    name="posterior cingulate cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/posteriorCingulateCortex"},
)
ParcellationEntity.dka_precentral_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_precentralGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_frontalLobe"}],
    lookup_label="DKA_precentralGyrus",
    name="precentral gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/precentralGyrus"},
)
ParcellationEntity.dka_precuneus_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_precuneusCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parietalLobe"}],
    lookup_label="DKA_precuneusCortex",
    name="precuneus cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/precuneusCortex"},
)
ParcellationEntity.dka_rostral_anterior_cingulate_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_rostralAnteriorCingulateCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_anteriorCingulateCortex"}],
    lookup_label="DKA_rostralAnteriorCingulateCortex",
    name="rostral anterior cingulate cortex",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/rostralAnteriorCingulateCortex"
    },
)
ParcellationEntity.dka_rostral_middle_frontal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_rostralMiddleFrontalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_middleFrontalGyrus"}],
    lookup_label="DKA_rostralMiddleFrontalGyrus",
    name="rostral middle frontal gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/rostralMiddleFrontalGyrus"},
)
ParcellationEntity.dka_superior_frontal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_superiorFrontalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_frontalLobe"}],
    lookup_label="DKA_superiorFrontalGyrus",
    name="superior frontal gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/superiorFrontalGyrus"},
)
ParcellationEntity.dka_superior_parietal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_superiorParietalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parietalLobe"}],
    lookup_label="DKA_superiorParietalCortex",
    name="superior parietal cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/superiorParietalCortex"},
)
ParcellationEntity.dka_superior_temporal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_superiorTemporalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_lateralAspect"}],
    lookup_label="DKA_superiorTemporalGyrus",
    name="superior temporal gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/superiorTemporalGyrus"},
)
ParcellationEntity.dka_supramarginal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_supramarginalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_parietalLobe"}],
    lookup_label="DKA_supramarginalGyrus",
    name="supramarginal gyrus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/supramarginalGyrus"},
)
ParcellationEntity.dka_temporal_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_cerebralCortex"}],
    lookup_label="DKA_temporalLobe",
    name="temporal lobe",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/temporalLobe"},
)
ParcellationEntity.dka_temporal_lobe_lateral_aspect = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_lateralAspect",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe"}],
    lookup_label="DKA_temporalLobe_lateralAspect",
    name="temporal lobe - lateral aspect",
)
ParcellationEntity.dka_temporal_lobe_medial_aspect = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_medialAspect",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe"}],
    lookup_label="DKA_temporalLobe_medialAspect",
    name="temporal lobe - medial aspect",
)
ParcellationEntity.dka_temporal_pole = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalPole",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_medialAspect"}],
    lookup_label="DKA_temporalPole",
    name="temporal pole",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/temporalPole"},
)
ParcellationEntity.dka_transverse_temporal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DKA_transverseTemporalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DKA_temporalLobe_lateralAspect"}],
    lookup_label="DKA_transverseTemporalCortex",
    name="transverse temporal cortex",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/transverseGyrusOfHeschl"},
)
ParcellationEntity.dwma_anterior_segement_of_arcuate_fasciculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_anteriorSegementOfArcuateFasciculus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_arcuateFasciculus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/DWMA_2018_anteriorSegementOfArcuateFasciculus"
        }
    ],
    lookup_label="DWMA_anteriorSegementOfArcuateFasciculus",
    name="anterior segment of arcuate fasciculus",
)
ParcellationEntity.dwma_arcuate_fasciculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_arcuateFasciculus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_deepWhiteMatter"}],
    lookup_label="DWMA_arcuateFasciculus",
    name="arcuate fasciculus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/arcuateFasciculus"},
)
ParcellationEntity.dwma_cingulum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_cingulum",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_deepWhiteMatter"}],
    lookup_label="DWMA_cingulum",
    name="cingulum",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/cingulumOfBrain"},
)
ParcellationEntity.dwma_corticospinal_tract = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_corticospinalTract",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_deepWhiteMatter"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/DWMA_2018_corticospinalTract"}
    ],
    lookup_label="DWMA_corticospinalTract",
    name="corticospinal tract",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/corticospinalTract"},
)
ParcellationEntity.dwma_deep_white_matter = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_deepWhiteMatter",
    lookup_label="DWMA_deepWhiteMatter",
    name="deep white matter",
)
ParcellationEntity.dwma_direct_segement_of_arcuate_fasciculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_directSegementOfArcuateFasciculus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_arcuateFasciculus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/DWMA_2018_directSegementOfArcuateFasciculus"
        }
    ],
    lookup_label="DWMA_directSegementOfArcuateFasciculus",
    name="direct segment of arcuate fasciculus",
)
ParcellationEntity.dwma_fornix = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_fornix",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_deepWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/DWMA_2018_fornix"}],
    lookup_label="DWMA_fornix",
    name="fornix",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/fornixOfBrain"},
)
ParcellationEntity.dwma_inferior_fronto_occipital_fasciculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_inferiorFronto-occipitalFasciculus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_deepWhiteMatter"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/DWMA_2018_inferiorFronto-occipitalFasciculus"
        }
    ],
    lookup_label="DWMA_inferiorFronto-occipitalFasciculus",
    name="inferior fronto-occipital fasciculus",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/inferiorOccipitofrontalFasciculus"
    },
)
ParcellationEntity.dwma_inferior_longitudinal_fasciculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_inferiorLongitudinalFasciculus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_deepWhiteMatter"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/DWMA_2018_inferiorLongitudinalFasciculus"
        }
    ],
    lookup_label="DWMA_inferiorLongitudinalFasciculus",
    name="inferior longitudinal fasciculus",
    related_uberon_term={
        "@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/inferiorLongitudinalFasciculus"
    },
)
ParcellationEntity.dwma_long_cingulate_fibres = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_longCingulateFibres",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_cingulum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/DWMA_2018_longCingulateFibres"}
    ],
    lookup_label="DWMA_longCingulateFibres",
    name="long cingulate fibres",
)
ParcellationEntity.dwma_posterior_segement_of_arcuate_fasciculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_posteriorSegementOfArcuateFasciculus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_arcuateFasciculus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/DWMA_2018_posteriorSegementOfArcuateFasciculus"
        }
    ],
    lookup_label="DWMA_posteriorSegementOfArcuateFasciculus",
    name="posterior segment of arcuate fasciculus",
)
ParcellationEntity.dwma_short_cingulate_fibres = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_shortCingulateFibres",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_cingulum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/DWMA_2018_shortCingulateFibres"}
    ],
    lookup_label="DWMA_shortCingulateFibres",
    name="short cingulate fibres",
)
ParcellationEntity.dwma_temporal_cingulate_fibres = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_temporalCingulateFibres",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_cingulum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/DWMA_2018_temporalCingulateFibres"}
    ],
    lookup_label="DWMA_temporalCingulateFibres",
    name="temporal cingulate fibres",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/temporalCortexCingulum"},
)
ParcellationEntity.dwma_uncinate_fasciculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_uncinateFasciculus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/DWMA_deepWhiteMatter"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/DWMA_2018_uncinateFasciculus"}
    ],
    lookup_label="DWMA_uncinateFasciculus",
    name="uncinate fasciculus",
    related_uberon_term={"@id": "https://openminds.ebrains.eu/instances/UBERONParcellation/uncinateFasciculus"},
)
ParcellationEntity.jba__acb_l = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_AcbL",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_ventralStriatum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_AcbL_PM-v5.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_AcbL_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_AcbL_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_AcbL_PM-v5.0"},
    ],
    lookup_label="JBA_AcbL",
    name="AcbL (Lateral Accumbens, Ventral Striatum)",
)
ParcellationEntity.jba__acb_m = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_AcbM",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_ventralStriatum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_AcbM_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_AcbM_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_AcbM_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_AcbM_PM-v5.0"},
    ],
    lookup_label="JBA_AcbM",
    name="AcbM (Medial Accumbens, Ventral Striatum)",
)
ParcellationEntity.jba__area_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_postcentralGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-1_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-1_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-1_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-1_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-1_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-1_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-1_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-1_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-1_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-1_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-1_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-1_PM-v12.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-1_PM-v12.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-1_PM-v12.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-1_PM-v12.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-1_PM-v12.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-1_PM-v12.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-1_PM-v12.1"
        },
    ],
    lookup_label="JBA_Area-1",
    name="Area 1 (PostCG)",
)
ParcellationEntity.jba__area_2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_postcentralGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-2_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-2_PM-v7.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-2_PM-v7.1"
        },
    ],
    lookup_label="JBA_Area-2",
    name="Area 2 (PostCS)",
)
ParcellationEntity.jba__area_25 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-25",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalCingulateGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-25_PM-v16.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-25_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-25_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-25_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-25_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-25_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-25_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-25_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-25_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-25_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-25_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-25_PM-v20.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-25_PM-v20.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-25_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-25_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-25_PM-v20.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-25_PM-v20.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-25_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-25",
    name="Area 25 (sACC)",
)
ParcellationEntity.jba__area_25_25a = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-25.25a",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-25"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-25.25a_PM-v8.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-25.25a_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-25.25a_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-25.25a_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-25.25a",
    name="Area 25.25a (sACC",
)
ParcellationEntity.jba__area_25_25p = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-25.25p",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-25"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-25.25p_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-25.25p_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-25.25p_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-25.25p_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-25.25p",
    name="Area 25.25p (sACC)",
)
ParcellationEntity.jba__area_33 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-33",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalCingulateGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-33_PM-v16.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-33_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-33_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-33_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-33_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-33_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-33_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-33_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-33_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-33_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-33_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-33_PM-v20.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-33_PM-v20.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-33_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-33_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-33_PM-v20.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-33_PM-v20.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-33_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-33",
    name="Area 33 (ACC)",
)
ParcellationEntity.jba__area_3a = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-3a",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_postcentralGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-3a_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-3a_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-3a_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-3a_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-3a_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-3a_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-3a_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-3a_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-3a_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-3a_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-3a_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-3a_PM-v12.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-3a_PM-v12.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-3a_PM-v12.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-3a_PM-v12.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-3a_PM-v12.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-3a_PM-v12.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-3a_PM-v12.1"
        },
    ],
    lookup_label="JBA_Area-3a",
    name="Area 3a (PostCG)",
)
ParcellationEntity.jba__area_3b = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-3b",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_postcentralGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-3b_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-3b_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-3b_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-3b_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-3b_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-3b_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-3b_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-3b_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-3b_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-3b_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-3b_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-3b_PM-v12.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-3b_PM-v12.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-3b_PM-v12.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-3b_PM-v12.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-3b_PM-v12.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-3b_PM-v12.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-3b_PM-v12.1"
        },
    ],
    lookup_label="JBA_Area-3b",
    name="Area 3b (PostCG)",
)
ParcellationEntity.jba__area_44 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-44",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-44_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-44_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-44_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-44_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-44_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-44_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-44_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-44_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-44_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-44_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-44_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-44_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-44_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-44_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-44_PM-v9.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-44_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-44_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-44_PM-v9.2"
        },
    ],
    lookup_label="JBA_Area-44",
    name="Area 44 (IFG)",
)
ParcellationEntity.jba__area_45 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-45",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-45_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-45_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-45_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-45_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-45_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-45_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-45_PM-v7.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-45_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-45_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-45_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-45_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-45_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-45_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-45_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-45_PM-v9.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-45_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-45_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-45_PM-v9.2"
        },
    ],
    lookup_label="JBA_Area-45",
    name="Area 45 (IFG)",
)
ParcellationEntity.jba__area_4a = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-4a",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_precentralGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-4a_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-4a_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-4a_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-4a_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-4a_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-4a_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-4a_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-4a_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-4a_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-4a_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-4a_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-4a_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-4a_PM-v13.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-4a_PM-v13.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-4a_PM-v13.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-4a_PM-v13.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-4a_PM-v13.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-4a_PM-v13.1"
        },
    ],
    lookup_label="JBA_Area-4a",
    name="Area 4a (PreCG)",
)
ParcellationEntity.jba__area_4p = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-4p",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_precentralGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-4p_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-4p_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-4p_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-4p_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-4p_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-4p_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-4p_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-4p_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-4p_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-4p_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-4p_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-4p_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-4p_PM-v13.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-4p_PM-v13.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-4p_PM-v13.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-4p_PM-v13.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-4p_PM-v13.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-4p_PM-v13.1"
        },
    ],
    lookup_label="JBA_Area-4p",
    name="Area 4p (PreCG)",
)
ParcellationEntity.jba__area_5_ci = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-5Ci",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-5Ci_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-5Ci_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-5Ci_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-5Ci_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-5Ci_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-5Ci_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-5Ci_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-5Ci_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-5Ci_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-5Ci_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-5Ci_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-5Ci_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-5Ci_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-5Ci_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-5Ci_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-5Ci_PM-v9.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-5Ci_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-5Ci_PM-v9.2"
        },
    ],
    lookup_label="JBA_Area-5Ci",
    name="Area 5Ci (SPL)",
)
ParcellationEntity.jba__area_5_l = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-5L",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-5L_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-5L_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-5L_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-5L_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-5L_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-5L_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-5L_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-5L_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-5L_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-5L_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-5L_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-5L_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-5L_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-5L_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-5L_PM-v9.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-5L_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-5L_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-5L_PM-v9.2"
        },
    ],
    lookup_label="JBA_Area-5L",
    name="Area 5L (SPL)",
)
ParcellationEntity.jba__area_5_m = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-5M",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-5M_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-5M_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-5M_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-5M_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-5M_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-5M_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-5M_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-5M_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-5M_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-5M_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-5M_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-5M_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-5M_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-5M_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-5M_PM-v9.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-5M_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-5M_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-5M_PM-v9.2"
        },
    ],
    lookup_label="JBA_Area-5M",
    name="Area 5M (SPL)",
)
ParcellationEntity.jba__area_6d1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-6d1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dorsalPrecentralGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-6d1_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-6d1_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-6d1_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-6d1_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-6d1_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-6d1_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-6d1_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-6d1_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-6d1_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-6d1_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-6d1_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-6d1_PM-v7.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-6d1_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-6d1_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-6d1_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-6d1_PM-v7.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-6d1_PM-v7.1"
        },
    ],
    lookup_label="JBA_Area-6d1",
    name="Area 6d1 (PreCG)",
)
ParcellationEntity.jba__area_6d2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-6d2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dorsalPrecentralGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-6d2_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-6d2_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-6d2_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-6d2_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-6d2_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-6d2_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-6d2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-6d2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-6d2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-6d2_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-6d2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-6d2_PM-v7.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-6d2_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-6d2_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-6d2_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-6d2_PM-v7.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-6d2_PM-v7.1"
        },
    ],
    lookup_label="JBA_Area-6d2",
    name="Area 6d2 (PreCG)",
)
ParcellationEntity.jba__area_6d3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-6d3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorFrontalSulcus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-6d3_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-6d3_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-6d3_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-6d3_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-6d3_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-6d3_PM-v4.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-6d3_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-6d3_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-6d3_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-6d3_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-6d3_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-6d3_PM-v7.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-6d3_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-6d3_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-6d3_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-6d3_PM-v7.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-6d3_PM-v7.1"
        },
    ],
    lookup_label="JBA_Area-6d3",
    name="Area 6d3 (SFS)",
)
ParcellationEntity.jba__area_6ma = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-6ma",
    has_parents=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_posteriorMedialSuperiorFrontalGyrus"}
    ],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-6ma_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-6ma_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-6ma_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-6ma_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-6ma_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-6ma_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-6ma_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-6ma_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-6ma_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-6ma_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-6ma_PM-v12.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-6ma_PM-v12.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-6ma_PM-v12.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-6ma_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-6ma_PM-v12.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-6ma_PM-v12.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-6ma_PM-v12.1"
        },
    ],
    lookup_label="JBA_Area-6ma",
    name="Area 6ma (preSMA, mesial SFG)",
)
ParcellationEntity.jba__area_6mp = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-6mp",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_mesialPrecentralGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-6mp_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-6mp_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-6mp_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-6mp_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-6mp_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-6mp_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-6mp_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-6mp_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-6mp_PM-v10.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-6mp_PM-v10.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-6mp_PM-v12.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-6mp_PM-v12.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-6mp_PM-v12.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-6mp_PM-v12.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-6mp_PM-v12.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-6mp_PM-v12.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-6mp_PM-v12.1"
        },
    ],
    lookup_label="JBA_Area-6mp",
    name="Area 6mp (SMA, mesial SFG)",
)
ParcellationEntity.jba__area_7_a = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-7A",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-7A_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-7A_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-7A_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-7A_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-7A_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-7A_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-7A_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-7A_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-7A_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-7A_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-7A_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-7A_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-7A_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-7A_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-7A_PM-v9.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-7A_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-7A_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-7A_PM-v9.2"
        },
    ],
    lookup_label="JBA_Area-7A",
    name="Area 7A (SPL)",
)
ParcellationEntity.jba__area_7_m = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-7M",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-7M_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-7M_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-7M_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-7M_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-7M_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-7M_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-7M_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-7M_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-7M_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-7M_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-7M_PM-v9.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-7M_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-7M_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-7M_PM-v9.2"
        },
    ],
    lookup_label="JBA_Area-7M",
    name="Area 7M (SPL)",
)
ParcellationEntity.jba__area_7_p = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-7P",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-7P_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-7P_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-7P_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-7P_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-7P_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-7P_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-7P_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-7P_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-7P_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-7P_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-7P_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-7P_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-7P_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-7P_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-7P_PM-v9.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-7P_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-7P_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-7P_PM-v9.2"
        },
    ],
    lookup_label="JBA_Area-7P",
    name="Area 7P (SPL)",
)
ParcellationEntity.jba__area_7_pc = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-7PC",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-7PC_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-7PC_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-7PC_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-7PC_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-7PC_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-7PC_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-7PC_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-7PC_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-7PC_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-7PC_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-7PC_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-7PC_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-7PC_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-7PC_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-7PC_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-7PC_PM-v9.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-7PC_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-7PC_PM-v9.2"
        },
    ],
    lookup_label="JBA_Area-7PC",
    name="Area 7PC (SPL)",
)
ParcellationEntity.jba__area_8d1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-8d1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorFrontalGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-8d1_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-8d1_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-8d1_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-8d1_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-8d1_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-8d1_PM-v4.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-8d1_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-8d1_PM-v4.2"
        },
    ],
    lookup_label="JBA_Area-8d1",
    name="Area 8d1 (SFG)",
)
ParcellationEntity.jba__area_8d2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-8d2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorFrontalGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-8d2_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-8d2_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-8d2_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-8d2_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-8d2_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-8d2_PM-v4.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-8d2_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-8d2_PM-v4.2"
        },
    ],
    lookup_label="JBA_Area-8d2",
    name="Area 8d2 (SFG)",
)
ParcellationEntity.jba__area_8v1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-8v1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_middleFrontalGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-8v1_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-8v1_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-8v1_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-8v1_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-8v1_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-8v1_PM-v4.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-8v1_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-8v1_PM-v4.2"
        },
    ],
    lookup_label="JBA_Area-8v1",
    name="Area 8v1 (MFG)",
)
ParcellationEntity.jba__area_8v2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-8v2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_middleFrontalGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-8v2_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-8v2_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-8v2_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-8v2_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-8v2_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-8v2_PM-v4.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-8v2_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-8v2_PM-v4.2"
        },
    ],
    lookup_label="JBA_Area-8v2",
    name="Area 8v2 (MFG)",
)
ParcellationEntity.jba__area__co_s1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-CoS1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_collateralSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-CoS1_PM-v8.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-CoS1_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-CoS1_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-CoS1_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-CoS1_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-CoS1_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-CoS1_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-CoS1_PM-v7.2"
        },
    ],
    lookup_label="JBA_Area-CoS1",
    name="Area CoS1 (CoS)",
)
ParcellationEntity.jba__area__fo1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_medialOrbitofrontalCortex"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-Fo1_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Fo1_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Fo1_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Fo1_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Fo1_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Fo1_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Fo1_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Fo1_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Fo1_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Fo1_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Fo1_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Fo1_PM-v5.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Fo1_PM-v5.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Fo1_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Fo1_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Fo1_PM-v5.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Fo1_PM-v5.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Fo1_PM-v5.2"
        },
    ],
    lookup_label="JBA_Area-Fo1",
    name="Area Fo1 (OFC)",
)
ParcellationEntity.jba__area__fo2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_medialOrbitofrontalCortex"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-Fo2_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Fo2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Fo2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Fo2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Fo2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Fo2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Fo2_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Fo2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Fo2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Fo2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Fo2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Fo2_PM-v5.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Fo2_PM-v5.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Fo2_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Fo2_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Fo2_PM-v5.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Fo2_PM-v5.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Fo2_PM-v5.2"
        },
    ],
    lookup_label="JBA_Area-Fo2",
    name="Area Fo2 (OFC)",
)
ParcellationEntity.jba__area__fo3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_medialOrbitofrontalCortex"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-Fo3_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Fo3_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Fo3_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Fo3_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Fo3_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Fo3_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Fo3_PM-v3.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Fo3_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Fo3_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Fo3_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Fo3_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Fo3_PM-v5.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Fo3_PM-v5.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Fo3_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Fo3_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Fo3_PM-v5.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Fo3_PM-v5.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Fo3_PM-v5.2"
        },
    ],
    lookup_label="JBA_Area-Fo3",
    name="Area Fo3 (OFC)",
)
ParcellationEntity.jba__area__fo4 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo4",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_lateralOrbitofrontalCortex"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Fo4_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Fo4_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Fo4_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Fo4_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Fo4_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Fo4_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Fo4_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Fo4_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Fo4_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Fo4_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Fo4_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Fo4_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Fo4_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Fo4_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Fo4_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Fo4_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Fo4_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-Fo4",
    name="Area Fo4 (OFC)",
)
ParcellationEntity.jba__area__fo5 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo5",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_lateralOrbitofrontalCortex"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Fo5_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Fo5_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Fo5_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Fo5_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Fo5_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Fo5_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Fo5_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Fo5_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Fo5_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Fo5_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Fo5_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Fo5_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Fo5_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Fo5_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Fo5_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Fo5_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Fo5_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-Fo5",
    name="Area Fo5 (OFC)",
)
ParcellationEntity.jba__area__fo6 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo6",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_lateralOrbitofrontalCortex"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Fo6_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Fo6_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Fo6_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Fo6_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Fo6_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Fo6_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Fo6_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Fo6_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Fo6_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Fo6_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Fo6_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Fo6_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Fo6_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Fo6_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Fo6_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Fo6_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Fo6_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-Fo6",
    name="Area Fo6 (OFC)",
)
ParcellationEntity.jba__area__fo7 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fo7",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_lateralOrbitofrontalCortex"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Fo7_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Fo7_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Fo7_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Fo7_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Fo7_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Fo7_PM-v2.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Fo7_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Fo7_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Fo7_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Fo7_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Fo7_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Fo7_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Fo7_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Fo7_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Fo7_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Fo7_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Fo7_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-Fo7",
    name="Area Fo7 (OFC)",
)
ParcellationEntity.jba__area__fp1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fp1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalPole"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-Fp1_PM-v2.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Fp1_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Fp1_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Fp1_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Fp1_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Fp1_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Fp1_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Fp1_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Fp1_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Fp1_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Fp1_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Fp1_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Fp1_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Fp1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Fp1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Fp1_PM-v5.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Fp1_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Fp1_PM-v5.1"
        },
    ],
    lookup_label="JBA_Area-Fp1",
    name="Area Fp1 (FPole)",
)
ParcellationEntity.jba__area__fp2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Fp2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalPole"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-Fp2_PM-v2.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Fp2_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Fp2_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Fp2_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Fp2_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Fp2_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Fp2_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Fp2_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Fp2_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Fp2_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Fp2_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Fp2_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Fp2_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Fp2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Fp2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Fp2_PM-v5.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Fp2_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Fp2_PM-v5.1"
        },
    ],
    lookup_label="JBA_Area-Fp2",
    name="Area Fp2 (FPole)",
)
ParcellationEntity.jba__area__ia = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ia",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_agranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Ia_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Ia_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Ia_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Ia_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Ia_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Ia_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Ia_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Ia_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Ia_PM-v4.0"},
    ],
    lookup_label="JBA_Area-Ia",
    name="Area Ia (Insula)",
)
ParcellationEntity.jba__area__ia1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ia1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_agranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Ia1_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Ia1_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Ia1_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Ia1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Ia1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Ia1_PM-v5.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Ia1_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Ia1_PM-v5.1"
        },
    ],
    lookup_label="JBA_Area-Ia1",
    name="Area Ia1 (Insula)",
)
ParcellationEntity.jba__area__ia2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ia2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_agranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Ia2_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Ia2_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Ia2_PM-v4.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Ia2_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Ia2_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Ia2_PM-v4.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Ia2_PM-v4.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Ia2_PM-v4.0"
        },
    ],
    lookup_label="JBA_Area-Ia2",
    name="Area Ia2 (Insula)",
)
ParcellationEntity.jba__area__ia3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ia3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_agranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Ia3_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Ia3_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Ia3_PM-v4.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Ia3_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Ia3_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Ia3_PM-v4.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Ia3_PM-v4.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Ia3_PM-v4.0"
        },
    ],
    lookup_label="JBA_Area-Ia3",
    name="Area Ia3 (Insula)",
)
ParcellationEntity.jba__area__id1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-Id1_PM-v11.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Id1_PM-v13.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Id1_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Id1_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Id1_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Id1_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Id1_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Id1_PM-v14.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Id1_PM-v14.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Id1_PM-v14.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Id1_PM-v14.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Id1_PM-v14.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Id1_PM-v14.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Id1_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Id1_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Id1_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Id1_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Id1_PM-v14.2"
        },
    ],
    lookup_label="JBA_Area-Id1",
    name="Area Id1 (Insula)",
)
ParcellationEntity.jba__area__id10 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id10",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Id10_PM-v14.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Id10_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Id10_PM-v4.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Id10_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Id10_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Id10_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Id10_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Id10_PM-v4.0"
        },
    ],
    lookup_label="JBA_Area-Id10",
    name="Area Id10 (Insula)",
)
ParcellationEntity.jba__area__id2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Id2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Id2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Id2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Id2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Id2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Id2_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Id2_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Id2_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Id2_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Id2_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Id2_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Id2_PM-v9.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Id2_PM-v9.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Id2_PM-v9.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Id2_PM-v9.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Id2_PM-v9.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Id2_PM-v9.1"
        },
    ],
    lookup_label="JBA_Area-Id2",
    name="Area Id2 (Insula)",
)
ParcellationEntity.jba__area__id3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Id3_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Id3_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Id3_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Id3_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Id3_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Id3_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Id3_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Id3_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Id3_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Id3_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Id3_PM-v9.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Id3_PM-v9.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Id3_PM-v9.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Id3_PM-v9.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Id3_PM-v9.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Id3_PM-v9.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Id3_PM-v9.1"
        },
    ],
    lookup_label="JBA_Area-Id3",
    name="Area Id3 (Insula)",
)
ParcellationEntity.jba__area__id4 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id4",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Id4_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Id4_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Id4_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Id4_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Id4_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Id4_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Id4_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Id4_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Id4_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Id4_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Id4_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Id4_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Id4_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Id4_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Id4_PM-v5.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Id4_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Id4_PM-v5.1"
        },
    ],
    lookup_label="JBA_Area-Id4",
    name="Area Id4 (Insula)",
)
ParcellationEntity.jba__area__id5 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id5",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Id5_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Id5_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Id5_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Id5_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Id5_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Id5_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Id5_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Id5_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Id5_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Id5_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Id5_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Id5_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Id5_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Id5_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Id5_PM-v5.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Id5_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Id5_PM-v5.1"
        },
    ],
    lookup_label="JBA_Area-Id5",
    name="Area Id5 (Insula)",
)
ParcellationEntity.jba__area__id6 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id6",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Id6_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Id6_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Id6_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Id6_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Id6_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Id6_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Id6_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Id6_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Id6_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Id6_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Id6_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Id6_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Id6_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Id6_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Id6_PM-v5.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Id6_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Id6_PM-v5.1"
        },
    ],
    lookup_label="JBA_Area-Id6",
    name="Area Id6 (Insula)",
)
ParcellationEntity.jba__area__id7 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id7",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Id7_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Id7_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Id7_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Id7_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Id7_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Id7_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Id7_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Id7_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Id7_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Id7_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Id7_PM-v8.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Id7_PM-v8.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Id7_PM-v8.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Id7_PM-v8.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Id7_PM-v8.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Id7_PM-v8.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Id7_PM-v8.1"
        },
    ],
    lookup_label="JBA_Area-Id7",
    name="Area Id7 (Insula)",
)
ParcellationEntity.jba__area__id8 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id8",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Id8_PM-v8.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Id8_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Id8_PM-v4.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Id8_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Id8_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Id8_PM-v4.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Id8_PM-v4.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Id8_PM-v4.0"
        },
    ],
    lookup_label="JBA_Area-Id8",
    name="Area Id8 (Insula)",
)
ParcellationEntity.jba__area__id9 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Id9",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Id9_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Id9_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Id9_PM-v4.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Id9_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Id9_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Id9_PM-v4.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Id9_PM-v4.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Id9_PM-v4.0"
        },
    ],
    lookup_label="JBA_Area-Id9",
    name="Area Id9 (Insula)",
)
ParcellationEntity.jba__area__ig1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ig1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_granularInsula"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-Ig1_PM-v11.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Ig1_PM-v13.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Ig1_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Ig1_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Ig1_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Ig1_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Ig1_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Ig1_PM-v14.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Ig1_PM-v14.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Ig1_PM-v14.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Ig1_PM-v14.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Ig1_PM-v14.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Ig1_PM-v14.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Ig1_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Ig1_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Ig1_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Ig1_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Ig1_PM-v14.2"
        },
    ],
    lookup_label="JBA_Area-Ig1",
    name="Area Ig1 (Insula)",
)
ParcellationEntity.jba__area__ig2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ig2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_granularInsula"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-Ig2_PM-v11.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Ig2_PM-v13.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Ig2_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Ig2_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Ig2_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Ig2_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Ig2_PM-v13.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Ig2_PM-v14.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Ig2_PM-v14.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Ig2_PM-v14.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Ig2_PM-v14.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Ig2_PM-v14.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Ig2_PM-v14.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Ig2_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Ig2_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Ig2_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Ig2_PM-v14.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Ig2_PM-v14.2"
        },
    ],
    lookup_label="JBA_Area-Ig2",
    name="Area Ig2 (Insula)",
)
ParcellationEntity.jba__area__ig3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ig3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_granularInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-Ig3_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-Ig3_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-Ig3_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-Ig3_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-Ig3_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-Ig3_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-Ig3_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-Ig3_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-Ig3_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Ig3_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Ig3_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Ig3_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Ig3_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Ig3_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Ig3_PM-v5.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Ig3_PM-v5.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Ig3_PM-v5.1"
        },
    ],
    lookup_label="JBA_Area-Ig3",
    name="Area Ig3 (Insula)",
)
ParcellationEntity.jba__area__ph1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ph1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parahippocampalGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Ph1_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Ph1_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Ph1_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Ph1_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Ph1_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Ph1_PM-v7.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Ph1_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Ph1_PM-v7.2"
        },
    ],
    lookup_label="JBA_Area-Ph1",
    name="Area Ph1 (PhG)",
)
ParcellationEntity.jba__area__ph2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ph2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parahippocampalGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Ph2_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Ph2_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Ph2_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Ph2_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Ph2_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Ph2_PM-v7.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Ph2_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Ph2_PM-v7.2"
        },
    ],
    lookup_label="JBA_Area-Ph2",
    name="Area Ph2 (PhG)",
)
ParcellationEntity.jba__area__ph3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-Ph3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parahippocampalGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-Ph3_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-Ph3_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-Ph3_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-Ph3_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-Ph3_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-Ph3_PM-v7.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-Ph3_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-Ph3_PM-v7.2"
        },
    ],
    lookup_label="JBA_Area-Ph3",
    name="Area Ph3 (PhG)",
)
ParcellationEntity.jba__area__te_i = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TeI",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-TeI_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-TeI_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-TeI_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-TeI_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-TeI_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-TeI_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-TeI_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-TeI_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-TeI_PM-v6.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-TeI_PM-v6.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-TeI_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-TeI_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-TeI_PM-v6.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-TeI_PM-v6.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-TeI_PM-v6.2"
        },
    ],
    lookup_label="JBA_Area-TeI",
    name="Area TeI (STG)",
)
ParcellationEntity.jba__area_a29 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-a29",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_retrosplenialPart"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-a29_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-a29_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-a29_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-a29_PM-v11.0"},
    ],
    lookup_label="JBA_Area-a29",
    name="Area a29 (retrosplenial)",
)
ParcellationEntity.jba__area_a30 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-a30",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_retrosplenialPart"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-a30_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-a30_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-a30_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-a30_PM-v11.0"},
    ],
    lookup_label="JBA_Area-a30",
    name="Area a30 (retrosplenial)",
)
ParcellationEntity.jba__area_fg1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-FG1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fusiformGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-FG1_PM-v1.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-FG1_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-FG1_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-FG1_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-FG1_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-FG1_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-FG1_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-FG1_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-FG1_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-FG1_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-FG1_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-FG1_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-FG1_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-FG1_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-FG1_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-FG1_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-FG1_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-FG1_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-FG1",
    name="Area FG1 (FusG)",
)
ParcellationEntity.jba__area_fg2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-FG2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fusiformGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-FG2_PM-v1.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-FG2_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-FG2_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-FG2_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-FG2_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-FG2_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-FG2_PM-v1.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-FG2_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-FG2_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-FG2_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-FG2_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-FG2_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-FG2_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-FG2_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-FG2_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-FG2_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-FG2_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-FG2_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-FG2",
    name="Area FG2 (FusG)",
)
ParcellationEntity.jba__area_fg3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-FG3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fusiformGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-FG3_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-FG3_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-FG3_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-FG3_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-FG3_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-FG3_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-FG3_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-FG3_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-FG3_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-FG3_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-FG3_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-FG3_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-FG3_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-FG3_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-FG3_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-FG3_PM-v7.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-FG3_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-FG3_PM-v7.2"
        },
    ],
    lookup_label="JBA_Area-FG3",
    name="Area FG3 (FusG)",
)
ParcellationEntity.jba__area_fg4 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-FG4",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fusiformGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-FG4_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-FG4_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-FG4_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-FG4_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-FG4_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-FG4_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-FG4_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-FG4_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-FG4_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-FG4_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-FG4_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-FG4_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-FG4_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-FG4_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-FG4_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-FG4_PM-v7.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-FG4_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-FG4_PM-v7.2"
        },
    ],
    lookup_label="JBA_Area-FG4",
    name="Area FG4 (FusG)",
)
ParcellationEntity.jba__area_h_ip1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_intraparietalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hIP1_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hIP1_PM-v6.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hIP1_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hIP1_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hIP1_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hIP1_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hIP1_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hIP1_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hIP1_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hIP1_PM-v7.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hIP1_PM-v7.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hIP1_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hIP1_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hIP1_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hIP1_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hIP1_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hIP1_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hIP1_PM-v7.2"
        },
    ],
    lookup_label="JBA_Area-hIP1",
    name="Area hIP1 (IPS)",
)
ParcellationEntity.jba__area_h_ip2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_intraparietalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hIP2_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hIP2_PM-v6.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hIP2_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hIP2_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hIP2_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hIP2_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hIP2_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hIP2_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hIP2_PM-v7.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hIP2_PM-v7.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hIP2_PM-v7.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hIP2_PM-v7.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hIP2_PM-v7.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hIP2_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hIP2_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hIP2_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hIP2_PM-v7.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hIP2_PM-v7.2"
        },
    ],
    lookup_label="JBA_Area-hIP2",
    name="Area hIP2 (IPS)",
)
ParcellationEntity.jba__area_h_ip3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_intraparietalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hIP3_PM-v8.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hIP3_PM-v8.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hIP3_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hIP3_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hIP3_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hIP3_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hIP3_PM-v8.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hIP3_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hIP3_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hIP3_PM-v9.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hIP3_PM-v9.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hIP3_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hIP3_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hIP3_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hIP3_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hIP3_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hIP3_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hIP3_PM-v9.2"
        },
    ],
    lookup_label="JBA_Area-hIP3",
    name="Area hIP3 (IPS)",
)
ParcellationEntity.jba__area_h_ip4 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP4",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_intraparietalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hIP4_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hIP4_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hIP4_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hIP4_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hIP4_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hIP4_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hIP4_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hIP4_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hIP4_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hIP4_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hIP4_PM-v7.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hIP4_PM-v7.3"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hIP4_PM-v7.3"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hIP4_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hIP4_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hIP4_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hIP4_PM-v7.3"
        },
    ],
    lookup_label="JBA_Area-hIP4",
    name="Area hIP4 (IPS)",
)
ParcellationEntity.jba__area_h_ip5 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP5",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_intraparietalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hIP5_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hIP5_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hIP5_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hIP5_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hIP5_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hIP5_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hIP5_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hIP5_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hIP5_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hIP5_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hIP5_PM-v7.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hIP5_PM-v7.3"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hIP5_PM-v7.3"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hIP5_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hIP5_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hIP5_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hIP5_PM-v7.3"
        },
    ],
    lookup_label="JBA_Area-hIP5",
    name="Area hIP5 (IPS)",
)
ParcellationEntity.jba__area_h_ip6 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP6",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_intraparietalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hIP6_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hIP6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hIP6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hIP6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hIP6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hIP6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hIP6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hIP6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hIP6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hIP6_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hIP6_PM-v7.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hIP6_PM-v7.3"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hIP6_PM-v7.3"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hIP6_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hIP6_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hIP6_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hIP6_PM-v7.3"
        },
    ],
    lookup_label="JBA_Area-hIP6",
    name="Area hIP6 (IPS)",
)
ParcellationEntity.jba__area_h_ip7 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP7",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_intraparietalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hIP7_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hIP7_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hIP7_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hIP7_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hIP7_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hIP7_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hIP7_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hIP7_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hIP7_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hIP7_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hIP7_PM-v7.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hIP7_PM-v7.3"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hIP7_PM-v7.3"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hIP7_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hIP7_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hIP7_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hIP7_PM-v7.3"
        },
    ],
    lookup_label="JBA_Area-hIP7",
    name="Area hIP7 (IPS)",
)
ParcellationEntity.jba__area_h_ip8 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hIP8",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_intraparietalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hIP8_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hIP8_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hIP8_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hIP8_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hIP8_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hIP8_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hIP8_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hIP8_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hIP8_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hIP8_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hIP8_PM-v7.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hIP8_PM-v7.3"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hIP8_PM-v7.3"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hIP8_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hIP8_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hIP8_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hIP8_PM-v7.3"
        },
    ],
    lookup_label="JBA_Area-hIP8",
    name="Area hIP8 (IPS)",
)
ParcellationEntity.jba__area_h_oc1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_occipitalCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hOc1_PM-v2.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hOc1_PM-v2.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hOc1_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hOc1_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hOc1_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hOc1_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hOc1_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hOc1_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hOc1_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hOc1_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hOc1_deep"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hOc1_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hOc1_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hOc1_PM-v4.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hOc1_deep"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hOc1_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hOc1_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hOc1_PM-v4.2"
        },
    ],
    lookup_label="JBA_Area-hOc1",
    name="Area hOc1 (V1, 17, CalcS)",
)
ParcellationEntity.jba__area_h_oc2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_occipitalCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hOc2_PM-v2.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hOc2_PM-v2.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hOc2_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hOc2_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hOc2_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hOc2_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hOc2_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hOc2_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hOc2_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hOc2_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hOc2_deep"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hOc2_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hOc2_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hOc2_PM-v4.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hOc2_deep"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hOc2_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hOc2_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hOc2_PM-v4.2"
        },
    ],
    lookup_label="JBA_Area-hOc2",
    name="Area hOc2 (V2, 18)",
)
ParcellationEntity.jba__area_h_oc3d = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc3d",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dorsalOccipitalCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hOc3d_PM-v2.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hOc3d_PM-v2.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hOc3d_PM-v2.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hOc3d_PM-v2.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hOc3d_PM-v2.4"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hOc3d_PM-v2.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hOc3d_PM-v2.4"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hOc3d_PM-v4.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hOc3d_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hOc3d_PM-v4.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hOc3d_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hOc3d_PM-v4.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hOc3d_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hOc3d_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hOc3d_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hOc3d_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hOc3d_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hOc3d_PM-v4.2"
        },
    ],
    lookup_label="JBA_Area-hOc3d",
    name="Area hOc3d (Cuneus)",
)
ParcellationEntity.jba__area_h_oc3v = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc3v",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_ventralOccipitalCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hOc3v_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hOc3v_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hOc3v_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hOc3v_PM-v3.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hOc3v_PM-v3.4"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hOc3v_PM-v3.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hOc3v_PM-v3.4"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hOc3v_PM-v5.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hOc3v_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hOc3v_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hOc3v_deep"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hOc3v_PM-v5.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hOc3v_PM-v5.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hOc3v_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hOc3v_deep"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hOc3v_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hOc3v_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hOc3v_PM-v5.2"
        },
    ],
    lookup_label="JBA_Area-hOc3v",
    name="Area hOc3v (LingG)",
)
ParcellationEntity.jba__area_h_oc4d = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc4d",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dorsalOccipitalCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hOc4d_PM-v2.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hOc4d_PM-v2.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hOc4d_PM-v2.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hOc4d_PM-v2.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hOc4d_PM-v2.4"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hOc4d_PM-v2.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hOc4d_PM-v2.4"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hOc4d_PM-v4.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hOc4d_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hOc4d_PM-v4.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hOc4d_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hOc4d_PM-v4.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hOc4d_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hOc4d_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hOc4d_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hOc4d_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hOc4d_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hOc4d_PM-v4.2"
        },
    ],
    lookup_label="JBA_Area-hOc4d",
    name="Area hOc4d (Cuneus)",
)
ParcellationEntity.jba__area_h_oc4la = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc4la",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_lateralOccipitalCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hOc4la_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hOc4la_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hOc4la_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hOc4la_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hOc4la_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hOc4la_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hOc4la_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hOc4la_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hOc4la_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hOc4la_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hOc4la_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hOc4la_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hOc4la_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hOc4la_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hOc4la_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hOc4la_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hOc4la_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hOc4la_PM-v5.2"
        },
    ],
    lookup_label="JBA_Area-hOc4la",
    name="Area hOc4la (LOC)",
)
ParcellationEntity.jba__area_h_oc4lp = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc4lp",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_lateralOccipitalCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hOc4lp_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hOc4lp_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hOc4lp_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hOc4lp_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hOc4lp_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hOc4lp_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hOc4lp_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hOc4lp_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hOc4lp_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hOc4lp_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hOc4lp_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hOc4lp_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hOc4lp_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hOc4lp_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hOc4lp_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hOc4lp_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hOc4lp_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hOc4lp_PM-v5.2"
        },
    ],
    lookup_label="JBA_Area-hOc4lp",
    name="Area hOc4lp (LOC)",
)
ParcellationEntity.jba__area_h_oc4v = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc4v",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_ventralOccipitalCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hOc4v_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hOc4v_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hOc4v_PM-v3.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hOc4v_PM-v3.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hOc4v_PM-v3.4"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hOc4v_PM-v3.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hOc4v_PM-v3.4"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hOc4v_PM-v5.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hOc4v_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hOc4v_PM-v5.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hOc4v_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hOc4v_PM-v5.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hOc4v_PM-v5.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hOc4v_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hOc4v_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hOc4v_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hOc4v_PM-v5.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hOc4v_PM-v5.2"
        },
    ],
    lookup_label="JBA_Area-hOc4v",
    name="Area hOc4v (LingG)",
)
ParcellationEntity.jba__area_h_oc5 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc5",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_lateralOccipitalCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-hOc5_PM-v2.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hOc5_PM-v2.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hOc5_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hOc5_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hOc5_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hOc5_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hOc5_PM-v2.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hOc5_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hOc5_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hOc5_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hOc5_deep"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hOc5_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hOc5_PM-v4.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hOc5_PM-v4.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hOc5_deep"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hOc5_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hOc5_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hOc5_PM-v4.2"
        },
    ],
    lookup_label="JBA_Area-hOc5",
    name="Area hOc5 (LOC)",
)
ParcellationEntity.jba__area_h_oc6 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hOc6",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dorsalOccipitalCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hOc6_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hOc6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hOc6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hOc6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hOc6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hOc6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hOc6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hOc6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hOc6_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hOc6_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hOc6_PM-v7.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hOc6_PM-v7.3"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hOc6_PM-v7.3"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hOc6_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hOc6_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hOc6_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hOc6_PM-v7.3"
        },
    ],
    lookup_label="JBA_Area-hOc6",
    name="Area hOc6 (POS)",
)
ParcellationEntity.jba__area_h_po1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-hPO1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parieto-occipitalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-hPO1_PM-v7.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-hPO1_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-hPO1_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-hPO1_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-hPO1_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-hPO1_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-hPO1_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-hPO1_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-hPO1_PM-v7.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-hPO1_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-hPO1_PM-v7.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-hPO1_PM-v7.3"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-hPO1_PM-v7.3"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-hPO1_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-hPO1_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-hPO1_PM-v7.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-hPO1_PM-v7.3"
        },
    ],
    lookup_label="JBA_Area-hPO1",
    name="Area hPO1 (POS)",
)
ParcellationEntity.jba__area_i29 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-i29",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_retrosplenialPart"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-i29_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-i29_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-i29_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-i29_PM-v11.0"},
    ],
    lookup_label="JBA_Area-i29",
    name="Area i29 (retrosplenial)",
)
ParcellationEntity.jba__area_i30 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-i30",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_retrosplenialPart"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-i30_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-i30_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-i30_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-i30_PM-v11.0"},
    ],
    lookup_label="JBA_Area-i30",
    name="Area i30 (retrosplenial)",
)
ParcellationEntity.jba__area_ifj1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFJ1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-IFJ1_PM-v9.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-IFJ1_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-IFJ1_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-IFJ1_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-IFJ1_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-IFJ1_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-IFJ1_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-IFJ1_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-IFJ1",
    name="Area IFJ1 (IFS,PreCS)",
)
ParcellationEntity.jba__area_ifj2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFJ2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-IFJ2_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-IFJ2_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-IFJ2_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-IFJ2_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-IFJ2_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-IFJ2_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-IFJ2_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-IFJ2_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-IFJ2",
    name="Area IFJ2 (IFS,PreCS)",
)
ParcellationEntity.jba__area_ifs1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFS1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-IFS1_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-IFS1_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-IFS1_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-IFS1_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-IFS1_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-IFS1_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-IFS1_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-IFS1_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-IFS1",
    name="Area IFS1 (IFS)",
)
ParcellationEntity.jba__area_ifs2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFS2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-IFS2_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-IFS2_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-IFS2_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-IFS2_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-IFS2_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-IFS2_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-IFS2_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-IFS2_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-IFS2",
    name="Area IFS2 (IFS)",
)
ParcellationEntity.jba__area_ifs3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFS3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-IFS3_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-IFS3_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-IFS3_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-IFS3_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-IFS3_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-IFS3_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-IFS3_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-IFS3_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-IFS3",
    name="Area IFS3 (IFS)",
)
ParcellationEntity.jba__area_ifs4 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-IFS4",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-IFS4_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-IFS4_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-IFS4_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-IFS4_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-IFS4_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-IFS4_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-IFS4_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-IFS4_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-IFS4",
    name="Area IFS4 (IFS)",
)
ParcellationEntity.jba__area_mfg1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-MFG1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_middleFrontalGyrus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-MFG1_deep"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-MFG1_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-MFG1_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-MFG1_PM-v9.0"
        },
    ],
    lookup_label="JBA_Area-MFG1",
    name="Area MFG1 (MFG)",
)
ParcellationEntity.jba__area_mfg2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-MFG2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fronto-marginalSulcus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-MFG2_deep"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-MFG2_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-MFG2_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-MFG2_PM-v9.0"
        },
    ],
    lookup_label="JBA_Area-MFG2",
    name="Area MFG2 (MFG)",
)
ParcellationEntity.jba__area_op1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalOperculum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-OP1_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-OP1_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-OP1_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-OP1_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-OP1_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-OP1_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-OP1_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-OP1_PM-v12.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-OP1_PM-v12.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-OP1_PM-v12.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-OP1_PM-v12.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-OP1_PM-v12.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-OP1_PM-v12.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-OP1_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-OP1_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-OP1_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-OP1_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-OP1_PM-v12.2"
        },
    ],
    lookup_label="JBA_Area-OP1",
    name="Area OP1 (POperc)",
)
ParcellationEntity.jba__area_op2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalOperculum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-OP2_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-OP2_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-OP2_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-OP2_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-OP2_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-OP2_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-OP2_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-OP2_PM-v12.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-OP2_PM-v12.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-OP2_PM-v12.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-OP2_PM-v12.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-OP2_PM-v12.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-OP2_PM-v12.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-OP2_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-OP2_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-OP2_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-OP2_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-OP2_PM-v12.2"
        },
    ],
    lookup_label="JBA_Area-OP2",
    name="Area OP2 (POperc)",
)
ParcellationEntity.jba__area_op3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalOperculum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-OP3_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-OP3_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-OP3_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-OP3_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-OP3_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-OP3_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-OP3_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-OP3_PM-v12.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-OP3_PM-v12.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-OP3_PM-v12.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-OP3_PM-v12.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-OP3_PM-v12.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-OP3_PM-v12.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-OP3_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-OP3_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-OP3_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-OP3_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-OP3_PM-v12.2"
        },
    ],
    lookup_label="JBA_Area-OP3",
    name="Area OP3 (POperc)",
)
ParcellationEntity.jba__area_op4 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP4",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalOperculum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-OP4_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-OP4_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-OP4_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-OP4_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-OP4_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-OP4_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-OP4_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-OP4_PM-v12.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-OP4_PM-v12.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-OP4_PM-v12.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-OP4_PM-v12.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-OP4_PM-v12.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-OP4_PM-v12.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-OP4_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-OP4_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-OP4_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-OP4_PM-v12.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-OP4_PM-v12.2"
        },
    ],
    lookup_label="JBA_Area-OP4",
    name="Area OP4 (POperc)",
)
ParcellationEntity.jba__area_op5 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP5",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalOperculum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-OP5_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-OP5_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-OP5_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-OP5_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-OP5_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-OP5_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-OP5_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-OP5_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-OP5_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-OP5_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-OP5_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-OP5_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-OP5_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-OP5_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-OP5_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-OP5",
    name="Area Op5 (Frontal Operculum)",
)
ParcellationEntity.jba__area_op6 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP6",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalOperculum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-OP6_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-OP6_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-OP6_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-OP6_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-OP6_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-OP6_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-OP6_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-OP6_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-OP6_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-OP6_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-OP6_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-OP6_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-OP6_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-OP6_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-OP6_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-OP6",
    name="Area Op6 (Frontal Operculum)",
)
ParcellationEntity.jba__area_op7 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP7",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalOperculum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-OP7_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-OP7_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-OP7_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-OP7_PM-v2.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-OP7_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-OP7_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-OP7_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-OP7_PM-v3.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-OP7_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-OP7_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-OP7_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-OP7_PM-v3.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-OP7_PM-v3.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-OP7_PM-v3.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-OP7_PM-v3.2"
        },
    ],
    lookup_label="JBA_Area-OP7",
    name="Area Op7 (Frontal Operculum)",
)
ParcellationEntity.jba__area_op8 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP8",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalOperculum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-OP8_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-OP8_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-OP8_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-OP8_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-OP8_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-OP8_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-OP8_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-OP8_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-OP8_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-OP8_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-OP8_PM-v6.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-OP8_PM-v6.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-OP8_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-OP8_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-OP8_PM-v6.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-OP8_PM-v6.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-OP8_PM-v6.2"
        },
    ],
    lookup_label="JBA_Area-OP8",
    name="Area Op8 (Frontal Operculum)",
)
ParcellationEntity.jba__area_op9 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-OP9",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalOperculum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-OP9_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-OP9_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-OP9_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-OP9_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-OP9_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-OP9_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-OP9_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-OP9_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-OP9_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-OP9_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-OP9_PM-v6.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-OP9_PM-v6.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-OP9_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-OP9_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-OP9_PM-v6.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-OP9_PM-v6.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-OP9_PM-v6.2"
        },
    ],
    lookup_label="JBA_Area-OP9",
    name="Area Op9 (Frontal Operculum)",
)
ParcellationEntity.jba__area_p24ab = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24ab",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalCingulateGyrus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-p24ab_PM-v16.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-p24ab_PM-v16.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-p24ab_PM-v16.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-p24ab_PM-v16.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-p24ab_PM-v16.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-p24ab_PM-v16.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-p24ab_PM-v18.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-p24ab_PM-v18.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-p24ab_PM-v18.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-p24ab_PM-v18.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-p24ab_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-p24ab_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-p24ab_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-p24ab_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-p24ab_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-p24ab_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-p24ab_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-p24ab",
    name="Area p24ab (pACC)",
)
ParcellationEntity.jba__area_p24ab_p24a = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24ab.p24a",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24ab"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-p24ab.p24a_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-p24ab.p24a_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-p24ab.p24a_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-p24ab.p24a_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-p24ab.p24a",
    name="Area p24ab.p24a (pACC)",
)
ParcellationEntity.jba__area_p24ab_p24b = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24ab.p24b",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24ab"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-p24ab.p24b_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-p24ab.p24b_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-p24ab.p24b_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-p24ab.p24b_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-p24ab.p24b",
    name="Area p24ab.p24b (pACC)",
)
ParcellationEntity.jba__area_p24c = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24c",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalCingulateGyrus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-p24c_PM-v16.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-p24c_PM-v16.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-p24c_PM-v16.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-p24c_PM-v16.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-p24c_PM-v16.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-p24c_PM-v16.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-p24c_PM-v18.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-p24c_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-p24c_PM-v18.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-p24c_PM-v18.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-p24c_PM-v20.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-p24c_PM-v20.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-p24c_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-p24c_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-p24c_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-p24c_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-p24c_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-p24c",
    name="Area p24c (pACC)",
)
ParcellationEntity.jba__area_p24c_pd24cd = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24c.pd24cd",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24c"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-p24c.pd24cd_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-p24c.pd24cd_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-p24c.pd24cd_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-p24c.pd24cd_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-p24c.pd24cd",
    name="Area p24c.pd24cd (pACC)",
)
ParcellationEntity.jba__area_p24c_pd24cv = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24c.pd24cv",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24c"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-p24c.pd24cv_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-p24c.pd24cv_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-p24c.pd24cv_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-p24c.pd24cv_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-p24c.pd24cv",
    name="Area p24c.pd24cv (pACC)",
)
ParcellationEntity.jba__area_p24c_pv24c = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24c.pv24c",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p24c"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-p24c.pv24c_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-p24c.pv24c_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-p24c.pv24c_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-p24c.pv24c_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-p24c.pv24c",
    name="Area p24c.pv24c (pACC)",
)
ParcellationEntity.jba__area_p29 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p29",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_retrosplenialPart"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-p29_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-p29_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-p29_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-p29_PM-v11.0"},
    ],
    lookup_label="JBA_Area-p29",
    name="Area p29 (retrosplenial)",
)
ParcellationEntity.jba__area_p30 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p30",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_retrosplenialPart"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-p30_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-p30_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-p30_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-p30_PM-v11.0"},
    ],
    lookup_label="JBA_Area-p30",
    name="Area p30 (retrosplenial)",
)
ParcellationEntity.jba__area_p32 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-p32",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalCingulateGyrus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-p32_PM-v16.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-p32_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-p32_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-p32_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-p32_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-p32_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-p32_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-p32_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-p32_PM-v18.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-p32_PM-v18.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-p32_PM-v20.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-p32_PM-v20.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-p32_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-p32_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-p32_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-p32_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-p32_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-p32",
    name="Area p32 (pACC)",
)
ParcellationEntity.jba__area_p_fcm = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PFcm",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorParietalLobule"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-PFcm_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-PFcm_PM-v9.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-PFcm_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-PFcm_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-PFcm_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-PFcm_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-PFcm_PM-v9.4"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-PFcm_PM-v11.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-PFcm_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-PFcm_PM-v11.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-PFcm_PM-v11.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-PFcm_PM-v11.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-PFcm_PM-v11.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-PFcm_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-PFcm_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-PFcm_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-PFcm_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-PFcm_PM-v11.2"
        },
    ],
    lookup_label="JBA_Area-PFcm",
    name="Area PFcm (IPL)",
)
ParcellationEntity.jba__area_p_fm = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PFm",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-PFm_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-PFm_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-PFm_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-PFm_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-PFm_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-PFm_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-PFm_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-PFm_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-PFm_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-PFm_PM-v11.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-PFm_PM-v11.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-PFm_PM-v11.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-PFm_PM-v11.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-PFm_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-PFm_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-PFm_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-PFm_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-PFm_PM-v11.2"
        },
    ],
    lookup_label="JBA_Area-PFm",
    name="Area PFm (IPL)",
)
ParcellationEntity.jba__area_p_fop = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PFop",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorParietalLobule"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-PFop_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-PFop_PM-v9.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-PFop_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-PFop_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-PFop_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-PFop_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-PFop_PM-v9.4"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-PFop_PM-v11.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-PFop_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-PFop_PM-v11.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-PFop_PM-v11.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-PFop_PM-v11.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-PFop_PM-v11.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-PFop_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-PFop_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-PFop_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-PFop_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-PFop_PM-v11.2"
        },
    ],
    lookup_label="JBA_Area-PFop",
    name="Area PFop (IPL)",
)
ParcellationEntity.jba__area_p_ft = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PFt",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-PFt_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-PFt_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-PFt_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-PFt_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-PFt_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-PFt_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-PFt_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-PFt_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-PFt_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-PFt_PM-v11.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-PFt_PM-v11.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-PFt_PM-v11.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-PFt_PM-v11.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-PFt_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-PFt_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-PFt_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-PFt_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-PFt_PM-v11.2"
        },
    ],
    lookup_label="JBA_Area-PFt",
    name="Area PFt (IPL)",
)
ParcellationEntity.jba__area_p_ga = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PGa",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-PGa_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-PGa_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-PGa_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-PGa_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-PGa_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-PGa_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-PGa_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-PGa_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-PGa_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-PGa_PM-v11.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-PGa_PM-v11.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-PGa_PM-v11.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-PGa_PM-v11.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-PGa_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-PGa_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-PGa_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-PGa_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-PGa_PM-v11.2"
        },
    ],
    lookup_label="JBA_Area-PGa",
    name="Area PGa (IPL)",
)
ParcellationEntity.jba__area_p_gp = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PGp",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-PGp_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-PGp_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-PGp_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-PGp_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-PGp_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-PGp_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-PGp_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-PGp_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-PGp_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-PGp_PM-v11.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-PGp_PM-v11.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-PGp_PM-v11.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-PGp_PM-v11.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-PGp_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-PGp_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-PGp_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-PGp_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-PGp_PM-v11.2"
        },
    ],
    lookup_label="JBA_Area-PGp",
    name="Area PGp (IPL)",
)
ParcellationEntity.jba__area_pf = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-PF",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorParietalLobule"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-PF_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-PF_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-PF_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-PF_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-PF_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-PF_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-PF_PM-v9.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-PF_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-PF_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-PF_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-PF_PM-v11.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-PF_PM-v11.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-PF_PM-v11.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-PF_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-PF_PM-v11.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-PF_PM-v11.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-PF_PM-v11.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-PF_PM-v11.2"
        },
    ],
    lookup_label="JBA_Area-PF",
    name="Area PF (IPL)",
)
ParcellationEntity.jba__area_s24 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-s24",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalCingulateGyrus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-s24_PM-v16.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-s24_PM-v16.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-s24_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-s24_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-s24_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-s24_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-s24_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-s24_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-s24_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-s24_PM-v18.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-s24_PM-v18.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-s24_PM-v20.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-s24_PM-v20.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-s24_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-s24_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-s24_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-s24_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-s24_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-s24",
    name="Area s24 (sACC)",
)
ParcellationEntity.jba__area_s24_s24a = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-s24.s24a",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-s24"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-s24.s24a_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-s24.s24a_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-s24.s24a_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-s24.s24a_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-s24.s24a",
    name="Area s24.s24a (sACC)",
)
ParcellationEntity.jba__area_s24_s24b = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-s24.s24b",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-s24"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-s24.s24b_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-s24.s24b_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-s24.s24b_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-s24.s24b_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-s24.s24b",
    name="Area s24.s24b (sACC)",
)
ParcellationEntity.jba__area_s32 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-s32",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalCingulateGyrus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-s32_PM-v16.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-s32_PM-v16.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-s32_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-s32_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-s32_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-s32_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-s32_PM-v16.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-s32_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-s32_PM-v18.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-s32_PM-v18.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-s32_PM-v18.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-s32_PM-v20.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-s32_PM-v20.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-s32_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-s32_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-s32_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-s32_PM-v20.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-s32_PM-v20.1"
        },
    ],
    lookup_label="JBA_Area-s32",
    name="Area s32 (sACC)",
)
ParcellationEntity.jba__area_sfs1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-SFS1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorFrontalSulcus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-SFS1_deep"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-SFS1_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-SFS1_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-SFS1_PM-v9.0"
        },
    ],
    lookup_label="JBA_Area-SFS1",
    name="Area SFS1 (SFS)",
)
ParcellationEntity.jba__area_sfs2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-SFS2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorFrontalSulcus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-SFS2_deep"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-SFS2_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-SFS2_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-SFS2_PM-v9.0"
        },
    ],
    lookup_label="JBA_Area-SFS2",
    name="Area SFS2 (SFS)",
)
ParcellationEntity.jba__area_sts1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-STS1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorTemporalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-STS1_PM-v3.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-STS1_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-STS1_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-STS1_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-STS1_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-STS1_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-STS1_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-STS1_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-STS1_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-STS1_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-STS1_PM-v5.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-STS1_PM-v5.3"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-STS1_PM-v5.3"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-STS1_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-STS1_PM-v5.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-STS1_PM-v5.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-STS1_PM-v5.3"
        },
    ],
    lookup_label="JBA_Area-STS1",
    name="Area STS1 (STS)",
)
ParcellationEntity.jba__area_sts2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-STS2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorTemporalSulcus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-STS2_PM-v3.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-STS2_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-STS2_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-STS2_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-STS2_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-STS2_PM-v3.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-STS2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-STS2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-STS2_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-STS2_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-STS2_PM-v5.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-STS2_PM-v5.3"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-STS2_PM-v5.3"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-STS2_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-STS2_PM-v5.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-STS2_PM-v5.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-STS2_PM-v5.3"
        },
    ],
    lookup_label="JBA_Area-STS2",
    name="Area STS2 (STS)",
)
ParcellationEntity.jba__area_te_1_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-1.0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_HeschlsGyrus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-TE-1.0_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-TE-1.0_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-TE-1.0_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-TE-1.0_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-TE-1.0_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-TE-1.0_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-TE-1.0_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-TE-1.0_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-TE-1.0_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-TE-1.0_PM-v6.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-TE-1.0_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-TE-1.0_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-TE-1.0_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-TE-1.0_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-TE-1.0_int"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-TE-1.0_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-TE-1.0_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-TE-1.0_PM-v6.2"
        },
    ],
    lookup_label="JBA_Area-TE-1.0",
    name="Area TE 1.0 (HESCHL)",
)
ParcellationEntity.jba__area_te_1_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-1.1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_HeschlsGyrus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-TE-1.1_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-TE-1.1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-TE-1.1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-TE-1.1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-TE-1.1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-TE-1.1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-TE-1.1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-TE-1.1_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-TE-1.1_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-TE-1.1_PM-v6.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-TE-1.1_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-TE-1.1_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-TE-1.1_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-TE-1.1_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-TE-1.1_int"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-TE-1.1_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-TE-1.1_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-TE-1.1_PM-v6.2"
        },
    ],
    lookup_label="JBA_Area-TE-1.1",
    name="Area TE 1.1 (HESCHL)",
)
ParcellationEntity.jba__area_te_1_2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-1.2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_HeschlsGyrus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-TE-1.2_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-TE-1.2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-TE-1.2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-TE-1.2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-TE-1.2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-TE-1.2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-TE-1.2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-TE-1.2_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-TE-1.2_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-TE-1.2_PM-v6.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-TE-1.2_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-TE-1.2_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-TE-1.2_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-TE-1.2_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-TE-1.2_int"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-TE-1.2_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-TE-1.2_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-TE-1.2_PM-v6.2"
        },
    ],
    lookup_label="JBA_Area-TE-1.2",
    name="Area TE 1.2 (HESCHL)",
)
ParcellationEntity.jba__area_te_2_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-2.1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorTemporalGyrus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-TE-2.1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-TE-2.1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-TE-2.1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-TE-2.1_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-TE-2.1_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-TE-2.1_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-TE-2.1_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-TE-2.1_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-TE-2.1_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-TE-2.1_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-TE-2.1_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-TE-2.1_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-TE-2.1_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-TE-2.1_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-TE-2.1_PM-v6.2"
        },
    ],
    lookup_label="JBA_Area-TE-2.1",
    name="Area TE 2.1 (STG)",
)
ParcellationEntity.jba__area_te_2_2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-2.2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorTemporalGyrus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-TE-2.2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-TE-2.2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-TE-2.2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-TE-2.2_PM-v5.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-TE-2.2_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-TE-2.2_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-TE-2.2_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-TE-2.2_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-TE-2.2_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-TE-2.2_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-TE-2.2_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-TE-2.2_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-TE-2.2_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-TE-2.2_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-TE-2.2_PM-v6.2"
        },
    ],
    lookup_label="JBA_Area-TE-2.2",
    name="Area TE 2.2 (STG)",
)
ParcellationEntity.jba__area_te_3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TE-3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorTemporalGyrus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Area-TE-3_PM-v5.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Area-TE-3_PM-v5.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Area-TE-3_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-TE-3_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-TE-3_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-TE-3_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-TE-3_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-TE-3_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-TE-3_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-TE-3_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-TE-3_int"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-TE-3_PM-v6.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-TE-3_PM-v6.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-TE-3_PM-v6.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-TE-3_int"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-TE-3_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-TE-3_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-TE-3_PM-v6.2"
        },
    ],
    lookup_label="JBA_Area-TE-3",
    name="Area TE 3 (STG)",
)
ParcellationEntity.jba__area_ti = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TI",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalInsula"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Area-TI_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Area-TI_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Area-TI_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Area-TI_PM-v5.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Area-TI_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Area-TI_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Area-TI_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-TI_PM-v6.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-TI_PM-v6.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-TI_PM-v6.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-TI_PM-v6.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-TI_PM-v6.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-TI_PM-v6.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-TI_PM-v6.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-TI_PM-v6.2"
        },
    ],
    lookup_label="JBA_Area-TI",
    name="Area TI (STG)",
)
ParcellationEntity.jba__area_tpj = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Area-TPJ",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporo-parietalJunction"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Area-TPJ_PM-v6.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Area-TPJ_PM-v6.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Area-TPJ_PM-v6.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Area-TPJ_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Area-TPJ_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Area-TPJ_PM-v6.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Area-TPJ_PM-v6.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Area-TPJ_PM-v6.2"
        },
    ],
    lookup_label="JBA_Area-TPJ",
    name="Area TPJ (STG/SMG)",
)
ParcellationEntity.jba__ch_123 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Ch-123",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_magnocellularGroup"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Ch-123_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Ch-123_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Ch-123_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Ch-123_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Ch-123_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Ch-123_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Ch-123_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Ch-123_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Ch-123_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Ch-123_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Ch-123_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Ch-123_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Ch-123_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Ch-123_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Ch-123_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Ch-123_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Ch-123_PM-v4.3"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Ch-123_PM-v4.3"
        },
    ],
    lookup_label="JBA_Ch-123",
    name="Ch 123 (Basal Forebrain)",
)
ParcellationEntity.jba__ch_4 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Ch-4",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_sublenticularBasalForebrain"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Ch-4_PM-v4.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Ch-4_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Ch-4_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Ch-4_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Ch-4_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Ch-4_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Ch-4_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Ch-4_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Ch-4_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Ch-4_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Ch-4_PM-v4.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Ch-4_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Ch-4_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Ch-4_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Ch-4_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Ch-4_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Ch-4_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Ch-4_PM-v4.3"},
    ],
    lookup_label="JBA_Ch-4",
    name="Ch 4 (Basal Forebrain)",
)
ParcellationEntity.jba__dorsal__dentate__nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Dorsal-Dentate-Nucleus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dentateNucleus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Dorsal-Dentate-Nucleus_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Dorsal-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Dorsal-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Dorsal-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Dorsal-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Dorsal-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Dorsal-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Dorsal-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Dorsal-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Dorsal-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Dorsal-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Dorsal-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Dorsal-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Dorsal-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Dorsal-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Dorsal-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Dorsal-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Dorsal-Dentate-Nucleus_PM-v6.3"
        },
    ],
    lookup_label="JBA_Dorsal-Dentate-Nucleus",
    name="Dorsal Dentate Nucleus (Cerebellum)",
)
ParcellationEntity.jba__entorhinal__cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Entorhinal-Cortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_hippocampalFormation"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Entorhinal-Cortex_PM-v11b.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Entorhinal-Cortex_PM-v11.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Entorhinal-Cortex_PM-v11.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Entorhinal-Cortex_PM-v11.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Entorhinal-Cortex_PM-v11.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Entorhinal-Cortex_PM-v11.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Entorhinal-Cortex_PM-v11.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Entorhinal-Cortex_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Entorhinal-Cortex_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Entorhinal-Cortex_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Entorhinal-Cortex_int"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Entorhinal-Cortex_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Entorhinal-Cortex_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Entorhinal-Cortex_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Entorhinal-Cortex_int"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Entorhinal-Cortex_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Entorhinal-Cortex_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Entorhinal-Cortex_PM-v13.2"
        },
    ],
    lookup_label="JBA_Entorhinal-Cortex",
    name="Entorhinal Cortex",
)
ParcellationEntity.jba__fastigial__nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Fastigial-Nucleus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebellarNuclei"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Fastigial-Nucleus_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Fastigial-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Fastigial-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Fastigial-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Fastigial-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Fastigial-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Fastigial-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Fastigial-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Fastigial-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Fastigial-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Fastigial-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Fastigial-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Fastigial-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Fastigial-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Fastigial-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Fastigial-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Fastigial-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Fastigial-Nucleus_PM-v6.3"
        },
    ],
    lookup_label="JBA_Fastigial-Nucleus",
    name="Fastigial Nucleus (Cerebellum)",
)
ParcellationEntity.jba__frontal_i = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-I",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Frontal-I_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Frontal-I_PM-v9.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Frontal-I_PM-v9.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Frontal-I_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Frontal-I_PM-v10.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Frontal-I_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Frontal-I_PM-v10.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Frontal-I_PM-v11.3"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Frontal-I_PM-v11.3"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Frontal-I_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Frontal-I_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Frontal-I_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Frontal-I_PM-v11.4"
        },
    ],
    lookup_label="JBA_Frontal-I",
    name="Frontal-I (GapMap)",
)
ParcellationEntity.jba__frontal_ii = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-II",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Frontal-II_PM-v9.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Frontal-II_PM-v9.0"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Frontal-II_PM-v9.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Frontal-II_PM-v9.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Frontal-II_PM-v10.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Frontal-II_PM-v10.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Frontal-II_PM-v10.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Frontal-II_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Frontal-II_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Frontal-II_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Frontal-II_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Frontal-II_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Frontal-II_PM-v11.4"
        },
    ],
    lookup_label="JBA_Frontal-II",
    name="Frontal-II (GapMap)",
)
ParcellationEntity.jba__frontal_to__occipital = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-to-Occipital",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Frontal-to-Occipital_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Frontal-to-Occipital_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Frontal-to-Occipital_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Frontal-to-Occipital_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Frontal-to-Occipital_PM-v10.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Frontal-to-Occipital_PM-v10.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Frontal-to-Occipital_PM-v10.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Frontal-to-Occipital_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Frontal-to-Occipital_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Frontal-to-Occipital_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Frontal-to-Occipital_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Frontal-to-Occipital_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Frontal-to-Occipital_PM-v11.4"
        },
    ],
    lookup_label="JBA_Frontal-to-Occipital",
    name="Frontal-to-Occipital (GapMap",
)
ParcellationEntity.jba__frontal_to__temporal = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-to-Temporal",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Frontal-to-Temporal_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Frontal-to-Temporal_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Frontal-to-Temporal_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Frontal-to-Temporal_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Frontal-to-Temporal_PM-v10.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Frontal-to-Temporal_PM-v10.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Frontal-to-Temporal_PM-v10.0"
        },
    ],
    lookup_label="JBA_Frontal-to-Temporal",
    name="Frontal-to-Temporal (GapMap)",
)
ParcellationEntity.jba__frontal_to__temporal_i = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-to-Temporal-I",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-to-Temporal"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Frontal-to-Temporal-I_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Frontal-to-Temporal-I_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Frontal-to-Temporal-I_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Frontal-to-Temporal-I_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Frontal-to-Temporal-I_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Frontal-to-Temporal-I_PM-v11.4"
        },
    ],
    lookup_label="JBA_Frontal-to-Temporal-I",
    name="Frontal-to-Temporal-I (GapMap)",
)
ParcellationEntity.jba__frontal_to__temporal_ii = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-to-Temporal-II",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Frontal-to-Temporal"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Frontal-to-Temporal-II_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Frontal-to-Temporal-II_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Frontal-to-Temporal-II_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Frontal-to-Temporal-II_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Frontal-to-Temporal-II_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Frontal-to-Temporal-II_PM-v11.4"
        },
    ],
    lookup_label="JBA_Frontal-to-Temporal-II",
    name="Frontal-to-Temporal-II (GapMap)",
)
ParcellationEntity.jba__fu_cd = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_FuCd",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_ventralStriatum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_FuCd_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_FuCd_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_FuCd_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_FuCd_PM-v5.0"},
    ],
    lookup_label="JBA_FuCd",
    name="FuCd (Fundus of Caudate Nucleus, Ventral Striatum)",
)
ParcellationEntity.jba__fu_p = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_FuP",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_ventralStriatum"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_FuP_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_FuP_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_FuP_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_FuP_PM-v5.0"},
    ],
    lookup_label="JBA_FuP",
    name="FuP (Fundus of Putamen, Ventral Striatum)",
)
ParcellationEntity.jba__heschls_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_HeschlsGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalLobe"}],
    lookup_label="JBA_HeschlsGyrus",
    name="Heschl’s gyrus",
)
ParcellationEntity.jba__interposed__nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Interposed-Nucleus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebellarNuclei"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Interposed-Nucleus_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Interposed-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Interposed-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Interposed-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Interposed-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Interposed-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Interposed-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Interposed-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Interposed-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Interposed-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Interposed-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Interposed-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Interposed-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Interposed-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Interposed-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Interposed-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Interposed-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Interposed-Nucleus_PM-v6.3"
        },
    ],
    lookup_label="JBA_Interposed-Nucleus",
    name="Interposed Nucleus (Cerebellum)",
)
ParcellationEntity.jba__subiculum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_hippocampalFormation"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Subiculum_PM-v11b.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Subiculum_PM-v11.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Subiculum_PM-v11.1"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Subiculum_PM-v11.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Subiculum_PM-v11.1"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Subiculum_PM-v11.1"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Subiculum_PM-v11.1"},
    ],
    lookup_label="JBA_Subiculum",
    name="Subiculum (Hippocampus)",
)
ParcellationEntity.jba__subiculum__pa_s = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum.PaS",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Subiculum.PaS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Subiculum.PaS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Subiculum.PaS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Subiculum.PaS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Subiculum.PaS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Subiculum.PaS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Subiculum.PaS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Subiculum.PaS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Subiculum.PaS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Subiculum.PaS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Subiculum.PaS_PM-v13.2"
        },
    ],
    lookup_label="JBA_Subiculum.PaS",
    name="Subiculum.PaS (Hippocampus)",
)
ParcellationEntity.jba__subiculum__pre_s = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum.PreS",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Subiculum.PreS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Subiculum.PreS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Subiculum.PreS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Subiculum.PreS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Subiculum.PreS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Subiculum.PreS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Subiculum.PreS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Subiculum.PreS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Subiculum.PreS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Subiculum.PreS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Subiculum.PreS_PM-v13.2"
        },
    ],
    lookup_label="JBA_Subiculum.PreS",
    name="Subiculum.PreS (Hippocampus)",
)
ParcellationEntity.jba__subiculum__pro_s = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum.ProS",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Subiculum.ProS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Subiculum.ProS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Subiculum.ProS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Subiculum.ProS_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Subiculum.ProS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Subiculum.ProS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Subiculum.ProS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Subiculum.ProS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Subiculum.ProS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Subiculum.ProS_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Subiculum.ProS_PM-v13.2"
        },
    ],
    lookup_label="JBA_Subiculum.ProS",
    name="Subiculum.ProS (Hippocampus)",
)
ParcellationEntity.jba__subiculum__sub = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum.Sub",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Subiculum"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Subiculum.Sub_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Subiculum.Sub_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Subiculum.Sub_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Subiculum.Sub_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Subiculum.Sub_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Subiculum.Sub_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Subiculum.Sub_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Subiculum.Sub_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Subiculum.Sub_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Subiculum.Sub_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Subiculum.Sub_PM-v13.2"
        },
    ],
    lookup_label="JBA_Subiculum.Sub",
    name="Subiculum.Sub (Hippocampus)",
)
ParcellationEntity.jba__temporal_to__parietal = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Temporal-to-Parietal",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Temporal-to-Parietal_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Temporal-to-Parietal_PM-v9.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Temporal-to-Parietal_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Temporal-to-Parietal_PM-v9.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Temporal-to-Parietal_PM-v10.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Temporal-to-Parietal_PM-v10.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Temporal-to-Parietal_PM-v10.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Temporal-to-Parietal_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Temporal-to-Parietal_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Temporal-to-Parietal_PM-v11.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Temporal-to-Parietal_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Temporal-to-Parietal_PM-v11.4"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Temporal-to-Parietal_PM-v11.4"
        },
    ],
    lookup_label="JBA_Temporal-to-Parietal",
    name="Temporal-to-Parietal (GapMap)",
)
ParcellationEntity.jba__terminal_islands = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Terminal-islands",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_olfactoryCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Terminal-islands_PM-v4.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Terminal-islands_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Terminal-islands_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Terminal-islands_PM-v4.0"
        },
    ],
    lookup_label="JBA_Terminal-islands",
    name="Terminal islands (Basal Forebrain)",
)
ParcellationEntity.jba__tuberculum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Tuberculum",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_olfactoryCortex"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Tuberculum_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Tuberculum_PM-v4.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Tuberculum_PM-v4.0"
        },
    ],
    lookup_label="JBA_Tuberculum",
    name="Tuberculum (Basal Forebrain)",
)
ParcellationEntity.jba__ventral__dentate__nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_Ventral-Dentate-Nucleus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dentateNucleus"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_Ventral-Dentate-Nucleus_PM-v6.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_Ventral-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_Ventral-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_Ventral-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_Ventral-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_Ventral-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_Ventral-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_Ventral-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_Ventral-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_Ventral-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_Ventral-Dentate-Nucleus_PM-v6.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_Ventral-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_Ventral-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_Ventral-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_Ventral-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_Ventral-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_Ventral-Dentate-Nucleus_PM-v6.3"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_Ventral-Dentate-Nucleus_PM-v6.3"
        },
    ],
    lookup_label="JBA_Ventral-Dentate-Nucleus",
    name="Ventral Dentate Nucleus (Cerebellum)",
)
ParcellationEntity.jba_agranular_insula = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_agranularInsula",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_insula"}],
    lookup_label="JBA_agranularInsula",
    name="agranular insula",
)
ParcellationEntity.jba_amygdala = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_amygdala",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralNuclei"}],
    lookup_label="JBA_amygdala",
    name="amygdala",
)
ParcellationEntity.jba_amygdaloid_groups = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_amygdaloidGroups",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_amygdala"}],
    lookup_label="JBA_amygdaloidGroups",
    name="amygdaloid groups",
)
ParcellationEntity.jba_basal_forebrain = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_basalForebrain",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralNuclei"}],
    lookup_label="JBA_basalForebrain",
    name="basal forebrain",
)
ParcellationEntity.jba_basal_ganglia = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_basalGanglia",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralNuclei"}],
    lookup_label="JBA_basalGanglia",
    name="basal ganglia",
)
ParcellationEntity.jba_brain = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_brain",
    lookup_label="JBA_brain",
    name="brain",
)
ParcellationEntity.jba_bst = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_BST",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_basalForebrain"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_BST_PM-v20.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_BST_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_BST_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_BST_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_BST_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_BST_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_BST_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_BST_PM-v6.1"},
    ],
    lookup_label="JBA_BST",
    name="BST (Bed Nucleus)",
)
ParcellationEntity.jba_ca = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CA",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_hippocampalFormation"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_CA_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_CA_PM-v11.1"},
    ],
    lookup_label="JBA_CA",
    name="CA (Hippocampus)",
)
ParcellationEntity.jba_ca1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CA1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_hippocampalFormation"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_CA1_PM-v11b.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_CA1_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_CA1_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_CA1_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_CA1_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_CA1_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_CA1_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_CA1_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_CA1_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_CA1_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_CA1_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_CA1_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_CA1_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_CA1_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_CA1_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_CA1_PM-v13.2"},
    ],
    lookup_label="JBA_CA1",
    name="CA1 (Hippocampus)",
)
ParcellationEntity.jba_ca2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CA2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_hippocampalFormation"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_CA2_PM-v11b.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_CA2_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_CA2_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_CA2_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_CA2_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_CA2_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_CA2_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_CA2_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_CA2_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_CA2_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_CA2_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_CA2_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_CA2_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_CA2_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_CA2_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_CA2_PM-v13.2"},
    ],
    lookup_label="JBA_CA2",
    name="CA2 (Hippocampus)",
)
ParcellationEntity.jba_ca3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CA3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_hippocampalFormation"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_CA3_PM-v11b.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_CA3_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_CA3_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_CA3_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_CA3_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_CA3_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_CA3_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_CA3_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_CA3_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_CA3_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_CA3_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_CA3_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_CA3_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_CA3_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_CA3_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_CA3_PM-v13.2"},
    ],
    lookup_label="JBA_CA3",
    name="CA3 (Hippocampus)",
)
ParcellationEntity.jba_cerebellar_nuclei = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebellarNuclei",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebellum"}],
    lookup_label="JBA_cerebellarNuclei",
    name="cerebellar nuclei",
)
ParcellationEntity.jba_cerebellum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebellum",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_metencephalon"}],
    lookup_label="JBA_cerebellum",
    name="cerebellum",
)
ParcellationEntity.jba_cerebral_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_telencephalon"}],
    lookup_label="JBA_cerebralCortex",
    name="cerebral cortex",
)
ParcellationEntity.jba_cerebral_nuclei = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralNuclei",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_telencephalon"}],
    lookup_label="JBA_cerebralNuclei",
    name="cerebral nuclei",
)
ParcellationEntity.jba_cgl = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_metathalamus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_CGL_PM-v12.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_CGL_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_CGL_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_CGL_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_CGL_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_CGL_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_CGL_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_CGL_PM-v10.0"},
    ],
    lookup_label="JBA_CGL",
    name="CGL (Metathalamus)",
)
ParcellationEntity.jba_cgl_lam1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL"}],
    lookup_label="JBA_CGL.lam1",
    name="CGL.lam1 (Metathalamus)",
)
ParcellationEntity.jba_cgl_lam2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL"}],
    lookup_label="JBA_CGL.lam2",
    name="CGL.lam2 (Metathalamus)",
)
ParcellationEntity.jba_cgl_lam3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL"}],
    lookup_label="JBA_CGL.lam3",
    name="CGL.lam3 (Metathalamus)",
)
ParcellationEntity.jba_cgl_lam4 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam4",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL"}],
    lookup_label="JBA_CGL.lam4",
    name="CGL.lam4 (Metathalamus)",
)
ParcellationEntity.jba_cgl_lam5 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam5",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL"}],
    lookup_label="JBA_CGL.lam5",
    name="CGL.lam5 (Metathalamus)",
)
ParcellationEntity.jba_cgl_lam6 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL.lam6",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGL"}],
    lookup_label="JBA_CGL.lam6",
    name="CGL.lam6 (Metathalamus)",
)
ParcellationEntity.jba_cgm = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGM",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_metathalamus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_CGM_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_CGM_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_CGM_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_CGM_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_CGM_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_CGM_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_CGM_PM-v10.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_CGM_PM-v10.0"},
    ],
    lookup_label="JBA_CGM",
    name="CGM (Metathalamus)",
)
ParcellationEntity.jba_cgm_cg_md = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGM.CGMd",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGM"}],
    lookup_label="JBA_CGM.CGMd",
    name="CGM.CGMd (Metathalamus)",
)
ParcellationEntity.jba_cgm_cg_mm = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGM.CGMm",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGM"}],
    lookup_label="JBA_CGM.CGMm",
    name="CGM.CGMm (Metathalamus)",
)
ParcellationEntity.jba_cgm_cg_mv = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGM.CGMv",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CGM"}],
    lookup_label="JBA_CGM.CGMv",
    name="CGM.CGMv (Metathalamus)",
)
ParcellationEntity.jba_cingulate_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cingulateGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_limbicLobe"}],
    lookup_label="JBA_cingulateGyrus",
    name="cingulate gyrus",
)
ParcellationEntity.jba_cm = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CM",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_amygdaloidGroups"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_CM_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_CM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_CM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_CM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_CM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_CM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_CM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_CM_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_CM_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_CM_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_CM_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_CM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_CM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_CM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_CM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_CM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_CM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_CM_PM-v8.2"},
    ],
    lookup_label="JBA_CM",
    name="CM (Amygdala)",
)
ParcellationEntity.jba_cm__ce = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CM.Ce",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CM"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_CM.Ce_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_CM.Ce_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_CM.Ce_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_CM.Ce_PM-v8.2"},
    ],
    lookup_label="JBA_CM.Ce",
    name="CM.Ce (Amygdala)",
)
ParcellationEntity.jba_cm__me = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CM.Me",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CM"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_CM.Me_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_CM.Me_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_CM.Me_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_CM.Me_PM-v8.2"},
    ],
    lookup_label="JBA_CM.Me",
    name="CM.Me (Amygdala)",
)
ParcellationEntity.jba_cm_aaa = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CM.AAA",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_CM"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_CM.AAA_PM-v11.4"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_CM.AAA_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_CM.AAA_PM-v8.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_CM.AAA_PM-v8.2"
        },
    ],
    lookup_label="JBA_CM.AAA",
    name="CM.AAA (Amygdala)",
)
ParcellationEntity.jba_collateral_sulcus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_collateralSulcus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalLobe"}],
    lookup_label="JBA_collateralSulcus",
    name="collateral sulcus",
)
ParcellationEntity.jba_dentate_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dentateNucleus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebellarNuclei"}],
    lookup_label="JBA_dentateNucleus",
    name="dentate nucleus",
)
ParcellationEntity.jba_dg = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_DG",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_hippocampalFormation"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_DG_PM-v11b.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_DG_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_DG_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_DG_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_DG_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_DG_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_DG_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_DG_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_DG_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_DG_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_DG_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_DG_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_DG_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_DG_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_DG_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_DG_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_DG_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_DG_PM-v13.2"},
    ],
    lookup_label="JBA_DG",
    name="DG (Hippocampus)",
)
ParcellationEntity.jba_diencephalon = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_diencephalon",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_brain"}],
    lookup_label="JBA_diencephalon",
    name="diencephalon",
)
ParcellationEntity.jba_dorsal_occipital_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dorsalOccipitalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_occipitalLobe"}],
    lookup_label="JBA_dorsalOccipitalCortex",
    name="dorsal occipital cortex",
)
ParcellationEntity.jba_dorsal_precentral_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dorsalPrecentralGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_dorsalPrecentralGyrus",
    name="dorsal precentral gyrus",
)
ParcellationEntity.jba_dysgranular_insula = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_dysgranularInsula",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_insula"}],
    lookup_label="JBA_dysgranularInsula",
    name="dysgranular insula",
)
ParcellationEntity.jba_fiber_masses = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fiberMasses",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_amygdala"}],
    lookup_label="JBA_fiberMasses",
    name="fiber masses",
)
ParcellationEntity.jba_frontal_cingulate_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalCingulateGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cingulateGyrus"}],
    lookup_label="JBA_frontalCingulateGyrus",
    name="frontal cingulate",
)
ParcellationEntity.jba_frontal_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralCortex"}],
    lookup_label="JBA_frontalLobe",
    name="frontal lobe",
)
ParcellationEntity.jba_frontal_operculum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalOperculum",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_frontalOperculum",
    name="frontal operculum",
)
ParcellationEntity.jba_frontal_pole = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalPole",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_frontalPole",
    name="frontal pole",
)
ParcellationEntity.jba_fronto_marginal_sulcus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fronto-marginalSulcus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_fronto-marginalSulcus",
    name="fronto-marginal sulcus",
)
ParcellationEntity.jba_fusiform_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fusiformGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalLobe"}],
    lookup_label="JBA_fusiformGyrus",
    name="fusiform gyrus",
)
ParcellationEntity.jba_granular_insula = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_granularInsula",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_insula"}],
    lookup_label="JBA_granularInsula",
    name="granular insula",
)
ParcellationEntity.jba_hata = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_HATA",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_hippocampalFormation"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_HATA_PM-v11b.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_HATA_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_HATA_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_HATA_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_HATA_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_HATA_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_HATA_PM-v11.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_HATA_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_HATA_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_HATA_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_HATA_PM-v13.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_HATA_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_HATA_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_HATA_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_HATA_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_HATA_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_HATA_PM-v13.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_HATA_PM-v13.2"},
    ],
    lookup_label="JBA_HATA",
    name="HATA (Hippocampus)",
)
ParcellationEntity.jba_hc__transsubiculum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_HC-Transsubiculum",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_hippocampalFormation"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_HC-Transsubiculum_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_HC-Transsubiculum_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_HC-Transsubiculum_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_HC-Transsubiculum_PM-v13.0"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_HC-Transsubiculum_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_HC-Transsubiculum_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_HC-Transsubiculum_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_HC-Transsubiculum_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_HC-Transsubiculum_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_HC-Transsubiculum_PM-v13.2"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_HC-Transsubiculum_PM-v13.2"
        },
    ],
    lookup_label="JBA_HC-Transsubiculum",
    name="HC-Transsubiculum (Hippocampus)",
)
ParcellationEntity.jba_hippocampal_formation = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_hippocampalFormation",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_limbicLobe"}],
    lookup_label="JBA_hippocampalFormation",
    name="hippocampal formation",
)
ParcellationEntity.jba_if = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_IF",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fiberMasses"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_IF_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_IF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_IF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_IF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_IF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_IF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_IF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_IF_PM-v8.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_IF_PM-v8.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_IF_PM-v8.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_IF_PM-v8.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_IF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_IF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_IF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_IF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_IF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_IF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_IF_PM-v8.2"},
    ],
    lookup_label="JBA_IF",
    name="IF (Amygdala)",
)
ParcellationEntity.jba_if_ice = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_IF.ice",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_IF"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_IF.ice_PM-v13.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_IF.ice_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_IF.ice_PM-v8.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_IF.ice_PM-v8.2"
        },
    ],
    lookup_label="JBA_IF.ice",
    name="IF.ice (Amygdala)",
)
ParcellationEntity.jba_if_iol = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_IF.iol",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_IF"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_IF.iol_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_IF.iol_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_IF.iol_PM-v8.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_IF.iol_PM-v8.2"
        },
    ],
    lookup_label="JBA_IF.iol",
    name="IF.iol (Amygdala)",
)
ParcellationEntity.jba_if_ld = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_IF.ld",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_IF"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_IF.ld_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_IF.ld_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_IF.ld_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_IF.ld_PM-v8.2"},
    ],
    lookup_label="JBA_IF.ld",
    name="IF.ld (Amygdala)",
)
ParcellationEntity.jba_inferior_frontal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_inferiorFrontalGyrus",
    name="inferior frontal gyrus",
)
ParcellationEntity.jba_inferior_frontal_sulcus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorFrontalSulcus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_inferiorFrontalSulcus",
    name="inferior frontal sulcus",
)
ParcellationEntity.jba_inferior_parietal_lobule = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_inferiorParietalLobule",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalLobe"}],
    lookup_label="JBA_inferiorParietalLobule",
    name="inferior parietal lobule",
)
ParcellationEntity.jba_insula = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_insula",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralCortex"}],
    lookup_label="JBA_insula",
    name="insula",
)
ParcellationEntity.jba_intraparietal_sulcus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_intraparietalSulcus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalLobe"}],
    lookup_label="JBA_intraparietalSulcus",
    name="intraparietal sulcus",
)
ParcellationEntity.jba_lateral_occipital_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_lateralOccipitalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_occipitalLobe"}],
    lookup_label="JBA_lateralOccipitalCortex",
    name="lateral occipital cortex",
)
ParcellationEntity.jba_lateral_orbitofrontal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_lateralOrbitofrontalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_lateralOrbitofrontalCortex",
    name="lateral orbitofrontal cortex",
)
ParcellationEntity.jba_lb = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_amygdaloidGroups"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_LB_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_LB_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_LB_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_LB_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_LB_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_LB_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_LB_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_LB_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_LB_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_LB_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_LB_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_LB_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_LB_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_LB_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_LB_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_LB_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_LB_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_LB_PM-v8.2"},
    ],
    lookup_label="JBA_LB",
    name="LB (Amygdala)",
)
ParcellationEntity.jba_lb__bl = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB.Bl",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_LB.Bl_PM-v3.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_LB.Bl_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_LB.Bl_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_LB.Bl_PM-v8.2"},
    ],
    lookup_label="JBA_LB.Bl",
    name="LB.Bl (Amygdala)",
)
ParcellationEntity.jba_lb__bm = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB.Bm",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_LB.Bm_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_LB.Bm_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_LB.Bm_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_LB.Bm_PM-v8.2"},
    ],
    lookup_label="JBA_LB.Bm",
    name="LB.Bm (Amygdala)",
)
ParcellationEntity.jba_lb__la = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB.La",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_LB.La_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_LB.La_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_LB.La_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_LB.La_PM-v8.2"},
    ],
    lookup_label="JBA_LB.La",
    name="LB.La (Amygdala)",
)
ParcellationEntity.jba_lb__pl = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB.Pl",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_LB"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_LB.Pl_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_LB.Pl_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_LB.Pl_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_LB.Pl_PM-v8.2"},
    ],
    lookup_label="JBA_LB.Pl",
    name="LB.Pl (Amygdala)",
)
ParcellationEntity.jba_limbic_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_limbicLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralCortex"}],
    lookup_label="JBA_limbicLobe",
    name="limbic lobe",
)
ParcellationEntity.jba_magnocellular_group = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_magnocellularGroup",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_basalForebrain"}],
    lookup_label="JBA_magnocellularGroup",
    name="magnocellular group",
)
ParcellationEntity.jba_medial_orbitofrontal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_medialOrbitofrontalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_medialOrbitofrontalCortex",
    name="medial orbitofrontal cortex",
)
ParcellationEntity.jba_mesial_precentral_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_mesialPrecentralGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_mesialPrecentralGyrus",
    name="mesial precentral gyrus",
)
ParcellationEntity.jba_metathalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_metathalamus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_thalamus"}],
    lookup_label="JBA_metathalamus",
    name="metathalamus",
)
ParcellationEntity.jba_metencephalon = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_metencephalon",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_brain"}],
    lookup_label="JBA_metencephalon",
    name="metencephalon",
)
ParcellationEntity.jba_mf = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_MF",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fiberMasses"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_MF_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_MF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_MF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_MF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_MF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_MF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_MF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_MF_PM-v8.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_MF_PM-v8.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_MF_PM-v8.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_MF_PM-v8.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_MF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_MF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_MF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_MF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_MF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_MF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_MF_PM-v8.2"},
    ],
    lookup_label="JBA_MF",
    name="MF (Amygdala)",
)
ParcellationEntity.jba_mf_icm = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_MF.icm",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_MF"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_MF.icm_PM-v10.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_MF.icm_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_MF.icm_PM-v8.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_MF.icm_PM-v8.2"
        },
    ],
    lookup_label="JBA_MF.icm",
    name="MF.icm (Amygdala)",
)
ParcellationEntity.jba_mf_lm = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_MF.lm",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_MF"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_MF.lm_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_MF.lm_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_MF.lm_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_MF.lm_PM-v8.2"},
    ],
    lookup_label="JBA_MF.lm",
    name="MF.lm (Amygdala)",
)
ParcellationEntity.jba_middle_frontal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_middleFrontalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_middleFrontalGyrus",
    name="middle frontal gyrus",
)
ParcellationEntity.jba_occipital_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_occipitalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_occipitalLobe"}],
    lookup_label="JBA_occipitalCortex",
    name="occipital cortex",
)
ParcellationEntity.jba_occipital_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_occipitalLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralCortex"}],
    lookup_label="JBA_occipitalLobe",
    name="occipital lobe",
)
ParcellationEntity.jba_olfactory_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_olfactoryCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_limbicLobe"}],
    lookup_label="JBA_olfactoryCortex",
    name="olfactory cortex",
)
ParcellationEntity.jba_parahippocampal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parahippocampalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalLobe"}],
    lookup_label="JBA_parahippocampalGyrus",
    name="parahippocampal gyrus",
)
ParcellationEntity.jba_parietal_lobe = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalLobe",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cerebralCortex"}],
    lookup_label="JBA_parietalLobe",
    name="parietal lobe",
)
ParcellationEntity.jba_parietal_operculum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalOperculum",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalLobe"}],
    lookup_label="JBA_parietalOperculum",
    name="parietal operculum",
)
ParcellationEntity.jba_parieto_occipital_sulcus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parieto-occipitalSulcus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalLobe"}],
    lookup_label="JBA_parieto-occipitalSulcus",
    name="parieto-occipital sulcus",
)
ParcellationEntity.jba_postcentral_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_postcentralGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalLobe"}],
    lookup_label="JBA_postcentralGyrus",
    name="postcentral gyrus",
)
ParcellationEntity.jba_posterior_medial_superior_frontal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_posteriorMedialSuperiorFrontalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_posteriorMedialSuperiorFrontalGyrus",
    name="posterior medial superior frontal gyrus",
)
ParcellationEntity.jba_precentral_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_precentralGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_precentralGyrus",
    name="precentral gyrus",
)
ParcellationEntity.jba_retrosplenial_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_retrosplenialPart",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_cingulateGyrus"}],
    lookup_label="JBA_retrosplenialPart",
    name="retrosplenial part",
)
ParcellationEntity.jba_sf = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_SF",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_amygdaloidGroups"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_SF_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_SF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_SF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_SF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_SF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_SF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_SF_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_SF_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_SF_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_SF_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_SF_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_SF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_SF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_SF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_SF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_SF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_SF_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_SF_PM-v8.2"},
    ],
    lookup_label="JBA_SF",
    name="SF (Amygdala)",
)
ParcellationEntity.jba_sf_a_hi = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_SF.AHi",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_SF"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_SF.AHi_PM-v11.0"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_SF.AHi_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_SF.AHi_PM-v8.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_SF.AHi_PM-v8.2"
        },
    ],
    lookup_label="JBA_SF.AHi",
    name="SF.AHi (Amygdala)",
)
ParcellationEntity.jba_sf_a_pir = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_SF.APir",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_SF"}],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_SF.APir_PM-v8.2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_SF.APir_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_SF.APir_PM-v8.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_SF.APir_PM-v8.2"
        },
    ],
    lookup_label="JBA_SF.APir",
    name="SF.APir (Amygdala)",
)
ParcellationEntity.jba_sf_v_co = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_SF.VCo",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_SF"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_SF.VCo_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_SF.VCo_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_SF.VCo_PM-v8.2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_SF.VCo_PM-v8.2"
        },
    ],
    lookup_label="JBA_SF.VCo",
    name="SF.VCo (Amygdala)",
)
ParcellationEntity.jba_stn = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_STN",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_subthalamus"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_STN_PM-v4.3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_STN_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_STN_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_STN_PM-v5.0"},
    ],
    lookup_label="JBA_STN",
    name="STN (Subthalamus)",
)
ParcellationEntity.jba_sublenticular_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_sublenticularPart",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_basalForebrain"}],
    lookup_label="JBA_sublenticularPart",
    name="sublenticular part",
)
ParcellationEntity.jba_subthalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_subthalamus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_diencephalon"}],
    lookup_label="JBA_subthalamus",
    name="subthalamus",
)
ParcellationEntity.jba_superior_frontal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorFrontalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_superiorFrontalGyrus",
    name="superior frontal gyrus",
)
ParcellationEntity.jba_superior_frontal_sulcus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorFrontalSulcus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_frontalLobe"}],
    lookup_label="JBA_superiorFrontalSulcus",
    name="superior frontal sulcus",
)
ParcellationEntity.jba_superior_parietal_lobule = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorParietalLobule",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_parietalLobe"}],
    lookup_label="JBA_superiorParietalLobule",
    name="superior parietal lobule",
)
ParcellationEntity.jba_superior_temporal_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorTemporalGyrus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalLobe"}],
    lookup_label="JBA_superiorTemporalGyrus",
    name="superior temporal gyrus",
)
ParcellationEntity.jba_superior_temporal_sulcus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_superiorTemporalSulcus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalLobe"}],
    lookup_label="JBA_superiorTemporalSulcus",
    name="superior temporal sulcus",
)
ParcellationEntity.jba_telencephalon = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_telencephalon",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_brain"}],
    lookup_label="JBA_telencephalon",
    name="telencephalon",
)
ParcellationEntity.jba_temporal_insula = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalInsula",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalLobe"}],
    lookup_label="JBA_temporalInsula",
    name="temporal insula",
)
ParcellationEntity.jba_temporo_parietal_junction = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporo-parietalJunction",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_temporalLobe"}],
    lookup_label="JBA_temporo-parietalJunction",
    name="temporo-parietal junction",
)
ParcellationEntity.jba_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_thalamus",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_diencephalon"}],
    lookup_label="JBA_thalamus",
    name="thalamus",
)
ParcellationEntity.jba_ventral_occipital_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_ventralOccipitalCortex",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_occipitalLobe"}],
    lookup_label="JBA_ventralOccipitalCortex",
    name="ventral occipital cortex",
)
ParcellationEntity.jba_ventral_striatum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_ventralStriatum",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_basalGanglia"}],
    lookup_label="JBA_ventralStriatum",
    name="ventral striatum",
)
ParcellationEntity.jba_vp = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_VP",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_basalGanglia"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_VP_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_VP_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_VP_PM-v5.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_VP_PM-v5.0"},
    ],
    lookup_label="JBA_VP",
    name="VP (Ventral Pallidum)",
)
ParcellationEntity.jba_vtm = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/JBA_VTM",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/JBA_fiberMasses"}],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.13-Colin27_VTM_PM-v6.1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-Colin27_VTM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v1.18-MNI152_VTM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-Colin27_VTM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.2-MNI152_VTM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-Colin27_VTM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.4-MNI152_VTM_PM-v6.4"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-Colin27_VTM_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.5-MNI152_VTM_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.6-MNI152_VTM_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-BigBrain_VTM_PM-v8.0"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-Colin27_VTM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-MNI152_VTM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v2.9-fsaverage_VTM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-BigBrain_VTM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-Colin27_VTM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-MNI152_VTM_PM-v8.2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/JBA_v3.0.2-fsaverage_VTM_PM-v8.2"},
    ],
    lookup_label="JBA_VTM",
    name="VTM (Amygdala)",
)
ParcellationEntity.swma__cu__li_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Cu-Li_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_Cu-Li_0"}],
    lookup_label="SWMA_Cu-Li_0",
    name="Cu-Li_0",
)
ParcellationEntity.swma__fu_lo_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Fu-LO_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_Fu-LO_0"}],
    lookup_label="SWMA_Fu-LO_0",
    name="Fu-LO_0",
)
ParcellationEntity.swma__fu_lo_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Fu-LO_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_Fu-LO_1"}],
    lookup_label="SWMA_Fu-LO_1",
    name="Fu-LO_1",
)
ParcellationEntity.swma__op__ins_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Op-Ins_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_Op-Ins_0"}],
    lookup_label="SWMA_Op-Ins_0",
    name="Op-Ins_0",
)
ParcellationEntity.swma__op__pr_c_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Op-PrC_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_Op-PrC_0"}],
    lookup_label="SWMA_Op-PrC_0",
    name="Op-PrC_0",
)
ParcellationEntity.swma__op__tr_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Op-Tr_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_Op-Tr_0"}],
    lookup_label="SWMA_Op-Tr_0",
    name="Op-Tr_0",
)
ParcellationEntity.swma__op_sf_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Op-SF_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_Op-SF_0"}],
    lookup_label="SWMA_Op-SF_0",
    name="Op-SF_0",
)
ParcellationEntity.swma__or__ins_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Or-Ins_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_Or-Ins_0"}],
    lookup_label="SWMA_Or-Ins_0",
    name="Or-Ins_0",
)
ParcellationEntity.swma__po_c__ins_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-Ins_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoC-Ins_0"}],
    lookup_label="SWMA_PoC-Ins_0",
    name="PoC-Ins_0",
)
ParcellationEntity.swma__po_c__pr_c_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-PrC_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoC-PrC_0"}],
    lookup_label="SWMA_PoC-PrC_0",
    name="PoC-PrC_0",
)
ParcellationEntity.swma__po_c__pr_c_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-PrC_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoC-PrC_1"}],
    lookup_label="SWMA_PoC-PrC_1",
    name="PoC-PrC_1",
)
ParcellationEntity.swma__po_c__pr_c_2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-PrC_2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoC-PrC_2"}],
    lookup_label="SWMA_PoC-PrC_2",
    name="PoC-PrC_2",
)
ParcellationEntity.swma__po_c__pr_c_3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-PrC_3",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoC-PrC_3"}],
    lookup_label="SWMA_PoC-PrC_3",
    name="PoC-PrC_3",
)
ParcellationEntity.swma__po_c_sm_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-SM_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoC-SM_0"}],
    lookup_label="SWMA_PoC-SM_0",
    name="PoC-SM_0",
)
ParcellationEntity.swma__po_c_sm_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-SM_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoC-SM_1"}],
    lookup_label="SWMA_PoC-SM_1",
    name="PoC-SM_1",
)
ParcellationEntity.swma__po_c_sp_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-SP_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoC-SP_0"}],
    lookup_label="SWMA_PoC-SP_0",
    name="PoC-SP_0",
)
ParcellationEntity.swma__po_c_sp_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoC-SP_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoC-SP_1"}],
    lookup_label="SWMA_PoC-SP_1",
    name="PoC-SP_1",
)
ParcellationEntity.swma__po_ci__pr_cu_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoCi-PrCu_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoCi-PrCu_0"}],
    lookup_label="SWMA_PoCi-PrCu_0",
    name="PoCi-PrCu_0",
)
ParcellationEntity.swma__po_ci__pr_cu_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoCi-PrCu_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoCi-PrCu_1"}],
    lookup_label="SWMA_PoCi-PrCu_1",
    name="PoCi-PrCu_1",
)
ParcellationEntity.swma__po_ci__pr_cu_2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoCi-PrCu_2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoCi-PrCu_2"}],
    lookup_label="SWMA_PoCi-PrCu_2",
    name="PoCi-PrCu_2",
)
ParcellationEntity.swma__po_ci_rac_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoCi-RAC_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoCi-RAC_0"}],
    lookup_label="SWMA_PoCi-RAC_0",
    name="PoCi-RAC_0",
)
ParcellationEntity.swma__po_ci_sf_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PoCi-SF_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PoCi-SF_0"}],
    lookup_label="SWMA_PoCi-SF_0",
    name="PoCi-SF_0",
)
ParcellationEntity.swma__pr_c__ins_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PrC-Ins_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PrC-Ins_0"}],
    lookup_label="SWMA_PrC-Ins_0",
    name="PrC-Ins_0",
)
ParcellationEntity.swma__pr_c_sf_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PrC-SF_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PrC-SF_0"}],
    lookup_label="SWMA_PrC-SF_0",
    name="PrC-SF_0",
)
ParcellationEntity.swma__pr_c_sm_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PrC-SM_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PrC-SM_0"}],
    lookup_label="SWMA_PrC-SM_0",
    name="PrC-SM_0",
)
ParcellationEntity.swma__pr_c_sp_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_PrC-SP_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_PrC-SP_0"}],
    lookup_label="SWMA_PrC-SP_0",
    name="PrC-SP_0",
)
ParcellationEntity.swma__tr__ins_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Tr-Ins_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_Tr-Ins_0"}],
    lookup_label="SWMA_Tr-Ins_0",
    name="Tr-Ins_0",
)
ParcellationEntity.swma__tr_sf_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_Tr-SF_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_Tr-SF_0"}],
    lookup_label="SWMA_Tr-SF_0",
    name="Tr-SF_0",
)
ParcellationEntity.swma_cac__po_ci_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CAC-PoCi_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_CAC-PoCi_0"}],
    lookup_label="SWMA_CAC-PoCi_0",
    name="CAC-PoCi_0",
)
ParcellationEntity.swma_cac__pr_cu_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CAC-PrCu_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_CAC-PrCu_0"}],
    lookup_label="SWMA_CAC-PrCu_0",
    name="CAC-PrCu_0",
)
ParcellationEntity.swma_cmf__op_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-Op_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_CMF-Op_0"}],
    lookup_label="SWMA_CMF-Op_0",
    name="CMF-Op_0",
)
ParcellationEntity.swma_cmf__po_c_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-PoC_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_CMF-PoC_0"}],
    lookup_label="SWMA_CMF-PoC_0",
    name="CMF-PoC_0",
)
ParcellationEntity.swma_cmf__pr_c_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-PrC_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_CMF-PrC_0"}],
    lookup_label="SWMA_CMF-PrC_0",
    name="CMF-PrC_0",
)
ParcellationEntity.swma_cmf__pr_c_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-PrC_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_CMF-PrC_1"}],
    lookup_label="SWMA_CMF-PrC_1",
    name="CMF-PrC_1",
)
ParcellationEntity.swma_cmf_rmf_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-RMF_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_CMF-RMF_0"}],
    lookup_label="SWMA_CMF-RMF_0",
    name="CMF-RMF_0",
)
ParcellationEntity.swma_cmf_sf_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-SF_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_CMF-SF_0"}],
    lookup_label="SWMA_CMF-SF_0",
    name="CMF-SF_0",
)
ParcellationEntity.swma_cmf_sf_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_CMF-SF_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_CMF-SF_1"}],
    lookup_label="SWMA_CMF-SF_1",
    name="CMF-SF_1",
)
ParcellationEntity.swma_ic__pr_cu_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IC-PrCu_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_IC-PrCu_0"}],
    lookup_label="SWMA_IC-PrCu_0",
    name="IC-PrCu_0",
)
ParcellationEntity.swma_ip_it_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-IT_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_IP-IT_0"}],
    lookup_label="SWMA_IP-IT_0",
    name="IP-IT_0",
)
ParcellationEntity.swma_ip_lo_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-LO_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_IP-LO_0"}],
    lookup_label="SWMA_IP-LO_0",
    name="IP-LO_0",
)
ParcellationEntity.swma_ip_lo_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-LO_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_IP-LO_1"}],
    lookup_label="SWMA_IP-LO_1",
    name="IP-LO_1",
)
ParcellationEntity.swma_ip_mt_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-MT_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_IP-MT_0"}],
    lookup_label="SWMA_IP-MT_0",
    name="IP-MT_0",
)
ParcellationEntity.swma_ip_sm_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-SM_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_IP-SM_0"}],
    lookup_label="SWMA_IP-SM_0",
    name="IP-SM_0",
)
ParcellationEntity.swma_ip_sp_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-SP_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_IP-SP_0"}],
    lookup_label="SWMA_IP-SP_0",
    name="IP-SP_0",
)
ParcellationEntity.swma_ip_sp_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IP-SP_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_IP-SP_1"}],
    lookup_label="SWMA_IP-SP_1",
    name="IP-SP_1",
)
ParcellationEntity.swma_it_mt_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IT-MT_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_IT-MT_0"}],
    lookup_label="SWMA_IT-MT_0",
    name="IT-MT_0",
)
ParcellationEntity.swma_it_mt_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IT-MT_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_IT-MT_1"}],
    lookup_label="SWMA_IT-MT_1",
    name="IT-MT_1",
)
ParcellationEntity.swma_it_mt_2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_IT-MT_2",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_IT-MT_2"}],
    lookup_label="SWMA_IT-MT_2",
    name="IT-MT_2",
)
ParcellationEntity.swma_lo_sp_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LO-SP_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_LO-SP_0"}],
    lookup_label="SWMA_LO-SP_0",
    name="LO-SP_0",
)
ParcellationEntity.swma_lof__or_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LOF-Or_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_LOF-Or_0"}],
    lookup_label="SWMA_LOF-Or_0",
    name="LOF-Or_0",
)
ParcellationEntity.swma_lof_mof_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LOF-MOF_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_LOF-MOF_0"}],
    lookup_label="SWMA_LOF-MOF_0",
    name="LOF-MOF_0",
)
ParcellationEntity.swma_lof_rmf_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LOF-RMF_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_LOF-RMF_0"}],
    lookup_label="SWMA_LOF-RMF_0",
    name="LOF-RMF_0",
)
ParcellationEntity.swma_lof_rmf_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LOF-RMF_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_LOF-RMF_1"}],
    lookup_label="SWMA_LOF-RMF_1",
    name="LOF-RMF_1",
)
ParcellationEntity.swma_lof_st_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_LOF-ST_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_LOF-ST_0"}],
    lookup_label="SWMA_LOF-ST_0",
    name="LOF-ST_0",
)
ParcellationEntity.swma_mof_st_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_MOF-ST_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_MOF-ST_0"}],
    lookup_label="SWMA_MOF-ST_0",
    name="MOF-ST_0",
)
ParcellationEntity.swma_mt_sm_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_MT-SM_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_MT-SM_0"}],
    lookup_label="SWMA_MT-SM_0",
    name="MT-SM_0",
)
ParcellationEntity.swma_mt_st_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_MT-ST_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_MT-ST_0"}],
    lookup_label="SWMA_MT-ST_0",
    name="MT-ST_0",
)
ParcellationEntity.swma_rac_sf_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_RAC-SF_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_RAC-SF_0"}],
    lookup_label="SWMA_RAC-SF_0",
    name="RAC-SF_0",
)
ParcellationEntity.swma_rac_sf_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_RAC-SF_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_RAC-SF_1"}],
    lookup_label="SWMA_RAC-SF_1",
    name="RAC-SF_1",
)
ParcellationEntity.swma_rmf_sf_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_RMF-SF_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_RMF-SF_0"}],
    lookup_label="SWMA_RMF-SF_0",
    name="RMF-SF_0",
)
ParcellationEntity.swma_rmf_sf_1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_RMF-SF_1",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_RMF-SF_1"}],
    lookup_label="SWMA_RMF-SF_1",
    name="RMF-SF_1",
)
ParcellationEntity.swma_sm__ins_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_SM-Ins_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_SM-Ins_0"}],
    lookup_label="SWMA_SM-Ins_0",
    name="SM-Ins_0",
)
ParcellationEntity.swma_sp_sm_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_SP-SM_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_SP-SM_0"}],
    lookup_label="SWMA_SP-SM_0",
    name="SP-SM_0",
)
ParcellationEntity.swma_st__ins_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_ST-Ins_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_ST-Ins_0"}],
    lookup_label="SWMA_ST-Ins_0",
    name="ST-Ins_0",
)
ParcellationEntity.swma_st_tt_0 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_ST-TT_0",
    has_parents=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntity/SWMA_superficialWhiteMatter"}],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_2018_ST-TT_0"}],
    lookup_label="SWMA_ST-TT_0",
    name="ST-TT_0",
)
ParcellationEntity.swma_superficial_white_matter = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntityVersion/SWMA_superficialWhiteMatter",
    abbreviation="SWM",
    lookup_label="SWMA_superficialWhiteMatter",
    name="superficial white matter",
)
ParcellationEntity.whss_datlas_4th_ventricle = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_4thVentricle",
    alternate_names=["4V"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_4thVentricle"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_4thVentricle"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_4thVentricle"},
    ],
    lookup_label="WHSSDatlas_4thVentricle",
    name="4th ventricle",
)
ParcellationEntity.whss_datlas_acoustic_striae = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_acousticStriae",
    alternate_names=["as"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_acousticStriae"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_acousticStriae"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_acousticStriae"},
    ],
    lookup_label="WHSSDatlas_acousticStriae",
    name="acoustic striae",
)
ParcellationEntity.whss_datlas_agranular_insular_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_agranularInsularCortex",
    alternate_names=["AI"],
    lookup_label="WHSSDatlas_agranularInsularCortex",
    name="agranular insular cortex",
)
ParcellationEntity.whss_datlas_agranular_insular_cortex_dorsal_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_agranularInsularCortexDorsalArea",
    alternate_names=["AI-d"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_agranularInsularCortexDorsalArea"
        }
    ],
    lookup_label="WHSSDatlas_agranularInsularCortexDorsalArea",
    name="agranular insular cortex dorsal area",
)
ParcellationEntity.whss_datlas_agranular_insular_cortex_posterior_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_agranularInsularCortexPosteriorArea",
    alternate_names=["AI-p"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_agranularInsularCortexPosteriorArea"
        }
    ],
    lookup_label="WHSSDatlas_agranularInsularCortexPosteriorArea",
    name="agranular insular cortex, posterior area",
)
ParcellationEntity.whss_datlas_agranular_insular_cortex_ventral_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_agranularInsularCortexVentralArea",
    alternate_names=["AI-v"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_agranularInsularCortexVentralArea"
        }
    ],
    lookup_label="WHSSDatlas_agranularInsularCortexVentralArea",
    name="agranular insular cortex, ventral area",
)
ParcellationEntity.whss_datlas_alveus_of_the_hippocampus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_alveusOfTheHippocampus",
    alternate_names=["alv"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_alveusOfTheHippocampus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_alveusOfTheHippocampus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_alveusOfTheHippocampus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_alveusOfTheHippocampus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_alveusOfTheHippocampus"
        },
    ],
    lookup_label="WHSSDatlas_alveusOfTheHippocampus",
    name="alveus of the hippocampus",
)
ParcellationEntity.whss_datlas_amygdaloid_area_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_amygdaloidAreaUnspecified",
    alternate_names=["Am-u"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_amygdaloidAreaUnspecified"
        }
    ],
    lookup_label="WHSSDatlas_amygdaloidAreaUnspecified",
    name="amygdaloid area, unspecified",
)
ParcellationEntity.whss_datlas_angular_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_angularThalamicNucleus",
    alternate_names=["Ang"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_angularThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_angularThalamicNucleus",
    name="angular thalamic nucleus",
)
ParcellationEntity.whss_datlas_anterior_commissure = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteriorCommissure",
    alternate_names=["ac"],
    lookup_label="WHSSDatlas_anteriorCommissure",
    name="anterior commissure",
)
ParcellationEntity.whss_datlas_anterior_commissure_anterior_limb = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteriorCommissureAnteriorLimb",
    alternate_names=["aca", "anterior commissure, anterior part"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_anteriorCommissureAnteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_anteriorCommissureAnteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_anteriorCommissureAnteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_anteriorCommissureAnteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_anteriorCommissureAnteriorLimb"
        },
    ],
    lookup_label="WHSSDatlas_anteriorCommissureAnteriorLimb",
    name="anterior commissure, anterior limb",
)
ParcellationEntity.whss_datlas_anterior_commissure_intrabulbar_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteriorCommissureIntrabulbarPart",
    alternate_names=["aci"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_anteriorCommissureIntrabulbarPart"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_anteriorCommissure"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_anteriorCommissure"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_anteriorCommissure"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_anteriorCommissureIntrabulbarPart"
        },
    ],
    lookup_label="WHSSDatlas_anteriorCommissureIntrabulbarPart",
    name="anterior commissure, intrabulbar part",
)
ParcellationEntity.whss_datlas_anterior_commissure_posterior_limb = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteriorCommissurePosteriorLimb",
    alternate_names=["acp", "anterior commissure, posterior part"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_anteriorCommissurePosteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_anteriorCommissurePosteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_anteriorCommissurePosteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_anteriorCommissurePosteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_anteriorCommissurePosteriorLimb"
        },
    ],
    lookup_label="WHSSDatlas_anteriorCommissurePosteriorLimb",
    name="anterior commissure, posterior limb",
)
ParcellationEntity.whss_datlas_anterior_nuclei_of_the_dorsal_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteriorNucleiOfTheDorsalThalamus",
    alternate_names=["ANT"],
    lookup_label="WHSSDatlas_anteriorNucleiOfTheDorsalThalamus",
    name="anterior nuclei of the dorsal thalamus",
)
ParcellationEntity.whss_datlas_anterodorsal_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anterodorsalThalamicNucleus",
    alternate_names=["AD"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_anterodorsalThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_anterodorsalThalamicNucleus",
    name="anterodorsal thalamic nucleus",
)
ParcellationEntity.whss_datlas_anteromedial_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteromedialThalamicNucleus",
    alternate_names=["AM"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_anteromedialThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_anteromedialThalamicNucleus",
    name="anteromedial thalamic nucleus",
)
ParcellationEntity.whss_datlas_anteroventral_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteroventralThalamicNucleus",
    alternate_names=["AV"],
    lookup_label="WHSSDatlas_anteroventralThalamicNucleus",
    name="anteroventral thalamic nucleus",
)
ParcellationEntity.whss_datlas_anteroventral_thalamic_nucleus_dorsomedial_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteroventralThalamicNucleusDorsomedialPart",
    alternate_names=["AV-dm"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_anteroventralThalamicNucleusDorsomedialPart"
        }
    ],
    lookup_label="WHSSDatlas_anteroventralThalamicNucleusDorsomedialPart",
    name="anteroventral thalamic nucleus, dorsomedial part",
)
ParcellationEntity.whss_datlas_anteroventral_thalamic_nucleus_ventrolateral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_anteroventralThalamicNucleusVentrolateralPart",
    alternate_names=["AV-vl"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_anteroventralThalamicNucleusVentrolateralPart"
        }
    ],
    lookup_label="WHSSDatlas_anteroventralThalamicNucleusVentrolateralPart",
    name="anteroventral thalamic nucleus, ventrolateral part",
)
ParcellationEntity.whss_datlas_ascending_fibers_of_the_facial_nerve = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ascendingFibersOfTheFacialNerve",
    alternate_names=["asc7"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_ascendingFibersOfTheFacialNerve"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_ascendingFibersOfTheFacialNerve"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_ascendingFibersOfTheFacialNerve"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_ascendingFibersOfTheFacialNerve"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ascendingFibersOfTheFacialNerve"
        },
    ],
    lookup_label="WHSSDatlas_ascendingFibersOfTheFacialNerve",
    name="ascending fibers of the facial nerve",
)
ParcellationEntity.whss_datlas_auditory_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_auditoryCortex",
    alternate_names=["Au"],
    lookup_label="WHSSDatlas_auditoryCortex",
    name="auditory cortex",
)
ParcellationEntity.whss_datlas_basal_forebrain_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_basalForebrainRegion",
    alternate_names=["BRF"],
    lookup_label="WHSSDatlas_basalForebrainRegion",
    name="basal forebrain region",
)
ParcellationEntity.whss_datlas_basal_forebrain_region_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_basalForebrainRegionUnspecified",
    alternate_names=["BFR-u"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_basalForebrainRegion"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_basalForebrainRegion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_basalForebrainRegion"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_basalForebrainRegion"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_basalForebrainRegionUnspecified"
        },
    ],
    lookup_label="WHSSDatlas_basalForebrainRegionUnspecified",
    name="basal forebrain region, unspecified",
)
ParcellationEntity.whss_datlas_bed_nucleus_of_the_stria_terminalis = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_bedNucleusOfTheStriaTerminalis",
    alternate_names=["BNST"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_bedNucleusOfTheStriaTerminalis"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_bedNucleusOfTheStriaTerminalis"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_bedNucleusOfTheStriaTerminalis"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_bedNucleusOfTheStriaTerminalis"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_bedNucleusOfTheStriaTerminalis"
        },
    ],
    lookup_label="WHSSDatlas_bedNucleusOfTheStriaTerminalis",
    name="bed nucleus of the stria terminalis",
)
ParcellationEntity.whss_datlas_brachium_of_the_superior_colliculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_brachiumOfTheSuperiorColliculus",
    alternate_names=["bsc"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_brachiumOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_brachiumOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_brachiumOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_brachiumOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_brachiumOfTheSuperiorColliculus"
        },
    ],
    lookup_label="WHSSDatlas_brachiumOfTheSuperiorColliculus",
    name="brachium of the superior colliculus",
)
ParcellationEntity.whss_datlas_brain = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_brain",
    alternate_names=["whole brain"],
    lookup_label="WHSSDatlas_brain",
    name="brain",
)
ParcellationEntity.whss_datlas_brainstem = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_brainstem",
    alternate_names=["BS"],
    lookup_label="WHSSDatlas_brainstem",
    name="brainstem",
)
ParcellationEntity.whss_datlas_brainstem_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_brainstemUnspecified",
    alternate_names=["BS-u", "brain stem, unspecified"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_brainstem"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_brainstem"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_brainstem"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_brainstem"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_brainstemUnspecified"},
    ],
    lookup_label="WHSSDatlas_brainstemUnspecified",
    name="brainstem, unspecified",
)
ParcellationEntity.whss_datlas_caudal_entorhinal_field = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_caudalEntorhinalField",
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_caudalEntorhinalField"
        }
    ],
    lookup_label="WHSSDatlas_caudalEntorhinalField",
    name="caudal entorhinal field",
)
ParcellationEntity.whss_datlas_caudate_putamen = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_caudatePutamen",
    alternate_names=["CPu"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_caudatePutamen"}
    ],
    lookup_label="WHSSDatlas_caudatePutamen",
    name="caudate putamen",
)
ParcellationEntity.whss_datlas_central_canal = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_centralCanal",
    alternate_names=["CC"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_centralCanal"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_centralCanal"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_centralCanal"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_centralCanal"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_centralCanal"},
    ],
    lookup_label="WHSSDatlas_centralCanal",
    name="central canal",
)
ParcellationEntity.whss_datlas_central_lateral_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_centralLateralThalamicNucleus",
    alternate_names=["CL"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_centralLateralThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_centralLateralThalamicNucleus",
    name="central lateral thalamic nucleus",
)
ParcellationEntity.whss_datlas_central_medial_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_centralMedialThalamicNucleus",
    alternate_names=["CM"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_centralMedialThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_centralMedialThalamicNucleus",
    name="central medial thalamic nucleus",
)
ParcellationEntity.whss_datlas_cerebellar_and_precerebellar_white_matter = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebellarAndPrecerebellarWhiteMatter",
    alternate_names=["cbt"],
    lookup_label="WHSSDatlas_cerebellarAndPrecerebellarWhiteMatter",
    name="cerebellar and precerebellar white matter",
)
ParcellationEntity.whss_datlas_cerebellum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebellum",
    alternate_names=["Cb"],
    lookup_label="WHSSDatlas_cerebellum",
    name="cerebellum",
)
ParcellationEntity.whss_datlas_cerebellum_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebellumUnspecified",
    alternate_names=["Cb-u", "deeper cerebellum"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_deeperCerebellum"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_granuleCellLevelOfTheCerebellum"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_granuleCellLevelOfTheCerebellum"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_granuleCellLevelOfTheCerebellum"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_cerebellumUnspecified"
        },
    ],
    lookup_label="WHSSDatlas_cerebellumUnspecified",
    name="cerebellum, unspecified",
)
ParcellationEntity.whss_datlas_cerebral_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebralCortex",
    alternate_names=["Cx"],
    lookup_label="WHSSDatlas_cerebralCortex",
    name="cerebral cortex",
)
ParcellationEntity.whss_datlas_cerebral_cortex_including_the_neocortex_and_the_hippocampus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebralCortexIncludingTheNeocortexAndTheHippocampus",
    lookup_label="WHSSDatlas_cerebralCortexIncludingTheNeocortexAndTheHippocampus",
    name="cerebral cortex including the neocortex and the hippocampus",
)
ParcellationEntity.whss_datlas_cerebral_nuclei = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebralNuclei",
    alternate_names=["CNc"],
    lookup_label="WHSSDatlas_cerebralNuclei",
    name="cerebral nuclei",
)
ParcellationEntity.whss_datlas_cerebrum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cerebrum",
    alternate_names=["CER"],
    lookup_label="WHSSDatlas_cerebrum",
    name="cerebrum",
)
ParcellationEntity.whss_datlas_cingulate_area1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cingulateArea1",
    alternate_names=["Cg1"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_cingulateArea1"}
    ],
    lookup_label="WHSSDatlas_cingulateArea1",
    name="cingulate area 1",
)
ParcellationEntity.whss_datlas_cingulate_area2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cingulateArea2",
    alternate_names=["Cg2", "cingulate cortex, area 2"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_cingulateCortexArea2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_cingulateCortexArea2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_cingulateCortexArea2"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_cingulateCortexArea2"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_cingulateArea2"},
    ],
    lookup_label="WHSSDatlas_cingulateArea2",
    name="cingulate area 2",
)
ParcellationEntity.whss_datlas_cingulate_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cingulateCortex",
    alternate_names=["Cg"],
    lookup_label="WHSSDatlas_cingulateCortex",
    name="cingulate cortex",
)
ParcellationEntity.whss_datlas_cingulate_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cingulateRegion",
    alternate_names=["CgR"],
    lookup_label="WHSSDatlas_cingulateRegion",
    name="cingulate region",
)
ParcellationEntity.whss_datlas_claustrum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_claustrum",
    alternate_names=["CLA"],
    has_versions=[{"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_claustrum"}],
    lookup_label="WHSSDatlas_claustrum",
    name="claustrum",
)
ParcellationEntity.whss_datlas_cochlea = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cochlea",
    alternate_names=["Co"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_cochlea"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_cochlea"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_cochlea"},
    ],
    lookup_label="WHSSDatlas_cochlea",
    name="cochlea",
)
ParcellationEntity.whss_datlas_cochlear_nerve = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cochlearNerve",
    alternate_names=["8cn"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_cochlearNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_cochlearNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_cochlearNerve"},
    ],
    lookup_label="WHSSDatlas_cochlearNerve",
    name="cochlear nerve",
)
ParcellationEntity.whss_datlas_cochlear_nucleus_dorsal_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cochlearNucleusDorsalPart",
    alternate_names=["DCN"],
    lookup_label="WHSSDatlas_cochlearNucleusDorsalPart",
    name="cochlear nucleus, dorsal part",
)
ParcellationEntity.whss_datlas_cochlear_nucleus_ventral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cochlearNucleusVentralPart",
    alternate_names=["VCN"],
    lookup_label="WHSSDatlas_cochlearNucleusVentralPart",
    name="cochlear nucleus, ventral part",
)
ParcellationEntity.whss_datlas_commissural_stria_terminalis = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_commissuralStriaTerminalis",
    alternate_names=["cst"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_commissuralStriaTerminalis"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_commissuralStriaTerminalis"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_commissuralStriaTerminalis"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_commissuralStriaTerminalis"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_commissuralStriaTerminalis"
        },
    ],
    lookup_label="WHSSDatlas_commissuralStriaTerminalis",
    name="commissural stria terminalis",
)
ParcellationEntity.whss_datlas_commissure_of_the_superior_colliculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_commissureOfTheSuperiorColliculus",
    alternate_names=["csc"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_commissureOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_commissureOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_commissureOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_commissureOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_commissureOfTheSuperiorColliculus"
        },
    ],
    lookup_label="WHSSDatlas_commissureOfTheSuperiorColliculus",
    name="commissure of the superior colliculus",
)
ParcellationEntity.whss_datlas_cornu_ammonis = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cornuAmmonis",
    alternate_names=["CA"],
    lookup_label="WHSSDatlas_cornuAmmonis",
    name="cornu ammonis",
)
ParcellationEntity.whss_datlas_cornu_ammonis1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cornuAmmonis1",
    alternate_names=["CA1"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_cornuAmmonis1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_cornuAmmonis1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_cornuAmmonis1"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_cornuAmmonis1"},
    ],
    lookup_label="WHSSDatlas_cornuAmmonis1",
    name="cornu ammonis 1",
)
ParcellationEntity.whss_datlas_cornu_ammonis2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cornuAmmonis2",
    alternate_names=["CA2"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_cornuAmmonis2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_cornuAmmonis2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_cornuAmmonis2"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_cornuAmmonis2"},
    ],
    lookup_label="WHSSDatlas_cornuAmmonis2",
    name="cornu ammonis 2",
)
ParcellationEntity.whss_datlas_cornu_ammonis3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_cornuAmmonis3",
    alternate_names=["CA3"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_cornuAmmonis3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_cornuAmmonis3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_cornuAmmonis3"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_cornuAmmonis3"},
    ],
    lookup_label="WHSSDatlas_cornuAmmonis3",
    name="cornu ammonis 3",
)
ParcellationEntity.whss_datlas_corpus_callosum_and_associated_subcortical_white_matter = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_corpusCallosumAndAssociatedSubcorticalWhiteMatter",
    alternate_names=["cc-ec-cing-dwm"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_corpusCallosumAndAssociatedSubcorticalWhiteMatter"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_corpusCallosumAndAssociatedSubcorticalWhiteMatter"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_corpusCallosumAndAssociatedSubcorticalWhiteMatter"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_corpusCallosumAndAssociatedSubcorticalWhiteMatter"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_corpusCallosumAndAssociatedSubcorticalWhiteMatter"
        },
    ],
    lookup_label="WHSSDatlas_corpusCallosumAndAssociatedSubcorticalWhiteMatter",
    name="corpus callosum and associated subcortical white matter",
)
ParcellationEntity.whss_datlas_cortical_plate = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_corticalPlate",
    alternate_names=["CPl"],
    lookup_label="WHSSDatlas_corticalPlate",
    name="cortical plate",
)
ParcellationEntity.whss_datlas_cortical_subplate = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_corticalSubplate",
    alternate_names=["CSP"],
    lookup_label="WHSSDatlas_corticalSubplate",
    name="cortical subplate",
)
ParcellationEntity.whss_datlas_corticofugal_pathways = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_corticofugalPathways",
    alternate_names=["cfp"],
    lookup_label="WHSSDatlas_corticofugalPathways",
    name="corticofugal pathways",
)
ParcellationEntity.whss_datlas_corticofugal_tract_and_corona_radiata = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_corticofugalTractAndCoronaRadiata",
    alternate_names=["ic-cp-lfp-py", "descending corticofugal pathways"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_descendingCorticofugalPathways"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_descendingCorticofugalPathways"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_descendingCorticofugalPathways"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_descendingCorticofugalPathways"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_corticofugalTractAndCoronaRadiata"
        },
    ],
    lookup_label="WHSSDatlas_corticofugalTractAndCoronaRadiata",
    name="corticofugal tract and corona radiata",
)
ParcellationEntity.whss_datlas_deeper_layers_of_the_superior_colliculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_deeperLayersOfTheSuperiorColliculus",
    alternate_names=["SuD"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_deeperLayersOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_deeperLayersOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_deeperLayersOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_deeperLayersOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_deeperLayersOfTheSuperiorColliculus"
        },
    ],
    lookup_label="WHSSDatlas_deeperLayersOfTheSuperiorColliculus",
    name="deeper layers of the superior colliculus",
)
ParcellationEntity.whss_datlas_dentate_gyrus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dentateGyrus",
    alternate_names=["DG"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_dentateGyrus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_dentateGyrus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_dentateGyrus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_dentateGyrus"},
    ],
    lookup_label="WHSSDatlas_dentateGyrus",
    name="dentate gyrus",
)
ParcellationEntity.whss_datlas_diencephalon = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_diencephalon",
    alternate_names=["Dien"],
    lookup_label="WHSSDatlas_diencephalon",
    name="diencephalon",
)
ParcellationEntity.whss_datlas_dorsal_cochlear_nucleus_deep_core = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalCochlearNucleusDeepCore",
    alternate_names=["DCND"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_dorsalCochlearNucleusDeepCore"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_dorsalCochlearNucleusDeepCore"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_dorsalCochlearNucleusDeepCore"
        },
    ],
    lookup_label="WHSSDatlas_dorsalCochlearNucleusDeepCore",
    name="dorsal cochlear nucleus, deep core",
)
ParcellationEntity.whss_datlas_dorsal_cochlear_nucleus_fusiform_and_granule_layer = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalCochlearNucleusFusiformAndGranuleLayer",
    alternate_names=["DCNFG"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_dorsalCochlearNucleusFusiformAndGranuleLayer"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_dorsalCochlearNucleusFusiformAndGranuleLayer"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_dorsalCochlearNucleusFusiformAndGranuleLayer"
        },
    ],
    lookup_label="WHSSDatlas_dorsalCochlearNucleusFusiformAndGranuleLayer",
    name="dorsal cochlear nucleus, fusiform and granule layer",
)
ParcellationEntity.whss_datlas_dorsal_cochlear_nucleus_molecular_layer = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalCochlearNucleusMolecularLayer",
    alternate_names=["DCNM"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_dorsalCochlearNucleusMolecularLayer"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_dorsalCochlearNucleusMolecularLayer"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_dorsalCochlearNucleusMolecularLayer"
        },
    ],
    lookup_label="WHSSDatlas_dorsalCochlearNucleusMolecularLayer",
    name="dorsal cochlear nucleus, molecular layer",
)
ParcellationEntity.whss_datlas_dorsal_lateral_geniculate_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalLateralGeniculateNucleus",
    alternate_names=["DLG"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_dorsalLateralGeniculateNucleus"
        }
    ],
    lookup_label="WHSSDatlas_dorsalLateralGeniculateNucleus",
    name="dorsal lateral geniculate nucleus",
)
ParcellationEntity.whss_datlas_dorsal_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalThalamus",
    alternate_names=["Thal-D"],
    lookup_label="WHSSDatlas_dorsalThalamus",
    name="dorsal thalamus",
)
ParcellationEntity.whss_datlas_dorsalcaudal_midline_group_of_the_dorsal_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalcaudalMidlineGroupOfTheDorsalThalamus",
    alternate_names=["DC-MID"],
    lookup_label="WHSSDatlas_dorsalcaudalMidlineGroupOfTheDorsalThalamus",
    name="dorsal-caudal midline group of the dorsal thalamus",
)
ParcellationEntity.whss_datlas_dorsalintermediate_entorhinal_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsalintermediateEntorhinalArea",
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_dorsalintermediateEntorhinalArea"
        }
    ],
    lookup_label="WHSSDatlas_dorsalintermediateEntorhinalArea",
    name="dorsal-intermediate entorhinal area",
)
ParcellationEntity.whss_datlas_dorsallateral_entorhinal_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsallateralEntorhinalArea",
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_dorsallateralEntorhinalArea"
        }
    ],
    lookup_label="WHSSDatlas_dorsallateralEntorhinalArea",
    name="dorsal-lateral entorhinal area",
)
ParcellationEntity.whss_datlas_dorsolateral_orbital_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dorsolateralOrbitalArea",
    alternate_names=["DLO"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_dorsolateralOrbitalArea"
        }
    ],
    lookup_label="WHSSDatlas_dorsolateralOrbitalArea",
    name="dorsolateral orbital area",
)
ParcellationEntity.whss_datlas_dysgranular_insular_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_dysgranularInsularCortex",
    alternate_names=["DI"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_dysgranularInsularCortex"
        }
    ],
    lookup_label="WHSSDatlas_dysgranularInsularCortex",
    name="dysgranular insular cortex",
)
ParcellationEntity.whss_datlas_endopiriform_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_endopiriformNucleus",
    alternate_names=["Endo"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_endopiriformNucleus"}
    ],
    lookup_label="WHSSDatlas_endopiriformNucleus",
    name="endopiriform nucleus",
)
ParcellationEntity.whss_datlas_entopeduncular_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_entopeduncularNucleus",
    alternate_names=["EP"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_entopeduncularNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_entopeduncularNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_entopeduncularNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_entopeduncularNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_entopeduncularNucleus"
        },
    ],
    lookup_label="WHSSDatlas_entopeduncularNucleus",
    name="entopeduncular nucleus",
)
ParcellationEntity.whss_datlas_entorhinal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_entorhinalCortex",
    alternate_names=["EC"],
    lookup_label="WHSSDatlas_entorhinalCortex",
    name="entorhinal cortex",
)
ParcellationEntity.whss_datlas_epithalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_epithalamus",
    alternate_names=["Thal-EPI"],
    lookup_label="WHSSDatlas_epithalamus",
    name="epithalamus",
)
ParcellationEntity.whss_datlas_ethmoid_limitans_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ethmoidLimitansNucleus",
    alternate_names=["Eth"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ethmoidLimitansNucleus"
        }
    ],
    lookup_label="WHSSDatlas_ethmoidLimitansNucleus",
    name="ethmoid-Limitans nucleus",
)
ParcellationEntity.whss_datlas_external_medullary_lamina = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_externalMedullaryLamina",
    alternate_names=["eml"],
    lookup_label="WHSSDatlas_externalMedullaryLamina",
    name="external medullary lamina",
)
ParcellationEntity.whss_datlas_external_medullary_lamina_auditory_radiation = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_externalMedullaryLaminaAuditoryRadiation",
    alternate_names=["eml-ar", "auditory radiation"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_auditoryRadiation"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_auditoryRadiation"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_externalMedullaryLaminaAuditoryRadiation"
        },
    ],
    lookup_label="WHSSDatlas_externalMedullaryLaminaAuditoryRadiation",
    name="external medullary lamina, auditory radiation",
)
ParcellationEntity.whss_datlas_external_medullary_lamina_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_externalMedullaryLaminaUnspecified",
    alternate_names=["eml-u"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_externalMedullaryLaminaUnspecified"
        }
    ],
    lookup_label="WHSSDatlas_externalMedullaryLaminaUnspecified",
    name="external medullary lamina, unspecified",
)
ParcellationEntity.whss_datlas_facial_nerve = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_facialNerve",
    alternate_names=["7n"],
    lookup_label="WHSSDatlas_facialNerve",
    name="facial nerve",
)
ParcellationEntity.whss_datlas_facial_nerve_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_facialNerveUnspecified",
    alternate_names=["7n-u"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_facialNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_facialNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_facialNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_facialNerve"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_facialNerveUnspecified"
        },
    ],
    lookup_label="WHSSDatlas_facialNerveUnspecified",
    name="facial nerve, unspecified",
)
ParcellationEntity.whss_datlas_fasciculus_retroflexus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_fasciculusRetroflexus",
    alternate_names=["fr"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_fasciculusRetroflexus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_fasciculusRetroflexus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_fasciculusRetroflexus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_fasciculusRetroflexus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_fasciculusRetroflexus"
        },
    ],
    lookup_label="WHSSDatlas_fasciculusRetroflexus",
    name="fasciculus retroflexus",
)
ParcellationEntity.whss_datlas_fasciola_cinereum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_fasciolaCinereum",
    alternate_names=["FC"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_fasciolaCinereum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_fasciolaCinereum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_fasciolaCinereum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_fasciolaCinereum"},
    ],
    lookup_label="WHSSDatlas_fasciolaCinereum",
    name="fasciola cinereum",
)
ParcellationEntity.whss_datlas_fields_of_forel = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_fieldsOfForel",
    alternate_names=["FoF"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_fieldsOfForel"}
    ],
    lookup_label="WHSSDatlas_fieldsOfForel",
    name="fields of Forel",
)
ParcellationEntity.whss_datlas_fimbria_of_the_hippocampus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_fimbriaOfTheHippocampus",
    alternate_names=["fi"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_fimbriaOfTheHippocampus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_fimbriaOfTheHippocampus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_fimbriaOfTheHippocampus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_fimbriaOfTheHippocampus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_fimbriaOfTheHippocampus"
        },
    ],
    lookup_label="WHSSDatlas_fimbriaOfTheHippocampus",
    name="fimbria of the hippocampus",
)
ParcellationEntity.whss_datlas_fornix = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_fornix",
    alternate_names=["f"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_fornix"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_fornix"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_fornix"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_fornix"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_fornix"},
    ],
    lookup_label="WHSSDatlas_fornix",
    name="fornix",
)
ParcellationEntity.whss_datlas_frontal_association_area3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_frontalAssociationArea3",
    alternate_names=["Fr3"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_frontalAssociationArea3"
        }
    ],
    lookup_label="WHSSDatlas_frontalAssociationArea3",
    name="frontal association area 3",
)
ParcellationEntity.whss_datlas_frontal_association_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_frontalAssociationCortex",
    alternate_names=["FrA"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_frontalAssociationCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_frontalAssociationCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_frontalAssociationCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_frontalAssociationCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_frontalAssociationCortex"
        },
    ],
    lookup_label="WHSSDatlas_frontalAssociationCortex",
    name="frontal association cortex",
)
ParcellationEntity.whss_datlas_frontal_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_frontalRegion",
    alternate_names=["Front"],
    lookup_label="WHSSDatlas_frontalRegion",
    name="frontal region",
)
ParcellationEntity.whss_datlas_genu_of_the_facial_nerve = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_genuOfTheFacialNerve",
    alternate_names=["g7"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_genuOfTheFacialNerve"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_genuOfTheFacialNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_genuOfTheFacialNerve"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_genuOfTheFacialNerve"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_genuOfTheFacialNerve"},
    ],
    lookup_label="WHSSDatlas_genuOfTheFacialNerve",
    name="genu of the facial nerve",
)
ParcellationEntity.whss_datlas_globus_pallidus_external = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_globusPallidusExternal",
    alternate_names=["Gpe", "globus pallidus"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_globusPallidus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_globusPallidus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_globusPallidus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_globusPallidus"},
    ],
    lookup_label="WHSSDatlas_globusPallidusExternal",
    name="globus pallidus external",
)
ParcellationEntity.whss_datlas_globus_pallidus_external_lateral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_globusPallidusExternalLateralPart",
    alternate_names=["GPe-l"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_globusPallidusExternalLateralPart"
        }
    ],
    lookup_label="WHSSDatlas_globusPallidusExternalLateralPart",
    name="globus pallidus external, lateral part",
)
ParcellationEntity.whss_datlas_globus_pallidus_external_medial_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_globusPallidusExternalMedialPart",
    alternate_names=["GPe-m"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_globusPallidusExternalMedialPart"
        }
    ],
    lookup_label="WHSSDatlas_globusPallidusExternalMedialPart",
    name="globus pallidus external, medial part",
)
ParcellationEntity.whss_datlas_glomerular_layer_of_the_accessory_olfactory_bulb = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_glomerularLayerOfTheAccessoryOlfactoryBulb",
    alternate_names=["GlA"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_glomerularLayerOfTheAccessoryOlfactoryBulb"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_glomerularLayerOfTheAccessoryOlfactoryBulb"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_glomerularLayerOfTheAccessoryOlfactoryBulb"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_glomerularLayerOfTheAccessoryOlfactoryBulb"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_glomerularLayerOfTheAccessoryOlfactoryBulb"
        },
    ],
    lookup_label="WHSSDatlas_glomerularLayerOfTheAccessoryOlfactoryBulb",
    name="glomerular layer of the accessory olfactory bulb",
)
ParcellationEntity.whss_datlas_glomerular_layer_of_the_olfactory_bulb = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_glomerularLayerOfTheOlfactoryBulb",
    alternate_names=["Gl"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_glomerularLayerOfTheOlfactoryBulb"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_glomerularLayerOfTheOlfactoryBulb"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_glomerularLayerOfTheOlfactoryBulb"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_glomerularLayerOfTheOlfactoryBulb"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_glomerularLayerOfTheOlfactoryBulb"
        },
    ],
    lookup_label="WHSSDatlas_glomerularLayerOfTheOlfactoryBulb",
    name="glomerular layer of the olfactory bulb",
)
ParcellationEntity.whss_datlas_granular_insular_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_granularInsularCortex",
    alternate_names=["GI"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_granularInsularCortex"}
    ],
    lookup_label="WHSSDatlas_granularInsularCortex",
    name="granular insular cortex",
)
ParcellationEntity.whss_datlas_gray_matter = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_grayMatter",
    alternate_names=["GM"],
    lookup_label="WHSSDatlas_grayMatter",
    name="gray matter",
)
ParcellationEntity.whss_datlas_habenular_commissure = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_habenularCommissure",
    alternate_names=["hbc"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_habenularCommissure"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_habenularCommissure"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_habenularCommissure"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_habenularCommissure"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_habenularCommissure"},
    ],
    lookup_label="WHSSDatlas_habenularCommissure",
    name="habenular commissure",
)
ParcellationEntity.whss_datlas_hindbrain = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hindbrain",
    alternate_names=["HB"],
    lookup_label="WHSSDatlas_hindbrain",
    name="hindbrain",
)
ParcellationEntity.whss_datlas_hippocampal_formation = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hippocampalFormation",
    alternate_names=["HF"],
    lookup_label="WHSSDatlas_hippocampalFormation",
    name="hippocampal formation",
)
ParcellationEntity.whss_datlas_hippocampal_formation_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hippocampalFormationUnspecified",
    alternate_names=["HF-u"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_hippocampalFormation"
        }
    ],
    lookup_label="WHSSDatlas_hippocampalFormationUnspecified",
    name="hippocampal formation, unspecified",
)
ParcellationEntity.whss_datlas_hippocampal_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hippocampalRegion",
    alternate_names=["HR"],
    lookup_label="WHSSDatlas_hippocampalRegion",
    name="hippocampal region",
)
ParcellationEntity.whss_datlas_hippocampal_white_matter = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hippocampalWhiteMatter",
    alternate_names=["hiw"],
    lookup_label="WHSSDatlas_hippocampalWhiteMatter",
    name="hippocampal white matter",
)
ParcellationEntity.whss_datlas_hypothalamic_region_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hypothalamicRegionUnspecified",
    alternate_names=["HTh-u"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_hypothalamicRegion"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_hypothalamicRegion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_hypothalamicRegion"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_hypothalamicRegion"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_hypothalamicRegionUnspecified"
        },
    ],
    lookup_label="WHSSDatlas_hypothalamicRegionUnspecified",
    name="hypothalamic region, unspecified",
)
ParcellationEntity.whss_datlas_hypothalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_hypothalamus",
    alternate_names=["HY"],
    lookup_label="WHSSDatlas_hypothalamus",
    name="hypothalamus",
)
ParcellationEntity.whss_datlas_inferior_cerebellar_peduncle = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorCerebellarPeduncle",
    alternate_names=["icp"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_inferiorCerebellarPeduncle"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_inferiorCerebellarPeduncle"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_inferiorCerebellarPeduncle"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_inferiorCerebellarPeduncle"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_inferiorCerebellarPeduncle"
        },
    ],
    lookup_label="WHSSDatlas_inferiorCerebellarPeduncle",
    name="inferior cerebellar peduncle",
)
ParcellationEntity.whss_datlas_inferior_colliculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculus",
    alternate_names=["IC"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_inferiorColliculus"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_inferiorColliculus"},
    ],
    lookup_label="WHSSDatlas_inferiorColliculus",
    name="inferior colliculus",
)
ParcellationEntity.whss_datlas_inferior_colliculus_brachium = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculusBrachium",
    alternate_names=["bic"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_inferiorColliculusBrachium"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_inferiorColliculusBrachium"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_inferiorColliculusBrachium"
        },
    ],
    lookup_label="WHSSDatlas_inferiorColliculusBrachium",
    name="inferior colliculus, brachium",
)
ParcellationEntity.whss_datlas_inferior_colliculus_central_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculusCentralNucleus",
    alternate_names=["CNIC"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_inferiorColliculusCentralNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_inferiorColliculusCentralNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_inferiorColliculusCentralNucleus"
        },
    ],
    lookup_label="WHSSDatlas_inferiorColliculusCentralNucleus",
    name="inferior colliculus, central nucleus",
)
ParcellationEntity.whss_datlas_inferior_colliculus_commissure = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculusCommissure",
    alternate_names=["cic", "commissure of the inferior colliculus"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_commissureOfTheInferiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_commissureOfTheInferiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_inferiorColliculusCommissure"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_inferiorColliculusCommissure"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_inferiorColliculusCommissure"
        },
    ],
    lookup_label="WHSSDatlas_inferiorColliculusCommissure",
    name="inferior colliculus, commissure",
)
ParcellationEntity.whss_datlas_inferior_colliculus_dorsal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculusDorsalCortex",
    alternate_names=["DCIC"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_inferiorColliculusDorsalCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_inferiorColliculusDorsalCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_inferiorColliculusDorsalCortex"
        },
    ],
    lookup_label="WHSSDatlas_inferiorColliculusDorsalCortex",
    name="inferior colliculus, dorsal cortex",
)
ParcellationEntity.whss_datlas_inferior_colliculus_external_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorColliculusExternalCortex",
    alternate_names=["ECIC"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_inferiorColliculusExternalCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_inferiorColliculusExternalCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_inferiorColliculusExternalCortex"
        },
    ],
    lookup_label="WHSSDatlas_inferiorColliculusExternalCortex",
    name="inferior colliculus, external cortex",
)
ParcellationEntity.whss_datlas_inferior_olive = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_inferiorOlive",
    alternate_names=["IO"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_inferiorOlive"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_inferiorOlive"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_inferiorOlive"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_inferiorOlive"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_inferiorOlive"},
    ],
    lookup_label="WHSSDatlas_inferiorOlive",
    name="inferior olive",
)
ParcellationEntity.whss_datlas_infralimbic_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_infralimbicArea",
    alternate_names=["IL"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_infralimbicArea"}
    ],
    lookup_label="WHSSDatlas_infralimbicArea",
    name="infralimbic area",
)
ParcellationEntity.whss_datlas_inner_ear = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_innerEar",
    alternate_names=["IE"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_innerEar"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_innerEar"},
    ],
    lookup_label="WHSSDatlas_innerEar",
    name="inner ear",
)
ParcellationEntity.whss_datlas_insular_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_insularRegion",
    alternate_names=["INS"],
    lookup_label="WHSSDatlas_insularRegion",
    name="insular region",
)
ParcellationEntity.whss_datlas_interanteromedial_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_interanteromedialThalamicNucleus",
    alternate_names=["IAM"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_interanteromedialThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_interanteromedialThalamicNucleus",
    name="interanteromedial thalamic nucleus",
)
ParcellationEntity.whss_datlas_interbrain = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_interbrain",
    alternate_names=["ItB"],
    lookup_label="WHSSDatlas_interbrain",
    name="interbrain",
)
ParcellationEntity.whss_datlas_intergeniculate_leaflet = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_intergeniculateLeaflet",
    alternate_names=["IGL"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_intergeniculateLeaflet"
        }
    ],
    lookup_label="WHSSDatlas_intergeniculateLeaflet",
    name="intergeniculate leaflet",
)
ParcellationEntity.whss_datlas_intermediodorsal_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_intermediodorsalThalamicNucleus",
    alternate_names=["IMD"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_intermediodorsalThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_intermediodorsalThalamicNucleus",
    name="intermediodorsal thalamic nucleus",
)
ParcellationEntity.whss_datlas_internal_medullary_lamina = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_internalMedullaryLamina",
    alternate_names=["iml"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_internalMedullaryLamina"
        }
    ],
    lookup_label="WHSSDatlas_internalMedullaryLamina",
    name="internal medullary lamina",
)
ParcellationEntity.whss_datlas_interpeduncular_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_interpeduncularNucleus",
    alternate_names=["IP"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_interpeduncularNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_interpeduncularNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_interpeduncularNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_interpeduncularNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_interpeduncularNucleus"
        },
    ],
    lookup_label="WHSSDatlas_interpeduncularNucleus",
    name="interpeduncular nucleus",
)
ParcellationEntity.whss_datlas_intralaminar_nuclei_of_the_dorsal_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_intralaminarNucleiOfTheDorsalThalamus",
    alternate_names=["ILM"],
    lookup_label="WHSSDatlas_intralaminarNucleiOfTheDorsalThalamus",
    name="intralaminar nuclei of the dorsal thalamus",
)
ParcellationEntity.whss_datlas_intramedullary_thalamic_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_intramedullaryThalamicArea",
    alternate_names=["ima"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_intramedullaryThalamicArea"
        }
    ],
    lookup_label="WHSSDatlas_intramedullaryThalamicArea",
    name="intramedullary thalamic area",
)
ParcellationEntity.whss_datlas_isocortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_isocortex",
    alternate_names=["Icx"],
    lookup_label="WHSSDatlas_isocortex",
    name="isocortex",
)
ParcellationEntity.whss_datlas_laminated_pallium = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_laminatedPallium",
    alternate_names=["LamP"],
    lookup_label="WHSSDatlas_laminatedPallium",
    name="laminated pallium",
)
ParcellationEntity.whss_datlas_lateral_entorhinal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralEntorhinalCortex",
    alternate_names=["LEC"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_lateralEntorhinalCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_lateralEntorhinalCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_lateralEntorhinalCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralEntorhinalCortex"
        },
    ],
    lookup_label="WHSSDatlas_lateralEntorhinalCortex",
    name="lateral entorhinal cortex",
)
ParcellationEntity.whss_datlas_lateral_habenular_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralHabenularNucleus",
    alternate_names=["LHb"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralHabenularNucleus"
        }
    ],
    lookup_label="WHSSDatlas_lateralHabenularNucleus",
    name="lateral habenular nucleus",
)
ParcellationEntity.whss_datlas_lateral_lemniscus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscus",
    alternate_names=["ll"],
    lookup_label="WHSSDatlas_lateralLemniscus",
    name="lateral lemniscus",
)
ParcellationEntity.whss_datlas_lateral_lemniscus_commissure = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscusCommissure",
    alternate_names=["ll-c"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_lateralLemniscusCommissure"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_lateralLemniscusCommissure"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralLemniscusCommissure"
        },
    ],
    lookup_label="WHSSDatlas_lateralLemniscusCommissure",
    name="lateral lemniscus, commissure",
)
ParcellationEntity.whss_datlas_lateral_lemniscus_dorsal_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscusDorsalNucleus",
    alternate_names=["DLL"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_lateralLemniscusDorsalNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_lateralLemniscusDorsalNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralLemniscusDorsalNucleus"
        },
    ],
    lookup_label="WHSSDatlas_lateralLemniscusDorsalNucleus",
    name="lateral lemniscus, dorsal nucleus",
)
ParcellationEntity.whss_datlas_lateral_lemniscus_intermediate_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscusIntermediateNucleus",
    alternate_names=["ILL"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_lateralLemniscusIntermediateNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_lateralLemniscusIntermediateNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralLemniscusIntermediateNucleus"
        },
    ],
    lookup_label="WHSSDatlas_lateralLemniscusIntermediateNucleus",
    name="lateral lemniscus, intermediate nucleus",
)
ParcellationEntity.whss_datlas_lateral_lemniscus_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscusUnspecified",
    alternate_names=["ll-u"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_lateralLemniscus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_lateralLemniscus"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralLemniscusUnspecified"
        },
    ],
    lookup_label="WHSSDatlas_lateralLemniscusUnspecified",
    name="lateral lemniscus, unspecified",
)
ParcellationEntity.whss_datlas_lateral_lemniscus_ventral_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralLemniscusVentralNucleus",
    alternate_names=["VLL"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_lateralLemniscusVentralNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_lateralLemniscusVentralNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralLemniscusVentralNucleus"
        },
    ],
    lookup_label="WHSSDatlas_lateralLemniscusVentralNucleus",
    name="lateral lemniscus, ventral nucleus",
)
ParcellationEntity.whss_datlas_lateral_olfactory_tract = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralOlfactoryTract",
    alternate_names=["lot"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralOlfactoryTract"}
    ],
    lookup_label="WHSSDatlas_lateralOlfactoryTract",
    name="lateral olfactory tract",
)
ParcellationEntity.whss_datlas_lateral_orbital_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralOrbitalArea",
    alternate_names=["LO"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralOrbitalArea"}
    ],
    lookup_label="WHSSDatlas_lateralOrbitalArea",
    name="lateral orbital area",
)
ParcellationEntity.whss_datlas_lateral_posterior_pulvinar_complex_of_the_dorsal_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralPosteriorPulvinarComplexOfTheDorsalThalamus",
    alternate_names=["LP"],
    lookup_label="WHSSDatlas_lateralPosteriorPulvinarComplexOfTheDorsalThalamus",
    name="lateral posterior (pulvinar) complex of the dorsal thalamus",
)
ParcellationEntity.whss_datlas_lateral_posterior_thalamic_nucleus_lateral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralPosteriorThalamicNucleusLateralPart",
    alternate_names=["LP-l"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralPosteriorThalamicNucleusLateralPart"
        }
    ],
    lookup_label="WHSSDatlas_lateralPosteriorThalamicNucleusLateralPart",
    name="lateral posterior thalamic nucleus, lateral part",
)
ParcellationEntity.whss_datlas_lateral_posterior_thalamic_nucleus_mediocaudal_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralPosteriorThalamicNucleusMediocaudalPart",
    alternate_names=["LP-mc"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralPosteriorThalamicNucleusMediocaudalPart"
        }
    ],
    lookup_label="WHSSDatlas_lateralPosteriorThalamicNucleusMediocaudalPart",
    name="lateral posterior thalamic nucleus, mediocaudal part",
)
ParcellationEntity.whss_datlas_lateral_posterior_thalamic_nucleus_mediorostral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralPosteriorThalamicNucleusMediorostralPart",
    alternate_names=["LP-mr"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralPosteriorThalamicNucleusMediorostralPart"
        }
    ],
    lookup_label="WHSSDatlas_lateralPosteriorThalamicNucleusMediorostralPart",
    name="lateral posterior thalamic nucleus, mediorostral part",
)
ParcellationEntity.whss_datlas_lateral_superior_olive = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_lateralSuperiorOlive",
    alternate_names=["LSO"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_lateralSuperiorOlive"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_lateralSuperiorOlive"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_lateralSuperiorOlive"},
    ],
    lookup_label="WHSSDatlas_lateralSuperiorOlive",
    name="lateral superior olive",
)
ParcellationEntity.whss_datlas_laterodorsal_thalamic_nuclei_of_the_dorsal_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_laterodorsalThalamicNucleiOfTheDorsalThalamus",
    alternate_names=["LD"],
    lookup_label="WHSSDatlas_laterodorsalThalamicNucleiOfTheDorsalThalamus",
    name="laterodorsal thalamic nuclei of the dorsal thalamus",
)
ParcellationEntity.whss_datlas_laterodorsal_thalamic_nucleus_dorsomedial_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_laterodorsalThalamicNucleusDorsomedialPart",
    alternate_names=["LD-dm"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_laterodorsalThalamicNucleusDorsomedialPart"
        }
    ],
    lookup_label="WHSSDatlas_laterodorsalThalamicNucleusDorsomedialPart",
    name="laterodorsal thalamic nucleus, dorsomedial part",
)
ParcellationEntity.whss_datlas_laterodorsal_thalamic_nucleus_ventrolateral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_laterodorsalThalamicNucleusVentrolateralPart",
    alternate_names=["LD-vl"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_laterodorsalThalamicNucleusVentrolateralPart"
        }
    ],
    lookup_label="WHSSDatlas_laterodorsalThalamicNucleusVentrolateralPart",
    name="laterodorsal thalamic nucleus, ventrolateral part",
)
ParcellationEntity.whss_datlas_mammillotegmental_tract = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mammillotegmentalTract",
    alternate_names=["mtg"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_mammillothalamicTract"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_mammillothalamicTract"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_mammillothalamicTract"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_mammillothalamicTract"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_mammillotegmentalTract"
        },
    ],
    lookup_label="WHSSDatlas_mammillotegmentalTract",
    name="mammillotegmental tract",
)
ParcellationEntity.whss_datlas_medial_entorhinal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialEntorhinalCortex",
    alternate_names=["MEC"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_entorhinalCortex"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_entorhinalCortex"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_entorhinalCortex"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_medialEntorhinalCortex"
        },
    ],
    lookup_label="WHSSDatlas_medialEntorhinalCortex",
    name="medial entorhinal cortex",
)
ParcellationEntity.whss_datlas_medial_entorhinal_field = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialEntorhinalField",
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_medialEntorhinalField"
        }
    ],
    lookup_label="WHSSDatlas_medialEntorhinalField",
    name="medial entorhinal field",
)
ParcellationEntity.whss_datlas_medial_geniculate_body_dorsal_division = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateBodyDorsalDivision",
    alternate_names=["MG-d"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_medialGeniculateBodyDorsalDivision"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_medialGeniculateBodyDorsalDivision"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_medialGeniculateBodyDorsalDivision"
        },
    ],
    lookup_label="WHSSDatlas_medialGeniculateBodyDorsalDivision",
    name="medial geniculate body, dorsal division",
)
ParcellationEntity.whss_datlas_medial_geniculate_body_marginal_zone = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateBodyMarginalZone",
    alternate_names=["MG-mz"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_medialGeniculateBodyMarginalZone"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_medialGeniculateBodyMarginalZone"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_medialGeniculateBodyMarginalZone"
        },
    ],
    lookup_label="WHSSDatlas_medialGeniculateBodyMarginalZone",
    name="medial geniculate body, marginal zone",
)
ParcellationEntity.whss_datlas_medial_geniculate_body_medial_division = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateBodyMedialDivision",
    alternate_names=["MG-m"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_medialGeniculateBodyMedialDivision"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_medialGeniculateBodyMedialDivision"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_medialGeniculateBodyMedialDivision"
        },
    ],
    lookup_label="WHSSDatlas_medialGeniculateBodyMedialDivision",
    name="medial geniculate body, medial division",
)
ParcellationEntity.whss_datlas_medial_geniculate_body_suprageniculate_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateBodySuprageniculateNucleus",
    alternate_names=["MG-sg"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_medialGeniculateBodySuprageniculateNucleus"
        }
    ],
    lookup_label="WHSSDatlas_medialGeniculateBodySuprageniculateNucleus",
    name="medial geniculate body, suprageniculate nucleus",
)
ParcellationEntity.whss_datlas_medial_geniculate_body_ventral_division = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateBodyVentralDivision",
    alternate_names=["MG-v"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_medialGeniculateBodyVentralDivision"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_medialGeniculateBodyVentralDivision"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_medialGeniculateBodyVentralDivision"
        },
    ],
    lookup_label="WHSSDatlas_medialGeniculateBodyVentralDivision",
    name="medial geniculate body, ventral division",
)
ParcellationEntity.whss_datlas_medial_geniculate_complex_of_the_dorsal_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialGeniculateComplexOfTheDorsalThalamus",
    alternate_names=["MG", "medial geniculate body"],
    lookup_label="WHSSDatlas_medialGeniculateComplexOfTheDorsalThalamus",
    name="medial geniculate complex of the dorsal thalamus",
)
ParcellationEntity.whss_datlas_medial_habenular_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialHabenularNucleus",
    alternate_names=["MHb"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_medialHabenularNucleus"
        }
    ],
    lookup_label="WHSSDatlas_medialHabenularNucleus",
    name="medial habenular nucleus",
)
ParcellationEntity.whss_datlas_medial_lemniscus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialLemniscus",
    alternate_names=["ml"],
    lookup_label="WHSSDatlas_medialLemniscus",
    name="medial lemniscus",
)
ParcellationEntity.whss_datlas_medial_lemniscus_decussation = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialLemniscusDecussation",
    alternate_names=["mlx"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_medialLemniscusDecussation"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_medialLemniscusDecussation"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_medialLemniscusDecussation"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_medialLemniscusDecussation"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_medialLemniscusDecussation"
        },
    ],
    lookup_label="WHSSDatlas_medialLemniscusDecussation",
    name="medial lemniscus decussation",
)
ParcellationEntity.whss_datlas_medial_lemniscus_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialLemniscusUnspecified",
    alternate_names=["ml-u"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_medialLemniscus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_medialLemniscus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_medialLemniscus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_medialLemniscus"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_medialLemniscusUnspecified"
        },
    ],
    lookup_label="WHSSDatlas_medialLemniscusUnspecified",
    name="medial lemniscus, unspecified",
)
ParcellationEntity.whss_datlas_medial_orbital_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialOrbitalArea",
    alternate_names=["MO"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_medialOrbitalArea"}
    ],
    lookup_label="WHSSDatlas_medialOrbitalArea",
    name="medial orbital area",
)
ParcellationEntity.whss_datlas_medial_superior_olive = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medialSuperiorOlive",
    alternate_names=["MSO"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_medialSuperiorOlive"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_medialSuperiorOlive"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_medialSuperiorOlive"},
    ],
    lookup_label="WHSSDatlas_medialSuperiorOlive",
    name="medial superior olive",
)
ParcellationEntity.whss_datlas_mediodorsal_nucleus_of_the_dorsal_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mediodorsalNucleusOfTheDorsalThalamus",
    alternate_names=["MD"],
    lookup_label="WHSSDatlas_mediodorsalNucleusOfTheDorsalThalamus",
    name="mediodorsal nucleus of the dorsal thalamus",
)
ParcellationEntity.whss_datlas_mediodorsal_thalamic_nucleus_central_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mediodorsalThalamicNucleusCentralPart",
    alternate_names=["MD-c"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_mediodorsalThalamicNucleusCentralPart"
        }
    ],
    lookup_label="WHSSDatlas_mediodorsalThalamicNucleusCentralPart",
    name="mediodorsal thalamic nucleus, central part",
)
ParcellationEntity.whss_datlas_mediodorsal_thalamic_nucleus_lateral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mediodorsalThalamicNucleusLateralPart",
    alternate_names=["MD-l"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_mediodorsalThalamicNucleusLateralPart"
        }
    ],
    lookup_label="WHSSDatlas_mediodorsalThalamicNucleusLateralPart",
    name="mediodorsal thalamic nucleus, lateral part",
)
ParcellationEntity.whss_datlas_mediodorsal_thalamic_nucleus_medial_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mediodorsalThalamicNucleusMedialPart",
    alternate_names=["MD-m"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_mediodorsalThalamicNucleusMedialPart"
        }
    ],
    lookup_label="WHSSDatlas_mediodorsalThalamicNucleusMedialPart",
    name="mediodorsal thalamic nucleus, medial part",
)
ParcellationEntity.whss_datlas_mediofrontal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mediofrontalCortex",
    alternate_names=["MFC"],
    lookup_label="WHSSDatlas_mediofrontalCortex",
    name="mediofrontal cortex",
)
ParcellationEntity.whss_datlas_medulla_oblongata = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_medullaOblongata",
    alternate_names=["MOb"],
    lookup_label="WHSSDatlas_medullaOblongata",
    name="medulla oblongata",
)
ParcellationEntity.whss_datlas_mesencephalon = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_mesencephalon",
    alternate_names=["Mes"],
    lookup_label="WHSSDatlas_mesencephalon",
    name="mesencephalon",
)
ParcellationEntity.whss_datlas_metencephalon = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_metencephalon",
    alternate_names=["Met"],
    lookup_label="WHSSDatlas_metencephalon",
    name="metencephalon",
)
ParcellationEntity.whss_datlas_midbrain = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_midbrain",
    alternate_names=["MB"],
    lookup_label="WHSSDatlas_midbrain",
    name="midbrain",
)
ParcellationEntity.whss_datlas_middle_cerebellar_peduncle = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_middleCerebellarPeduncle",
    alternate_names=["mcp"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_middleCerebellarPeduncle"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_middleCerebellarPeduncle"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_middleCerebellarPeduncle"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_middleCerebellarPeduncle"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_middleCerebellarPeduncle"
        },
    ],
    lookup_label="WHSSDatlas_middleCerebellarPeduncle",
    name="middle cerebellar peduncle",
)
ParcellationEntity.whss_datlas_molecular_cell_layer_of_the_cerebellum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_molecularCellLayerOfTheCerebellum",
    alternate_names=["Cb-m"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_molecularCellLayerOfTheCerebellum"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_molecularLayerOfTheCerebellum"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_molecularLayerOfTheCerebellum"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_molecularLayerOfTheCerebellum"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_molecularCellLayerOfTheCerebellum"
        },
    ],
    lookup_label="WHSSDatlas_molecularCellLayerOfTheCerebellum",
    name="molecular cell layer of the cerebellum",
)
ParcellationEntity.whss_datlas_motor_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_motorCortex",
    alternate_names=["M"],
    lookup_label="WHSSDatlas_motorCortex",
    name="motor cortex",
)
ParcellationEntity.whss_datlas_myelencephalon = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_myelencephalon",
    alternate_names=["Myel"],
    lookup_label="WHSSDatlas_myelencephalon",
    name="myelencephalon",
)
ParcellationEntity.whss_datlas_neocortex_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_neocortexUnspecified",
    alternate_names=["Ncx-u"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_neocortex"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_neocortex"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_neocortex"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_neocortex"},
    ],
    lookup_label="WHSSDatlas_neocortexUnspecified",
    name="neocortex, unspecified",
)
ParcellationEntity.whss_datlas_nonlaminated_pallium = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nonlaminatedPallium",
    alternate_names=["N-LamP"],
    lookup_label="WHSSDatlas_nonlaminatedPallium",
    name="non-laminated pallium",
)
ParcellationEntity.whss_datlas_nuclei_of_the_lateral_lemniscus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleiOfTheLateralLemniscus",
    alternate_names=["NLL"],
    lookup_label="WHSSDatlas_nucleiOfTheLateralLemniscus",
    name="nuclei of the lateral lemniscus",
)
ParcellationEntity.whss_datlas_nucleus_accumbens = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusAccumbens",
    alternate_names=["NAc"],
    lookup_label="WHSSDatlas_nucleusAccumbens",
    name="nucleus accumbens",
)
ParcellationEntity.whss_datlas_nucleus_accumbens_core = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusAccumbensCore",
    alternate_names=["NAc-c"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_nucleusAccumbensCore"}
    ],
    lookup_label="WHSSDatlas_nucleusAccumbensCore",
    name="nucleus accumbens, core",
)
ParcellationEntity.whss_datlas_nucleus_accumbens_shell = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusAccumbensShell",
    alternate_names=["NAc-sh"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_nucleusAccumbensShell"}
    ],
    lookup_label="WHSSDatlas_nucleusAccumbensShell",
    name="nucleus accumbens, shell",
)
ParcellationEntity.whss_datlas_nucleus_of_the_lateral_olfactory_tract = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusOfTheLateralOlfactoryTract",
    alternate_names=["NLOT"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_nucleusOfTheLateralOlfactoryTract"
        }
    ],
    lookup_label="WHSSDatlas_nucleusOfTheLateralOlfactoryTract",
    name="nucleus of the lateral olfactory tract",
)
ParcellationEntity.whss_datlas_nucleus_of_the_stria_medullaris = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusOfTheStriaMedullaris",
    alternate_names=["SMn"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_nucleusOfTheStriaMedullaris"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_nucleusOfTheStriaMedullaris"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_nucleusOfTheStriaMedullaris"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_nucleusOfTheStriaMedullaris"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_nucleusOfTheStriaMedullaris"
        },
    ],
    lookup_label="WHSSDatlas_nucleusOfTheStriaMedullaris",
    name="nucleus of the stria medullaris",
)
ParcellationEntity.whss_datlas_nucleus_of_the_trapezoid_body = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusOfTheTrapezoidBody",
    alternate_names=["NTB"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_nucleusOfTheTrapezoidBody"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_nucleusOfTheTrapezoidBody"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_nucleusOfTheTrapezoidBody"
        },
    ],
    lookup_label="WHSSDatlas_nucleusOfTheTrapezoidBody",
    name="nucleus of the trapezoid body",
)
ParcellationEntity.whss_datlas_nucleus_sagulum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_nucleusSagulum",
    alternate_names=["Sag"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_nucleusSagulum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_nucleusSagulum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_nucleusSagulum"},
    ],
    lookup_label="WHSSDatlas_nucleusSagulum",
    name="nucleus sagulum",
)
ParcellationEntity.whss_datlas_occipital_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_occipitalRegion",
    alternate_names=["Oc"],
    lookup_label="WHSSDatlas_occipitalRegion",
    name="occipital region",
)
ParcellationEntity.whss_datlas_olfactory_bulb = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_olfactoryBulb",
    alternate_names=["OB", "olfactory system", "olfactory areas"],
    lookup_label="WHSSDatlas_olfactoryBulb",
    name="olfactory bulb",
)
ParcellationEntity.whss_datlas_olfactory_bulb_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_olfactoryBulbUnspecified",
    alternate_names=["OB-u"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_olfactoryBulb"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_olfactoryBulb"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_olfactoryBulb"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_olfactoryBulb"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_olfactoryBulbUnspecified"
        },
    ],
    lookup_label="WHSSDatlas_olfactoryBulbUnspecified",
    name="olfactory bulb, unspecified",
)
ParcellationEntity.whss_datlas_olfactory_white_matter = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_olfactoryWhiteMatter",
    alternate_names=["olf"],
    lookup_label="WHSSDatlas_olfactoryWhiteMatter",
    name="olfactory white matter",
)
ParcellationEntity.whss_datlas_optic_fiber_system_and_supraoptic_decussation = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_opticFiberSystemAndSupraopticDecussation",
    alternate_names=["ofs"],
    lookup_label="WHSSDatlas_opticFiberSystemAndSupraopticDecussation",
    name="optic fiber system and supraoptic decussation",
)
ParcellationEntity.whss_datlas_optic_nerve = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_opticNerve",
    alternate_names=["2n"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_opticNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_opticNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_opticNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_opticNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_opticNerve"},
    ],
    lookup_label="WHSSDatlas_opticNerve",
    name="optic nerve",
)
ParcellationEntity.whss_datlas_optic_tract_and_optic_chiasm = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_opticTractAndOpticChiasm",
    alternate_names=["opt-och"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_opticTractAndOpticChiasm"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_opticTractAndOpticChiasm"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_opticTractAndOpticChiasm"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_opticTractAndOpticChiasm"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_opticTractAndOpticChiasm"
        },
    ],
    lookup_label="WHSSDatlas_opticTractAndOpticChiasm",
    name="optic tract and optic chiasm",
)
ParcellationEntity.whss_datlas_orbitofrontal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_orbitofrontalCortex",
    alternate_names=["Orb"],
    lookup_label="WHSSDatlas_orbitofrontalCortex",
    name="orbitofrontal cortex",
)
ParcellationEntity.whss_datlas_pallidum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pallidum",
    alternate_names=["PAL"],
    lookup_label="WHSSDatlas_pallidum",
    name="pallidum",
)
ParcellationEntity.whss_datlas_paracentral_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_paracentralThalamicNucleus",
    alternate_names=["PCN"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_paracentralThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_paracentralThalamicNucleus",
    name="paracentral thalamic nucleus",
)
ParcellationEntity.whss_datlas_parafascicular_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parafascicularThalamicNucleus",
    alternate_names=["PF"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_parafascicularThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_parafascicularThalamicNucleus",
    name="parafascicular thalamic nucleus",
)
ParcellationEntity.whss_datlas_parahippocampal_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parahippocampalRegion",
    alternate_names=["PHR"],
    lookup_label="WHSSDatlas_parahippocampalRegion",
    name="parahippocampal region",
)
ParcellationEntity.whss_datlas_parasubiculum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parasubiculum",
    alternate_names=["PaS"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_parasubiculum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_parasubiculum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_parasubiculum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_parasubiculum"},
    ],
    lookup_label="WHSSDatlas_parasubiculum",
    name="parasubiculum",
)
ParcellationEntity.whss_datlas_parataenial_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parataenialThalamicNucleus",
    alternate_names=["PT"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_parataenialThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_parataenialThalamicNucleus",
    name="parataenial thalamic nucleus",
)
ParcellationEntity.whss_datlas_paraventricular_thalamic_nuclei_anterior_and_posterior = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_paraventricularThalamicNucleiAnteriorAndPosterior",
    alternate_names=["PV"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_paraventricularThalamicNucleiAnteriorAndPosterior"
        }
    ],
    lookup_label="WHSSDatlas_paraventricularThalamicNucleiAnteriorAndPosterior",
    name="paraventricular thalamic nuclei (anterior and posterior)",
)
ParcellationEntity.whss_datlas_parietal_association_cortex_lateral_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parietalAssociationCortexLateralArea",
    alternate_names=["lPPC"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_parietalAssociationCortexLateralArea"
        }
    ],
    lookup_label="WHSSDatlas_parietalAssociationCortexLateralArea",
    name="parietal association cortex, lateral area",
)
ParcellationEntity.whss_datlas_parietal_association_cortex_medial_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parietalAssociationCortexMedialArea",
    alternate_names=["mPPC"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_parietalAssociationCortexMedialArea"
        }
    ],
    lookup_label="WHSSDatlas_parietalAssociationCortexMedialArea",
    name="parietal association cortex, medial area",
)
ParcellationEntity.whss_datlas_parietal_association_cortex_posterior_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parietalAssociationCortexPosteriorArea",
    alternate_names=["PtP"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_parietalAssociationCortexPosteriorArea"
        }
    ],
    lookup_label="WHSSDatlas_parietalAssociationCortexPosteriorArea",
    name="parietal association cortex, posterior area",
)
ParcellationEntity.whss_datlas_parietal_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_parietalRegion",
    alternate_names=["Par"],
    lookup_label="WHSSDatlas_parietalRegion",
    name="parietal region",
)
ParcellationEntity.whss_datlas_periaqueductal_gray = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_periaqueductalGray",
    alternate_names=["PAG"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_periaqueductalGray"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_periaqueductalGray"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_periaqueductalGray"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_periaqueductalGray"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_periaqueductalGray"},
    ],
    lookup_label="WHSSDatlas_periaqueductalGray",
    name="periaqueductal gray",
)
ParcellationEntity.whss_datlas_peripeduncular_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_peripeduncularNucleus",
    alternate_names=["PP"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_peripeduncularNucleus"}
    ],
    lookup_label="WHSSDatlas_peripeduncularNucleus",
    name="peripeduncular nucleus",
)
ParcellationEntity.whss_datlas_perirhinal_area35 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_perirhinalArea35",
    alternate_names=["PER35"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_perirhinalArea35"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_perirhinalArea35"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_perirhinalArea35"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_perirhinalArea35"},
    ],
    lookup_label="WHSSDatlas_perirhinalArea35",
    name="perirhinal area 35",
)
ParcellationEntity.whss_datlas_perirhinal_area36 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_perirhinalArea36",
    alternate_names=["PER36"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_perirhinalArea36"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_perirhinalArea36"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_perirhinalArea36"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_perirhinalArea36"},
    ],
    lookup_label="WHSSDatlas_perirhinalArea36",
    name="perirhinal area 36",
)
ParcellationEntity.whss_datlas_perirhinal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_perirhinalCortex",
    alternate_names=["PER"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_perirhinalCortex"}
    ],
    lookup_label="WHSSDatlas_perirhinalCortex",
    name="perirhinal cortex",
)
ParcellationEntity.whss_datlas_periventricular_gray = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_periventricularGray",
    alternate_names=["PVG"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_periventricularGray"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_periventricularGray"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_periventricularGray"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_periventricularGray"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_periventricularGray"},
    ],
    lookup_label="WHSSDatlas_periventricularGray",
    name="periventricular gray",
)
ParcellationEntity.whss_datlas_pineal_gland = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pinealGland",
    alternate_names=["PG"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_pinealGland"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_pinealGland"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_pinealGland"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_pinealGland"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_pinealGland"},
    ],
    lookup_label="WHSSDatlas_pinealGland",
    name="pineal gland",
)
ParcellationEntity.whss_datlas_piriform_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_piriformCortex",
    alternate_names=["PIR"],
    lookup_label="WHSSDatlas_piriformCortex",
    name="piriform cortex",
)
ParcellationEntity.whss_datlas_piriform_cortex_layer1 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_piriformCortexLayer1",
    alternate_names=["PIR1"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_piriformCortexLayer1"}
    ],
    lookup_label="WHSSDatlas_piriformCortexLayer1",
    name="piriform cortex, layer 1",
)
ParcellationEntity.whss_datlas_piriform_cortex_layer2 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_piriformCortexLayer2",
    alternate_names=["PIR2"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_piriformCortexLayer2"}
    ],
    lookup_label="WHSSDatlas_piriformCortexLayer2",
    name="piriform cortex, layer 2",
)
ParcellationEntity.whss_datlas_piriform_cortex_layer3 = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_piriformCortexLayer3",
    alternate_names=["PIR3"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_piriformCortexLayer3"}
    ],
    lookup_label="WHSSDatlas_piriformCortexLayer3",
    name="piriform cortex, layer 3",
)
ParcellationEntity.whss_datlas_pons = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pons",
    alternate_names=["P"],
    lookup_label="WHSSDatlas_pons",
    name="pons",
)
ParcellationEntity.whss_datlas_pontine_nuclei = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pontineNuclei",
    alternate_names=["Pn"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_pontineNuclei"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_pontineNuclei"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_pontineNuclei"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_pontineNuclei"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_pontineNuclei"},
    ],
    lookup_label="WHSSDatlas_pontineNuclei",
    name="pontine nuclei",
)
ParcellationEntity.whss_datlas_posterior_commissure = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorCommissure",
    alternate_names=["pc"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_posteriorCommissure"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_posteriorCommissure"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_posteriorCommissure"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_posteriorCommissure"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_posteriorCommissure"},
    ],
    lookup_label="WHSSDatlas_posteriorCommissure",
    name="posterior commissure",
)
ParcellationEntity.whss_datlas_posterior_complex_of_the_dorsal_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorComplexOfTheDorsalThalamus",
    alternate_names=["PoC"],
    lookup_label="WHSSDatlas_posteriorComplexOfTheDorsalThalamus",
    name="posterior complex of the dorsal thalamus",
)
ParcellationEntity.whss_datlas_posterior_intralaminar_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorIntralaminarNucleus",
    alternate_names=["PIL"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_posteriorIntralaminarNucleus"
        }
    ],
    lookup_label="WHSSDatlas_posteriorIntralaminarNucleus",
    name="posterior intralaminar nucleus",
)
ParcellationEntity.whss_datlas_posterior_parietal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorParietalCortex",
    alternate_names=["PPC"],
    lookup_label="WHSSDatlas_posteriorParietalCortex",
    name="posterior parietal cortex",
)
ParcellationEntity.whss_datlas_posterior_thalamic_nuclear_group_triangular_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorThalamicNuclearGroupTriangularPart",
    alternate_names=["Po-t"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_posteriorThalamicNuclearGroupTriangularPart"
        }
    ],
    lookup_label="WHSSDatlas_posteriorThalamicNuclearGroupTriangularPart",
    name="posterior thalamic nuclear group, triangular part",
)
ParcellationEntity.whss_datlas_posterior_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_posteriorThalamicNucleus",
    alternate_names=["Po"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_posteriorThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_posteriorThalamicNucleus",
    name="posterior thalamic nucleus",
)
ParcellationEntity.whss_datlas_postrhinal_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_postrhinalCortex",
    alternate_names=["POR"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_postrhinalCortex"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_postrhinalCortex"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_postrhinalCortex"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_postrhinalCortex"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_postrhinalCortex"},
    ],
    lookup_label="WHSSDatlas_postrhinalCortex",
    name="postrhinal cortex",
)
ParcellationEntity.whss_datlas_pregeniculate_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pregeniculateNucleus",
    alternate_names=["PrG"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_pregeniculateNucleus"}
    ],
    lookup_label="WHSSDatlas_pregeniculateNucleus",
    name="pregeniculate nucleus",
)
ParcellationEntity.whss_datlas_prelimbic_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_prelimbicArea",
    alternate_names=["PrL"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_prelimbicArea"}
    ],
    lookup_label="WHSSDatlas_prelimbicArea",
    name="prelimbic area",
)
ParcellationEntity.whss_datlas_presubiculum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_presubiculum",
    alternate_names=["PrS"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_presubiculum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_presubiculum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_presubiculum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_presubiculum"},
    ],
    lookup_label="WHSSDatlas_presubiculum",
    name="presubiculum",
)
ParcellationEntity.whss_datlas_pretectal_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pretectalRegion",
    alternate_names=["PRT"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_pretectalRegion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_pretectalRegion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_pretectalRegion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_pretectalRegion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_pretectalRegion"},
    ],
    lookup_label="WHSSDatlas_pretectalRegion",
    name="pretectal region",
)
ParcellationEntity.whss_datlas_pretectothalamic_lamina = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pretectothalamicLamina",
    alternate_names=["ptl"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_pretectothalamicLamina"
        }
    ],
    lookup_label="WHSSDatlas_pretectothalamicLamina",
    name="pretectothalamic lamina",
)
ParcellationEntity.whss_datlas_pretectum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pretectum",
    alternate_names=["PreT"],
    lookup_label="WHSSDatlas_pretectum",
    name="pretectum",
)
ParcellationEntity.whss_datlas_prethalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_prethalamus",
    alternate_names=["Thal-Pre"],
    lookup_label="WHSSDatlas_prethalamus",
    name="prethalamus",
)
ParcellationEntity.whss_datlas_primary_auditory_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primaryAuditoryArea",
    alternate_names=["Au1"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_primaryAuditoryCortex"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_primaryAuditoryCortex"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_primaryAuditoryArea"},
    ],
    lookup_label="WHSSDatlas_primaryAuditoryArea",
    name="primary auditory area",
)
ParcellationEntity.whss_datlas_primary_motor_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primaryMotorArea",
    alternate_names=["M1"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_primaryMotorArea"}
    ],
    lookup_label="WHSSDatlas_primaryMotorArea",
    name="primary motor area",
)
ParcellationEntity.whss_datlas_primary_somatosensory_area_barrel_field = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaBarrelField",
    alternate_names=["S1-bf"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_primarySomatosensoryAreaBarrelField"
        }
    ],
    lookup_label="WHSSDatlas_primarySomatosensoryAreaBarrelField",
    name="primary somatosensory area, barrel field",
)
ParcellationEntity.whss_datlas_primary_somatosensory_area_dysgranular_zone = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaDysgranularZone",
    alternate_names=["S1-dz"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_primarySomatosensoryAreaDysgranularZone"
        }
    ],
    lookup_label="WHSSDatlas_primarySomatosensoryAreaDysgranularZone",
    name="primary somatosensory area, dysgranular zone",
)
ParcellationEntity.whss_datlas_primary_somatosensory_area_face_representation = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaFaceRepresentation",
    alternate_names=["S1-f"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_primarySomatosensoryAreaFaceRepresentation"
        }
    ],
    lookup_label="WHSSDatlas_primarySomatosensoryAreaFaceRepresentation",
    name="primary somatosensory area, face representation",
)
ParcellationEntity.whss_datlas_primary_somatosensory_area_forelimb_representation = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaForelimbRepresentation",
    alternate_names=["S1-fl"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_primarySomatosensoryAreaForelimbRepresentation"
        }
    ],
    lookup_label="WHSSDatlas_primarySomatosensoryAreaForelimbRepresentation",
    name="primary somatosensory area, forelimb representation",
)
ParcellationEntity.whss_datlas_primary_somatosensory_area_hindlimb_representation = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaHindlimbRepresentation",
    alternate_names=["S1-hl"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_primarySomatosensoryAreaHindlimbRepresentation"
        }
    ],
    lookup_label="WHSSDatlas_primarySomatosensoryAreaHindlimbRepresentation",
    name="primary somatosensory area, hindlimb representation",
)
ParcellationEntity.whss_datlas_primary_somatosensory_area_trunk_representation = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryAreaTrunkRepresentation",
    alternate_names=["S1-tr"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_primarySomatosensoryAreaTrunkRepresentation"
        }
    ],
    lookup_label="WHSSDatlas_primarySomatosensoryAreaTrunkRepresentation",
    name="primary somatosensory area, trunk representation",
)
ParcellationEntity.whss_datlas_primary_somatosensory_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primarySomatosensoryCortex",
    alternate_names=["S1"],
    lookup_label="WHSSDatlas_primarySomatosensoryCortex",
    name="primary somatosensory cortex",
)
ParcellationEntity.whss_datlas_primary_visual_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_primaryVisualArea",
    alternate_names=["V1"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_primaryVisualArea"}
    ],
    lookup_label="WHSSDatlas_primaryVisualArea",
    name="primary visual area",
)
ParcellationEntity.whss_datlas_pyramidal_decussation = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_pyramidalDecussation",
    alternate_names=["pyx"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_pyramidalDecussation"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_pyramidalDecussation"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_pyramidalDecussation"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_pyramidalDecussation"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_pyramidalDecussation"},
    ],
    lookup_label="WHSSDatlas_pyramidalDecussation",
    name="pyramidal decussation",
)
ParcellationEntity.whss_datlas_reticular_prethalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_reticularPrethalamicNucleus",
    alternate_names=["RT", "reticular nucleus of the thalamus"],
    lookup_label="WHSSDatlas_reticularPrethalamicNucleus",
    name="reticular (pre)thalamic nucleus",
)
ParcellationEntity.whss_datlas_reticular_prethalamic_nucleus_auditory_segment = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_reticularPrethalamicNucleusAuditorySegment",
    alternate_names=["RT-a", "reticular thalamic nucleus, auditory segment"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_reticularThalamicNucleusAuditorySegment"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_reticularThalamicNucleusAuditorySegment"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_reticularPrethalamicNucleusAuditorySegment"
        },
    ],
    lookup_label="WHSSDatlas_reticularPrethalamicNucleusAuditorySegment",
    name="reticular (pre)thalamic nucleus, auditory segment",
)
ParcellationEntity.whss_datlas_reticular_prethalamic_nucleus_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_reticularPrethalamicNucleusUnspecified",
    alternate_names=["RT-u"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_reticularPrethalamicNucleusUnspecified"
        }
    ],
    lookup_label="WHSSDatlas_reticularPrethalamicNucleusUnspecified",
    name="reticular (pre)thalamic nucleus, unspecified",
)
ParcellationEntity.whss_datlas_retroreuniens_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_retroreuniensThalamicNucleus",
    alternate_names=["RRe"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_retroreuniensThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_retroreuniensThalamicNucleus",
    name="retroreuniens thalamic nucleus",
)
ParcellationEntity.whss_datlas_retrosplenial_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_retrosplenialCortex",
    alternate_names=["RS"],
    lookup_label="WHSSDatlas_retrosplenialCortex",
    name="retrosplenial cortex",
)
ParcellationEntity.whss_datlas_retrosplenial_dysgranular_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_retrosplenialDysgranularArea",
    alternate_names=["RSD"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_retrosplenialDysgranularArea"
        }
    ],
    lookup_label="WHSSDatlas_retrosplenialDysgranularArea",
    name="retrosplenial dysgranular area",
)
ParcellationEntity.whss_datlas_retrosplenial_granular_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_retrosplenialGranularArea",
    alternate_names=["RSG"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_retrosplenialGranularArea"
        }
    ],
    lookup_label="WHSSDatlas_retrosplenialGranularArea",
    name="retrosplenial granular area",
)
ParcellationEntity.whss_datlas_reuniens_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_reuniensThalamicNucleus",
    alternate_names=["Re"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_reuniensThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_reuniensThalamicNucleus",
    name="reuniens thalamic nucleus",
)
ParcellationEntity.whss_datlas_rhombencephalon = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_rhombencephalon",
    alternate_names=["Rho"],
    lookup_label="WHSSDatlas_rhombencephalon",
    name="rhombencephalon",
)
ParcellationEntity.whss_datlas_rhomboid_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_rhomboidThalamicNucleus",
    alternate_names=["Rh"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_rhomboidThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_rhomboidThalamicNucleus",
    name="rhomboid thalamic nucleus",
)
ParcellationEntity.whss_datlas_secondary_auditory_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryAuditoryArea",
    alternate_names=["Au2"],
    lookup_label="WHSSDatlas_secondaryAuditoryArea",
    name="secondary auditory area",
)
ParcellationEntity.whss_datlas_secondary_auditory_area_dorsal_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryAuditoryAreaDorsalPart",
    alternate_names=["Au2-d"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_secondaryAuditoryCortexDorsalArea"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_secondaryAuditoryCortexDorsalArea"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_secondaryAuditoryAreaDorsalPart"
        },
    ],
    lookup_label="WHSSDatlas_secondaryAuditoryAreaDorsalPart",
    name="secondary auditory area, dorsal part",
)
ParcellationEntity.whss_datlas_secondary_auditory_area_ventral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryAuditoryAreaVentralPart",
    alternate_names=["Au2-v"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_secondaryAuditoryCortexVentralArea"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_secondaryAuditoryCortexVentralArea"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_secondaryAuditoryAreaVentralPart"
        },
    ],
    lookup_label="WHSSDatlas_secondaryAuditoryAreaVentralPart",
    name="secondary auditory area, ventral part",
)
ParcellationEntity.whss_datlas_secondary_motor_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryMotorArea",
    alternate_names=["M2"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_secondaryMotorArea"}
    ],
    lookup_label="WHSSDatlas_secondaryMotorArea",
    name="secondary motor area",
)
ParcellationEntity.whss_datlas_secondary_somatosensory_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondarySomatosensoryArea",
    alternate_names=["S2"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_secondarySomatosensoryArea"
        }
    ],
    lookup_label="WHSSDatlas_secondarySomatosensoryArea",
    name="secondary somatosensory area",
)
ParcellationEntity.whss_datlas_secondary_visual_area_lateral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryVisualAreaLateralPart",
    alternate_names=["V2L"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_secondaryVisualAreaLateralPart"
        }
    ],
    lookup_label="WHSSDatlas_secondaryVisualAreaLateralPart",
    name="secondary visual area, lateral part",
)
ParcellationEntity.whss_datlas_secondary_visual_area_medial_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryVisualAreaMedialPart",
    alternate_names=["V2M"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_secondaryVisualAreaMedialPart"
        }
    ],
    lookup_label="WHSSDatlas_secondaryVisualAreaMedialPart",
    name="secondary visual area, medial part",
)
ParcellationEntity.whss_datlas_secondary_visual_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_secondaryVisualCortex",
    alternate_names=["V2"],
    lookup_label="WHSSDatlas_secondaryVisualCortex",
    name="secondary visual cortex",
)
ParcellationEntity.whss_datlas_septal_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_septalRegion",
    alternate_names=["Sep"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_septalRegion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_septalRegion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_septalRegion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_septalRegion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_septalRegion"},
    ],
    lookup_label="WHSSDatlas_septalRegion",
    name="septal region",
)
ParcellationEntity.whss_datlas_somatosensory_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_somatosensoryCortex",
    alternate_names=["SS"],
    lookup_label="WHSSDatlas_somatosensoryCortex",
    name="somatosensory cortex",
)
ParcellationEntity.whss_datlas_spinal_cord = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_spinalCord",
    alternate_names=["SpC"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_spinalCord"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_spinalCord"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_spinalCord"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_spinalCord"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_spinalCord"},
    ],
    lookup_label="WHSSDatlas_spinalCord",
    name="spinal cord",
)
ParcellationEntity.whss_datlas_spinal_trigeminal_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_spinalTrigeminalNucleus",
    alternate_names=["Sp5n"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_spinalTrigeminalNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_spinalTrigeminalNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_spinalTrigeminalNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_spinalTrigeminalNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_spinalTrigeminalNucleus"
        },
    ],
    lookup_label="WHSSDatlas_spinalTrigeminalNucleus",
    name="spinal trigeminal nucleus",
)
ParcellationEntity.whss_datlas_spinal_trigeminal_tract = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_spinalTrigeminalTract",
    alternate_names=["sp5t"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_spinalTrigeminalTract"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_spinalTrigeminalTract"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_spinalTrigeminalTract"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_spinalTrigeminalTract"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_spinalTrigeminalTract"
        },
    ],
    lookup_label="WHSSDatlas_spinalTrigeminalTract",
    name="spinal trigeminal tract",
)
ParcellationEntity.whss_datlas_spiral_ganglion = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_spiralGanglion",
    alternate_names=["SpG"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_spiralGanglion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_spiralGanglion"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_spiralGanglion"},
    ],
    lookup_label="WHSSDatlas_spiralGanglion",
    name="spiral ganglion",
)
ParcellationEntity.whss_datlas_stria_medullaris_thalami = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_striaMedullarisThalami",
    alternate_names=["sm", "stria medullaris of the thalamus"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_striaMedullarisOfTheThalamus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_striaMedullarisOfTheThalamus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_striaMedullarisOfTheThalamus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_striaMedullarisOfTheThalamus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_striaMedullarisThalami"
        },
    ],
    lookup_label="WHSSDatlas_striaMedullarisThalami",
    name="stria medullaris thalami",
)
ParcellationEntity.whss_datlas_stria_terminalis = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_striaTerminalis",
    alternate_names=["st"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_striaTerminalis"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_striaTerminalis"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_striaTerminalis"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_striaTerminalis"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_striaTerminalis"},
    ],
    lookup_label="WHSSDatlas_striaTerminalis",
    name="stria terminalis",
)
ParcellationEntity.whss_datlas_striatum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_striatum",
    alternate_names=["Str"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_striatum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_striatum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_striatum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_striatum"},
    ],
    lookup_label="WHSSDatlas_striatum",
    name="striatum",
)
ParcellationEntity.whss_datlas_subgeniculate_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_subgeniculateNucleus",
    alternate_names=["SubG"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_subgeniculateNucleus"}
    ],
    lookup_label="WHSSDatlas_subgeniculateNucleus",
    name="subgeniculate nucleus",
)
ParcellationEntity.whss_datlas_subiculum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_subiculum",
    alternate_names=["SUB"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_subiculum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_subiculum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_subiculum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_subiculum"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_subiculum"},
    ],
    lookup_label="WHSSDatlas_subiculum",
    name="subiculum",
)
ParcellationEntity.whss_datlas_submedius_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_submediusThalamicNucleus",
    alternate_names=["SMT"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_submediusThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_submediusThalamicNucleus",
    name="submedius thalamic nucleus",
)
ParcellationEntity.whss_datlas_subpallium = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_subpallium",
    alternate_names=["SubPAL"],
    lookup_label="WHSSDatlas_subpallium",
    name="subpallium",
)
ParcellationEntity.whss_datlas_subparafascicular_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_subparafascicularNucleus",
    alternate_names=["SPF"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_subparafascicularNucleus"
        }
    ],
    lookup_label="WHSSDatlas_subparafascicularNucleus",
    name="subparafascicular nucleus",
)
ParcellationEntity.whss_datlas_substantia_nigra = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_substantiaNigra",
    alternate_names=["SN"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_substantiaNigra"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_substantiaNigra"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_substantiaNigra"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_substantiaNigra"},
    ],
    lookup_label="WHSSDatlas_substantiaNigra",
    name="substantia nigra",
)
ParcellationEntity.whss_datlas_substantia_nigra_compact_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_substantiaNigraCompactPart",
    alternate_names=["SN-c"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_substantiaNigraCompactPart"
        }
    ],
    lookup_label="WHSSDatlas_substantiaNigraCompactPart",
    name="substantia nigra, compact part",
)
ParcellationEntity.whss_datlas_substantia_nigra_lateral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_substantiaNigraLateralPart",
    alternate_names=["SN-l"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_substantiaNigraLateralPart"
        }
    ],
    lookup_label="WHSSDatlas_substantiaNigraLateralPart",
    name="substantia nigra, lateral part",
)
ParcellationEntity.whss_datlas_substantia_nigra_reticular_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_substantiaNigraReticularPart",
    alternate_names=["SN-r"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_substantiaNigraReticularPart"
        }
    ],
    lookup_label="WHSSDatlas_substantiaNigraReticularPart",
    name="substantia nigra, reticular part",
)
ParcellationEntity.whss_datlas_subthalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_subthalamicNucleus",
    alternate_names=["STh"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_subthalamicNucleus"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_subthalamicNucleus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_subthalamicNucleus"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_subthalamicNucleus"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_subthalamicNucleus"},
    ],
    lookup_label="WHSSDatlas_subthalamicNucleus",
    name="subthalamic nucleus",
)
ParcellationEntity.whss_datlas_superficial_gray_layer_of_the_superior_colliculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superficialGrayLayerOfTheSuperiorColliculus",
    alternate_names=["SuG"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_superficialGrayLayerOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_superficialGrayLayerOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_superficialGrayLayerOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_superficialGrayLayerOfTheSuperiorColliculus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_superficialGrayLayerOfTheSuperiorColliculus"
        },
    ],
    lookup_label="WHSSDatlas_superficialGrayLayerOfTheSuperiorColliculus",
    name="superficial gray layer of the superior colliculus",
)
ParcellationEntity.whss_datlas_superior_cerebellar_peduncle_and_prerubral_field = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superiorCerebellarPeduncleAndPrerubralField",
    alternate_names=["scp-pr"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_superiorCerebellarPeduncleAndPrerubralField"
        }
    ],
    lookup_label="WHSSDatlas_superiorCerebellarPeduncleAndPrerubralField",
    name="superior cerebellar peduncle and prerubral field",
)
ParcellationEntity.whss_datlas_superior_colliculus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superiorColliculus",
    alternate_names=["Su"],
    lookup_label="WHSSDatlas_superiorColliculus",
    name="superior colliculus",
)
ParcellationEntity.whss_datlas_superior_olivary_complex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superiorOlivaryComplex",
    alternate_names=["SO"],
    lookup_label="WHSSDatlas_superiorOlivaryComplex",
    name="superior olivary complex",
)
ParcellationEntity.whss_datlas_superior_paraolivary_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superiorParaolivaryNucleus",
    alternate_names=["SPN"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_superiorParaolivaryNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_superiorParaolivaryNucleus"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_superiorParaolivaryNucleus"
        },
    ],
    lookup_label="WHSSDatlas_superiorParaolivaryNucleus",
    name="superior paraolivary nucleus",
)
ParcellationEntity.whss_datlas_superior_periolivary_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_superiorPeriolivaryRegion",
    alternate_names=["SPR"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_superiorPeriolivaryRegion"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_superiorPeriolivaryRegion"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_superiorPeriolivaryRegion"
        },
    ],
    lookup_label="WHSSDatlas_superiorPeriolivaryRegion",
    name="superior periolivary region",
)
ParcellationEntity.whss_datlas_supraoptic_decussation = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_supraopticDecussation",
    alternate_names=["sox"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_supraopticDecussation"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_supraopticDecussation"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_supraopticDecussation"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_supraopticDecussation"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_supraopticDecussation"
        },
    ],
    lookup_label="WHSSDatlas_supraopticDecussation",
    name="supraoptic decussation",
)
ParcellationEntity.whss_datlas_tectum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_tectum",
    alternate_names=["Tc"],
    lookup_label="WHSSDatlas_tectum",
    name="tectum",
)
ParcellationEntity.whss_datlas_tegmentum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_tegmentum",
    alternate_names=["Tg"],
    lookup_label="WHSSDatlas_tegmentum",
    name="tegmentum",
)
ParcellationEntity.whss_datlas_telencephalon = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_telencephalon",
    alternate_names=["medial "],
    lookup_label="WHSSDatlas_telencephalon",
    name="telencephalon",
)
ParcellationEntity.whss_datlas_temporal_association_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_temporalAssociationCortex",
    alternate_names=["TeA"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_temporalAssociationCortex"
        }
    ],
    lookup_label="WHSSDatlas_temporalAssociationCortex",
    name="temporal association cortex",
)
ParcellationEntity.whss_datlas_temporal_region = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_temporalRegion",
    alternate_names=["Te"],
    lookup_label="WHSSDatlas_temporalRegion",
    name="temporal region",
)
ParcellationEntity.whss_datlas_thalamic_tracts = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_thalamicTracts",
    alternate_names=["tht"],
    lookup_label="WHSSDatlas_thalamicTracts",
    name="thalamic tracts",
)
ParcellationEntity.whss_datlas_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_thalamus",
    alternate_names=["Thal"],
    lookup_label="WHSSDatlas_thalamus",
    name="thalamus",
)
ParcellationEntity.whss_datlas_thalamus_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_thalamusUnspecified",
    alternate_names=["Thal-u"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_thalamus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_thalamus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_thalamus"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_thalamus"},
    ],
    lookup_label="WHSSDatlas_thalamusUnspecified",
    name="thalamus, unspecified",
)
ParcellationEntity.whss_datlas_transverse_fibers_of_the_pons = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_transverseFibersOfThePons",
    alternate_names=["tfp"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_transverseFibersOfThePons"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_transverseFibersOfThePons"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_transverseFibersOfThePons"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_transverseFibersOfThePons"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_transverseFibersOfThePons"
        },
    ],
    lookup_label="WHSSDatlas_transverseFibersOfThePons",
    name="transverse fibers of the pons",
)
ParcellationEntity.whss_datlas_trapezoid_body = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_trapezoidBody",
    alternate_names=["tz"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_trapezoidBody"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_trapezoidBody"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_trapezoidBody"},
    ],
    lookup_label="WHSSDatlas_trapezoidBody",
    name="trapezoid body",
)
ParcellationEntity.whss_datlas_ventral_anterior_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralAnteriorThalamicNucleus",
    alternate_names=["VA"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralAnteriorThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_ventralAnteriorThalamicNucleus",
    name="ventral anterior thalamic nucleus",
)
ParcellationEntity.whss_datlas_ventral_cochlear_nucleus_anterior_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralCochlearNucleusAnteriorPart",
    alternate_names=["AVCN"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_ventralCochlearNucleusAnteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_ventralCochlearNucleusAnteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralCochlearNucleusAnteriorPart"
        },
    ],
    lookup_label="WHSSDatlas_ventralCochlearNucleusAnteriorPart",
    name="ventral cochlear nucleus, anterior part",
)
ParcellationEntity.whss_datlas_ventral_cochlear_nucleus_cap_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralCochlearNucleusCapArea",
    alternate_names=["Cap"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_ventralCochlearNucleusCapArea"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_ventralCochlearNucleusCapArea"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralCochlearNucleusCapArea"
        },
    ],
    lookup_label="WHSSDatlas_ventralCochlearNucleusCapArea",
    name="ventral cochlear nucleus, cap area",
)
ParcellationEntity.whss_datlas_ventral_cochlear_nucleus_granule_cell_layer = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralCochlearNucleusGranuleCellLayer",
    alternate_names=["GCL"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_ventralCochlearNucleusGranuleCellLayer"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_ventralCochlearNucleusGranuleCellLayer"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralCochlearNucleusGranuleCellLayer"
        },
    ],
    lookup_label="WHSSDatlas_ventralCochlearNucleusGranuleCellLayer",
    name="ventral cochlear nucleus, granule cell layer",
)
ParcellationEntity.whss_datlas_ventral_cochlear_nucleus_posterior_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralCochlearNucleusPosteriorPart",
    alternate_names=["PVCN"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_ventralCochlearNucleusPosteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_ventralCochlearNucleusPosteriorPart"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralCochlearNucleusPosteriorPart"
        },
    ],
    lookup_label="WHSSDatlas_ventralCochlearNucleusPosteriorPart",
    name="ventral cochlear nucleus, posterior part",
)
ParcellationEntity.whss_datlas_ventral_hippocampal_commissure = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralHippocampalCommissure",
    alternate_names=["vhc"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_ventralHippocampalCommissure"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_ventralHippocampalCommissure"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_ventralHippocampalCommissure"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_ventralHippocampalCommissure"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralHippocampalCommissure"
        },
    ],
    lookup_label="WHSSDatlas_ventralHippocampalCommissure",
    name="ventral hippocampal commissure",
)
ParcellationEntity.whss_datlas_ventral_midline_group_of_the_dorsal_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralMidlineGroupOfTheDorsalThalamus",
    alternate_names=["V-MID"],
    lookup_label="WHSSDatlas_ventralMidlineGroupOfTheDorsalThalamus",
    name="ventral midline group of the dorsal thalamus",
)
ParcellationEntity.whss_datlas_ventral_nuclei_of_the_dorsal_thalamus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralNucleiOfTheDorsalThalamus",
    alternate_names=["VENT"],
    lookup_label="WHSSDatlas_ventralNucleiOfTheDorsalThalamus",
    name="ventral nuclei of the dorsal thalamus",
)
ParcellationEntity.whss_datlas_ventral_orbital_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralOrbitalArea",
    alternate_names=["VO"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralOrbitalArea"}
    ],
    lookup_label="WHSSDatlas_ventralOrbitalArea",
    name="ventral orbital area",
)
ParcellationEntity.whss_datlas_ventral_pallidum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPallidum",
    alternate_names=["VP"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralPallidum"}
    ],
    lookup_label="WHSSDatlas_ventralPallidum",
    name="ventral pallidum",
)
ParcellationEntity.whss_datlas_ventral_periolivary_nuclei = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPeriolivaryNuclei",
    alternate_names=["VPO"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_ventralPeriolivaryNuclei"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_ventralPeriolivaryNuclei"
        },
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralPeriolivaryNuclei"
        },
    ],
    lookup_label="WHSSDatlas_ventralPeriolivaryNuclei",
    name="ventral periolivary nuclei",
)
ParcellationEntity.whss_datlas_ventral_posterior_nucleus_of_the_thalamus_parvicellular_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPosteriorNucleusOfTheThalamusParvicellularPart",
    alternate_names=["VP-pc"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralPosteriorNucleusOfTheThalamusParvicellularPart"
        }
    ],
    lookup_label="WHSSDatlas_ventralPosteriorNucleusOfTheThalamusParvicellularPart",
    name="ventral posterior nucleus of the thalamus, parvicellular part",
)
ParcellationEntity.whss_datlas_ventral_posterior_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPosteriorThalamicNucleus",
    alternate_names=["VPN"],
    lookup_label="WHSSDatlas_ventralPosteriorThalamicNucleus",
    name="ventral posterior thalamic nucleus",
)
ParcellationEntity.whss_datlas_ventral_posterolateral_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPosterolateralThalamicNucleus",
    alternate_names=["VPL"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralPosterolateralThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_ventralPosterolateralThalamicNucleus",
    name="ventral posterolateral thalamic nucleus",
)
ParcellationEntity.whss_datlas_ventral_posteromedial_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralPosteromedialThalamicNucleus",
    alternate_names=["VPM"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralPosteromedialThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_ventralPosteromedialThalamicNucleus",
    name="ventral posteromedial thalamic nucleus",
)
ParcellationEntity.whss_datlas_ventral_striatal_region_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralStriatalRegionUnspecified",
    alternate_names=["VSR-u"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralStriatalRegionUnspecified"
        }
    ],
    lookup_label="WHSSDatlas_ventralStriatalRegionUnspecified",
    name="ventral striatal region, unspecified",
)
ParcellationEntity.whss_datlas_ventral_tegmental_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralTegmentalArea",
    alternate_names=["VTA"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventralTegmentalArea"}
    ],
    lookup_label="WHSSDatlas_ventralTegmentalArea",
    name="ventral tegmental area",
)
ParcellationEntity.whss_datlas_ventralintermediate_entorhinal_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventralintermediateEntorhinalArea",
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_ventralintermediateEntorhinalArea"
        }
    ],
    lookup_label="WHSSDatlas_ventralintermediateEntorhinalArea",
    name="ventral-intermediate entorhinal area",
)
ParcellationEntity.whss_datlas_ventricular_system = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventricularSystem",
    alternate_names=["V"],
    lookup_label="WHSSDatlas_ventricularSystem",
    name="ventricular system",
)
ParcellationEntity.whss_datlas_ventricular_system_unspecified = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventricularSystemUnspecified",
    alternate_names=["V-u"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v1.01_ventricularSystem"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v2_ventricularSystem"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_ventricularSystem"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_ventricularSystem"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventricularSystemUnspecified"
        },
    ],
    lookup_label="WHSSDatlas_ventricularSystemUnspecified",
    name="ventricular system, unspecified",
)
ParcellationEntity.whss_datlas_ventrolateral_orbital_area = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventrolateralOrbitalArea",
    alternate_names=["VLO"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventrolateralOrbitalArea"
        }
    ],
    lookup_label="WHSSDatlas_ventrolateralOrbitalArea",
    name="ventrolateral orbital area",
)
ParcellationEntity.whss_datlas_ventrolateral_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventrolateralThalamicNucleus",
    alternate_names=["VL"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventrolateralThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_ventrolateralThalamicNucleus",
    name="ventrolateral thalamic nucleus",
)
ParcellationEntity.whss_datlas_ventromedial_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_ventromedialThalamicNucleus",
    alternate_names=["VM"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_ventromedialThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_ventromedialThalamicNucleus",
    name="ventromedial thalamic nucleus",
)
ParcellationEntity.whss_datlas_vestibular_apparatus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_vestibularApparatus",
    alternate_names=["VeA"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_vestibularApparatus"},
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_vestibularApparatus"
        },
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_vestibularApparatus"},
    ],
    lookup_label="WHSSDatlas_vestibularApparatus",
    name="vestibular apparatus",
)
ParcellationEntity.whss_datlas_vestibular_nerve = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_vestibularNerve",
    alternate_names=["8vn"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3_vestibularNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v3.01_vestibularNerve"},
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_vestibularNerve"},
    ],
    lookup_label="WHSSDatlas_vestibularNerve",
    name="vestibular nerve",
)
ParcellationEntity.whss_datlas_visual_cortex = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_visualCortex",
    alternate_names=["Vis"],
    lookup_label="WHSSDatlas_visualCortex",
    name="visual cortex",
)
ParcellationEntity.whss_datlas_white_matter = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_whiteMatter",
    alternate_names=["wmt"],
    lookup_label="WHSSDatlas_whiteMatter",
    name="white matter",
)
ParcellationEntity.whss_datlas_white_matter_of_the_brainstem = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_whiteMatterOfTheBrainstem",
    alternate_names=["bsw"],
    lookup_label="WHSSDatlas_whiteMatterOfTheBrainstem",
    name="white matter of the brainstem",
)
ParcellationEntity.whss_datlas_white_matter_of_the_tectum = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_whiteMatterOfTheTectum",
    alternate_names=["tew"],
    lookup_label="WHSSDatlas_whiteMatterOfTheTectum",
    name="white matter of the tectum",
)
ParcellationEntity.whss_datlas_xiphoid_thalamic_nucleus = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_xiphoidThalamicNucleus",
    alternate_names=["Xi"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_xiphoidThalamicNucleus"
        }
    ],
    lookup_label="WHSSDatlas_xiphoidThalamicNucleus",
    name="xiphoid thalamic nucleus",
)
ParcellationEntity.whss_datlas_zona_incerta = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncerta",
    alternate_names=["ZI"],
    lookup_label="WHSSDatlas_zonaIncerta",
    name="zona incerta",
)
ParcellationEntity.whss_datlas_zona_incerta_a11_dopamine_cells = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaA11DopamineCells",
    alternate_names=["ZI-A11"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_zonaIncertaA11DopamineCells"
        }
    ],
    lookup_label="WHSSDatlas_zonaIncertaA11DopamineCells",
    name="zona incerta, A11 dopamine cells",
)
ParcellationEntity.whss_datlas_zona_incerta_a13_dopamine_cells = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaA13DopamineCells",
    alternate_names=["ZI-A13"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_zonaIncertaA13DopamineCells"
        }
    ],
    lookup_label="WHSSDatlas_zonaIncertaA13DopamineCells",
    name="zona incerta, A13 dopamine cells",
)
ParcellationEntity.whss_datlas_zona_incerta_caudal_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaCaudalPart",
    alternate_names=["ZI-c"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_zonaIncertaCaudalPart"}
    ],
    lookup_label="WHSSDatlas_zonaIncertaCaudalPart",
    name="zona incerta, caudal part",
)
ParcellationEntity.whss_datlas_zona_incerta_dorsal_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaDorsalPart",
    alternate_names=["ZI-d"],
    has_versions=[
        {"@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_zonaIncertaDorsalPart"}
    ],
    lookup_label="WHSSDatlas_zonaIncertaDorsalPart",
    name="zona incerta, dorsal part",
)
ParcellationEntity.whss_datlas_zona_incerta_rostral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaRostralPart",
    alternate_names=["ZI-r"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_zonaIncertaRostralPart"
        }
    ],
    lookup_label="WHSSDatlas_zonaIncertaRostralPart",
    name="zona incerta, rostral part",
)
ParcellationEntity.whss_datlas_zona_incerta_ventral_part = ParcellationEntity(
    id="https://openminds.ebrains.eu/instances/parcellationEntity/WHSSDatlas_zonaIncertaVentralPart",
    alternate_names=["ZI-v"],
    has_versions=[
        {
            "@id": "https://openminds.ebrains.eu/instances/parcellationEntityVersion/WHSSDatlas_v4_zonaIncertaVentralPart"
        }
    ],
    lookup_label="WHSSDatlas_zonaIncertaVentralPart",
    name="zona incerta, ventral part",
)
