# 4.1 - Route Between Nodes: 
# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.
#
# This solution uses Adjacency Lists to represent the graph, where every node stores a list of adjacent 
# nodes (i.e. children). In a directed graph, an edge like 'A -> B' would be stored only in A's list of 
# adjacent nodes and B would not know about A. 
#
# Breadth-First Search (BFS) is used to find a path between two nodes (source and destination).
# BFS starts at a selected node and explores each direct child node before moving further
# on to their child nodes, i.e. go wide before going deep. If the destination node is found then a
# path must exist between the two nodes. 
#
# As BFS should not be recursive, the core of this BFS is a queue that orders nodes in terms of next to 
# be visited, and a while loop iterates over that queue to visit each node in turn. 
# If there are multiple paths toward a particular node, then it might be visited more than once, 
# however the following two alternatives were considered:
# 1. Add 'visited' flag attribute to Node object; would couple data structure to the algorithm. 
# 2. Store visited Nodes in separate data structure; would increase storage and algorithm complexity.

from graph import *
from queue import Queue

def enqueueAll(nodes, queue):
    for n in nodes:
        queue.put(n)

def is_path(source, destination):
    print(f"Searching for path between {source.data} and {destination.data}...")

    awaiting_visit = Queue() 
    awaiting_visit.put(source) # Enqueue.

    while (awaiting_visit.qsize() > 0): # Until all nodes have been visited.
        n = awaiting_visit.get() # Dequeue.
        if (n == destination):
            return True
        enqueueAll(n.children, awaiting_visit)

    return False

# Tests.
def evaluate(expect, actual):
    print({True: "Pass.", False: "FAIL!!!"} [expect==actual] +" -- "+ f"Expect {expect}, actual {actual}.")

def build_graph():
    graph = Graph()
    graph.nodes = [Node(0), Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7)]
    graph.nodes[0].children = [graph.nodes[1], graph.nodes[2]]
    graph.nodes[1].children = [graph.nodes[5], graph.nodes[3]]
    graph.nodes[2].children = [graph.nodes[4]]
    graph.nodes[3].children = [graph.nodes[2]]
    graph.nodes[4].children = []
    graph.nodes[5].children = [graph.nodes[6]]
    graph.nodes[6].children = []
    graph.nodes[7].children = [graph.nodes[5]]  
    return graph

graph = build_graph()

evaluate(True, is_path(graph.nodes[0], graph.nodes[6]))
evaluate(False, is_path(graph.nodes[2], graph.nodes[5]))
evaluate(False, is_path(graph.nodes[0], graph.nodes[7]))
evaluate(True, is_path(graph.nodes[7], graph.nodes[6]))
evaluate(False, is_path(graph.nodes[3], graph.nodes[5]))