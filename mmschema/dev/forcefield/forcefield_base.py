"""
The base file for FF MMSchema.
"""

__all__ = ["ForceField"]

ForceField = {
    "type": "object",
    "description": "Wavefunction properties resulting from a computation."
    "Matrix quantities are stored in column-major order.",
    "additionalProperties": False,
    "properties": {
        "schema_name": {
            "title": "Schema Name",
            "description": "The MMSchema specification to which this model conforms. Explicitly fixed as mmschema_forcefield.",
            "default": "mmschema_forcefield",
            "pattern": "^(mmschema_forcefield)$",
            "type": "string"
        },
        "schema_version": {
            "title": "Schema Version",
            "description": "The version number of ``schema_name`` to which this model conforms.",
            "default": 0,
            "type": "integer"
        },
        "name": {
            "title": "Name",
            "description": "Common or human-readable name to assign to this model. This field can be arbitrary.",
            "type": "string"
        },
        "comment": {
            "title": "Comment",
            "description": "Additional comments for this model. Intended for pure human/user consumption and clarity.",
            "type": "string"
        },
        "symbols": {
            "title": "Symbols",
            "description": "An ordered (natom,) list of particle (e.g. atomic) elemental symbols.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "nonbonded": {
            "title": "Nonbonded",
            "description": "Nonbonded parameters model.",
            "anyOf": [
                {
                    "type": "object",
                    "$ref": "#/definitions/NonBonded"
                },
                {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/NonBonded"
                    }
                }
            ]
        },
        "bonds": {
            "title": "Bonds",
            "description": "2-body covalent bond model.",
            "anyOf": [
                {
                    "type": "object",
                    "$ref": "#/definitions/Bonds"
                },
                {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Bonds"
                    }
                }
            ]
        },
        "angles": {
            "title": "Angles",
            "description": "3-body angular bond model.",
            "anyOf": [
                {
                    "$ref": "#/definitions/Angles"
                },
                {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Angles"
                    }
                }
            ]
        },
        "dihedrals": {
            "title": "Dihedrals",
            "description": "4-body torsional bond model.",
            "anyOf": [
                {
                    "$ref": "#/definitions/Dihedrals"
                },
                {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Dihedrals"
                    }
                }
            ]
        },
        "charges": {
            "title": "Charges",
            "description": "Atomic charges. Default unit is in elementary charge units.",
            "type": "array",
            "items": {
                "type": "number"
            }
        },
        "charges_units": {
            "title": "Charges Units",
            "description": "Atomic charge unit.",
            "default": "e",
            "type": "string"
        },
        "masses": {
            "title": "Masses",
            "description": "List of atomic masses. If not provided, the mass of each atom is inferred from its most common isotope. If this is provided, it must be the same length as ``symbols``.",
            "type": "array",
            "items": {
                "type": "number"
            }
        },
        "masses_units": {
            "title": "Masses Units",
            "description": "Units for atomic masses. Defaults to unified atomic mass unit.",
            "default": "amu",
            "type": "string"
        },
        "charge_groups": {
            "title": "Charge Groups",
            "description": "Charge groups per atom. Length of the array must be natoms.",
            "type": "array",
            "items": {
                "type": "number",
                "multipleOf": 1.0
            }
        },
        "exclusions": {
            "title": "Exclusions",
            "description": "Which pairs of bonded atoms to exclude from non-bonded calculations.     \tThe rules to apply in choosing bonded exclusions are specifed in the configuration file using the exclude parameter. The     \tchoices for exclusions are None, 1-2, 1-3, 1-4, etc. With None, no atom pairs are excluded. With 1-2, only atoms that are connected     \tvia a linear bond are excluded. With 1-3, any pair of atoms connected via a bond or bonded to a common third atom are excluded.     \tWith 1-4, any atoms that are connected by a linear bond, or a sequence of two bonds, or a sequence of three bonds, are excluded.     \tWith scaled1-4, exclusions are applied in the same manner as the 1-3 setting, but those pairs that are connected by a sequence of     \t3 bonds are calculated using the modified 1-4 methods described rather than the standard force calculations.",
            "type": "string"
        },
        "inclusions": {
            "title": "Inclusions",
            "description": "Which pairs of 1-4 excluded bonded atoms to include in non-bonded calculations.",
            "type": "string"
        },
        "identifier": {
            "title": "Identifier",
            "description": "Forcefield unique identifier e.g. charmm27, amber99, etc.",
            "type": "string"
        },
        "defs": {
            "title": "Defs",
            "description": "Particle definition. For atomic forcefields, this could be the atom type (e.g. HH31) or SMIRKS (OFF) representation. The type names are associated with the atomic elements defined in other objects e.g. see the :class:``Molecule`` model.",
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "substructs": {
            "title": "Substructs",
            "description": "A list of substructure names the particles belong to. E.g. [('ALA', 4), ('ACE', 0)] means atom1 belong to residue ALA (alanine) with residue number 4, while atom2 belongs to residue ACE (acetyl) with residue number 0.",
            "type": "array",
            "items": {
                "type": "array",
                "items": [
                    {
                        "type": "string"
                    },
                    {
                        "type": "integer"
                    }
                ]
            }
        },
        "combination_rule": {
            "title": "Combination Rule",
            "description": "Combination rule for the force field.",
            "default": "Lorentz-Berthelot",
            "type": "string"
        },
        "atomic_numbers": {
            "title": "Atomic Numbers",
            "description": "An optional ordered 1-D array-like object of atomic numbers of shape (nat,). Index matches the 0-indexed indices of all other per-atom settings like ``symbols``. Values are inferred from the ``symbols`` list if not explicitly set. ",
            "type": "array",
            "items": {
                "type": "number",
                "multipleOf": 1.0
            }
        },
        "provenance": {
            "title": "Provenance",
            "type": "object", 
            "$ref": "#/definitions/provenance",
            "description": "The provenance information about how this object (and its attributes) were generated, provided, and manipulated.",
            "default": {
                "creator": "MMElemental",
                "version": "0+untagged.611.gebcba65.dirty",
                "routine": "mmelemental.models.forcefield.mm_ff"
            },
        },
        "extras": {
            "title": "Extras",
            "description": "Additional information to bundle with the object. Use for schema development and scratch space.",
            "type": "object"
        }
    },
    "required": [
        "symbols"
    ],
    "additionalProperties": False,
    "$schema": "http://json-schema.org/draft-04/schema#",
    "definitions": {
        "NonBonded": {
            "title": "NonBonded",
            "description": "Model that describes non-bonded interactions between particles",
            "type": "object",
            "properties": {
                "form": {
                    "title": "Form",
                    "description": "Name or form of the potential. See cls.supported_potentials() for available potentials.",
                    "type": "string"
                },
                "params": {
                    "title": "Params",
                    "description": "Specific force field parameters model."
                }
            },
            "required": [
                "form",
                "params"
            ],
            "additionalProperties": False
        },
        "Bonds": {
            "title": "Bonds",
            "type": "object",
            "properties": {
                "form": {
                    "title": "Form",
                    "description": "Name or form of the potential.",
                    "type": "string"
                },
                "params": {
                    "title": "Params",
                    "description": "Specific force field parameters model."
                },
                "lengths": {
                    "title": "Lengths",
                    "description": "Equilibrium bond lengths. Default unit is Angstroms.",
                    "type": "array",
                    "items": {
                        "type": "number"
                    }
                },
                "lengths_units": {
                    "title": "Lengths Units",
                    "description": "Equilibrium bond lengths unit.",
                    "default": "angstroms",
                    "type": "string"
                },
                "indices": {
                    "title": "Indices",
                    "description": "Particle indices for each bond and the bond order: (index1, index2, order).",
                    "minItems": 1,
                    "type": "array",
                    "items": {
                        "type": "array",
                        "items": [
                            {
                                "type": "integer"
                            },
                            {
                                "type": "integer"
                            },
                            {
                                "type": "number"
                            }
                        ]
                    }
                }
            },
            "required": [
                "form",
                "params",
                "lengths",
                "indices"
            ],
            "additionalProperties": False
        },
        "Angles": {
            "title": "Angles",
            "type": "object",
            "properties": {
                "form": {
                    "title": "Form",
                    "description": "Name or form of the potential.",
                    "type": "string"
                },
                "params": {
                    "title": "Params",
                    "description": "Specific force field parameters model."
                },
                "angles": {
                    "title": "Angles",
                    "description": "Equilibrium angles. Default unit is degrees.",
                    "type": "array",
                    "items": {
                        "type": "number"
                    }
                },
                "angles_units": {
                    "title": "Angles Units",
                    "description": "Equilibrium angle units.",
                    "default": "degrees",
                    "type": "string"
                },
                "indices": {
                    "title": "Indices",
                    "description": "Particle indices for each angle.",
                    "minItems": 1,
                    "type": "array",
                    "items": {
                        "type": "array",
                        "items": [
                            {
                                "type": "integer"
                            },
                            {
                                "type": "integer"
                            },
                            {
                                "type": "integer"
                            }
                        ]
                    }
                }
            },
            "required": [
                "form",
                "params",
                "angles",
                "indices"
            ],
            "additionalProperties": False
        },
        "Dihedrals": {
            "title": "Dihedrals",
            "type": "object",
            "properties": {
                "form": {
                    "title": "Form",
                    "description": "Name or form of the potential.",
                    "type": "string"
                },
                "params": {
                    "title": "Params",
                    "description": "Specific force field parameters model."
                },
                "indices": {
                    "title": "Indices",
                    "description": "Particle indices for each dihedral angle.",
                    "minItems": 1,
                    "type": "array",
                    "items": {
                        "type": "array",
                        "items": [
                            {
                                "type": "integer"
                            },
                            {
                                "type": "integer"
                            },
                            {
                                "type": "integer"
                            },
                            {
                                "type": "integer"
                            }
                        ]
                    }
                },
                "weights": {
                    "title": "Weights",
                    "description": "Something to consider later on? Ses CHARMM dihedral_style for LAMMPS.",
                    "type": "array",
                    "items": {
                        "type": "number"
                    }
                }
            },
            "required": [
                "form",
                "params",
                "indices"
            ],
            "additionalProperties": False
        },
        "Provenance": {
            "title": "Provenance",
            "description": "Provenance information.",
            "type": "object",
            "properties": {
                "creator": {
                    "title": "Creator",
                    "description": "The creator of the object.",
                    "type": "string"
                },
                "version": {
                    "title": "Version",
                    "description": "The version of the creator.",
                    "type": "string"
                },
                "routine": {
                    "title": "Routine",
                    "description": "The routine of the creator.",
                    "type": "string"
                }
            },
            "required": [
                "creator"
            ]
        }
    }
}
