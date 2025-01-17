from math import pi


class Shape():
    def area(self):
        return 0


class Reactangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi*pow(self.radius, 2)


Rect_object = Reactangle(2, 3)
Circle_object = Circle(5)

print(f"Area of Reactangle is: {Rect_object.area()}")
print(f"Area of Circle is: {Circle_object.area():.2f}")
