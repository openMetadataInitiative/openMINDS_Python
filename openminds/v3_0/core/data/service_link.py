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
    context = {"vocab": "https://openminds.ebrains.eu/vocab/"}

    properties = [
        Property(
            "data_location",
            [
                "openminds.v3_0.core.File",
                "openminds.v3_0.core.FileArchive",
                "openminds.v3_0.core.FileBundle",
                "openminds.v3_0.core.ModelVersion",
                "openminds.v3_0.publications.LivePaperResourceItem",
                "openminds.v3_0.sands.ParcellationEntityVersion",
            ],
            "vocab:dataLocation",
            required=True,
            description="no description available",
            instructions="Add the location of the data that are linked to this specific service (e.g., stored as file (bundles) or registered as other entities such as atlas annotations).",
        ),
        Property(
            "display_label",
            str,
            "vocab:displayLabel",
            formatting="text/plain",
            description="no description available",
            instructions="Enter a display label for this service link.",
        ),
        Property(
            "open_data_in",
            IRI,
            "vocab:openDataIn",
            required=True,
            description="no description available",
            instructions="Enter the internationalized resource identifier (IRI) to the linked data in the specified service.",
        ),
        Property(
            "preview_image",
            "openminds.v3_0.core.File",
            "vocab:previewImage",
            description="no description available",
            instructions="Add an image file to this service link that acts as a preview of its content or could function as an icon.",
        ),
        Property(
            "service",
            "openminds.v3_0.controlled_terms.Service",
            "vocab:service",
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