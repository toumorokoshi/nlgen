import pytest
from nlgen.exception import IncongruentFeature
from nlgen.cfg.feature import unify_features


def test_feature():
    left = {"gender": set(["male"]), "person": set([1])}
    right = {"gender": set(["male"]), "person": set([1])}
    expect = {"gender": set(["male"]), "person": set([1])}
    assert unify_features(left, right) == expect


def test_empty_features():
    """ empty feature values on one side should default to the other side's values. """
    left = {"person": set([1])}
    right = {"gender": set(["male"])}
    expect = {"gender": set(["male"]), "person": set([1])}
    assert unify_features(left, right) == expect


def test_incongruent_feature():
    left = {"gender": set(["female"]), "person": set([1])}
    right = {"gender": set(["male"]), "person": set([1])}
    with pytest.raises(IncongruentFeature):
        unify_features(left, right)


def test_incongruent_feature_includes_incongruent_field():
    left = {"gender": set(["female"]), "person": set([1])}
    right = {"gender": set(["male"]), "person": set([1])}
    result = unify_features(left, right, match_required=set(["person"]))
    assert result == {"gender": set(), "person": set([1])}


def test_ignore():
    left = {"gender": set(["female"]), "person": set([1])}
    right = {"gender": set(["male"]), "person": set([1])}
    result = unify_features(left, right, ignore=True)
    assert result == {}


def test_ignore_selection():
    left = {"gender": set(["female"]), "person": set([1])}
    right = {"gender": set(["male"]), "person": set([1])}
    result = unify_features(left, right, ignore=["gender"])
    assert result == {"person": set([1])}


def test_explicit_emptiness_ensures_no_match():
    """
    distinguish between explicit emptiness, and allowing all.

    sometimes, it may be important to distinguish between an explicitly
    empty feature (which will thus have no match), and a FeatureSet that
    doesn't care about that particular feature.

    None is used to denote ignoring, and an empty set is used to
    denote allowing no matches.
    """
    with pytest.raises(IncongruentFeature):
        unify_features({"gender": set()}, {"gender": set(["male"])})

    result = unify_features({"gender": None}, {"gender": set(["male"])})
    assert result == {"gender": set(["male"])}
