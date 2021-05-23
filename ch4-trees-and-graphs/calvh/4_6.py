from collections import deque

def build_order(projects):

    """
    Problem:
    You are given a list of projects and a list of dependencies (which is a list of pairs of
    projects, where the second project is dependent on the first project). Ail of a project's dependencies
    must be built before the project is. Find a build order that will allow the projects to be built. If there
    is no valid build order, return an error.
    EXAMPLE
    Input:
    p r o j e c t s :
    a, b, c, d, e, f
    dependencies:
    (a, d), (f, b), (b, d), (f, a), (d, c)
    Output: F, e, a, b, d, c


    Solution:
    Construct a directed graph and do a topological sort.
    """

    g = Digraph(projects)

    stack = deque()
    order = []
    in_counter = {}

    for u in g.get_vertices():
        in_counter[u] = g.in_degree(u)
        if in_counter[u] == 0:
            stack.append(u)

    while len(stack) > 0:

        u = stack.pop()
        order.append(u)

        for e in g.outgoing_edges(u):

            w = g.opposite(u, e)
            in_counter[w] = in_counter[w] - 1

            if in_counter[w] == 0:
                stack.append(w)

    # Digraph has no directed cycles
    if len(order) == len(g.get_vertices()):
        return order

    # Digraph has a directed cycle
    return False


