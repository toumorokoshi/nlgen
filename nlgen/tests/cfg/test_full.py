from nlgen.cfg import CFG, PList, PRef, PTerminal


def test_full_example():
    my_cfg = CFG([
        ("PRONOUN", PTerminal("I")),
        ("VERB", PTerminal("have")),
        ("NOUN", PTerminal("candy")),
        ("NOUN", PTerminal("bonbons")),
        ("SENTENCE", PList([
            PRef("PRONOUN"),
            PRef("VERB"),
            PRef("NOUN")
        ]))
    ])
    result = set(my_cfg.permutation_values("SENTENCE"))
    expect = set([
        ("I", "have", "candy"),
        ("I", "have", "bonbons"),
    ])


def test_feature_mismatch():
    """ a feature mismatch should result """
    my_cfg = CFG([
        ("PRONOUN", PTerminal("I", features={"person": set("1")})),
        ("PRONOUN", PTerminal("You", features={"person": set("2")})),
        ("VERB", PTerminal("have", features={"person": set("2")})),
        ("NOUN", PTerminal("candy")),
        ("SENTENCE", PList([
            PRef("PRONOUN"),
            PRef("VERB"),
            PRef("NOUN")
        ]))
    ])
    result = set(my_cfg.permutation_values("SENTENCE"))
    expect = set([("You", "have", "candy")])
    assert result == expect
