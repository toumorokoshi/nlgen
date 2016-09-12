from nlgen.cfg import CFG, Terminal, ProductionRef, Production


def test_simple_production():
    cfg = CFG([
        ("S", Production([Terminal("foo"), Terminal("bar")]))
    ])
    expect = [("foo", "bar")]
    result = list(cfg.permutation_values("S"))
    assert expect == result
