def subsets(s, arr=[]):
	if len(s) == 0:
		return arr

	new_subsets = []
	for sbst in arr:
		new_subsets.append(sbst + [s[0]])

	arr += new_subsets
	arr.append([s[0]])
	return subsets(s[1:], arr)
