"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class AnalysisTechnique(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/AnalysisTechnique"
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
            description="Longer statement or account giving the characteristics of the analysis technique.",
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
            description="Word or phrase that constitutes the distinctive designation of the analysis technique.",
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


AnalysisTechnique.activation_likelihood_estimation = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/activationLikelihoodEstimation",
    definition="An 'activation likelihood estimation' is a coordinate-based meta-analysis of neuroimaging data that determines the above-chance convergence of activation probabilities between experiments (i.e., not between foci). [adapted from [Eickhoff et al., 2011](https://dx.doi.org/10.1016%2Fj.neuroimage.2011.09.017)]",
    name="activation likelihood estimation",
    synonyms=[
        "activation likelihood estimation analysis",
        "activation likelihood estimation meta-analysis",
        "ALE",
        "ALE analysis",
        "ALE meta-analysis",
    ],
)
AnalysisTechnique.affine_image_registration = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/affineImageRegistration",
    definition="A 'affine image registration' is a process of bringing a set of images into the same coordinate system using affine transformation.",
    name="affine image registration",
)
AnalysisTechnique.affine_transformation = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/affineTransformation",
    definition="An 'affine transformation' is a specific linear transformation using combinations of rotations, translations, reflections, scaling and shearing to map coordinates between two coordinate spaces.",
    name="affine transformation",
)
AnalysisTechnique.anatomical_delineation_technique = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/anatomicalDelineationTechnique",
    name="anatomical delineation technique",
)
AnalysisTechnique.average_linkage_clustering = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/averageLinkageClustering",
    name="average linkage clustering",
)
AnalysisTechnique.bias_field_correction = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/biasFieldCorrection",
    definition="A 'bias field correction' is a mathematical technique to remove a corrupting, low frequency signal from magnetic resonance images. This bias field signal is typically caused by inhomogeneities in the magnetic ﬁelds of the magnetic resonance imaging machine.",
    name="bias field correction",
    synonyms=["BFC"],
)
AnalysisTechnique.bootstrap_aggregating = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/bootstrapAggregating",
    definition="A specialized machine learning ensemble meta-algorithm designed to improve the stability and accuracy of machine learning algorithms used in statistical classification and regression. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Bootstrap_aggregating)]",
    name="bootstrap aggregating",
    synonyms=[
        "bagging",
        "bootstrap aggregation",
        "bagging ensemble learning",
        "bagging ensemble method",
        "ensemble learning bagging",
    ],
)
AnalysisTechnique.bootstrapping = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/bootstrapping",
    name="bootstrapping",
)
AnalysisTechnique.boundary_based_registration = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/boundaryBasedRegistration",
    definition="The term 'boundary-based registration' refers to feature based image registration methods which utilize a boundary which can be identified in the source and target image.",
    name="boundary-based registration",
    synonyms=["BBR"],
)
AnalysisTechnique.cluster_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/clusterAnalysis",
    name="cluster analysis",
)
AnalysisTechnique.combined_volume_surface_registration = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/combinedVolumeSurfaceRegistration",
    definition="The term 'combined volume-surface registration' refers to an image registration framework which utilizes information from the brain surface and the brain volume to perform the registration (cf. [Postelnicu et al. (2009)](https://doi.org/10.1109/TMI.2008.2004426)).",
    name="combined volume–surface registration",
    synonyms=["CVS registration"],
)
AnalysisTechnique.communication_profiling = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/communicationProfiling",
    name="communication profiling",
)
AnalysisTechnique.conjunction_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/conjunctionAnalysis",
    name="conjunction analysis",
)
AnalysisTechnique.connected_component_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/connected-componentAnalysis",
    definition="'connected-component analysis' is an algorithmic application of graph theory, where subsets of connected components are uniquely labeled based on a given heuristic. [adapted from: [wikipedia](https://en.wikipedia.org/wiki/Connected-component_labeling)]",
    name="connected-component analysis",
    synonyms=["CCA", "CCL", "connected-component labeling"],
)
AnalysisTechnique.connectivity_based_parcellation_technique = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/connectivityBasedParcellationTechnique",
    name="connectivity based parcellation technique",
)
AnalysisTechnique.convolution = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/convolution",
    definition="In functional analysis, 'convolution' is a mathematical operation on two functions (f and g) producing a third function (f * g) that expresses how the shape of one is modified by the other. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Convolution)]",
    name="convolution",
    synonyms=["convolution technique"],
)
AnalysisTechnique.correlation_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/correlationAnalysis",
    name="correlation analysis",
)
AnalysisTechnique.covariance_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/covarianceAnalysis",
    name="covariance analysis",
)
AnalysisTechnique.current_source_density_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/currentSourceDensityAnalysis",
    name="current source density analysis",
)
AnalysisTechnique.cytoarchitectonic_mapping = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/cytoarchitectonicMapping",
    definition="'Cytoarchitectonic mapping' is a delineation technique that defines regional borders based on histological analysis of the cellular composition of the studied tissue.",
    name="cytoarchitectonic mapping",
)
AnalysisTechnique.deep_learning = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/deepLearning",
    name="deep learning",
)
AnalysisTechnique.density_measurement = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/densityMeasurement",
    name="density measurement",
)
AnalysisTechnique.dictionary_learning = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/dictionaryLearning",
    definition="'Dictionary learning' is a branch of signal processing and machine learning that aims at finding a frame (called dictionary) in which some training data admits a sparse representation.",
    name="dictionary learning",
    synonyms=["sparse dictionary learning"],
)
AnalysisTechnique.diffeomorphic_registration = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/diffeomorphicRegistration",
    definition="'Diffeomorphic registration' refers to a suite of algorithms that register or build correspondences between dense coordinate systems in medical imaging by ensuring the solutions are diffeomorphic.",
    name="diffeomorphic registration",
    synonyms=["diffeomorphic mapping", "large deformation diffeomorphic metric mapping"],
)
AnalysisTechnique.dynamic_causal_modeling = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/dynamicCausalModeling",
    definition="An analysis framework for specifying non-linear state-space models in continuous time using stochastic or ordinary differential equations, for fitting them to data and comparing their evidence using Bayesian model comparison.[adapted from [Wikipedia](https://en.wikipedia.org/wiki/Dynamic_causal_modeling)]",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0103618"),
    name="dynamic causal modeling",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/ilx_0103618"),
    synonyms=["dynamic causal model", "DCM"],
)
AnalysisTechnique.eye_movement_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/eyeMovementAnalysis",
    definition="'Eye movement analysis' refers to a group of techniques used to analyze eye movements from video or images.",
    name="eye movement analysis",
    synonyms=["eye motion analysis"],
)
AnalysisTechnique.four_points_congruent_sets_alignment = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/4PointsCongruentSetsAlignment",
    definition="4-points congruent sets alignment is a fast and robust alignment technique for 3D point sets without pre-filtering or denoising the data, even if the data are noisy and/or contaminated with outliers ([Aiger et al., 2008](https://doi.org/10.1145/1360612.1360684)).",
    name="4-points congruent sets alignment",
    synonyms=[
        "4-points congruent sets",
        "4-points congruent sets registration",
        "4PCS",
        "4PCS alignment",
        "4PCS registration",
    ],
)
AnalysisTechnique.general_linear_modeling = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/generalLinearModeling",
    name="general linear modeling",
)
AnalysisTechnique.genetic_correlation_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/geneticCorrelationAnalysis",
    name="genetic correlation analysis",
)
AnalysisTechnique.genetic_risk_score = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/geneticRiskScore",
    definition="A genetic risk score is an estimate of the cumulative contribution of genetic factors to a specific outcome of interest in an individual (Igo et al, 2019).",
    description="[described in: Igo, R. P., Jr, Kinzy, T. G., & Cooke Bailey, J. N. (2019). Genetic Risk Scores. Current protocols in human genetics, 104(1), e95. https://doi.org/10.1002/cphg.95]",
    name="genetic risk score",
    synonyms=["GRS"],
)
AnalysisTechnique.global_signal_regression = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/globalSignalRegression",
    definition="A 'global signal regression' is a denoising technique where the global signal is removed from the time series of each voxel through linear regression. [adapted from: [Murphy & Fox, 2017](https://dx.doi.org/10.1016%2Fj.neuroimage.2016.11.052)]",
    name="global signal regression",
    synonyms=["GSR"],
)
AnalysisTechnique.grubbs_test = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/GrubbsTest",
    definition="The 'Grubbs test' is a statistical test, first published by [Grubbs (1950)](https://doi.org/10.1214/aoms/1177729885), used to detect outliers in univariate data that are assumed to come from a normally distributed population. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Grubbs%27s_test)]",
    name="Grubbs' test",
    synonyms=["extreme studentized deviate test", "Grubbs test", "maximum normalized residual test"],
)
AnalysisTechnique.hierarchical_agglomerative_clustering = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/hierarchicalAgglomerativeClustering",
    name="hierarchical agglomerative clustering",
)
AnalysisTechnique.hierarchical_clustering = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/hierarchicalClustering",
    name="hierarchical clustering",
)
AnalysisTechnique.hierarchical_divisive_clustering = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/hierarchicalDivisiveClustering",
    name="hierarchical divisive clustering",
)
AnalysisTechnique.hilbert_transform = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/HilbertTransform",
    definition="A convolution technique for a function u(t) of a real variable with the function h(t) = 1/πt, known as the Cauchy kernel, producing a function of a real variable H(u)(t). [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Hilbert_transform)]",
    name="Hilbert transform",
)
AnalysisTechnique.ica_based_denoising_technique = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/ICABasedDenoisingTechnique",
    definition="An 'ICA based denoising technique' removes independent components from input data to reduce noise while preserving the features of interest in the data.",
    name="ICA based denoising technique",
    synonyms=[
        "ICA based denoising",
        "ICA based denoising method",
        "ICA-based denoising",
        "ICA-based denoising method",
        "ICA-based denoising technique",
        "independent component analysis based denoising technique",
    ],
)
AnalysisTechnique.image_distortion_correction = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/imageDistortionCorrection",
    definition="'Image distortion correction' is the general term for any image processing technique correcting optical or perspective aberrations of an image.",
    name="image distortion correction",
)
AnalysisTechnique.image_registration = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/imageRegistration",
    definition="An 'image registration' is a process of bringing a set of images into the same coordinate system.",
    name="image registration",
    synonyms=["spatial registration"],
)
AnalysisTechnique.independent_component_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/independentComponentAnalysis",
    name="independent component analysis",
)
AnalysisTechnique.inter_subject_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/interSubjectAnalysis",
    name="inter-subject analysis",
)
AnalysisTechnique.interpolation = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/interpolation",
    definition="An 'interpolation' is an analysis technique that delivers estimates for new data points based on a range of a discrete set of known data points.",
    name="interpolation",
)
AnalysisTechnique.intra_subject_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/intraSubjectAnalysis",
    name="intra-subject analysis",
)
AnalysisTechnique.isomap = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/Isomap",
    definition="A manifold learning algorithm used for computing a quasi-isometric, low-dimensional embedding of a set of high-dimensional data points to perform a nonlinear dimensionality reduction. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Isomap)]",
    name="Isomap",
    synonyms=["isomap"],
)
AnalysisTechnique.isometric_mapping = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/isometricMapping",
    definition="A superclass of distance-preserving transformations between metric spaces, often used to reduce dimensionality of data by embedding one space into another. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Isometry)]",
    name="isometric mapping",
    synonyms=["isometry"],
)
AnalysisTechnique.k_means_clustering = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/k-meansClustering",
    definition="'k-means clustering' is a centroid-based cluster analysis technique that aims to partition n observations into a pre-defined number of k clusters by assigning each observation to the cluster with the nearest mean (centroid).",
    name="k-means clustering",
    synonyms=["k-means", "k-means cluster analysis"],
)
AnalysisTechnique.linear_image_registration = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/linearImageRegistration",
    definition="A 'linear image registration' is a process of bringing a set of images into the same coordinate system using linear transformation.",
    name="linear image registration",
)
AnalysisTechnique.linear_regression = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/linearRegression",
    definition="A 'linear regression' is an analysis approach for modelling the linear relationship between a scalar response and one or more explanatory variables.",
    name="linear regression",
)
AnalysisTechnique.linear_transformation = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/linearTransformation",
    definition="A 'linear transformation' is a linear mathematical function to map coordinates between two different coordinate systems while preserving straight lines.",
    name="linear transformation",
)
AnalysisTechnique.literature_mining = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/literatureMining",
    name="literature mining",
)
AnalysisTechnique.macromolecular_tissue_volume_image_processing = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/macromolecularTissueVolumeImageProcessing",
    definition="Magnetic resonance imaging analysis technique that provides a quantitative estimate of the macromolecular tissue volume within the image. [adapted from [Mezer et al., (2013)](https://doi.org/10.1038/nm.3390)].",
    name="macromolecular tissue volume image processing",
    synonyms=["macromolecular tissue volume estimation", "MTV estimation", "MTV image processing"],
)
AnalysisTechnique.magnetization_transfer_ratio_image_processing = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/magnetizationTransferRatioImageProcessing",
    name="magnetization transfer ratio image processing",
)
AnalysisTechnique.magnetization_transfer_saturation_image_processing = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/magnetizationTransferSaturationImageProcessing",
    definition="Magnetization transfer estimation method that improves the contrast between white matter, gray matter, and cerebrospinal fluid, as well as the correlation with macromolecular content [adapted from [Longoni et al., (2023)](https://doi.org/10.1177/13524585221137500)].",
    name="magnetization transfer saturation image processing",
    synonyms=["magnetization transfer saturation estimation", "MTsat estimation", "MTsat image processing"],
)
AnalysisTechnique.manifold_learning = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/manifoldLearning",
    definition="'manifold learning' refers to a group of machine learning algorithms for non-linear dimensionality reduction of high-dimensionalty data.",
    name="manifold learning",
)
AnalysisTechnique.mann_whitney_u_test = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/MannWhitneyUTest",
    definition="The 'Mann–Whitney U test' is a nonparametric test of the null hypothesis that, for randomly selected values X and Y from two populations, the probability of X being greater than Y is equal to the probability of Y being greater than X. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test)]",
    name="Mann–Whitney U test",
    synonyms=[
        "Mann–Whitney–Wilcoxon test",
        "MWU test",
        "MWW test",
        "Wilcoxon rank-sum test",
        "Wilcoxon–Mann–Whitney test",
        "WMW test",
    ],
)
AnalysisTechnique.mass_univariate_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/massUnivariateAnalysis",
    definition="A 'mass univariate analysis' is the statistical analysis of a massive number of simultaneously measured dependent variables via the performance of univariate hypothesis tests.",
    name="mass univariate analysis",
)
AnalysisTechnique.maximum_likelihood_estimation = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/maximumLikelihoodEstimation",
    definition="'Maximum likelihood estimation' is a statistical analysis technique that estimates the parameters of an assumed probability distribution for some observed data by maximizing a likelihood function so that, under the assumed statistical model, the observed data is most probable. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation)]",
    name="maximum likelihood estimation technique",
    synonyms=["MLE", "maximum likelihood estimation technique"],
)
AnalysisTechnique.maximum_probability_projection = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/maximumProbabilityProjection",
    name="maximum probability projection",
)
AnalysisTechnique.meta_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/metaAnalysis",
    name="meta-analysis",
)
AnalysisTechnique.meta_analytic_connectivity_modeling = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/metaAnalyticConnectivityModeling",
    name="meta-analytic connectivity modeling",
)
AnalysisTechnique.metadata_parsing = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/metadataParsing",
    name="metadata parsing",
)
AnalysisTechnique.model_based_stimulation_artifact_correction = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/modelBasedStimulationArtifactCorrection",
    definition="The 'model-based stimulation artifact correction' is a model-based analysis technique for removing stimulation artifacts from intracranial electroencephalography signals to uncover the cortico-cortical evoked potentials caused by the stimulation (cf. [Trebaul et al. (2016)](https://doi.org/10.1016/j.jneumeth.2016.03.002)).",
    name="model-based stimulation artifact correction",
    synonyms=["model-based artifact correction"],
)
AnalysisTechnique.morphometry = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/morphometry",
    name="morphometry",
    synonyms=["morphometric analysis"],
)
AnalysisTechnique.motion_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/motionAnalysis",
    definition="'Motion analysis' refers to a group of analysis techniques used to measure from video/images the movement and/or position of an object, specimen, or anatomical parts of a specimen over a given period of time.",
    name="motion analysis",
    synonyms=["movement analysis"],
)
AnalysisTechnique.motion_correction = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/motionCorrection",
    definition="'Motion correction' is the general term for any preprocessing analysis technique used to correct for motion artifacts in imaging time-series.",
    name="motion correction",
)
AnalysisTechnique.multi_scale_individual_component_clustering = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/multi-scaleIndividualComponentClustering",
    definition="'multi-scale individual component clustering' is a multi-scale, unsupervised cluster analysis technique to group individual, independent components of a single-object/single-subject independent component analysis (ICA) from an object-pool/subject-pool (cf. [Naveau et al, 2012](https://doi.org/10.1007/s12021-012-9145-2)).",
    name="multi-scale individual component clustering",
    synonyms=["MICCA", "multi-scale individual component cluster algorithm"],
)
AnalysisTechnique.multi_voxel_pattern_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/multiVoxelPatternAnalysis",
    definition="A 'multi-voxel pattern analysis' is considered as a supervised classification problem where a classifier attempts to capture the relationships between spatial patterns of functional magnetic resonance imaging activity and experimental conditions ([Mahmoudi et al., 2012](https://doi.org/10.1155/2012/961257), [Davatzikos et al., 2005](https://doi.org/10.1016/j.neuroimage.2005.08.009)).",
    name="multi-voxel pattern analysis",
    synonyms=["MVPA"],
)
AnalysisTechnique.multiple_linear_regression = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/multipleLinearRegression",
    definition="A 'multiple linear regression' is a linear approach for modelling the relationship between a scalar response and multiple explanatory variables. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Linear_regression)]",
    name="multiple linear regression",
    synonyms=["MLR", "multi-linear regression", "multilinear regression", "multiple regression"],
)
AnalysisTechnique.multivariate_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/multivariateAnalysis",
    definition="Any statistical analysis of data where multiple measurements are made on each experimental unit and where the relationships among multivariate measurements and their structure are important. [adapted from [Olkin and Sampson, 2001](https://doi.org/10.1016/B0-08-043076-7/00472-1)]",
    name="multivariate analysis",
    synonyms=["MVA", "multivariate statistics"],
)
AnalysisTechnique.myelin_water_fraction_image_processing = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/myelinWaterFractionImageProcessing",
    name="myelin water fraction image processing",
)
AnalysisTechnique.nonlinear_image_registration = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/nonlinearImageRegistration",
    definition="A 'nonlinear image registration' is a process of bringing a set of images into the same coordinate system using nonlinear transformation.",
    name="nonlinear image registration",
    synonyms=["non-linear image registration"],
)
AnalysisTechnique.nonlinear_transformation = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/nonlinearTransformation",
    definition="A 'nonlinear transformation' is a mathematical function to map coordinates between two different coordinate systems, not preserving straight lines.",
    name="nonlinear transformation",
    synonyms=["non-linear transformation"],
)
AnalysisTechnique.nonrigid_image_registration = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/nonrigidImageRegistration",
    definition="A 'nonrigid image registration' is a process of bringing a set of images into the same coordinate system using nonrigid transformation.",
    name="nonrigid image registration",
    synonyms=["non-rigid image registration"],
)
AnalysisTechnique.nonrigid_motion_correction = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/nonrigidMotionCorrection",
    name="nonrigid motion correction",
    synonyms=["non-rigid motion correction"],
)
AnalysisTechnique.nonrigid_transformation = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/nonrigidTransformation",
    definition="A 'nonrigid transformation' is a specific linear transformation using combinations of rotations, translations, reflections, scaling, shearing, and perspective projections to map coordinates between two coordinate spaces.",
    name="nonrigid transformation",
    synonyms=["non-rigid transformation"],
)
AnalysisTechnique.nuisance_regression = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/nuisanceRegression",
    definition="'Nuisance regression' is an image processing technique which seeks to attenuate non-neural BOLD fluctuations from measurable noise sources such as scanner drift and head motion, as well as periodic physiological signals. [adapted from [Hallquist et al. 2013](https://doi.org/10.1016%2Fj.neuroimage.2013.05.116)]",
    name="nuisance regression",
    synonyms=["NR"],
)
AnalysisTechnique.pathway_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/pathwayAnalysis",
    definition="A 'pathway analysis' refers to a group of techniques that aim to discover what biological themes, and which biomolecules, are crucial to understand biological pathways of (typically) high-throughput biological data (adapted from [García-Campos et al., 2015](https://doi.org/10.3389/fphys.2015.00383)).",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0778897"),
    name="pathway analysis",
    preferred_ontology_identifier=IRI("http://edamontology.org/operation_3928"),
    synonyms=[
        "biological pathway modelling",
        "biological pathway prediction",
        "functional enrichment analysis",
        "functional pathway analysis",
        "PA",
        "pathway comparison",
        "pathway modelling",
        "pathway prediction",
        "pathway simulation",
    ],
)
AnalysisTechnique.performance_profiling = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/performanceProfiling",
    name="performance profiling",
)
AnalysisTechnique.phase_synchronization_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/phaseSynchronizationAnalysis",
    definition="A 'phase synchronization analysis' detects and quantifies synchronization between two time series.",
    name="phase synchronization analysis",
    synonyms=["PS analysis", "PSA"],
)
AnalysisTechnique.principal_component_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/principalComponentAnalysis",
    definition="A 'principal component analysis' is a statistical technique for reducing the dimensionality of a dataset by linearly transforming the data into a new coordinate system where (most of) the variation in the data can be described with fewer dimensions than the initial data. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Principal_component_analysis)]",
    name="principal component analysis",
    synonyms=["PCA"],
)
AnalysisTechnique.probabilistic_anatomical_parcellation_technique = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/probabilisticAnatomicalParcellationTechnique",
    name="probabilistic anatomical parcellation technique",
)
AnalysisTechnique.probabilistic_diffusion_tractography = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/probabilisticDiffusionTractography",
    name="probabilistic diffusion tractography",
)
AnalysisTechnique.qualitative_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/qualitativeAnalysis",
    definition="'Qualitative analysis' uses subjective judgment to analyze data based on non-quantifiable information. The resulting data are typically nonnumerical.",
    name="qualitative analysis",
)
AnalysisTechnique.quantitative_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/quantitativeAnalysis",
    name="quantitative analysis",
)
AnalysisTechnique.ratiometry = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/ratiometry",
    definition="Quantitative analysis technique utilizing the ratio of two signals or responses obtained from a sample.",
    name="ratiometry",
    synonyms=["ratiometric analysis"],
)
AnalysisTechnique.reconstruction_technique = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/reconstructionTechnique",
    definition="A 'reconstruction technique' is able to re-build, re-assemble, re-create, or re-imagine something by applying (often mathematical) principles to physical evidence.",
    name="reconstruction technique",
)
AnalysisTechnique.rigid_image_registration = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/rigidImageRegistration",
    definition="A 'rigid image registration' is a process of bringing a set of images into the same coordinate system using rigid transformation.",
    name="rigid image registration",
)
AnalysisTechnique.rigid_motion_correction = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/rigidMotionCorrection",
    name="rigid motion correction",
)
AnalysisTechnique.rigid_transformation = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/rigidTransformation",
    definition="A 'rigid transformation' is a specific linear transformation using combinations of rotations, translations, and reflections to map coordinates between two coordinate spaces, leaving the object congruent.",
    name="rigid transformation",
)
AnalysisTechnique.seed_based_correlation_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/seed-basedCorrelationAnalysis",
    name="seed-based correlation analysis",
)
AnalysisTechnique.semantic_anchoring = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/semanticAnchoring",
    name="semantic anchoring",
)
AnalysisTechnique.semiquantitative_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/semiquantitativeAnalysis",
    definition="An analysis technique which constitutes or involves less than quantitative precision.",
    name="semiquantitative analysis",
)
AnalysisTechnique.shapiro_wilk_test = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/ShapiroWilkTest",
    definition="The 'Shapiro–Wilk test' is a statistical test of normality of a complete sample, first described by [Shapiro and Wilk (1965)](https://doi.org/10.1093/biomet/52.3-4.591). [adapted from [wikipedia](https://en.wikipedia.org/wiki/Shapiro%E2%80%93Wilk_test)]",
    name="Shapiro-Wilk test",
    synonyms=["Shapiro-Wilk normality test"],
)
AnalysisTechnique.signal_filtering_technique = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/signalFilteringTechnique",
    definition="'Signal filtering' is a signal processing technique used to remove or suppress unwanted components or features (e.g., certain frequencies) from a measured signal. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Filter_(signal_processing))]",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739623"),
    name="signal filtering technique",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/indexes/ontologies/methods/151"),
    synonyms=["filtering", "signal filtering"],
)
AnalysisTechnique.signal_processing_technique = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/signalProcessingTechnique",
    definition="'Signal processing' refers to a class of analysis techniques used to improve transmission, storage efficiency and subjective quality as well as to emphasize or detect components of interest in a measured signal. [adapted from [wikipedia](https://en.wikipedia.org/wiki/Signal_processing)]",
    interlex_identifier=IRI("http://uri.interlex.org/ilx_0739633"),
    name="signal processing technique",
    preferred_ontology_identifier=IRI("http://uri.interlex.org/tgbugs/uris/readable/technique/sigproc"),
    synonyms=["signal processing"],
)
AnalysisTechnique.slice_timing_correction = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/sliceTimingCorrection",
    definition="'Slice timing correction' is a preprocessing technique applied to functional magnetic resonance image data in order to correct for temporal offsets between 2D image slices during the data acquisition. [adapted from [Parker and Razlighi, 2019](https://doi.org/10.3389/fnins.2019.00821)]",
    name="slice timing correction",
    synonyms=["STC"],
)
AnalysisTechnique.spearmans_rank_order_correlation = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/SpearmansRankOrderCorrelation",
    definition="The 'Spearman's rank-order correlation' is the nonparametric version of the Pearson product-moment correlation measuring the strength and direction of association between a set of two ranked variables. [adapted from [Laerd.com](https://statistics.laerd.com/statistical-guides/spearmans-rank-order-correlation-statistical-guide.php)]",
    name="Spearman's rank-order correlation",
    synonyms=["Spearman’s correlation", "Spearman’s correlation test", "Spearman’s rank correlation"],
)
AnalysisTechnique.spectral_power_auto_segmentation_technique = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/spectralPowerAutoSegmentationTechnique",
    definition="A 'spectral power auto-segmentation technique' makes use of the power spectrum along the time axis of individual pixels or voxels in an image to automatically generate a segmentation.",
    name="spectral power auto-segmentation technique",
    synonyms=["spectral power image auto-segmentation technique"],
)
AnalysisTechnique.spike_sorting = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/spikeSorting",
    definition="'Spike sorting' is a class of techniques used in the analysis of extracellular electrophysiological data to extract the activity of one or more neurons from the background electrical noise by making use of the typical waveforms action potentials (spikes) create in the recorded neuronal signal.",
    interlex_identifier=IRI("http://uri.interlex.org/base/ilx_0739628"),
    name="spike sorting",
    synonyms=["spike sorting technique"],
)
AnalysisTechnique.stochastic_online_matrix_factorization = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/stochasticOnlineMatrixFactorization",
    definition="'Stochastic online matrix factorization' is a matrix-factorization algorithm that scales to input matrices with both huge number of rows and columns [(Mensch et al., 2018)](https://doi.org/10.1109/TSP.2017.2752697).",
    name="stochastic online matrix factorization",
    synonyms=["SOMF"],
)
AnalysisTechnique.structural_covariance_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/structuralCovarianceAnalysis",
    name="structural covariance analysis",
)
AnalysisTechnique.support_vector_machine_classifier = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/supportVectorMachineClassifier",
    definition="A 'support-vector machine classifier' is a supervised machine learning technique that analyzes data for classification.",
    name="support-vector machine classifier",
    synonyms=[
        "support-vector machine",
        "support-vector machine learning",
        "SVC",
        "SVM",
        "SVM classifier",
        "SVM learning",
    ],
)
AnalysisTechnique.support_vector_machine_regression = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/supportVectorMachineRegression",
    definition="A 'Support-Vector Regression Algorithm' is a supervised machine learning technique used to estimate the relationship between a dependent and a number of independent variables.",
    name="support-vector regression algorithm",
    synonyms=[
        "support vector regression",
        "support vector regression algorithm",
        "support-vector regression",
        "SVR",
        "SVR algorithm",
    ],
)
AnalysisTechnique.surface_projection = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/surfaceProjection",
    name="surface projection",
    synonyms=["surface texture projection"],
)
AnalysisTechnique.temporal_filtering = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/temporalFiltering",
    definition="'Temporal filtering' is a functional image signal processing technique that aims to remove or attenuate frequencies that vary along the time axis of the raw signal. [adapted from [Wikibooks](https://en.wikibooks.org/wiki/Neuroimaging_Data_Processing/Processing/Steps/Temporal_Filtering)]",
    name="temporal filtering",
    synonyms=["temporal filtering technique", "temporal image filtering", "temporal image filtering technique"],
)
AnalysisTechnique.tractography = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/tractography",
    name="tractography",
)
AnalysisTechnique.transformation = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/transformation",
    definition="A 'transformation' is a mathematical function to map coordinates between two different coordinate systems.",
    name="transformation",
)
AnalysisTechnique.univariate_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/univariateAnalysis",
    definition="Any statistical analysis that is carried out on only one (dependent) variable of the data to summarize or describe that variable. [adapted from [Dandilands, 2014](https://doi.org/10.1007/978-94-007-0753-5_3108)]",
    name="univariate analysis",
    synonyms=["univariate statistics"],
)
AnalysisTechnique.video_annotation = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/videoAnnotation",
    name="video annotation",
)
AnalysisTechnique.voxel_based_morphometry = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/voxel-basedMorphometry",
    name="voxel-based morphometry",
)
AnalysisTechnique.ward_clustering = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/WardClustering",
    definition="'Ward clustering' is a general agglomerative hierarchical clustering procedure, where the criterion for choosing the pair of clusters to merge at each step is based on the optimal value of an objective function (typically aiming to minimize the total within-cluster variance). [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Ward%27s_method)]",
    name="Ward clustering",
)
AnalysisTechnique.z_score_analysis = AnalysisTechnique(
    id="https://openminds.om-i.org/instances/analysisTechnique/zScoreAnalysis",
    definition="The 'z-score analysis' is a statistical normalization technique where the z-score is calculated by subtracting the population mean from an individual raw score (observed data point) and dividing the difference by the population standard deviation. [adapted from [Wikipedia](https://en.wikipedia.org/wiki/Standard_score)]",
    name="z-score analysis",
    synonyms=["standard score analysis"],
)
