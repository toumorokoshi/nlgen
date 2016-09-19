from nlgen.cfg import (
    CFG,
    read_production,
    read_cfg,
    Production, ProductionRef,
    Terminal
)


def test_simple_case():
    result = read_production("PRONOUN VI NOUN")
    assert result == Production([
        ProductionRef("PRONOUN"),
        ProductionRef("VI"),
        ProductionRef("NOUN"),
    ])

CFG_EXAMPLE = """
SENTENCE -> PRONOUN VERB NOUN;
PRONOUN -> "I";
VERB -> "have";
NOUN -> "tickets";
"""


def test_cfg():
    result = read_cfg(CFG_EXAMPLE)
    assert CFG([
        ("SENTENCE", Production([ProductionRef("PRONOUN"),
                                 ProductionRef("VERB"),
                                 ProductionRef("NOUN")])),
        ("PRONOUN", Terminal("I")),
        ("VERB", Terminal("have")),
        ("NOUN", Terminal("tickets"))
    ]) == result
