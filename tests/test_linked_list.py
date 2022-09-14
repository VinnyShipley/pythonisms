from pythonisms.linked_list import LinkedList

def test_init():
  assert LinkedList

def test_insert_with_iter():
  list = LinkedList()
  thing_list = []
  
  list.insert('clown')
  
  for thing in list:
    thing_list.append(thing)
    
  actual = thing_list 
  expected = ['clown']
  
  assert actual == expected
  
