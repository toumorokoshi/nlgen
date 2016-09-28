from nlgen.cfg import CFG, PTerminal, PUnion


def test_simple_production_union():
    cfg = CFG([
        ("S", PUnion([
            PTerminal("foo"),
            PTerminal("bar")
        ])),
    ])
    expect = [("foo",), ("bar",)]
    result = list(cfg.permutation_values("S"))
    assert expect == result


def test_equality():
    assert (PUnion([PTerminal("foo"), PTerminal("bar")])
            ==
            PUnion([PTerminal("foo"), PTerminal("bar")]))
