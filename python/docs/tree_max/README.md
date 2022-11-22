# Challenge Summary
Create the following two methods for the Binary tree class:

find_maximum_value() which takes in no arguments and returns the maximum value number of the tree it is called on.  The values can be assumed that they are numeric, yet code should be written to cover what to do if a string is passed.

## Whiteboard Process
[Tree Max Whiteboard Documentation](/docs/tree_max/tree_max.png)

## Approach & Efficiency
This is a O(n) approach.

## Solution
Version 1.0 Nov 21, 2023 - implemented whiteboard and algorithm to tree-max code challenge
I created a temporary element to store the value. Using the post-order() traversal method, I reviewed the node values from left to right. Using a boolean, if the node value is higher than the temporary value, I reassigned the temporary value to the higher value. Finally, I returned the highest node value after traversing the entire tree.

