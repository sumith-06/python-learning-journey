# Insertion sort

# Time complexity : O(n**2); Best case : O(n)
# Space complexity : O(1)

def insertion_sort(arr):
  n = len(arr)

  for i in range(1,n):
    j = i
    while j > 0:
      if arr[j] < arr[j-1]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1
      else:
        break
  return arr

arr = [7,3,5,1,9,2]
print(insertion_sort(arr))