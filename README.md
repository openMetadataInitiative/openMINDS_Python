# openMINDS Python library

openMINDS Python is a small library to support the creation and use of openMINDS metadata models and schemas in your Python application, with import and export in JSON-LD format.

## Installation

```
pip install openMINDS
```

## Usage

``` python
from datetime import date
from openminds import Collection, IRI
import openminds.latest.core as omcore

# Create an empty metadata collection

collection = Collection()

# Create some metadata

mgm = omcore.Organization(
    full_name="Metro-Goldwyn-Mayer Studios, Inc.",
    short_name="MGM",
    homepage=IRI("https://www.mgm.com")
)

stan = omcore.Person(
    given_name="Stan",
    family_name="Laurel",
    affiliations=omcore.Affiliation(member_of=mgm, start_date=date(1942, 1, 1))
)

ollie = omcore.Person(
    given_name="Oliver",
    family_name="Hardy",
    affiliations=omcore.Affiliation(member_of=mgm, start_date=date(1942, 1, 1))
)

# Add the metadata to the collection

collection.add(stan, ollie, mgm)

# Check the metadata are valid

failures = collection.validate()

# Save the collection in a single JSON-LD file

collection.save("my_collection.jsonld")

# Save each node in the collection to a separate file

collection.save("my_collection", individual_files=True)  # creates files within the 'my_collection' directory

# Load a collection from file
new_collection = Collection()
new_collection.load("my_collection.jsonld")
```

## License

This work is licensed under the MIT License.

## Getting help

In case of questions about **openMINDS**, please contact us at support@openmetadatainitiative.org.
If you find a bug in the Python library or would like to suggest an enhancement or new feature,
please open a ticket in the [openMINDS Python library issue tracker](https://github.com/openMetadataInitiative/openMINDS_Python/issues).

If you identify a problem or would like to suggest changes to the openMINDS specification itself,
please open a ticket in the [openMINDS issue tracker](https://github.com/openMetadataInitiative/openMINDS/issues).

## Development

Contributions are welcome, please see our [contribution guidelines](https://openminds-documentation.readthedocs.io/en/latest/shared/contribution_guidelines.html).

This repository has two main branches: `pipeline` and `main`.
The `pipeline` contains the code for building the Python package from the openMINDS schemas.
The build process is triggered by changes to the schemas, and runs as a GitHub action.
The resultant package is copied to the `main` branch, and at intervals is published on PyPI.

## Acknowledgements

<div><img src="https://www.braincouncil.eu/wp-content/uploads/2018/11/wsi-imageoptim-EU-Logo.jpg" alt="EU Logo" height="23%" width="15%" align="right" style="margin-left: 10px"></div>

This open source software code was developed in part or in whole in the Human Brain Project, funded from the European Union's Horizon 2020 Framework Programme for Research and Innovation under Specific Grant Agreements No. 720270, No. 785907 and No. 945539 (Human Brain Project SGA1, SGA2 and SGA3).
