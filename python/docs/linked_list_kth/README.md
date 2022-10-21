# Challenge Summary

Write the following method for the Linked List class:

kth from end
argument: a number, k, as a parameter.
Return the node’s value that is k places from the tail of the linked list.
You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Authors:

Whiteboard: Natalija Germek, Daniel Brott, Andy Nguyen
Method implementation in code: Natalija Germek

## Whiteboard Process
[Linked List kth Whiteboard](linked_list_kth.jpg)
[Link to Code](/data_structures/linked_list.py)

## Approach & Efficiency
Big O:
Time: O(n)
Space: O(1)

Our approach was to traverse through the linked list, count the nodes, subtract the kth number from the final node in the list and return the value of the kth node.

## Solution

We defined a function kth_from_end() with the arguments of self and k.
Created a variable called count and assigned the value to 0 to create pointer for identifying length of linked list.

```python
def kth_from_end(self, k):
    count = 0
    current = self.head
```

Initiated a while loop to traverse the linked list and count the number of nodes.

```python
while current:
    count += 1
    current = current.next
```

We set the conditional that if the number of the k variable is greater than the count, or less than zero, or equaled the count we would raise an exception. This would account for the kth number not being included in the list, not being negative and accounting for a parameter of 0.

```python
if k > count or k < 0 or k == count:
    raise Exception
```
We created a variable and assigned the value of the head to it. We completed a for loop through the range of the initial node value and the length of the list subtracting the value of k. Re-assigned the variable to the sum to move the pointer to the proper kth node.

```python
temp = self.head

for i in range(1, count - k):
    temp = temp.next
```

Finally, we returned the value of k.

```python
return temp.value
```
