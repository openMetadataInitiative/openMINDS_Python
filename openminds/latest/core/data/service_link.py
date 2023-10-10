"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class ServiceLink(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/core/ServiceLink"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "data_location",
            [
                "openminds.latest.core.File",
                "openminds.latest.core.FileArchive",
                "openminds.latest.core.FileBundle",
                "openminds.latest.core.ModelVersion",
                "openminds.latest.publications.LivePaperResourceItem",
                "openminds.latest.sands.ParcellationEntityVersion",
            ],
            "dataLocation",
            required=True,
            description="no description available",
            instructions="Add the location of the data that are linked to this specific service (e.g., stored as file (bundles) or registered as other entities such as atlas annotations).",
        ),
        Property(
            "display_label",
            str,
            "displayLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a display label for this service link.",
        ),
        Property(
            "open_data_in",
            IRI,
            "openDataIn",
            required=True,
            description="no description available",
            instructions="Enter the internationalized resource identifier (IRI) to the linked data in the specified service.",
        ),
        Property(
            "preview_image",
            "openminds.latest.core.File",
            "previewImage",
            description="no description available",
            instructions="Add an image file to this service link that acts as a preview of its content or could function as an icon.",
        ),
        Property(
            "service",
            "openminds.latest.controlled_terms.Service",
            "service",
            required=True,
            description="no description available",
            instructions="Add the service in which the specified data can be opened.",
        ),
    ]

    def __init__(
        self, id=None, data_location=None, display_label=None, open_data_in=None, preview_image=None, service=None
    ):
        return super().__init__(
            id=id,
            data_location=data_location,
            display_label=display_label,
            open_data_in=open_data_in,
            preview_image=preview_image,
            service=service,
        )
