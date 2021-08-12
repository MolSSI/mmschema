"""
Integrates all components of the QC Schema into a single one.
"""

import copy

from . import molecule
from . import forcefield

# The base schema definition
base_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "name": "qcschema_input",
    "version": "1.dev",
    "description": "The MolSSI Quantum Chemistry Schema",
    "type": "object",
    "properties": {
        "molecule": molecule.Molecule,
        "schema_name": {"type": "string", "pattern": "^(qc_?schema)$"},
        "schema_version": {"type": "integer"},
        "driver": {
            "definition": "The type of computation requested",
            "enum": ["energy", "gradient", "hessian"],
        },
        "model": {
            "definition": "The method and basis specification requested",
            "properties": {
                "method": {"type": "string"},
                "basis": {
                    "anyOf": [
                        basis.basis,
                        {
                            "description": "Name of the basis set to apply to the whole molecule",
                            "type": "string",
                        },
                    ]
                },
            },
            "required": ["method", "basis"],
            "description": "The quantum chemistry model to be run.",
        },
        "keywords": {
            "type": "object",
            "description": "Program specific parameters to be used.",
        },
        "provenance": {
            "anyOf": [
                {"type": "object", "$ref": "#/definitions/provenance"},
                {
                    "type": "array",
                    "items": {"type": "object", "$ref": "#/definitions/provenance"},
                },
            ]
        },
    },
    "required": [
        "schema_name",
        "schema_version",
        "molecule",
        "driver",
        "keywords",
        "model",
    ],
    "definitions": definitions.definitions,
}


# Build out the molecule schema
molecule_dev_schema = copy.deepcopy(molecule.Molecule)

# Build out the forcefield schema
forcefield_dev_schema = copy.deepcopy(forcefield.ForceField)
