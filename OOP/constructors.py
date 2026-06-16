# A constructor is a special method that is automatically called when an object is created from a class.
# Its primary purpose is to initialize the object's data.

"""
Syntax:
class ClassName:
    def __init__(self):
        pass
"""
# Python automatically calls __init__()
# when a new object is created.

#Example: passing data to objects

class Student:
  def __init__(self, name, rollno):
    self.name = name
    self.rollno = rollno


student1 = Student("Sumith", 553)

student1 = Student("Sumith", 553)
# Internally, Python does something similar to:
# Student.__init__(student1, "Sumith", 553),  Its calls __init__()

print(f"{student1.name} - {student1.rollno} ")

# Instance variables: Variables stored inside an object is called Instance variables
#Example:
#self.name, self.marks