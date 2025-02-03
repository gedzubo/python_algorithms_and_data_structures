from linked_list import LinkedList

def test_push():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.print() == '1 -> 2 -> 3'

def test_push_single_element():
    linked_list = LinkedList()
    linked_list.push(1)
    assert linked_list.print() == '1'