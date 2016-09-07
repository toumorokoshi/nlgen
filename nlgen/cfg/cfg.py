from collections import defaultdict
from .production import Production


class CFG(object):
    """
    a context-free-grammar representation.  this cfg honors
    productions with features, as well.
    """
    def __init__(self, productions):
        self._compiled = defaultdict(list)
        for p in productions:
            self.add(p)

    def permutations(self, reference, required_terminals=None):
        required_terminals = required_terminals or []
        if not isinstance(reference, Production):
            if reference not in self._compiled:
                raise IndexError("no production {0} found.".format(reference))
            reference = self._compiled[reference]

    def _permutations(self, production):
        for s in production.symbols:
            self._permutations(s)
        pass

    def _permutation_from_list(self, production_list):
        for lhs in production_list[0].productions:
            for rhs in self._permutations_from_list(production_list[1:]):
                yield lhs + rhs
                pass

    def add(self, name, production):
        """ add a production to the compiled context """
        self._compiled[name].append(production)
