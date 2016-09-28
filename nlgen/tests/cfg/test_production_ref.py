from nlgen.cfg import CFG, PTerminal, PRef


def test_simple_production_ref():
    cfg = CFG([
        ("S", PTerminal("foo")),
    ])
    expect = [("foo",)]
    result = list(cfg.permutation_values(PRef("S")))
    assert expect == result
