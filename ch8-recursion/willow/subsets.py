def subsets(s, arr=None):
	if arr is None:
		arr=[]
	if len(s) == 0:
		return arr

	new_subsets = []
	for sbst in arr:
		new_subsets.append(sbst + [s[0]])

	arr += new_subsets
	arr.append([s[0]])
	return subsets(s[1:], arr)


def subsets_not_unique(s, arr=None, seen=None):
	if arr is None:
		arr=[]
		seen={}

	if len(s) == 0:
		return arr

	if s[0] in seen:
		return subsets_not_unique(s[1:], arr, seen)

	new_subsets = []
	for sbst in arr:
		new_subsets.append(sbst + [s[0]])

	arr += new_subsets
	arr.append([s[0]])
	seen[s[0]] = True

	return subsets_not_unique(s[1:], arr, seen)
