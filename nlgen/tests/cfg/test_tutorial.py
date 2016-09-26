from nlgen.cfg import read_cfg

EXAMPLE_NO_FEATURE = """
# example.nlcfg
SENTENCE -> PRONOUN VI NOUN;
VI -> VERB;
PRONOUN -> "I";
VERB -> "play";
NOUN -> "blackjack" | "poker";
""".strip()


def test_no_feature_example():
    cfg = read_cfg(EXAMPLE_NO_FEATURE)
    # permutations returns a generator.
    # we use sets for comparisons as there's
    # no guaranteed order for generated
    # values.
    assert set(cfg.permutation_values("SENTENCE")) == set([
        ("I", "play", "blackjack"),
        ("I", "play", "poker"),
    ])

EXAMPLE_WITH_FEATURE = """
# example.nlcfg
SENTENCE -> PRONOUN VI NOUN;
VI -> VERB;
PRONOUN -> "I" {"person": 1} |
           "you" {"person": "2"} |
           "she" {"person": 3};
VERB -> "play"  {"person": ["1", "2"]} |
        "plays" {"person": 3};
NOUN -> "blackjack" | "poker";
"""


def test_with_feature_example():
    cfg = read_cfg(EXAMPLE_WITH_FEATURE)
    # permutations returns a generator.
    # we use sets for comparisons as there's
    # no guaranteed order for generated
    # values.
    assert set(cfg.permutation_values("SENTENCE")) == set([
        ("I", "play", "blackjack"),
        ("you", "play", "blackjack"),
        ("she", "plays", "blackjack"),
        ("I", "play", "poker"),
        ("you", "play", "poker"),
        ("she", "plays", "poker"),
    ])
