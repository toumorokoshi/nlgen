"""
it is typically more convenient to use a markup language to define grammars,
instead of using the programmatic interface. This handles the parsing.
"""
from .markup_parser import CFGMarkupParser
from grako.model import ModelBuilderSemantics


def parse_cfg_string(text):
    semantics = ModelBuilderSemantics()
    parser = CFGMarkupParser(semantics=semantics)
    return parser.parse(text, "cfg")
