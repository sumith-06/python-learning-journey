"""
Traverse the array.
If the target is found:
Return its index.
If the target is not found:
Return -1
"""

def linear_search(arr, target):
  for i in range(len(arr)):
    if target == arr[i]:
      return i
  return -1
