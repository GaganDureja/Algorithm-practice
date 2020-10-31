# You will be given an array of integers and a target value.
# Determine the number of pairs of array elements that have 
# a difference equal to a target value.

# For example, given an array of [1, 2, 3, 4] and a target 
# value of 1, we have three values meeting the condition:
# 2-1=1, 3-2=1 and 4-3=1.







from itertools import combinations
def pairs(k, arr):
	return len([x for x in combinations(arr,2) if abs(x[0]-x[1])==k])



print(pairs(2,[1,5,3,4,2]))