# This problem was asked by Facebook.

# Given a multiset of integers, return whether it can be partitioned into
# two subsets whose sums are the same.

# For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would
# return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35},
# which both add up to 55.

# Given the multiset {15, 5, 20, 10, 35}, it would return false, since we
# can't split it up into two subsets that add up to the same sum.








from itertools import combinations as cb
def equal_multiset(lst):
	half = sum(lst)//2
	for x in range(1,len(lst)):
		for y in cb(lst,x):
			if half==sum(y):
		 		return True
		
	return False
		




print(equal_multiset([15, 5, 20, 10, 35, 15, 10]))
print(equal_multiset([15, 5, 20, 10, 35]))