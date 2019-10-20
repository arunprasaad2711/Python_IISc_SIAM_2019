import sys

def factorial(n):
	
	'''
	
	n = 4
	
	fact = 1
	
	range(2, n+1) = 2, 3, 4
	
	iteration 1:
	
	i = 2
	
	fact = fact * i
		 = 1 * 2
		 = 2
	
	iteration 2:
	
	i = 3
	fact = 2
	
	fact = fact * i
		 = 2 * 3
		 = 6
	
	iteration 3:
	
	i = 4
	fact = 6
	
	fact = fact * i
		 = 6 * 4
		 = 24
	'''
	
	
	fact = 1
	# checks if the variable is an integer or not
	if isinstance(n, int) and n >= 0:
		
		if n is (0 or 1):
			return fact
		else:
			for i in range(2, n+1):
				fact *= i
			return fact
	else:
		return 0


def pascal_row(row_num):
	
	row_vals = []
	if (isinstance(row_num, int) and row_num > 0):
		for i in range(0, row_num):
			
			num = factorial(row_num - 1)
			den = factorial(row_num - 1 - i) * factorial(i)
			nck = num // den
			
			row_vals.append(nck)
	
	return row_vals

def pascal_tri(nrows):

	for i in range(1, nrows+1):
		print(pascal_row(i))

pascal_tri(5)

f = factorial(100000)

print(((f.bit_length() + 7) // 8) // 1024)