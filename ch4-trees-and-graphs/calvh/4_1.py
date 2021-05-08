def path_exists_between_vertices(g, v1, v2):
    """
    Problem:
    Given a directed graph, design an algorithm to find out whether there is a route between two vertices.

    Strategy:
    Perform a directed BFS starting v1. If v2 is found, return True. Else, repeat the BFS from v2 to find v1. If v1 is not found, return False.

    """

    def bfs(start, target):

        l = deque()
        l.append(start)

        while len(l) > 0:

            v = l.popleft()

            for edge in g.outgoing_edges(v):

                if g.get_edge_field(edge[0], edge[1], "explored") is False:

                    w = edge[1]  # opposite vertex

                    if g.get_vertex_field(w, "explored") is False:
                        if w == target:
                            return True

                        g.set_vertex_field(w, explored=True)
                        l.append(w)

        return False

    if bfs(v1, v2) is True:
        return True
    else:
        return bfs(v2, v1)