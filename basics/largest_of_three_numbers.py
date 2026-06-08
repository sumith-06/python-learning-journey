"""
This code gives the largest number among the 3 numbers given by user
without using max()
"""
print("Enter the three numbers:")
first_number = int(input("first number: "))
second_number = int(input("second number: "))
third_number = int(input("third number: "))
if first_number >= second_number and first_number >= third_number:
  print(f"{first_number} is the largest number among them")
elif second_number >= first_number and second_number >= third_number:
  print(f"{second_number} is the largest number among them")
else: 
  print(f"{third_number} is the largest number among them")