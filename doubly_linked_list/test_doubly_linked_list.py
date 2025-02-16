from doubly_linked_list import DoublyLinkedList

def test_push():
    linked_list = DoublyLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.print() == '1 -> 2 -> 3'

def test_push_single_element():
    linked_list = DoublyLinkedList()
    linked_list.push(1)
    assert linked_list.print() == '1'

def test_pop():
    linked_list = DoublyLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.pop() == 3
    assert linked_list.pop() == 2
    assert linked_list.pop() == 1
    assert linked_list.pop() == None

def test_shift():
    linked_list = DoublyLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.shift() == 1
    assert linked_list.shift() == 2
    assert linked_list.shift() == 3
    assert linked_list.shift() == None

def test_unshift():
    linked_list = DoublyLinkedList()
    linked_list.unshift(1)
    linked_list.unshift(2)
    linked_list.unshift(3)
    assert linked_list.print() == '3 -> 2 -> 1'

def test_get():
    linked_list = DoublyLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.get(0).value == 1
    assert linked_list.get(1).value == 2
    assert linked_list.get(2).value == 3
    assert linked_list.get(3) == None

def test_get_out_of_bounds():
    linked_list = DoublyLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.get(-1) == None
    assert linked_list.get(3) == None

def test_set():
    linked_list = DoublyLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.set(0, 4)
    linked_list.set(1, 5)
    linked_list.set(2, 6)
    assert linked_list.print() == '4 -> 5 -> 6'

def test_insert():
    linked_list = DoublyLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.insert(0, 4)
    linked_list.insert(2, 5)
    linked_list.insert(4, 6)
    assert linked_list.print() == '4 -> 1 -> 5 -> 2 -> 6 -> 3'

def test_insert_out_of_bounds():
    linked_list = DoublyLinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.insert(-1, 4) == False
    assert linked_list.insert(4, 4) == False