# this file was auto-generated!


from openminds.v3.controlled_terms.file_repository_type import FileRepositoryType


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
