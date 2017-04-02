#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import math

def is_palindrome(val):
	s = str(val)
	first = s[0:math.ceil(len(s)/2)]
	second = s[math.floor(len(s)/2):]
#	print(first)
#	print(second)
	if first == second[::-1]:
		return True
	else:
		return False

#ps = {}
ps = []
for i in range(1000, 1, -1):
	for j in range(1000, 1, -1):
		if is_palindrome(i*j):
			found = False
			for p in ps:
				if p >= i*j:
					found = True
			if not found:
				#ps[(i,j)] = i*j
				ps.append(i*j)
				print("%s*%s = %s" %(i,j,i*j))

print(ps)
#print(is_palindrome(1001))