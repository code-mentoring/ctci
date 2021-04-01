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


/* Create an linked list with a specified tail node. */
function buildLinkedListWithTail(arr, tail) {
	const myNode = new Node(arr.shift(), null);
	let i = myNode;
	for (val of arr) {
		i.next = new Node(val, null);
		i = i.next;
	};
	i.next = tail;
	return myNode;
};


/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
const getIntersectionNode = function(headA, headB) {
  // Solution with O(n) time complexity and O(n) space complexity.
  if (headA == null || headB == null) {
      return null;
  };

  if (headA == headB) {
      return headA;
  };

  // Unpack both nodes into an array, in reverse.
  let arrA = [];
  for (let i = headA; i != null; i = i.next) {
      arrA.unshift(i);
  };
  let arrB = [];
  for (let j = headB; j != null; j = j.next) {
      arrB.unshift(j);
  };

  // If the last node doesn't match, there's no intersection.
  if (arrA[0] != arrB[0]) {
      return null;
  };

  // Iterate the arrays until we find a node that doesn't match.
  let k = 0;
  while (arrA[k] == arrB[k]) {
      k++;
  };
  // Return the node before the one that didn't match.
  return arrA[(k-1)];
};


const tail = buildLinkedList([5, 8, 1, 2])
const headOne = buildLinkedListWithTail([8, 1, 2], tail)
const headTwo = buildLinkedListWithTail([42, 42, 42], tail)
const headThree = buildLinkedListWithTail([42, 42, 42, 42, 42, 42, 42, 42], tail)
const noMatch = buildLinkedList([5, 8, 1, 2]);

console.log(getIntersectionNode(headOne, headTwo));
console.log(getIntersectionNode(headOne, headOne));
console.log(getIntersectionNode(headOne, null));
console.log(getIntersectionNode(headOne, headThree));
console.log(getIntersectionNode(tail, noMatch));
