/**
 * Just a little helper to keep track of the steps we took.
*/
function updateJourney(journey, towers){
	journey.push(JSON.stringify(towers))
}

/**
 * Solve Towers of Hanoi for a starting stack of height N.
 * this function just sets up for the initial call to `moveStack`
 *
 * @return an array of strings representing all of the steps in the process.
*/
export default function towersOfHanoi(n) {
	if (n == 0) {
		return [[],[],[]]
	}
	const journey = []
	const towers = [[], [], []]

	for (let i = n - 1; i >= 0; i --) {
		towers[0].push(i)
	}
	updateJourney(journey, towers);

	moveStack(0,2,1,0,towers,journey);

	return journey;
}

/**
 * Move a portion of a stack from one stack to the other.
 *
 * @param source - the stack to move disks away from
 * @param dest - the stack to move to
 * @param inter - the stack to use as in intermediary
 * @param startIndex - the index marking the beginning of the segment of the stack to move.
 *			for example, if the stack was [3,2,1], passing `startIndex = 1`
 *			would imply you wanted to move the 1 and 2, but not the 3
 * @params towers and journey - the current state of the towers and journey.
*/
function moveStack(source, dest, inter, startIndex, towers, journey) {
	if (startIndex === towers[source].length - 1) {
		// This implies that we're trying to move the "top" element (ie the end of the stack).
		// It's interesting that we don't actually need to use `startIndex` in this block.
		// `startIndex` is really just controlling the recursion!
		towers[dest].push(towers[source].pop())
		updateJourney(journey, towers);
		return towers;
	}

	// Since the above did not trigger, we know the stack we are trying to move has more than 1 element.

	// Save the length of `inter` so we know how many to target in the 3rd recursive call.
	// Need to initialize this here because it will be mutated in the first 2 recursive calls.
	const inTheWay = towers[inter].length

	// Move all but the bottom element to `inter`.
	moveStack(source,inter,dest,startIndex + 1,towers,journey)
	// Move the bottom element to `dest`.
	// This doesn't really need a recursive call, but it doesn't make much difference.
	moveStack(source,dest,inter,startIndex,towers,journey)
	// Move everything we put in `inter` to `dest`.
	// Note the use of `inTheWay` as the startIndex.
	moveStack(inter,dest,source,inTheWay,towers,journey)
	return towers;
}

console.log(towersOfHanoi(3))
