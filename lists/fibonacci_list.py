"""
This code gives the fibonacci series of first n numbers
"""

number = int(input("Enter the number: "))

def fibonacci(number):
  if number == 1:
    return [0]
  fiba = [0,1]
  first, second = 0, 1
  for i in range(2, number):
    next_number = first + second
    fiba.append(next_number)
    first, second = second, next_number
  return fiba


if number > 0:
  result = fibonacci(number)
  print(f"Fibonacci series of first {number} numbers is : {result}")
else:
  print("Invalid input")