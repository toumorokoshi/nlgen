from nlgen.cfg.markup import parse_production
from nlgen.cfg import (
    Production, ProductionRef
)


def test_simple_case():
    result = parse_production("PRONOUN VI NOUN")
    assert result == Production([
        ProductionRef("PRONOUN"),
        ProductionRef("VI"),
        ProductionRef("NOUN"),
    ])
