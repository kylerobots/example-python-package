"""Tests for the multiply function."""

from example_python_package.simple_math import multiply


def test_multiply() -> None:
    """Test the multiply function with a simple case."""
    assert multiply(a=4, b=2) == 8  # noqa: PLR2004
