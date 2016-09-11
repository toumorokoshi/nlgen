import pytest
from nlgen.exception import IncongruentFeature
from nlgen.cfg.feature import unify_features


def test_feature():
    left = {"gender": set(["male"]), "person": set([1])}
    right = {"gender": set(["male"]), "person": set([1])}
    expect = {"gender": set(["male"]), "person": set([1])}
    assert unify_features(left, right) == expect


def test_incongruent_feature():
    left = {"gender": set(["female"]), "person": set([1])}
    right = {"gender": set(["male"]), "person": set([1])}
    with pytest.raises(IncongruentFeature):
        unify_features(left, right)


def test_incongruent_feature_ignores_incongruent_field():
    left = {"gender": set(["female"]), "person": set([1])}
    right = {"gender": set(["male"]), "person": set([1])}
    result = unify_features(left, right, match_required=set(["person"]))
    assert result == {"gender": set(["female", "male"]), "person": set([1])}
