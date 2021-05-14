"""
The base file for FF MMSchema.
"""

from .nonbonded import NonBonded
from .bonds import Bonds

# from .scf_wavefunction import scf_wavefunction
# from .localized_wavefunction import localized_wavefunction
# from .core_wavefunction import core_wavefunction
# from ..basis import basis

__all__ = ["ForceField"]

ForceField = {
    "type": "object",
    "properties": {"nonbonded": NonBonded},
    "description": "Wavefunction properties resulting from a computation."
    "Matrix quantities are stored in column-major order.",
    "additionalProperties": False,
    "required": ["nonbonded"],
}

# Update new keys
ForceField["properties"].update(Bonds)
# output_wavefunction["properties"].update(scf_wavefunction)
# output_wavefunction["properties"].update(localized_wavefunction)
# output_wavefunction["properties"].update(core_wavefunction)
