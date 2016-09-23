=============================
Featured Context-Free Grammar
=============================

An FCFG is a extension of a `context-free grammar <https://en.wikipedia.org/wiki/Context-free_grammar>_`, that also
agreement of features (string-string pairs) on terminal values to be considered valid by the grammar.

For example, consider a grammar that contains two conjugations of the verb "has":

.. code-block:: text

    PRONOUN = "I" {"person": 1} |
              "YOU"
