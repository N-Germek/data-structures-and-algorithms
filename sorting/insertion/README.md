# Blog Notes: Insertion Sort

The problem domain we have here today is to write a blog article with visuals that takes you through a step by step
walk-through of what Insertion Sort does in an algorithm.

## Whiteboard Process

Our pseudocode for this process is as follows:
```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```

We will be utilizing this sample array for demonstration:

```
[8,4,23,42,16,15]
```

Now let's get into the steps. Our first step will be to assign the value of i for our for loop.  This will cause the
pointer to loop through the array to determine the length of the array.

On our first pass it will look like this:

```
 i = 0,  length = 6 indexes
[8,    4,   23,   42,   16,   15]
 ^     ^     ^     ^     ^     ^
 0 --> 1 --> 2 --> 3 --> 4 --> 5 --> None
```

Second step is to assign a variable to our second loop.  This will be the way in which we will pinpoint the rest of the
list to compare the selected integer to for sorting purposes.

```
 j = 0,  length = 6 indexes
[8,    4,   23,   42,   16,   15]
 ^     ^     ^     ^     ^     ^
 0 --> 1 --> 2 --> 3 --> 4 --> 5 --> None
```

Now we will assign a variable for our integer that we will be comparing the rest to.

```
 0 --> 1 --> 2 --> 3 --> 4 --> 5
[8,    4,   23,   42,   16,   15]
 ^
temp = 8
```

## Approach & Efficiency
Version 1 *Created the initial code challenge and started with the blog post* 29 December 2022
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

## Solution
<!-- Show how to run your code, and examples of it in action -->

## References

[Insertion Sort](https://canvas.instructure.com/courses/5298434/assignments/32434068?return_to=https%3A%2F%2Fcanvas.instructure.com%2Fcalendar%23view_name%3Dmonth%26view_start%3D2022-12-29)
