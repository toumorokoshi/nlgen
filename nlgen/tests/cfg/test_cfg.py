from nlgen.cfg import CFG, Terminal


def test_simple_case():
    cfg = CFG([
        ("S", Terminal("foo"))
    ])
    assert list(cfg.permutations) == [Terminal("foo")]
