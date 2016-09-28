from nlgen.cfg import CFG, PTerminal


def test_simple_terminal():
    cfg = CFG([
        ("S", PTerminal("foo"))
    ])
    assert list(cfg.permutation_values("S")) == [("foo",)]


def test_equal():
    assert (PTerminal("I", features={"person": "1"}) ==
            PTerminal("I", features={"person": "1"}))


def test_coerce_features():
    """ we should be able to coerce common feature descriptions. """
    # string as value
    assert PTerminal("foo", features={"num": "1"}).features == {"num": {"1"}}
    # list as value
    assert PTerminal("foo", features={"num": ["1", "2"]}).features == {"num": {"1", "2"}}
    # coerce all else as strings.
    assert PTerminal("foo", features={"num": 1}).features == {"num": {"1"}}
