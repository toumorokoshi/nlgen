from nlgen.cfg import CFG, Terminal


def test_simple_case():
    cfg = CFG([
        ("S", Terminal("foo"))
    ])
    assert list(cfg.permutations("S")) == [(Terminal("foo"),)]


def test_multiple_productions_same_rule():
    cfg = CFG([
        ("S", Terminal("foo")),
        ("S", Terminal("bar"))
    ])
    result = cfg.permutations("S")
    expect = [(Terminal("foo"),), (Terminal("bar"),)]
    assert set(result) == set(expect)
