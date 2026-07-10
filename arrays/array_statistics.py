"""
Returns all of these of an array:
Sum
Maximum
Minimum
Count of even numbers
"""

def array_statistics(arr):
  if not arr:
    return None
  total, maximum, minimum, count_even = 0, arr[0], arr[0], 0
  for num in arr:
    total += num
    if num > maximum:
      maximum = num
    if num < minimum:
      minimum = num
    if num%2 == 0:
      count_even += 1
  return total, maximum, minimum, count_even
