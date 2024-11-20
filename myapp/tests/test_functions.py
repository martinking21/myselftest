# myapp/tests/test_functions.py

import pytest
from myapp.functions import add

def test_add():
    """Test unitaire pour la fonction add."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
