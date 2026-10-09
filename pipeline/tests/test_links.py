"""
Tests of Node.links and Node._direct_links.
"""

from openminds.latest.controlled_terms.age_reference import AgeReference
from openminds.latest.controlled_terms.species import Species
from openminds.latest.controlled_terms.unit_of_measurement import UnitOfMeasurement
from openminds.latest.core.miscellaneous.quantitative_value import QuantitativeValue
from openminds.latest.core.research.specimen_age import SpecimenAge
from openminds.latest.core.research.subject import Subject
from openminds.latest.core.research.subject_state import SubjectState


def build_state(label, weeks, previous=None):
    return SubjectState(
        lookup_label=label,
        descended_from=previous,
        age=SpecimenAge(
            age=QuantitativeValue(value=weeks, unit=UnitOfMeasurement.week),
            reference=AgeReference.birth,
        ),
    )


def test_direct_links_returns_only_direct_links():
    # only the first layer is returned
    first = SubjectState(lookup_label="first")
    second = SubjectState(lookup_label="second", descended_from=first)
    third = SubjectState(lookup_label="third", descended_from=second)
    assert third._direct_links == [second]


def test_direct_links_look_through_embedded_nodes():
    # embedded nodes (SpecimenAge, QuantitativeValue) are looked through
    state = build_state("s", 1)
    assert state._direct_links == [UnitOfMeasurement.week, AgeReference.birth]


def test_links_order_and_duplicates():
    # each directly linked node is followed by its own links (depth-first),
    # embedded nodes are looked through, and duplicates are kept
    week, birth = UnitOfMeasurement.week, AgeReference.birth
    a = build_state("A", 1)
    b = build_state("B", 2, previous=a)
    subject = Subject(lookup_label="S", species=Species.mus_musculus, studied_states=[a, b])

    assert subject.links == [Species.mus_musculus, a, week, birth, b, week, birth, a, week, birth]
