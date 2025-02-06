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

def test_pop():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.pop() == 3
    assert linked_list.pop() == 2
    assert linked_list.pop() == 1
    assert linked_list.pop() == None

def test_shift():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.shift() == 1
    assert linked_list.shift() == 2
    assert linked_list.shift() == 3
    assert linked_list.shift() == None

def test_unshift():
    linked_list = LinkedList()
    linked_list.unshift(1)
    linked_list.unshift(2)
    linked_list.unshift(3)
    assert linked_list.print() == '3 -> 2 -> 1'

def test_get():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.get(0) == 1
    assert linked_list.get(1) == 2
    assert linked_list.get(2) == 3
    assert linked_list.get(3) == None

def test_get_out_of_bounds():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    assert linked_list.get(-1) == None
    assert linked_list.get(3) == None

def test_set():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    linked_list.push(3)
    linked_list.set(0, 4)
    linked_list.set(1, 5)
    linked_list.set(2, 6)
    assert linked_list.print() == '4 -> 5 -> 6'