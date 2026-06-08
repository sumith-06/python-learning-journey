"""
This code runs an interactive guessing game that repeatedly asks the user for a number, offers "too high" or "too low" hints, 
and stops only when the correct secret number is guessed.
"""

secret = 22

while True:
  guess_number = int(input("Enter your guess: "))

  if guess_number == secret:
    print("That's correct!")
    break
  elif guess_number > secret:
    print("Wrong guess. (Hint : your guess is number greater than the secret number)")
    print("Try again\n")
  else:
    print("Wrong guess. (Hint : your guess is number less than the secret number)")
    print("Try again\n")