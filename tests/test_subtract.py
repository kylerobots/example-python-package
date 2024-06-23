"""Tests for the subtract function."""

from example_python_package.simple_math import subtract


def test_subtract() -> None:
    """Test the subtract function with some simple cases."""
    assert subtract(a=1, b=2) == -1
    assert subtract(a=0, b=0) == 0
    assert subtract(a=-1, b=1) == -2  # noqa: PLR2004
    assert subtract(a=1, b=-1) == 2  # noqa: PLR2004
    assert subtract(a=-1, b=-1) == 0
