# Change log

## Release 0.1.0 (2023-12-05)

First release

## Release 0.2.0 (2024-03-12)

Added the openMINDS instance library (predefined metadata instances)
as class attributes. For example:
```python
In [1]: from openminds.latest.controlled_terms import AgeCategory

In [2]: AgeCategory.adult
Out[2]: <openminds.latest.controlled_terms.age_category.AgeCategory at 0x104eb3970>

In [3]: AgeCategory.adult.id
Out[3]: 'https://openminds.ebrains.eu/instances/ageCategory/adult'

In [4]: AgeCategory.adult.definition
Out[4]: "'Adult' categorizes the life cycle stage of an animal or human that reached sexual maturity."
```

In some cases it is more convenient to retrieve instances by name or synonym, e.g.:
```
In [1]: from openminds.latest.controlled_terms import MolecularEntity

In [2]: MolecularEntity.by_name("HEPES") == MolecularEntity.by_name("4-(2-hydroxyethyl)-1-piperazine ethanesulfonic acid")
Out[2]: True
```

For more detail see #29.

## Release 0.2.1 (2024-03-29)

- Improved property descriptions, for example the `identifier` property of the `ProductSource` class now has the description "Term or code used to identify the product source" whereas previously it was the generic "Term or code used to identify something or someone".
- Non-HTTP IRIs are now allowed.

## Release 0.2.2 (2024-03-29)

- Bug fixes:
    - instance properties that should be IRI objects were just plain strings
    - passing an integer to a property of type "number" produced a validation error
    - when validating collections the "ignore" argument wasn't being passed down
    - type hints were producing an error with Python 3.8

## Release 0.2.3 (2024-06-21)

- Update to latest openMINDS schemas and instances
- Internal import statements are now sorted alphabetically

## Release 0.3.0 (2025-04-09)

- Added release candidate for openMINDS v4
- Nodes in a collection are now sorted by ID.

## Release 0.3.1 (2025-09-09)

- includes fixes and additions to instance library, including:
    - replacement of MRAcquisitionType by MRSpatialEncoding
    - the addition of a Marmoset brain atlas, and some other new instances
    - improved consistency of @id paths, spelling corrections, improved term definitions
- more reliable export as JSON-LD: specifically when a property which expects a single value
  has a list/tuple as a value, this would break JSON-LD export.
  Now, although it is marked as a validation failure, this does not prevent export.
- addition of a `Link` class, to allow making reference to remote graph nodes defined by their `@id`
  that are not present locally.
- improved CI testing: we now test v3 and v4, as well as "latest".

## Release 0.4.0 (2025-11-18)

- drop support for Python 3.8, add support for Python 3.14.
- more forgiving import of JSON-LD:
  - an option to allow additional (non-openMINDS) keys in a JSON-LD document [#63](https://github.com/openMetadataInitiative/openMINDS_Python/pull/63)
  - support fully-expanded IRIs as keys in JSON-LD documents [#64](https://github.com/openMetadataInitiative/openMINDS_Python/pull/64)
  - accept `datetime` strings for properties with type `date` [#65](https://github.com/openMetadataInitiative/openMINDS_Python/pull/65)
  - accept `"@type": [<IRI>]` as well as `"@type": <IRI>` [#66](https://github.com/openMetadataInitiative/openMINDS_Python/pull/66)
- make the class registry reusable by other packages [#70](https://github.com/openMetadataInitiative/openMINDS_Python/pull/70)
- bug fix: prevent infinite recursion in `validate()` where there are loops in the graph [#76](https://github.com/openMetadataInitiative/openMINDS_Python/pull/76)
- allow the user to specify which openMINDS version should be used by `Collection.load()` [#77](https://github.com/openMetadataInitiative/openMINDS_Python/pull/77)
- add the option to group files into subdirectories by schema when saving [#80](https://github.com/openMetadataInitiative/openMINDS_Python/pull/80)
- improvements to the `by_name()` method [#81](https://github.com/openMetadataInitiative/openMINDS_Python/pull/81)

## Release 0.4.1 (2026-02-16)

- fixed a TypeError in `by_name()` when a name was not found [#83](https://github.com/openMetadataInitiative/openMINDS_Python/pull/83)
- fixed a bug where properties whose value evaluated to False (e.g., zero) were not serialized if using `include_empty_properties=False` [#84](https://github.com/openMetadataInitiative/openMINDS_Python/pull/84)
- updates to the "latest" module


## Release 0.5.0 (2026-03-23)

- Added openMINDS v5 schemas. For full details of the changes, see the [Release Notes](https://github.com/openMetadataInitiative/openMINDS/blob/main/schemas/v5.0/release_notes_v5.0.txt).


## Release 0.5.1 (2026-04-02)

- Changed `embed_linked_nodes` from boolean to LinkedNodeEmbedding enum [#92](https://github.com/openMetadataInitiative/openMINDS_Python/pull/92). This adds an option "if necessary", which embeds linked nodes inline when they lack an @id, and otherwise uses a reference — useful for mixed scenarios where some nodes don't yet have identifiers. This is backwards compatible: True is accepted in place of "always" and False in place of "never.


## Release 0.6.0 (2026-08-20)

Note that this release contains two changes in behaviour which, although they are bug fixes, may require changes in downstream code. See "Changes in behaviour" below.

- New options for the `by_name()` method [#100](https://github.com/openMetadataInitiative/openMINDS_Python/pull/100), [#103](https://github.com/openMetadataInitiative/openMINDS_Python/pull/103):
    - `case_sensitive` (default `True`); set it to `False` to ignore case when matching.
    - a third `match` mode, `"within"`, which finds instances whose name-like property is contained in the string you provide (the mirror image of `"contains"`).
    - `ignore_accents` (default `False`); set it to `True` to ignore accents and other diacritical marks when matching, and to treat special letters such as ß, æ, ø and ł as their closest plain-letter equivalents. For example, `SovereignState.by_name("Republique francaise", ignore_accents=True)` finds "France". Combine it with `case_sensitive=False` to ignore differences in case as well.
- Bug fixes in `by_name()` [#100](https://github.com/openMetadataInitiative/openMINDS_Python/pull/100):
    - a crash when an instance did not have one of the name-like properties set.
    - `by_name(..., all=True)` could return the same instance more than once, where it matched through several keys (e.g. a name that is also listed as one of its own synonyms).

### Changes in behaviour

- Cross-references between instance library instances are now resolved to typed openMINDS objects instead of being left as raw dicts [#95](https://github.com/openMetadataInitiative/openMINDS_Python/pull/95), fixing [#94](https://github.com/openMetadataInitiative/openMINDS_Python/issues/94). For example, `Accessibility.direct_virtual_open_access.payment_models[0]` is now a `PaymentModelType` object, where previously it was a dict. Code that treated such values as dicts will need updating. As part of this fix, `Node._resolve_links()` now keeps an unresolvable `Link` in a list-valued property rather than raising `KeyError`.
- IRI validation has moved from the `IRI` constructor to the `validate()` method [#101](https://github.com/openMetadataInitiative/openMINDS_Python/pull/101), fixing [#93](https://github.com/openMetadataInitiative/openMINDS_Python/issues/93). Creating an `IRI` with an invalid value no longer raises `ValueError`; the problem is instead reported as a validation failure, with a specific hint to replace spaces with "%20" where that would make the IRI valid.
