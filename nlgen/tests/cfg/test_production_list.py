from nlgen.cfg import CFG, Terminal, ProductionList


def test_simple_production():
    cfg = CFG([
        ("S", ProductionList([Terminal("foo"), Terminal("bar")]))
    ])
    expect = [("foo", "bar")]
    result = list(cfg.permutation_values("S"))
    assert expect == result


def test_equality():
    assert (ProductionList([Terminal("foo"), Terminal("bar")])
            ==
            ProductionList([Terminal("foo"), Terminal("bar")]))
    assert not (ProductionList([Terminal("foo"), Terminal("bar")])
                !=
                ProductionList([Terminal("foo"), Terminal("bar")]))
