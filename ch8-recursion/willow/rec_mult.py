def rec_mult(a,b):
	if b == 0:
		return 0
	if b == 1:
		return a
	return a + rec_mult(a, b-1)


def rec_mult_bitwise(a,b):
	# Solution works for negative and positive integers
	# but converts to positive for multiplication.
	negative_answer = (a < 0 and b > 0) or (a > 0 and b < 0)
	if a < 0:
		a = a * -1
	if b < 0:
		b = b * -1

	def inner(a,b):
		# Base cases for recursion
		if b == 0:
			return 0
		if b == 1:
			return a

		# Get Most Significant Bit of b
		# From https://math.stackexchange.com/questions/3028227/least-and-most-significant-bit-calculation-using-bitwise-operations
		x = b
		x|=(x>>1)
		x|=(x>>2)
		x|=(x>>4)
		x|=(x>>8)
		x|=(x>>16)
		x += 1
		msb = x >> 1

		# This gets the square root of a power of 2 (which we know the MSB is)
		sqrt_of_msb = 0
		i = 1
		while i < msb:
			i <<= 1
			sqrt_of_msb += 1

		# To understand the return value, remember:
		# 1: Left shifting by the square root of a power of 2 is the same as multiplying by that number (ie x*16=x<<4)
		# 2: Once we've done that, we still need to multiply by the remainder, hence b - msb
		return (a << sqrt_of_msb) + inner(a, b - msb)

	if negative_answer:
		return inner(a, b) * -1
	return inner(a, b)
