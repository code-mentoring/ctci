def rec_mult(a,b):
	if b == 0:
		return 0
	if b == 1:
		return a
	return a + rec_mult(a, b-1)


def rec_mult_bitwise(a,b):
	# Base cases for recursion
	if b == 0:
		return 0
	if b == 1:
		return a

	# Get the most significant bit and the power of two it represents
	msb = 1
	pwr_of_2 = 0
	while True:
		next_msb = msb << 1
		if next_msb > b:
			break
		pwr_of_2 += 1
		msb = next_msb
		if msb == b:
			break

	# To understand the return value, remember:
	# 1: Left shifting by the power of two is the same as multiplying by the number itself (ie x*16=x<<4)
	# 2: Once we've done that, we still need to multiply by the remainder, hence b - msb
	return (a << pwr_of_2) + rec_mult_bitwise(a, b - msb)
