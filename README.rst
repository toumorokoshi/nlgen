=====
nlgen
=====

Natural Language Generator for Python

-------
Summary
-------

The goal of nlgen is to allow for generation of a natural sentence
with a specific meaning. For example, translating "I like candy" to
"Mi gustan los dulces".

----
How?
----

Ensuring that a sentence is grammatically correct is difficult.
For now, nlgen will focus on generation using featured context-free-grammars.

---
API
---

.. code-block:: python

    from nlgen.fcfg import FCFG, FProduction

    FCFG.add_production(FRule("VI", "
