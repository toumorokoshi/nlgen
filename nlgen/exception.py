"""
all exceptions belong here.
"""


class NLGenException(Exception):
    """ All exceptions should inherit from this exception. """
    pass


class IncongruentFeature(Exception):
    """
    raised when a feature set can be merged
    with another feature set.
    """
