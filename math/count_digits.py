# this function counts the number of digits in an integer n


def count_digits(n):
  count, n = 0, abs(n)
  if n == 0:
    return 1
  while n > 0:
    n //= 10
    count += 1
  return count

# Example usage:
print(count_digits(12345))  # Output: 5   
print(count_digits(0))      # Output: 1
print(count_digits(-123))   # Output: 3