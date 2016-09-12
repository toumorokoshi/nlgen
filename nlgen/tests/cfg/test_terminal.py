from nlgen.cfg import CFG, Terminal


def test_simple_terminal():
    cfg = CFG([
        ("S", Terminal("foo"))
    ])
    assert list(cfg.permutation_values("S")) == [("foo",)]
