arr = [1,2,3,4,5]

sum = 0
maximum = arr[0]
minimum = arr[0]

for num in arr:
  print(num, end=" ")
  sum += num
  if num > maximum:
    maximum = num
  if num < minimum:
    minimum = num
print("\n")
print(f"Sum is {sum}")
print(f"Largest number is {maximum}")
print(f"Smallest number is {minimum}")