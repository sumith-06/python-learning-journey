"""
Returns the indices of the target element.
"""
def search_indices(arr, target):
  indices = []
  for i in range(len(arr)):
    if target == arr[i]:
      indices.append(i)
  return indices

