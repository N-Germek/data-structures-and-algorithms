# Trees

Binary Trees are a data structure in which the nodes do not have a specific organization to them. There is a limit of
two children nodes to each node, however additional nodes can be added wherever needed in them.

Binary Search Tree are a data structure in which there is an organized method to the nodes in the tree.  Specifically
the larger nodes are on the right of the root and the smaller nodes are on the left.

K-ary Trees are able to have more than two children and with the maximum amount of children being k. The traversal
method needed to be used is breadth first since we can potentially have any number of children nodes under parent nodes.

## Challenge

Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

Create a Binary Tree class
Define a method for each of the depth first traversals:
- pre order
- in order
- post order
Each depth first traversal method should return an array of values, ordered appropriately.

Create a Binary Search Tree class
This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional
methods:
- Add
Arguments: value
Return: nothing
Adds a new node with that value in the correct location in the binary search tree.

- Contains
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency

Version 1.0 - Nov 19, 2022, implemented pre-order method in binary tree class.
Version 2.0 - Nov 21, 2022, implemented in-order and post-order methods in binary tree class.
Version 3.0 - Nov 22, 2022, finalized implementation of binary search tree methods add() and contains() then updated
README's.

[Binary Tree Methods](/data_structures/binary_tree.py)
[Binary Search Tree Methods](/data_structures/binary_search_tree.py)

BigO for the Binary tree in time is O(n) when inserting a new node since you may need to traverse through the entire
tree to identify the next available location to create a node. BigO for space is O(w) for the need to traverse the width
of the entire tree from right to left one level at a time. Any nodes added would have to take into account the rule of
two children per root node.

BigO for the Binary Search Tree in time is O(h). With a depth first approach of searching for data that matches the
search parameters, the worst case would be to traverse the entire height of one side of the tree to locate that
information. BigO for space is O(1) since we are searching through the existing data structures for the matching data
versus creating new data structures within.

## Methods

### Binary Tree Methods

pre_order(self): This method will search the binary tree in the order of the root, then left node, then right node. It
will return the value of the node searched.

in_order(self): This method will search the binary tree in the order of the left node, then root, then right node. It
will return the value of the node searched.

post_order(self): This method will search the binary tree in the order of the left node, then right node, then root. It
will return the value of the node searched.

### Binary Search Tree Methods

add(self, value): This method will add a node after searching for the location to add it in the tree.

contains(self, value): This method will search the nodes and return a boolean if the value searching for exists in the tree.
