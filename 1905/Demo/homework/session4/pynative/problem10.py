#  Calculate the area of different shapes using OOP
# You have given a Shape class and subclasses Circle  and Square. The parent class (Shape) has a area() method.

# class Shape:
#     def area(self):
#         raise NotImplementedError("Area method must be implemented by subclasses")

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        # raise NotImplementedError("Area method must be implemented by subclasses")
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):  # Overriding the area method
        return math.pi * self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):  # Overriding the area method
        return self.side * self.side

# s = Shape()

# Example of polymorphism
shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(shape.area())  # Output: 78.53975, 49, 28.27431