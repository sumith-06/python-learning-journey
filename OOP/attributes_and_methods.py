"""ATTRIBUTES"""
# Atributes are the properities  of an object created from a class
# They are simply variables that belong to an object.

class Student:
  pass

student1 = Student()

student1.name = "sumith"
student1.marks = 100


student2 = Student()

student2.name = "ravi"
student2.marks = 87

print(f"{student1.name} got {student1.marks} marks",
      f"{student2.name} got {student2.marks} marks",
      sep = "\n")

# Output:
# sumith got 100 marks
# ravi got 87 marks


"""METHODS"""
# Methods are the functions inside a class, which can be performed by the objects created from that class.

class Car:
  def intro(self):                             #self : "The object that is calling the method."
    print(f"This car is a {self.name}")


car1 = Car()

car1.name = "Range Rover"

car1.intro()

#output:
# This car is a Range Rover


#Another example using attributes and methods:

class  Bike:

  def about(self):
    print(f"The brand of bike is {self.brand}",
          f"Its model is {self.model}",
          f"The price is {self.price} on-road",
          sep ="\n")


first_bike = Bike()

first_bike.brand = "Kawasaki"
first_bike.model = "Ninja H2R (Hypersport)"
first_bike.price = "88 Lakh - 98 Lakh"

first_bike.about()

#Output:
#The brand of bike is Kawasaki
#Its model is Ninja H2R (Hypersport)
#The price is 88 Lakh - 98 Lakh on-road