class BinaryTree:
    """
    ALGORITHM preOrder(root)

  OUTPUT <-- root.value

  if root.left is not None
      preOrder(root.left)

  if root.right is not None
      preOrder(root.right)

      ALGORITHM inOrder(root)
    // INPUT <-- root node
    // OUTPUT <-- in-order output of tree node's values

    if root.left is not None
        inOrder(root.left)

    OUTPUT <-- root.value

    if root.right is not None
        inOrder(root.right)
    """

    def __init__(self, root=None):
        self.root = root

    def some_method(self):
        # method body here
        pass

    def pre_order(self, values=[]):

        def walk(input_node, value_list):
            if not input_node:
                return
            value_list.append(input_node.value)
            walk(input_node.left, value_list)
            walk(input_node.right, value_list)
        walk(self.root, values)
        return values

    # left, root, right
    def in_order(self, values=[]):
        def new_walk(input_node2, value_list2):
            # new_root = self.root.value
            if not input_node2.left:
                return
            new_walk(input_node2.left, value_list2)
            value_list2.append(input_node2.left.value)
            value_list2.append(input_node2.value)
            value_list2.append(input_node2.right.value)
            new_walk(input_node2.right, value_list2)

            #
        new_walk(self.root, values)
        return values


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
