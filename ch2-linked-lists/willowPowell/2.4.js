class Node {
	constructor(val, next) {
		this.val = val;
		this.next = next; // Node or null
	};
};

function buildLinkedList(arr) {
	const myNode = new Node(arr.shift(), null);
	let i = myNode;
	for (val of arr) {
		i.next = new Node(val, null);
		i = i.next;
	};
	return myNode;
};

function partition(head, x) {
	let leftHead = null;
	let rightHead = null;
	let left = null; // most recent left node
	let right = null; // most recent right node
	let i = head; // currently being assessed node

	while (i != null) {
		if (i.val < x) {
			if (rightHead == null) {
				leftHead = i;
				left = i;
				i = left.next;
			} else {
				left.next = i; // this is where the list "breaks"
				left = left.next;
				i = left.next;
			};
		};

		if (i && i.val >= x) {
			if (rightHead == null) {
				rightHead = i;
				right = i;
				i = right.next;
			} else {
				right.next = i; // this is where the list "breaks"
				right = right.next;
				i = right.next;
			};
		};
	};

	if (leftHead == null) {
		return rightHead;
	} else {
		left.next = rightHead;
		return leftHead;
	};
};

const nodular = buildLinkedList([1, 2, 3, 5, 8, 1, 2]);

console.log(partition(nodular, 5));
