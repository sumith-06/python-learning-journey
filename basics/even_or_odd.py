#This code asks the user to enter a number and correctly identifies whether it is even or odd.
num = int(input("Enter the number: "))
if num%2==0:
  print(f"{num} is an even number")
else:
  print(f"{num} is an odd number")
