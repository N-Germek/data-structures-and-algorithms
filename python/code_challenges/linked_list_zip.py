from data_structures.linked_list import LinkedList, Node


def zip_lists(ll1, ll2):
    list_a_current = LinkedList.insert(ll1.head)
    list_b_current = LinkedList.insert(ll2.head)
    temp_list1 = list_a_current.next
    temp_list2 = list_b_current.next
    lists_zipped = LinkedList()
    lists_zipped.head = None

    while temp_list1 and temp_list2 is not None:
        list_a_current.next = list_b_current
        list_b_current.next = temp_list1
        list_a_current = temp_list1
        temp_list1 = temp_list1.next
        list_b_current = temp_list2
        temp_list2 = temp_list2.next
        if temp_list1.next is None:
            temp_list1.next = temp_list2.next
        elif temp_list2.next is None:
            temp_list2.next = temp_list1.next
        temp_list1 = lists_zipped
    return lists_zipped
