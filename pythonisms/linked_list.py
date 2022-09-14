class LinkedList:
  
  # Dunder methods
  
  def __init__(self, collection=None):
    self.head = None
    if collection:
      for item in reversed(collection):
        self.insert(item)
        
  def __iter__(self):
    
    def value_generator():
      current = self.head
      
      while current:
        yield current.value
        current = current.next

    return value_generator()

  def __str__(self):
      out = ''
      
      for value in self:
        out += f'{ {value} } -> '
      
      return out + 'None'


  # Class methods
  
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