# Program to run three different prime number generating algorithms

import numpy as np
import time


def listprimes01(n):
	"""
	This is the generalised method to find the prime numbers upto n.
	"""
	
	primes = [2]
	
	for num in range(3, n, 2):
		
		isPrime = True
		lim = (num + 1) // 2
		# lim = int(np.sqrt(n))
		
		for factor in range(3, lim, 2):
			
			if (num % factor == 0):
				isPrime = False
				break
		
		if (isPrime):
			# print(f"number = {num}, prime = {isPrime}")
			primes.append(num)
	
	return primes


def pascal_coeff(p):
	"""
	This is the function to generate the pascal triangle coefficients for the crude AKS method.
	"""
	
	coeff = 1
	vals = [coeff]
	for j in range(1, p, 1):
		coeff = coeff * (p - j) // j
		vals.append(coeff)
	return vals


def listprimes02(n):
	"""
	This is the function to list prime numbers using a crude implementation of AKS primality test.
	"""
	
	primes = [2]
	for num in range(3, n, 2):
		isPrime = True
		coeffs = pascal_coeff(num + 1)[1:-1]
		
		for coeff in coeffs:
			if (coeff % num != 0):
				isPrime = False
				break
		
		if (isPrime):
			primes.append(num)
	
	return primes


def listprimes03(n):
	"""
	This is the function to list prime numbers using Sieve of Eratosthenes.

	https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
	"""
	
	prime = [True for i in range(n + 1)]
	p = 2
	
	primes = []
	
	while (p * p <= n + 1):
		if prime[p]:
			for i in range(p * p, n + 1, p):
				prime[i] = False
		
		p += 1
	
	for p in range(2, n + 1):
		if prime[p]:
			primes.append(p)
	
	return primes


# max number of primes
n = 5000

start1 = time.time()
primes1 = listprimes01(n)
end1 = time.time()

start2 = time.time()
primes2 = listprimes02(n)
end2 = time.time()

start3 = time.time()
primes3 = listprimes03(n)
end3 = time.time()

p1 = np.array(primes1)
p2 = np.array(primes2)
p3 = np.array(primes3)
print(np.allclose(p1, p2))
print(np.allclose(p1, p3))

# print(p1)
# print(p3)

print(f"Generic method took {end1 - start1} second(s)")
print(f"while pascal aks implementation took {end2 - start2} second(s)")
print(f"While Sieve of Erathones method took {end3 - start3} second(s)")

