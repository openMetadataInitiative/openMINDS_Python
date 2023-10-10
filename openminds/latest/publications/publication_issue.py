"""
<description not available>
"""

# this file was auto-generated!


from openminds.base import LinkedMetadata
from openminds.properties import Property


class PublicationIssue(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/publications/PublicationIssue"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "is_part_of",
            "openminds.latest.publications.PublicationVolume",
            "isPartOf",
            required=True,
            description="Reference to the ensemble of multiple things or beings.",
            instructions="Add the publication volume this publication issue is part of.",
        ),
        Property(
            "issue_number",
            str,
            "issueNumber",
            formatting="text/plain",
            required=True,
            description="no description available",
            instructions="Enter the issue number of this publication issue.",
        ),
    ]

    def __init__(self, id=None, is_part_of=None, issue_number=None):
        return super().__init__(
            id=id,
            is_part_of=is_part_of,
            issue_number=issue_number,
        )
