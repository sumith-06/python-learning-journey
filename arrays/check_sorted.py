def check_sorted(arr):
  for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
      return False
    i += 1
  return True