# Challenge Summary
Write a function called breadth first that takes in the argument of a tree and returns the values in the tree in the
order they were encountered. Expected traversal approach is Breadth-first.

## Whiteboard Process
[Tree Breadth First Function Whiteboard](/docs/tree_breadth_first/tree_breadth_first.png)
[Tree Breadth First Function](/code_challenges/tree_breadth_first.py)

## Approach & Efficiency

My approach was to assign a variable to an empty list. Using a queue, I am traversing the nodes in the tree and
appending the values to the list. If the list is empty, it returns an empty list value. If there are nodes in the
tree, the values of those nodes will be returned in the form of a list starting with traversing the nodes from right to
left. My BigO for this is time: O(n) because the traversal will only go through at the rate of the nodes in the tree.
The BigO for space will be O(n) because the only data structure added is the list in which the values of the tree are
removed and added to that list.

## Solution
<!-- Show how to run your code, and examples of it in action -->

