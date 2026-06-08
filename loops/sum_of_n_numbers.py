"""
This code calculates the sum of the first 'n' natural numbers.
"""
number = int(input("Enter the number: "))
result = 0
for i in range(1, number + 1):
  result += i
print(f"The sum of first {number} natural numbers is: {result}")
