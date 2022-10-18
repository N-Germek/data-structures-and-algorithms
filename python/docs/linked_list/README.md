# Singly Linked List

A linked list is a sequence of nodes that are connected to each other and reference the connecting node.
A singly linked list is when the individual nodes reference only one node (the next) in the list with no further information about any prior or future nodes in the list.

## Challenge

Problem Domain is to create a linked list with the below features.
Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
Create a Linked List class, include a HEAD property that instantiates an empty link list.
The linked list class should contain the following methods: insert, includes, and to string.
The insert method needs to apply the Arguments: value, Return: nothing, and add a new node with that value to the head of the list with an O(1) time performance.
The includes method needs to apply the arguments: value, return a Boolean that indicates that value's existence in the list.
The to string method needs to apply arguments: value and return a string representing all the values in the format of "{ a } -> { b } -> { c } -> None".

## Author

Natalija Germek with clarification assistance from Daniel Brott.

## Approach & Efficiency

Version 1.0
Version 1.2

Daniel Brott assisted in troubleshooting my __str__ method which was placed in my Node class in error versus in my Linked List class.

BigO
Time: O(n)
Space: O(n)

## API

Insert method appends a new node at the HEAD of the linked list it traverses through.
Includes method will return truthy or falsy based on the data being passed through the node.
My to string method aka __str__ method will return a string of a linked list with all the values in the format of "{ a } -> { b } -> { c } -> None".
