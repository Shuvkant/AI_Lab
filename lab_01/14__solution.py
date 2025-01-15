"""
 Write a pithon program to create a class representing a Circle. Include methods to calculate its area
and perimeter.
"""
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = (math.pi)*pow(self.radius, 2)
        print(f"{area:.2f}")

    def perimeter(self):
        perimeter = (math.pi)*2*(self.radius)
        print(f"{perimeter:.2f}")


p1 = Circle(5)
p1.area()
p1.perimeter()
