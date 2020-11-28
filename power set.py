# The power set of a set is the set of all its subsets. Write a function
# that, given a set, generates its power set.

# For example, given the set {1, 2, 3}, it should return {{}, {1}, {2},
# {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}



from itertools import combinations as cb
def power_set(lst):
	return sum([[list(x) for x in cb(lst,y)] for y in range(len(lst)+1)],[])





print(power_set([1,2,3]))