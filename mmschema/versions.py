import json
from pathlib import Path


_data_path = Path(__file__).parent.resolve() / "data"

_aliases = {
    "molecule": "Molecule",
    "trajectory": "Trajectory",
    "forcefield": "ForceField",
    "ensemble": "Ensemble",
    "provenance": "Provenance",
}

_versions_list = {
    "molecule": [1, "dev"],
    "trajectory": [1, "dev"],
    "forcefield": [1, "dev"],
    "ensemble": [1, "dev"],
    "provenance": [1, "dev"],
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
    if version == "dev":
        version = 2
    else:
        raise KeyError(
            "Schema type should be among {} (+aliases), not '{}'.".format(
                list(_aliases.keys()), schema_type
            )
        )

    fpath = _data_path / ("v" + str(version)) / (fname + ".schema")
    ret = json.loads(fpath.read_text())

    return ret
