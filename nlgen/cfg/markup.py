"""
it is typically more convenient to use a markup language to define grammars,
instead of using the programmatic interface. This handles the parsing.
"""
from .markup_parser import CFGMarkupParser
from .production import (
    ProductionUnion, Production, ProductionRef, Terminal
)


def parse_production(text):
    """ generate a production from the standard cfg notation of NLGEN. """
    semantics = ProductionSemantics()
    parser = CFGMarkupParser(semantics=semantics)
    ast = parser.parse(text, "production")
    return ast


class ProductionSemantics(object):

    def terminal(self, ast):
        return Terminal(ast.value)

    def reference(self, ast):
        return ProductionRef(ast.key)

    def production(self, ast):
        return Production(ast.production_list)
