from abc import ABC, abstractmethod


class GeometricShape(ABC):
    pi = 3.14

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        print("I probably have corners")


class Square(GeometricShape):
    def __init__(self, side):
        self.__side = side

    @property
    def get_side(self):
        return self.__side

    def set_side(self, new_side):
        self.__side = new_side

    def delete_side(self):
        del self.__side

    def area(self):
        return self.__side ** 2


class Circle(GeometricShape):
    def __init__(self, radius):
        self.__radius = radius

    @property
    def get_radius(self):
        return self.__radius

    def set_radius(self, new_radius):
        self.__radius = new_radius

    def delete_radius(self):
        del self.__radius

    def area(self):
        return self.pi * self.__radius ** 2

    def describe(self):
        print("I don't have corners")


square1 = Square(5)
square1.describe()
print("The side of the square is:", square1.get_side)
print("The area of the square is:", square1.area())
square1.set_side(8)
print("After calling 'set' method, the side of the square is:", square1.get_side)
print("The area of the square becomes:", square1.area())
square1.delete_side()
# square1.get_side  #  <-- if we do this, we'll get an AttributeError, because after delete, object has no attribute
print("------------------------------------------------------")
circle1 = Circle(3)
circle1.describe()
print("The radius of the circle is:", circle1.get_radius)
print("The area of the circle is:", circle1.area())
circle1.set_radius(5)
print("After calling 'set' method, the radius of the circle is:", circle1.get_radius)
print("The area of the circle becomes:", circle1.area())
circle1.delete_radius()
# circle1.get_radius  #  <-- if we do this, we'll get an AttributeError,
