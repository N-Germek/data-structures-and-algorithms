# Challenge Summary
Create the following two methods for the Binary tree class:

find_maximum_value() which takes in no arguments and returns the maximum value number of the tree it is called on.
The values can be assumed that they are numeric, yet code should be written to cover what to do if a string is passed.

## Whiteboard Process
[Tree Max Whiteboard Documentation](/docs/tree_max/tree_max.png)
[Tree Max Method](/data_structures/binary_tree.py)

## Approach & Efficiency
This is a O(n) time and space approach to accommodate the for loop needed after recursion in identify the max value of
the node in the list created.

## Solution
Version 1.0 Nov 21, 2023 - implemented whiteboard and algorithm to tree-max code challenge
Version 2.0 Nov 22, 2023 - finalized tree_max method and updated README.

To begin, I assign the max value to None to account for negative integers. I called my post_order() method to traverse
my nodes and save the values to a list. Using a for loop, I checked if the value of each node is greater than the max
value, updated max value with that value. Finally, I returned the max value.

## Method

find_maximum_value(self): This method will locate the maximum value of the node in a Binary tree and return that value
as an integer. If the value input is a string, an exception will be raised for invalid data type.
