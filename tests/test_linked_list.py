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


def test_list_comprehension():
  list = LinkedList()
  list.append('a')
  list.append('b')
  list.append('c')
  
  comp_list = [x for x in list]
  
  actual = comp_list
  expected = ['a', 'b', 'c']
  
  assert actual == expected
  

def test_length():
  list = LinkedList
  list.append(1)
  list.append('b')
  list.append('c')
  
  actual = len(list)
  expected = 3
  assert actual == expected