import json
from pathlib import Path


_data_path = Path(__file__).parent.resolve() / "data"
_supported_versions = [
    1,
]

_aliases = {
    "molecule": "Molecule",
    "trajectory": "Trajectory",
    "forcefield": "ForceField",
    "ensemble": "Ensemble",
    "provenance": "Provenance",
}

_versions_list = {
    "molecule": _supported_versions,
    "trajectory": _supported_versions,
    "forcefield": _supported_versions,
    "ensemble": _supported_versions,
    "provenance": _supported_versions,
}


def list_versions(schema_type):
    """
    Lists all current JSON schema versions.
    """
    return [1, "dev"]


def get_schema(schema_type, version="dev"):
    """
    Returns the requested schema (input or output) for a given version number.
    """
    # temporary
    if version not in _supported_versions:
        raise ValueError(
            f"Unsupported version ({version}). Supported versions are : {_versions_list}."
        )
    if schema_type not in _aliases.keys():
        raise KeyError(
            "Schema type should be among {} (+aliases), not '{}'.".format(
                list(_aliases.keys()), schema_type
            )
        )

    fpath = _data_path / ("v" + str(version)) / (schema_type + ".schema")
    ret = json.loads(fpath.read_text())

    return ret
