def reverse_array(arr):
  L, R = 0, len(arr)-1
  while L < R:
    arr[L], arr[R] = arr[R], arr[L]
    L += 1
    R -= 1
  return arr