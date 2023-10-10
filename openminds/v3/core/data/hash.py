"""
Structured information on a hash.
"""

# this file was auto-generated!


from openminds.base import EmbeddedMetadata
from openminds.properties import Property


class Hash(EmbeddedMetadata):
    """
    Structured information on a hash.
    """

    type_ = "https://openminds.ebrains.eu/core/Hash"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "v3.0"

    properties = [
        Property(
            "algorithm",
            str,
            "algorithm",
            formatting="text/plain",
            required=True,
            description="Procedure for solving a mathematical problem in a finite number of steps. Can involve repetition of an operation.",
            instructions="Enter the algorithm used to generate this hash.",
        ),
        Property(
            "digest",
            str,
            "digest",
            formatting="text/plain",
            required=True,
            description="Summation or condensation of a body of information.",
            instructions="Enter the digest of this hash.",
        ),
    ]

    def __init__(self, algorithm=None, digest=None):
        return super().__init__(
            algorithm=algorithm,
            digest=digest,
        )
