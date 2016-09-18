from nlgen.cfg import CFG, Terminal, ProductionUnion


def test_simple_production_union():
    cfg = CFG([
        ("S", ProductionUnion([
            Terminal("foo"),
            Terminal("bar")
        ])),
    ])
    expect = [("foo",), ("bar",)]
    result = list(cfg.permutation_values("S"))
    assert expect == result


def test_equality():
    assert (ProductionUnion([Terminal("foo"), Terminal("bar")])
            ==
            ProductionUnion([Terminal("foo"), Terminal("bar")]))
