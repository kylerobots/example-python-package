import pytest
from example_python_package.simple_math import divide

def test_defined():
    assert divide(a=4, b=2) == 2

def test_undefined():
    with pytest.raises(expected_exception=ValueError):
        divide(a=4, b=0)
