"""
The json-schema for the Molecule definition
"""
Molecule = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "name": "mmschema_molecule",
    "version": "0.dev",
    "description": "The MolSSI Molecular Mechanics Molecule Schema",
    "type": "object",
    "properties": {
        "schema_name": {
            "guidance": "required properties schema_name within molecule block (instead of 'qcschema_[in|out]put' from one level higher) starts with schema_name=qcschema_molecule and schema_version=2",
            "type": "string",
            "pattern": "^(mmschema_molecule)$",
        },
        "schema_version": {"type": "integer"},
        "symbols": {
            "description": "(natom, ) atom symbols.",
            "type": "array",
            "items": {"type": "string"},
        },
        "ndim": {
            "description": "Number of spatial dimensions of the molecule geometry.",
            "type": "number",
            "multipleOf": 1.0,
        },
        "geometry": {
            "description": "(ndim * natom, ) vector of [X,Y,Z] coordinates of the particles.",
            "type": "array",
            "items": {"type": "number"},
        },
        "geometry_units": {
            "description": "Geometry units. Any spatial unit available in pint is supported.",
            "type": "string",
        },
        "velocities": {
            "description": "(ndim * natom, ) vector of [X,Y,Z] velocities of the particles.",
            "type": "array",
            "items": {"type": "number"},
        },
        "velocities_units": {
            "description": "Velocities units. Any speed unit available in pint is supported.",
            "type": "string",
        },
        "masses": {
            "description": "(natom, ) atom masses; if not given, canonical weights are assumed for atomic particles.",
            "type": "array",
            "items": {"type": "number"},
        },
        "masses_units": {
            "description": "Masses units. Any mass unit available in pint is supported.",
            "type": "string",
        },
        "atomic_numbers": {
            "description": "(natom, ) atomic numbers, nuclear charge for atoms.",
            "type": "array",
            "items": {"type": "number", "multipleOf": 1.0},
        },
        "mass_numbers": {
            "description": "(natom, ) mass numbers for atoms, if known isotope, else -1.",
            "type": "array",
            "items": {"type": "number", "multipleOf": 1.0},
        },
        "atom_labels": {
            "description": "(natom, ) atom labels with any user tagging information.",
            "type": "array",
            "items": {"type": "string"},
        },
        "name": {"description": "The name of the molecule.", "type": "string"},
        "comment": {
            "description": "Any additional comment one would attach to the molecule.",
            "type": "string",
        },
        "molecular_charge": {
            "description": "The overall charge of the molecule.",
            "type": "number",
            "default": 0.0,
        },
        "molecular_charge_units": {
            "description": "Molecular charge units. Any charge unit available in pint is supported.",
            "type": "string",
        },
        "connectivity": {
            "description": "A list describing bonds within a molecule. Each element is a (atom1, atom2, order) tuple.",
            "guidance": "Bonds may be freely reordered and inverted.",
            "type": "array",
            "items": {
                "type": "array",
                "minItems": 3,
                "maxItems": 3,
                "items": [
                    {
                        "description": "Atom number (0-indexed) at one end of bond.",
                        "type": "number",
                        "multipleOf": 1.0,
                    },
                    {
                        "description": "Atom number (0-indexed) at other end of bond.",
                        "type": "number",
                        "multipleOf": 1.0,
                    },
                    {
                        "description": "Bond order.",
                        "type": "number",
                    },
                ],
            },
        },
        "substructs": {
            "description": "(name, index) list of connected atoms constituting a portion of the structure.",
            "guidance": "Order follows atomic indices from 0 till natom-1.  E.g. [('ALA', 4), ...] means atom1 belongs to aminoacid alanine with residue number 4.",
            "type": "array",
            "items": {
                "type": "array",
                "minItems": 2,
                "maxItems": 2,
                "items": [
                    {
                        "description": "Substructure name this atom belongs to.",
                        "type": "string",
                    },
                    {
                        "description": "Substructure index this atom belongs to.",
                        "type": "number",
                        "multipleOf": 1.0,
                    },
                ],
            },
        },
        "provenance": {"type": "object", "$ref": "#/definitions/provenance"},
    },
    "required": ["schema_name", "schema_version"],
    "description": "Representation of an all-atom or coarse-grained molecule",
}
