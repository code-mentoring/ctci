def stairs(n):
	if n < 1:
		return 0
	memo = [None] * (n + 1)
	memo[0] = 1
	return _stairs(n, memo)

def _stairs(n, memo):
	if n < 0:
		return 0
	if memo[n]:
		return memo[n]
	memo[n] = _stairs(n-1, memo) + _stairs(n-2, memo) + _stairs(n-3, memo)
	return memo[n]
