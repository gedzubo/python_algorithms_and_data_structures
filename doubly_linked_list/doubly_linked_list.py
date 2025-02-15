from node import Node

class DoublyLinkedList:
    def __init__(self, initial_value=None):
        if initial_value is not None:
            new_node = Node(initial_value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def __len__(self):
        return self.length
    
    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def print(self):
        nodes = []
        current_node = self.head
        while current_node is not None:
            nodes.append(str(current_node))
            current_node = current_node.next

        return ' -> '.join(nodes)

    def pop(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
            self.length -= 1
            return temp.value
        
    def shift(self):
        if self.head is None:
            return None
        elif self.length == 1:
            value = self.head.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            tmp = self.head
            self.head = self.head.next
            self.head.prev = None
            tmp.next = None
            self.length -= 1
            return tmp.value
        
    def unshift(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index < self.length / 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            return current_node
        else:
            current_node = self.tail
            i = self.length - 1
            while i > index:
                current_node = current_node.prev
                i -= 1
            return current_node
        
    def set(self, index, value):
        if index < 0 or index >= self.length:
            return False
        else:
            current_node = self.get(index)
            current_node.value = value
            return True


