# Linked List Insertions

A linked list is a sequence of nodes that are connected to each other and reference the connecting node.
A singly linked list is when the individual nodes reference only one node (the next) in the list with no further information about any prior or future nodes in the list.
This is the implementation of writing the following methods: append, insert before, and insert after methods.

## Challenge

Problem Domain is to create a linked list with the below features.
Create a team whiteboard to satisfy problem domain and include in docs directory.
Create an append method with the argument of a new value and adds a node with the given value at the end of the linked list.
Create an insert before method that takes in the arguments index value and new value.  This node with the given value will be added to the linked list immediately before the first node that has the value specified.
Create an insert after method that takes in the arguments index value and new value.  This node with the given value will be added to the linked list immediately after the first node that has the value specified.
All methods must be written using TDD and must pass unit tests provided in testing file.

## Author

Whiteboard Team: Natalija Germek, Daniel Brott, Alejandro Rivera
Code Challenge author: Natalija Germek.

## Approach & Efficiency

Version 1.0
Version 1.2
Version 1.3

BigO
Time: O(n)
Space: O(n)

## API

[Whiteboard](linked_list_insertions.png)

Append method appends a new node as the new HEAD of the linked list it traverses through.
Insert before method will return a linked list with a new node with a given value before the first node in the linked list.
Insert after method will return a linked list with a new node with a given value after the first node in the linked list.
