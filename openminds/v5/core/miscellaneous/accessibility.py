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
    schema_version = "v5.0"

    properties = [
        Property(
            "channel",
            "openminds.v5.controlled_terms.AccessChannel",
            "channel",
            required=True,
            description="no description available",
            instructions="Add the relevant access channel indicating where access takes place (physical, virtual, or hybrid).",
        ),
        Property(
            "eligibility",
            "openminds.v5.controlled_terms.AccessEligibilityType",
            "eligibility",
            required=True,
            description="no description available",
            instructions="Add the relevant access eligibility type indicating who is allowed to access (open, controlled, or restricted).",
        ),
        Property(
            "form",
            "openminds.v5.controlled_terms.AccessForm",
            "form",
            required=True,
            description="no description available",
            instructions="Add the relevant access form indicating whether the user interacts directly or through mediation.",
        ),
        Property(
            "payment_models",
            "openminds.v5.controlled_terms.PaymentModelType",
            "paymentModel",
            multiple=True,
            unique_items=True,
            min_items=1,
            required=True,
            description="no description available",
            instructions="Add all relevant payment model types indicating how access costs are determined. If no payment is requires, select zero-cost payment model.",
        ),
        Property(
            "process",
            "openminds.v5.controlled_terms.AccessProcessType",
            "process",
            required=True,
            description="no description available",
            instructions="Add the relevant access process type indicating how access is granted (immediate, registered, authenticated, or authorized).",
        ),
    ]

    def __init__(self, id=None, channel=None, eligibility=None, form=None, payment_models=None, process=None):
        return super().__init__(
            id=id,
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
        case_sensitive: bool = True,
    ):
        """
        Search for instances in the openMINDS instance library based on their name.

        This includes properties "name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation", and "synonyms".

        Note that not all metadata classes have a name.

        Args:
            name (str): a string to search for.
            match (str, optional): either "equals" (exact match - default), "contains"
                (the name-like property contains the given string), or "within"
                (the given string contains the name-like property).
            all (bool, optional): Whether to return all objects that match the name, or only the first. Defaults to False.
            case_sensitive (bool, optional): Whether the search should be case-sensitive. Defaults to True.
        """
        namelike_properties = ("name", "lookup_label", "family_name", "full_name", "short_name", "abbreviation")
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                keys = []
                for prop_name in namelike_properties:
                    value = getattr(instance, prop_name, None)
                    if value is not None:
                        keys.append(value)
                if hasattr(instance, "synonyms"):
                    for synonym in instance.synonyms or []:
                        keys.append(synonym)
                for key in keys:
                    if key in cls._instance_lookup:
                        cls._instance_lookup[key].append(instance)
                    else:
                        cls._instance_lookup[key] = [instance]

        def normalize(s):
            return s if case_sensitive else s.casefold()

        if match == "equals":
            if case_sensitive:
                matches = cls._instance_lookup.get(name, [])
            else:
                matches = []
                for key, instances in cls._instance_lookup.items():
                    if key.casefold() == name.casefold():
                        matches.extend(instances)
        elif match == "contains":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if normalize(name) in normalize(key):
                    matches.extend(instances)
        elif match == "within":
            matches = []
            for key, instances in cls._instance_lookup.items():
                if normalize(key) in normalize(name):
                    matches.extend(instances)
        else:
            raise ValueError("'match' must be either 'equals', 'contains', or 'within'")
        if not matches:
            return None
        elif all:
            return list(dict.fromkeys(matches))
        else:
            return matches[0]


from . import accessibility_instances as _  # noqa: F401
