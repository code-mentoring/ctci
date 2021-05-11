Trees and Graphs
----------------

The intro is pretty dense for this chapter.
Please see text (or web search) for some basics on the topics:
Trees (in general)
-> balanced, unbalanced
-> complete, full, perfect
Binary Trees
-> Traversals: in-order, pre-order, post-order
Binary Search
Binary Heaps
Tries 
Graphs (in general)
-> adjacency list
-> adjacency matrices
Graph Search: BFS, DFS

--

4.1 - Route Between Nodes: 
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

4.2 - Minimal Tree: 
Given a sorted (increasing order) array with unique integer elements, write an algorithm to create a binary search tree with minimal height.

4.3 - List of Depths: 
Given a binary tree, design an algorithm which creates a linked list of all the nodes 
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists)

--

4.4 - Check Balanced: 
Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.

4.5 - Validate BST: 
Implement a function to check if a binary tree is a binary search tree.

4.6 - Build Order: 
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
