"""
it is typically more convenient to use a markup language to define grammars,
instead of using the programmatic interface. This handles the parsing.
"""
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

    def terminal(self, ast):
        return Terminal(ast.value)

    def reference(self, ast):
        return ProductionRef(ast.key)

    def production(self, ast):
        return Production([ast.single_production] + ast.production_list)

    def named_production(self, ast):
        return (ast.name, ast.production)

    def CFG(self, ast):
        return CFG(ast.named_production_list)
