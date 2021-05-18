"""
The json-schema for the Bonds model definition
"""
import mmelemental
import sys

__all__ = ["Bonds"]
current_module = sys.modules[__name__]


Bonds = {
    "title": "Bonds",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "name": "mmschema_bonds",
    "version": "0.dev",
    "description": "Model that describes bonded (2-body) interactions between particles.",
    "type": "object",
    "properties": {
        "schema_name": {
            "type": "string",
            "pattern": "^(mmschema_bonds)$",
        },
        "schema_version": {"type": "integer"},
        "form": {"description": "Name or form of the potential.", "type": "string"},
        "params": {
            "type": "object",
            "title": "Params",
            "description": "Specific force field parameters model.",
        },
    },
    "required": ["form", "params"],
    "additionalProperties": False,
}

for (
    name,
    obj,
) in mmelemental.models.forcefield.bonded.Bonds.supported_potentials().items():
    __all__.append(name)
    setattr(current_module, name, obj.schema())
