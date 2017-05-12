import pytest
from nlgen.cfg import CFG, PTerminal


def test_multiple_productions_same_rule():
    cfg = CFG([
        ("S", PTerminal("foo")),
        ("S", PTerminal("bar"))
    ])
    result = cfg.permutation_values("S")
    expect = [("foo",), ("bar",)]
    assert set(result) == set(expect)


def test_equality():
    lhs = CFG([
        ("S", PTerminal("foo")),
        ("S", PTerminal("bar"))
    ])
    rhs = CFG([
        ("S", PTerminal("foo")),
        ("S", PTerminal("bar"))
    ])
    assert lhs == rhs


@pytest.mark.parametrize("features,expected", [
    ({"person": 1}, {("I",)}),
    ({"person": 2}, {("you",)}),
    ({"person": 3}, {("she", ), ("he", )}),
    ({"person": 3, "gender": "m"}, {("he", )}),
    ({"person": 2, "gender": "m"}, {("you", )}),
])
def test_passing_features(features, expected):
    """ asking for a permutation with specific features should work. """
    cfg = CFG([
        ("S", PTerminal("I", features={"person": 1})),
        ("S", PTerminal("you", features={"person": 2})),
        ("S", PTerminal("he", features={"person": 3, "gender": "m"})),
        ("S", PTerminal("she", features={"person": 3, "gender": "f"}))
    ])
    print(expected)
    print(set(cfg.permutation_values("S", features=features)))
    assert set(cfg.permutation_values("S", features=features)) == expected
