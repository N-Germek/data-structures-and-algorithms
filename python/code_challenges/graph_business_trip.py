from data_structures.graph import Graph


def direct_flights(graph, lst):
    edge_total = 0
    city = Graph.get_neighbors(lst)
    if graph is None:
        raise Exception("Graph is empty")
    elif lst.len() <= 1:
        raise Exception("Not enough cities for edge, or city list is empty.")
    for city in lst:
        if city.is_neighbor():
            edges = graph.add_edge(city[0], city[1])
            edges += edge_total
        return edge_total
    return None
