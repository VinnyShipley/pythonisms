class LinkedList:
  
  # Dunder methods
  
  def __init__(self, collection=None):
    self.head = None
    if collection:
      for item in reversed(collection):
        self.insert(item)
        
  def __iter__(self):
    pass
  
  # Regular methods
  
  def insert(self, value):
    self.head = Node(value)
  
  def append(self, value):
    if self.head == None:
      self.head = Node(value)
      
    current = self.head
    
    while current.next:
      current = current.next
    
    current.next = Node(value)


class Node:
  
  # Dunder methods
  
  def __init__(self, value, next=None):
    self.value = value
    self.next = next