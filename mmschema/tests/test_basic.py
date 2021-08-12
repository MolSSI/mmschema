"""
Basic sanity test for the mmschema package.
"""
import pytest
import mmschema
import mm_data
import json


def test_mmschema_imported():
    """Sample test, will always pass so long as import statement worked"""
    import sys

    assert "mmschema" in sys.modules


def test_validate():
    with open(mm_data.mols["alanine.json"], "r") as fileobj:
        mol = json.load(fileobj)
    mmschema.validate(mol, "molecule", 1)
