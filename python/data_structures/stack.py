class Stack:
    """
    Put docstring here

    push(value)
    // INPUT < -- value to add, wrapped in Node internally
    // OUTPUT < -- none
    node = new Node(value)
    node.next < -- Top
    top < -- Node
    """

    def __init__(self, top=None):
        # initialization here
        self.top = top

    def some_method(self):
        # method body here
        pass

    def push(self, value):
        node = Node(value)
        top = node.next
        node.top = node
        if self.top is None:
            self.top = node
        elif self.top is not None:
            node.next = self.top
        self.top = node

    # ALGORITHM
    # pop()
    # // INPUT < -- No input
    # // OUTPUT < -- value of top Node in stack
    # // EXCEPTION if stack is empty
    #
    # Node temp < -- top
    # top < -- top.next
    # temp.next < -- null
    # return temp.value
    def pop(self, value):
        temp = self.top
        top = Node(value)
        if temp is None:
            return Exception
        else:
            temp = self.next.top
            top = self.temp.value
        return temp.value

    def peek(self, value):
        self.top = Node(value)
        if self.top is None:
            return Exception
        else:
            return self.top.value


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


if __name__=="__main__":
    stack = []

