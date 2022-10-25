# Challenge Summary

Write a function called zip lists that takes in two arguments of linked lists and returns a new linked list zipped as alternating values between the initial lists passed into it. Additional space should be kept at O(1) if at all possible. The Node class and all properties on the LInked List class including prior methods are accessible.

## Whiteboard Process

[Linked List Zip Whiteboard](linked_list_zip.jpg)

## Author

Whiteboard Team: Natalija Germek, Daniel Brott, Andy Nguyen
Code Challenge author: Natalija Germek.

## Approach & Efficiency

BigO
Time: O(n)
Space: O(1)

The approach decided was to take the separate linked lists and assign the values of the head for them individually. Two variables were then assigned the value of the two linked list's head's next nodes. The final variables created were assigned to an empty linked list to hold the newly created linked list and the variable needed to start the head of that linked list. While traversing both the initial linked lists, the values of their next are then added into the new linked list in alternating order. An if statement is created to end the while loop and account for one list being longer then the other. This final list is returned with alternating values. Since each list needs only be iterated through as many times as there are values it is O(n) and since one list is being returned the space needed is O(1).

## Solution

<!-- Show how to run your code, and examples of it in action -->
