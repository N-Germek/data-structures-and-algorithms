from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):

    def add(self, value_input):

        new_value = Node(value_input)

        if self.root is None:
            self.root = new_value
            return new_value
        current = self.root

        while current is not None:
            if current.value > value_input:
                if current.left is None:
                    current.left = new_value
                    return
                else:
                    current = current.left

            if current.value < value_input:
                if current.right is None:
                    current.right = new_value
                    return
                else:
                    current = current.right

                if current.value == value_input:
                    return "Value already exists in the tree"

    def contains(self, values):
        current = self.root
        while current is not None:
            if current.value > values:
                current = current.left
            if current.value < values:
                current = current.right
            if current.value == values:
                return True
            else:
                return False

    def some_method(self):
        # method body here
        pass
