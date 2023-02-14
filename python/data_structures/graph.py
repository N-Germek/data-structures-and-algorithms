class Graph:
    """
    Algorithm:
    create graph class passing dictionary
    create vertex class passing vertex value
    create edge class passing

    instantiate a graph by defining a list
    instantiate a node by declaring a value and adding attribute of next and previous
    instantiate a size by passing a node with value and adding attribute of edge and weight

    if graph list is empty,
    add node with value and assign size to 1 node
    return node with value

    check graph for two nodes,
    assign value of edge to 1
    point edge to node1 and node2

    check graph for nodes
    define list for node results
    if nodes exist,
    return nodes and values in node results list
    else return empty list

    check graph for nodes
    define neighbor list
    define weight of edge and set to zero
    define node to be checked (temp)
    if node to be checked has a next or a previous
    return neighbor list of node and value
    return edge weight
    else return empty list

    check graph for nodes
    define node counter
    if nodes in length of graph
    add node to counter
    return total nodes counted
    else return zero
    """

    def __init__(self):
        # initializing what graph looks like.
        self.collection_list = {}

    def add_node(self, value):
        # creating instance of vertex
        vertex = Vertex(value)
        self.collection_list[vertex] = []
        return vertex

    def add_edge(self, node1, node2, weight=1):
        if node1 in self.collection_list and node2 in self.collection_list:
            # instance to take in value and weight assigned to it
            # this will assign the value of the edge to start the link to node2
            edge2 = Edge(node2, weight)
            # creates instance of second node to append the edge to
            #  this will assign the value of the edge to end the link for node1
            self.collection_list[node1].append(edge2)
    #         {node1: [edge(which includes node2 and weight for link and weight)]}
        else:
            raise KeyError("no vertex to attach edge to")

    def get_nodes(self):
        if self.collection_list is not None:
            return self.collection_list
        else:
            return {}

    def get_neighbors(self, vertex1):
        return self.collection_list[vertex1]

    def size(self):
        # return the size of graph based on the length of collection nodes
        if self.collection_list is not None:
            return len(self.collection_list)
        return 0


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:

    def __init__(self, vertex, weight=1):
        self.weight = weight
        self.vertex = vertex


if __name__ == '__main__':
    graph_view = Graph()
    graph_view.add_node("spam")
    print(graph_view)
