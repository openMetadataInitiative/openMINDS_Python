"""
This module provides the Collection class, which can be used to
create a collection of openMINDS metadata nodes.

The collection can be saved to and loaded from disk, in JSON-LD format.
"""

from collections import Counter
from glob import glob
from importlib import import_module
import json
import os
from .registry import lookup_type
from .base import Link


DEFAULT_VERSION = "v4"


class Collection:
    """
    A collection of metadata nodes that can be saved to
    and loaded from disk.

    Args
    ----

    *nodes (LinkedMetadata):
        Nodes to store in the collection when creating it.
        Child nodes that are referenced from the explicitly
        listed nodes will also be added.
    """

    def __init__(self, *nodes):
        self.nodes = {}
        self.add(*nodes)

    def __len__(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes.values())

    def add(self, *nodes):
        """
        Add one or more metadata nodes to the collection.

        Child nodes that are referenced from the explicitly
        listed nodes will also be added.
        """
        for node in nodes:
            self._add_node(node)

    def _add_node(self, node):
        if node.id is None:
            node.id = self._get_blank_node_identifier()
        self.nodes[node.id] = node
        for linked_node in node.links:
            self._add_node(linked_node)

    def _get_blank_node_identifier(self):
        # see https://www.w3.org/TR/json-ld11/#identifying-blank-nodes

        # here we're choosing to use a zero-padded identifier to make
        # testing and debugging easier.
        # It might be easier just to use uuids, however
        fmt = f"_:{{identifier:06d}}"
        identifier = len(self.nodes)
        return fmt.format(identifier=identifier)

    def _sort_nodes_by_id(self):
        sorted_nodes = dict(sorted(self.nodes.items()))
        self.nodes = sorted_nodes

    def generate_ids(self, id_generator):
        """
        Generate an IRI id for all nodes in the graph that do not possess one.

        Args
        ----

        id_generator (function):
            a function that takes the node as an argument, and returns a unique IRI
        """
        for node_id in list(self.nodes.keys()):
            if node_id.startswith("_:"):
                node = self.nodes.pop(node_id)
                node.id = id_generator(node)
                self.nodes[node.id] = node

    @property
    def complete(self):
        """Do all nodes have an IRI?"""
        for node_id in self.nodes:
            if node_id.startswith("_:"):
                return False
        return True

    def save(self, path, individual_files=False, include_empty_properties=False, group_by_schema=False):
        """
        Save the node collection to disk in JSON-LD format.

        Args
        ----

        path (str):
            either a file or a directory into which the metadata will be written.
            It is recommended to use the extension ".jsonld".
        individual_files (bool):
            if False (default), save the entire collection into a single file.
            if True, `path` must be a directory, and each node is saved into a
            separate file within that directory.
        include_empty_properties (bool):
            if False (default), do not include properties with value None.
            if True, include all properties.
        group_by_schema (bool):
            Only applies if `individual_files` is True.
            If False (default), save all files in a single directory.
            If True, save into subdirectories according to the schema name.

        Returns
        -------

        A list of the file paths created.
        """
        # in case a user has added additional child nodes _after_ adding the parent node to the collection
        # we first re-add all child nodes to the collection.
        # This is probably not the most elegant or fast way to do this, but it is simple and robust.
        for node in tuple(self.nodes.values()):
            if node.type_.startswith("https://openminds.ebrains.eu/"):
                data_context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
            else:
                data_context = {"@vocab": "https://openminds.om-i.org/props/"}

            for linked_node in node.links:
                self._add_node(linked_node)
        # Now we can actually save the nodes
        if not individual_files:
            if os.path.exists(path):
                if not os.path.isfile(path):
                    raise OSError(f"Cannot create file {path} because a directory with that name already exists.")
            else:
                parent_dir = os.path.dirname(path)
                if parent_dir:
                    os.makedirs(parent_dir, exist_ok=True)
            self._sort_nodes_by_id()
            data = {
                "@context": data_context,
                "@graph": [
                    node.to_jsonld(
                        embed_linked_nodes=False, include_empty_properties=include_empty_properties, with_context=False
                    )
                    for node in self
                ],
            }
            with open(path, "w") as fp:
                json.dump(data, fp, indent=2)
            output_paths = [path]
        else:
            if not os.path.exists(path):
                os.makedirs(path, exist_ok=True)
            if not os.path.isdir(path):
                raise OSError(
                    f"If saving to multiple files, `path` must be a directory. path={path}, pwd={os.getcwd()}"
                )
            self._sort_nodes_by_id()
            output_paths = []
            for node in self:
                if node.id.startswith("http"):
                    file_identifier = node.uuid
                else:
                    assert node.id.startswith("_:")
                    file_identifier = node.id[2:]
                if group_by_schema:
                    dir_path = os.path.join(path, node.__class__.__name__)
                    os.makedirs(dir_path, exist_ok=True)
                    file_path = os.path.join(dir_path, f"{file_identifier}.jsonld")
                else:
                    file_path = os.path.join(path, f"{file_identifier}.jsonld")
                with open(file_path, "w") as fp:
                    data = node.to_jsonld(embed_linked_nodes=False, include_empty_properties=include_empty_properties)
                    json.dump(data, fp, indent=2)
                    output_paths.append(file_path)
        return output_paths

    def load(self, *paths, version=DEFAULT_VERSION):
        """
        Load openMINDS metadata from one or more JSON-LD files.

        `*paths` may contain either:

        1) a single directory, in which case all JSON-LD files in this directory
        and any non-hidden subdirectories will be loaded
        (where hidden subdirectories are those whose name starts with ".").

        2) one or more JSON-LD files, which will all be loaded.

        By default, openMINDS v4 will be used.
        If the JSON-LD files use a different openMINDS version, specify it
        with the `version` argument, e.g.::

            import openminds.latest

            c = Collection()
            c.load("/path/to/my/metadata.jsonld", version="latest")

        """

        import_module(f"openminds.{version}")

        if len(paths) == 1 and os.path.isdir(paths[0]):
            data_dir = paths[0]
            json_paths = glob(f"{data_dir}/**/*.jsonld", recursive=True) + glob(
                f"{data_dir}/**/*.json", recursive=True
            )
        else:
            json_paths = paths

        for path in json_paths:
            assert os.path.isfile(path)
            with open(path, "r") as fp:
                data = json.load(fp)
            if "@graph" in data:
                for item in data["@graph"]:
                    if "@type" in item:
                        cls = lookup_type(item["@type"], version=version)
                        node = cls.from_jsonld(item)
                    else:
                        # allow links to metadata instances outside this collection
                        if not item["@id"].startswith("http"):
                            raise ValueError("Local nodes must have @type specified")
                        node = Link(item["@id"])
                    self.add(node)
            else:
                if "@type" in data:
                    cls = lookup_type(data["@type"], version=version)
                    node = cls.from_jsonld(data)
                else:
                    # allow links to metadata instances outside this collection
                    if not data["@id"].startswith("http"):
                        raise ValueError("Local nodes must have @type specified")
                    node = Link(data["@id"])
                self.add(node)
        self._resolve_links()

    def _resolve_links(self):
        """Replace `Link` attributes with typed Nodes where possible"""
        for node in self.nodes.values():
            node._resolve_links(self.nodes)

    def validate(self, ignore=None):
        """
        Check whether all constraints are satisfied.

        Arguments:
            ignore: an optional list of check types that should be ignored
                    ("required", "type", "multiplicity")

        Returns a dict containing information about any validation failures.
        """
        all_failures = {}
        for node in self:
            failures = node.validate(ignore=ignore)
            if failures:
                all_failures[node.id] = failures
        return all_failures

    @property
    def is_valid(self):
        failures = self.validate()
        return len(failures) == 0

    def sort_nodes_for_upload(self):
        """
        Return a list of nodes, sorted so that they can be uploaded to a graph database safely,
        i.e., child nodes will be saved before their parents.

        The upload code is assumed to generate @ids and update the Python instances accordingly.
        """
        unsorted = set(self.nodes.keys())
        sorted = []
        # initial step: move nodes with no children (downstream links) directly to `sorted`
        for node_id in unsorted:
            if len(self.nodes[node_id].links) == 0:
                sorted.append(node_id)
        unsorted -= set(sorted)
        # now iteratively add nodes to `sorted` if all their children are already in `sorted`
        while len(unsorted) > 0:
            newly_sorted = []
            for node_id in unsorted:
                child_ids = set(child.id for child in self.nodes[node_id].links)
                if not child_ids.difference(sorted):
                    sorted.append(node_id)
                    newly_sorted.append(node_id)
            unsorted -= set(newly_sorted)
        return [self.nodes[node_id] for node_id in sorted]

    def statistics(self):
        """
        Return a counter containing the number of nodes of each type.
        """
        stats = Counter(node.__class__.__name__ for node in self.nodes.values())
        return stats
