# Given an array of integers, find the first missing positive integer in linear time and constant space. 
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.










def missing_integer(lst):
	for x in range(1,max(lst)+2):
		if x not in lst:
			return x
		
	







print(missing_integer([3,4,-1,1]))

print(missing_integer([1,2,0]))

print(missing_integer([3,3,-1,1]))
