from nlgen.cfg import CFG, Production, PRef, Terminal

# (optional) a list of productions can be passed in, as
# the first argument.
my_cfg = CFG(
    [
        ("PRONOUN", Terminal("I", feature={"person": 1})),
        ("VERB", Terminal("have", feature={"tense": "present", "person": 1})),
        # features are optional
        ("NOUN", Terminal("candy")),
        # a value of a production can be a list of
        # string or production references, as well.
        ("SENTENCE", ProductionList(
            [PRef("PRONOUN"), Terminal(""),
             PRef("VERB"), Terminal(""),
             PRef("NOUN")]
        )),
        # as a convenience, NLTK's fcfg notation is also parsed.
        ("SENTENCE", Production.fromstring("PRONOUN VERB NOUN"))
    ]
)

# productions can also be added later.
my_cfg.add(
    # adding the same production will add to any existing productions.
    # in this case, VERB = 'gave' | 'have'
    Production("VERB", "gave", features={"person": 1, "tense": "present"})
)

# you can ask productions for a list of all valid productions:

valid_sentences = [s for s in my_cfg.permutations("SENTENCE")]

# by default, cfgs will require agreement between all features within a sentence.
# TODO: allow optional agreement.

# you can also require that certain terminals must be used:

valid_sentence_matching_requirements = next(my_cfg.permutations(
    "SENTENCE", required_terminals=["I", "have", "candy"]
))

# and you can pass in a new production, against the existing grammar.

my_cfg.permutations(
    Production("SENTENCE", "PRONOUN VERB NOUN")
)
