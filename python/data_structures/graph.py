class Graph:
    """
    Algorithm:
    create graph class
    create node class
    create size class

    instantiate a graph by defining a list with attribute of size and node with value
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
        # self.size = size
        # initializing what graph looks like.
        self.collection_list = {}

    def add_node(self, value):
        vertex = Vertex(value)
        self.collection_list[vertex] = []
        return vertex

    def add_edge(self, node1, node2, weight=0):
        if node1 in self.collection_list and node2 in self.collection_list:
            # this will assign the value of the edge to start the link to node2
            edge1 = Edge(node1, node2, weight)
            #  this will assign the value of the edge to end the link for node1
            self.collection_list[node1].append(edge1)
    #         {node1: [edge(which includes node2 and weight for link and weight)]}

    def get_nodes(self):
        if self.collection_list is not None:
            return self.collection_list
        else:
            return {}

    def get_neighbors(self, vertex1):
        pass
        # look for solution in 6 lines of code or less:
        # edge_collection = {}
        # neighbor = vertex1.neighbor
        # if vertex1 is not None:
        #     return edge_collection
        # elif Edge(vertex1, vertex1.neighbor) != 0:
        #     edge_collection[vertex1].append(neighbor)
        #
        #     vertex1.neighbor
        # neighbor_node = self.get_neighbors(vertex1)
        # edge = Edge(vertex1, neighbor_node)
        #
        # while edge in self.collection_list:
        #     edge_collection[vertex1].append(edge, weight)
        #     return edge_collection

    def get_size(self):
        if self.collection_list is not None:
            return len(self.collection_list)
        else:
            return 0
        # total_vertex = 0
        # current = self.head
        # while current is not None:
        #     total_vertex += 1
        #     return total_vertex
        # return 0


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:

    def __init__(self, start, end, weight=0):
        self.weight = weight
        self.start = start
        self.end = end


if __name__ == '__main__':
    graph_view = Graph()
    graph_view.add_node("spam")
    print(graph_view)
