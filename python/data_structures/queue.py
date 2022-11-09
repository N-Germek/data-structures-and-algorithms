from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    enqueue(value)
    // INPUT <-- value to add to queue (will be wrapped in Node internally)
    // OUTPUT <-- none
   node = new Node(value)
   rear.next <-- node
   rear <-- node

    dequeue()
    // INPUT <-- none
    // OUTPUT <-- value of the removed Node
    // EXCEPTION if queue is empty

   Node temp <-- front
   front <-- front.next
   temp.next <-- null

   return temp.value

    peek()
    // INPUT <-- none
    // OUTPUT <-- value of the front Node in Queue
    // EXCEPTION if Queue is empty

   return front.value

    """

    def __init__(self, front=None):
        # initialization here
        self.front = front
        self.next = next

    def some_method(self):
        # method body here
        pass

    def traverse(self):
        current = self.front
        while current.next is not None:
            current = current.next
        return current

    def enqueue(self, value):
        if not self.front:
            self.front = Node(value)
        else:
            while self.next is not None:
                current = self.front
                node = Node(value)
                final_node = self.traverse()
                current = final_node
                current.next = node

    # def pop(self):
    #     # temp = self.top
    #     # top = Node(value)
    #     if not self.top:
    #         raise InvalidOperationError(Exception("Method not allowed on empty collection"))
    #     temp = self.top
    #     self.top = self.top.next
    #     return temp.value
    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError(Exception())
        elif self.front is not None:
            temp = self.front
            temp.next = None
            return temp.value

    def peek(self):
        pass

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
