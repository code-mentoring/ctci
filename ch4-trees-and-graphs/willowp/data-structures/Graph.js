const Queue = require('./Queue')

class Graph {
  constructor(directed = true) {
    this.directed = directed;
    this.adjList = {};
  }
  addVertex(id, data = null) {
    if (this.adjList[id] !== undefined) {
      throw new Error(`vertex ${id} already exists`);
    }
    this.adjList[id] = {};
    this.adjList[id].id = id;
    this.adjList[id].adjacent = [];
    this.adjList[id].data = data;
  }
  addEdge(srcId, destId) {
    this.adjList[srcId].adjacent.push(destId);
    if (!this.directed) {
      this.adjList[destId].adjacent.push(srcId);
    }
  }
  dfs(
    rootId,
    callback,
    visited = {},
  ) {
    const root = this.adjList[rootId];
    if (callback(root) === true) {
      return true;
    }
    const visitedMap = {
      ...visited,
      [rootId]: true,
    };
    return root.adjacent.some((adj) => {
      if (visitedMap[adj] === undefined) {
        return this.dfs(adj, callback, visitedMap)
      }
      return false;
    });
  }
  bfs(srcId, destId) {
    const queue = new Queue();
    const visitedMap = { [srcId]: true };
    queue.enqueue(this.adjList[srcId]);
    while (!queue.isEmpty()) {
      const current = queue.dequeue();
      if (current.id === destId) {
        return true;
      }
      current.adjacent.forEach((adj) => {
        if (visitedMap[adj] === undefined) {
          visitedMap[adj] = true;
          queue.enqueue(this.adjList[adj]);
        }
      });
    }
    return false;
  }
}

module.exports = Graph;
