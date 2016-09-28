"""
it is typically more convenient to use a markup language to define grammars,
instead of using the programmatic interface. This handles the parsing.
"""
import json
from .markup_parser import CFGMarkupParser
from .cfg import CFG
from .production import (
    PUnion, PList,
    PRef, PTerminal
)


def read_production(text):
    """ generate a production from the standard cfg notation of NLGEN. """
    return _get_parser().parse(text, "production")


def read_cfg(text):
    return _get_parser().parse(text, "CFG")


def _get_parser():
    semantics = ProductionSemantics()
    return CFGMarkupParser(
        semantics=semantics
    )


class ProductionSemantics(object):

    def CFG(self, ast):
        # remove the semicolon we don't care about.
        return CFG([el[0] for el in ast.named_production_list])

    def named_production(self, ast):
        return (ast.name, ast.production)

    def production(self, ast):
        if ast.rest:
            # remove unneeded "|"
            rest = [e[1] for e in ast.rest]
            return PUnion([ast.head] + rest)
        return ast.head

    def production_list(self, ast):
        return PList([ast.head] + ast.rest)

    def terminal(self, ast):
        features = ast.features
        if features is not None:
            features = json.loads("".join(features))
        return PTerminal(ast.value, features=features)

    def reference(self, ast):
        return PRef(ast.key)
