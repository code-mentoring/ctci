def magic(arr, i=0):

	if arr[i] == i:
		return i

	if i == len(arr) - 1 or arr[i] > len(arr) - 1:
		return None

	return magic(arr, max(arr[i], i + 1))
