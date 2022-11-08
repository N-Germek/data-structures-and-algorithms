# Stacks and Queues

Stack is the FILO data structure which passes the properties for the top to begin the stack and a next to traverse to the next node.
Queue is the FIFO data structure which passes a property of front to begin the queue.

## Challenge

Implement already created methods:

Create a new class called PseudoQueue.
Without using an existing queue, use a standard queue interface, two list method, and internally, utilize two stack instances to create and manage the PseudoQueue.

Methods:
enqueque(self, value) which takes in a value using a first in, first our approach.
dequeue(self, value) which extracts a value from the queue using a first in, first out approach.

Input: Queue
Output: Two stacked lists

## Approach & Efficiency

Version 1.0 8-Nov-2022 "Initial creation of whiteboard and README updates

## Methods

Stack Methods

push() which will take in a value, and add a new node to the top of the stack.
pop() which will pass no arguments, return the value from the node on the top of the stack, remove the node from the top of the stack.

Queue methods

enqueue() which will take in a value, add a new node with the value to the back of the queue with a O(1) time performance.
dequeue() which will take in no arguments, return the value from the node in the front of the queue, remove the node from the front of the queue and wil raise an exception if it is called on an empty queue.

## Link

[Code Challenge 11](/code_challenges/stack_queue_pseudo.py)
