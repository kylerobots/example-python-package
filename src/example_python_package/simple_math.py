"""Simple math functions."""

import numpy


def add(a: float | int, b: float | int) -> float | int:
    """Add two numbers together.

    Parameters
    ----------
    a
        The first number.
    b
        The second number.

    Returns
    -------
        a + b
    """
    # This is overly complex, but is done to incorporate a numpy dependency.
    a_array = numpy.array(object=[a])
    b_array = numpy.array(object=[b])
    result = numpy.add(a_array, b_array)
    return result.flatten()[0].item()


def subtract(a: float | int, b: float | int) -> float | int:
    """Subtract two numbers.

    Parameters
    ----------
    a
        The first number.
    b
        The second number.

    Returns
    -------
        a - b
    """
    return a - b


def multiply(a: float | int, b: float | int) -> float | int:
    """Multiply two numbers.

    Parameters
    ----------
    a
        The first number.
    b
        The second number.

    Returns
    -------
        a * b
    """
    return a * b


def divide(a: float | int, b: float | int) -> float:
    """Divide two numbers.

    Parameters
    ----------
    a
        The numerator.
    b
        The denominator.

    Returns
    -------
        a / b

    Raises
    ------
    ValueError
        Raised if the denominator is zero.
    """
    if b == 0:
        msg = "Cannot divide by zero."
        raise ValueError(msg)
    return a / b
