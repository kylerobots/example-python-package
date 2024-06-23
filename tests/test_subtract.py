from example_python_package.simple_math import subtract

def test_subtract():
    assert subtract(a=1, b=2) == -1
    assert subtract(a=0, b=0) == 0
    assert subtract(a=-1, b=1) == -2
    assert subtract(a=1, b=-1) == 2
    assert subtract(a=-1, b=-1) == 0
