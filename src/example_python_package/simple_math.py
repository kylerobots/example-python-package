import numpy

def add(a, b):
    # This is overly complex, but is done to incorporate a numpy dependency.
    a_array = numpy.array(object=[a])
    b_array = numpy.array(object=[b])
    result = numpy.add(a_array, b_array)
    return result.flatten()[0].item()

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
