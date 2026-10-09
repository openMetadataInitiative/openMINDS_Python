"""
Tests for the name-matching helpers in `openminds.base`, 
and for the parts of the `by_name()` contract that depend on them.
"""

import pytest

import openminds.latest
import openminds.v4
from openminds.base import (
    MATCH_TYPES,
    NAMELIKE_PROPERTIES,
    matches_name,
    normalize_name,
    remove_accents,
)


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Müller", "Muller"),
        ("République française", "Republique francaise"),
        ("Azərbaycan Respublikası", "Azerbaycan Respublikasi"),
        ("Straße", "Strasse"),
        ("Œuvre", "OEuvre"),
        ("Ångström", "Angstrom"),
        ("plain text", "plain text"),
    ],
)
def test_remove_accents(text, expected):
    assert remove_accents(text) == expected


def test_normalize_name():
    assert normalize_name("Raphé") == "Raphé"
    assert normalize_name("Raphé", case_sensitive=False) == "raphé"
    assert normalize_name("Raphé", ignore_accents=True) == "Raphe"
    assert normalize_name("Raphé", case_sensitive=False, ignore_accents=True) == "raphe"
    assert normalize_name("CLARITY/TDE") == "CLARITY/TDE"
    assert normalize_name("CLARITY/TDE", ignore_separators=True) == "CLARITY TDE"
    assert normalize_name("two-photon  imaging", ignore_separators=True) == "two photon imaging"


class TestMatchesName:
    def test_equals_is_case_sensitive_by_default(self):
        assert matches_name("Mus musculus", "Mus musculus")
        assert not matches_name("Mus musculus", "mus musculus")
        assert matches_name("Mus musculus", "mus musculus", case_sensitive=False)

    def test_accents(self):
        assert not matches_name("République française", "Republique francaise")
        assert matches_name("République française", "Republique francaise", ignore_accents=True)
        assert matches_name("Republique francaise", "République française", ignore_accents=True)

    def test_contains(self):
        assert matches_name("Mus musculus", "musculus", match="contains")
        assert not matches_name("musculus", "Mus musculus", match="contains")

    def test_within(self):
        assert matches_name("Mus musculus", "Mus musculus - House mouse", match="within")
        assert not matches_name("Mus musculus - House mouse", "Mus musculus", match="within")

    def test_separators(self):
        assert not matches_name("CLARITY/TDE", "CLARITY-TDE")
        assert matches_name("CLARITY/TDE", "CLARITY-TDE", ignore_separators=True)
        assert matches_name("CLARITY/TDE", "CLARITY   TDE", ignore_separators=True)
        assert matches_name("two-photon fluorescence microscopy", "two photon fluorescence microscopy",
                            ignore_separators=True)

    def test_invalid_match(self):
        with pytest.raises(ValueError):
            matches_name("a", "a", match="approximately")

    def test_match_types(self):
        assert MATCH_TYPES == ("equals", "contains", "within")


@pytest.mark.parametrize("om", [openminds.latest])
class TestByNameUsesMatchesName:
    """`by_name()` must apply exactly the rules `matches_name()` describes."""

    @staticmethod
    def namelike_values(instance):
        """Every value `by_name()` is expected to compare the query against."""
        values = [getattr(instance, prop_name, None) for prop_name in NAMELIKE_PROPERTIES]
        values += list(instance.synonyms or []) if hasattr(instance, "synonyms") else []
        return [value for value in values if value is not None]

    @pytest.mark.parametrize("match", MATCH_TYPES)
    @pytest.mark.parametrize("case_sensitive", [True, False])
    @pytest.mark.parametrize("ignore_accents", [True, False])
    @pytest.mark.parametrize("ignore_separators", [True, False])
    def test_agreement(self, om, match, case_sensitive, ignore_accents, ignore_separators):
        SovereignState = om.controlled_terms.SovereignState
        query = "Republique francaise"
        options = dict(
            match=match,
            case_sensitive=case_sensitive,
            ignore_accents=ignore_accents,
            ignore_separators=ignore_separators,
        )
        found = SovereignState.by_name(query, all=True, **options)
        expected = [
            state
            for state in SovereignState.instances()
            if any(matches_name(name, query, **options) for name in self.namelike_values(state))
        ]
        # every matching instance must be returned, once each, and no others
        assert sorted(state.id for state in found or []) == sorted(state.id for state in expected)
        if not expected:
            assert found is None

    def test_invalid_match_is_rejected(self, om):
        with pytest.raises(ValueError):
            om.controlled_terms.Species.by_name("Mus musculus", match="approximately")
