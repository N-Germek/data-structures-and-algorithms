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

    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def add_node(self, value):
        vertex = Vertex(value)
        collection_list = []
        if self.head is None:
            self.head = vertex
            collection_list.append(vertex)
        elif self.head is not None:
            vertex.next = self.head
            self.head = vertex
        return

    def add_edge(self, node_value, another_node_value):
        node = Vertex(node_value)
        node.next = Vertex(another_node_value)
        edge = 0
        if node_value in graph_view and another_node_value in graph_view:
            edge += 1

    def get_node(self):
        collection_returned = []
        current = self.head
        while current is not None:
            collection_returned.append(self.head)
            # vertex.next = self.head
            # self.head = vertex.next

    def get_neighbors(self):
        pass

    def get_size(self):
        total_vertex = 0
        current = self.head
        while current is not None:
            total_vertex += 1
            return total_vertex
        return 0

    def some_method(self):
        # method body here
        pass


class Vertex:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Edge:

    def __init__(self, size=0):
        self.size = size


if __name__ == '__main__':
    graph_view = Graph()
    graph_view.add_node("spam")
    print(graph_view)
