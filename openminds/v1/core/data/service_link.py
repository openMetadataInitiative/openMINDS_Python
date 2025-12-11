"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ServiceLink(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/ServiceLink"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v1.0"

    properties = [
        Property(
            "data_location",
            ["openminds.v1.core.File", "openminds.v1.core.FileBundle"],
            "dataLocation",
            required=True,
            description="no description available",
            instructions="Add the file or file bundle with the data that are linked to the specified service.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            description="Word or phrase that constitutes the distinctive designation of the service link.",
            instructions="Enter a name that should be used as preferred display label for this service link.",
        ),
        Property(
            "open_data_in",
            "openminds.v1.core.URL",
            "openDataIn",
            required=True,
            description="no description available",
            instructions="Add the uniform resource locator (URL) to open the linked data in the specified service.",
        ),
        Property(
            "service",
            "openminds.v1.controlled_terms.Service",
            "service",
            required=True,
            description="no description available",
            instructions="Add the service in which the specified data can be opened.",
        ),
    ]

    def __init__(self, id=None, data_location=None, name=None, open_data_in=None, service=None):
        return super().__init__(
            id=id,
            data_location=data_location,
            name=name,
            open_data_in=open_data_in,
            service=service,
        )
