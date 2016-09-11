from ..exception import IncongruentFeature


class FeatureSet(object):

    def __init__(self, raw_dict):
        pass


def unify_features(l, r, match_required=None):
    """
    generate the union of left and right feature dictionaries., and
    raise an exception if there is a conflict in values.

    left, right are assumed to be dict<str, set()> objects

    if match_required is None, all keys must match.
    if match_required is not None, all keys found in the variable
    will require matching (empty collections are valid)
    """
    l = l.copy()
    r = r.copy()
    union = {}
    for key in set(l.keys()) | set(r.keys()):
        require_match = match_required is None or key in match_required
        union[key] = _combine_values(l.get(key), r.get(key),
                                     require_match=require_match)
    return union


def _combine_values(l_values, r_values, require_match=False):
    if require_match and l_values != r_values:
        raise IncongruentFeature(
            "{0} != {1}, and is a required match.".format(l_values, r_values)
        )
    return l_values | r_values
