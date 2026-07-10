#Returns the number of times target element appeared

def count_occurrence(arr, target):
  count = 0
  for element in arr:
    if target == element:
      count += 1
  return count
