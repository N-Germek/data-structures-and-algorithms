class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return f'{self.head}'

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        #     inserted the second node into the head position
        elif self.head is not None:
            node.next = self.head
#             assigned head to be new node
            self.head = node

        #     Head
        #     [5] -> [4] -> [3] -> None
        #       ^
        #       Current
    def traverse(self):
        current = self.head
        while current is not None:
            pass
            current = current.next
        return current

    def includes(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            else:
                current = current.next
        return False


class Node:
    def __init__(self, value, next=None):
        # initialization here
        self.value = value
        self.next = next
    #     if self.head is not None:
    #       node.next = self.head
    #     self.head = node

    def some_method(self):
        # method body here
        pass

    def __repr__(self):
        return f'{self.value}, {self.next}'


class TargetError:
    pass


if __name__ == '__main__':

    ll = LinkedList()
    print(ll)
    node = Node(10, None)
    print(node.value)
    ll.insert("banana")
    print(node.value)
    ll.insert("apple")
    print(ll.head.value)
    print(ll.__repr__())
# node2 = Node(5, node)
# ll.head = node2
