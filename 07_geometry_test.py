# Testing the geometry package
from geometry import circle, rectangle

radius = float(input("Enter circle radius: "))
print("Area of circle:", round(circle.area(radius), 2))

length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breadth: "))
print("Area of rectangle:", rectangle.area(length, breadth))
