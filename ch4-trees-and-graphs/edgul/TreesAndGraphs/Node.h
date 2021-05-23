#pragma once

#include <iostream>
#include <vector>
#include <assert.h>
#include <numeric>
#include <unordered_set>
#include <algorithm>
#include "Utils.h"

class Node
{
public:
    Node(int value) : value(value) {}
    Node(int value, std::vector<Node *> nodes) : value(value), nodes(nodes) {}
    int value;
    std::vector<Node *> nodes;

    void print(int depth = 0)
    {
        if (visited_)
        {
            std::cout << "CYCLE DETECTED (Not drawn)" << std::endl;
            return;
        }

        for (int i : range(0,depth)) { std::cout << "->"; }
        std::cout << value << std::endl;
        visited_ = true;
        for (Node *node : nodes)
        {
            node->print(depth+1);
        }
    }
private:
    bool visited_ = false;
};


// 4.1
bool routeBetween(Node *start, Node *end)
{
    //vprint("Looking for: ", end );
    //vprint("Checking: "   , start);
    if (start == end) return true;

    std::vector<Node *> explore = start->nodes;
    std::unordered_set<Node *> explored; // constant insert and lookup (average), linear insert/lookup for worstcase
    while (explore.size())
    {
        Node *node = explore.at(0);
        explore.erase(explore.begin());

        if (explored.find(node) == explored.end()) // don't double check a cycle or it's children
        {
            //vprint("Checking: ", node);
            if (node == end) return true;
            explore.insert(explore.end(), node->nodes.begin(), node->nodes.end());
        }
        explored.insert(node);
    }
    return false;
}

struct ProjDep 
{
    int project;
    int dependency;
    ProjDep(int proj, int dep) : project(proj), dependency(dep) {}
};

bool build_order_node(Node *node, 
                      std::vector<int> &bo, 
                      std::vector<Node *> &remaining,
                      std::vector<int> &chain)
{
    std::cout << "Attempting to find build order for node: " << node->value << std::endl;
    if (!node) 
    {
        std::cout << "Early return";
        return true;
    }

    bool succ = true;
    for (Node *child : node->nodes)
    {
        //std::cout << "Checking child: " << child->value << std::endl;
       auto childIt = std::find(chain.begin(), chain.end(), child->value);
       if (childIt != chain.end())
       {
           std::cout << "Loop detected" << std::endl;
           return false;
       }

       succ = build_order_node(child, bo, remaining, chain);
       if (!succ) 
       {
           //std::cout << "Recursion failed" << std::endl;
           return false;
       }
    }

    auto it = std::find(bo.begin(), bo.end(), node->value); 
    if (it == bo.end())
    {
        //std::cout << "Adding to build order: " << node->value << std::endl;
        bo.push_back(node->value);

        auto sameNode = [node](Node *n) { return node->value == n->value; };
        auto nodeIt = std::find(remaining.begin(), remaining.end(), node);
        if (nodeIt != remaining.end())
            remaining.erase(nodeIt);
    }
    return true;
}

// 4.6 - build order
// Assuming projects are "named" by int (where 0 is invalid name)
std::vector<int> build_order(std::vector<ProjDep> projDeps)
{
    std::cout << "--- Attempting to find build_order\n";
    std::vector<int> bo;
    std::vector<Node *> remaining;

    // prepare graph
    std::vector<Node *> graph;
    for (ProjDep projDep : projDeps)
    {
        //std::cout << "ProjDep: " << projDep.project << " " << projDep.dependency << std::endl;
        if (projDep.project == 0) continue; // don't do anything for invalid proj name

        Node *proj = nullptr;
        Node *dep = nullptr;
        
        // creates new node for dep if necessary
        if (projDep.dependency != 0)
        {
            // creates a new node for dep if necessary
            auto sameNodeValue = [projDep](Node *n) {
                return n->value == projDep.dependency;
            };
            auto depIt = std::find_if(graph.begin(), graph.end(), sameNodeValue);
            if (depIt == graph.end())
            {
                //std::cout << "Creating node for: " << projDep.dependency << std::endl;
               dep = new Node(projDep.dependency); 
               graph.push_back(dep);
            }
            else
            {
                dep = *depIt;
            }
        }
      
        // creates or finds node for proj 
        auto sameNodeValueProj = [projDep](Node *n) {
            return n->value == projDep.project;
        };
        auto projIt = std::find_if(graph.begin(), graph.end(), sameNodeValueProj);
        if (projIt == graph.end())
        {
            //std::cout << "creating node for: " << projDep.project << std::endl;
            proj = new Node(projDep.project);
            graph.push_back(proj);
        }
        else
        {
            proj = *projIt;
        }

        // link the proj to dependency
        if (dep)
        {
            //std::cout << "Adding dependency: " << dep->value << " to : " << proj->value << std::endl;
            proj->nodes.push_back(dep);
        }
   }

    // add projects with no dependencies to build order
    // otherwise add to remaining list
    for (Node *node : graph)
    {
        std::cout << "Graph entry: " << node->value << " -> ";
        std::for_each(node->nodes.begin(), node->nodes.end(), [](Node *n) { std::cout << n->value << " "; });
        std::cout << std::endl;
        if (node->nodes.empty())
        {
           bo.push_back(node->value);
        }
        else
        {
            remaining.push_back(node);
        }
    }

    int success = true;
    while (!remaining.empty())
    {
        std::cout << "Starting new chain" << std::endl;
        Node *node = remaining.front();
        std::vector<int> chain;
        chain.push_back(node->value);
        success = build_order_node(node, bo, remaining, chain);
        if (!success) 
        {
            std::cout << "Failed to generate build order" << std::endl;
            return std::vector<int>();
        }
    }

    std::cout << "Returning build order: ";
    auto printVec = [](int val) { std::cout << val << " "; };
    std::for_each(bo.begin(), bo.end(), printVec);
    std::cout << std::endl;
    return bo;

}
