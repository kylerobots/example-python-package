"""Tests for the add function."""

from example_python_package.simple_math import add


def test_add() -> None:
    """Test the add function with some simple cases."""
    assert add(a=1, b=2) == 3  # noqa: PLR2004
    assert add(a=0, b=0) == 0
    assert add(a=-1, b=1) == 0
    assert add(a=1, b=-1) == 0
    assert add(a=-1, b=-1) == -2  # noqa: PLR2004
