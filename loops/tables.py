"""
This code prints the multiplication table of a number given by user
"""
number = int(input("Enter the number: "))
print(f"The multiplication table of {number} is:")
for i in range(1, 11):
  print(f"{number} * {i} = {number * i}")
