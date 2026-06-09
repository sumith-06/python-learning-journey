"""
This code checks if the password is valid/invalid based on the condition.
condition for the password to be valid:
1. password must contain only numbers.
2. 8 <= length of password <= 12 
"""

password = input("Enter the password: ")

if password.isdigit() and 8 <= len(password) <=12:
  print("Valid")
else:
  print("Invalid")
