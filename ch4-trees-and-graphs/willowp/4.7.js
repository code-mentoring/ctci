const { Graph } = require('./data-structures');

function buildOrder(projects, dependencies) {
  const answer = [];
  const graph = new Graph();
  projects.forEach((p) => {
    graph.addVertex(p, { numDeps: 0 });
  });
  dependencies.forEach((d) => {
    const [child, parent] = d;
    graph.addEdge(d[1], d[0]);
    graph.adjList[d[0]].data.numDeps += 1;
  });
  projects.forEach((p) => {
    if (graph.adjList[p].data.numDeps === 0) {
      answer.push(p);
    }
  });
  let current = 0;
  while (answer.length < projects.length) {
    if (current === answer.length) {
      return -1;
    }
    graph.adjList[answer[current]].adjacent.forEach((child) => {
      graph.adjList[child].data.numDeps -= 1;
      if (graph.adjList[child].data.numDeps === 0) {
        answer.push(child);
      }
    });
    current += 1;
  }
  return answer;
}

console.log(buildOrder(
  ['a', 'b', 'c', 'd', 'e', 'f'],
  [['d', 'a'], ['b', 'f'], ['d', 'b'], ['a', 'f'], ['c', 'd']],
), '= [{f, e}, {a, b}, d, c]');

console.log(buildOrder(
  ['a', 'b', 'c', 'd', 'e'],
  [['b', 'a'], ['c', 'b'], ['d', 'c'], ['e', 'd'], ['b', 'e']],
), '= -1');

console.log(buildOrder(
  ['a', 'b', 'c', 'd'],
  [['b', 'a'], ['b', 'c'], ['c', 'a'], ['d', 'b']],
), '= [a, c, b, d]');

console.log(buildOrder(
  ['a', 'b', 'c', 'd'],
  [['b', 'a'], ['b', 'c'], ['c', 'a'], ['d', 'b'], ['a', 'd']],
), '= -1');

console.log(buildOrder(
  ['a', 'b', 'c', 'd', 'e'],
  [['d', 'a'], ['d', 'c'], ['d', 'b'], ['e', 'd']],
), '= [{a, c, b}, d, e]');

console.log(buildOrder(
  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
  [['d', 'a'], ['d', 'c'], ['d', 'b'], ['e', 'd'], ['a', 'h'], ['i', 'f'], ['h', 'f']],
), '= [{f, c, b, g},{h, i}, {d, a}, e]');

console.log(buildOrder(
  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
  [['e', 'a'], ['e', 'b'], ['a', 'b'], ['a', 'c'], ['c', 'f'], ['b', 'f'], ['g', 'd']],
), '= [{f, d}, {g?, c, b}, {a, g?}, {e, g?}]');

console.log(buildOrder(
  ['a', 'b', 'c', 'f', 'd', 'e', 'g'],
  [['e', 'a'], ['e', 'b'], ['a', 'b'], ['a', 'c'], ['c', 'f'], ['b', 'f'], ['g', 'd']],
), '= [{f, d}, {g?, c, b}, {a, g?}, {e, g?}]');