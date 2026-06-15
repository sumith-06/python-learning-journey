"""
Module 0: Why OOP Exists

Class: A blueprint for creating objects.
Object: An instance of a class.
"""

# Suppose we are building a Student Management System.
# Creating separate variables for each student is difficult.
# Example:
# student1_name = "Sumith"
# student2_name = "Rahul"
# ...
# student1000_name = "Alex"

# Managing thousands of such variables is inefficient.

# Instead, we create a class (blueprint)
# and generate multiple student objects from it.

class Student:
    pass

# Creating objects (instances) of Student class
student1 = Student()
student2 = Student()

print(student1)
print(student2)

# Output:
# <__main__.Student object at ...>
# <__main__.Student object at ...>

#Another Example


class Car():
   pass

toyato = Car()
print(toyato)

#Output:
#<__main__.Car object at ....>
