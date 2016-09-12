from collections import defaultdict
from .production import (
    ProductionBase,
    Production,
    ProductionUnion,
    Terminal
)


class CFG(object):
    """
    a context-free-grammar representation.  this cfg honors
    productions with features, as well.
    """
    def __init__(self, productions):
        self._compiled = defaultdict(list)
        for p in productions:
            self.add(*p)

    def permutations(self, reference):
        production = self._resolve_production(reference)
        return production.permutations(self)

    def permutation_values(self, reference):
        """
        returns just a list of the valid value, instead of
        result objects
        """
        for result in self.permutations(reference):
            yield result.value

    def _resolve_production(self, reference):
        if not isinstance(reference, ProductionBase):
            if reference not in self._compiled:
                raise IndexError("no production {0} found.".format(reference))
            return ProductionUnion(self._compiled[reference])
        return reference

    def add(self, name, production):
        """ add a production to the compiled context """
        self._compiled[name].append(production)
