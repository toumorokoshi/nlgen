from nlgen.cfg import CFG, ProductionList, ProductionRef, Terminal


def test_full_example():
    my_cfg = CFG([
        ("PRONOUN", Terminal("I")),
        ("VERB", Terminal("have")),
        ("NOUN", Terminal("candy")),
        ("NOUN", Terminal("bonbons")),
        ("SENTENCE", ProductionList([
            ProductionRef("PRONOUN"),
            ProductionRef("VERB"),
            ProductionRef("NOUN")
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
        ("PRONOUN", Terminal("I", features={"person": set("1")})),
        ("PRONOUN", Terminal("You", features={"person": set("2")})),
        ("VERB", Terminal("have", features={"person": set("2")})),
        ("NOUN", Terminal("candy")),
        ("SENTENCE", ProductionList([
            ProductionRef("PRONOUN"),
            ProductionRef("VERB"),
            ProductionRef("NOUN")
        ]))
    ])
    result = set(my_cfg.permutation_values("SENTENCE"))
    expect = set([("You", "have", "candy")])
    assert result == expect
