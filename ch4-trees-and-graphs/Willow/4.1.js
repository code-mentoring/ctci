function RouteBetweenNodes(g, n1, n2) {
  function helper(g, n1, n2, departurePoint) {
    if (g[n1].indexOf(n2) !== -1 || g[n2].indexOf(n1) !== -1) {
      return true;
    }
    return g[n1].some((neighb) => {
      if (neighb !== n1 && neighb !== departurePoint) {
        if (helper(g, neighb, n2, n1)) {
          return true;
        }
      }
    })
    || g[n2].some((neighb2) => {
      if (neighb2 !== n2 && neighb2 !== departurePoint) {
        if (helper(g, n1, neighb2, n2)) {
          return true;
        }
      }
    });
  }
  return helper(g, n1, n2);
}

const graph = {
  a: ['a', 'b'],
  b: ['c'],
  c: ['d'],
  d: ['b', 'c']
}

const graph2 = {
  a: ['a', 'b'],
  b: [],
  c: [],
  d: ['b', 'c']
}

const graph3 = {
  a: ['a'],
  b: [],
  c: [],
  d: ['b', 'c']
}

const graph4 = {
  a: [],
  b: ['a'],
  c: ['d'],
  d: ['b', 'c']
}

const graph5 = {
  a: ['a'],
  b: ['a'],
  c: ['e'],
  d: ['c'],
  e: ['c', 'b'],
}

console.log(RouteBetweenNodes(graph, 'a', 'd'));
console.log(RouteBetweenNodes(graph2, 'a', 'd'));
console.log(RouteBetweenNodes(graph3, 'a', 'd'));
console.log(RouteBetweenNodes(graph4, 'a', 'd'));
console.log(RouteBetweenNodes(graph5, 'a', 'd'));
