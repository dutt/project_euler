#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_div(val):
	#print("testing %s" % val)
	for i in range(1, 21):
		if val % i != 0:
			#print("not cleanly divisible by %s" % i)
			return False
	return True

val = 5
while True:
	if is_div(val):
		print(val)
		break
	else:
		val += 1
