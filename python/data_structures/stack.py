from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Put docstring here

    push(value)
    // INPUT < -- value to add, wrapped in Node internally
    // OUTPUT < -- none
    node = new Node(value)
    node.next < -- Top
    top < -- Node

    pop()
    // INPUT < -- No input
    // OUTPUT < -- value of top Node in stack
    // EXCEPTION if stack is empty

    Node temp < -- top
    top < -- top.next
    temp.next < -- none
    return temp.value

    peek()
     // INPUT <-- none
    // OUTPUT <-- value of top Node in stack
    // EXCEPTION if stack is empty
    return top.value

    isEmpty()
    // INPUT <-- none
    // OUTPUT <-- boolean
    return top = None

    """

    def __init__(self, top=None):
        # initialization here
        self.top = top
        # self.size = 0

    def some_method(self):
        # method body here
        pass

    def push(self, value):
        self.top = Node(value, self.top)
        # node = Node(value)
        # node.next = self.top
        # self.top = node

    # self.size += 1, note to increase size of array

    # if self.top is None:
    #     self.top = node
    # elif self.top is not None:
    #     node.next = self.top
    # self.top = node

    def pop(self):
        # temp = self.top
        # top = Node(value)
        if not self.top:
            raise InvalidOperationError(Exception("Method not allowed on empty collection"))
        temp = self.top
        self.top = self.top.next
        return temp.value

    def peek(self):
        # self.top = Node(value)
        if self.top is None:
            raise InvalidOperationError(Exception("Method not allowed on empty collection"))
        else:
            return self.top.value

    def is_empty(self):
        # if self.top is None:
        return self.top is None

# if self.top is none:
# return self.top
# else:
# return self.top.value


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

