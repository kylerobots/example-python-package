import nox

@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
@nox.parametrize(arg_names="numpy", arg_values_list=["1.26.4", "2.0.0"])
def tests(session, numpy):
    session.install(f"numpy=={numpy}")
    session.install("pytest")
    session.install(".")
    session.run("pytest")
