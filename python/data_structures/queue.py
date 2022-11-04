class Queue:
    """
    enqueue(value)
    // INPUT <-- value to add to queue (will be wrapped in Node internally)
    // OUTPUT <-- none
   node = new Node(value)
   rear.next <-- node
   rear <-- node


    """

    def __init__(self, front=None):
        # initialization here
        self.front = front
        self.next = next

    def some_method(self):
        # method body here
        pass

    def traverse(self):
        current = self.head
        while current.next is not None:
            current = current.next
        return current

    def enqueue(self, value):
        while self.next is not None:
            node.self(traverse()):
        self.next = Node(value)


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
