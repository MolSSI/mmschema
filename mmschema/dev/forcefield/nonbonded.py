"""
The json-schema for the NonBonded model definition
"""
import mmelemental
import sys

__all__ = ["NonBonded"]
current_module = sys.modules[__name__]


NonBonded = {
    "title": "NonBonded",
    "$schema": "http://json-schema.org/draft-04/schema#",
    "name": "mmschema_nonbonded",
    "version": "0.dev",
    "description": "Model that describes non-bonded interactions between particles.",
    "type": "object",
    "properties": {
        "schema_name": {
            "type": "string",
            "pattern": "^(mmschema_nonbonded)$",
        },
        "schema_version": {"type": "integer"},
        "form": {"description": "Name or form of the potential.", "type": "string"},
        "params": {
            "title": "Params",
            "type": "object",
            "description": "Specific force field parameters model.",
        },
    },
    "required": ["form", "params"],
    "additionalProperties": False,
}

for (
    name,
    obj,
) in mmelemental.models.forcefield.nonbonded.NonBonded.supported_potentials().items():
    __all__.append(name)
    setattr(current_module, name, obj.schema())
