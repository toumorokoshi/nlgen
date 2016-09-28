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
