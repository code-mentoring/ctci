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

4.6/4.7(depending on version) - Build Order: 
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

--

4.8 First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.

4.9 BST Sequences: A binary search tree was created by traversing through an array from left to right
and inserting each element. Given a binary search tree with distinct elements, print all possible
arrays that could have led to this tree.

---

4.10 Check Subtree: T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl .
A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2,
That is, if you cut off the tree at node n, the two trees would be identical.


4.11
Random Node: You are implementing a binary tree class from scratch which, in addition to
insert, find, and delete, has a method getRandomNode() which returns a random node
from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm
for getRandomNode, and explain how you would implement the rest of the methods.
