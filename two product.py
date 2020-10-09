#Link:  https://edabit.com/challenge/6cj6i2DACHTbtNnCD



def two_product(lst, n):
	for x in lst:
		if n%x==0 and n//x in lst:
			return sorted([x,n//x])







print(two_product([1, 2, 3, 4, 13, 5], 39))