number = int(input("Enter the number: "))

def fibonacci(number):
  print(0, 1, end=" ")
  first, second = 0, 1
  for i in range(number):
    next_num = first + second
    print(next_num, end=" ")
    first, second = second, next_num

    
if number == 0:
  print(0)
elif number == 1:
  print(1)
elif number<1:
  fibonacci(number)
else:
  print("Invalid input")