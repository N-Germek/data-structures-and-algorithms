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
        self.rear = None

    def some_method(self):
        # method body here
        pass

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            while self.rear.next is None:
                self.rear.next = new_node

    def dequeue(self):
        # if self.front is None:
        #     raise InvalidOperationError(Exception())
        if self.front:
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            if self.rear is not None:
                self.rear = None
                raise InvalidOperationError(Exception())

    def peek(self):
        if self.front is None:
            raise InvalidOperationError(Exception())
        else:
            return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
