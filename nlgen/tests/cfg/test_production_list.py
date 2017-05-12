from nlgen.cfg import CFG, PTerminal, PList, PRef, PUnion


def test_simple_production():
    cfg = CFG([
        ("S", PList([PTerminal("foo"), PTerminal("bar")]))
    ])
    expect = [("foo", "bar")]
    result = list(cfg.permutation_values("S"))
    assert expect == result


def test_equality():
    assert (PList([PTerminal("foo"), PTerminal("bar")])
            ==
            PList([PTerminal("foo"), PTerminal("bar")]))
    assert not (PList([PTerminal("foo"), PTerminal("bar")])
                !=
                PList([PTerminal("foo"), PTerminal("bar")]))


def test_list_with_features():
    """
    if a feature is passed into the list, it will only
    accept a collected feature set that matches.
    """
    cfg = CFG([
        ("AB_UPPER", PList([PRef("A"), PRef("B")],
                           features={"case": "upper"})),
        ("AB_LOWER", PList([PRef("A"), PRef("B")],
                           features={"case": "lower"})),
        ("A", PUnion(
            [PTerminal("a", features={"case": "lower"}),
             PTerminal("A", features={"case": "upper"})]
        )),
        ("B", PUnion(
            [PTerminal("b", features={"case": "lower"}),
             PTerminal("B", features={"case": "upper"})]
        ))
    ])
    assert list(cfg.permutation_values("AB_UPPER")) == [("A", "B")]
    assert list(cfg.permutation_values("AB_LOWER")) == [("a", "b")]
