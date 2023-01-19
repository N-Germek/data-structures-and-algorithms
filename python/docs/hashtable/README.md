# Hashtables

Hash tables are data structures that utilize key value pairs in the forms of a node or bucket. The structure is
primarily used for storage. The hash will change the key into an integer index and store the value at that specific
index. With the hash, multiple keys can be stored into the same index. This is known as a collision.

## Challenge

Our problem domain is to implement a Hashtable class with the following methods: set(), get(), has(), keys(), hash().
Utilizing the single responsibility principal, testing should pass for each of the methods.

## Approach & Efficiency

Andy and Roger assisted me in the walk-through so I could properly implement the code.

BigO space will be O(1) due to the need to implement an array of lists and time will also be O(1) due to the risk of
collisions and need to update the value.

*Version 1.0* Initial creation of Hashtable class and initiation of methods. Updated README.md and link in root
README.md - 14 January 2023

*Version 2.0* Completed Hashtable Implementation and updated README.md. - 18 January 2023

## API

[Hashtable Code Implementation](/data_structures/hashtable.py)

set() - Should take in the arguments of a key and value, return nothing, should include hashing of the key setting the
key value pair into the table, and handle collisions as needed.

get() - Should take in the argument of a key and return the value associated with that key from the table.

has() - Should take in the argument of a key and return a boolean of weather that key is or is not in the table.

keys() - Should return a list or collection of the keys that exist in the table.

hash() - Should take in the argument of the key and return the index of the collection of that key.
