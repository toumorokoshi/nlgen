from nlgen.cfg import CFG, Production, ProductionRef, Terminal


def test_full_example():
    my_cfg = CFG([
        ("PRONOUN", Terminal("I")),
        ("VERB", Terminal("have")),
        ("NOUN", Terminal("candy")),
        ("NOUN", Terminal("bonbons")),
        ("SENTENCE", Production([
            ProductionRef("PRONOUN"),
            ProductionRef("VERB"),
            ProductionRef("NOUN")
        ]))
    ])
    result = set(my_cfg.permutations("SENTENCE"))
    expect = set([
        ("I", "have", "candy"),
        ("I", "have", "bonbons"),
    ])
