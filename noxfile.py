"""A Nox file to test different versions of NumPy and Python."""

import nox


@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
@nox.parametrize(arg_names="numpy", arg_values_list=["1.26.4", "2.0.0"])
def tests(session: nox.Session, numpy: str) -> None:
    """Run unit tests on different versions of NumPy and Python.

    Arguments:
        session -- The Nox session object.
        numpy -- The version of NumPy to use.
    """
    session.install(f"numpy=={numpy}")
    session.install("pytest")
    session.install(".")
    session.run("pytest")
