"""This module contains simple math functions."""

import numpy


def add(a: float | int, b: float | int) -> float | int:
    """Add two numbers.

    Arguments:
        a -- The first number to add.
        b -- The second number to add.

    Returns:
        a + b
    """
    # This is overly complex, but is done to incorporate a numpy dependency.
    a_array = numpy.array(object=[a])
    b_array = numpy.array(object=[b])
    result = numpy.add(a_array, b_array)
    return result.flatten()[0].item()


def subtract(a: float | int, b: float | int) -> float | int:
    """Subtract two numbers.

    Arguments:
        a -- The first number to subtract.
        b -- The second number to subtract.

    Returns:
        a - b
    """
    return a - b


def multiply(a: float | int, b: float | int) -> float | int:
    """Multiple two numbers.

    Arguments:
        a -- The first number to multiply.
        b -- The second number to multiply.

    Returns:
        a * b
    """
    return a * b


def divide(a: float | int, b: float | int) -> float:
    """Divide two numbers.

    Arguments:
        a -- The numerator.
        b -- The denominator.

    Raises:
        ValueError: Raised if the denominator is zero.

    Returns:
        a / b
    """
    if b == 0:
        msg = "Cannot divide by zero."
        raise ValueError(msg)
    return a / b
