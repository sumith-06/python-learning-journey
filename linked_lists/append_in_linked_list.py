class Node():
    def __init__(self, data, next_node = None):
      self.data = data
      self.next_node = next_node

class LinkedList():
  def __init__(self):
    self.head = None

  def append(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      
    else:
      current = self.head

      while current.next_node != None:
        current = current.next_node
      current.next_node = new_node