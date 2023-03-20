# make a queue object

class Node:
    def __init__(self, value, pointer = None):
        self.value = value
        self.pointer = pointer
    
    def __repr__(self):
        return self.value

class Stack:
    def __init__(self, nodes = None):
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next

    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        for current_node in self:
            pass
        current_node.next = node

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def print(self):
        node = self.head
        while node is not None:
            print(node)
            node = node.next


s = Stack()

n1 = Node("a")
n2 = Node("b")
n3 = Node("c")

s.head = n1

n1.next = n2 
n2.next = n3

s.print()