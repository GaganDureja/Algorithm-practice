#Link:  https://edabit.com/challenge/yFEMocjdiRjPhoDqv



def prime_in_range(n1, n2):
	for x in range(n1, n2+1):
		for y in range(2,x):
			if x%y==0:
				break
		else:
			return True
	return False




print(prime_in_range(62,66))

print(prime_in_range(10,12))
