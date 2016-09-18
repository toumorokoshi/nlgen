from nlgen.cfg import (
    read_production,
    read_cfg,
    Production, ProductionRef
)


def test_simple_case():
    result = read_production("PRONOUN VI NOUN")
    assert result == Production([
        ProductionRef("PRONOUN"),
        ProductionRef("VI"),
        ProductionRef("NOUN"),
    ])

CFG = """
SENTENCE -> PRONOUN VERB NOUN
PRONOUN -> "I"
VERB -> "have"
NOUN -> "tickets"
"""


def test_cfg():
    result = read_cfg(CFG)
