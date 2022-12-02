from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree


def fizz_buzz_tree(tree):
    tree = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10],
        [11],
        [12],
        [13],
        [14, 15]
        ]
    new_tree = []
    root = KaryTree.root
    k = 3
    node = KaryTree.root.value
    k.value = node.value
    if new_tree is None:
        if tree.root.value is not None:
            KaryTree.breadth_first(tree)
            if node.value([1]/3 == 1) and node.value([1]/5 == 1):
                node.value = "FizzBuzz"
            if node.value([1]/3 ==1) and node.value([1]/5 != 1):
                node.value = "Fizz"
            if node.value([1]/5 ==1) and node.value([1]/3 != 1):
                node.value = "Buzz"
            else:
                node.value([1]/3 != 1) and node.value([1]/5 != 1)
                node.value = str(node.value)
            new_tree.append(node.value)
        return new_tree
