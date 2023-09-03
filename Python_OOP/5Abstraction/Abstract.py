from abc import ABC #abstract base class, not nessesary but used to clarity that class is abstract
import math


class Shape(ABC):
    
    def area(self):
        pass

    
    def perimeter(self):
        pass



# Concrete subclasses
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius



rectangle = Rectangle(5, 4)
circle = Circle(3)

print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

print(f"Circle Area: {circle.area()}")
print(f"Circle Circumference: {circle.perimeter()}")
