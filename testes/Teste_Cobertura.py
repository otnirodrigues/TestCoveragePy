import pytest
from src.triangle import triangle_type


def testNotTriangle():
    assert triangle_type(3,13,5) == 'Not a triangle'

def testIsEquilateral():
    assert triangle_type(3,3,3) == 'Equilateral'

def testIsIsosceles():
        assert triangle_type(3,3,5) == 'Isosceles'

def testIsScalene():
    assert triangle_type(7,3,5) == 'Scalene'