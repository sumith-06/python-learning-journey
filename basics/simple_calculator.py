"""
This code is a simple calculator that performs basic arithmetic operations
like addition, subtraction, multiplication, and division based on user input.
It also handles division by zero and invalid operations gracefully."""
print("Enter the two numbers:")
first_number = float(input("first number: "))
second_number = float(input("second number: "))
print("Enter the operator (+, -, *, /):")
operation = input("operator: ")
if operation == "+":
  print(f"{first_number} + {second_number} = {first_number + second_number}")
elif operation == "-":
  print(f"{first_number} - {second_number} = {first_number - second_number}")
elif operation == "*":
  print(f"{first_number} * {second_number} = {first_number * second_number}")
elif operation == "/":
  if second_number == 0:
    print("Division by zero is not allowed.")
  else:
    print(f"{first_number} / {second_number} = {first_number / second_number}")
else:
  print("Invalid operation")