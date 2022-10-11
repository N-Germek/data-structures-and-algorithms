# Binary Search of Sorted Array
Write a function called BinarySearch which takes in 2 parameters: a sorted list and the search key. Without utilizing any of the built-in methods available to your language, return the index of the lists’ element that is equal to the value of the search key, or -1 if the element is not in the list.
NOTE: The search algorithm used in your function should be a binary search.

## Whiteboard Process
[Array Binary Search](array_binary_search.png)

## Approach & Efficiency

BigO:

Time: log(n) The time needed is based on how long it takes to loop through the list.
Space: O(1) Since the algorithm is not changing the variables in the list, it is reassigning existing ones and the list is getting shorter to loop through for the search.
