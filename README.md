# MMSchema

[![GitHub Actions Build Status](https://github.com/MolSSI/mmschema/workflows/CI/badge.svg)](https://github.com/MolSSI/mmschema/actions?query=workflow%3ACI)

A vocabulary specification for Molecular Mechanics. Supported schemas:

- [JSON](https://json-schema.org)
- [HDF5](https://support.hdfgroup.org/HDF5/doc1.6/UG/03_Model.html)

Supported formats:

- [JSON](https://www.json.org)
- [YAML](https://yaml.org)
- [HDF5](https://www.hdfgroup.org/solutions/hdf5)

See the [documentation](https://molssi.github.io/mmschema) for more info.

# Sample files
See the following files for CO2 molecule representation:

- [JSON](mmschema/data/sample/co2.json): representation in JavaScript Object Notation format
- [YAML](mmschema/data/sample/co2.yaml): representation in YAML Ain't Markup Language format
- [HDF5](mmschema/data/sample/co2.hdf5): representation in a hierarchichal (filesystem-like) data format
- [HDF5-JSON](mmschema/data/sample/co2-h5.json): representation in an HDF5-equivalent JSON file based on the HDF5-JSON specification
