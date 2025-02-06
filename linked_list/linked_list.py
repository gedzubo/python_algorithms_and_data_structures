from node import Node

class LinkedList:
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
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            value = self.tail.value
            self.tail = current_node
            self.tail.next = None
            self.length -= 1
            return value
    
    def shift(self):
        if self.head is None:
            return None
        else:
            value = self.head.value
            self.head = self.head.next
            self.length -= 1
            return value

    def unshift(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            return current_node.value
        
    def set(self, index, value):
        if index < 0 or index >= self.length:
            return False
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            current_node.value = value
            return True