from data_structures.binary_tree import BinaryTree
from data_structures.hashtable import Hashtable

'''
Define a function passing two binary trees
    traverse through first tree
        if tree is empty
            raise exception
        else
            hash all values of tree one
            save to hashtable
    traverse through second tree
        if tree is empty
            raise exception
        else
            hash all values of tree two
            save to hashtable
    if a collision is determined
        place that data into a new data structure
    check hashed values from both trees
        if any values match
        return matched values.
'''


def tree_intersection(binary_tree_1, binary_tree_2):
    matching_nodes = []
    hashtable = []
    collision_list = []
    while matching_nodes is None:
        BinaryTree.post_order(binary_tree_1)
        bt_1_indexes = Hashtable.hash(binary_tree_1)
        bt_1_hashed_keys = Hashtable.set(binary_tree_1[bt_1_indexes])
        print(bt_1_hashed_keys)

        BinaryTree.post_order(binary_tree_2)
        bt_2_indexes = binary_tree_2.Hashtable.hash(binary_tree_2)
        bt_2_hashed_keys = hashtable.append(Hashtable.set(bt_2_indexes))

        if bt_1_hashed_keys == bt_2_hashed_keys:
            collision_list.append([bt_1_hashed_keys])
            collision_list.append(bt_2_hashed_keys)
            return collision_list
        # for keys in collision_list:


if __name__ == '__main__':
    bt_1 = BinaryTree(10)
    bt_2 = BinaryTree(7)

