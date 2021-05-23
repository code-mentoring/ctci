def list_of_nodes_by_depth(tree):

    """
    Problem:
    Given a binary tree, design an algorithm which creates a linked list of all the nodes
    at each depth (e.g., if you have a tree with depth D, you'll have D linked lists)

    Solution:
    Do a BFS search from the root, which will yield the nodes in level-order
    """

    if tree.is_empty():
        return []

    l = []

    # l is a list of lists indexed by depth
    l.append([tree.root])

    depth = 0

    while True:

        node_list = []

        for node in l[depth]:
            if node.left is not None:
                node_list.append(node.left)

            if node.right is not None:
                node_list.append(node.right)

        if len(node_list) == 0:
            # no new external nodes, traversal complete
            return l

        l.append(node_list)
        depth += 1

    return l