import json
from pathlib import Path


_data_path = Path(__file__).parent.resolve() / "data"
_supported_versions = [
    1,
]

_aliases = {
    "molecule": "molecule.schema",
    "trajectory": "trajectory.schema",
    "forcefield": "forcefield.schema",
    "nonbonded": "nonbonded.schema",
    "nonbonded_eam": Path("nonbonded_types") / "eam.schema",
    "nonbonded_lj": Path("nonbonded_types") / "lj.schema",
    "bonds": "bonds.schema",
    "angles": "angles.schema",
    "dihedrals": "dihedrals.schema",
    "ensemble": "ensemble.schema",
    "provenance": "provenance.schema",
}


def get_versions(schema_type):
    """
    Lists all currently available schema versions.
    """
    return _supported_versions


def get_schema(schema_type, version="dev"):
    """
    Returns the requested schema (input or output) for a given version number.
    """
    # temporary
    if version not in _supported_versions:
        raise ValueError(
            f"Unsupported version ({version}). Supported versions are : {_supported_versions}."
        )
    if schema_type not in _aliases.keys():
        raise KeyError(
            "Schema type should be among {} (+aliases), not '{}'.".format(
                list(_aliases.keys()), schema_type
            )
        )

    fpath = _data_path / ("v" + str(version)) / _aliases[schema_type]
    ret = json.loads(fpath.read_text())

    return ret
