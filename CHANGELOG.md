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