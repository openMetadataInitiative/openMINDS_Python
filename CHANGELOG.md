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
