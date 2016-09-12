from nlgen.cfg import CFG, Terminal, ProductionRef


def test_simple_production_ref():
    cfg = CFG([
        ("S", Terminal("foo")),
    ])
    expect = [("foo",)]
    result = list(cfg.permutation_values(ProductionRef("S")))
    assert expect == result
