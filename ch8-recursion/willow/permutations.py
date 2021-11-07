def add_char(c, perms):
	"""
	Given a character and a list of permutations,
	return a list of the permutations available by adding that character.
	"""
	new_perms = []
	for p in perms:
		# Add to front
		new_perms.append(c + p)
		for i, d in enumerate(p):
			# Add at every index
			new_perms.append(p[i:] + c + p[:i])
	return new_perms


def permutations_no_dups(s, i=0, perms=None):
	if perms is None:
		"""Initialize """
		perms = [s[0]]
	else:
		perms = add_char(s[i], perms)

	if i == len(s) - 1:
		return perms

	return permutations_no_dups(s, i + 1, perms=perms)


def permutations_with_dups(s, i=0, perms=None, seen=None):
	if perms is None:
		"""Initialize"""
		perms = [ s[0] ]
		seen = { s[0] }

	if s[i] not in seen:
		perms = add_char(s[i], perms)
		seen.add(s[i])

	if i == len(s) - 1:
		return perms

	return permutations_with_dups(s, i + 1, perms=perms, seen=seen)
