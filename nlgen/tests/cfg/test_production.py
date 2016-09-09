from nlgen.cfg import CFG, Terminal, ProductionRef, Production


def test_simple_production():
    cfg = CFG([
        ("S", Production([Terminal("foo"), Terminal("bar")]))
    ])
    expect = [("foo", "bar")]
    result = list(cfg.permutations("S"))
    assert expect == result
