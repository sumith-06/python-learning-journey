# This function takes an integer n as input and returns its reverse.

def reverse_integer(n):
  if n == 0:
    return 0
  n_abs = abs(n)
  reversed_number = 0
  while n_abs > 0:
    reversed_number = (reversed_number * 10) + n_abs % 10
    n_abs //= 10
  return -reversed_number if n < 0 else reversed_number

# Example usage:
print(reverse_integer(12345))  # Output: 54321
print(reverse_integer(-123))   # Output: -321
print(reverse_integer(0))      # Output: 0