# MMSchema

[![GitHub Actions Build Status](https://github.com/MolSSI/mmschema/workflows/CI/badge.svg)](https://github.com/MolSSI/mmschema/actions?query=workflow%3ACI)

A specification for Molecular Mechanics. Supported schemas:

- [JSON](https://json-schema.org)
- [HDF5-JSON](https://hdf5-json.readthedocs.io)

See the [documentation](https://molssi.github.io/mmschema) for more info.

# Sample files
See the following files for CO2 molecule representation:

- [JSON-simple](mmschema/data/sample/co2-simple.json): simplest representation (with no JSON schema metadata)
- [JSON-complete](mmschema/data/sample/co2.json): more complex representation with full compliance with the JSON schema specification
- [HDF5](mmschema/data/sample/co2.hdf5): representation in a hierarchichal (filesystem-like) data format
- [HDF5-JSON](mmschema/data/sample/co2-h5.json): representation in an HDF5-equivalent JSON file based on the HDF5-JSON specification
