class Node():
    def __init__(self, data, next_node = None):
      self.data = data
      self.next_node = next_node

class LinkedList():
  def __init__(self):
    self.head = None

  def display(self):
    if self.head is None:
      print("It is empty")
      return
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next_node