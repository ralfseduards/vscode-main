#linked lists are lists where elements have a value and a pointer to the next value
# there are stacks and queues with coresponding LIFO and FIFO structures
# collections .deque - double ended queue (can acess items from the beginning or the end with O(1))

# deque(["a", "b", "c"]) == deque("abc") >> True

# .append(); .pop(); .remove(); .insert() works on deques
# if i want to pop or append from the beginning i use: .appendleft(); .popleft()


# QUEUES
# add values - enqueue, remove - dequeue

# traversing = iterating over


# types of linked lists:
# 1. single pointer (classic)
# 2. double pointer (can traverse in both directions)
# circular (end points to the head)


def deque():
    from collections import deque

    queue = deque()
    queue.append("Mary")
    queue.append("John")
    queue.append("Alice")
    # a queue should remove from the start (FIFO)
    queue.popleft()


    stack = deque()
    stack.appendleft("https://realpython.com/")
    stack.appendleft("https://realpython.com/pandas-read-write-files/")
    stack.appendleft("https://realpython.com/python-csv/")
    # how to go back to the home page?
    stack.popleft()
    stack.popleft()
    print(stack)

# this shit fucked me up https://realpython.com/linked-lists-python/
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
                # takes the first node
            node = Node(nodes.pop(0))
                # sets it as head
            self.head = node
                # inits all nodes(except the popped one) as Node
            for elem in nodes:
                node.next = Node(elem)
                node = node.next


    def add_first(self, value):
        # The node has to be an instance of the Node class
        node = Node(value)
        # points the starting node to the current node
        node.next = self.head
        # sets the head as node
        self.head = node

    def add_last(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        for current_node in self: # interesting! - itereating over self is possible due to the __iter__ method; the for loop is used to get the last node!
            pass
        current_node.next = node # the previously last node points to the new one

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("The list is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = target_node_data
                return
        raise Exception(f"Node with data {target_node_data} is not found!")
    
    def remove_node(self, target_node_value):
        if self.head is None:
            raise Exception("There are no nodes!")
        previous_node = self.head
        for node in self:
            if node.data == target_node_value:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception(f"The node with value {target_node_value} could not be found!")


    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Node:
    def __init__(self, data):
        # define the main elements of a linked list
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

llist = LinkedList()
# init nodes
first_node = Node("a")
second_node = Node("b")
third_node = Node("c")

# set the head
llist.head = first_node

# set pointers
first_node.next = second_node
second_node.next = third_node

llist2 = LinkedList(["a", "b", "c"])
llist2.add_first("1")
llist2.add_last("last")
print(llist2)
llist2.remove_node("c")
print(llist2)
