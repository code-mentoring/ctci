/* Create a node in a linked list. */
class Node {
	constructor(val, next) {
		this.val = val;
		this.next = next; // Node or null
	};
};

/* Create an linked list from an array. */
function buildLinkedList(arr) {
	const myNode = new Node(arr.shift(), null);
	let i = myNode;
	for (val of arr) {
		i.next = new Node(val, null);
		i = i.next;
	};
	return myNode;
};

/* Create an array representing a reversed linked list. */
function buildReverseArr(head) {
	let arr = [];
	let i = head;
	while (i != null) {
		arr.unshift(i.val);
		i = i.next;
	}
	return arr;
};

function intersection(h1, h2) {
	// Reverse the arrays because it's easier to iterate forwards in JS.
	const arr1 = buildReverseArr(h1);
	const arr2 = buildReverseArr(h2);

	// Count how many matching values there are from the end of the array.
	let i = 0;
	while (arr1[i] == arr2[i]) {
		i ++;
	};
	// Number of nodes that need to be skipped.
	const h1HeadLength = arr1.length - i;
	let ans = h1
	for (let j = 0; true; j++) {
		if (j == h1HeadLength) {
			return ans;
		};
		ans = ans.next;
	};
};

const nodular = buildLinkedList([1, 2, 3, 5, 8, 1, 2]);
const nodulus = buildLinkedList([7, 5, 5, 5, 8, 1, 2]);
const shorty = buildLinkedList([8, 1, 2]);
const nothingness = buildLinkedList([]);
const realChallenge = buildLinkedList([1, 2, 3, 5, 8]);
const realChallengeTheSecond = buildLinkedList([8, 8, 1, 2, 8, 1, 2, 8, 1, 2]);

console.log(intersection(nodular, nodulus));
console.log("Should look like:")
console.log(buildLinkedList([5, 8, 1, 2]));
console.log(intersection(nodular, shorty));
console.log("Should look like:")
console.log(buildLinkedList([8, 1, 2]));
console.log(intersection(nodular, nothingness));
console.log("Should look like:")
console.log(null);
console.log(intersection(nodular, realChallenge));
console.log("Should look like:")
console.log(null);
console.log(intersection(nodular, realChallengeTheSecond));
console.log("Should look like:")
console.log(buildLinkedList([8, 1, 2]));
