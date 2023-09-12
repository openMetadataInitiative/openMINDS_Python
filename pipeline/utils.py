import glob
import os
import shutil
from typing import List

from git import Repo, GitCommandError

source_url = "https://github.com/openMetadataInitiative/openMINDS.git"

def clone_sources():
    if os.path.exists("sources"):
        shutil.rmtree("sources")
    Repo.clone_from(source_url, to_path="sources", depth=1)

class SchemaLoader(object):

    def __init__(self):
        self._root_directory = os.path.realpath(".")
        self.schemas_sources = os.path.join(self._root_directory, "sources", "schemas")

    def get_schema_versions(self) -> List[str]:
        return os.listdir(self.schemas_sources)

    def find_schemas(self, version:str) -> List[str]:
        return glob.glob(os.path.join(self.schemas_sources, version, f'**/*.schema.omi.json'), recursive=True)
