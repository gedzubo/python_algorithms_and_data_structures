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