# this file was auto-generated!


from openminds.latest.controlled_terms.meta_data_model_type import MetaDataModelType


MetaDataModelType.common_data_elements = MetaDataModelType(
    id="https://openminds.om-i.org/instances/metaDataModelType/commonDataElements",
    definition="Common Data Elements (CDEs) define standardized key terms or concepts for diseases in form of a data dictionary that can be used in both relational and graph metadata models.",
    name="common data elements",
)

MetaDataModelType.data_repository_model = MetaDataModelType(
    id="https://openminds.om-i.org/instances/metaDataModelType/dataRepositoryModel",
    definition="A data repository model defines the file and folder naming and structure as well as partially the file content (metadata definitions) and preferred format.",
    name="data repository model",
)

MetaDataModelType.graph_metadata_model = MetaDataModelType(
    id="https://openminds.om-i.org/instances/metaDataModelType/graphMetadataModel",
    definition="A graph metadata model defines a set of modular metadata schemas (including their relations) as architectural base of a graph database for describing the products represented in that database.",
    name="graph metadata model",
)

MetaDataModelType.relational_metadata_model = MetaDataModelType(
    id="https://openminds.om-i.org/instances/metaDataModelType/relationalMetadataModel",
    definition="A relational metadata model defines a set of tabular metadata schemas (including their relations) as architectural base of a relational database for describing the products represented in that database.",
    name="relational metadata model",
)
