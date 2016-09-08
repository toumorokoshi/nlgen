from nlgen.cfg import CFG, Terminal, ProductionRef


def test_simple_production_ref():
    cfg = CFG([
        ("S", Terminal("foo")),
    ])
    expect = [(Terminal("foo"),)]
    result = list(cfg.permutations(ProductionRef("S")))
    assert expect == result
