.. _index_data_contracts:

Data Contracts Index
====================

Data contract documents define the field-level details for each
major data structure in LatticeLang. They are the authoritative
source for serialization formats, validation rules, and data
schema.

.. note::
   This separation follows Cockburn's guidance in *Writing
   Effective Use Cases* and Constantine & Lockwood's *Software
   for Use*. See :ref:`decisions` for the full decision
   record.

Use cases reference data contracts by information nickname rather
than duplicating field definitions. See :ref:`adr-026`.

.. toctree::
   :maxdepth: 1

   dc_constraints
   dc_inventory
   dc_ipa_reference
   dc_language_definition
   dc_orthography_rules
   dc_phoneme
   dc_syllable_template