class Node():
    def __init__(self, data, next_node = None):
      self.data = data
      self.next_node = next_node

class LinkedList():
  def __init__(self):
    self.head = None

  def search(self, value):
    current = self.head
    while current is not None:
      if current.data == value:
        return True
      current = current.next_node
    return False