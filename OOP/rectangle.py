"""
Practice Problem: Rectangle Class

Concepts Practiced:
- Constructors (__init__)
- Instance variables
- Methods
- Returning values from methods

This program calculates the area and perimeter
of a rectangle using object-oriented programming.
"""

class Rectangle:
  def __init__(self, length, width):
    self.length = length
    self.width = width

  def  area(self):
    return  self.length * self.width
  
  def perimeter(self):
    return 2 * (self.length + self.width)

rect = Rectangle(5, 10)

print(f"Area : {rect.area()}",
      f"Perimeter : {rect.perimeter()}",
      sep = "\n")