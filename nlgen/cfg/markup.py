"""
it is typically more convenient to use a markup language to define grammars,
instead of using the programmatic interface. This handles the parsing.
"""
import json
from .markup_parser import CFGMarkupParser
from .cfg import CFG
from .production import (
    ProductionUnion, Production,
    ProductionRef, Terminal
)


def read_production(text):
    """ generate a production from the standard cfg notation of NLGEN. """
    semantics = ProductionSemantics()
    parser = CFGMarkupParser(semantics=semantics)
    ast = parser.parse(text, "production")
    return ast


def read_cfg(text):
    semantics = ProductionSemantics()
    parser = CFGMarkupParser(semantics=semantics)
    ast = parser.parse(text, "CFG")
    return ast


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
            return ProductionUnion([ast.head] + rest)
        return ast.head

    def production_list(self, ast):
        return Production([ast.head] + ast.rest)

    def terminal(self, ast):
        features = ast.features
        if features is not None:
            features = json.loads("".join(features))
        return Terminal(ast.value, features=features)

    def reference(self, ast):
        return ProductionRef(ast.key)
