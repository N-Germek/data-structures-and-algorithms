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

    # def traverse(self):
    #     current = self.front
    #     while current.next is not None:
    #         current = current.next
    #     return current

    def enqueue(self, value):
        new_node = Node(value)
        Node.next = self.rear(Node += 1)
        self.rear = new_node

        # if not self.front:
        #     self.front = Node(value)
        # else:
        #     while self.front.next is not None:
        #         current = self.front
        #         node = Node(value)
        #         final_node = self.traverse()
        #         current = final_node
        #         current.back = node

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError(Exception())
        if self.front:
            temp = self.front
            self.front = self.front.back
            temp.back = None
            print(temp.value)
            return temp.value

    def peek(self):
        if self.front is None:
            return self.front.value
        else:
            raise InvalidOperationError(Exception())

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
