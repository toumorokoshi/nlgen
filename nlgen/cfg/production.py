class ProductionBase(object):
    pass


class ProductionUnion(ProductionBase):
    """
    the union of several productions. It will
    iterate through all matches through all production lists.
    """

    def __init__(self, individual_production_list):
        self._individual_production_list = individual_production_list

    def permutations(self, cfg):
        for production in self._individual_production_list:
            for permutation in production.permutations(cfg):
                yield permutation


class Production(ProductionBase):
    """
    a list of productions, such as
    PRONOUN " " VERB " " NOUN
    """

    def __init__(self, production_list):
        self._production_list = production_list

    def permutations(self, cfg):
        return self._permutations_from_list(
            self._production_list, cfg
        )

    def _permutations_from_list(self, production_list, cfg):
        if len(production_list) == 0:
            yield ()
        else:
            lhs = production_list[0]
            rhs = production_list[1:]
            for lhs_value in lhs.permutations(cfg):
                for rhs_value in self._permutations_from_list(rhs, cfg):
                    yield lhs_value + rhs_value


class ProductionRef(ProductionBase):

    def __init__(self, key):
        self._key = key

    def permutations(self, cfg):
        return cfg.permutations(self._key)


class Terminal(ProductionBase):

    def __init__(self, value):
        self._value = value

    def permutations(self, cfg):
        yield (self._value,)

    def __eq__(self, other):
        return (
            isinstance(other, Terminal) and
            self._value == other._value
        )

    def __repr__(self):
        return "<Terminal: {0}>".format(self._value)

    def __hash__(self):
        return hash(self._value)
