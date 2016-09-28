from collections import defaultdict
from .production import (
    Production,
    PUnion,
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
        if not isinstance(reference, Production):
            if reference not in self._compiled:
                raise IndexError("no production {0} found.".format(reference))
            return PUnion(self._compiled[reference])
        return reference

    def add(self, name, production):
        """ add a production to the compiled context """
        self._compiled[name].append(production)

    def __eq__(self, other):
        if not isinstance(other, CFG):
            return False
        return self._compiled == other._compiled

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "<CFG: {0}>".format(self._compiled)
