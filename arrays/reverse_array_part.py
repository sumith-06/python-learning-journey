def reverse_array_part(arr, start_index, end_index):
  while start_index < end_index:
    arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
    start_index += 1
    end_index -= 1
  return arr
