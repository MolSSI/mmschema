"""
Schema validation tools
"""

import jsonschema
from . import versions
from typing import Dict, Any


def validate(data: Dict[str, Any], schema_type: str, version: int):
    """
    Validates a given input for a schema input and output type.
    """
    schema = versions.get_schema(schema_type, version)

    for key, value in data.items():
        if hasattr(value, "shape"):
            data[key] = value.tolist()  # expensive

    jsonschema.validate(data, schema)
