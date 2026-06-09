"""
This code checks if the given string is a palindrome or not.
It also uses .lower() and .replace() so,
# the code is case-insensitive
# ignores spaces between the words
Example:
"Nurses Run" -> Palindrome
"hello"      -> Not a palindrome
"""

def is_palindrome(text):
  clean_text = text.lower().replace(" ", "")
  reverse_text = clean_text[::-1]
  return clean_text == reverse_text
  

text = input("Enter the text: ")
if is_palindrome(text):
  print(f"{text} is a palindrome")
else:
  print(f"{text} is not a palindrome")