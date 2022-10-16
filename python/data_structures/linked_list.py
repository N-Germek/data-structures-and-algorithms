class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        #     inserted the second node into the head position
        if self.head is not None:
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


# if self.value == self.ll[]:
#     return True


# while the nodes value not in list, return False else return True
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


class TargetError:
    pass


if __name__ == '__main__':

    ll = LinkedList
    print(ll)
    node = Node(10, None)
    print(node.value)
    node.value = 11
    print(node.value)
    ll.head = node
    print(ll.head.value)
    linked_list = ll
    print(linked_list.value)
# node2 = Node(5, node)
# ll.head = node2
