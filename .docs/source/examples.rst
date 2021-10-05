Examples
========

Several examples of completed schema are provided below. 
For clarity, all array-based values have been truncated up to 4 decimal places.

Water SPC Model
~~~~~~~~~~~~~~~~

.. code:: python

    {
        "schema_name": "mmschema_molecule",
        "schema_version": 1,
        "symbols": [
            "O",
            "H",
            "H"
        ],
        "name": "H2O",
        "ndim": 3,
        "atom_labels": [
            "OW",
            "HW1",
            "HW2"
        ],
        "atomic_numbers": [
            8,
            1,
            1
        ],
        "masses": [
            15.999,
            1.0079,
            1.0079
        ],
        "masses_units": "dalton",
        "molecular_charge": 0.0,
        "molecular_charge_units": "elementary_charge",
        "formal_charges_units": "elementary_charge",
        "partial_charges_units": "elementary_charge",
        "geometry": [
            2.0,
            2.09,
            0.0,
            2.82,
            2.09,
            0.58,
            1.18,
            2.09,
            0.58
        ],
        "geometry_units": "angstrom",
        "velocities_units": "angstrom / femtosecond",
        "connectivity": [
            [
                0,
                2,
                1.0
            ],
            [
                0,
                1,
                1.0
            ]
        ],
        "substructs": [
            [
                "HOH",
                0
            ],
            [
                "HOH",
                0
            ],
            [
                "HOH",
                0
            ]
        ],
        "provenance": {
            "creator": "MMElemental",
            "version": "0+untagged.586.g645c496.dirty",
            "routine": "mmelemental.models.molecule.mm_mol"
        },
        "hash": "87bdbb331a17bf9b57bc1df4ce07a38830966629"
    }
