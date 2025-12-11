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
