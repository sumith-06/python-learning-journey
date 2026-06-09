#for a given string this code gives reverse of it.
#using two pointer approach.

def reverse_string(word):
  letters = list(word)
  j = len(letters)-1
  for i in range(len(letters)//2):
    letters[i], letters[j] = letters[j], letters[i]
    j -= 1
  return letters

text = input("enter the text: ")
reverse_text = reverse_string(text)
print("".join(reverse_text))