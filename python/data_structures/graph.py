class Graph:
    """
    Algorithm:
    create graph class passing dictionary
        instantiate a graph by defining a dictionary
    create vertex class passing vertex value
        instantiate a node by declaring a value and adding the vertex to the dictionary
    create edge class passing vertex and weight
        instantiate a vertex with value and instantiate edge weight

    add_node():
    if graph list is empty,
    add vertex with value to graph
    return vertex with value

    add_edge():
    check graph for two vertex,
    create instance of edge assignment to vertex and assign weight
    create instance of second vertex to append to other side of edge

    get_nodes():
    check graph for vertex
    if graph has vertex
    return dictionary with all vertex in graph
    else return empty list

    get_neighbors():
    return neighbor list of vertex edges if in graph
    else return empty list

    size():
    check graph for vertex
    if vertex in length of graph
    return total nodes counted in the list
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

    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 in self.collection_list and vertex2 in self.collection_list:
            # instance to take in value and weight assigned to it
            # this will assign the value of the edge to start the link to node2
            edge2 = Edge(vertex2, weight)
            # creates instance of second node to append the edge to
            #  this will assign the value of the edge to end the link for node1
            self.collection_list[vertex1].append(edge2)
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
