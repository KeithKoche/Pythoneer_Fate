import math


class Geometric_figure:
    angles = 4

    def add_area(self, other):
        if isinstance(other, T):
            return other.area() + self.area()
        if isinstance(other, S):
            return other.area() + self.area()
        if isinstance(other, R):
            return other.area() + self.area()
        if isinstance(other, C):
            return other.area() + self.area()
        raise NotImplemented

class T(Geometric_figure):
    angles = 3
    name = 'Triangle'
    def __init__(self, a, b ,c):
        self.side1 = a
        self.side2 = b
        self.side3 = c


    def perimeter(self):
        return math.floor(self.side1 + self.side2 + self.side3)

    def half_perimeter(self):
        return math.floor((self.side1 + self.side2 + self.side3) / 2)

    def area(self):
        return math.floor((((((((self.side1 + self.side2 + self.side3) / 2) * (((self.side1 + self.side2 + self.side3) / 2) -
        self.side1)) * (((self.side1 + self.side2 + self.side3) / 2) - self.side2)) * (((self.side1 + self.side2 +
        self.side3) / 2) - self.side3)))**0.5))


class R(Geometric_figure):
    name = 'Rectangle'
    def __init__(self, a, b):
        self.side1 = a
        self.side2 = b

    def area(self):
        return math.floor(self.side1 * self.side2)

    def perimeter(self):
        return math.floor((self.side1 + self.side2) * 2)


class S(Geometric_figure):
    name = 'Square'
    def __init__(self, a):
        self.side = a

    def area(self):
        return math.floor(self.side**2)

    def perimeter(self):
        return math.floor(self.side * 4)


class C(Geometric_figure):
   angles = 0
   name = 'Circle'
   def __init__(self, r):
       self.rad = r

   def area(self):
       return math.floor(self.rad**2 * math.pi)

   def perimeter(self):
       return math.floor(self.rad * 2 * math.pi)


import pytest


def test_pytraise():
    with pytest.raises(TypeError):
        R()

def test_class():
    assert T(443, 333, 123).__class__ == T

def test_per():
    assert R(2, 4).perimeter() == 12

def test_name():
    assert C.name == 'Circle'

def test_angless():
    assert S.angles != 3

def test_ar():
    assert C(35.3333).area() == 3922


