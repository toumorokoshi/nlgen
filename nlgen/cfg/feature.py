from ..exception import IncongruentFeature


class FeatureSet(object):

    def __init__(self, raw_dict):
        pass


def unify_features(l, r, match_required=None, ignore=False):
    """
    generate the union of left and right feature dictionaries., and
    raise an exception if there is a conflict in values.

    left, right are assumed to be dict<str, set()> objects

    if match_required is None, all keys must match.
    if match_required is not None, all keys found in the variable
    will require matching (empty collections are valid)

    if ignore is False, no keys will be ignored.
    if ignore is True, all keys will be ignored.
    if ignore is a list, only keys within the list will be ignored.
    """
    if ignore is True:
        return {}
    l = l.copy()
    r = r.copy()
    union = {}
    for key in set(l.keys()) | set(r.keys()):
        if ignore and key in ignore:
            continue
        require_match = match_required is None or key in match_required
        union[key] = _combine_values(l.get(key), r.get(key),
                                     require_match=require_match)
    return union


def _combine_values(l_values, r_values, require_match=False):
    if l_values is None:
        return r_values
    if r_values is None:
        return l_values
    if l_values == r_values:
        return l_values
    intersection = l_values & r_values
    if require_match and len(intersection) == 0:
        raise IncongruentFeature(
            "{0} != {1}, and is a required match.".format(l_values, r_values)
        )
    return intersection
