# Challenge Summary

Write a function called validate brackets
Arguments: string
Return: boolean
representing whether or not the brackets in the string are balanced
There are 3 types of brackets:

Round Brackets : ()
Square Brackets : []
Curly Brackets : {}

## Whiteboard Process
[Stack Queue Bracket Whiteboard](/docs/stack_queue_brackets/stack_queue_brackets.png)
[Stack Queue Bracket Function](/code_challenges/stack_queue_brackets.py)

## Approach & Efficiency
BigO:
Time: O(n)
Space: O(n)

## Solution

My approach to this problem domain was to identify the character of the string.
For each character in the string, if the character was the same as one of the brackets in my bracket list, add it to a temporary storage list until no more string characters exist.
In the same order that the brackets were being added to that array, if the order was the same then I would remove them from my storage list (This is where I visualize a palindrome.)
Once the storage list was at zero, I could tell that it was a successful palindrome of brackets and I returned a boolean True.
If the brackets did not create a palindrome, then it would return a boolean False.
