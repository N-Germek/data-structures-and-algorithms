# Graphs

Utilization is of an adjacency list for the assumed graph entries.

## Challenge

Graph implementation with Graph class, Vertex class and Edge class. The methods needed are:
add_node(), add_edge(), get_nodes(), get_neighbors(), get_size().

## Approach & Efficiency

[Whiteboard for Visual aid of Implementation](/docs/graph/graphs.png)
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

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
