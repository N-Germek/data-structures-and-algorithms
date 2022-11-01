# Stacks and Queues

Stack is the FILO data structure which passes the properties for the top to begin the stack and a next to traverse to the next node.
Queue is the FIFO data structure which passes a property of front to begin the queue.

## Challenge

Implement new methods in stack and queue structures, test the new methods and determine the BigO for each structure.

Create the following methods for the stack data structure:

push()
pop()
peek()
is_empty()

Create the following methods for the queue data structure:

enqueue()
dequeue()
peek()
is_empty()

## Approach & Efficiency

After the initial creation of my node, I create a whiteboard of all the elements needed to accomplish for each method. Additionally, I complete my README.md file to set up my files.
BigO for each method is as follows:

Stack:
push() is O(1).
pop() is O(1).
peek() is O(1).
is_empty() is O(1).

Queue:
enqueue() is O(1).
dequeue() is O(1).
peek() is O(1).
is_empty() is O(1).

## Methods

Stack Methods

push() which will take in a value, and add a new node to the top of the stack.
pop() which will pass no arguments, return the value from the node on the top of the stack, remove the node from the top of the stack, and will raise an exception when it calls on an empty stack.
peek() which passes no arguments, returns the value of the node at the top of the stack, and will raise an exception when called on an empty stack.
is_empty() which passes no arguments and returns a boolean indicating True or False on if the stack is empty or not.

Queue methods

enqueue() which will take in a value, add a new node with the value to the back of the queue with a O(1) time performance.
dequeue() which will take in no arguments, return the value from the node in the front of the queue, remove the node from the front of the queue and wil raise an exception if it is called on an empty queue.
peek() which will take in no arguments, return the value of the node located in the front of the queue and will raise an exception when it is called on an empty queue.
is_empty() which will take in no arguments and will return a boolean indicating True or False if the queue is empty or not.

<!-- Description of each method publicly available to your Stack and Queue-->
