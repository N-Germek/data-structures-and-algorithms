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
Time:
Space:

My approach for my algorithm was identify the character of the string and then input that index into a stack list, pop it off to skip if not on stack list. For my next itteration, I am looking at the items in the stack list and comparing if the values are opposite of eachother.  If the comparison is true, return True, if the comparison is false, raise exception with message for corresponding missing bracket.

## Solution
<!-- Show how to run your code, and examples of it in action -->
