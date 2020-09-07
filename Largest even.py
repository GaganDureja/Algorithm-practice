#Link: https://edabit.com/challenge/ksZrMdraPqHjvbaE6


def largest_even(lst):	
	try:
		m = min(x for x in lst if x%2==0)
	except ValueError:
		return -1
	res = [m]
	for x in lst:
		if x%2==0 and x>res[-1]:
			res.append(x)
	return res[-1]
	





print(largest_even([3,2, 7, 1, 7, 9, 13]))