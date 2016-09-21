from nlgen.cfg import CFG, Terminal


def test_simple_terminal():
    cfg = CFG([
        ("S", Terminal("foo"))
    ])
    assert list(cfg.permutation_values("S")) == [("foo",)]


def test_equal():
    assert (Terminal("I", features={"person": "1"}) ==
            Terminal("I", features={"person": "1"}))


def test_coerce_features():
    """ we should be able to coerce common feature descriptions. """
    # string as value
    assert Terminal("foo", features={"num": "1"}).features == {"num": {"1"}}
    # list as value
    assert Terminal("foo", features={"num": ["1", "2"]}).features == {"num": {"1", "2"}}
    # coerce all else as strings.
    assert Terminal("foo", features={"num": 1}).features == {"num": {"1"}}
