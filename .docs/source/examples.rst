Examples
========

Several examples of completed schema. As the input is duplicated in the output
the corresponding input of these schema are the input fields alone.
Effectively, this is all keys above the "provenance" field. For clarity, all
array-based values have been truncated to four decimal places.

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
            15.9994,
            1.0079,
            1.0079
        ],
        "masses_units": "dalton",
        "molecular_charge": 0.0,
        "molecular_charge_units": "e",
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
        }
    }
