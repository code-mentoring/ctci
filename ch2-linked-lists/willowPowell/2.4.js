class Node {
	constructor(val, next) {
		this.val = val;
		this.next = next;
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
	let left = null;
	let right = null;
	let i = head;

	while (i != null) {
		if (i && i.val < x) {
			if (!leftHead) {
				leftHead = i;
				left = i;
				i = left.next;
			} else {
				left.next = i;
				left = left.next;
				i = left.next;
			};
		};

		if (i && i.val >= x) {
			if (!rightHead) {
				rightHead = i;
				right = i;
				i = right.next;
			} else {
				right.next = i;
				right = right.next;
				i = right.next;
			};
		};
	};

	if (!leftHead) {
		return rightHead;
	} else {
		left.next = rightHead;
		return leftHead;
	};
};

const nodular = buildLinkedList([1, 2, 3, 5, 8, 1, 2]);

console.log(partition(nodular, 5));
