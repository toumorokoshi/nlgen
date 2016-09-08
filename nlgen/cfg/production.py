class ProductionBase(object):
    pass


class ProductionUnion(ProductionBase):
    """
    the union of several productions. It will
    iterate through all matches through all production lists.
    """

    def __init__(self, individual_production_list):
        self._individual_production_list = individual_production_list

    def productions(self, cfg):
        for production in self._individual_production_list:
            yield production.productions(cfg)


class Production(ProductionBase):
    """
    a list of productions, such as
    PRONOUN " " VERB " " NOUN
    """

    def __init__(self, production_list):
        self._production_list = production_list

    def productions(self, cfg):
        return self._productions_from_list(
            self._production_list, cfg
        )

    def _productions_from_list(self, production_list, cfg):
        if len(production_list) == 0:
            yield []
        else:
            lhs = production_list[0]
            rhs = production_list[1:]
            for lhs_value in lhs.productions(cfg):
                for rhs_value in self._productions_from_list(rhs):
                    yield lhs_value + rhs_value


class PRef(ProductionBase):

    def __init__(self, key):
        self._key = key

    def productions(self, cfg):
        return cfg.permutations(self._key)


class Terminal(ProductionBase):

    def __init__(self, value):
        return self._value

    def productions(self, cfg):
        yield [self]
