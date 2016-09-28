from nlgen.cfg import CFG, PTerminal, PList


def test_simple_production():
    cfg = CFG([
        ("S", PList([PTerminal("foo"), PTerminal("bar")]))
    ])
    expect = [("foo", "bar")]
    result = list(cfg.permutation_values("S"))
    assert expect == result


def test_equality():
    assert (PList([PTerminal("foo"), PTerminal("bar")])
            ==
            PList([PTerminal("foo"), PTerminal("bar")]))
    assert not (PList([PTerminal("foo"), PTerminal("bar")])
                !=
                PList([PTerminal("foo"), PTerminal("bar")]))
