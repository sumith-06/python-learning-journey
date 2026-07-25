def isPalindrome(n):
  if n < 0:
    return False
  original = n
  reversed_number = 0
  while n > 0:
    reversed_number = (reversed_number * 10) + n % 10
    n //= 10 
  return original == reversed_number

# Example usage:
print(isPalindrome(121))   # Output: True
print(isPalindrome(-121))  # Output: False
print(isPalindrome(10))    # Output: False