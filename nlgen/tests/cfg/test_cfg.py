from nlgen.cfg import CFG, Terminal


def test_multiple_productions_same_rule():
    cfg = CFG([
        ("S", Terminal("foo")),
        ("S", Terminal("bar"))
    ])
    result = cfg.permutation_values("S")
    expect = [("foo",), ("bar",)]
    assert set(result) == set(expect)


def test_equality():
    lhs = CFG([
        ("S", Terminal("foo")),
        ("S", Terminal("bar"))
    ])
    rhs = CFG([
        ("S", Terminal("foo")),
        ("S", Terminal("bar"))
    ])
    assert lhs == rhs
