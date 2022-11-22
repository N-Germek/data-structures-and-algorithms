from data_structures.invalid_operation_error import InvalidOperationError


class BinaryTree:
    """
    ALGORITHM preOrder(root)

  OUTPUT <-- root.value

  if root.left is not None
      preOrder(root.left)

  if root.right is not None
      preOrder(root.right)

     ALGORITHM inOrder(root)
    INPUT <-- root node
    OUTPUT <-- in-order output of tree node's values

    if root.left is not None
        inOrder(root.left)

    OUTPUT <-- root.value

    if root.right is not None
        inOrder(root.right)

     ALGORITHM postOrder(root)
    INPUT <-- root node
    OUTPUT <-- post-order output of tree node's values

    if root.left is not None
        postOrder(root.left)

    if root.right is not None
        postOrder(root.right)

    OUTPUT <-- root.value
    """

    def __init__(self, root=None):
        self.root = root

    def some_method(self):
        # method body here
        pass

    # def pre_order(self):

    # pre_order_traversal = []
    #     if self.root is not None:
    #         return None
    #
    #     def traversal_pre_order(root):
    #         pre_order_traversal.append(root.value)
    #         if root.left is not None:
    #             traversal_pre_order(root.left)
    #         if root.right is not None:
    #             traversal_pre_order(root.right)
    #         traversal_pre_order(self.root)
    #         return pre_order_traversal

    def pre_order(self, values=[]):

        def walk(input_node, value_list):
            if not input_node:
                return
            value_list.append(input_node.value)
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)
        walk(self.root, values)
        return values

    def in_order(self, values=[]):
        def new_walk(input_node2, value_list2):
            if input_node2.left:
                new_walk(input_node2.left, value_list2)
            value_list2.append(input_node2.value)
            if input_node2.right:
                new_walk(input_node2.right, value_list2)

        new_walk(self.root, values)
        return values

    def post_order(self, values=[]):
        def another_walk(input_node3, value_list3):
            if input_node3.left:
                another_walk(input_node3.left, value_list3)
            if input_node3.right:
                another_walk(input_node3.right, value_list3)
            value_list3.append(input_node3.value)
        another_walk(self.root, values)
        return values

    def find_maximum_value(self, values=[]):
        max_val = 0
        current = self.root

        def walking(current_val, value_list4):
            if current is not None:
                if current_val.left:
                    walking(current_val.left, value_list4)
                if current_val.right:
                    walking(current_val.right, value_list4)
        if self.root is None:
            return max_val
        if self.root == "":
            raise InvalidOperationError(Exception("Method not allowed on string."))
        while current.value > max_val:
            max_val += current.value
            walking(self.root, values)
        return max_val


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


if __name__ == '__main__':
    #                       4
    #                     /   \
    #                   7      18
    #                 /   \   /   \
    #                3     1 5     11
    # expected   [4, 7, 3, 1, 18, 5, 11]
    bt = BinaryTree()
    node3 = Node(3)
    node1 = Node(1)
    node7 = Node(7, node3, node1)
    node5 = Node(5)
    node11 = Node(11)
    node18 = Node(18, node5, node11)
    node4 = Node(4, node7, node18)
    bt.root = node4
    print(bt.pre_order())
