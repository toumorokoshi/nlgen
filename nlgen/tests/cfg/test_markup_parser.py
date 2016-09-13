from nlgen.cfg.markup import parse_cfg_string


def test_simple_case():
    result = parse_cfg_string("SENTENCE->PRONOUN")
