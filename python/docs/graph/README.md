# Graphs

Utilization is of an adjacency list for the assumed graph entries.

## Challenge

Graph implementation with Graph class, Vertex class and Edge class. The methods needed are:
add_node(), add_edge(), get_nodes(), get_neighbors(), get_size().

## Approach & Efficiency

*Version 1.0* Create initial code, complete whiteboard and methods, troubleshoot method error. - 30 January 2023
*Version 2.0* Create README.md, attach whiteboard, refactor first two methods and start two more methods. - 31 January 2023
*Version 3.0* Complete README.md, refactoring graph code challenge. - 13 February 2023
*Version 4.0* Completed refactoring and algorithm in graph implementation, final update to README.md. - 14 February 2023

[Whiteboard for Visual aid of Implementation](/docs/graph/graphs.png)

For BigO time and space for Adjacency List Graph is O(n<sup>2</sup>) in the case of a complete graph.

## API

add_node(): which takes in a value argument, adds the node to the graph and returns the node in the graph.

add_edge(): which takes in two nodes connected by an edge. The edge is assigned a weight if applicable. Also, both nodes
should be in the graph.

get_nodes(): which returns all nodes in the graph as a collection, yet if no nodes exist in the graph, the return
will be an empty collection.

get_neighbors(): which takes in the argument of a node, and returns a collection of edges to that given node. If a
weight is assigned to that edge, return the weight. If there are no nodes in the collection, it will return an empty
collection.

get_size(): which returns the total number of nodes in the graph or 0 if none exist.
