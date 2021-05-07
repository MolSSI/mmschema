"""
Basic sanity test for the mmschema package.
"""
import pytest
import mmschema


def test_mmschema_imported():
    """Sample test, will always pass so long as import statement worked"""
    import sys

    assert "mmschema" in sys.modules
