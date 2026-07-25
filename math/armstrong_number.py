# This function checks if a given number is an Armstrong number.

def isArmstrong(n):
  if n < 0:
    return False
  original = n
  count = 0
  if n == 0:
    count = 1
  else:
    while n > 0:
      n //= 10
      count += 1
  n = original
  sum = 0
  while n > 0:
    sum += (n % 10) ** count
    n //= 10
  return original == sum

# Example usage:
print(isArmstrong(153))  # Output: True
print(isArmstrong(9474)) # Output: True
print(isArmstrong(123))  # Output: False