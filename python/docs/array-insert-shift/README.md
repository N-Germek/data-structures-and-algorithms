# Insert and Shift a List

Write a function called insertShiftList which takes in a list and a value to be added. Without utilizing any of the built-in methods available to your language, return a list with the new value added at the middle index.

## Whiteboard Process

[Array Insert Shift](array_insert_shift.jpeg)

## Approach & Efficiency

Big O:
Time: O(n)
Space: O(n)

Authors: Natalija Germek Clarke(Navigator), Alejandro Rivera(Navigator) and Andy Nguyen (Driver/Navigator)

We created an insert_shift_list function that creates an empty list variable to assign the values of our input list. After the list values are assigned, our function creates a length counter that iterates through the values of the input list and adds a new index per value.  This is to identify the final list index length which was assigned to a variable called results_list_length.  Using if/else statements, we iterated through the length of the input list and identified the index locations. Based on the results of odd or even list length, we shifted the indexes so the value being added would be in the center most index location.  We called our function to solve our problem domain while not utilizing built in python methods.
