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