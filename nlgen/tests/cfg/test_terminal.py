from nlgen.cfg import CFG, Terminal


def test_simple_terminal():
    cfg = CFG([
        ("S", Terminal("foo"))
    ])
    assert list(cfg.permutations("S")) == [("foo",)]
