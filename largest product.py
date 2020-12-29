# This problem was asked by Facebook.

# Given a list of integers, return the largest product that can be
# made by multiplying any three integers.

# For example, if the list is [-10, -10, 5, 2], we should return 500,
# since that's -10 * -10 * 5.









from itertools import combinations as cb

def product(lst):
	res = 1
	for x in lst:
		res*=x
	return res


def largest_product(lst):
	return max(product(x) for x in cb(lst,3))









print(largest_product([-10,-10,5,2]))