"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class FileRepositoryType(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/FileRepositoryType"
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


FileRepositoryType.ftp = FileRepositoryType(
    id="https://openminds.ebrains.eu/instances/fileRepositoryType/ftp",
    definition="A 'FTP repository' is located on a server that uses the file transfer protocol (FTP), a standard internet communication protocol which allows the transfer of files between clients and a server.",
    name="FTP repository",
    synonyms=["file transfer protocol repository"],
)
FileRepositoryType.git = FileRepositoryType(
    id="https://openminds.ebrains.eu/instances/fileRepositoryType/git",
    definition="A Git repository offers version control and source code management functionalities.",
    name="Git repository",
    synonyms=[
        "Git repository",
        "Git remote repository",
        "remote Git repository",
        "GitHub repository",
        "GitLab repository",
    ],
)
FileRepositoryType.git_annex = FileRepositoryType(
    id="https://openminds.ebrains.eu/instances/fileRepositoryType/gitAnnex",
    definition="git-annex allows managing large files with git, without storing the file contents in git.",
    name="git-annex repository",
)
FileRepositoryType.gpfs = FileRepositoryType(
    id="https://openminds.ebrains.eu/instances/fileRepositoryType/gpfs",
    definition="GPFS, short for General Parallel File System is a high-performance clustered file system developed by IBM",
    name="GPFS repository",
)
FileRepositoryType.s3 = FileRepositoryType(
    id="https://openminds.ebrains.eu/instances/fileRepositoryType/s3",
    definition="An S3 repository uses the cloud storage of the Amazon S3 service.",
    name="Amazon S3 repository",
    synonyms=["S3 repository", "Amazon Simple Storage Service repository"],
)
FileRepositoryType.seafile = FileRepositoryType(
    id="https://openminds.ebrains.eu/instances/fileRepositoryType/seafile",
    definition="Seafile is an open source file sync&share solution designed for high reliability, performance and productivity.",
    name="Seafile repository",
)
FileRepositoryType.swift = FileRepositoryType(
    id="https://openminds.ebrains.eu/instances/fileRepositoryType/swift",
    definition="A Swift repository uses the long-term cloud storage of the OpenStack Object Store project which is particularly designed for retrieving and updating large amounts of static data without the need of a central point of control.",
    name="Swift repository",
)
