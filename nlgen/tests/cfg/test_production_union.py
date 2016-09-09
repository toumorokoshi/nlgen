from nlgen.cfg import CFG, Terminal, ProductionUnion


def test_simple_production_union():
    cfg = CFG([
        ("S", ProductionUnion([
            Terminal("foo"),
            Terminal("bar")
        ])),
    ])
    expect = [("foo",), ("bar",)]
    result = list(cfg.permutations("S"))
    assert expect == result
