# Blog Notes: Merge Sort

The problem domain we have here today is to write a blog article with visuals that takes you through a step by step
walk-through of what Merge Sort does in an algorithm.

## Whiteboard Process

Our pseudocode for this process is as follows:
```
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left

```

We will be utilizing this sample array for demonstration:

```
[8,4,23,42,16,15]
```

Now let's get into the steps. Our first step will be to declare the variable of n to the value of our integer we are sorting.
If the value of n is greater than 1 we will declare the middle, left side and right side of our list.
The middle is declared as the point in the list of n/2. Any number above 0 and below half the value of the list will be
placed on the left and any integer above the midway point to the end of the list will go on the right.

Based on the value of n we will be traversing the length of the list and sorting as we go. This will cause the pointer to loop through the array to determine the length of the array.

On our first pass it will look like this:

```
[8,    4,   23,   42,   16,   15]
```

```
[8,    4,   23,   42,   16,   15]
```

```
[8,    4,   23,   42,   16,   15]
```

## Approach & Efficiency
Version 1 *Created the initial code challenge and started with the blog post* 29 December 2022
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
<!-- Show how to run your code, and examples of it in action -->

## References

[Merge Sort](https://canvas.instructure.com/courses/5298434/assignments/32434069?return_to=https%3A%2F%2Fcanvas.instructure.com%2Fcalendar%23view_name%3Dmonth%26view_start%3D2022-12-29)
