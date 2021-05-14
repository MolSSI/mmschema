"""
The json-schema for the NonBonded model definition
"""
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
            "description": "Specific force field parameters model.",
        },
    },
    "required": ["form", "params"],
    "additionalProperties": False,
}
