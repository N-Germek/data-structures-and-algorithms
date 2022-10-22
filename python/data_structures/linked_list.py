class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        # print(ll)
        return_string = ''
        current = self.head

        while current:
            return_string += f'{{ {current.value} }} -> '
            current = current.next
            print(return_string)
        return return_string + "None"

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
        while current.next is not None:
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

    def append(self, value):
        final_node = Node(value)
        current = self.traverse()
        current.next = final_node

    def insert_before(self, value, new_value):
        prior_node = Node(value)
        current = self.traverse()
        current.next = prior_node



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

    ll = LinkedList([1, 3, 5, 6])
    # print(ll)
    ll.append(4)
    print(ll)
    # node = Node("a")
#     node2 = Node("b")
#     node3 = Node("c")
#     node = Node(10, None)
#     print(node.value)
#     ll.insert("banana")
#     print(node.value)
#     ll.insert("apple")
#     print(ll.head.value)
#     print(ll.__str__())
#     print(ll)
# node2 = Node(5, node)
# ll.head = node2
