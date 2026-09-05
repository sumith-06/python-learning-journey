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


  def display(self):
    if self.head is None:
      print("It is empty")
      return
    current = self.head
    while current is not None:
      print(current.data)
      current = current.next_node

  def search(self, value):
    current = self.head
    while current is not None:
      if current.data == value:
        return True
      current = current.next_node
    return False

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
