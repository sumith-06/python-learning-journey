# Bubble sort

# Time complexity = O(n**2)
# Space complexity = O(1)

def bubble_sort(nums):
  n = len(nums)
  for i in range(1,n):
    swapped = False
    for j in range(n - i):
      if nums[j] > nums[j + 1]:
        nums[j], nums[j + 1] = nums[j + 1], nums[j]
        swapped = True
    if not swapped:
      return nums
  return nums

arr = [1, 2, 3, 4, 5]
print(bubble_sort(arr))