from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):

    def __init__(self, root=None):
        self.root = root

    def add(self, values):
        new_value = Node(values)

        if self.root is None:
            self.root = new_value
            current = self.root
            if values is not None or type(values) == str:
                return "Node must be equal to interger"

            while current is not None:
                if current.values > values:
                    if current.left is None:
                        current.left = new_value
                    else:
                        current = current.left

                elif current.values < values:
                    if current.right is None:
                        current.right = new_value
                    else:
                        current = current.right

                if current.values == values:
                    return "Value already exists in the tree"

    def contains(self, values):
        current = self.root
        while current is not None:
            if current.values > values:
                current = current.left
            if current.values < values:
                current = current.right
            if current.values == values:
                return True
            else:
                return False

    def some_method(self):
        # method body here
        pass
