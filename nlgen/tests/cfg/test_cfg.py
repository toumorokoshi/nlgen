from nlgen.cfg import CFG, Terminal


def test_multiple_productions_same_rule():
    cfg = CFG([
        ("S", Terminal("foo")),
        ("S", Terminal("bar"))
    ])
    result = cfg.permutations("S")
    expect = [("foo",), ("bar",)]
    assert set(result) == set(expect)
