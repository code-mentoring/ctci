const { ChaosTree } = require('./data-structures');
const { rword } = require('rword');

const chaos = new ChaosTree(1);

chaos.insert(2);
chaos.insert(3);
chaos.insert(4);
chaos.insert(5);
chaos.insert(6);
chaos.insert(7);
chaos.insert(8);
chaos.insert(9);
chaos.insert(10);

console.log(JSON.stringify(chaos, null, 2));
console.log(chaos.getRandomNode());
console.log(chaos.delete());
console.log(chaos);
console.log(chaos.delete());
console.log(JSON.stringify(chaos, null, 2));

const chaos2 = ChaosTree.initiateChaos(6, rword.generate);
console.log(chaos2);

const chaos3 = ChaosTree.initiateChaos(6);
console.log(chaos3);
