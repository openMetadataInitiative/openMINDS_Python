"""
This module provides the Collection class, which can be used to
create a collection of openMINDS metadata nodes.

The collection can be saved to and loaded from disk, in JSON-LD format.
"""

import json
import os
from .registry import lookup_type
from .base import Link


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

    def save(self, path, individual_files=False, include_empty_properties=False):
        """
        Save the node collection to disk in JSON-LD format.

        Args
        ----

        path (str):
            either a file or a directory into which the metadata will be written.
        individual_files (bool):
            if False (default), save the entire collection into a single file.
            if True, `path` must be a directory, and each node is saved into a
            separate file within that directory.

        Returns
        -------

        A list of the file paths created.
        """
        # in case a user has added additional child nodes _after_ adding the parent node to the collection
        # we first re-add all child nodes to the collection.
        # This is probably not the most elegant or fast way to do this, but it is simple and robust.
        for node in tuple(self.nodes.values()):
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
            data = {
                "@context": {"@vocab": "https://openminds.ebrains.eu/vocab/"},
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
                raise OSError("if saving to multiple files, `path` must be a directory")
            output_paths = []
            for node in self:
                if node.id.startswith("http"):
                    file_identifier = node.uuid
                else:
                    assert node.id.startswith("_:")
                    file_identifier = node.id[2:]
                file_path = os.path.join(path, f"{file_identifier}.jsonld")
                with open(file_path, "w") as fp:
                    data = node.to_jsonld(embed_linked_nodes=False, include_empty_properties=include_empty_properties)
                    json.dump(data, fp, indent=2)
                    output_paths.append(file_path)
        return output_paths

    def load(self, *paths):
        """
        Load openMINDS metadata from one or more JSON-LD files.

        `*paths` may contain either:

        1) a single directory, in which case
        all JSON-LD files all the top level of this directory will be loaded
        (but without descending into subdirectories)

        2) one or more JSON-LD files, which will all be loaded.
        """
        if len(paths) == 1 and os.path.isdir(paths[0]):
            data_dir = paths[0]
            json_paths = [
                os.path.join(data_dir, item)
                for item in os.listdir(data_dir)
                if os.path.splitext(item)[1] in (".json", ".jsonld")
            ]
        else:
            json_paths = paths

        for path in json_paths:
            assert os.path.isfile(path)
            with open(path, "r") as fp:
                data = json.load(fp)
            if "@graph" in data:
                for item in data["@graph"]:
                    if "@type" in item:
                        cls = lookup_type(item["@type"])
                        node = cls.from_jsonld(item)
                    else:
                        # allow links to metadata instances outside this collection
                        if not item["@id"].startswith("http"):
                            raise ValueError("Local nodes must have @type specified")
                        node = Link(item["@id"])
                    self.add(node)
            else:
                if "@type" in data:
                    cls = lookup_type(data["@type"])
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

    def validate(self):
        """
        Check whether all constraints are satisfied.

        Returns a dict containing information about any validation failures.
        """
        all_failures = {}
        for node in self:
            failures = node.validate()
            if failures:
                all_failures[node.id] = failures
        return all_failures

    @property
    def is_valid(self):
        failures = self.validate()
        return len(failures) == 0
