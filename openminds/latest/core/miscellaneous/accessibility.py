"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Accessibility(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.om-i.org/types/Accessibility"
    context = {"@vocab": "https://openminds.om-i.org/props/"}
    schema_version = "latest"

    properties = [
        Property(
            "application",
            str,
            "application",
            formatting="text/plain",
            description="no description available",
            instructions="Enter guidance on when this access type should be selected. Describe the applicable access conditions, eligibility criteria, or usage scenario that distinguishes it from the other access types.",
        ),
        Property(
            "channel",
            "openminds.latest.controlled_terms.AccessChannel",
            "channel",
            required=True,
            description="no description available",
            instructions="Add the relevant access channel indicating where access takes place (physical, virtual, or hybrid).",
        ),
        Property(
            "eligibility",
            "openminds.latest.controlled_terms.AccessEligibilityType",
            "eligibility",
            required=True,
            description="no description available",
            instructions="Add the relevant access eligibility type indicating who is allowed to access (open, controlled, or restricted).",
        ),
        Property(
            "form",
            "openminds.latest.controlled_terms.AccessForm",
            "form",
            required=True,
            description="no description available",
            instructions="Add the relevant access form indicating whether the user interacts directly or through mediation.",
        ),
        Property(
            "payment_models",
            "openminds.latest.controlled_terms.PaymentModelType",
            "paymentModel",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all relevant payment model types indicating how access costs are determined. If no payment is required, select zero-cost payment model.",
        ),
        Property(
            "process",
            "openminds.latest.controlled_terms.AccessProcessType",
            "process",
            required=True,
            description="no description available",
            instructions="Add the relevant access process type indicating how access is granted (immediate, registered, authenticated, or authorized).",
        ),
    ]

    def __init__(
        self, id=None, application=None, channel=None, eligibility=None, form=None, payment_models=None, process=None
    ):
        return super().__init__(
            id=id,
            application=application,
            channel=channel,
            eligibility=eligibility,
            form=form,
            payment_models=payment_models,
            process=process,
        )

    @classmethod
    def instances(cls):
        return [value for value in cls.__dict__.values() if isinstance(value, cls)]

    @classmethod
    def by_name(
        cls,
        name: str,
        match: str = "equals",
        all: bool = False,
    ):
        """
        Search for instances in the openMINDS instance library based on their name.

        This includes properties "name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation", and "synonyms".

        Note that not all metadata classes have a name.

        Args:
            name (str): a string to search for.
            match (str, optional): either "equals" (exact match - default) or "contains".
            all (bool, optional): Whether to return all objects that match the name, or only the first. Defaults to False.
        """
        namelike_properties = ("name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation")
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                keys = []
                for prop_name in namelike_properties:
                    if hasattr(instance, prop_name):
                        keys.append(getattr(instance, prop_name))
                if hasattr(instance, "synonyms"):
                    for synonym in instance.synonyms or []:
                        keys.append(synonym)
                for key in keys:
                    if key in cls._instance_lookup:
                        cls._instance_lookup[key].append(instance)
                    else:
                        cls._instance_lookup[key] = [instance]
        if match == "equals":
            matches = cls._instance_lookup.get(name, [])
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if name in key:
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals' or 'contains'")
        if not matches:
            return None
        elif all:
            return matches
        else:
            return matches[0]


from . import accessibility_instances as _  # noqa: F401
