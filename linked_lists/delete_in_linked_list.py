class Node():
    def __init__(self, data, next_node = None):
      self.data = data
      self.next_node = next_node

class LinkedList():
  def __init__(self):
    self.head = None

  def delete(self, value):

    if self.head is None:
      return

    if self.head.data == value:
      temp = self.head
      self.head = temp.next_node
      temp.next_node = None
      return
    
    current = self.head
     
    while current.next_node is not None and current.next_node.data != value:
      current = current.next_node

    if current.next_node is None:
      print(f"{value} doesn't exist")
      return

    temp = current.next_node
    current.next_node = temp.next_node
    temp.next_node = None
