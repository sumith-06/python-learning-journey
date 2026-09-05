class Node():
    def __init__(self, data, next_node = None):
      self.data = data
      self.next_node = next_node

class LinkedList():
  def __init__(self):
    self.head = None

  def insert_at(self, data, position):
    new_node = Node(data)

    if position < 0:
      print("Invalid position")
      return 
    
    if position == 0:
      new_node.next_node = self.head
      self.head = new_node
      return

    current = self.head
    index = 0


    while current is not None and index != position - 1:
      current = current.next_node
      index += 1

    if current is None:
      print("Invalid Position")
      return
    
    new_node.next_node = current.next_node
    current.next_node = new_node


  def insert_sorted(self, data):
    new_node = Node(data)

    if self.head is None:
      self.head = new_node
      return
    
    if new_node.data < self.head.data:
      new_node.next_node = self.head
      self.head = new_node
      return
    
    current = self.head
    
    while current.next_node is not None and current.next_node.data < new_node.data:
      current = current.next_node
    
    if current.next_node is None:
      current.next_node = new_node
      return
    
    new_node.next_node = current.next_node
    current.next_node = new_node