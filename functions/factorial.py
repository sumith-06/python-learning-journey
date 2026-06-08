def factorial(number):
  solution = 1
  for i in range(1, number + 1):
    solution *= i
  return solution


number = input("Enter the number: ")
if number.isdigit() and int(number) >= 0:
  number = int(number)
  fact = factorial(number)
  print(f"The factorial of {number} is: {fact}")
else:
  print("Invalid input")