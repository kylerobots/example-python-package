from example_python_package.simple_math import add

def test_add():
    assert add(a=1, b=2) == 3
    assert add(a=0, b=0) == 0
    assert add(a=-1, b=1) == 0
    assert add(a=1, b=-1) == 0
    assert add(a=-1, b=-1) == -2
