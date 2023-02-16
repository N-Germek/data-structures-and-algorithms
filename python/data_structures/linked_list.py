class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
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
        # linked-list-zip
        current = self.head
        final_node = Node(value)
        if current is None:
            current = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = final_node

    def insert_before(self, value, new_value):
        current = self.head
        while current and current.next is not None:
            if current.next.value == value:
                # the order of values passed in the parameter determines the order of updating
                temp_value = Node(new_value, current.next)
                current.next = temp_value
                return temp_value
            current = current.next

    def reverse(self):
        current = self.head
        previous = None
        print(current.value)
        while current and current.next:
            next = current.next
            print(next.value)
            current.next = previous
            previous = current
            print(previous.value)
            current = next
            print(current.value)
        previous = self.head
        return previous

    def ll_add_one(self):
        carryover = True
        self.reverse()
        current = self.head
        while current:
            if current.value == 9 and current.next is not None:
                current.value = 0
                carryover = True
                current = current.next
            elif current.value < 9:
                current.value += 1
                carryover = False
                break
            if current.next is None:
                current.value = 0
                node = Node(1)
                current.next = None
            self.reverse()
            return


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class TargetError:
    pass


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(4)
    # print(ll)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    print(ll)
    ll.reverse(ll)
    print(ll)
