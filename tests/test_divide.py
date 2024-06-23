"""Tests for the divide function."""

import pytest

from example_python_package.simple_math import divide


def test_defined() -> None:
    """Test the divide function with a simple case."""
    assert divide(a=4, b=2) == 2  # noqa: PLR2004


def test_undefined() -> None:
    """Test the divide function with a case that should raise an exception."""
    with pytest.raises(expected_exception=ValueError):
        divide(a=4, b=0)
