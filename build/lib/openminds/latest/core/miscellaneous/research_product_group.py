"""
<description not available>
"""

# this file was auto-generated!



from openminds.base import LinkedMetadata
from openminds.properties import Property


class ResearchProductGroup(LinkedMetadata):
    """
    <description not available>
    """
    type_ = ["https://openminds.ebrains.eu/core/ResearchProductGroup"]
    context = {
        "vocab": "https://openminds.ebrains.eu/vocab/"
    }

    properties = [
        Property(
            "context",
            str,
            "vocab:context",formatting="text/plain",
            
            required=True,
            description="no description available",
            instructions="Enter the common context for this research product group."
        ),
        Property(
            "has_part",
            ['openminds.latest.computation.ValidationTest', 'openminds.latest.computation.ValidationTestVersion', 'openminds.latest.computation.WorkflowRecipe', 'openminds.latest.computation.WorkflowRecipeVersion', 'openminds.latest.core.Dataset', 'openminds.latest.core.DatasetVersion', 'openminds.latest.core.MetaDataModel', 'openminds.latest.core.MetaDataModelVersion', 'openminds.latest.core.Model', 'openminds.latest.core.ModelVersion', 'openminds.latest.core.Software', 'openminds.latest.core.SoftwareVersion', 'openminds.latest.core.WebService', 'openminds.latest.core.WebServiceVersion', 'openminds.latest.publications.LivePaper', 'openminds.latest.publications.LivePaperVersion', 'openminds.latest.sands.BrainAtlas', 'openminds.latest.sands.BrainAtlasVersion', 'openminds.latest.sands.CommonCoordinateSpace', 'openminds.latest.sands.CommonCoordinateSpaceVersion'],
            "vocab:hasPart",
            multiple=True,
            unique_items=True,
            min_items=1,
            
            required=True,
            description="no description available",
            instructions="Add all research products (research product versions) that should be grouped under the given 'context'."
        ),
        
    ]

    def __init__(self, id=None, context=None, has_part=None):
        return super().__init__(id=id,context=context,has_part=has_part,)

