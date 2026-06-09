"""
Given a list of numbers which contain a unique number and all other numbers appear twice.
find the unique number from the list.
"""
numbers = [4, 3, 5, 3, 5, 9, 4, 13, 9]
def get_unq_number(numbers):
  unq = 0
  for number in numbers:
    unq ^= number
  return unq
print(f"The unique number in the list is {get_unq_number(numbers)}")