from nlgen.cfg import (
    CFG,
    read_production,
    read_cfg,
    PList,
    PRef,
    PUnion,
    PTerminal
)


def test_simple_case():
    result = read_production("PRONOUN VI NOUN")
    assert result == PList([
        PRef("PRONOUN"),
        PRef("VI"),
        PRef("NOUN"),
    ])

CFG_EXAMPLE = """
SENTENCE -> PRONOUN VERB NOUN;
PRONOUN -> "I" {"person": "1"} | "You" {"person": "2"};
NOUN -> "tickets";
VERB -> "have";
""".strip()


def test_cfg():
    result = read_cfg(CFG_EXAMPLE)
    assert CFG([
        ("SENTENCE", PList([PRef("PRONOUN"),
                                     PRef("VERB"),
                                     PRef("NOUN")])),
        ("PRONOUN", PUnion([
            PTerminal("I", features={"person": "1"}),
            PTerminal("You", features={"person": "2"})
        ])),
        ("VERB", PTerminal("have")),
        ("NOUN", PTerminal("tickets"))
    ]) == result

WITH_COMMENTS = """
# start
PRONOUN -> "I";
# comment
VERB -> "play"; # foo
""".strip()


def test_comments():
    assert read_cfg(WITH_COMMENTS) == CFG([
        ("PRONOUN", PTerminal("I")),
        ("VERB", PTerminal("play"))
    ])
