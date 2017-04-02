#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

import json, math

primes = [2,3,5]

def setup_primes_div(maxval):
	global primes
	for i in range(max(primes), math.floor(math.sqrt(maxval))):
		found = False
		for p in primes:
			if i % p == 0:
				found = True
				break
		if not found:
			primes.append(i)
		
def factorialize(n):
	fs = []
	val = n
	for p in primes:
		while val % p == 0:
			val = val / p
			if not p in fs:
				fs.append(p)
	return fs

def main():
	setup_primes_div(600851475143)
	fs = factorialize(600851475143)
	print(max(fs))

if __name__ == '__main__':
	main()