# Merge sort

# Time complexity : O(n log n)
# Space complexity : O(1)

def merge_sort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  left =  merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  i = j = 0
  result = []

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  if i < len(left):
    result += left[i:]
  if j < len(right):
    result += right[j:]

  return result

arr = [7,4,2,9,4,1]
print(merge_sort(arr))